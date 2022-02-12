---
title: "Hello Hugo"
date: 2022-02-02T05:11:04+08:00
---

## 新年新气象

因为<s>忙于工作~</s>纵情向前，之前搭建在阿里云上的 WordPress 网站忘记续费而关闭，在农历大年初二的晚上三点我终于下定决定使用 Hugo 重启这个博客站点。

创作的目的是为了总结思考督促成长，另一方面雁过留声，总觉得应该写点什么留下来，也算是对抗虚无和时空湮灭的一种聊以慰藉的方式！

### 建站步骤
下面介绍下使用 Hugo 搭建博客站点的步骤，总耗时约 2h：
1. 跟随 [Quick Start](https://gohugo.io/getting-started/quick-start/) 即可，其中包含了：
    - 安装 Hugo
    - 安装主题：
      1. 从主题列表[^1]里选择一款合适的 
      2. 之后将其作为 git submodule 
      3. 根据主题使用说明配置[^2]即可，一般是将配置文件内容更新到项目下的 `config.toml` 
2. 将整个文件夹托管到 GitHub
3. 配置 [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), 有两种方式：
   - 将静态资源文件夹 `public` 里的内容专门放在用于部署的分支，然后根据 [文档](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) 配置选择此分支即可
   - 👇 下面这种方式更自动化，推荐
4. [Optional] 参考 [hosting-on-github](https://gohugo.io/hosting-and-deployment/hosting-on-github/) 配置 GitHub Actions(即 workflows），commit push 之后会自动构建为静态站点并部署更新，非常方便👍
5. [Optional] [配置自定义域名](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-an-apex-domain)
   

### 使用
- 新建博客时： `hugo new post/your-blog-name.md`
- 本地预览：`hugo server -D`
- 构建：`hugo -D`
- 常用 Git 操作

### 参考
1. [Even 主题预览](https://hugo-theme-even.netlify.app/post/even-preview/)
2. [Hugo 搭建博客实践](https://creaink.github.io/post/Devtools/Hugo/Hugo-intro.html)
3. [图片路径问题](http://i.lckiss.com/?p=7455)
4. [生成 favico](https://www.favicon-generator.org/)
5. [写文章常用的快捷键](https://gohugo.io/content-management/shortcodes/)


[^1]: [所有主题](https://themes.gohugo.io/)
[^2]: [Even 主题配置](https://github.com/olOwOlo/hugo-theme-even/blob/master/README-zh.md)
