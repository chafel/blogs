---
title: "JavaScript 事件循环：微任务和宏任务"
date: 2019-08-12T23:02:15+08:00
draft: false
tags: ["Development", "javascript"]
categories: ["Development"]
---


# 事件循环：微任务和宏任务

JavaScript 在浏览器里的执行流程跟在 Node.js 中一样，是基于**事件循环**的。

理解事件循环如何运行对于代码优化是重要的，有时对于正确的架构也很重要。

在本掌中我们首先覆盖关于这个事情是如何运作的理论细节，然后看看这个知识的实际应用。

## 事件循环

**事件循环**的概念非常简单。它是一个在 JavaScript 引擎等待任务、执行任务和休眠等待更多任务这几个状态之间的无穷无尽的循环。

执行引擎通用的算法：

1. 当有任务时：
    - 从最先进入的任务开始执行
2. 休眠到有新的任务进入，然后到第 1 步

当我们浏览一个网页时就是上述这种形式。JavaScript 引擎大多数时候什么也不做，只在一个脚本、处理函数或者事件被激活时运行。

任务举例：

- 当外部脚本 `<script src="...">` 加载进来时，任务就是执行它。
- 当用户移动鼠标时，任务就是派发出 `mousemove` 事件和执行处理函数。
- 当定时器 `setTimeout` 到期时，任务就是运行其回调。
- ……诸如此类。

任务队列就是一个集合，引擎来处理它们，然后等待更多的任务（即休眠，几乎不消耗 CPU 资源）。

一个任务到来时引擎可能正处于运行状态，那么这个任务就被入队。

多个任务组成了一个队列，命名为“宏任务队列”（v8 术语）：

