---
title: "？在正则表达式的应用"
date: 2019-08-01T11:12:25+08:00
draft: false
tags: ["Development", "javascript", "RegExp"]
categories: ["Development"]
---

{{% admonition example %}}
很多文章讲述正则是从元字符的认知到量词和基本匹配，再到零宽断言贪婪匹配这些高阶知识讲解的。本文另辟蹊径，只讲述问号的应用，从一个点剖析正则表达式的一些非全面覆盖的知识点。
{{% /admonition %}}


### 量词 quantifier

问号表示前面的字符为可选，也就是出现的次数是 0 或者 1 次。

```javascript
let str = `The car is parked in the garage.`;
let reg = /T?he/g;

str.match(reg) // ["The", "he"]
```


### 命名一个捕获组

使用 `?<>` 来命名一个捕获组，然后使用 `\k<>` 来在表达式中引用组：

```javascript
let str = "aaa123aaaaaa"
let reg = /(?<word>\w+)(\d+)\k<word>/g

str.match(reg) // ["aaa123aaa"]
```


需要注意捕获到的内容是 exactly the same 的，如果 `str="aaa123bbb"` 就跟表达式不匹配。所以我们可以用来处理引号的匹配来获取各语言里面的话语内容：

```javascript
let str = `He said: "She's the one!".`;
let reg = /(?<quote>['"])(.*?)\k<quote>/g;

str.match(reg) // [""She's the one!""]
```



### 开启 lazy 模式

正则表达式默认采用贪婪匹配模式，在该模式下意味着会匹配尽可能长的子串。我们可以使用`?`将贪婪匹配模式转化为惰性匹配模式。



```javascript
let str = `The fat cat sat on the mat.`;
let reg = /(.*at)/g;

str.match(reg) // ["The fat cat sat on the mat"]

reg = /(.*?at)/g;
str.match(reg) // ["The fat", " cat", " sat", " on the mat"]
```



### 零宽断言

也叫前后预查(匹配)，用来判断要匹配的内容是否在另一个约束条件周围。匹配内容在前约束条件在后的叫先行断言（look ahead），反之则为后发断言（look behind）。两种约束又分为正（positive）和负（negative），用来表达包含和排除。


| 符号       | 描述        |
| ------------- |:---------------:| 	
| ?=	| 正先行断言-存在 |
| ?!	| 负先行断言-排除 |
| ?<=   | 正后发断言-存在 |
| ?<!	| 负后发断言-排除 |




分别举例：


```javascript

let str="1 人民币约等于 $7（$是美元符号）"
let reg = /\$/g
str.match(reg) // (2) ["$", "$"]

// 正先行
reg = /\$(?=\d+)/g
str.match(reg) // ["$"]

// 负先行
reg = /\$(?!\d+)/g
str.match(reg) // ["$"]

reg = /\d/g
str.match(reg) // (2) ["1", "7"]

// 正后发
reg = /(?<=\$)\d+/g
str.match(reg) // ["7"]

// 负后发
reg = /(?<!\$)\d+/g
str.match(reg) // ["1"]
```



需要注意的是别看这也是被括号包围的形式，但约束条件却是非捕获的，需要捕获得再包围一个括号。


```javascript

let str = "1 人民币约等于 $7"
let reg = /(?<=(\$))\d+/;
str.match(reg) // (2) ["7", "$", index: 10, input: "1 人民币约等于 $7", groups: undefined]
```



可以观察到即使断言组在前，结果 `$` 仍出现在 `7` 之后。先行断言也一样，匹配内容先出现。




### 忽略捕获组

使用 `(?:)` 来将后缀的匹配设为非捕获的组，我们也就无法使用 `$` 跟数字的形式来引用这个组。

```javascript
let str = "123aaabbb"
let reg = /(\d+)(.*)/g

reg.test(str) // true
RegExp.$1 // "123"
RegExp.$2 // "aaabbb"

reg = /(\d+)(?:.*)/g
reg.test(str) // true
RegExp.$1 // "123"
RegExp.$2 // ""
```

### 结语
以上就是我对正则中问号的总结，希望对您有所帮助！
