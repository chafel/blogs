# 定律与方法目录维护

页面入口为 `/knowledge/`，从博客顶部“定律与方法”进入。

当前目录包含 10 个领域、184 个条目，均已有独立正文，路径为 `/knowledge/<id>/`。正文源文件位于 `content/knowledge/<id>.md`，阅读模板为 `layouts/knowledge/single.html`，样式为 `static/css/knowledge-article.css`。

## 添加条目与文章链接

编辑 `data/knowledge.json`，在合适分类的 `items` 中添加条目：

```json
{
  "id": "unique-entry-id",
  "name": "中文名称",
  "english": "English name",
  "aliases": ["别名", "缩写"],
  "type": "方法",
  "description": "用一句话解释这个工具做什么，必要时注明适用前提。",
  "url": "",
  "sources": ["https://example.com/original-source"]
}
```

- `id` 是稳定的英文短名，分类和条目之间不能重复。可用 `/knowledge/#unique-entry-id` 直接定位条目。
- `type` 使用：定律、定理、效应、模型、原则、方法、理论。
- `url` 留空时显示“待撰写”，不会生成虚假的文章链接。
- 写好文章后，把 `url` 改为 `/knowledge/unique-entry-id/`；页面会自动显示“阅读解读”，并纳入“只看有解读”的筛选。目录模板也支持外部文档地址，但当前完整性检查按站内正文约定执行。
- `sources` 是资料线索，和自己的解读地址分开维护。页面底部的参考列表来自顶层 `sources`。
- 修改数量、增加分类后，页面统计会在 Hugo 构建时自动更新。

搜索覆盖中文名、英文名、别名、简介、分类和类型。多个词用空格分隔，需同时匹配。按 `/` 聚焦搜索，搜索框内按 Escape 重置全部筛选。分类链接是页面锚点；若该分类被当前筛选隐藏，点击会重置筛选再定位。

## 正文格式与修订

每篇使用 JSON 形式的 front matter（位于 `---` 之间，兼容 YAML），包含 `title`、`date`、`draft: false`、`type: "knowledge"`、`knowledge_id`、`description`。`knowledge_id` 必须与目录条目 ID 和文件名一致。日期是文章创建日期；批量创建不代表已配置每日发布。

正文统一使用八个二级标题，保留编号：

1. 一个具体问题
2. 一句话解释
3. 出处与原意
4. 原理与机制
5. 一个完整案例
6. 适用条件与反例
7. 今天可以尝试的行动
8. 参考资料与关联条目

修改时优先保留原创解释、可核算的案例与适用边界。假设案例明确标注，经验规则与数学定理分开描述，争议或无法确认的归属不写成确定史实。最后一节保留主题参考资料与至少两个站内关联条目。更新参考资料时同步目录条目的 `sources`。

侧边目录、手机折叠目录、同领域上一篇/下一篇和返回原条目的链接由模板自动生成，无需在正文重复维护。

## 本地预览

使用与现有主发布配置一致的 Hugo Extended 0.108.0：

```sh
HUGO_RESOURCEDIR=/tmp/blog-hugo-resources hugo server --bind 127.0.0.1 --port 1313 --baseURL http://localhost:1313/ --disableFastRender --cacheDir /tmp/blog-hugo-cache
```

打开 `http://localhost:1313/knowledge/`。普通本地服务默认在内存构建，不会重写现有 `public` 文件。

## 发布前检查

- 确认名称、别名、分类与类型准确，避免同一概念重复收录。
- 核对文章地址真实可访问；不把参考资料地址误填成自己的文章地址。
- 核对计数、搜索、类型筛选、无结果提示和手机布局。
- 定期复查原始出处、争议与适用边界，尤其是心理效应与投资模型；正文中的参考链接便于继续修订。

运行 `python3 scripts/validate_knowledge.py` 可检查目录覆盖、元数据、八段结构、来源和关联条目。构建到独立临时目录后，再运行 `python3 scripts/validate_knowledge.py --build-dir /path/to/build`，检查生成页面和所有知识库站内链接、锚点及重复 ID。检查不替代内容审阅，也不自动判断外部来源的学术可靠性。