![Event Loop](https://zh.javascript.info/article/event-loop/eventLoop.svg)


例如，当引擎忙于执行一段 `script` 时，还可能有用户移动鼠标产生了 `mousemove` 事件，`setTimeout` 或许也刚好到期等这些事件，这些任务组成一个队列，如上图所示。

队列里的任务执行基于“先进先出”原则。当浏览器引擎执行完 `script`，然后来处理 `mousemove` 事件，然后再执行 `setTimeout`  的执行函数，诸如此类。

到目前为止很简单，是吧？

两个更细节的点：
1. 当引擎处理任务时不会执行渲染。如果执行需要很长一段时间也是如此。对于 DOM 的修改只有当任务执行完成才会被绘制。
2. 如果一个任务执行时间过长，浏览器无法处理其他任务，在一定时间后就会在整个页面抛出一个如“页面未响应”的警示建议终止这个任务。这样的场景经常发生在很多复杂计算或者程序错误执行到死循环里。

这样我们有了一个理论，接下来我们来应用所学到的知识。

## 用例 1：拆分 CPU 耗费型任务

假如我们有一个 CPU 耗费型任务。

例如，语法高亮（用来给本示例页面代码上色）是相当繁重的 CPU 任务。为了高亮代码，它执行分析，创造了很多上色后的元素，并把它们添加到页面文档中，这样长文本就会消耗很多的时间。

当引擎忙于语法高亮时，它就无法处理其他 DOM 相关的事情，执行用户的事件等。这样或许会导致浏览器“中断”甚至是“挂起”一段时间，这没法接受。

我们可以拆分大任务为小片任务来规避问题。高亮前 100 行，然后设定`setTimeout`（延时参数为 0）来高亮另外的 100 行，以此类推。

为了演示此方法，从简洁性上考虑，我们用从 `1` 数到 `1000000000` 的函数来代替语法高亮。

如果你运行如下代码，引擎会"挂起"一段时间。对于服务端 JS 这会显而易见，当运行在浏览器上，尝试点击页面上其他按钮时，你会注意到没有任何其他的事件被执行知道数数函数执行完成。

```js run
let i = 0;

let start = Date.now();

function count() {

  // 执行了一些繁重的任务
  for (let j = 0; j < 1e9; j++) {
    i++;
  }

  alert("Done in " + (Date.now() - start) + 'ms');
}

count();

```

浏览器甚至可能会出现“脚本执行时间过长”的警告。

让我们用嵌套的 `setTimeout` 拆分这个任务：

```js run
let i = 0;

let start = Date.now();

function count() {

  // 做一个繁重工作的一部分 (*)
  do {
    i++;
  } while (i % 1e6 != 0);

  if (i == 1e9) {
    alert("Done in " + (Date.now() - start) + 'ms');
  } else {
    setTimeout(count); // 计划新的调用 (**)
  }

}

count();

```

现在浏览器界面在数数执行过程中是完全可用的。

单次运行 `count` 做了一部分工作 `(*)`，然后如果必要的话，重新计划自身的执行 `(**)`：

1. 首先运行数数：`i=1...1000000`。
2. 然后运行数数：`i=1000001..2000000`。
3. 以此类推。

现在，如果一个任务（例如 `onclick` 事件）在引擎忙着执行第一步的时候同时发生，它就会入队然后在第一步执行完成后且第二步之前执行。周期性地在 `count` 的执行返回到事件循环，为 JavaScript 引擎提供了足够的 “空间” 来做别的事情，比如对用户的行为作出反应。

需要关注的是两者变体 —— 有和没有用 `setTimeout` 拆分任务 —— 在执行速度上是相当的。在执行数数的总耗时是没有多少差异的。

为了使两者耗时更接近，我们来做一个改进。

我们把定时任务放在 `count()` 的一开始：

```js run
let i = 0;

let start = Date.now();

function count() {

  // 移动定时任务到开始处
  if (i < 1e9 - 1e6) {
    setTimeout(count); // 定时发起新的调用
  }

  do {
    i++;
  } while (i % 1e6 != 0);

  if (i == 1e9) {
    alert("Done in " + (Date.now() - start) + 'ms');
  }

}

count();

```

现在我们开始调用 `count()`，在发现我们还将需要调用 `count()` 时，就在做具体的任务之前立即定时。

如果你运行它，会注意到耗时明显减少。

为什么？

很简单：你应该还记得，浏览器执行多个嵌套的 `setTimeout` 调用最小延时 4ms。即使设置了 `0` 还是 `4ms`（或者更久一些）。所以我们早一点定时，它就会运行地快一些。

最后，我们拆分 CPU 耗费型任务为几部分，现在它不会阻塞用户的界面了。 而且总耗时并不会多很多。

## 用例 2：进度指示器

另外一个给浏览器脚本拆分繁重任务的好处是我们可以展示进度指示器。

通常浏览器会在当前运行的代码完成后执行渲染。如果一个任务耗时很久也是这样。对 DOM 的修改只有在任务结束后才会被绘制。

从一方面讲，这非常好，因为我们的函数可能创造出很多的元素，把它们挨个地插入到文档中然后改变它们的样式 —— 页面访问者就不会看到任何的 “中间态”，也就是未完成的状态。很重要，对吧？

这是一个样例，`i` 的改变在函数结束前不会有变化，所以我们只会看到最后的值：

```html run
<div id="progress"></div>

<script>

  function count() {
    for (let i = 0; i < 1e6; i++) {
      i++;
      progress.innerHTML = i;
    }
  }

  count();
</script>

```

……但是我们可能会想要在执行任务期间展示一些东西，例如进度条。

如果我们用 `setTimeout` 拆分繁重任务为小片段，值的改变就会在它们之间被绘制。

这样看起来好多了：

```html run
<div id="progress"></div>

<script>
  let i = 0;

  function count() {

    // 执行一些繁重的工作 (*)
    do {
      i++;
      progress.innerHTML = i;
    } while (i % 1e3 != 0);

    if (i < 1e7) {
      setTimeout(count);
    }

  }

  count();
</script>
``` 

现在 `div` 展示了 `i` 的值的增长，跟进度条很类似了。

## 用例 3：在事件之后做一些事情

在事件处理中我们可能要延期一些行为的执行，直到事件冒泡完成并被所有层级接手和处理之后。我们可以把这部分代码放在 0 延迟的 `setTimeout`。

在 [生成自定义事件](https://zh.javascript.info/dispatch-events) 章节中，我们看到这样一个例子：自定义事件 `menu-open` 在 `setTimeout` 中被派发，所以它发生在“click”事件被完全处理后。

```js
menu.onclick = function() {
  // ...

  // 创建一个附带被点击菜单项数据的自定义事件
  let customEvent = new CustomEvent("menu-open", {
    bubbles: true
  });

  // 异步派发自定义事件
  setTimeout(() => menu.dispatchEvent(customEvent));
};
```

## 宏任务和微任务

伴随本章描述的**宏任务**还存在着**微任务**，在章节 [微任务](https://zh.javascript.info/microtask-queue) 有提及到。

微任务仅仅由我们的代码产生。它们通常由 promises 生成：对于 `.then/catch/finally` 的处理函数变成了一个微任务。微任务通常"隐藏在" `await` 下，因为它也是另一种处理 promise 的形式。

有一个特殊的函数 `queueMicrotask(func)`，可以将 `func` 加入到微任务队列来执行。

**在每个宏任务之后，引擎立即执行所有微任务队列中的任务，比任何其他的宏任务或者渲染或者其他事情都要优先。**

来看看例子：

```js run
setTimeout(() => alert("timeout"));

Promise.resolve()
  .then(() => alert("promise"));

alert("code");
```

这里的执行顺序是什么呢？

1. `code` 首先出现，因为它是常规的同步调用。
2. `promise` 第二个出现，因为 `then` 从微任务队列中来，在当前代码之后执行。
3. `timeout` 最后出现，因为它是一个宏任务。

更详细的事件循环图如下：

![full-event-loop](https://zh.javascript.info/article/event-loop/eventLoop-full.svg)

**所有的微任务在任何其他的事件处理或者渲染或者任何其他的宏任务发生之前完成调用。**

这非常重要，因为它保证了微任务中的程序运行环境基本一致（没有鼠标位置改变，没有新的网络返回数据，等等）。

如果我们想要异步执行（在当前代码之后）一个函数，但是要在修改被渲染或者新的事件被处理之前，我们可以用 `queueMicrotask` 来定时执行。

还是跟前面的类似的“数数型进度展示条”的例子，不同的是用 `queueMicrotask` 来代替 `setTimeout`。你可以看到它在最后才渲染。就像写的是同步代码：

```html run
<div id="progress"></div>

<script>
  let i = 0;

  function count() {

    // 执行一些繁重的工作 (*)
    do {
      i++;
      progress.innerHTML = i;
    } while (i % 1e3 != 0);

    if (i < 1e6) {
      queueMicrotask(count);
    }

  }

  count();
</script>
```

## 总结

更具体的事件循环的算法（尽管跟 [标准](https://html.spec.whatwg.org/multipage/webappapis.html#event-loop-processing-model) 相比是简化过的）：

1. 从**宏任务**队列出列并执行最前面的任务（比如“script”）。
2. 执行所有的**微任务**：
    - 当微任务队列非空时：
        - 出列并运行最前面的微任务。
3. 如有需要执行渲染。
4. 如果宏任务队列为空，休眠直到一个宏任务出现。
5. 到步骤 1 中。

计划一个新的**宏任务**：
- 使用 0 延时的 `setTimeout(f)`。

它被用来拆分一个计算耗费型任务为小片段，使浏览器可以对用户行为作出反馈和展示计算的进度。

也被用在事件处理函数中来定时执行一个行为，在当前事件被完全处理（冒泡结束）之后。

计划一个新的**微任务**：
- 使用 `queueMicrotask(f)`。
- promise 的处理函数也是进入到微任务队列。

在微任务中间没有 UI 或者网络事件的处理：它们一个接一个地立即执行。

所以我们可以用 `queueMicrotask` 来异步地执行函数，但是保持环境状态的一致。

```smart header="Web Workers"
为了繁重任务不至于阻塞事件循环，我们可以用 [Web Workers](https://html.spec.whatwg.org/multipage/workers.html)。

这是一个在平行线程中运行代码的办法。

Web Workers 可以跟主线程交换信息，但是它们可以有自己的变量和自己的事件循环。

Web Workers 无权访问 DOM，所以它们主要在计算上有用，用来使用多核 CPU 同时执行的能力。
```

{{% admonition tip 提示 %}}
本篇译自和首发于 [javascript.info](https://zh.javascript.info/event-loop) ，英文版质量不错，遂译为中文并贡献了 [PullRequest](https://github.com/javascript-tutorial/zh.javascript.info/pull/446)
{{% /admonition %}}