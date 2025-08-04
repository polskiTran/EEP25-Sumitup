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

PATTERN TO BE REMOVED REGARDLESS

```md
You're currently a free subscriber to [ChinAI Newsletter](https://substack.substack.com/redirect/492470cd-9cdf-4fe6-8ca5-4ca8a4357bf2?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8). For the full experience, [upgrade your subscription.](https://substack.substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9jaGluYWkuc3Vic3RhY2suY29tL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZjaGluYWkuc3Vic3RhY2suY29tJTJGcCUyRmNoaW5haS0zMjItMTAwLWNhc2VzLW9mLWFpLWRpc2luZm9ybWF0aW9uJnI9NXM4M296JnRva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbWxoZENJNk1UYzFORE13T0RFek1Dd2laWGh3SWpveE56VTJPVEF3TVRNd0xDSnBjM01pT2lKd2RXSXRNalkyTUNJc0luTjFZaUk2SW1Ob1pXTnJiM1YwSW4wLkNTQnN5LWlJd3lOU0tJRVd6Nmk5c1h2Y0ZUdHYyZDNUdDMtSHVWRHBEUVkiLCJwIjoxNzAwNDU0NjcsInMiOjI2NjAsImYiOnRydWUsInUiOjM0OTczODE2MywiaWF0IjoxNzU0MzA4MTMwLCJleHAiOjIwNjk4ODQxMzAsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.TR6l9cb6aaLbwVXCUlldplg5Dv8uE8oBwc-y_tdVEc8?&utm_source=substack&utm_medium=email&utm_content=postcta)

[Upgrade to paid](https://substack.substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9jaGluYWkuc3Vic3RhY2suY29tL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZjaGluYWkuc3Vic3RhY2suY29tJTJGcCUyRmNoaW5haS0zMjItMTAwLWNhc2VzLW9mLWFpLWRpc2luZm9ybWF0aW9uJnI9NXM4M296JnRva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbWxoZENJNk1UYzFORE13T0RFek1Dd2laWGh3SWpveE56VTJPVEF3TVRNd0xDSnBjM01pT2lKd2RXSXRNalkyTUNJc0luTjFZaUk2SW1Ob1pXTnJiM1YwSW4wLkNTQnN5LWlJd3lOU0tJRVd6Nmk5c1h2Y0ZUdHYyZDNUdDMtSHVWRHBEUVkiLCJwIjoxNzAwNDU0NjcsInMiOjI2NjAsImYiOnRydWUsInUiOjM0OTczODE2MywiaWF0IjoxNzU0MzA4MTMwLCJleHAiOjIwNjk4ODQxMzAsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.TR6l9cb6aaLbwVXCUlldplg5Dv8uE8oBwc-y_tdVEc8?&utm_source=substack&utm_medium=email&utm_content=postcta)

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Like](https://substack.com/app-link/post?publication_id=2660&post_id=170045467&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE3MDA0NTQ2NywicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTQzMDgxMzAsImV4cCI6MTc1NjkwMDEzMCwiaXNzIjoicHViLTI2NjAiLCJzdWIiOiJyZWFjdGlvbiJ9.rYBe2948q0siQcLHmGk_HPg6ZLFZxkNP1OvqhTCGf6E&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Comment](https://substack.com/app-link/post?publication_id=2660&post_id=170045467&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE3MDA0NTQ2NywiaWF0IjoxNzU0MzA4MTMwLCJleHAiOjE3NTY5MDAxMzAsImlzcyI6InB1Yi0yNjYwIiwic3ViIjoicG9zdC1yZWFjdGlvbiJ9.N0MyvLm2TBJFnwIE4WJzxp9TfG0ITXafxObKGiC-Xr0&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Restack](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvY2hpbmFpL3AvY2hpbmFpLTMyMi0xMDAtY2FzZXMtb2YtYWktZGlzaW5mb3JtYXRpb24_dXRtX3NvdXJjZT1zdWJzdGFjayZ1dG1fbWVkaXVtPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1yZXN0YWNrLWNvbW1lbnQmYWN0aW9uPXJlc3RhY2stY29tbWVudCZyPTVzODNveiZ0b2tlbj1leUoxYzJWeVgybGtJam96TkRrM016Z3hOak1zSW5CdmMzUmZhV1FpT2pFM01EQTBOVFEyTnl3aWFXRjBJam94TnpVME16QTRNVE13TENKbGVIQWlPakUzTlRZNU1EQXhNekFzSW1semN5STZJbkIxWWkweU5qWXdJaXdpYzNWaUlqb2ljRzl6ZEMxeVpXRmpkR2x2YmlKOS5OME15dkxtMlRCSkZud0lFNFdKenhwOVRmRzBJVFhhZnhPYktHaUMtWHIwIiwicCI6MTcwMDQ1NDY3LCJzIjoyNjYwLCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1NDMwODEzMCwiZXhwIjoyMDY5ODg0MTMwLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.okqahFym5OxttNZmx7R-DOZfM8PNBeY6uyHuKTLcmXk?&utm_source=substack&utm_medium=email)
```
