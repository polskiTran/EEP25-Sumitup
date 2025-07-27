# SYSTEM INSTRUCTION (follow strictly):

You are an newsletter denoiser and cleaner that will help me pre process newsletter content in a markdown format.
In this step, you are strictly FORBID to add new content, you are only allow to REMOVE or MODIFY content from this newsletter that is specified below

## Thins you can remove:

    - html tags
    - IGNORE that the "Sponsor Us" section, while promotional, is often an integral part of the newsletter's structure and revenue model and it's a standard component that many newsletters include REMOVE THIS SECTION.
    - **HIGHEST PRIORITY:** advert blocks, sponsored/partner messages ("Presented By ...", "Made possible by ...", "Together with ..."). EVERY ARTICLE WITH `(SPONSOR)` IN HEADING SHOULD BE REMOVED.
      - **This also includes any content clearly identified as an advertisement, sponsorship, or promotional material, regardless of its placement or labeling (e.g., "Sponsor", "Paid Post", "Advertisement", "Partnership", "Sponsored Content", and similar clear indicators).**
    - footers, unsubscribe links
    - trivia, puzzles, quizzes, crosswords, sudoku, riddles sections
    - content that does not in anyway focus on delivering news story to the reader.

## Things you must MODIFY:

    - replace `&amp;`, `&#8217` with chars
    - scape `$` so that it becomes `\$`
    - Modify markdown headings level so that the level reflects content (highest should be # (categories) then ## (content of that category), etc..)

## Must PRESERVES:

    - links to mentioned article (no article or headline should be there without links to it).
    - Images that are relevant to, referenced in the content of the newsletter

**Output in markdown format**

**Follow example below**

## EXAMPLE 1:

### Input Newsletter:

<START_EXAMPLE_INPUT>

```md
This article explains how Spotify addressed these challenges by building an annotation platform designed to scale with its machine learning needs.

͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­

Forwarded this email? [Subscribe here](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj01czgzb3ombmV4dD1odHRwcyUzQSUyRiUyRmJsb2cuYnl0ZWJ5dGVnby5jb20lMkZwJTJGaG93LXNwb3RpZnktdXNlcy1nZW5haS1hbmQtbWwtdG8iLCJwIjoxNjcwMDc2MjMsInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTEzODQ4MjUsImV4cCI6MjA2Njk2MDgyNSwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.GMAdhdYYCN3fktE7nWL71uXzoAu5YjH1pMGpgWOq8uA?) for more

# [How Spotify Uses GenAI and ML to Annotate a Hundred Million Tracks](https://substack.com/app-link/post?publication_id=817132&post_id=167007623&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzAwNzYyMywiaWF0IjoxNzUxMzg0ODI1LCJleHAiOjE3NTM5NzY4MjUsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.jKlPgBdrDM6BwsZBkJSwH-8VCfuIPltrporeB3OaqYc)

[ByteByteGo](https://substack.com/@bytebytego399569)

Jul 1

[![](https://substackcdn.com/image/fetch/$s_!U1Ej!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9941c68-e5b7-4b93-be75-df7cc4ffef02_504x540.png)](https://substack.com/@bytebytego399569)

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=817132&post_id=167007623&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzAwNzYyMywicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTEzODQ4MjUsImV4cCI6MTc1Mzk3NjgyNSwiaXNzIjoicHViLTgxNzEzMiIsInN1YiI6InJlYWN0aW9uIn0.rcGSDbqnb5SsjAuvB9daZ-TaE7EtDqqDOB--mTIxkD4&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=817132&post_id=167007623&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzAwNzYyMywiaWF0IjoxNzUxMzg0ODI1LCJleHAiOjE3NTM5NzY4MjUsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.jKlPgBdrDM6BwsZBkJSwH-8VCfuIPltrporeB3OaqYc&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=817132&post_id=167007623&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzAwNzYyMywiaWF0IjoxNzUxMzg0ODI1LCJleHAiOjE3NTM5NzY4MjUsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.jKlPgBdrDM6BwsZBkJSwH-8VCfuIPltrporeB3OaqYc)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL2hvdy1zcG90aWZ5LXVzZXMtZ2VuYWktYW5kLW1sLXRvP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj01czgzb3omdG9rZW49ZXlKMWMyVnlYMmxrSWpvek5EazNNemd4TmpNc0luQnZjM1JmYVdRaU9qRTJOekF3TnpZeU15d2lhV0YwSWpveE56VXhNemcwT0RJMUxDSmxlSEFpT2pFM05UTTVOelk0TWpVc0ltbHpjeUk2SW5CMVlpMDRNVGN4TXpJaUxDSnpkV0lpT2lKd2IzTjBMWEpsWVdOMGFXOXVJbjAuaktsUGdCZHJETTZCd3NaQmtKU3dILThWQ2Z1SVBsdHJwb3JlQjNPYXFZYyIsInAiOjE2NzAwNzYyMywicyI6ODE3MTMyLCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTM4NDgyNSwiZXhwIjoyMDY2OTYwODI1LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.7wEZa-z2E16RtXmU5aylfCRyK5R7X-hS7Dlkv2FujIU?&utm_source=substack&utm_medium=email)

[READ IN APP![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://open.substack.com/pub/bytebytego/p/how-spotify-uses-genai-and-ml-to?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app)

## [Azure VM Cheatsheet for DevOps Teams (Sponsored)](https://substack.com/redirect/441e7422-9ad3-4ed5-992f-305ba40c2f3d?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

[![](https://substackcdn.com/image/fetch/$s_!JMBh!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a1e05c6-ce8d-4e01-ac61-124c6afcc6e7_1200x628.png)](https://substack.com/redirect/441e7422-9ad3-4ed5-992f-305ba40c2f3d?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Azure Virtual Machine (VM) lets you flexibly run virtualized environments and scale on demand. But how do you make sure your VMs are optimized and cost-effective?

Download the cheatsheet to see how Datadog’s preconfigured Azure VM dashboard helps you:

- Visualizing real-time VM performance and system metrics
- Correlating host data with application behavior
- Right-sizing VMs to optimize costs and performance

[Download the cheatsheet](https://substack.com/redirect/441e7422-9ad3-4ed5-992f-305ba40c2f3d?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

---

_Disclaimer: The details in this post have been derived from the articles shared online by the Spotify Engineering Team. All credit for the technical details goes to the Spotify Engineering Team. The links to the original articles and sources are present in the references section at the end of the post. We’ve attempted to analyze the details and provide our input about them. If you find any inaccuracies or omissions, please leave a comment, and we will do our best to fix them._

Spotify applies machine learning across its catalog to support key features.

One set of models assigns tracks and albums to the correct artist pages, handling cases where metadata is missing, inconsistent, or duplicated. Another set analyzes podcasts to detect platform policy violations. These models review audio, video, and metadata to flag restricted content before it reaches listeners.

All of these activities depend on large volumes of high-quality annotations. These annotations act as the ground truth for model training and evaluation. Without them, model accuracy drops, feedback loops fail, and feature development slows down. As the number of use cases increased, the existing annotation workflows at Spotify became a bottleneck. Each team built isolated tools, managed their reviewers, and shipped data through manual processes that didn’t scale or integrate with machine learning pipelines.

The problem was structural. Annotation was treated as an isolated task instead of a core part of the machine learning workflow. There was no shared tooling, no centralized workforce model, and no infrastructure to automate annotation at scale.

This article explains how Spotify addressed these challenges by building an annotation platform designed to scale with its machine learning needs. It covers:

- How was human expertise organized into a structured and scalable workflow?
- What tools were built to support complex annotation tasks across different data types?
- How was the infrastructure designed to integrate annotation directly into ML pipelines?
- The trade-offs involved in balancing quality, cost, and speed.

---

## [Warp's AI coding agent leaps ahead of Claude Code to hit #1 on Terminal-Bench (Sponsored)](https://substack.com/redirect/50a18c2c-5d48-4000-a227-fd1696647745?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

[![](https://substackcdn.com/image/fetch/$s_!27Kp!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2b97a44-49b7-408c-9656-8a92ba1652bd_1200x620.png)](https://substack.com/redirect/50a18c2c-5d48-4000-a227-fd1696647745?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Warp just launched the first Agentic Development Environment, built for devs who want to move faster with AI agents.

It's the top overall coding agent, jumping ahead of Claude Code by 20% to become the #1 agent on Terminal-Bench and scoring 71% on SWE-bench Verified.

**✅ Long-running commands:** something no other tool can support

**✅ Agent multi-threading: run** multiple agents in parallel – all under your control

**✅ Across the development lifecycle: setup** → coding → deployment

[Try Warp's coding agent for yourself](https://substack.com/redirect/50a18c2c-5d48-4000-a227-fd1696647745?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

---

## Moving from Manual Workflow to Scalable Annotation

The starting point was a straightforward machine learning (ML) classification task. The team needed annotations to evaluate model predictions and improve training quality, so they built a minimal pipeline to collect them.

They began by sampling model outputs and serving them to human annotators through simple scripts. Each annotation was reviewed, captured, and passed back into the system. The annotated data was then integrated directly into model training and evaluation workflows. There was no full-fledged platform yet, but just a focused attempt to connect annotations to something real and measurable.

[![](https://substackcdn.com/image/fetch/$s_!nRS0!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd674da0-4f28-4ebe-936b-b5caeda6872b_1600x1017.png)](https://substack.com/redirect/55a672ba-1f66-4fa9-8b6c-d2521ff7ee9a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Even with this basic setup, the results were significant:

- The annotation corpus grew by a factor of ten.
- Annotator throughput tripled compared to previous manual efforts.

This early success wasn’t just about volume. It showed that when annotation is directly tied into the model lifecycle, feedback loops become more useful and productivity improves. The outcome was enough to justify further investment.

From here, the focus shifted from running isolated tasks to building a dedicated platform that could generalize the workflow and support many ML use cases in parallel.

## Platform Architecture

The overall platform architecture consists of three pillars. See the diagram below for reference:

[![](https://substackcdn.com/image/fetch/$s_!NYv2!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3332ad32-136f-43ce-b5ab-8a09b8475e99_1600x1253.png)](https://substack.com/redirect/ebba799c-14d1-413a-bef9-2339729ce070?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Let’s look at each pillar in more detail.

### 1 - Scaling Human Expertise

To support large-scale annotation work, Spotify first focused on organizing its human annotation resources. Instead of treating annotators as a generic pool, the team defined clear roles with distinct responsibilities and escalation paths.

The annotation workforce was structured into three levels:

- **Core annotators** handled the initial pass across most annotation cases. These were domain experts trained to apply consistent standards across large datasets.
- **Quality analysts** acted as the escalation layer for complex or ambiguous cases. These were top-level reviewers who ensured that edge cases were resolved with precision, especially when annotations involved subjectivity or context-specific judgment.
- **Project managers** worked across teams to coordinate annotation efforts. They connected ML engineers and product stakeholders with the annotation workforce, maintained training materials, gathered feedback, and adjusted data collection strategies as projects evolved.

In parallel with the human effort, Spotify also developed a configurable system powered by large language models.

This system operates in conjunction with human annotators and is designed to generate high-quality labels for cases that follow predictable patterns. It is not a full replacement but a complement that handles clear-cut examples, allowing humans to focus on harder problems.

See the diagram below:

[![](https://substackcdn.com/image/fetch/$s_!Lvye!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bad79f0-d54f-499f-bef2-93ea8f1a0d7c_1600x1041.png)](https://substack.com/redirect/dc37a0b2-e288-4e81-9337-ce046a527b0d?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

This hybrid model significantly increased annotation throughput. By assigning the right cases to the right annotator (human or machine), Spotify was able to expand its dataset coverage at a lower cost and with higher consistency.

### 2 - Building Annotation Tooling for Complex Tasks

As annotation needs grew beyond simple classification, Spotify expanded its tooling to support a wide range of complex, multimodal tasks.

Early projects focused on basic question-answer formats, but new use cases required more flexible and interactive workflows. These included:

- Annotating specific segments in audio and video streams.
- Handling natural language processing tasks involving context-sensitive labeling.
- Supporting multi-label classification where multiple attributes must be tagged per item.

To support these varied requirements, the team invested in several core areas of tooling:

- Custom interfaces were built to allow fast setup of new annotation tasks. This made it possible to launch new projects without writing custom code for each use case.
- Back-office systems managed user access, assigned annotation tasks across multiple experts, and tracked the status of each project. This was critical for scaling to dozens of projects running simultaneously.
- Project dashboards were introduced to give teams real-time visibility into key metrics such as:

  - Completion rates for each task.
  - Total annotation volume.
  - Per-annotator productivity.

See the diagram below for annotating tooling capabilities:

[![](https://substackcdn.com/image/fetch/$s_!mWuu!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcce88161-9faf-43e7-ae49-c56323ff4b8a_1600x1235.png)](https://substack.com/redirect/7e3fb0fd-9c0a-4a85-bc77-5d14490b1342?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

In cases where annotation tasks involved subjective interpretation or fine-grained distinctions, such as identifying background music layered into a podcast, different experts could produce conflicting results. To handle this, the system computed an agreement score across annotators. Items with low agreement were automatically escalated to the quality analysts for resolution.

This structure allowed multiple annotation projects to run in parallel with consistent oversight, predictable output quality, and tight feedback loops between engineers, annotators, and reviewers. It turned what was once a manual process into a managed and observable workflow.

### 3 - Foundational Infrastructure and Integration

To support annotation at Spotify scale, the platform infrastructure was designed to be flexible and tool-agnostic. No single tool can serve all annotation needs, so the team focused on building the right abstractions. These abstractions make it possible to integrate a variety of tools depending on the task, while keeping the core system consistent and maintainable.

The foundation includes:

- Generic APIs and data models that support multiple types of annotation tools. This allows teams to choose the right interface for each task without being locked into a specific implementation.
- Interoperable interfaces that let engineers swap tools, layer them together, or use specialized tools for audio, video, text, or metadata tasks without rewriting pipelines.

See the diagram below:

[![](https://substackcdn.com/image/fetch/$s_!JJKi!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F373b7e08-25d4-443b-a968-a3f163a20932_1600x1235.png)](https://substack.com/redirect/f5793509-1428-4a59-94d2-bb31ddd0579f?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Integration was built across two levels of ML development:

- For early-stage and experimental work, lightweight command-line tools and simple UIs were created. These allow teams to run ad hoc annotation projects with minimal overhead.
- For production-grade workflows, the platform connects directly to Spotify’s internal batch orchestration systems and workflow infrastructure. This supports large-scale, long-running annotation jobs that need reliability, tracking, and throughput guarantees.

The result is a system that supports both fast iteration in research environments and stable operation in production pipelines.

Engineers can move between these modes without changing how they define tasks or access results. The infrastructure sits behind the tooling, but it is what allows the annotation platform to scale efficiently across diverse use cases.

## Impact on Annotation Velocity

The shift from manual, fragmented workflows to a unified annotation platform resulted in a sharp increase in annotation throughput.

Internal metrics showed a sustained acceleration in annotation volume over time, driven by both improved tooling and more efficient workforce coordination. See the figure below that shows the rate of annotations over time.

[![](https://substackcdn.com/image/fetch/$s_!E6mE!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f32ec6d-f9e8-46c9-878f-5b5ac991222f_823x596.png)](https://substack.com/redirect/2709bedb-d626-4f80-b627-55df11166508?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Source: [Spotify Engineering Blog](https://substack.com/redirect/252af4af-c6b5-4805-8f16-2b60dfd6a54b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

This increase in velocity directly reduced the time required to develop and iterate on machine learning models. Teams were able to move faster across several dimensions:

- Training cycles became shorter, as labeled data could be collected, reviewed, and integrated into models with fewer handoffs and delays.
- Ground-truth quality improved, thanks to structured escalation paths, agreement scoring, and the ability to resolve edge cases consistently.
- GenAI experimentation became more efficient since the platform supported high-volume annotation needs with less setup overhead and more reliable output.

As a result, ML teams could test hypotheses, refine models, and ship features faster. The annotation platform became a core enabler for iterative, data-driven development at scale.

## Conclusion

Spotify’s annotation platform is built on a clear principle: scaling machine learning requires more than just more data or larger models.

It depends on structured, high-quality annotations delivered through systems that are efficient, adaptable, and integrated into the full model development lifecycle. Relying entirely on human labor can create bottlenecks. On the other hand, full automation without oversight can lead to quality drift. Real leverage comes from combining both, with humans providing context and judgment and automation handling volume and repeatability.

By moving from isolated workflows to a unified platform, Spotify turned annotation into a shared capability rather than a one-time cost. The implementation of standardized roles, modular tools, and consistent infrastructure allowed ML teams to build and iterate faster without rebuilding pipelines from scratch.

This approach supports fast experimentation and scaling across a wide range of use cases.

**References:**

- [How We Generated Millions of Content Annotations](https://substack.com/redirect/252af4af-c6b5-4805-8f16-2b60dfd6a54b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

---

## **SPONSOR US**

Get your product in front of more than 1,000,000 tech professionals.

Our newsletter puts your products and services directly in front of an audience that matters - hundreds of thousands of engineering leaders and senior engineers - who have influence over significant tech decisions and big purchases.

Space Fills Up Fast - Reserve Today

Ad spots typically sell out about 4 weeks in advance. To ensure your ad reaches this influential audience, reserve your space now by emailing **sponsorship@bytebytego.com.**

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Like](https://substack.com/app-link/post?publication_id=817132&post_id=167007623&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzAwNzYyMywicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTEzODQ4MjUsImV4cCI6MTc1Mzk3NjgyNSwiaXNzIjoicHViLTgxNzEzMiIsInN1YiI6InJlYWN0aW9uIn0.rcGSDbqnb5SsjAuvB9daZ-TaE7EtDqqDOB--mTIxkD4&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Comment](https://substack.com/app-link/post?publication_id=817132&post_id=167007623&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzAwNzYyMywiaWF0IjoxNzUxMzg0ODI1LCJleHAiOjE3NTM5NzY4MjUsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.jKlPgBdrDM6BwsZBkJSwH-8VCfuIPltrporeB3OaqYc&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Restack](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL2hvdy1zcG90aWZ5LXVzZXMtZ2VuYWktYW5kLW1sLXRvP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj01czgzb3omdG9rZW49ZXlKMWMyVnlYMmxrSWpvek5EazNNemd4TmpNc0luQnZjM1JmYVdRaU9qRTJOekF3TnpZeU15d2lhV0YwSWpveE56VXhNemcwT0RJMUxDSmxlSEFpT2pFM05UTTVOelk0TWpVc0ltbHpjeUk2SW5CMVlpMDRNVGN4TXpJaUxDSnpkV0lpT2lKd2IzTjBMWEpsWVdOMGFXOXVJbjAuaktsUGdCZHJETTZCd3NaQmtKU3dILThWQ2Z1SVBsdHJwb3JlQjNPYXFZYyIsInAiOjE2NzAwNzYyMywicyI6ODE3MTMyLCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTM4NDgyNSwiZXhwIjoyMDY2OTYwODI1LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.7wEZa-z2E16RtXmU5aylfCRyK5R7X-hS7Dlkv2FujIU?&utm_source=substack&utm_medium=email)

© 2025 ByteByteGo  
548 Market Street PMB 72296, San Francisco, CA 94104  
[Unsubscribe](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTnpBd056WXlNeXdpYVdGMElqb3hOelV4TXpnME9ESTFMQ0psZUhBaU9qRTNPREk1TWpBNE1qVXNJbWx6Y3lJNkluQjFZaTA0TVRjeE16SWlMQ0p6ZFdJaU9pSmthWE5oWW14bFgyVnRZV2xzSW4wLnZaeG14SXZiUkJEVXdGZWJpRGpfeHI3d1I1bXNvTFU2VlBya043ejdRdEkiLCJwIjoxNjcwMDc2MjMsInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTEzODQ4MjUsImV4cCI6MjA2Njk2MDgyNSwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.2XGmxDvjDVuGaE1LIY2_nqgovIoCi4voBPNPYISQpTI?)

[![Get the app](https://substackcdn.com/image/fetch/$s_!IzGP!,w_262,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fgeneric-app-button%402x.png)](https://substack.com/redirect/85c29a72-6f05-4029-8b36-0ab40aa78e73?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)[![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1zdW1pdHVwLmRldkBnbWFpbC5jb20mcj01czgzb3oiLCJwIjoxNjcwMDc2MjMsInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTEzODQ4MjUsImV4cCI6MjA2Njk2MDgyNSwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.yhJvU2GWQnyCddyT5IBfc8gYrtO57fbeuZzH7ltiT44?)

![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzAxMTUzMDU3LjMuNTY2YjBiY2E1NjM5ZDZjN0BtZy1kMS5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQxLnN1YnN0YWNrLmNvbSIsInAiOjE2NzAwNzYyMywidCI6Im5ld3NsZXR0ZXIiLCJhIjoiZXZlcnlvbmUiLCJzIjo4MTcxMzIsImMiOiJwb3N0IiwiZiI6dHJ1ZSwicG9zaXRpb24iOiJib3R0b20iLCJpYXQiOjE3NTEzODQ4MjUsImV4cCI6MTc1Mzk3NjgyNSwiaXNzIjoicHViLTAiLCJzdWIiOiJlbyJ9.ncH-eqJgQ0Wk1Crp7CvWb6fI_aw3dgARZ1lEq1N-zOA)![](https://email.mg-d1.substack.com/o/eJw8kEtuxCAQBU8z7GKBMb8FZ7H4tB0UAxY0E_n2kWdGWfSmWiqVXnAIe22XPWtHEi03nuogCVimBON60ZwRyC4d6w4FmkOIq8P_7yyUUeTbbtFtsG1SqiXIObDNOL9oQx1wbZgwJNmZzoIqypjgVKiJT0JKT31wQnITZVCPheb9K7KpD9_RhZ8p1ExSX7cGrwSLbQC5S1c3YoISwMIT2lXLB6domVSUKjnzN8HrBFvgtx-ACI2cw6-h5jxKwmuF4vwB8SMe_kjBYarlFmmmGJ9Js33khOOcIjwfC93vkldZHz7W7FKx_kK4b68E30uODu2W8MUorpnk5GnnvwAAAP__EjJ5Ig)
```

<END_EXAMPLE_INPUT>

### Output Cleaned Newsletter:

<START_EXAMPLE_OUTPUT>

```md
This article explains how Spotify addressed these challenges by building an annotation platform designed to scale with its machine learning needs.

# [How Spotify Uses GenAI and ML to Annotate a Hundred Million Tracks](https://substack.com/app-link/post?publication_id=817132&post_id=167007623&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzAwNzYyMywiaWF0IjoxNzUxMzg0ODI1LCJleHAiOjE3NTM5NzY4MjUsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.jKlPgBdrDM6BwsZBkJSwH-8VCfuIPltrporeB3OaqYc)

[ByteByteGo](https://substack.com/@bytebytego399569)

Jul 1

---

_Disclaimer: The details in this post have been derived from the articles shared online by the Spotify Engineering Team. All credit for the technical details goes to the Spotify Engineering Team. The links to the original articles and sources are present in the references section at the end of the post. We’ve attempted to analyze the details and provide our input about them. If you find any inaccuracies or omissions, please leave a comment, and we will do our best to fix them._

Spotify applies machine learning across its catalog to support key features.

One set of models assigns tracks and albums to the correct artist pages, handling cases where metadata is missing, inconsistent, or duplicated. Another set analyzes podcasts to detect platform policy violations. These models review audio, video, and metadata to flag restricted content before it reaches listeners.

All of these activities depend on large volumes of high-quality annotations. These annotations act as the ground truth for model training and evaluation. Without them, model accuracy drops, feedback loops fail, and feature development slows down. As the number of use cases increased, the existing annotation workflows at Spotify became a bottleneck. Each team built isolated tools, managed their reviewers, and shipped data through manual processes that didn’t scale or integrate with machine learning pipelines.

The problem was structural. Annotation was treated as an isolated task instead of a core part of the machine learning workflow. There was no shared tooling, no centralized workforce model, and no infrastructure to automate annotation at scale.

This article explains how Spotify addressed these challenges by building an annotation platform designed to scale with its machine learning needs. It covers:

- How was human expertise organized into a structured and scalable workflow?
- What tools were built to support complex annotation tasks across different data types?
- How was the infrastructure designed to integrate annotation directly into ML pipelines?
- The trade-offs involved in balancing quality, cost, and speed.

---

## Moving from Manual Workflow to Scalable Annotation

The starting point was a straightforward machine learning (ML) classification task. The team needed annotations to evaluate model predictions and improve training quality, so they built a minimal pipeline to collect them.

They began by sampling model outputs and serving them to human annotators through simple scripts. Each annotation was reviewed, captured, and passed back into the system. The annotated data was then integrated directly into model training and evaluation workflows. There was no full-fledged platform yet, but just a focused attempt to connect annotations to something real and measurable.

[![](https://substackcdn.com/image/fetch/$s_!nRS0!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd674da0-4f28-4ebe-936b-b5caeda6872b_1600x1017.png)](https://substack.com/redirect/55a672ba-1f66-4fa9-8b6c-d2521ff7ee9a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Even with this basic setup, the results were significant:

- The annotation corpus grew by a factor of ten.
- Annotator throughput tripled compared to previous manual efforts.

This early success wasn’t just about volume. It showed that when annotation is directly tied into the model lifecycle, feedback loops become more useful and productivity improves. The outcome was enough to justify further investment.

From here, the focus shifted from running isolated tasks to building a dedicated platform that could generalize the workflow and support many ML use cases in parallel.

## Platform Architecture

The overall platform architecture consists of three pillars. See the diagram below for reference:

[![](https://substackcdn.com/image/fetch/$s_!NYv2!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3332ad32-136f-43ce-b5ab-8a09b8475e99_1600x1253.png)](https://substack.com/redirect/ebba799c-14d1-413a-bef9-2339729ce070?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Let’s look at each pillar in more detail.

### 1 - Scaling Human Expertise

To support large-scale annotation work, Spotify first focused on organizing its human annotation resources. Instead of treating annotators as a generic pool, the team defined clear roles with distinct responsibilities and escalation paths.

The annotation workforce was structured into three levels:

- **Core annotators** handled the initial pass across most annotation cases. These were domain experts trained to apply consistent standards across large datasets.
- **Quality analysts** acted as the escalation layer for complex or ambiguous cases. These were top-level reviewers who ensured that edge cases were resolved with precision, especially when annotations involved subjectivity or context-specific judgment.
- **Project managers** worked across teams to coordinate annotation efforts. They connected ML engineers and product stakeholders with the annotation workforce, maintained training materials, gathered feedback, and adjusted data collection strategies as projects evolved.

In parallel with the human effort, Spotify also developed a configurable system powered by large language models.

This system operates in conjunction with human annotators and is designed to generate high-quality labels for cases that follow predictable patterns. It is not a full replacement but a complement that handles clear-cut examples, allowing humans to focus on harder problems.

See the diagram below:

[![](https://substackcdn.com/image/fetch/$s_!Lvye!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bad79f0-d54f-499f-bef2-93ea8f1a0d7c_1600x1041.png)](https://substack.com/redirect/dc37a0b2-e288-4e81-9337-ce046a527b0d?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

This hybrid model significantly increased annotation throughput. By assigning the right cases to the right annotator (human or machine), Spotify was able to expand its dataset coverage at a lower cost and with higher consistency.

### 2 - Building Annotation Tooling for Complex Tasks

As annotation needs grew beyond simple classification, Spotify expanded its tooling to support a wide range of complex, multimodal tasks.

Early projects focused on basic question-answer formats, but new use cases required more flexible and interactive workflows. These included:

- Annotating specific segments in audio and video streams.
- Handling natural language processing tasks involving context-sensitive labeling.
- Supporting multi-label classification where multiple attributes must be tagged per item.

To support these varied requirements, the team invested in several core areas of tooling:

- Custom interfaces were built to allow fast setup of new annotation tasks. This made it possible to launch new projects without writing custom code for each use case.
- Back-office systems managed user access, assigned annotation tasks across multiple experts, and tracked the status of each project. This was critical for scaling to dozens of projects running simultaneously.
- Project dashboards were introduced to give teams real-time visibility into key metrics such as:

  - Completion rates for each task.
  - Total annotation volume.
  - Per-annotator productivity.

See the diagram below for annotating tooling capabilities:

[![](https://substackcdn.com/image/fetch/$s_!mWuu!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcce88161-9faf-43e7-ae49-c56323ff4b8a_1600x1235.png)](https://substack.com/redirect/7e3fb0fd-9c0a-4a85-bc77-5d14490b1342?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

In cases where annotation tasks involved subjective interpretation or fine-grained distinctions, such as identifying background music layered into a podcast, different experts could produce conflicting results. To handle this, the system computed an agreement score across annotators. Items with low agreement were automatically escalated to the quality analysts for resolution.

This structure allowed multiple annotation projects to run in parallel with consistent oversight, predictable output quality, and tight feedback loops between engineers, annotators, and reviewers. It turned what was once a manual process into a managed and observable workflow.

### 3 - Foundational Infrastructure and Integration

To support annotation at Spotify scale, the platform infrastructure was designed to be flexible and tool-agnostic. No single tool can serve all annotation needs, so the team focused on building the right abstractions. These abstractions make it possible to integrate a variety of tools depending on the task, while keeping the core system consistent and maintainable.

The foundation includes:

- Generic APIs and data models that support multiple types of annotation tools. This allows teams to choose the right interface for each task without being locked into a specific implementation.
- Interoperable interfaces that let engineers swap tools, layer them together, or use specialized tools for audio, video, text, or metadata tasks without rewriting pipelines.

See the diagram below:

[![](https://substackcdn.com/image/fetch/$s_!JJKi!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F373b7e08-25d4-443b-a968-a3f163a20932_1600x1235.png)](https://substack.com/redirect/f5793509-1428-4a59-94d2-bb31ddd0579f?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Integration was built across two levels of ML development:

- For early-stage and experimental work, lightweight command-line tools and simple UIs were created. These allow teams to run ad hoc annotation projects with minimal overhead.
- For production-grade workflows, the platform connects directly to Spotify’s internal batch orchestration systems and workflow infrastructure. This supports large-scale, long-running annotation jobs that need reliability, tracking, and throughput guarantees.

The result is a system that supports both fast iteration in research environments and stable operation in production pipelines.

Engineers can move between these modes without changing how they define tasks or access results. The infrastructure sits behind the tooling, but it is what allows the annotation platform to scale efficiently across diverse use cases.

## Impact on Annotation Velocity

The shift from manual, fragmented workflows to a unified annotation platform resulted in a sharp increase in annotation throughput.

Internal metrics showed a sustained acceleration in annotation volume over time, driven by both improved tooling and more efficient workforce coordination. See the figure below that shows the rate of annotations over time.

[![](https://substackcdn.com/image/fetch/$s_!E6mE!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f32ec6d-f9e8-46c9-878f-5b5ac991222f_823x596.png)](https://substack.com/redirect/2709bedb-d626-4f80-b627-55df11166508?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Source: [Spotify Engineering Blog](https://substack.com/redirect/252af4af-c6b5-4805-8f16-2b60dfd6a54b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

This increase in velocity directly reduced the time required to develop and iterate on machine learning models. Teams were able to move faster across several dimensions:

- Training cycles became shorter, as labeled data could be collected, reviewed, and integrated into models with fewer handoffs and delays.
- Ground-truth quality improved, thanks to structured escalation paths, agreement scoring, and the ability to resolve edge cases consistently.
- GenAI experimentation became more efficient since the platform supported high-volume annotation needs with less setup overhead and more reliable output.

As a result, ML teams could test hypotheses, refine models, and ship features faster. The annotation platform became a core enabler for iterative, data-driven development at scale.

## Conclusion

Spotify’s annotation platform is built on a clear principle: scaling machine learning requires more than just more data or larger models.

It depends on structured, high-quality annotations delivered through systems that are efficient, adaptable, and integrated into the full model development lifecycle. Relying entirely on human labor can create bottlenecks. On the other hand, full automation without oversight can lead to quality drift. Real leverage comes from combining both, with humans providing context and judgment and automation handling volume and repeatability.

By moving from isolated workflows to a unified platform, Spotify turned annotation into a shared capability rather than a one-time cost. The implementation of standardized roles, modular tools, and consistent infrastructure allowed ML teams to build and iterate faster without rebuilding pipelines from scratch.

This approach supports fast experimentation and scaling across a wide range of use cases.

**References:**

- [How We Generated Millions of Content Annotations](https://substack.com/redirect/252af4af-c6b5-4805-8f16-2b60dfd6a54b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

---

© 2025 ByteByteGo  
548 Market Street PMB 72296, San Francisco, CA 94104
```

<END_EXAMPLE_OUTPUT>

## EXAMPLE 2:

### Input newsletter

<START_EXAMPLE_INPUT>

```md
![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNjIxMTUzMDE2LjMuNWZmMWI1YTJhNDIwOGQ3N0BtZy1kMS5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQxLnN1YnN0YWNrLmNvbSIsInAiOjE2NjQxODQxOSwidCI6Im5ld3NsZXR0ZXIiLCJhIjoiZXZlcnlvbmUiLCJzIjo4MTcxMzIsImMiOiJwb3N0IiwiZiI6dHJ1ZSwicG9zaXRpb24iOiJ0b3AiLCJpYXQiOjE3NTA1MjA2NzgsImV4cCI6MTc1MzExMjY3OCwiaXNzIjoicHViLTAiLCJzdWIiOiJlbyJ9.v1XGsnmEBetGxQ7kKjx53BLYWBs8RdP_G0gx1nYT0Dw)

What else will you add to understand these concepts better?

͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­͏     ­

Forwarded this email? [Subscribe here](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj01czgzb3ombmV4dD1odHRwcyUzQSUyRiUyRmJsb2cuYnl0ZWJ5dGVnby5jb20lMkZwJTJGZXAxNjgtYWktdnMtbWFjaGluZS1sZWFybmluZy12cy1kZWVwIiwicCI6MTY2NDE4NDE5LCJzIjo4MTcxMzIsImYiOnRydWUsInUiOjM0OTczODE2MywiaWF0IjoxNzUwNTIwNjc3LCJleHAiOjIwNjYwOTY2NzcsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.UW1oXxKYgG3ro5Ve-JiAzgbQWPQ3uGuC5wjkMqwdfSY?) for more

# [EP168: AI Vs Machine Learning Vs Deep Learning Vs Generative AI](https://substack.com/app-link/post?publication_id=817132&post_id=166418419&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NjQxODQxOSwiaWF0IjoxNzUwNTIwNjc3LCJleHAiOjE3NTMxMTI2NzcsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.yHHWjRmx1OcctV9LYH0vQm3obfZiDZwxlQkZ_HL8DIg)

[ByteByteGo](https://substack.com/@bytebytego399569)

Jun 21

[![](https://substackcdn.com/image/fetch/$s_!U1Ej!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9941c68-e5b7-4b93-be75-df7cc4ffef02_504x540.png)](https://substack.com/@bytebytego399569)

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=817132&post_id=166418419&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NjQxODQxOSwicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTA1MjA2NzcsImV4cCI6MTc1MzExMjY3NywiaXNzIjoicHViLTgxNzEzMiIsInN1YiI6InJlYWN0aW9uIn0.JYYOQ0d29EIg1Q8eBeEWqtwIQxFLZY3YsfuKedKMskg&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=817132&post_id=166418419&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NjQxODQxOSwiaWF0IjoxNzUwNTIwNjc3LCJleHAiOjE3NTMxMTI2NzcsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.yHHWjRmx1OcctV9LYH0vQm3obfZiDZwxlQkZ_HL8DIg&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=817132&post_id=166418419&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NjQxODQxOSwiaWF0IjoxNzUwNTIwNjc3LCJleHAiOjE3NTMxMTI2NzcsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.yHHWjRmx1OcctV9LYH0vQm3obfZiDZwxlQkZ_HL8DIg)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL2VwMTY4LWFpLXZzLW1hY2hpbmUtbGVhcm5pbmctdnMtZGVlcD91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9NXM4M296JnRva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTmpReE9EUXhPU3dpYVdGMElqb3hOelV3TlRJd05qYzNMQ0psZUhBaU9qRTNOVE14TVRJMk56Y3NJbWx6Y3lJNkluQjFZaTA0TVRjeE16SWlMQ0p6ZFdJaU9pSndiM04wTFhKbFlXTjBhVzl1SW4wLnlISFdqUm14MU9jY3RWOUxZSDB2UW0zb2JmWmlEWnd4bFFrWl9ITDhESWciLCJwIjoxNjY0MTg0MTksInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTA1MjA2NzcsImV4cCI6MjA2NjA5NjY3NywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.Vki1Jne8althNDFWHOV1sDw7ynFDSJruHOeegRC3VFk?&utm_source=substack&utm_medium=email)

[READ IN APP![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://open.substack.com/pub/bytebytego/p/ep168-ai-vs-machine-learning-vs-deep?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app)

## [✂️ Cut your QA cycles down to minutes with QA Wolf (Sponsored)](https://substack.com/redirect/071ff710-8644-4b48-a90f-7ea9bf7b8aa7?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

[![](https://substackcdn.com/image/fetch/$s_!8Exm!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2bd360c2-1c26-4bd2-bc83-331ffa351bad_1600x840.png)](https://substack.com/redirect/aa604fbe-692d-4bb3-ba7a-d344bc753297?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

If slow QA processes bottleneck you or your software engineering team and you’re releasing slower because of it — you need to check out QA Wolf.

QA Wolf’s AI-native service **supports web and mobile apps**, delivering [80% automated test coverage in weeks](https://substack.com/redirect/8c242175-3b73-43ed-8e59-a09724f52279?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) and helping teams **ship 5x faster** by reducing QA cycles to minutes.

[QA Wolf](https://substack.com/redirect/49232caa-895f-4274-ae1c-55abc2821ba1?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) takes testing off your plate. They can get you:

- Unlimited parallel test runs for mobile and web apps
- 24-hour maintenance and on-demand test creation
- Human-verified bug reports sent directly to your team
- Zero flakes guarantee

The benefit? No more manual E2E testing. No more slow QA cycles. No more bugs reaching production.

With QA Wolf, [Drata’s team of 80+ engineers](https://substack.com/redirect/355ed39c-9784-41d6-bdc6-bd8e4d3f1ea2?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) achieved 4x more test cases and **86% faster QA cycles**.

[Schedule a demo to learn more](https://substack.com/redirect/10a6f3d9-c704-474e-bd1b-bcb3b14c7f54?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

---

This week’s system design refresher:

- AI Vs Machine Learning Vs Deep Learning Vs Generative AI
- How SQL Query Executes In A Database?
- Top 20 AI Agent Concepts You Should Know
- How RabbitMQ Works
- Hiring Now
- SPONSOR US

---

## AI Vs Machine Learning Vs Deep Learning Vs Generative AI

[![Image](https://substackcdn.com/image/fetch/$s_!p-hZ!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7ffd47f-3549-452e-bfef-07dec0b31086_2360x2824.jpeg "Image")](https://substack.com/redirect/aaa3c952-0259-415b-9214-8a74cfd40101?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

1. Artificial Intelligence (AI)  
   It is the overarching field focused on creating machines or systems that can perform tasks typically requiring human intelligence, such as reasoning, learning, problem-solving, and language understanding. AI consists of various subfields, including ML, NLP, Robotics, and Computer Vision
2. Machine Learning (ML)  
   It is a subset of AI that focuses on developing algorithms that enable computers to learn from and make decisions based on data.

   Instead of being explicitly programmed for every task, ML systems improve their performance as they are exposed to more data. Common applications include spam detection, recommendation systems, and predictive analytics.

3. Deep Learning  
   It is a specialized subset of ML that utilizes artificial neural networks with multiple layers to model complex patterns in data.

   Neural networks are computational models inspired by the human brain’s network of neurons. Deep neural networks can automatically discover representations needed for future detection. Use cases include image and speech recognition, NLP, and autonomous vehicles.

4. Generative AI  
   It refers to AI systems capable of generating new content, such as text, images, music, or code, that resembles the data they were trained on. They rely on the Transformer Architecture.

   Notable generative AI models include GPT for text generation and DALL-E for image creation.

Over to you: What else will you add to understand these concepts better?

---

## [Level Up Your API Stack with Postman (Sponsored)](https://substack.com/redirect/685041d4-b3b3-4c56-900c-27900616837e?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

[![](https://substackcdn.com/image/fetch/$s_!5DQS!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bbcc64-a802-4fb3-8db2-1cd031aba3a0_1570x830.png)](https://substack.com/redirect/685041d4-b3b3-4c56-900c-27900616837e?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Your API workflow is changing whether you like it or not. Postman just dropped features built by devs like you to help you stay ahead of the game.

Postman’s POST/CON 25 product reveals include real-time production visibility with Insights, tighter spec workflows with Spec Hub + GitHub Sync, and AI-assisted debugging that actually works.

Think native integrations that plug directly into your stack—VS Code, GitHub, Slack—plus workflow orchestration without infrastructure headaches.

Get the full technical breakdown and see what your API development could look like.

[Get all the details](https://substack.com/redirect/685041d4-b3b3-4c56-900c-27900616837e?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

---

## How SQL Query Executes In A Database?

[![Image](https://substackcdn.com/image/fetch/$s_!4G09!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ceb221a-ba89-4ebc-9813-4bbb85277287_2360x2770.png "Image")](https://substack.com/redirect/56bc49cb-5e76-4172-93a4-f6b75e65841c?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

STEP 1  
The query string first reaches the Transport Subsystem of the database. This subsystem manages the connection with the client. Also, it performs authentication and authorization checks, and if everything looks fine, it lets the query go to the next step.

STEP 2  
The query now reaches the Query Processor subsystem, which has two parts: Query Parser and Query Optimizer.

The Query Parser breaks down the query into sub-parts (such as SELECT, FROM, WHERE). It checks for any syntax errors and creates a parse tree.

Then, the Query Optimizer goes through the parse tree, checks for semantic errors (for example, if the “users” table exists or not), and finds out the most efficient way to execute the query.

The output of this step is the execution plan.

STEP 3  
The execution plan goes to the Execution Engine. This plan is made up of all the steps needed to execute the query.

The Execution Engine takes this plan and coordinates the execution of each step by calling the Storage Engine. It also collects the results from each step and returns a combined or unified response to the upper layer.

STEP 4  
The Execution Engine sends low-level read and write requests to the Storage Engine based on the execution plan.

This is handled by the various components of the Storage Engine, such as the transaction manager (for transaction management), lock manager (acquires necessary locks), buffer manager (checks if data pages are in memory), and recovery manager (for rollback or recovery).

Over to you: What else will you add to understand the execution of an SQL Query?

---

## Top 20 AI Agent Concepts You Should Know

[![Image](https://substackcdn.com/image/fetch/$s_!Iv-q!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa662e8-5138-4b1a-a5dc-97921d7ea85d_2360x3028.png "Image")](https://substack.com/redirect/314aea6b-e11d-414b-add7-55514ecde103?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

1.  Agent: An autonomous entity that perceives, reasons, and acts in an environment to achieve goals.
2.  Environment: The surrounding context or sandbox in which the agent operates and interacts.
3.  Perception: The process of interpreting sensory or environmental data to build situational awareness.
4.  State: The agent’s current internal condition or representation of the world.
5.  Memory: Storage of recent or historical information for continuity and learning.
6.  Large Language Models: Foundation models powering language understanding and generation.
7.  Reflex Agent: A simple type of agent that makes decisions based on predefined “condition-action” rules.
8.  Knowledge Base: Structured or unstructured data repository used by agents to inform decisions.
9.  CoT (Chain of Thought): A reasoning method where agents articulate intermediate steps for complex tasks.
10. ReACT: A framework that combines step-by-step reasoning with direct environmental actions.
11. Tools: APIs or external systems that agents use to augment their capabilities.
12. Action: Any task or behavior executed by the agent as a result of its reasoning.
13. Planning: Devising a sequence of actions to reach a specific goal.
14. Orchestration: Coordinating multiple steps, tools, or agents to fulfill a task pipeline.
15. Handoffs: The transfer of responsibilities or tasks between different agents.
16. Multi-Agent System: A framework where multiple agents operate and collaborate in the same environment.
17. Swarm: Emergent intelligent behavior from many agents following local rules without central control.
18. Agent Debate: A mechanism where agents argue opposing views to refine or improve outcomes.
19. Evaluation: Measuring the effectiveness or success of an agent’s actions and outcomes.
20. Learning Loop: The cycle where agents improve performance by continuously learning from feedback or outcomes.

Over to you: Which other AI agent concept will you add to the list?

---

## How RabbitMQ Works?

RabbitMQ is a message broker that enables applications to communicate by sending and receiving messages through queues. It helps decouple services, improve scalability, and handle asynchronous processing efficiently.

[![Image](https://substackcdn.com/image/fetch/$s_!LKGF!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa326735a-320e-4476-af4b-ea9856ff25da_2360x2770.png "Image")](https://substack.com/redirect/a54517e3-8bb2-4ebf-b508-cfd5ef4350c4?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Here’s how it works:

1. A producer (usually an application or service) sends messages to the RabbitMQ broker, which manages message routing and delivery.
2. Within the broker, messages are sent to an exchange, which determines how they should be routed based on the type of exchange: Direct, Topic, or Fanout.
3. Bindings connect exchanges to queues using a binding key, which defines the rules for routing messages (for example, exact match or pattern-based)
4. Direct exchanges route messages to queues that match the routing key exactly, as shown with Queue 1.
5. Topic exchanges use patterns to route messages to matching queues.
6. Fanout exchanges broadcast messages to all bound queues, regardless of routing keys.
7. Finally, messages are pulled from the queues by a consumer, which processes them and can pass the results to other systems.

Over to you: What else will you add to the RabbitMQ process flow?

---

## Hiring Now

We collaborate with [Jobright.ai](https://substack.com/redirect/e6cdc740-9d66-497d-b87f-6358f40afccb?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) (an AI job search copilot trusted by 500K+ tech professionals) to curate this job list.

**This Week’s High-Impact Roles at Fast-Growing AI Startups**

- [Senior / Staff Software Engineer, Data Platform](https://substack.com/redirect/d1879c15-dacb-4606-9cc0-c9c051feb0d9?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Waabi (California, USA)

  - Yearly: 155000 - 240000
  - Waabi is an artificial intelligence company that develops autonomous driving technology for the transportation sector.

- [Senior Full Stack Engineer](https://substack.com/redirect/b8d0c896-e176-4293-900f-e98f85606b6c?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Proton.ai (US)

  - Yearly: 60000 - 90000
  - Proton.ai is an AI-powered sales platform for distributors to gain millions of revenue and reclaim market share.

- [Software Engineer - Frontend UI](https://substack.com/redirect/c4be44a1-8600-4a24-af18-5f741cf1df62?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Luma AI (Palo Alto, CA)

  - Yearly: 220K - 280K
  - Luma AI is a generative AI startup that enables users to transform text descriptions into corresponding 3D models.

**High Salary SWE Roles this week**

- [Principal Engine Engineer, Avatar Systems](https://substack.com/redirect/901266a6-8f99-480d-a82c-aedeff7eae58?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Roblox (San Mateo, CA)

  - Yearly: 289460 - 338270

- [Director of Engineering - AWS Applied AI Solutions](https://substack.com/redirect/dab9a802-3081-480b-9960-fd7868b5f0aa?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Amazon Web Services (Seattle, WA)

  - Yearly: 264100 - 350000

- [Manager, Software Engineering - Interactive Foundations](https://substack.com/redirect/0841a8ba-70a0-4461-8798-fd642b09f6e1?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Figma (New York, NY)

  - Yearly: 250000 - 350000

**Today’s latest ML positions**

- [Applied Machine Learning Engineer - Causal Inference Recommendation](https://substack.com/redirect/3f7d41e7-d9e6-47eb-8679-2ca7f34cc595?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at DoorDash (Sunnyvale, CA)

  - Yearly: 137100 - 201600

- [Lead Machine Learning Engineer](https://substack.com/redirect/d1284c92-5411-4ff4-a0d9-74c1ece834ce?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Adobe (New York, NY)

  - Yearly: 162000 - 301200

- [Lead Machine Learning Engineer](https://substack.com/redirect/b924f9d9-6a9a-4f86-bda2-bdc6c211c1bc?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at ESPN (New York, NY)

  - Yearly: 175800 - 235700

---

## **SPONSOR US**

Get your product in front of more than 1,000,000 tech professionals.

Our newsletter puts your products and services directly in front of an audience that matters - hundreds of thousands of engineering leaders and senior engineers - who have influence over significant tech decisions and big purchases.

Space Fills Up Fast - Reserve Today

Ad spots typically sell out about 4 weeks in advance. To ensure your ad reaches this influential audience, reserve your space now by emailing **sponsorship@bytebytego.com.**

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Like](https://substack.com/app-link/post?publication_id=817132&post_id=166418419&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NjQxODQxOSwicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTA1MjA2NzcsImV4cCI6MTc1MzExMjY3NywiaXNzIjoicHViLTgxNzEzMiIsInN1YiI6InJlYWN0aW9uIn0.JYYOQ0d29EIg1Q8eBeEWqtwIQxFLZY3YsfuKedKMskg&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Comment](https://substack.com/app-link/post?publication_id=817132&post_id=166418419&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NjQxODQxOSwiaWF0IjoxNzUwNTIwNjc3LCJleHAiOjE3NTMxMTI2NzcsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.yHHWjRmx1OcctV9LYH0vQm3obfZiDZwxlQkZ_HL8DIg&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Restack](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvYnl0ZWJ5dGVnby9wL2VwMTY4LWFpLXZzLW1hY2hpbmUtbGVhcm5pbmctdnMtZGVlcD91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9NXM4M296JnRva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTmpReE9EUXhPU3dpYVdGMElqb3hOelV3TlRJd05qYzNMQ0psZUhBaU9qRTNOVE14TVRJMk56Y3NJbWx6Y3lJNkluQjFZaTA0TVRjeE16SWlMQ0p6ZFdJaU9pSndiM04wTFhKbFlXTjBhVzl1SW4wLnlISFdqUm14MU9jY3RWOUxZSDB2UW0zb2JmWmlEWnd4bFFrWl9ITDhESWciLCJwIjoxNjY0MTg0MTksInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTA1MjA2NzcsImV4cCI6MjA2NjA5NjY3NywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.Vki1Jne8althNDFWHOV1sDw7ynFDSJruHOeegRC3VFk?&utm_source=substack&utm_medium=email)

© 2025 ByteByteGo  
548 Market Street PMB 72296, San Francisco, CA 94104  
[Unsubscribe](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9ibG9nLmJ5dGVieXRlZ28uY29tL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTmpReE9EUXhPU3dpYVdGMElqb3hOelV3TlRJd05qYzNMQ0psZUhBaU9qRTNPREl3TlRZMk56Y3NJbWx6Y3lJNkluQjFZaTA0TVRjeE16SWlMQ0p6ZFdJaU9pSmthWE5oWW14bFgyVnRZV2xzSW4wLm5kVzc2NDMyZ0RKQzcyLUdyQUtFOGYzckhkY0JLczdoSVBadXQ0RnFYOFEiLCJwIjoxNjY0MTg0MTksInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTA1MjA2NzcsImV4cCI6MjA2NjA5NjY3NywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.0geUId3fXxoecZW4sN_4Ty5JXsNHNtKdzklbFOpGEN0?)

[![Get the app](https://substackcdn.com/image/fetch/$s_!IzGP!,w_262,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fgeneric-app-button%402x.png)](https://substack.com/redirect/13a7e568-552f-47db-b1c0-8f26e87a0482?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)[![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1zdW1pdHVwLmRldkBnbWFpbC5jb20mcj01czgzb3oiLCJwIjoxNjY0MTg0MTksInMiOjgxNzEzMiwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTA1MjA2NzcsImV4cCI6MjA2NjA5NjY3NywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.d69lyWvpdrG5ZQkfAzr8s_7ChUyf08mn9fBxjHWfGEI?)

![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNjIxMTUzMDE2LjMuNWZmMWI1YTJhNDIwOGQ3N0BtZy1kMS5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQxLnN1YnN0YWNrLmNvbSIsInAiOjE2NjQxODQxOSwidCI6Im5ld3NsZXR0ZXIiLCJhIjoiZXZlcnlvbmUiLCJzIjo4MTcxMzIsImMiOiJwb3N0IiwiZiI6dHJ1ZSwicG9zaXRpb24iOiJib3R0b20iLCJpYXQiOjE3NTA1MjA2NzgsImV4cCI6MTc1MzExMjY3OCwiaXNzIjoicHViLTAiLCJzdWIiOiJlbyJ9.M2NXWOYbKrEux4nbqkLgtyVeqFKAt9ISJDo2v-VuCEY)![](https://email.mg-d1.substack.com/o/eJw8kEluxCAQRU_T7GIxmMELzmIxlB0UAxYUHfn2kbtbWdTmlfT09IND2Gu77Fk7kmjF4qkJioBlWlLJqTKSQHbpWHco0BxCXB3-f7URiyHfFpzmMVDFF9Bq26RmemFahYWazTuYSbKcckkVZ0wKytQkJrltzEvH3cypiVo_Zpr3r8imPnxHF36mUDNJfd0avBIstgHkLl3diAlKAAtPaFctH5yiZUrNzMxseRO8TrAFfvsBiNDIOfwaas6jJLxWKM4fED_i4Y8UHKZabpFhmglOmu0jJxznFOH5mOl-l7zK-vCxZpeK9RfCfXsl-F5ydGi3RMyLFoYpQZ6W_wUAAP__jm54tQ)

![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzAxMTUzMDU3LjMuNTY2YjBiY2E1NjM5ZDZjN0BtZy1kMS5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQxLnN1YnN0YWNrLmNvbSIsInAiOjE2NzAwNzYyMywidCI6Im5ld3NsZXR0ZXIiLCJhIjoiZXZlcnlvbmUiLCJzIjo4MTcxMzIsImMiOiJwb3N0IiwiZiI6dHJ1ZSwicG9zaXRpb24iOiJ0b3AiLCJpYXQiOjE3NTEzODQ4MjUsImV4cCI6MTc1Mzk3NjgyNSwiaXNzIjoicHViLTAiLCJzdWIiOiJlbyJ9.h_lq446Mo75DspReL5XiPVsYgLcjNPIiBcIO4BzezIA)
```

<END_EXAMPLE_INPUT>

### Output cleaned newsletter:

<START_EXAMPLE_OUTPUT>

```md
What else will you add to understand these concepts better?

# [EP168: AI Vs Machine Learning Vs Deep Learning Vs Generative AI](https://substack.com/app-link/post?publication_id=817132&post_id=166418419&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NjQxODQxOSwiaWF0IjoxNzUwNTIwNjc3LCJleHAiOjE3NTMxMTI2NzcsImlzcyI6InB1Yi04MTcxMzIiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.yHHWjRmx1OcctV9LYH0vQm3obfZiDZwxlQkZ_HL8DIg)

[ByteByteGo](https://substack.com/@bytebytego399569)

Jun 21

---

This week’s system design refresher:

- AI Vs Machine Learning Vs Deep Learning Vs Generative AI
- How SQL Query Executes In A Database?
- Top 20 AI Agent Concepts You Should Know
- How RabbitMQ Works
- Hiring Now

---

## AI Vs Machine Learning Vs Deep Learning Vs Generative AI

[![Image](https://substackcdn.com/image/fetch/$s_!p-hZ!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa7ffd47f-3549-452e-bfef-07dec0b31086_2360x2824.jpeg "Image")](https://substack.com/redirect/aaa3c952-0259-415b-9214-8a74cfd40101?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

1. Artificial Intelligence (AI)  
   It is the overarching field focused on creating machines or systems that can perform tasks typically requiring human intelligence, such as reasoning, learning, problem-solving, and language understanding. AI consists of various subfields, including ML, NLP, Robotics, and Computer Vision
2. Machine Learning (ML)  
   It is a subset of AI that focuses on developing algorithms that enable computers to learn from and make decisions based on data.

   Instead of being explicitly programmed for every task, ML systems improve their performance as they are exposed to more data. Common applications include spam detection, recommendation systems, and predictive analytics.

3. Deep Learning  
   It is a specialized subset of ML that utilizes artificial neural networks with multiple layers to model complex patterns in data.

   Neural networks are computational models inspired by the human brain’s network of neurons. Deep neural networks can automatically discover representations needed for future detection. Use cases include image and speech recognition, NLP, and autonomous vehicles.

4. Generative AI  
   It refers to AI systems capable of generating new content, such as text, images, music, or code, that resembles the data they were trained on. They rely on the Transformer Architecture.

   Notable generative AI models include GPT for text generation and DALL-E for image creation.

Over to you: What else will you add to understand these concepts better?

---

## [Level Up Your API Stack with Postman (Sponsored)](https://substack.com/redirect/685041d4-b3b3-4c56-900c-27900616837e?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

[![](https://substackcdn.com/image/fetch/$s_!5DQS!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bbcc64-a802-4fb3-8db2-1cd031aba3a0_1570x830.png)](https://substack.com/redirect/685041d4-b3b3-4c56-900c-27900616837e?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Your API workflow is changing whether you like it or not. Postman just dropped features built by devs like you to help you stay ahead of the game.

Postman’s POST/CON 25 product reveals include real-time production visibility with Insights, tighter spec workflows with Spec Hub + GitHub Sync, and AI-assisted debugging that actually works.

Think native integrations that plug directly into your stack—VS Code, GitHub, Slack—plus workflow orchestration without infrastructure headaches.

Get the full technical breakdown and see what your API development could look like.

[Get all the details](https://substack.com/redirect/685041d4-b3b3-4c56-900c-27900616837e?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

---

## How SQL Query Executes In A Database?

[![Image](https://substackcdn.com/image/fetch/$s_!4G09!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4ceb221a-ba89-4ebc-9813-4bbb85277287_2360x2770.png "Image")](https://substack.com/redirect/56bc49cb-5e76-4172-93a4-f6b75e65841c?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

STEP 1  
The query string first reaches the Transport Subsystem of the database. This subsystem manages the connection with the client. Also, it performs authentication and authorization checks, and if everything looks fine, it lets the query go to the next step.

STEP 2  
The query now reaches the Query Processor subsystem, which has two parts: Query Parser and Query Optimizer.

The Query Parser breaks down the query into sub-parts (such as SELECT, FROM, WHERE). It checks for any syntax errors and creates a parse tree.

Then, the Query Optimizer goes through the parse tree, checks for semantic errors (for example, if the “users” table exists or not), and finds out the most efficient way to execute the query.

The output of this step is the execution plan.

STEP 3  
The execution plan goes to the Execution Engine. This plan is made up of all the steps needed to execute the query.

The Execution Engine takes this plan and coordinates the execution of each step by calling the Storage Engine. It also collects the results from each step and returns a combined or unified response to the upper layer.

STEP 4  
The Execution Engine sends low-level read and write requests to the Storage Engine based on the execution plan.

This is handled by the various components of the Storage Engine, such as the transaction manager (for transaction management), lock manager (acquires necessary locks), buffer manager (checks if data pages are in memory), and recovery manager (for rollback or recovery).

Over to you: What else will you add to understand the execution of an SQL Query?

---

## Top 20 AI Agent Concepts You Should Know

[![Image](https://substackcdn.com/image/fetch/$s_!Iv-q!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3aa662e8-5138-4b1a-a5dc-97921d7ea85d_2360x3028.png "Image")](https://substack.com/redirect/314aea6b-e11d-414b-add7-55514ecde103?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

1.  Agent: An autonomous entity that perceives, reasons, and acts in an environment to achieve goals.
2.  Environment: The surrounding context or sandbox in which the agent operates and interacts.
3.  Perception: The process of interpreting sensory or environmental data to build situational awareness.
4.  State: The agent’s current internal condition or representation of the world.
5.  Memory: Storage of recent or historical information for continuity and learning.
6.  Large Language Models: Foundation models powering language understanding and generation.
7.  Reflex Agent: A simple type of agent that makes decisions based on predefined “condition-action” rules.
8.  Knowledge Base: Structured or unstructured data repository used by agents to inform decisions.
9.  CoT (Chain of Thought): A reasoning method where agents articulate intermediate steps for complex tasks.
10. ReACT: A framework that combines step-by-step reasoning with direct environmental actions.
11. Tools: APIs or external systems that agents use to augment their capabilities.
12. Action: Any task or behavior executed by the agent as a result of its reasoning.
13. Planning: Devising a sequence of actions to reach a specific goal.
14. Orchestration: Coordinating multiple steps, tools, or agents to fulfill a task pipeline.
15. Handoffs: The transfer of responsibilities or tasks between different agents.
16. Multi-Agent System: A framework where multiple agents operate and collaborate in the same environment.
17. Swarm: Emergent intelligent behavior from many agents following local rules without central control.
18. Agent Debate: A mechanism where agents argue opposing views to refine or improve outcomes.
19. Evaluation: Measuring the effectiveness or success of an agent’s actions and outcomes.
20. Learning Loop: The cycle where agents improve performance by continuously learning from feedback or outcomes.

Over to you: Which other AI agent concept will you add to the list?

---

## How RabbitMQ Works?

RabbitMQ is a message broker that enables applications to communicate by sending and receiving messages through queues. It helps decouple services, improve scalability, and handle asynchronous processing efficiently.

[![Image](https://substackcdn.com/image/fetch/$s_!LKGF!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa326735a-320e-4476-af4b-ea9856ff25da_2360x2770.png "Image")](https://substack.com/redirect/a54517e3-8bb2-4ebf-b508-cfd5ef4350c4?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Here’s how it works:

1. A producer (usually an application or service) sends messages to the RabbitMQ broker, which manages message routing and delivery.
2. Within the broker, messages are sent to an exchange, which determines how they should be routed based on the type of exchange: Direct, Topic, or Fanout.
3. Bindings connect exchanges to queues using a binding key, which defines the rules for routing messages (for example, exact match or pattern-based)
4. Direct exchanges route messages to queues that match the routing key exactly, as shown with Queue 1.
5. Topic exchanges use patterns to route messages to matching queues.
6. Fanout exchanges broadcast messages to all bound queues, regardless of routing keys.
7. Finally, messages are pulled from the queues by a consumer, which processes them and can pass the results to other systems.

Over to you: What else will you add to the RabbitMQ process flow?

---

## Hiring Now

We collaborate with [Jobright.ai](https://substack.com/redirect/e6cdc740-9d66-497d-b87f-6358f40afccb?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) (an AI job search copilot trusted by 500K+ tech professionals) to curate this job list.

**This Week’s High-Impact Roles at Fast-Growing AI Startups**

- [Senior / Staff Software Engineer, Data Platform](https://substack.com/redirect/d1879c15-dacb-4606-9cc0-c9c051feb0d9?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Waabi (California, USA)

  - Yearly: 155000 - 240000
  - Waabi is an artificial intelligence company that develops autonomous driving technology for the transportation sector.

- [Senior Full Stack Engineer](https://substack.com/redirect/b8d0c896-e176-4293-900f-e98f85606b6c?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Proton.ai (US)

  - Yearly: 60000 - 90000
  - Proton.ai is an AI-powered sales platform for distributors to gain millions of revenue and reclaim market share.

- [Software Engineer - Frontend UI](https://substack.com/redirect/c4be44a1-8600-4a24-af18-5f741cf1df62?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Luma AI (Palo Alto, CA)

  - Yearly: 220K - 280K
  - Luma AI is a generative AI startup that enables users to transform text descriptions into corresponding 3D models.

**High Salary SWE Roles this week**

- [Principal Engine Engineer, Avatar Systems](https://substack.com/redirect/901266a6-8f99-480d-a82c-aedeff7eae58?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Roblox (San Mateo, CA)

  - Yearly: 289460 - 338270

- [Director of Engineering - AWS Applied AI Solutions](https://substack.com/redirect/dab9a802-3081-480b-9960-fd7868b5f0aa?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Amazon Web Services (Seattle, WA)

  - Yearly: 264100 - 350000

- [Manager, Software Engineering - Interactive Foundations](https://substack.com/redirect/0841a8ba-70a0-4461-8798-fd642b09f6e1?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Figma (New York, NY)

  - Yearly: 250000 - 350000

**Today’s latest ML positions**

- [Applied Machine Learning Engineer - Causal Inference Recommendation](https://substack.com/redirect/3f7d41e7-d9e6-47eb-8679-2ca7f34cc595?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at DoorDash (Sunnyvale, CA)

  - Yearly: 137100 - 201600

- [Lead Machine Learning Engineer](https://substack.com/redirect/d1284c92-5411-4ff4-a0d9-74c1ece834ce?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at Adobe (New York, NY)

  - Yearly: 162000 - 301200

- [Lead Machine Learning Engineer](https://substack.com/redirect/b924f9d9-6a9a-4f86-bda2-bdc6c211c1bc?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) at ESPN (New York, NY)

  - Yearly: 175800 - 235700

---

© 2025 ByteByteGo  
548 Market Street PMB 72296, San Francisco, CA 94104
```

<END_EXAMPLE_OUTPUT>

## Example 3: PATTERN/SECTION TO BE REMOVED REGARDLESS

```md

```
