---
title: "认知迭代"
date: 2022-06-02T10:12:04+08:00
lastmod: 2022-06-02T18:19:52+08:00
keywords: ["认知迭代", "Cognitive Iteration"]
description: "认知迭代"
tags: ["认知迭代", "work"]
categories: ["认知迭代"]
draft: true
weight: 50
---

### 2023.03.30
两篇震撼的博客：
1. [重新理解Web](https://zhuanlan.zhihu.com/p/581977751) ：角度奇特，抽象接近于道的层面，但又从术的层面解释地很清楚，杨杨还是厉害！
2. [bicycle](https://ciechanow.ski/bicycle/)  : 读这篇真是一中享受，作者的可视化和 WebGL 功底深厚！


### 2023.03.24
骑车路上想到了一个观点：人脑是一种缓存。


### 2023.01.16
### 2023.01.16
### 2023.01.16

### 2023.01.16
**对外沟通**
这半年经历了多次的各方沟通，逐渐克服了最开始的恐惧和生硬，过程中跟学姐学到了很多，如通过一般闲聊逐渐深入到关注点；主要是听对方展开来获取信息，沟通时的氛围保持很关键，保持愉悦地对话可以促进对方不断展开来带出有效信息，也对沟通后的信息交流和有下次沟通的机会有帮助；不同信息有不同收集方式，可以通过事前对话了解背景信息，然后熟悉对方的文档后准备关键问题，通过预先练习来克服心理障碍；从对方的角度去理解其立场和思路，而不是总站在建设者的角度急于下结论和反驳，才能更好地回答对方的问题和有效沟通。

### 2022.12.09
**技术项目方案的设计：**

- 为什么做：首先立足于业务，从质量、效率和体验三个维度里面找出业务的痛点，针对用户特定需求出发来建设；
- 做什么：在特定维度里把当前问题的业界最佳解决方案列举出来，找到这些解决方案提供的功能集，然后选择与要解决业务现状匹配的功能点，基于公司成熟基建通过最小成本完成该功能；
- 怎么做：说明在特定时间周期达成的广度和深度上的里程碑，尽量消除实现过程的不确定性。

### 2022.11.11

**稳定性建设方法论**

跟组织能力建设（员工思维即愿不愿意、员工能力即会不会和员工治理即容不容许）类似，业务的稳定离不开三方面的建设：
- 工具建设：对应员工能力，需要有工具的建设来补全稳定性需要的能力，从以下两个底层原理建设：
  - 从提升可靠性方面，告诉我们有那些手段，可以避免和减少故障；
  - 从提升可用性方面，告诉我们有那些手段，可以提前发现故障、减小故障范围和程度、快速修复故障；
- 意识培养：对应员工思维，没有正确的认知，就不会有意愿建立起正确的做事方法和行为，也难以设立起正确的目标，如“六要两不要”；
- 规章制度：我们需要建立起完善的制度与机制，并建立工具文化，最大程度的不犯低级错误和重复性错误，如CodeReview制度、发布Checklist制度和COE制度。

### 2022.10.08
> 你这样安排就成了一个快乐的程序员!

十月份学姐听了我的业务支持时间安排后说的这句话令我振聋发聩。如我在上文所述的安排，每天都有技术要求不高的业务开发和需求进展，感到充实而快乐；另一方面感觉每一天都很忙，一个阶段后回头看其实只是在按照既定的路线低效推进，而没有时间来思考真正重要的事情。“时间分割成许多段，等于没有时间” 一本书中这句话非常有警示作用，碎片时间的机械执行容易把手段当成了目的，技术项目上应留大块时间深入思考、回顾目标和寻求更优的路径等重要困难的事情。应该做的是更合理的时间管理为更重要的事情服务，重要的是谋求发展而不是快乐。
如履薄冰、战战兢兢、居安思危、脚踏实地、仰望星空！

### 2022.09.20
_活在当下_：之前除了管理系统的开发还使用过H5、SSR和MRN等技术栈的C端产品，这段开发经历帮助我在前端演练探索上得以快速理解不同技术栈的实现路径和工程化细节；而之前到餐的稳定性平台建设经历帮助我对稳定性建设体系和方法论有了基本的理解，在演练方案设计时能从整体上思考。对未来我们总有期盼和焦虑，更应该脚踏实地活在当下，关注自己负责的手头工作。小到每个项目、大到每个人生阶段，我们很难预见当下的经历对未来的影响，因此需要我们认真对待每件身边事，尊重每段人生经历独特的价值，沉淀必然会有用。

### 2022.08.02
>When there is only one single-line text input field in a form, the user agent should accept Enter in that field as a request to submit the form.
>
> https://www.w3.org/MarkUp/html-spec/html-spec_8.html#SEC8.2

当 form 只有一个 input 时，UA 应该接受 Enter 键来提交表单；而默认表单提交行为是刷新页面。所以当我们使用原生写法或者某些组件库（如 Element UI）时就会碰到表单中一个输入框时回车页面刷新的古怪行为。

### 2022.06.02
之前治理了一些业务的线上异常，但是修改完成之后异常率下降缓慢。所以本周排查了一下，发现了很严重的缓存问题，也就是有很多用户访问的是旧版本代码。
通常前端项目不会给入口文件 index.html 加 hash 值，也就不会触发强制更新。在浏览器端依赖的是 `Cache Control` 头来标识缓存策略。观察了我们的项目只携带了 `Etag` ，那么在没有指定明确策略的情况下浏览器怎么缓存呢？
答案是 [Heuristic caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching#heuristic_caching) ，非常聪明的一种策略。甚至有哲学的味道，也就是说存在很久的东西大概率会存活更长时间，比如故事、神话和宗教会一直流传，而蒸汽机发明时间较短被革新之后也就只能存在博物馆里了。

另外 [MDN 上关于缓存的这篇文章](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) 只有英文版内容完善。所以程序员一定要学好英文，信息时代会大大提高处理问题的效率和质量。

### 2022.04.16
>对于软件任务的进度安排，以下是我使用了很多年的经验法则：
> - 1/3计划
> - 1/6编码
> - 1/4构件测试和早期系统测试
> - 1/4系统测试，所有的构件已完成
>
> 《人月神话》

说下我的理解：因为对于所有的创造性活动都包含了三个阶段：构思、实现和交流。而这其中最重要的是实现前的完备构思和实现后的沟通交流。
- 1/3计划：从充分保障质量的角度可以让我们更好地实现代码，正所谓"谋定而后动"；
- 1/2联调测试：预留充足联调和测试时间用于跟其他各个角色沟通，如 PM、UI、UX、QA 和后端开发人员，好处有以下几点：
  - 更多沟通有助于保障产品细节的正确交付，毕竟单个角度的个体思维有限；
  - 即使出现重大问题，也能及时发现，并且时间还充足能够提供解决方案；
  - 从项目管理的角度也有好处，如果给开发留太多时间测试不充分，可能快到 deadline 了发现之前的 fatal bug 影响了产品相关的后续所有商业行为（如合同、发布会等）。
- 1/6编码：无疑给我们很大的压力，但也同时要求我们有更好的能力，如使用抽象和模型、更好的时间管理方式等，能让我们对自己有更高要求从而获得成长。

### 2022.03.25
- 本周在一件跟合作方确定一件小事上，从 leader 身上学到了质疑精神，也就是不迷信合作方的权威，比如这次产品提出的保障最佳体验会增加工作量，而不这么做又不甚影响用户体验，导致按产品想法实现的话 ROI 很低。
  我重新拉会后，leader 从实现方案应尽可能降低前后端工作量、未来的标准化和整体交付影响几个方面说服了产品，我学到了：
    - 在不质疑人（产品后端等）的专业性前提下，从事的整体角度考虑问题，尽可能地去想解决方案并跟合作方沟通。
    - 尽可能多地去了解业务，比如多看看一个功能在竞对和别的事业部里的实现，结合环境和业务特点去想为什么这么做，可以更好地帮助我们实现和把握全局，从而避免被人牵着走。
- 在读《卓有成效的管理者》时看到一句西方谚语“No man is a hero to his valet”，觉得等于谚语中的“近之则不逊”，这种情况的产生是为什么呢？是因为 hero 不只是 hero 还是一个平凡人，而 valet 却只是 valet。告诫我们在生活中不能因为目睹了同事领导的缺点却忽略了优点，而应该虚心学习做好同级沟通和向上管理，从而更好地完成工作

### 2022.03.18
在读《格鲁夫给经理人的第一课》，认识到所有的组织（不管是政府还是学校、企业还是事业单位）都是混合型组织：即职能部门和业务部门混合在一起。在我们公司里：
- 职能部门有财务、人力和后勤等保障工作部门外，还有XX平台和XX平台这样服务于业务部门的技术职能部门；
- 业务部门有外卖、美食、买菜和优选等。

这样做有什么好处呢？

1. 职能部门收集到各业务部门需求汇总可以实现高效的资源分配，可以更有规模效益，不仅能服务地更专业还能避免重复建设，共享也有利于知识的沉淀传播；
2. 业务部门可以聚焦在具体的事情上，从而对市场更敏感，需求更加明确，决策更加灵活，人员也更加有凝聚力和长期有耐心。

往小了看，在团队内部在做的技术项目建设可以看成是更小范围的组织划分后的职能部门，收集到需求后建设支持将成果传播，以支持其他专注做业务同学的生产力提升，而专注做业务的同学可以保持对业务的理解和敏感，同时保持稳定的产出。

### 2022.03.17
最近接触的东西都很有意思：
1. [利用API简化内容创建流程](https://www.sohu.com/a/280274317_118792) 的 [Contentful](https://www.contentful.com)
2. 能在浏览器中运行 Node.js 的在线编辑器 stackblitz 的 [Web Container](https://blog.stackblitz.com/posts/introducing-webcontainers/)
3. 将数据库分布式到用户的浏览器: [Database in the Browser, a Spec](https://stopa.io/post/279)


### 2022.02.25
**_治大国如烹小鲜_**

去饭店吃饭我们的需求是快速地吃到便宜又好吃的食物，类比到工作中，就是我们需要按预定的时间、可接受的品质以及最低的成本，来产出自己的交付物。

也就是说在 FE （甚至所有工程师）不能只考虑如期交付万事大吉，而是在这个过程中做好质量、效率和体验的工作，才能让组织更强大。因为，一个系统的整体效能远远大于各个部分的效能的简单叠加。

### 2022.02.18
MT 是一个注重方法论的组织，为了探索更高效的工作和生活方式，最近读了《微习惯：简单到不可能失败的自我管理法则》，学习到的方法论和感悟如下：

1. 大脑中习惯改变中的两个关键工具：
  - 基底神经节：愚蠢的重复者，控制条件反射的动作，如喝水、走路，
  - 前额皮层：聪明的管理者，主管思考和理性决策，如编码
2. 我们往往靠意志力来坚持一个习惯，也就是依靠前额皮层，在精力充沛时容易做到。可问题是，它容易疲劳。因为它的功能太过强大，所以会消耗太多精力，让你感到疲劳。而且当你疲劳时，掌管重复的部分就会接管大脑
3. 就像电流总是去往电阻最小的通路，我们会在疲劳时有抵触情绪时感到压力从而陷入消极情绪，这时候不仅坚持不了好习惯，还会朝着坏习惯走去

篇幅所限不再展开，作者在分析大脑是如何工作的之后，得出了微习惯才是最有效的管理自我的手段，也就是小目标简单重复，让目标达成没有压力从而依靠神经节的惯性重复形成习惯。
[全书介绍](/post/mini-habits/)


### 2022.01.21
在孤独大脑公众号看到这么一则公式：`好运气 = 做对的事情 * 把事情做好`，有以下思考：
1. 本周探索组件库之外的样式库结论是没有必要，这不是一件对的事情，即使做得好也无用武之地；而组件库是对的事情，在做好组件库的情况下，两者相乘必然拿到好的结果；
2. 团队里的 leader 属于做选择，也就是带领大家做对的事情；我们被带领的情况下，需要做好自己的事情；只有这样两者相乘，都做得好，才有机会打造出更好的前端团队，各位共勉！

### 2022.01.14
[豆瓣技术团队的指环王文化](https://blog.douban.com/douban/2007/12/17/105) 推荐给命名困难的你，这样的命名方式可以结合技术和兴趣，让工作变得有意思！

### 2022.01.07
关于输入和输出：在团队技术周刊产出过程中，发现产出比消费难好多，哪怕只是周刊这种知识的搬运呈现也要消化后总结。我们只有输入足够多的信息，经过消化吸收沉淀才变成自己的知识。有了足够多的知识才有可能再加工、创造和分享，变成我们的输出，这也就要求我们与时俱进和活到老学到老。反过来刻意的输出也会倒逼输入，比如我们工作中需要产出什么就会搜索学习积累到足够的知识来完成开发，再比如罗振宇为了每天发 60s 读书心得相关语音必然会保持阅读的习惯。

### 2021.12.31
1. 解决分享图片问题时反思了自己的错误行为：
- 上工治未病之病、中工治欲病之病、下工治已病之病：

    高明或有远见的智者，往往是在疾病没有蔓延或症候的时候及早干预，防范于未然，提前做好防护，防止疾病的发生或蔓延。相应地我们写代码时尽量提高代码质量是“未病”时预防，流程中的规范操作和监控告警 Lint 等工具是“欲病”时拦截，测试或线上出了问题就是“已病”了，这时候就要排查和修复问题了，不免焦头烂额手忙脚乱。
- 谋定而后动：在压力下排查问题会手忙脚乱，往往病急乱投医，这时候更需要充分运用对照实验和 [归纳推理](https://zh.wikipedia.org/wiki/归纳推理) 找出根因，才可少走弯路。
2. 受 [这篇文章](https://jeffhuang.com/productivity_text_file/) 影响，坚持用 txt 记录日志三年了，回顾半年日志，发现这种记事方式：
- 好处：可以做到事事有着落，一天里做完的事情是 0 完成的标记为 x，第二天将没有完成的复制到当天继续
- 不足：
    - 一个是不利于检索，长期的事情不能很好联系起来，明年记录时会尝试加 tag；
    - 一个是记了太多细碎的事情，看起来一天里事情堆得很满，忙着完成会导致思考太少，而很多事情不思考就会越来越忙但能力和见识不会提高。所以明年需要加入每天的思考，再每周融汇成认知迭代，周会时头脑风暴和讨论时也可以用得上。

### 2021.12.10
之前以为"1971客厅"是创新的业务，但最近看了[这篇关于线下空间预订功能的思考](http://www.woshipm.com/pd/4450965.html) 才知道这是之前已经尝试过又很快下线的业务，对这个模式不做评价上线后可以见分晓。这里想说的是 UI 和 UE，在页面功能上原版跟我们这次对比，优化了很多，比如：不展示悬浮的客服入口：节省界面空间；套餐决定时间段：跟用户自由选择时间段比不会产生浪费；展示日期周几和将人数选择放在场地套餐选择之后：直观上降低用户的决策的成本等。作为跟界面打交道的前端，这些视觉和交互作为我们的产出物，也是功能呈现，了解清楚他们的想法和意图有助于我们评审和更好地实现，也对我们去做没有设计的技术项目排版需要自由发挥时有帮助。

### 2021.11.20
只有个人才行动，行动只能由个人“实施者”来完成。只有个人具有目的，并能付诸行动以达到目的。“社会”与“团体”不能独立于成员的个人行动而存在。

最近读的三本书连起来了，《教父》《第一本经济学》《反脆弱》，宁愿相信黑手党头目给你的一个承诺而不是政府的一个竞选口号。因为政府不是个人，政府的目的是组成者各自目的的妥协和平衡，而个人作为个体有明确的荣辱人格，但作为团体的一部分往往盲目执行。

就像《让子弹飞》里面讲的，政府丧失公信力的时候，鸣冤鼓长草，民间由袍哥在讲茶大堂里话事。

### 2021.11.5
最近在看《 [反脆弱](https://book.douban.com/subject/25782902/) 》一书，大受震撼！分享几点：

- 尼采说”杀不死我的，使我更强大“，为什么呢？想想疫苗的作用便是利用灭活病毒的 DNA 使人体产生抗体，人为地制造“以毒攻毒”的条件从而在真正感染时有一个更强大的免疫系统；衍生到稳定性工作，为什么需要放火演练？再衍生到公司，为什么鼓励每天前进一公里？

- 把最紧急的工作交给办公室里最忙的人更容易完成，因为他们具有反脆弱性。

- 为什么初代 iPhone 和 iPad 只有一个 Home 键却击败了全键盘的诺基亚和黑莓，因为优雅简单本身就减去了脆弱性。 这恰恰是工程师欠缺的，我们总喜欢精确，喜欢关注事务而不是人。我们去写三体可能会写出水滴和二向箔，但绝不会写出程心。

- 为什么今年郑州水灾不可预测，因为预测总是根据以往发生的事情来推测的。而未来总是复杂多变，让之前根据经验设置的应急机制和设施显得脆弱。

最后留给大家一个思考，最近看到一个 [新闻](http://vblog.people.com.cn/index/playvideo/contentid/467912) ，换做是你会这么做吗？

### 2021.10.22
必要的冗余-存储数据的表应该跟可能的连接查询项添加外键直接关联，在服务端存储时添加数据，以便之后的数据分析环节通过 JOIN 操作获取，而不是各主体间为了简洁层层关联给数据获取和处理增加难度。
