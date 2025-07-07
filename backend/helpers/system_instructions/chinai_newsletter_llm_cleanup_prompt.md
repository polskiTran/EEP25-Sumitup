# SYSTEM INSTRUCTION (follow strictly):

"You are an newsletter denoiser and cleaner that will help me pre process newsletter content in a markdown format before going to another summary process.
In this step, you are strictly FORBID to add new content or modify content to the input newsletter, you are only allow to REMOVE content from this newsletter that is extra

## Thins you can remove:

    - html tags
    - remove social media link at the end of the newsletter, links that call to upgrade to paid
    -IGNORE that the "Sponsor Us" section, while promotional, is often an integral part of the newsletter's structure and revenue model and it's a standard component that many newsletters include REMOVE THIS SECTION.
    - **HIGHEST PRIORITY:** advert blocks, sponsored/partner messages ("Presented By ...", "Made possible by ...", "Together with ..."). EVERY ARTICLE WITH `(SPONSOR)` IN HEADING SHOULD BE REMOVED.
        - **This also includes any content clearly identified as an advertisement, sponsorship, or promotional material, regardless of its placement or labeling (e.g., "Sponsor", "Paid Post", "Advertisement", "Partnership", "Sponsored Content", and similar clear indicators).**
    - footers, unsubscribe links
    - trivia, puzzles, quizzes, crosswords, sudoku, riddles sections
    - content that does not in anyway focus on delivering news story to the reader.

