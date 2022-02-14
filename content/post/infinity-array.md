---
title: "如何创建无穷数组"
date: 2019-05-02T20:13:14+08:00
draft: false
tags: ["Development", "javascript"]
categories: ["Development"]
---

{{% admonition example %}}
「无穷」意味着永恒

我们总是渴求永恒和永生

但宇宙之中万物皆缥缈

不存在一成不变的可能性

科学给我们的幻想打了个零分
{{% /admonition %}}

如何在 JavaScript 里产生一个无穷数组呢？这里对无穷的定义是，数组包含了 Infinite 边界之内的任意个元素。我们知道无穷对应的是有限，我们可以直接 new Array(length) 指定定长数组，但如何产生不定长的数组呢？

先来看有限状态机的特点：
- 状态总数（state）是有限的；
- 任一时刻，只处在一种状态之中；
- 某种条件下，会从一种状态转变（transition）到另一种状态。

我们只需要改变特点 1 ，让状态总数无穷即可。这里很容易看出使用生成器（Generator）可以生成无穷的状态。在 ES6 之前，我们可以用以下代码模拟：

```javascript
function InfiniteArray() {  
var i = 0;  
this.next = function() { return i++; };  
}  
var a = new InfiniteArray();  
a.next();  
a.next();  
```
我们每次调用 `a.next()` 作为下标给数组赋值即可生成无穷数组。ES6 之后我们代码可以改写了：
```javascript
function *numbers() {    let i = 0;    while(true) { yield i++ }}
```
👆生成器会一直改写状态，因为生成器也是迭代器，我们可以直接调用 `Array.from` 和 `...` 来迭代 `numbers`。

`[...numbers()]`真正意义上实现了无穷数组，但我们计算机的物理内存空间有限，直接这么做没有任何业务价值，只会导致 stack overflow。我们需要让状态机支持无限状态，但只在我们需要取状态时才迭代，实现受控下的无穷。按需产生长度，除了👆提到的下标手动赋值来控制外，可以先指定数组的长度，类似👇：
```javascript
Array.from({length: 5}, (v, i) => i);
// [0, 1, 2, 3, 4]
```
我们将无穷的生成器封装为接收固定长度即可:
```javascript
function take(length) {
   const numIterator = numbers();
   return Array.from({ length }, () => numIterator.next().value)
}
```

👆例子即可按需生成不固定长度的数组，仔细思考就会发现，我们创建了一个流（stream）。以现实举例，工厂的传送带不断运行，在理想情况相当于一个可以无限生成商品。我们把商品比作数组项，工人从传动带拿走商品装箱，也就是我们用 take 函数从无穷生成器取出几项。

传送带不断运行，围绕这个传送带建立了一条生产线，包括一系列工序，不同的工序承担单一而确定的职责。每个工位上有一个工人。

整个传送带的起点是原料箱，原料箱中的原料不断被放到传送带上。工人只需要待在自己的工位上，对面前的原料进行加工，然后放回传送带上或放到另一条传送带上即可，简单、高效、无意外 —— 符合程序员的审美。

而且这个生产线还非常先进 —— 不接单就不生产，非常有效地杜绝了浪费😄。

这就引出了 FRP（函数响应式编程），这种 Observable 的编程范式也就是程序等待外界的输入，并做出响应。流水线每个工位上的工人正是这种工作模式。更多介绍见👆引文。ReactiveX 是一组 FRP 库，RxJS 就是 ReactiveX 在 JavaScript 语言上的实现，显然我们可以用其实现无穷数组：

```javascript
import { interval } from 'rxjs';

const arr = new Array()
interval(1000)
   .pipe(take(4))
   .subscribe((x) => arr.push(x))
console.log(arr)
```
👆代码就产生了下图这样一个无尽流，产生了一个由所有自然数组成的每隔一秒生成一个数的流。流不会主动终止，但仍然是可以处理的，因为需要多少项是由消费者决定的。可以把这个“智能”传送带理解为由下一个工位“叫号”的，没“叫号”下一项数据就不会过来。

![interval marble diagram](https://pic1.zhimg.com/80/v2-0262d25ad4ca316709a3daf7149e6184_1440w.png)

以上三种方式分别用状态机和流的抽象实现了某种意义上的无穷数组，抛砖引玉，供各位在实际编码中参考。
