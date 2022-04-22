---
title: "理解 CSS 中的就近原则"
date: 2022-04-07T22:50:12+08:00
draft: false
tags: ["Development", "css"]
categories: ["Development"]
---
常见的一道面试题：

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>就近原则</title>
	<style type="text/css">
		.classA {
		    color: red;
		}
		.classB {
		    color: yellow;
		}
	</style>
</head>
<body>
	<div id="test" class="classB classA">文字会是什么颜色的呢？</div>
</body>
</html>
```

正确答案：根据就近原则，文字会展示为黄色。追问“为什么呢？”，很少有候选人能解释清楚。

常见的答案是“后面定义的会覆盖掉前面的样式”，但其实不然。

> The browser goes through each rule set in the CSS, creating a tree of nodes with parent, child, and sibling relationships based on the CSS selectors.
As with HTML, the browser needs to convert the received CSS rules into something it can work with. Hence, it repeats the HTML-to-object process, but for the CSS.
https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work

上文已经说清楚了，不会有覆盖发生，浏览器只是在尽可能地去构造 CSSOM。产生这种猜想的是将关键渲染路径中构造 CSSOM 的过程跟 DOM 构造过程同化了。

我们可以通过 [csstree](https://github.com/csstree/csstree) 来呈现 CSS 解析后的对象，跟浏览器中其实是一致的，因为都要遵循 [W3C 规范](https://www.w3.org/TR/WD-CSS2-971104/cover.html#toc) 。

```html
<script type="module">
  import * as csstree from 'https://cdn.jsdelivr.net/npm/css-tree';
    
  // parse CSS to AST 
  const ast = csstree.parse('p { color: red;} p {color: yellow;}');

  // generate CSS from AST
  console.log(csstree.toPlainObject(ast));
</script>
```

`p { color: red;} p {color: yellow;}` 的结果
{{<figure src="im1.png" width="300px" alt="result1">}}

`.classA { color: red;}.classB {color: yellow;}` 的结果
{{<figure src="im2.png" width="300px" alt="result2">}}

可以看到两个 p 不会产生合并为一个，而是两个声明，这个结果同样地可以在浏览器中通过 `document.styleSheets` 来看到：
{{<figure src="im3.png" width="500px" alt="result3">}}

所以并没有发生合并，但为什么渲染树生成后就变成了合并后的结果呢？因为 W3C 中 [对于级联的规定](https://www.w3.org/TR/WD-CSS2-971104/cascade.html) ，注意看第 5 条：

>Conflicting rules are intrinsic to the CSS mechanism. To find the value for an element/property combination, user agents must apply the following algorithm:
> 1. Find all declarations that apply to the element/property in question. Declarations apply if the associated selector matches the element in question. If no declarations apply, terminate the algorithm.
> 2. Sort the declarations by explicit weight: declarations marked '!important' carry more weight than unmarked (normal) declarations. See the section on 'important' rules for more information.
> 3. Sort by origin: the author's style sheets override the reader's style sheet which override the UA's default values. An imported style sheet has the same origin as the style sheet from which it is imported.
> 4. Sort by specificity of selector: more specific selectors will override more general ones. The definition and calculation of specificity is object-language dependent. Pseudo-elements and pseudo-classes are counted as normal elements and classes, respectively.
> 5. Sort by order specified: if two rules have the same weight, the latter specified wins. Rules in imported style sheets are considered to be before any rules in the style sheet itself.

那浏览器是怎么实现的呢？怎么在生成渲染树的时候将这个规则达成的呢？明明是在 DOM 中后声明的 classA 啊怎么没有覆盖前面的 classB 呢？
![renderPage.png](https://web-dev.imgix.net/image/C47gYyWYVMMhDmtYSLOWazuyePF2/b6Z2Gu6UD1x1imOu1tJV.png?auto=format&w=800)

可能的实现如下：
```javascript
// 步骤1 构造 CSSOM 
const cssom = {
	classA: {
  	color: 'red'
  },
  classB: {
  	color: 'yellow'
  }
}

// 步骤2 在构造 renderTree 时从 DOM 节点上找到 classList 再从 CSS tree(或者 map) 上获取到声明值
// 再计算出 computedStyle
const result = Object.keys(cssom).filter(x => ['classB', 'classA'].includes(x)).reduce((result, item) => {
 return {
   ...result,
   ...cssom[item]
 }
}, {})

// 结果：array + map = result 
console.log(result)
// VM101:17 {color: 'yellow'}
```

{{<figure src="chromium.jpeg" width="500px" alt="chromium">}}

注意以上发生在 Blink 的 style 内联过程在实际情况中必然更复杂，以上只是简化理解的伪代码，但理解到这里我们的问题再结合下面这几个推荐阅读就了然了：
1. https://medium.com/jspoint/how-the-browser-renders-a-web-page-dom-cssom-and-rendering-df10531c9969
2. https://developer.mozilla.org/en-US/docs/Web/Performance/How_browsers_work
3. https://web.dev/critical-rendering-path-render-tree-construction/