## Things you can MODIFY:

    - replace every `$` with `\$`
    - replace `&amp;`, `&#8217` with chars
    - Modify markdown headings level so that the level reflects content (highest should be # (categories) then ## (content of that category), etc..)

## Must PRESERVES:

    - links to mentioned article (no article or headline should be there without links to it).
    - Credits to writers and sources
    - Images that are relevant to, referenced in the content of the newsletter

Before every heading, a proper newline must be inserted.

**Output in markdown format. Follow example below**

# EXAMPLE 1

## Input Newsletter:

<START_EXAMPLE_INPUT>

```md
![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzA3MTEwMzIzLjMuNjFmYjY5M2QxN2YwMDViNkBtZy1kMC5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQwLnN1YnN0YWNrLmNvbSIsInAiOjE2NzU1OTM3MCwidCI6Im5ld3NsZXR0ZXIiLCJhIjoiZXZlcnlvbmUiLCJzIjoyNjYwLCJjIjoicG9zdCIsImYiOnRydWUsInBvc2l0aW9uIjoidG9wIiwiaWF0IjoxNzUxODg2NjY3LCJleHAiOjE3NTQ0Nzg2NjcsImlzcyI6InB1Yi0wIiwic3ViIjoiZW8ifQ.H1xjkpqj2tIG5U0M9IqbDZcU9woTn-Nq8drI9B3cjFQ)

Greetings from a world where…

͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­

Forwarded this email? [Subscribe here](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9jaGluYWkuc3Vic3RhY2suY29tL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj01czgzb3ombmV4dD1odHRwcyUzQSUyRiUyRmNoaW5haS5zdWJzdGFjay5jb20lMkZwJTJGY2hpbmFpLTMxOS1jaGluYS1kZXZlbG9wZXItc3VydmV5IiwicCI6MTY3NTU5MzcwLCJzIjoyNjYwLCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTg4NjY2NywiZXhwIjoyMDY3NDYyNjY3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.288yEfIsBVAy2dKtXpHEcbvZkefRpez847NLjn0ryNo?) for more

# [ChinAI #319: China Developer Survey Report (2024)](https://substack.com/app-link/post?publication_id=2660&post_id=167559370&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1OTM3MCwiaWF0IjoxNzUxODg2NjY3LCJleHAiOjE3NTQ0Nzg2NjcsImlzcyI6InB1Yi0yNjYwIiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.mOKAW3IMhmewGN45S3aG50Sw3BfCBH-idO2ShBQBBAI)

[Jeffrey Ding](https://substack.com/@chinai)

Jul 7

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=2660&post_id=167559370&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1OTM3MCwicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTE4ODY2NjcsImV4cCI6MTc1NDQ3ODY2NywiaXNzIjoicHViLTI2NjAiLCJzdWIiOiJyZWFjdGlvbiJ9.uFXFJnaKfeQt1qa25VC1YrXxeC3P5-6E2Z49reg04A8&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=2660&post_id=167559370&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1OTM3MCwiaWF0IjoxNzUxODg2NjY3LCJleHAiOjE3NTQ0Nzg2NjcsImlzcyI6InB1Yi0yNjYwIiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.mOKAW3IMhmewGN45S3aG50Sw3BfCBH-idO2ShBQBBAI&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=2660&post_id=167559370&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1OTM3MCwiaWF0IjoxNzUxODg2NjY3LCJleHAiOjE3NTQ0Nzg2NjcsImlzcyI6InB1Yi0yNjYwIiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.mOKAW3IMhmewGN45S3aG50Sw3BfCBH-idO2ShBQBBAI)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvY2hpbmFpL3AvY2hpbmFpLTMxOS1jaGluYS1kZXZlbG9wZXItc3VydmV5P3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj01czgzb3omdG9rZW49ZXlKMWMyVnlYMmxrSWpvek5EazNNemd4TmpNc0luQnZjM1JmYVdRaU9qRTJOelUxT1RNM01Dd2lhV0YwSWpveE56VXhPRGcyTmpZM0xDSmxlSEFpT2pFM05UUTBOemcyTmpjc0ltbHpjeUk2SW5CMVlpMHlOall3SWl3aWMzVmlJam9pY0c5emRDMXlaV0ZqZEdsdmJpSjkubU9LQVczSU1obWV3R040NVMzYUc1MFN3M0JmQ0JILWlkTzJTaEJRQkJBSSIsInAiOjE2NzU1OTM3MCwicyI6MjY2MCwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTE4ODY2NjcsImV4cCI6MjA2NzQ2MjY2NywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.aMqmrcOf6jekw6kY59FdMgk1r1w7BfANRH5-6zxnpzk?&utm_source=substack&utm_medium=email)

[READ IN APP![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://open.substack.com/pub/chinai/p/chinai-319-china-developer-survey?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app)

Greetings from a world where…

buffets and JazzFest in Iowa City are the best way to celebrate the Fourth

…As always, the searchable archive of all past issues is [**here**](https://substack.com/redirect/1b069e6d-fcb5-48a4-a0a7-9418f1413285?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8). Please please [**subscribe here**](https://substack.com/redirect/2f542220-ef07-4004-913f-e9eacfedd3cd?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) to support ChinAI under a _Guardian_/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).

## **Feature Translation: [The 2024 China Developer Survey Report is here!](https://substack.com/redirect/eebf54b9-3af5-47e9-b2fc-927f8e704d01?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

**Context:** The China Software Developer Network (CSDN) is the largest software developer community in China, which provides IT news coverage and hosts code — a mix of Stack Overflow, Hacker News, and Github. It has fielded a large-scale annual survey of Chinese developers since 2004, and this 2024 version was published in July 2024. One important methodology note before we delve into 17 pages of findings: Even though CSDN brands this effort as “[**the largest survey covering all types of Chinese developers**](https://substack.com/redirect/27599b00-438e-43e1-9c63-1ce76f83ac0b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)”, it does not share any details about the survey sample, including even the number of total respondents.

- _I have a few inquiries out to get more details about the survey methodology, but if anyone knows folks at CSDN who could give clarification, please let me know._
- _CSDN has also been [**accused**](https://substack.com/redirect/a928fedf-aa6a-4dee-a65b-3dfe109017b0?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) of copying GitHub projects to its own site in ways that go against open-source._

\*Again, before we get into the data, take these findings as rough temperature gauges, rather than a national representative sample of Chinese developers — and I’ll update this post if we get clarification on the methodology.

**Key Takeaways: In terms of basic demographics of developers, 72% of respondents were under the age of 30, and only 49% said that their salary had increased in the past year.**

- While young developers are still the main force, the proportion of developers over 30 actually increased compared with past years, which suggests a somewhat improved situation for this “job that relies on youth” \[青春饭]. Men made up 84% of respondents under the age of 30.
- There’s been some stagnation of salaries, though some of this could be attributed to more developers moving to lower cost-of-living cities. From the report: “_49% of developers said that their salary has increased in the past year, while the figure was 51% in 2023 and 62% in 2022_.”

**A day in the working life of a Chinese developer involves spending less than half of one’s time writing code.** Interestingly, in the report’s discussion about work habits and involution, they cited a [viral tweet](https://substack.com/redirect/957a54da-8917-48a2-8eeb-2d5787801763?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) from OpenAI developer Jason Wei about his daily schedule (which was meant to be satirical).

- Nearly 80% of respondents said that code-writing time is less than half of their overall working time. 74% of developers write less than 300 effective lines of code per day.
- ChatGPT is the top chatbot used by Chinese developers (56% of respondents reported that they used it). As the below image shows, Baidu’s ErnieBot, Alibaba’s Tongyi Qianwen, and iFlytek’s SparkDesk follow behind with 48%, 23%, and 12% of developers that report usage, respectively.

|     |                                                                                                                                                                                                                                                                                                                                                                            |     |
| --- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     | [![](https://substackcdn.com/image/fetch/$s_!_dOQ!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0f552d9-695a-43cf-8c2b-c3108797e81d_1080x642.png)](https://substack.com/redirect/00fc2be1-38e5-4717-972a-bbe13df7dd4c?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) |     |

Source: 2024 CSDN China Developer Survey Report; multiple survey items can be selected

- Other top tools used by Chinese developers: MySQL for commercial database; Vue.js for web development frameworks; Alibaba Cloud for container cloud platforms.
- The results for most popular AI coding assistants were surprising. Alibaba’s Tongyi Lingma leads the way (19%) and ChatDev, an open-source tool developed by ModelBest and Tsinghua NLP lab, placed second (14%). GitHub Copilot and OpenAI Codex lagged behind with 9% and 8%, respectively.
- When asked to asses the impact of AI coding assistants on their workload, the plurality of respondents (38%) said it could reduce their workload by 20-40%; very close behind, 35% of respondents said it decreased their workload by just 0-20%.

**Some other trends in the Chinese developer community related to cloud computing and open-source software:**

- The survey investigated attitudes toward “cloud repatriation” \[下云], a process of migrating workloads from a public cloud to an on-premises data center. This trend has not been taken up in China: _“foreign companies have voiced their intention to ‘go off the cloud,’ claiming that the cost of going to the cloud is too high, and some have even built their own servers to reduce costs. However, in China, more than half of the respondents (60%) said they had no experience of ‘going off the cloud.’”_
- Though the open-source environment is growing, only 14% of respondents develop open-source software as their full-time job. Most either participate in open-source on a part-time and spare time basis (35% of respondents) or as freelance developers (34%).
- AI is fueling the growth of China’s open-source software community. It ranks first among open-source tech domain that developer pay attention to (see image below), followed by big data and cloud-native computing.

|     |                                                                                                                                                                                                                                                                                                                                                                           |     |
| --- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
|     | [![](https://substackcdn.com/image/fetch/$s_!ZCxf!,w_498,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc2a6e7d-b16b-43b1-94ba-8a98cb65d5ac_1080x715.png)](https://substack.com/redirect/b159539f-15b0-4405-9a3e-a2b5f68ad104?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) |     |

Source: CSDN 2024 China Developer Survey Report. _Open source technology fields that developers pay attention to (multiple items can be selected)._

**FULL TRANSLATION: [The 2024 China Developer Survey Report is here!](https://substack.com/redirect/eebf54b9-3af5-47e9-b2fc-927f8e704d01?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

## **ChinAI Links (Four to Forward)**

### **Must-read: [Promising Topics for U.S.–China Dialogues on AI Risks and Governance](https://substack.com/redirect/48e31848-511b-4919-ba40-5d816a8afef1?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

How can we foster meaningful cooperation between the US and China on AI risks? This FAccT2025 paper, led by Saad Siddiqui and Lujain Ibrahim, reviewed 40+ Chinese and U.S. documents to map areas of common ground: “_Specifically, using an adapted version of the AI Governance and Regulatory Archive (AGORA) — a comprehensive repository of global AI governance documents — we analyze these materials in their original languages to identify areas of convergence in (1) sociotechnical risk perception and (2) governance approaches. We find strong and moderate overlap in several areas such as on concerns about algorithmic transparency, system reliability, agreement on the importance of inclusive multi-stakeholder engagement, and AI’s role in enhancing safety. These findings suggest that despite strategic competition, there exist concrete opportunities for bilateral U.S.- China cooperation in the development of responsible AI_.”

### **Should-read: [Two Rulings on Fair Use and LLM Training](https://substack.com/redirect/be837723-34be-406e-a0dd-32e110cb06ad?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

Ben Murphy, current GovAI fellow, wrote up some in-depth analysiss on two copyright cases involving Anthropic and Meta’s use of pirated books to train their AI models. Some fascinating details about how Anthropic dealt with concerns about pirating millions of books: “_It then realized that it might have a copyright issue, and proceeded to buy physical copies of books, cut the pages, scan them, and use those transcribed copies for actual training_.”

### **Should-watch: [Can Multinationals Win in China? Lessons from Apple’s Experience](https://substack.com/redirect/22f5cdb4-d591-4d26-ba0b-9a47c328d585?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

CSIS hosted a thoughtful discussion on Patrick McGee’s recent book _Apple in China_. Grateful for the opportunity to provide some thoughts alongside Meg Rithmire and James McGregor.

### **Should-read: [Financial Security: Lian Ping on US Sanctions, SWIFT and De-Dollarisation](https://substack.com/redirect/beaac20c-c873-44e4-8f48-43a7564533bf?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

I found this _Sinification_ post to be really illuminating. Bert Hofman, who was previously Country Director for China at the World Bank, provided some context and scene-setting for the feature translation: Lian Ping, President and Chief Economist, Guangkai Chief Industry Research Institute, on US Sanctions, SWIFT and De-Dollarisation.

## **Thank you for reading and engaging.**

These are Jeff Ding's (sometimes) weekly translations of Chinese-language musings on AI and related topics. Jeff is an Assistant Professor of Political Science at George Washington University.

Check out the archive of all past issues [**here**](https://substack.com/redirect/1b069e6d-fcb5-48a4-a0a7-9418f1413285?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) &amp; please [**subscribe here**](https://substack.com/redirect/2f542220-ef07-4004-913f-e9eacfedd3cd?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) to support ChinAI under a _Guardian_/Wikipedia-style tipping model (everyone gets the same content but those who can pay for a subscription will support access for all).

Also! Listen to narrations of the ChinAI Newsletter in podcast format [**here**](https://substack.com/redirect/927d9af4-02d7-4bf4-a930-356c7da0374a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8).

You're currently a free subscriber to [ChinAI Newsletter](https://substack.com/redirect/2f542220-ef07-4004-913f-e9eacfedd3cd?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8). For the full experience, [upgrade your subscription.](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9jaGluYWkuc3Vic3RhY2suY29tL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZjaGluYWkuc3Vic3RhY2suY29tJTJGcCUyRmNoaW5haS0zMTktY2hpbmEtZGV2ZWxvcGVyLXN1cnZleSZyPTVzODNveiZ0b2tlbj1leUoxYzJWeVgybGtJam96TkRrM016Z3hOak1zSW1saGRDSTZNVGMxTVRnNE5qWTJOeXdpWlhod0lqb3hOelUwTkRjNE5qWTNMQ0pwYzNNaU9pSndkV0l0TWpZMk1DSXNJbk4xWWlJNkltTm9aV05yYjNWMEluMC5PX0lnTGJKZVJ4Uy16S3dGSHA3aDhiUk43ZUs0a0xIQTAxdlZLcGdsWUZnIiwicCI6MTY3NTU5MzcwLCJzIjoyNjYwLCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTg4NjY2NywiZXhwIjoyMDY3NDYyNjY3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.PT8MT3olJqbhCJszkmIvTminO5wEwdViFL8tSwQA8tc?&utm_source=substack&utm_medium=email&utm_content=postcta)

[Upgrade to paid](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9jaGluYWkuc3Vic3RhY2suY29tL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZjaGluYWkuc3Vic3RhY2suY29tJTJGcCUyRmNoaW5haS0zMTktY2hpbmEtZGV2ZWxvcGVyLXN1cnZleSZyPTVzODNveiZ0b2tlbj1leUoxYzJWeVgybGtJam96TkRrM016Z3hOak1zSW1saGRDSTZNVGMxTVRnNE5qWTJOeXdpWlhod0lqb3hOelUwTkRjNE5qWTNMQ0pwYzNNaU9pSndkV0l0TWpZMk1DSXNJbk4xWWlJNkltTm9aV05yYjNWMEluMC5PX0lnTGJKZVJ4Uy16S3dGSHA3aDhiUk43ZUs0a0xIQTAxdlZLcGdsWUZnIiwicCI6MTY3NTU5MzcwLCJzIjoyNjYwLCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTg4NjY2NywiZXhwIjoyMDY3NDYyNjY3LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.PT8MT3olJqbhCJszkmIvTminO5wEwdViFL8tSwQA8tc?&utm_source=substack&utm_medium=email&utm_content=postcta)

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Like](https://substack.com/app-link/post?publication_id=2660&post_id=167559370&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1OTM3MCwicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTE4ODY2NjcsImV4cCI6MTc1NDQ3ODY2NywiaXNzIjoicHViLTI2NjAiLCJzdWIiOiJyZWFjdGlvbiJ9.uFXFJnaKfeQt1qa25VC1YrXxeC3P5-6E2Z49reg04A8&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Comment](https://substack.com/app-link/post?publication_id=2660&post_id=167559370&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1OTM3MCwiaWF0IjoxNzUxODg2NjY3LCJleHAiOjE3NTQ0Nzg2NjcsImlzcyI6InB1Yi0yNjYwIiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.mOKAW3IMhmewGN45S3aG50Sw3BfCBH-idO2ShBQBBAI&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Restack](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvY2hpbmFpL3AvY2hpbmFpLTMxOS1jaGluYS1kZXZlbG9wZXItc3VydmV5P3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY2FtcGFpZ249ZW1haWwtcmVzdGFjay1jb21tZW50JmFjdGlvbj1yZXN0YWNrLWNvbW1lbnQmcj01czgzb3omdG9rZW49ZXlKMWMyVnlYMmxrSWpvek5EazNNemd4TmpNc0luQnZjM1JmYVdRaU9qRTJOelUxT1RNM01Dd2lhV0YwSWpveE56VXhPRGcyTmpZM0xDSmxlSEFpT2pFM05UUTBOemcyTmpjc0ltbHpjeUk2SW5CMVlpMHlOall3SWl3aWMzVmlJam9pY0c5emRDMXlaV0ZqZEdsdmJpSjkubU9LQVczSU1obWV3R040NVMzYUc1MFN3M0JmQ0JILWlkTzJTaEJRQkJBSSIsInAiOjE2NzU1OTM3MCwicyI6MjY2MCwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTE4ODY2NjcsImV4cCI6MjA2NzQ2MjY2NywiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.aMqmrcOf6jekw6kY59FdMgk1r1w7BfANRH5-6zxnpzk?&utm_source=substack&utm_medium=email)

© 2025 Jeffrey Ding  
[Unsubscribe](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9jaGluYWkuc3Vic3RhY2suY29tL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTnpVMU9UTTNNQ3dpYVdGMElqb3hOelV4T0RnMk5qWTNMQ0psZUhBaU9qRTNPRE0wTWpJMk5qY3NJbWx6Y3lJNkluQjFZaTB5TmpZd0lpd2ljM1ZpSWpvaVpHbHpZV0pzWlY5bGJXRnBiQ0o5LmJvZHpud3dsM0hEd3FGOWxfUWNwRzRlRVpST2dmQzRMNExnajROSUtkRm8iLCJwIjoxNjc1NTkzNzAsInMiOjI2NjAsImYiOnRydWUsInUiOjM0OTczODE2MywiaWF0IjoxNzUxODg2NjY3LCJleHAiOjIwNjc0NjI2NjcsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.oLpIEuNijBBVE1H4JJR4OLbKqtKDveXM6CmT9Y9w51U?)

[![Get the app](https://substackcdn.com/image/fetch/$s_!IzGP!,w_262,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fgeneric-app-button%402x.png)](https://substack.com/redirect/1811bb96-e189-47b1-a665-ee5873f51f9d?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)[![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1zdW1pdHVwLmRldkBnbWFpbC5jb20mcj01czgzb3oiLCJwIjoxNjc1NTkzNzAsInMiOjI2NjAsImYiOnRydWUsInUiOjM0OTczODE2MywiaWF0IjoxNzUxODg2NjY3LCJleHAiOjIwNjc0NjI2NjcsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.nlUiKH8taArYYKCQGxW5aFbcMg2qOAwKxzBc7LPpLmk?)

![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzA3MTEwMzIzLjMuNjFmYjY5M2QxN2YwMDViNkBtZy1kMC5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQwLnN1YnN0YWNrLmNvbSIsInAiOjE2NzU1OTM3MCwidCI6Im5ld3NsZXR0ZXIiLCJhIjoiZXZlcnlvbmUiLCJzIjoyNjYwLCJjIjoicG9zdCIsImYiOnRydWUsInBvc2l0aW9uIjoiYm90dG9tIiwiaWF0IjoxNzUxODg2NjY3LCJleHAiOjE3NTQ0Nzg2NjcsImlzcyI6InB1Yi0wIiwic3ViIjoiZW8ifQ.86u2l80an3FEcpp6Rvdajtb9O0Ieb5NuwUfQO20knL4)![](https://email.mg-d0.substack.com/o/eJw80N2uqyAQBeCnKXfHDCKgFzyLGWCw5CgYfrrj2-_YNvt2TWbly3LYaMvlMmeujXmjBAbpGRmuJZ9npbRmdGDc140SFWzkV2x_V6XVMrGnma2D4INfZi_nIEfkCNJyWJag5wmBRTPCKEGD5hzEKAYxKB6sWoTnOgBIqx4THNs_D0PttjZ0_weXDxbrGgq9CaaVTuyGrth9pOTI0IvKldM3jt5wpaVchIZP0q6TTKKfulNrVNjZ7erycfQU27VSQruT_xZ3u0eHLeZ0F41KASum9iO2fg6eXo8JttvxdtVufT4wJuOeMWFk7TNhr1TudzEtWsxcCfYy428AAAD__9nmdog)
```

<END_EXAMPLE_INPUT>

## Ouput Cleaned Newsletter:

<START_EXAMPLE_OUTPUT>

```md
# [ChinAI #319: China Developer Survey Report (2024)](https://substack.com/app-link/post?publication_id=2660&post_id=167559370&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1OTM3MCwiaWF0IjoxNzUxODg2NjY3LCJleHAiOjE3NTQ0Nzg2NjcsImlzcyI6InB1Yi0yNjYwIiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.mOKAW3IMhmewGN45S3aG50Sw3BfCBH-idO2ShBQBBAI)

[Jeffrey Ding](https://substack.com/@chinai)

Jul 7

Greetings from a world where…

buffets and JazzFest in Iowa City are the best way to celebrate the Fourth

…As always, the searchable archive of all past issues is [**here**](https://substack.com/redirect/1b069e6d-fcb5-48a4-a0a7-9418f1413285?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8). Please please [**subscribe here**](https://substack.com/redirect/2f542220-ef07-4004-913f-e9eacfedd3cd?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) to support ChinAI under a _Guardian_/Wikipedia-style tipping model (everyone gets the same content but those who can pay support access for all AND compensation for awesome ChinAI contributors).

## **Feature Translation: [The 2024 China Developer Survey Report is here!](https://substack.com/redirect/eebf54b9-3af5-47e9-b2fc-927f8e704d01?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

**Context:** The China Software Developer Network (CSDN) is the largest software developer community in China, which provides IT news coverage and hosts code — a mix of Stack Overflow, Hacker News, and Github. It has fielded a large-scale annual survey of Chinese developers since 2004, and this 2024 version was published in July 2024. One important methodology note before we delve into 17 pages of findings: Even though CSDN brands this effort as “[**the largest survey covering all types of Chinese developers**](https://substack.com/redirect/27599b00-438e-43e1-9c63-1ce76f83ac0b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)”, it does not share any details about the survey sample, including even the number of total respondents.

- _I have a few inquiries out to get more details about the survey methodology, but if anyone knows folks at CSDN who could give clarification, please let me know._
- _CSDN has also been [**accused**](https://substack.com/redirect/a928fedf-aa6a-4dee-a65b-3dfe109017b0?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) of copying GitHub projects to its own site in ways that go against open-source._

\*Again, before we get into the data, take these findings as rough temperature gauges, rather than a national representative sample of Chinese developers — and I’ll update this post if we get clarification on the methodology.

**Key Takeaways: In terms of basic demographics of developers, 72% of respondents were under the age of 30, and only 49% said that their salary had increased in the past year.**

- While young developers are still the main force, the proportion of developers over 30 actually increased compared with past years, which suggests a somewhat improved situation for this “job that relies on youth” \[青春饭]. Men made up 84% of respondents under the age of 30.
- There’s been some stagnation of salaries, though some of this could be attributed to more developers moving to lower cost-of-living cities. From the report: “_49% of developers said that their salary has increased in the past year, while the figure was 51% in 2023 and 62% in 2022_.”

**A day in the working life of a Chinese developer involves spending less than half of one’s time writing code.** Interestingly, in the report’s discussion about work habits and involution, they cited a [viral tweet](https://substack.com/redirect/957a54da-8917-48a2-8eeb-2d5787801763?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) from OpenAI developer Jason Wei about his daily schedule (which was meant to be satirical).

- Nearly 80% of respondents said that code-writing time is less than half of their overall working time. 74% of developers write less than 300 effective lines of code per day.
- ChatGPT is the top chatbot used by Chinese developers (56% of respondents reported that they used it). As the below image shows, Baidu’s ErnieBot, Alibaba’s Tongyi Qianwen, and iFlytek’s SparkDesk follow behind with 48%, 23%, and 12% of developers that report usage, respectively.

|     |                                                                                                                                                                                                                                                                                                                                                                            |     |
| --- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     | [![](https://substackcdn.com/image/fetch/$s_!_dOQ!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd0f552d9-695a-43cf-8c2b-c3108797e81d_1080x642.png)](https://substack.com/redirect/00fc2be1-38e5-4717-972a-bbe13df7dd4c?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) |     |

Source: 2024 CSDN China Developer Survey Report; multiple survey items can be selected

- Other top tools used by Chinese developers: MySQL for commercial database; Vue.js for web development frameworks; Alibaba Cloud for container cloud platforms.
- The results for most popular AI coding assistants were surprising. Alibaba’s Tongyi Lingma leads the way (19%) and ChatDev, an open-source tool developed by ModelBest and Tsinghua NLP lab, placed second (14%). GitHub Copilot and OpenAI Codex lagged behind with 9% and 8%, respectively.
- When asked to asses the impact of AI coding assistants on their workload, the plurality of respondents (38%) said it could reduce their workload by 20-40%; very close behind, 35% of respondents said it decreased their workload by just 0-20%.

**Some other trends in the Chinese developer community related to cloud computing and open-source software:**

- The survey investigated attitudes toward “cloud repatriation” \[下云], a process of migrating workloads from a public cloud to an on-premises data center. This trend has not been taken up in China: _“foreign companies have voiced their intention to ‘go off the cloud,’ claiming that the cost of going to the cloud is too high, and some have even built their own servers to reduce costs. However, in China, more than half of the respondents (60%) said they had no experience of ‘going off the cloud.’”_
- Though the open-source environment is growing, only 14% of respondents develop open-source software as their full-time job. Most either participate in open-source on a part-time and spare time basis (35% of respondents) or as freelance developers (34%).
- AI is fueling the growth of China’s open-source software community. It ranks first among open-source tech domain that developer pay attention to (see image below), followed by big data and cloud-native computing.

|     |                                                                                                                                                                                                                                                                                                                                                                           |     |
| --- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- |
|     | [![](https://substackcdn.com/image/fetch/$s_!ZCxf!,w_498,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdc2a6e7d-b16b-43b1-94ba-8a98cb65d5ac_1080x715.png)](https://substack.com/redirect/b159539f-15b0-4405-9a3e-a2b5f68ad104?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) |     |

Source: CSDN 2024 China Developer Survey Report. _Open source technology fields that developers pay attention to (multiple items can be selected)._

**FULL TRANSLATION: [The 2024 China Developer Survey Report is here!](https://substack.com/redirect/eebf54b9-3af5-47e9-b2fc-927f8e704d01?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

## **ChinAI Links (Four to Forward)**

### **Must-read: [Promising Topics for U.S.–China Dialogues on AI Risks and Governance](https://substack.com/redirect/48e31848-511b-4919-ba40-5d816a8afef1?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

How can we foster meaningful cooperation between the US and China on AI risks? This FAccT2025 paper, led by Saad Siddiqui and Lujain Ibrahim, reviewed 40+ Chinese and U.S. documents to map areas of common ground: “_Specifically, using an adapted version of the AI Governance and Regulatory Archive (AGORA) — a comprehensive repository of global AI governance documents — we analyze these materials in their original languages to identify areas of convergence in (1) sociotechnical risk perception and (2) governance approaches. We find strong and moderate overlap in several areas such as on concerns about algorithmic transparency, system reliability, agreement on the importance of inclusive multi-stakeholder engagement, and AI’s role in enhancing safety. These findings suggest that despite strategic competition, there exist concrete opportunities for bilateral U.S.- China cooperation in the development of responsible AI_.”

### **Should-read: [Two Rulings on Fair Use and LLM Training](https://substack.com/redirect/be837723-34be-406e-a0dd-32e110cb06ad?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

Ben Murphy, current GovAI fellow, wrote up some in-depth analysiss on two copyright cases involving Anthropic and Meta’s use of pirated books to train their AI models. Some fascinating details about how Anthropic dealt with concerns about pirating millions of books: “_It then realized that it might have a copyright issue, and proceeded to buy physical copies of books, cut the pages, scan them, and use those transcribed copies for actual training_.”

### **Should-watch: [Can Multinationals Win in China? Lessons from Apple’s Experience](https://substack.com/redirect/22f5cdb4-d591-4d26-ba0b-9a47c328d585?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

CSIS hosted a thoughtful discussion on Patrick McGee’s recent book _Apple in China_. Grateful for the opportunity to provide some thoughts alongside Meg Rithmire and James McGregor.

### **Should-read: [Financial Security: Lian Ping on US Sanctions, SWIFT and De-Dollarisation](https://substack.com/redirect/beaac20c-c873-44e4-8f48-43a7564533bf?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)**

I found this _Sinification_ post to be really illuminating. Bert Hofman, who was previously Country Director for China at the World Bank, provided some context and scene-setting for the feature translation: Lian Ping, President and Chief Economist, Guangkai Chief Industry Research Institute, on US Sanctions, SWIFT and De-Dollarisation.

## **Thank you for reading and engaging.**

These are Jeff Ding's (sometimes) weekly translations of Chinese-language musings on AI and related topics. Jeff is an Assistant Professor of Political Science at George Washington University.

Check out the archive of all past issues [**here**](https://substack.com/redirect/1b069e6d-fcb5-48a4-a0a7-9418f1413285?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) &amp; please [**subscribe here**](https://substack.com/redirect/2f542220-ef07-4004-913f-e9eacfedd3cd?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) to support ChinAI under a _Guardian_/Wikipedia-style tipping model (everyone gets the same content but those who can pay for a subscription will support access for all).

Also! Listen to narrations of the ChinAI Newsletter in podcast format [**here**](https://substack.com/redirect/927d9af4-02d7-4bf4-a930-356c7da0374a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8).

© 2025 Jeffrey Ding
```

<END_EXAMPLE_OUTPUT>

# EXAMPLE 2:

## Input Newsletter:

<START_EXAMPLE_INPUT>

```md
Office AI use rises, Gallup finds.

[![](https://link.morningbrew.com/img/683083fb5bc6b6d210091294o0ql5.8gsd/dc5a0370.gif)](http://www.morningbrew.com) ![Advertisement](https://ad.doubleclick.net/ddm/trackimp/N777353.5630320TECHBREW/B32914031.421570664;dc_trk_aid=614157770;dc_trk_cid=227781026;ord=832917322;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=;gdpr=%24;gdpr_consent=%24;ltd=;dc_tdv=1?)

June 23, 2025[View Online](https://links.morningbrew.com/c/ANR?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) | [Sign Up](https://links.morningbrew.com/c/sKe?kid=b7ace59c&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Tech Brew](https://cdn.sanity.io/images/bl383u0v/production/d5b3971d4da6a3131b8dcba6f48df6759e76f381-1350x330.png?w=900&fit=max)](https://links.morningbrew.com/c/6Qv?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

Presented By

[![Fin](https://cdn.sanity.io/images/bl383u0v/production/8b7688fe374ab7d73d5f52c66f312cd98c24091e-245x140.png?w=192&q=100&auto=format)](https://links.morningbrew.com/c/ANS?lp=logo&mbadid=813b88bfffac8c48bc9d0523acaf5d56&mbadv=a&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

**It’s Monday.** News from a recent Gallup survey that in-office AI use is up is perhaps not surprising. And that might seem like nail-biting news amid tech CEOs’ insistence that AI is coming for our jobs, but Gallup also found workers are _not super stressed_ about being replaced. Tech Brew’s Patrick Kulp has deets from the whole report.

**In today’s edition:**

- [AI use at work has almost doubled in the past year, Gallup finds](https://links.morningbrew.com/c/ANT?mblid=0c8c06f5fe03&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
- [A new AI development framework puts civil rights first](https://links.morningbrew.com/c/ANU?mblid=b5bd54ab7430&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
- [Some green tech has Trump DOE support, but mass layoffs could hinder wide adoption, expert says](https://links.morningbrew.com/c/ANV?mblid=f7ca1e3b2cef&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

—_Patrick Kulp, Tricia Crimmins, Annie Saunders_

### AI

# [It’s a trend](https://links.morningbrew.com/c/ANT?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Workers in an office space with surrounded AI patterns.](https://cdn.sanity.io/images/bl383u0v/production/d22dd837e710a5f051bca841a487fca72d859535-1500x1000.jpg?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/ANT?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

_Anna Kim_

ChatGPT and its ilk seem to be taking on ever more work in modern offices.

A [new survey](https://links.morningbrew.com/c/ANW?mblid=27e6eba94804&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) from Gallup finds that AI use at work has been accelerating. Nearly one in five workers now say they use it a few times a week, and 8% of respondents report daily AI interactions. Both those numbers have essentially doubled from Gallup’s first measure in 2023.

But not all workers use AI equally. The surge is mostly among white-collar workers, for one; production and frontline staffers have actually seen a slight dip in usage over the past couple of years (from 11% to 9%). Sectors with the highest concentrations of workers frequently turning to AI included the tech industry (50%), professional services (34%), and finance (32%).

**BYOAI:** Like [other](https://links.morningbrew.com/c/knX?mblid=d29b8c92b826&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) [surveys](https://links.morningbrew.com/c/rOq?mblid=7157563e7858&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) have shown, AI usage among employees has also continued to race ahead of employer planning and leadership on the tech. That can create security headaches and lead to a lack of consistent guidelines for workplaces.

While the number of organizations that have communicated a clear plan for integrating AI improved from 15% to 22% in the past year, “it’s still quite low,” according to Jim Harter, Gallup’s chief scientist of workplace management and well-being.

“\[Organizations] need to be intentional about the planning process, about the training process,” Harter told Tech Brew. “They’ve got to have a plan about how it can best benefit their company and the jobs that they have, and how it can be a companion for efficiency’s sake in those jobs.”

**[Keep reading here](https://links.morningbrew.com/c/ANT?mblid=584b4820f977&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).—PK**

[![](https://cdn.sanity.io/images/bl383u0v/production/cab2ac077d288f7ba1df3571cb0ec28ce8f32b86-357x357.png?w=50&fit=max)](https://links.morningbrew.com/c/ANX?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/7372d7c942cc95144c43e3004730ca0cf8a23025-96x96.png)](https://links.morningbrew.com/c/ANY?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/774271f5d2278014f1af0759475660e1761384eb-357x357.png?w=50&fit=max)](https://links.morningbrew.com/c/ANZ?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

### Presented By Fin

# [**Meet the AI agent transforming customer service**](https://links.morningbrew.com/c/ANS?lp=title&mbadid=813b88bfffac8c48bc9d0523acaf5d56&mbadv=a&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Fin](https://cdn.sanity.io/images/bl383u0v/production/889ce5a0e8db8656ff15db016690b2f0568a278b-2001x1500.jpg?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/ANS?lp=image&mbadid=813b88bfffac8c48bc9d0523acaf5d56&mbadv=a&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

Customer support questions piling up? G2’s #1-rated AI agent for customer service, [Fin, can help with that](https://links.morningbrew.com/c/ANS?lp=text1&mbadid=813b88bfffac8c48bc9d0523acaf5d56&mbadv=a&mblid=10192de63773&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy). Fin resolves up to 86% of customer queries automatically with human-quality answers on any channel in any language, 24/7.

With completely configurable and code-optional setup, Fin can start answering queries quickly and efficiently. [Fin works on any helpdesk](https://links.morningbrew.com/c/ANS?lp=text2&mbadid=813b88bfffac8c48bc9d0523acaf5d56&mbadv=a&mblid=150a0358f469&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) with no migration needed, offering all the benefits of AI-powered support without the hassle of platform changes.

Over 5,000 customer service leaders, including teams at top AI companies like Anthropic, have transformed their support with Fin. It delivered higher CSAT scores and improved operational efficiency—all without scaling their headcount.

[Learn more at fin.ai](https://links.morningbrew.com/c/ANS?lp=text3&mbadid=813b88bfffac8c48bc9d0523acaf5d56&mbadv=a&mblid=346377daa6b5&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).

### AI

# [It’s a right](https://links.morningbrew.com/c/ANU?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Scales of justice graphic on a microchip](https://cdn.sanity.io/images/bl383u0v/production/bcd97eab7094dc63f6a002692574cf74ff027917-6192x4128.jpg?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/ANU?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

_Sakorn Sukkasemsakorn/Getty Images_

With the federal government [backing off](https://links.morningbrew.com/c/vF7?mblid=8d15bd373847&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) AI [safety research](https://links.morningbrew.com/c/vtj?mblid=e64020fcfeb3&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), it could leave a void of standards for risk-proofing AI models.

The Center for Civil Rights and Technology at the Leadership Conference on Civil and Human Rights wants to help fill those needs with a new framework meant to help companies and other orgs design and deploy AI systems with equity in mind.

The [36-page document](https://links.morningbrew.com/c/AN-?mblid=d425342282ba&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) covers each stage of the development process with considerations for protecting the civil rights of marginalized groups, as well as case studies and resources. It’s aimed at companies and investors in “specific sectors that utilize consumer-focused tech,” including those at a particular risk for discrimination, like housing, banking, and healthcare.

“Private industry doesn’t have to wait on Congress or the White House to catch up; they can start implementing this Innovation Framework immediately,” Kostubh “KJ” Bagchi, VP of the Center for Civil Rights and Technology, said in a statement.

Founded in 1950, the Conference is a coalition of national organizations born out of the civil rights movement. The group formed the Center for Civil Rights and Technology as a joint project with its education and research arm in 2023 to advocate specifically around AI and privacy, industry accountability, and broadband access.

The framework’s release came just before Commerce Secretary Howard Lutnick renamed the National Institute for Standards and Technology’s AI Safety Institute to [drop](https://links.morningbrew.com/c/AN_?mblid=0d0a5308b15f&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) the word “safety.” NIST released a [widely](https://links.morningbrew.com/c/n93?mblid=95455182f04d&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) [cited](https://links.morningbrew.com/c/kqp?mblid=8ec070d0b56e&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) AI risk management framework in 2023 under President Biden that faced opposition from some Republicans, including Senator Ted Cruz, who called the org’s AI safety standards “woke.”

**[Keep reading here](https://links.morningbrew.com/c/ANU?mblid=d13407f8fd53&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).—PK**

[![](https://cdn.sanity.io/images/bl383u0v/production/cab2ac077d288f7ba1df3571cb0ec28ce8f32b86-357x357.png?w=50&fit=max)](https://links.morningbrew.com/c/AO0?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/7372d7c942cc95144c43e3004730ca0cf8a23025-96x96.png)](https://links.morningbrew.com/c/AO1?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/774271f5d2278014f1af0759475660e1761384eb-357x357.png?w=50&fit=max)](https://links.morningbrew.com/c/AO2?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

### Together With KPMG Managed Services

[![KPMG Managed Services](https://cdn.sanity.io/images/bl383u0v/production/55ef29d7d992227d93ba36d7880f2746ccb12816-1000x750.png?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/z6C?lp=image&mbadid=9b13dff2f03f94007552161134172db5&mbadv=a&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

**A guide to the tech maze.** New technologies pop up every day. [Learn more](https://links.morningbrew.com/c/z6C?lp=text1&mbadid=9b13dff2f03f94007552161134172db5&mbadv=a&mblid=143ee96237a0&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) about how KPMG helps companies fortify their strategic goals by integrating emerging tech. See how modern managed services serve as a gateway to highly skilled talent that can elevate your tech game.

### GREEN TECH

# [It takes talent](https://links.morningbrew.com/c/ANV?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Nuclear power plant smokestacks emitting us flag](https://cdn.sanity.io/images/bl383u0v/production/30b08f3ba2ef81e1d1fd7253b96b2985252de4ee-1500x1000.jpg?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/ANV?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

_Francis Scialabba_

Republicans in Washington seem to be softening a bit on some facets of green tech: Last month, House Republicans expressed excitement about [geothermal energy](https://links.morningbrew.com/c/ynW?mblid=003d8a1fb877&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) production in a [hearing](https://links.morningbrew.com/c/zbX?mblid=c88969c3d11b&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), and the Trump administration stated its intentions to “usher in a nuclear renaissance” via four executive orders.

But widespread adoption of both geothermal and nuclear will face obstacles due to personnel shortages and a lack of industrial strategy, former Department of Energy Deputy Secretary David Turk told Tech Brew. In the first 100 days of the Trump administration, thousands of DOE employees and scientists were [fired or resigned](https://links.morningbrew.com/c/AO3?mblid=e5d8515baac6&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) as part of a “deferred resignation” program designed to reduce the federal workforce.

“There are some technologies that I think will get attention \[and] should have strong bipartisan support. And then it’s a matter of execution,” Turk said. “You can’t execute on anything, whether it’s a loan program or grant or anything, unless you have really talented people.”

And Turk told Tech Brew that many (though “not all”) of the DOE’s talented workers are no longer with the department, resulting in “about a third less staff.”

**[Keep reading here](https://links.morningbrew.com/c/ANV?mblid=ca9f8d4811c4&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).—TC**

[![](https://cdn.sanity.io/images/bl383u0v/production/cab2ac077d288f7ba1df3571cb0ec28ce8f32b86-357x357.png?w=50&fit=max)](https://links.morningbrew.com/c/AO4?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/7372d7c942cc95144c43e3004730ca0cf8a23025-96x96.png)](https://links.morningbrew.com/c/AO5?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/774271f5d2278014f1af0759475660e1761384eb-357x357.png?w=50&fit=max)](https://links.morningbrew.com/c/AO6?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

### Together With Amazon Web Services

[![Amazon Web Services](https://cdn.sanity.io/images/bl383u0v/production/287da5ce94605049e73c7768be02eb6038b6cca8-1000x750.png?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/AR_?lp=image&mbadid=f9e4f98dfe2c9549e8561316fd15c762&mbadv=a&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

**Old-school security ain’t cuttin’ it.** With application and service environments becoming more and more complex, traditional security practices can struggle to adapt. Fortunately, AWS integrates with Palo Alto Networks’ [VM Series Next-Generation Firewall](https://links.morningbrew.com/c/AR_?lp=text1&mbadid=f9e4f98dfe2c9549e8561316fd15c762&mbadv=a&mblid=99514a435234&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) (NGFW) and App ID functionality for scalable, centralized zero-trust security. [Check out this article](https://links.morningbrew.com/c/AR_?lp=text2&mbadid=f9e4f98dfe2c9549e8561316fd15c762&mbadv=a&mblid=57bd523c1ae9&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) for a technical overview on implementation.

![Resource Roundup banner](https://cdn.sanity.io/images/bl383u0v/production/4799f401808cac0a4fe8a8d4997e119e0c93bd58-1350x330.png?w=800&fit=max)

Level up your career with these resources from our sponsors!

- [**What can AI agents do for core modernization?**](https://links.morningbrew.com/c/AOb?mblid=c15838dc34d4&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

<!--THE END-->

- [**Future-proof your workforce with expert insights on the booming alternative employment landscape. Get the guide.**](https://links.morningbrew.com/c/yLQ?mblid=91315073b176&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

### BITS AND BYTES

**Stat:** 93%. That was the percentage of new US energy projects powered by renewable sources in 2024, Canary Media [reported](https://links.morningbrew.com/c/AO7?mblid=aa18f53767a9&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy). “Meanwhile, construction of new large-scale fossil-gas power plants is constrained by turbine shortages that are unlikely to ease in the near term,” the publication added.

**Quote:** “There’s no one in employment at the moment that is incapable of gaining the skills that will be needed in the economy in the next five years. That is the optimistic way of saying, act now, and you will thrive into the future. Don’t, and I think that some people will be left behind. And that’s what worries me the most.”—[Peter Kyle](https://links.morningbrew.com/c/AO8?mblid=bd2ed16fa07d&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), the UK’s technology secretary, to The Guardian about UK workers needing to “act now” to adopt AI tools

**Read:** [The Clear Cut built an AI platform to change its pricing model](https://links.morningbrew.com/c/AO9?mblid=bcb65d7ee4cd&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) (Revenue Brew)

**Customer support questions piling up?** See how [Fin](https://links.morningbrew.com/c/AOa?mblid=a9ea55be632f&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) can completely transform your [customer experience](https://links.morningbrew.com/c/AOa?mblid=f98590c80923&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), resolving up to 86% of customer queries with human-quality answers on any channel in any language, 24/7.\*

_\*A message from our sponsor._

### SHARE THE BREW

[Share Tech Brew](https://links.morningbrew.com/c/aOH?access_token=1CAffDM1mBsqW8DsMz3ifDsy&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) with your coworkers, acquire free Brew swag, and then make new friends as a result of your fresh Brew swag.

We’re saying we’ll give you free stuff and more friends if you share a link. One link.

[![](https://cdn.sanity.io/images/bl383u0v/production/e8c0d668fd2ce584105a14629f9409b29ddffc91-3840x2160.png?w=640&q=60)](https://links.morningbrew.com/c/aOH?access_token=1CAffDM1mBsqW8DsMz3ifDsy&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

**Your referral count:** 0

[Click to Share](https://links.morningbrew.com/c/aOH?access_token=1CAffDM1mBsqW8DsMz3ifDsy&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

Or copy &amp; paste your referral link to others:  
[emergingtechbrew.com/r/?kid=b7ace59c](https://links.morningbrew.com/c/aOI?kid=b7ace59c&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![](https://cdn.sanity.io/images/bl383u0v/production/365b8a21162a71a71c4190f5b1b6e2acd45a212f-96x96.png)](https://links.morningbrew.com/c/Hl?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/bc850f15719e478323219cbfe24640074ab0c306-96x96.png)](https://links.morningbrew.com/c/Hm?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/4be3fbb7e388adf000065f63e01e069db9fdd60a-96x96.png)](https://links.morningbrew.com/c/Hn?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/6af774b2e94fc201bff9ad736da144c7f1f8468a-96x96.png)](https://links.morningbrew.com/c/Ho?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/ccfbd021e2000f116305d0f75c4e95dbdb2996ba-96x96.png)](https://links.morningbrew.com/c/4du?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [![](https://cdn.sanity.io/images/bl383u0v/production/56835eaa4b1e8e7314950c4862d5dfccc9fc410c-96x96.png)](https://links.morningbrew.com/c/Hq?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

Written by [Patrick Kulp](https://links.morningbrew.com/c/s-Q?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), [Tricia Crimmins](https://links.morningbrew.com/c/sNL?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), and [Annie Saunders](https://links.morningbrew.com/c/sNM?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

Was this email forwarded to you? Sign up [here](https://links.morningbrew.com/c/sKg?kid=b7ace59c&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).

![](https://cdn.sanity.io/images/bl383u0v/production/4dce88cb3b80f3818bbf61d2bb99117943c1b1b8-641x568.png?w=40&fit=max)   Guide → [What is AI?](https://links.morningbrew.com/c/Hu?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

![](https://cdn.sanity.io/images/bl383u0v/production/6a05a5ce61b1d5a7c556fccc6097f1af471be089-530x449.png?w=40&fit=max)   Guide → [What is 5G?](https://links.morningbrew.com/c/Hv?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

**Take The Brew to work**

- Marketers: [Marketing Brew](https://links.morningbrew.com/c/6QP?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
- Corporate: [CFO Brew](https://links.morningbrew.com/c/6QQ?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [HR Brew](https://links.morningbrew.com/c/6QR?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [Revenue Brew](https://links.morningbrew.com/c/yIU?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
- Retailers: [Retail Brew](https://links.morningbrew.com/c/6QT?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
- Healthcare: [Healthcare Brew](https://links.morningbrew.com/c/6QU?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

**Get smarter in just 5 minutes**

- Money &amp; Career: [Money With Katie](https://links.morningbrew.com/c/s4z?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [Bossy](https://links.morningbrew.com/c/s4A?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [Brew Markets](https://links.morningbrew.com/c/s4B?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)   [The Playbook](https://links.morningbrew.com/c/s4C?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

**Interested in podcasts?**

- Check out ours [here](https://links.morningbrew.com/c/s4D?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[ADVERTISE](https://links.morningbrew.com/c/w_v?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) // [CAREERS](https://links.morningbrew.com/c/w_w?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) // [SHOP](https://links.morningbrew.com/c/6QZ?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) // [FAQ](https://links.morningbrew.com/c/6Q_?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

Update your email preferences or unsubscribe [here](https://links.morningbrew.com/c/7sN?access_token=1CAffDM1mBsqW8DsMz3ifDsy&bid=40345241&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).  
View our privacy policy [here](https://links.morningbrew.com/c/6R0?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).
```

<END_EXAMPLE_INPUT>

## Output Cleaned Newsletter:

<START_EXAMPLE_OUTPUT>

```md
Office AI use rises, Gallup finds.

It’s Monday. News from a recent Gallup survey that in-office AI use is up is perhaps not surprising. And that might seem like nail-biting news amid tech CEOs’ insistence that AI is coming for our jobs, but Gallup also found workers are _not super stressed_ about being replaced. Tech Brew’s Patrick Kulp has deets from the whole report.

In today’s edition:

- [AI use at work has almost doubled in the past year, Gallup finds](https://links.morningbrew.com/c/ANT?mblid=0c8c06f5fe03&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
- [A new AI development framework puts civil rights first](https://links.morningbrew.com/c/ANU?mblid=b5bd54ab7430&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
- [Some green tech has Trump DOE support, but mass layoffs could hinder wide adoption, expert says](https://links.morningbrew.com/c/ANV?mblid=f7ca1e3b2cef&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

—_Patrick Kulp, Tricia Crimmins, Annie Saunders_

# AI

## [It's a trend](https://links.morningbrew.com/c/ANT?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Workers in an office space with surrounded AI patterns.](https://cdn.sanity.io/images/bl383u0v/production/d22dd837e710a5f051bca841a487fca72d859535-1500x1000.jpg?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/ANT?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

_Anna Kim_

ChatGPT and its ilk seem to be taking on ever more work in modern offices.

A [new survey](https://links.morningbrew.com/c/ANW?mblid=27e6eba94804&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) from Gallup finds that AI use at work has been accelerating. Nearly one in five workers now say they use it a few times a week, and 8% of respondents report daily AI interactions. Both those numbers have essentially doubled from Gallup’s first measure in 2023.

But not all workers use AI equally. The surge is mostly among white-collar workers, for one; production and frontline staffers have actually seen a slight dip in usage over the past couple of years (from 11% to 9%). Sectors with the highest concentrations of workers frequently turning to AI included the tech industry (50%), professional services (34%), and finance (32%).

**BYOAI:** Like [other](https://links.morningbrew.com/c/knX?mblid=d29b8c92b826&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) [surveys](https://links.morningbrew.com/c/rOq?mblid=7157563e7858&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) have shown, AI usage among employees has also continued to race ahead of employer planning and leadership on the tech. That can create security headaches and lead to a lack of consistent guidelines for workplaces.

While the number of organizations that have communicated a clear plan for integrating AI improved from 15% to 22% in the past year, “it’s still quite low,” according to Jim Harter, Gallup’s chief scientist of workplace management and well-being.

“\[Organizations] need to be intentional about the planning process, about the training process,” Harter told Tech Brew. “They’ve got to have a plan about how it can best benefit their company and the jobs that they have, and how it can be a companion for efficiency’s sake in those jobs.”

[**Keep reading here**](https://links.morningbrew.com/c/ANT?mblid=584b4820f977&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).—PK

# AI

## [It's a right](https://links.morningbrew.com/c/ANU?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Scales of justice graphic on a microchip](https://cdn.sanity.io/images/bl383u0v/production/bcd97eab7094dc63f6a002692574cf74ff027917-6192x4128.jpg?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/ANU?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

_Sakorn Sukkasemsakorn/Getty Images_

With the federal government [backing off](https://links.morningbrew.com/c/vF7?mblid=8d15bd373847&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) AI [safety research](https://links.morningbrew.com/c/vtj?mblid=e64020fcfeb3&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), it could leave a void of standards for risk-proofing AI models.

The Center for Civil Rights and Technology at the Leadership Conference on Civil and Human Rights wants to help fill those needs with a new framework meant to help companies and other orgs design and deploy AI systems with equity in mind.

The [36-page document](https://links.morningbrew.com/c/AN-?mblid=d425342282ba&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) covers each stage of the development process with considerations for protecting the civil rights of marginalized groups, as well as case studies and resources. It’s aimed at companies and investors in “specific sectors that utilize consumer-focused tech,” including those at a particular risk for discrimination, like housing, banking, and healthcare.

“Private industry doesn’t have to wait on Congress or the White House to catch up; they can start implementing this Innovation Framework immediately,” Kostubh “KJ” Bagchi, VP of the Center for Civil Rights and Technology, said in a statement.

Founded in 1950, the Conference is a coalition of national organizations born out of the civil rights movement. The group formed the Center for Civil Rights and Technology as a joint project with its education and research arm in 2023 to advocate specifically around AI and privacy, industry accountability, and broadband access.

The framework’s release came just before Commerce Secretary Howard Lutnick renamed the National Institute for Standards and Technology’s AI Safety Institute to [drop](https://links.morningbrew.com/c/AN_?mblid=0d0a5308b15f&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) the word “safety.” NIST released a [widely](https://links.morningbrew.com/c/n93?mblid=95455182f04d&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) [cited](https://links.morningbrew.com/c/kqp?mblid=8ec070d0b56e&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) AI risk management framework in 2023 under President Biden that faced opposition from some Republicans, including Senator Ted Cruz, who called the org’s AI safety standards “woke.”

[**Keep reading here**](https://links.morningbrew.com/c/ANU?mblid=d13407f8fd53&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).—PK

# GREEN TECH

## [It takes talent](https://links.morningbrew.com/c/ANV?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

[![Nuclear power plant smokestacks emitting us flag](https://cdn.sanity.io/images/bl383u0v/production/30b08f3ba2ef81e1d1fd7253b96b2985252de4ee-1500x1000.jpg?w=1336&q=80&auto=format)](https://links.morningbrew.com/c/ANV?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)

_Francis Scialabba_

Republicans in Washington seem to be softening a bit on some facets of green tech: Last month, House Republicans expressed excitement about [geothermal energy](https://links.morningbrew.com/c/ynW?mblid=003d8a1fb877&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) production in a [hearing](https://links.morningbrew.com/c/zbX?mblid=c88969c3d11b&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), and the Trump administration stated its intentions to “usher in a nuclear renaissance” via four executive orders.

But widespread adoption of both geothermal and nuclear will face obstacles due to personnel shortages and a lack of industrial strategy, former Department of Energy Deputy Secretary David Turk told Tech Brew. In the first 100 days of the Trump administration, thousands of DOE employees and scientists were [fired or resigned](https://links.morningbrew.com/c/AO3?mblid=e5d8515baac6&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) as part of a “deferred resignation” program designed to reduce the federal workforce.

“There are some technologies that I think will get attention \[and] should have strong bipartisan support. And then it’s a matter of execution,” Turk said. “You can’t execute on anything, whether it’s a loan program or grant or anything, unless you have really talented people.”

And Turk told Tech Brew that many (though “not all”) of the DOE’s talented workers are no longer with the department, resulting in “about a third less staff.”

[**Keep reading here**](https://links.morningbrew.com/c/ANV?mblid=ca9f8d4811c4&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy).—TC

# BITS AND BYTES

**Stat:** 93%. That was the percentage of new US energy projects powered by renewable sources in 2024, Canary Media [reported](https://links.morningbrew.com/c/AO7?mblid=aa18f53767a9&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy). “Meanwhile, construction of new large-scale fossil-gas power plants is constrained by turbine shortages that are unlikely to ease in the near term,” the publication added.

**Quote:** “There's no one in employment at the moment that is incapable of gaining the skills that will be needed in the economy in the next five years. That is the optimistic way of saying, act now, and you will thrive into the future. Don't, and I think that some people will be left behind. And that's what worries me the most.”—[Peter Kyle](https://links.morningbrew.com/c/AO8?mblid=bd2ed16fa07d&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), the UK’s technology secretary, to The Guardian about UK workers needing to “act now” to adopt AI tools

**Read:** [The Clear Cut built an AI platform to change its pricing model](https://links.morningbrew.com/c/AO9?mblid=bcb65d7ee4cd&mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy) (Revenue Brew)

Written by [Patrick Kulp](https://links.morningbrew.com/c/s-Q?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), [Tricia Crimmins](https://links.morningbrew.com/c/sNL?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy), and [Annie Saunders](https://links.morningbrew.com/c/sNM?mbcid=40345241.395005&mid=858c9b623cc2711c5f02e0f39af85262&mbuuid=1CAffDM1mBsqW8DsMz3ifDsy)
```

<END_EXAMPLE_OUTPUT>
