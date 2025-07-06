# SYSTEM INSTRUCTION (follow strictly):

"You are an newsletter denoiser and cleaner that will help me pre process newsletter content in a markdown format before going to another summary process.
In this step, you are strictly FORBID to add new content or modify content to the input newsletter, you are only allow to REMOVE content from this newsletter that is extra

## Thins you can remove:

    - html tags
    - advert blocks, sponsored/partner messages ("Presented By ...", "Made possible by ...", "Together with ...")
    - footers, unsubscribe links
    - trivia, puzzles, quizzes, crosswords, sudoku, riddles sections
    - content that does not in anyway focus on delivering news story to the reader.

## Things you can MODIFY:

    - Modify markdown headings level so that the level reflects content (highest should be # (categories) then ## (content of that category), etc..)

## Must PRESERVES:

    - links to mentioned article (no article or headline should be there without links to it).
    - Credits to writers and sources
    - Images that are relevant to, referenced in the content of the newsletter

Before every heading, a proper newline must be inserted.

**AT THE VERY END OF THE CLEANING PROCESS, replace every `$` with `\$`, replace `&amp;`, `&#8217` with chars**
**Output in markdown format**

# EXAMPLE 1:

## Input Newsletter:

<START_EXAMPLE_INPUT>

```md
![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzAzMjI1MjI1LjMuZmQwZTNhMTczYTViZDcwOUBtZzIuc3Vic3RhY2suY29tPiIsInUiOjkwOTEwOTEwLCJyIjoidC5hbmh0aWVwMTE0QGdtYWlsLmNvbSIsImQiOiJtZzIuc3Vic3RhY2suY29tIiwicCI6MTY3NDc5MDE1LCJ0IjoibmV3c2xldHRlciIsImEiOiJldmVyeW9uZSIsInMiOjExMDM1OCwiYyI6InBvc3QiLCJmIjp0cnVlLCJwb3NpdGlvbiI6InRvcCIsImlhdCI6MTc1MTU4MzI3MSwiZXhwIjoxNzU0MTc1MjcxLCJpc3MiOiJwdWItMCIsInN1YiI6ImVvIn0.PxvbiPAWu9CR38wkZCNKsQc8-ku1vj_b8jYGLPnTHNw)

Mark Zuckerberg announces his AI ‘superintelligence’ super-group, DeepMind launches AlphaGenome, aiming to predict gene regulation from DNA sequence, and more!

͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­

Forwarded this email? [Subscribe here](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj0xaTRqYjImbmV4dD1odHRwcyUzQSUyRiUyRmxhc3R3ZWVraW4uYWklMkZwJTJGbGFzdC13ZWVrLWluLWFpLTMxNC1tZXRhcy1zdXBlcmludGVsbGlnZW5jZSIsInAiOjE2NzQ3OTAxNSwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1Ijo5MDkxMDkxMCwiaWF0IjoxNzUxNTgzMjcxLCJleHAiOjIwNjcxNTkyNzEsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.zasgkshFEjO2kRTmfXlGtw_pUXE0wJPOUDCMuLpfVQ0?) for more

[![](https://substackcdn.com/image/fetch/$s_!xT4S!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f4944be-2d39-4340-a41c-3ca79f17665a_2400x800.png)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3AvbGFzdC13ZWVrLWluLWFpLTMxNC1tZXRhcy1zdXBlcmludGVsbGlnZW5jZT91dG1fY2FtcGFpZ249ZW1haWwtaGFsZi1wb3N0JnI9MWk0amIyJnRva2VuPWV5SjFjMlZ5WDJsa0lqbzVNRGt4TURreE1Dd2ljRzl6ZEY5cFpDSTZNVFkzTkRjNU1ERTFMQ0pwWVhRaU9qRTNOVEUxT0RNeU56RXNJbVY0Y0NJNk1UYzFOREUzTlRJM01Td2lhWE56SWpvaWNIVmlMVEV4TURNMU9DSXNJbk4xWWlJNkluQnZjM1F0Y21WaFkzUnBiMjRpZlEud1k3aFBEVHloSDg3bEQxNVVLbVB3X21oTTgzeXZfOGxrcHhtM0FkVlBLdyIsInAiOjE2NzQ3OTAxNSwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1Ijo5MDkxMDkxMCwiaWF0IjoxNzUxNTgzMjcxLCJleHAiOjIwNjcxNTkyNzEsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.KpzHXWeUu_xVK1oDNtHfU9-DSXxqEZJl5ONGAr_XTsQ?)

Hello from Last Week in AI! Thank you for being a subscriber :)

If you like our stuff, consider following us on [Twitter](https://substack.com/redirect/8a478c35-ebb9-42ed-84e9-85f220b9ad86?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc), checking out our [podcast](https://substack.com/redirect/ca9d79f2-0594-46c8-afcb-7dc09645c1a6?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc), and sharing the newsletter with friends. Oh, and consider getting a paid subscription.

[Get 20% off forever](https://substack.com/redirect/731052a0-e210-40e8-98f4-7225a4ddf7cd?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

If you would like to become a sponsor for the newsletter, podcast, or both, please fill out [this form](https://substack.com/redirect/78fbff82-0c68-464a-a118-094bc3cfe240?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc).

---

# [Last Week in AI #314 - Meta's Superintelligence hires, AlphaGenome, Gemini CLI](https://substack.com/app-link/post?publication_id=110358&post_id=167479015&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=1i4jb2&token=eyJ1c2VyX2lkIjo5MDkxMDkxMCwicG9zdF9pZCI6MTY3NDc5MDE1LCJpYXQiOjE3NTE1ODMyNzEsImV4cCI6MTc1NDE3NTI3MSwiaXNzIjoicHViLTExMDM1OCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.wY7hPDTyhH87lD15UKmPw_mhM83yv_8lkpxm3AdVPKw)

### Mark Zuckerberg announces his AI ‘superintelligence’ super-group, DeepMind launches AlphaGenome, aiming to predict gene regulation from DNA sequence, and more!

[Last Week in AI](https://substack.com/@lastweekinai)

Jul 3

[![](https://substackcdn.com/image/fetch/$s_!QAnE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ef58ddc-993f-40a5-a130-df80b858aeae_512x512.jpeg)](https://substack.com/@lastweekinai)

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=110358&post_id=167479015&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjo5MDkxMDkxMCwicG9zdF9pZCI6MTY3NDc5MDE1LCJyZWFjdGlvbiI6IuKdpCIsImlhdCI6MTc1MTU4MzI3MSwiZXhwIjoxNzU0MTc1MjcxLCJpc3MiOiJwdWItMTEwMzU4Iiwic3ViIjoicmVhY3Rpb24ifQ.yr9s8dzW58Yb2MJYbvJcagf5s5AX4r4hUeFlRz520Rs&utm_medium=email&utm_campaign=email-reaction&r=1i4jb2)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=110358&post_id=167479015&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjo5MDkxMDkxMCwicG9zdF9pZCI6MTY3NDc5MDE1LCJpYXQiOjE3NTE1ODMyNzEsImV4cCI6MTc1NDE3NTI3MSwiaXNzIjoicHViLTExMDM1OCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.wY7hPDTyhH87lD15UKmPw_mhM83yv_8lkpxm3AdVPKw&r=1i4jb2&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=110358&post_id=167479015&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=1i4jb2&token=eyJ1c2VyX2lkIjo5MDkxMDkxMCwicG9zdF9pZCI6MTY3NDc5MDE1LCJpYXQiOjE3NTE1ODMyNzEsImV4cCI6MTc1NDE3NTI3MSwiaXNzIjoicHViLTExMDM1OCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.wY7hPDTyhH87lD15UKmPw_mhM83yv_8lkpxm3AdVPKw)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbGFzdHdlZWtpbmFpL3AvbGFzdC13ZWVrLWluLWFpLTMxNC1tZXRhcy1zdXBlcmludGVsbGlnZW5jZT91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9MWk0amIyJnRva2VuPWV5SjFjMlZ5WDJsa0lqbzVNRGt4TURreE1Dd2ljRzl6ZEY5cFpDSTZNVFkzTkRjNU1ERTFMQ0pwWVhRaU9qRTNOVEUxT0RNeU56RXNJbVY0Y0NJNk1UYzFOREUzTlRJM01Td2lhWE56SWpvaWNIVmlMVEV4TURNMU9DSXNJbk4xWWlJNkluQnZjM1F0Y21WaFkzUnBiMjRpZlEud1k3aFBEVHloSDg3bEQxNVVLbVB3X21oTTgzeXZfOGxrcHhtM0FkVlBLdyIsInAiOjE2NzQ3OTAxNSwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1Ijo5MDkxMDkxMCwiaWF0IjoxNzUxNTgzMjcxLCJleHAiOjIwNjcxNTkyNzEsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.FfC_p0NECZWnO61YtmVBu63rQ1sowtPQwOyPx_omZus?&utm_source=substack&utm_medium=email)

[READ IN APP![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://open.substack.com/pub/lastweekinai/p/last-week-in-ai-314-metas-superintelligence?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app)

### Top News

#### [Mark Zuckerberg announces his AI ‘superintelligence’ super-group](https://substack.com/redirect/9e37d4f5-171c-46ba-9095-546ee6dc9eed?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

|     |                                                                                                                                                                                                                                                                                                                                                                                           |     |
| --- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     | [![Image](https://substackcdn.com/image/fetch/$s_!2fKl!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44204f7d-36bb-4960-b2e7-6ac5aac0d39d_2048x1311.jpeg "Image")](https://substack.com/redirect/1cfe7166-51c1-48b5-8715-8f9a5bafbd01?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) |     |

Meta CEO Mark Zuckerberg has announced the creation of a new group within the company, the "Meta Superintelligence Labs", which will be responsible for all AI-related work. The group will be led by former Scale AI CEO Alexandr Wang, who recently joined Meta as part of a multibillion-dollar deal, and will be assisted by former GitHub CEO Nat Friedman. In addition, Meta has made 11 new AI-focused hires, including former employees of Anthropic, Google DeepMind, and OpenAI.

Zuckerberg has reportedly been making substantial offers to potential hires, with figures reaching into the eight-figure range, in an effort to boost Meta's AI capabilities, which have been lagging behind other major AI companies. The company has also been in discussions to acquire several AI companies, including Thinking Machines Lab, Perplexity, and Safe Superintelligence, although none of these talks have resulted in formal offers.

More on this:

- [Meta shares hit all-time high as Mark Zuckerberg goes on AI hiring blitz](https://substack.com/redirect/765dacab-ec12-4d72-a328-be7f1227bd39?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [The A.I. Frenzy Is Escalating. Again.](https://substack.com/redirect/11940538-333a-4ad4-8798-2a4e55aca215?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [In Pursuit of Godlike Technology, Mark Zuckerberg Amps Up the A.I. Race](https://substack.com/redirect/f2adfad0-ec26-427e-86c9-b10a2829582a?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Meta hires key OpenAI researcher to work on AI reasoning models](https://substack.com/redirect/1b39478c-fb9d-4e2d-a371-210c7bbe02b8?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Here Is Everyone Mark Zuckerberg Has Hired So Far for Meta’s ‘Superintelligence’ Team](https://substack.com/redirect/dbecebad-5e32-44b5-a50b-9776438ce3a9?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Here’s What Mark Zuckerberg Is Offering Top AI Talent](https://substack.com/redirect/29d68346-f441-4781-97c0-63a3d5714801?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [OpenAI Leadership Responds to Meta Offers: ‘Someone Has Broken Into Our Home’](https://substack.com/redirect/4e0e2641-f87c-4ee5-980c-3e3eb37943bd?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Sam Altman Slams Meta’s AI Talent-Poaching Spree: ‘Missionaries Will Beat Mercenaries’](https://substack.com/redirect/9bce36da-8d65-4960-8c14-1c6f3ea8088f?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

#### [DeepMind launches AlphaGenome, aiming to predict gene regulation from DNA sequence](https://substack.com/redirect/a5769572-0c3e-442f-b088-5f457ed11e5b?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

[![](https://substackcdn.com/image/fetch/$s_!nQkn!,w_1100,h_618,c_fill,f_auto,q_auto:good,fl_progressive:steep/l_play_button_usfui2,w_144,e_colorize:0/https%3A%2F%2Fsubstack-video.s3.amazonaws.com%2Fvideo_upload%2Fpost%2F167479015%2Fff3871fb-221a-43a9-8fa8-38a6ff43d6d0%2Ftranscoded-00001.png)](https://substack.com/redirect/f50564fa-909b-47e5-891d-e054fc018582?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

DeepMind, known for its protein-folding deep learning model AlphaFold, has recently ventured into the complex field of predicting gene regulation from DNA sequences. The company announced its latest model, AlphaGenome, in a preprint and [blog post](https://substack.com/redirect/050c2b55-2080-4a58-93e9-64ab63b3ebf8?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc). This model represents an early step towards potential applications in therapeutic development. Research engineer Natasha Latysheva acknowledges that compared to protein structure prediction, genomics is a more ambiguous field with no single metric of success. As a result, DeepMind is pursuing multiple metrics in its quest to predict gene regulation.

More on this:

- [DeepMind blog - AlphaGenome: AI for better understanding the genome](https://substack.com/redirect/050c2b55-2080-4a58-93e9-64ab63b3ebf8?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Paper - AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](https://substack.com/redirect/d80c4c33-8e3e-439e-9193-18d924c2bb4d?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Google’s new AI will help researchers understand how our genes work](https://substack.com/redirect/8f8499d4-83d3-4ddb-ba5a-07ac819f1422?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

#### [Google is bringing Gemini CLI to developers’ terminals](https://substack.com/redirect/915ce8dd-1405-4bdf-a269-a08bdea24a85?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

|     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
| --- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     | [![Install Google Gemini CLI in Windows for AI Command Line! - Virtualization  Howto](https://substackcdn.com/image/fetch/$s_!iY7t!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3270c8bd-099d-4229-a102-705c2057267c_1113x626.jpeg "Install Google Gemini CLI in Windows for AI Command Line! - Virtualization  Howto")](https://substack.com/redirect/f7c5e938-304b-43e8-95f4-f5c2b3afa821?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) |     |

Google has introduced a new open-source AI agent, Gemini CLI, that brings Gemini's coding, content generation, and research capabilities directly to developers' terminals. The tool is designed to enhance the command line experience, allowing developers to write and debug code using natural language prompts. Gemini CLI uses Google's Gemini 2.5 Pro reasoning model, which supports a 1 million token context window, and is integrated with Gemini Code Assist. It also includes built-in Model Context Protocol (MCP) and Google Search support, and enables developers to generate images and video using Google's Veo and Imagen AI tools.

Gemini CLI is currently available for developers to preview for free through a Gemini Code Assist license that can be obtained via a personal Google account. This license allows users a usage limit of 60 model requests per minute and 1,000 requests per day, which Google claims is the "largest allowance" in the industry.

### Other News

#### Tools

|     |                                                                                                                                                                                                                                                                                                                                                                            |     |
| --- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     | [![](https://substackcdn.com/image/fetch/$s_!hH25!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a9fc78b-6911-44f1-baaa-7c6adb161547_680x390.jpeg)](https://substack.com/redirect/72bad8cf-ef6c-42c1-929e-6ae8e866e67d?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) |     |

[Google embraces AI in the classroom with new Gemini tools for educators, chatbots for students, and more](https://substack.com/redirect/370be2a4-fa3b-41b3-a7a8-cbb17983351c?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Google is enhancing educational experiences by integrating over 30 AI tools, including personalized learning aids and interactive study guides, into classrooms through its Gemini AI suite, aiming to support teachers and students while addressing the challenges posed by AI in education.

[Mayo Clinic’s AI tool identifies 9 dementia types, including Alzheimer’s, with one scan](https://substack.com/redirect/c674e950-115a-42bb-befa-74cab46fdfb0?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Mayo Clinic's AI tool, StateViewer, significantly improves the speed and accuracy of diagnosing nine types of dementia, including Alzheimer's, by analyzing brain activity patterns from a single FDG-PET scan, offering transformative potential for early and precise dementia care.

[Creative Commons debuts CC signals, a framework for an open AI ecosystem](https://substack.com/redirect/66aea329-95c8-4609-81aa-0f8fe9b15c7c?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Creative Commons has introduced CC signals, a project aimed at creating a legal and technical framework to guide the ethical reuse of data for AI training, balancing openness with data protection.

[Baidu releases open source model family ERNIE 4.5](https://substack.com/redirect/d26010e3-a0b4-4db6-bff4-ca367b76310d?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Baidu's decision to open-source its ERNIE 4.5 model family under the Apache 2.0 license marks a strategic shift aimed at fostering global AI development and challenging industry norms set by companies like OpenAI and Anthropic.

[Cloudflare Introduces Default Blocking of A.I. Data Scrapers](https://substack.com/redirect/19f4680e-d82a-4e13-9a28-acfae71692a7?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Cloudflare's new setting allows websites to block AI data scrapers by default, requiring explicit permission for bots to access content, aiming to protect original digital content and influence the AI development landscape.

[Anthropic now lets you make apps right from its Claude AI chatbot](https://substack.com/redirect/fc982cdf-b6e2-4195-9f32-6986377dfd2b?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Anthropic's Claude AI chatbot now includes a beta feature that allows users to create and share AI-powered apps directly within the app, leveraging the Artifacts feature for interactive development and API integration.

[Google's Imagen 4 text-to-image model promises 'significantly improved' boring images](https://substack.com/redirect/dd5e3305-6013-482b-8a10-29edd21f175e?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Google's Imagen 4 and Imagen 4 Ultra models offer improved text-to-image rendering with precise prompt following, though they still produce images that appear machine-generated and lack the charm of competitors like Dall-E and Midjourney.

[Google launches Doppl, a new app that lets you visualize how an outfit might look on you](https://substack.com/redirect/ec299bcc-d44b-41df-a9c2-f8aa751f1052?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Doppl allows users to upload a full-body photo to virtually try on outfits, creating AI-generated images and videos of themselves in different clothes, enhancing personal style exploration and data collection for Google.

#### Business

|     |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
| --- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     | [![A screenshot of a Runway AI game.](https://substackcdn.com/image/fetch/$s_!QCiT!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc4030e33-479d-4ee5-8848-ba1482aecbb8_1469x1846.png "A screenshot of a Runway AI game.")](https://substack.com/redirect/54ab833e-fc61-4106-b61a-7b9b4a0f99a6?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) |     |

[Runway is going to let people generate video games with AI](https://substack.com/redirect/957c85fe-fab1-44a6-8a2e-34a0cd014235?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Runway is expanding its generative AI technology from Hollywood to the gaming industry, aiming to accelerate game development and is in discussions with gaming companies for collaboration and data access.

[OpenAI turns to Google's AI chips to power its products, source says](https://substack.com/redirect/cb2e7f1c-aa20-443b-bf85-9af6c15ae61a?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - OpenAI has started renting Google's tensor processing units (TPUs) to power its products, marking a shift from relying solely on Nvidia GPUs and Microsoft's data centers, while Google expands its cloud business by offering its AI technology to external customers.

[As job losses loom, Anthropic launches program to track AI’s economic fallout](https://substack.com/redirect/1bdd24bd-e250-4ba0-b56c-22f8334fd589?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Anthropic's Economic Futures Program aims to research AI's impact on the labor market and economy, offering grants and hosting symposia to develop policy proposals and track AI's economic effects.

[At Amazon’s Biggest Data Center, Everything Is Supersized for A.I.](https://substack.com/redirect/2d248889-efe6-4671-80a4-dff8d629dc35?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Amazon's new data center complex in Indiana, part of Project Rainier, is designed to support AI development with massive infrastructure and resources, primarily serving the AI start-up Anthropic.

[Alibaba Unveils Latest AI Service for Images in Push for Users](https://substack.com/redirect/06b5338c-7b80-4397-864f-cc2ef4477967?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Alibaba's new AI service, Qwen VLo, enhances user experience by enabling text-to-image and image-to-image generation with a progressive creation feature.

[OpenRouter nabs $40M in funding for its AI inference API](https://substack.com/redirect/a3a73f58-9af4-46c0-b5ac-c742209ee7db?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Connect with 11,413+ industry leaders from our network of tech and business leaders forming a unique trusted network effect.

[Getty drops key copyright claims against Stability AI, but UK lawsuit continues](https://substack.com/redirect/646f7bb3-e5aa-4e2b-94a8-c7895834d335?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Getty Images has dropped its primary copyright infringement claims against Stability AI in the UK, focusing instead on secondary infringement and trademark claims, while continuing a separate lawsuit in the U.S. over similar issues.

[Sam Altman takes his ‘io’ trademark battle public](https://substack.com/redirect/123fbc61-c4ba-48a6-9e5e-29220628dea5?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Sam Altman publicly shares email exchanges with Iyo's founder amid a trademark lawsuit over OpenAI's upcoming device, highlighting the tension between the two companies and OpenAI's decision to change its branding due to a temporary restraining order.

#### Research

|     |                                                                                                                                                                                                                                                                                                                                                                                                                |     |
| --- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
|     | [![Refer to caption](https://substackcdn.com/image/fetch/$s_!7z1g!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdcc796-08b4-44f9-91e3-f989a12fe949_1661x2106.png "Refer to caption")](https://substack.com/redirect/846ac9cd-8cb0-4057-a813-a18840c1f9e7?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) |     |

[Microsoft Says Its New AI System Diagnosed Patients 4 Times More Accurately Than Human Doctors](https://substack.com/redirect/40f13bd0-8200-41b1-b29b-a1b746455a82?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Microsoft's new AI system, MAI-DxO, significantly outperformed human doctors in diagnostic accuracy and cost efficiency by orchestrating multiple AI models to mimic expert collaboration. Paper: [Sequential Diagnosis with Language Models](https://substack.com/redirect/de43c9c4-f1be-4155-ab90-ada253a2ed51?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

[MMSearch-R1: Incentivizing LMMs to Search](https://substack.com/redirect/924f1c66-4979-4de0-b836-764c4402ec90?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - MMSearch-R1 introduces an end-to-end reinforcement learning approach to train Large Multimodal Models (LMMs) to effectively perform on-demand searches in real-world internet environments, enhancing their ability to handle complex, knowledge-intensive tasks by integrating multimodal search tools and optimizing search strategies.

[In-Context Learning Strategies Emerge Rationally](https://substack.com/redirect/14598d6a-d0c1-45a2-8401-0ef572a1857d?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - A hierarchical Bayesian framework models in-context learning as a balance between strategy loss and complexity, providing both explanatory and predictive insights.

[Visual Structures Helps Visual Reasoning: Addressing the Binding Problem in VLMs](https://substack.com/redirect/935f015c-63e2-4490-b1f7-0966d99297ad?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - A novel method combining visual scaffolding with textual prompts significantly enhances feature-object binding and visual reasoning in Vision-Language Models, addressing the binding problem and improving performance across various tasks without requiring model retraining.

[OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling](https://substack.com/redirect/13ca624a-67bd-440c-8c6c-921f4cd54d1f?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - OctoThinker demonstrates that scaling up mid-training with high-quality mathematical corpora and a two-stage strategy can transform Llama models into effective base models for reinforcement learning, achieving performance comparable to more RL-friendly models like Qwen.

[Inverse-and-Edit: Effective and Fast Image Editing by Cycle Consistency Models](https://substack.com/redirect/8ae04700-a1da-471f-862f-3bf78867d4c2?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Inverse-and-Edit introduces a cycle-consistency optimization method that enhances image inversion and editing quality in distilled models, achieving results comparable to full-step diffusion models but with significantly reduced computational cost.

#### Concerns

[A.I. Is Starting to Wear Down Democracy](https://substack.com/redirect/2e412bad-0c25-49ab-9570-a3fed163c547?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Generative AI is increasingly influencing elections by spreading misleading content, amplifying divisions, and affecting outcomes, as seen in recent cases in Europe.

[Authors call on publishers to limit their use of AI](https://substack.com/redirect/549ac225-5a50-4deb-9c7d-31715074bf17?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Authors are urging publishers to limit AI use in the industry, emphasizing the importance of human creativity and fair compensation for writers.

#### Policy

[Judge Rejects Authors’ Claim That Meta AI Training Violated Copyrights](https://substack.com/redirect/fbc34f00-30c0-4f68-b6d7-69e4b90598e0?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Judge Vincent Chhabria ruled that Meta's use of copyrighted books to train its Llama language model constituted "fair use," dismissing the authors' claims of copyright violation due to lack of evidence of market harm.

[Germany tells Apple, Google to block DeepSeek as the Chinese AI app faces rising pressure in Europe](https://substack.com/redirect/5630e31e-4387-4b9a-82d3-1b519ffee669?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Germany's data protection watchdog has accused DeepSeek of unlawfully transferring user data to China and urged Apple and Google to block the app, potentially leading to an EU-wide ban.

[Denmark to tackle deepfakes by giving people copyright to their own features](https://substack.com/redirect/322541f2-5974-4245-8830-980d1c171102?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Denmark plans to amend copyright law to give individuals control over their digital likenesses, aiming to combat the misuse of AI-generated deepfakes and set a precedent for other European countries.

[How Some of China’s Top AI Thinkers Built Their Own AI Safety Institute](https://substack.com/redirect/8de90169-6d09-4fa5-b0af-f9e2d0bc3094?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - China's AI Safety and Development Association (CnAISDA) was established to engage in international AI safety governance, reflecting China's evolving focus on balancing AI innovation with safety concerns and its integration into global AI safety discussions.

[Republicans scrap deal in 'big, beautiful bill' to lower restrictions on states' AI regulations](https://substack.com/redirect/f2f54816-5da7-4e16-8b50-07c1dd2aafa9?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - A deal that had been reached between Sens. Marsha Blackburn, R-Tenn., and Ted Cruz, R-Texas, over how states can regulate artificial intelligence has been pulled from President Donald Trump's "big, beautiful" bill.

#### Explainers

[How Do You Teach Computer Science in the A.I. Era?](https://substack.com/redirect/da3d31b9-5370-4199-9c19-fec6060e3486?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Carnegie Mellon University is re-evaluating its computer science curriculum to address the challenges posed by the rapid advancement of generative AI technologies like ChatGPT.

[My Couples Retreat With 3 AI Chatbots and the Humans Who Love Them](https://substack.com/redirect/05472f16-dd00-45ee-9d0a-4ab78b566e7e?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc) - Exploring the growing phenomenon of human-AI romantic relationships, the article highlights how AI companions like Xia are becoming emotionally significant partners for people like Damien, who find solace and connection in these digital relationships.

_You’re a free subscriber to_ [Last Week in AI](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpP3V0bV9jYW1wYWlnbj1lbWFpbC1ob21lJnI9MWk0amIyIiwicCI6MTY3NDc5MDE1LCJzIjoxMTAzNTgsImYiOnRydWUsInUiOjkwOTEwOTEwLCJpYXQiOjE3NTE1ODMyNzEsImV4cCI6MjA2NzE1OTI3MSwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.YUDk4v50cjfX49IXyrtjE1-Yuqp6WvDvRpWziXOvMFo?)_. For the full experience, [become a paying subscriber](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZsYXN0d2Vla2luLmFpJTJGcCUyRmxhc3Qtd2Vlay1pbi1haS0zMTQtbWV0YXMtc3VwZXJpbnRlbGxpZ2VuY2Umcj0xaTRqYjImdG9rZW49ZXlKMWMyVnlYMmxrSWpvNU1Ea3hNRGt4TUN3aWFXRjBJam94TnpVeE5UZ3pNamN4TENKbGVIQWlPakUzTlRReE56VXlOekVzSW1semN5STZJbkIxWWkweE1UQXpOVGdpTENKemRXSWlPaUpqYUdWamEyOTFkQ0o5LkhFNmF0NlgyMnVPdXloem9kbHVvZlN6QVg0TlFfZXR3TGI1NHRUZGh4NFkiLCJwIjoxNjc0NzkwMTUsInMiOjExMDM1OCwiZiI6dHJ1ZSwidSI6OTA5MTA5MTAsImlhdCI6MTc1MTU4MzI3MSwiZXhwIjoyMDY3MTU5MjcxLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.gm48UaJ1GoBtF4ENBqiqthZ96-UK7wHbgCvj51Jd97g?)._

[Upgrade to paid](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZsYXN0d2Vla2luLmFpJTJGcCUyRmxhc3Qtd2Vlay1pbi1haS0zMTQtbWV0YXMtc3VwZXJpbnRlbGxpZ2VuY2Umcj0xaTRqYjImdG9rZW49ZXlKMWMyVnlYMmxrSWpvNU1Ea3hNRGt4TUN3aWFXRjBJam94TnpVeE5UZ3pNamN4TENKbGVIQWlPakUzTlRReE56VXlOekVzSW1semN5STZJbkIxWWkweE1UQXpOVGdpTENKemRXSWlPaUpqYUdWamEyOTFkQ0o5LkhFNmF0NlgyMnVPdXloem9kbHVvZlN6QVg0TlFfZXR3TGI1NHRUZGh4NFkiLCJwIjoxNjc0NzkwMTUsInMiOjExMDM1OCwiZiI6dHJ1ZSwidSI6OTA5MTA5MTAsImlhdCI6MTc1MTU4MzI3MSwiZXhwIjoyMDY3MTU5MjcxLCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.gm48UaJ1GoBtF4ENBqiqthZ96-UK7wHbgCvj51Jd97g?&utm_medium=email&utm_source=subscribe-widget&utm_content=167479015)

If you would like to become a sponsor for the newsletter, podcast, or both, please fill out [this form](https://substack.com/redirect/78fbff82-0c68-464a-a118-094bc3cfe240?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc).

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Like](https://substack.com/app-link/post?publication_id=110358&post_id=167479015&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjo5MDkxMDkxMCwicG9zdF9pZCI6MTY3NDc5MDE1LCJyZWFjdGlvbiI6IuKdpCIsImlhdCI6MTc1MTU4MzI3MSwiZXhwIjoxNzU0MTc1MjcxLCJpc3MiOiJwdWItMTEwMzU4Iiwic3ViIjoicmVhY3Rpb24ifQ.yr9s8dzW58Yb2MJYbvJcagf5s5AX4r4hUeFlRz520Rs&utm_medium=email&utm_campaign=email-reaction&r=1i4jb2)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Comment](https://substack.com/app-link/post?publication_id=110358&post_id=167479015&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjo5MDkxMDkxMCwicG9zdF9pZCI6MTY3NDc5MDE1LCJpYXQiOjE3NTE1ODMyNzEsImV4cCI6MTc1NDE3NTI3MSwiaXNzIjoicHViLTExMDM1OCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.wY7hPDTyhH87lD15UKmPw_mhM83yv_8lkpxm3AdVPKw&r=1i4jb2&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Restack](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbGFzdHdlZWtpbmFpL3AvbGFzdC13ZWVrLWluLWFpLTMxNC1tZXRhcy1zdXBlcmludGVsbGlnZW5jZT91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9MWk0amIyJnRva2VuPWV5SjFjMlZ5WDJsa0lqbzVNRGt4TURreE1Dd2ljRzl6ZEY5cFpDSTZNVFkzTkRjNU1ERTFMQ0pwWVhRaU9qRTNOVEUxT0RNeU56RXNJbVY0Y0NJNk1UYzFOREUzTlRJM01Td2lhWE56SWpvaWNIVmlMVEV4TURNMU9DSXNJbk4xWWlJNkluQnZjM1F0Y21WaFkzUnBiMjRpZlEud1k3aFBEVHloSDg3bEQxNVVLbVB3X21oTTgzeXZfOGxrcHhtM0FkVlBLdyIsInAiOjE2NzQ3OTAxNSwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1Ijo5MDkxMDkxMCwiaWF0IjoxNzUxNTgzMjcxLCJleHAiOjIwNjcxNTkyNzEsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.FfC_p0NECZWnO61YtmVBu63rQ1sowtPQwOyPx_omZus?&utm_source=substack&utm_medium=email)

© 2025 Skynet Today  
548 Market Street PMB 72296, San Francisco, CA 94104  
[Unsubscribe](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqbzVNRGt4TURreE1Dd2ljRzl6ZEY5cFpDSTZNVFkzTkRjNU1ERTFMQ0pwWVhRaU9qRTNOVEUxT0RNeU56RXNJbVY0Y0NJNk1UYzRNekV4T1RJM01Td2lhWE56SWpvaWNIVmlMVEV4TURNMU9DSXNJbk4xWWlJNkltUnBjMkZpYkdWZlpXMWhhV3dpZlEuRi1MRF9XWFRMdUV5M2JIWTlKTlBkdmVnZHR3TW5wMzNtZU1WbnE2OXhiSSIsInAiOjE2NzQ3OTAxNSwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1Ijo5MDkxMDkxMCwiaWF0IjoxNzUxNTgzMjcxLCJleHAiOjIwNjcxNTkyNzEsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.AokO8hICs4Hv1xv4kzPmUeOLCcILZP0UBc8i0SuwFM8?)

[![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD10LmFuaHRpZXAxMTRAZ21haWwuY29tJnI9MWk0amIyIiwicCI6MTY3NDc5MDE1LCJzIjoxMTAzNTgsImYiOnRydWUsInUiOjkwOTEwOTEwLCJpYXQiOjE3NTE1ODMyNzEsImV4cCI6MjA2NzE1OTI3MSwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.-mTCLOTlh3ilyKbaqMGAkF5n7Wzo1pfO09KQsIhBmXc?)

![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzAzMjI1MjI1LjMuZmQwZTNhMTczYTViZDcwOUBtZzIuc3Vic3RhY2suY29tPiIsInUiOjkwOTEwOTEwLCJyIjoidC5hbmh0aWVwMTE0QGdtYWlsLmNvbSIsImQiOiJtZzIuc3Vic3RhY2suY29tIiwicCI6MTY3NDc5MDE1LCJ0IjoibmV3c2xldHRlciIsImEiOiJldmVyeW9uZSIsInMiOjExMDM1OCwiYyI6InBvc3QiLCJmIjp0cnVlLCJwb3NpdGlvbiI6ImJvdHRvbSIsImlhdCI6MTc1MTU4MzI3MSwiZXhwIjoxNzU0MTc1MjcxLCJpc3MiOiJwdWItMCIsInN1YiI6ImVvIn0.ZGt8YA6igZjznbAxEcoHXdkF08cBVZwzkn_tZGdk1cE)![](https://email.mg2.substack.com/o/eJxEkNHKwyAMRp9mXpaotbYXPktJNetkrRaNG337n26DH3J1AofD55FpzeV0R64sguuDHM0oyElrpBm1skrQjnGbV0pUkCnMyP9fOWgQDzcAen9XCrVavIYJDA3Kggmm92h8ENEpUAYsaKWMUqbT3T0AaZRWo1mChenWw76qrralMvpn5_MuYp3vhT4BjksjcWXO2EKk5MnRi8qZ0w_H4ORgezuBNF_C50Eu0btuxExFHG2Zfd73liKfMyVcNgo_cVu26JFjTh-RBG1GURx3mB4c6ZCyv_WwXimftNqWkHeMyW1Y-U30jAmj4O-SrVK5PBNM8jrxcuovAAD__x38eAo)
```

<END_EXAMPLE_INPUT>

## Output Cleaned Newsletter:

<START_EXAMPLE_OUTPUT>

```md
Mark Zuckerberg announces his AI ‘superintelligence’ super-group, DeepMind launches AlphaGenome, aiming to predict gene regulation from DNA sequence, and more!

# Top News

## [Mark Zuckerberg announces his AI ‘superintelligence’ super-group](https://substack.com/redirect/9e37d4f5-171c-46ba-9095-546ee6dc9eed?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Meta CEO Mark Zuckerberg has announced the creation of a new group within the company, the "Meta Superintelligence Labs", which will be responsible for all AI-related work. The group will be led by former Scale AI CEO Alexandr Wang, who recently joined Meta as part of a multibillion-dollar deal, and will be assisted by former GitHub CEO Nat Friedman. In addition, Meta has made 11 new AI-focused hires, including former employees of Anthropic, Google DeepMind, and OpenAI.

Zuckerberg has reportedly been making substantial offers to potential hires, with figures reaching into the eight-figure range, in an effort to boost Meta's AI capabilities, which have been lagging behind other major AI companies. The company has also been in discussions to acquire several AI companies, including Thinking Machines Lab, Perplexity, and Safe Superintelligence, although none of these talks have resulted in formal offers.

More on this:

- [Meta shares hit all-time high as Mark Zuckerberg goes on AI hiring blitz](https://substack.com/redirect/765dacab-ec12-4d72-a328-be7f1227bd39?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [The A.I. Frenzy Is Escalating. Again.](https://substack.com/redirect/11940538-333a-4ad4-8798-2a4e55aca215?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [In Pursuit of Godlike Technology, Mark Zuckerberg Amps Up the A.I. Race](https://substack.com/redirect/f2adfad0-ec26-427e-86c9-b10a2829582a?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Meta hires key OpenAI researcher to work on AI reasoning models](https://substack.com/redirect/1b39478c-fb9d-4e2d-a371-210c7bbe02b8?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Here Is Everyone Mark Zuckerberg Has Hired So Far for Meta’s ‘Superintelligence’ Team](https://substack.com/redirect/dbecebad-5e32-44b5-a50b-9776438ce3a9?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Here’s What Mark Zuckerberg Is Offering Top AI Talent](https://substack.com/redirect/29d68346-f441-4781-97c0-63a3d5714801?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [OpenAI Leadership Responds to Meta Offers: ‘Someone Has Broken Into Our Home’](https://substack.com/redirect/4e0e2641-f87c-4ee5-980c-3e3eb37943bd?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Sam Altman Slams Meta’s AI Talent-Poaching Spree: ‘Missionaries Will Beat Mercenaries’](https://substack.com/redirect/9bce36da-8d65-4960-8c14-1c6f3ea8088f?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

## [DeepMind launches AlphaGenome, aiming to predict gene regulation from DNA sequence](https://substack.com/redirect/a5769572-0c3e-442f-b088-5f457ed11e5b?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

DeepMind, known for its protein-folding deep learning model AlphaFold, has recently ventured into the complex field of predicting gene regulation from DNA sequences. The company announced its latest model, AlphaGenome, in a preprint and [blog post](https://substack.com/redirect/050c2b55-2080-4a58-93e9-64ab63b3ebf8?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc). This model represents an early step towards potential applications in therapeutic development. Research engineer Natasha Latysheva acknowledges that compared to protein structure prediction, genomics is a more ambiguous field with no single metric of success. As a result, DeepMind is pursuing multiple metrics in its quest to predict gene regulation.

More on this:

- [DeepMind blog - AlphaGenome: AI for better understanding the genome](https://substack.com/redirect/050c2b55-2080-4a58-93e9-64ab63b3ebf8?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Paper - AlphaGenome: advancing regulatory variant effect prediction with a unified DNA sequence model](https://substack.com/redirect/d80c4c33-8e3e-439e-9193-18d924c2bb4d?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)
- [Google’s new AI will help researchers understand how our genes work](https://substack.com/redirect/8f8499d4-83d3-4ddb-ba5a-07ac819f1422?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

## [Google is bringing Gemini CLI to developers’ terminals](https://substack.com/redirect/915ce8dd-1405-4bdf-a269-a08bdea24a85?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Google has introduced a new open-source AI agent, Gemini CLI, that brings Gemini's coding, content generation, and research capabilities directly to developers' terminals. The tool is designed to enhance the command line experience, allowing developers to write and debug code using natural language prompts. Gemini CLI uses Google's Gemini 2.5 Pro reasoning model, which supports a 1 million token context window, and is integrated with Gemini Code Assist. It also includes built-in Model Context Protocol (MCP) and Google Search support, and enables developers to generate images and video using Google's Veo and Imagen AI tools.

Gemini CLI is currently available for developers to preview for free through a Gemini Code Assist license that can be obtained via a personal Google account. This license allows users a usage limit of 60 model requests per minute and 1,000 requests per day, which Google claims is the "largest allowance" in the industry.

# Other News

## Tools

### [Google embraces AI in the classroom with new Gemini tools for educators, chatbots for students, and more](https://substack.com/redirect/370be2a4-fa3b-41b3-a7a8-cbb17983351c?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Google is enhancing educational experiences by integrating over 30 AI tools, including personalized learning aids and interactive study guides, into classrooms through its Gemini AI suite, aiming to support teachers and students while addressing the challenges posed by AI in education.

### [Mayo Clinic’s AI tool identifies 9 dementia types, including Alzheimer’s, with one scan](https://substack.com/redirect/c674e950-115a-42bb-befa-74cab46fdfb0?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Mayo Clinic's AI tool, StateViewer, significantly improves the speed and accuracy of diagnosing nine types of dementia, including Alzheimer's, by analyzing brain activity patterns from a single FDG-PET scan, offering transformative potential for early and precise dementia care.

### [Creative Commons debuts CC signals, a framework for an open AI ecosystem](https://substack.com/redirect/66aea329-95c8-4609-81aa-0f8fe9b15c7c?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Creative Commons has introduced CC signals, a project aimed at creating a legal and technical framework to guide the ethical reuse of data for AI training, balancing openness with data protection.

### [Baidu releases open source model family ERNIE 4.5](https://substack.com/redirect/d26010e3-a0b4-4db6-bff4-ca367b76310d?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Baidu's decision to open-source its ERNIE 4.5 model family under the Apache 2.0 license marks a strategic shift aimed at fostering global AI development and challenging industry norms set by companies like OpenAI and Anthropic.

### [Cloudflare Introduces Default Blocking of A.I. Data Scrapers](https://substack.com/redirect/19f4680e-d82a-4e13-9a28-acfae71692a7?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Cloudflare's new setting allows websites to block AI data scrapers by default, requiring explicit permission for bots to access content, aiming to protect original digital content and influence the AI development landscape.

### [Anthropic now lets you make apps right from its Claude AI chatbot](https://substack.com/redirect/fc982cdf-b6e2-4195-9f32-6986377dfd2b?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Anthropic's Claude AI chatbot now includes a beta feature that allows users to create and share AI-powered apps directly within the app, leveraging the Artifacts feature for interactive development and API integration.

### [Google's Imagen 4 text-to-image model promises 'significantly improved' boring images](https://substack.com/redirect/dd5e3305-6013-482b-8a10-29edd21f175e?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Google's Imagen 4 and Imagen 4 Ultra models offer improved text-to-image rendering with precise prompt following, though they still produce images that appear machine-generated and lack the charm of competitors like Dall-E and Midjourney.

### [Google launches Doppl, a new app that lets you visualize how an outfit might look on you](https://substack.com/redirect/ec299bcc-d44b-41df-a9c2-f8aa751f1052?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Doppl allows users to upload a full-body photo to virtually try on outfits, creating AI-generated images and videos of themselves in different clothes, enhancing personal style exploration and data collection for Google.

## Business

### [Runway is going to let people generate video games with AI](https://substack.com/redirect/957c85fe-fab1-44a6-8a2e-34a0cd014235?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Runway is expanding its generative AI technology from Hollywood to the gaming industry, aiming to accelerate game development and is in discussions with gaming companies for collaboration and data access.

### [OpenAI turns to Google's AI chips to power its products, source says](https://substack.com/redirect/cb2e7f1c-aa20-443b-bf85-9af6c15ae61a?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

OpenAI has started renting Google's tensor processing units (TPUs) to power its products, marking a shift from relying solely on Nvidia GPUs and Microsoft's data centers, while Google expands its cloud business by offering its AI technology to external customers.

### [As job losses loom, Anthropic launches program to track AI’s economic fallout](https://substack.com/redirect/1bdd24bd-e250-4ba0-b56c-22f8334fd589?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Anthropic's Economic Futures Program aims to research AI's impact on the labor market and economy, offering grants and hosting symposia to develop policy proposals and track AI's economic effects.

### [At Amazon’s Biggest Data Center, Everything Is Supersized for A.I.](https://substack.com/redirect/2d248889-efe6-4671-80a4-dff8d629dc35?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Amazon's new data center complex in Indiana, part of Project Rainier, is designed to support AI development with massive infrastructure and resources, primarily serving the AI start-up Anthropic.

### [Alibaba Unveils Latest AI Service for Images in Push for Users](https://substack.com/redirect/06b5338c-7b80-4397-864f-cc2ef4477967?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Alibaba's new AI service, Qwen VLo, enhances user experience by enabling text-to-image and image-to-image generation with a progressive creation feature.

### [OpenRouter nabs $40M in funding for its AI inference API](https://substack.com/redirect/a3a73f58-9af4-46c0-b5ac-c742209ee7db?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Connect with 11,413+ industry leaders from our network of tech and business leaders forming a unique trusted network effect.

### [Getty drops key copyright claims against Stability AI, but UK lawsuit continues](https://substack.com/redirect/646f7bb3-e5aa-4e2b-94a8-c7895834d335?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Getty Images has dropped its primary copyright infringement claims against Stability AI in the UK, focusing instead on secondary infringement and trademark claims, while continuing a separate lawsuit in the U.S. over similar issues.

### [Sam Altman takes his ‘io’ trademark battle public](https://substack.com/redirect/123fbc61-c4ba-48a6-9e5e-29220628dea5?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Sam Altman publicly shares email exchanges with Iyo's founder amid a trademark lawsuit over OpenAI's upcoming device, highlighting the tension between the two companies and OpenAI's decision to change its branding due to a temporary restraining order.

## Research

### [Microsoft Says Its New AI System Diagnosed Patients 4 Times More Accurately Than Human Doctors](https://substack.com/redirect/40f13bd0-8200-41b1-b29b-a1b746455a82?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Microsoft's new AI system, MAI-DxO, significantly outperformed human doctors in diagnostic accuracy and cost efficiency by orchestrating multiple AI models to mimic expert collaboration. Paper: [Sequential Diagnosis with Language Models](https://substack.com/redirect/de43c9c4-f1be-4155-ab90-ada253a2ed51?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

### [MMSearch-R1: Incentivizing LMMs to Search](https://substack.com/redirect/924f1c66-4979-4de0-b836-764c4402ec90?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

MMSearch-R1 introduces an end-to-end reinforcement learning approach to train Large Multimodal Models (LMMs) to effectively perform on-demand searches in real-world internet environments, enhancing their ability to handle complex, knowledge-intensive tasks by integrating multimodal search tools and optimizing search strategies.

### [In-Context Learning Strategies Emerge Rationally](https://substack.com/redirect/14598d6a-d0c1-45a2-8401-0ef572a1857d?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

A hierarchical Bayesian framework models in-context learning as a balance between strategy loss and complexity, providing both explanatory and predictive insights.

### [Visual Structures Helps Visual Reasoning: Addressing the Binding Problem in VLMs](https://substack.com/redirect/935f015c-63e2-4490-b1f7-0966d99297ad?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

A novel method combining visual scaffolding with textual prompts significantly enhances feature-object binding and visual reasoning in Vision-Language Models, addressing the binding problem and improving performance across various tasks without requiring model retraining.

### [OctoThinker: Mid-training Incentivizes Reinforcement Learning Scaling](https://substack.com/redirect/13ca624a-67bd-440c-8c6c-921f4cd54d1f?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

OctoThinker demonstrates that scaling up mid-training with high-quality mathematical corpora and a two-stage strategy can transform Llama models into effective base models for reinforcement learning, achieving performance comparable to more RL-friendly models like Qwen.

### [Inverse-and-Edit: Effective and Fast Image Editing by Cycle Consistency Models](https://substack.com/redirect/8ae04700-a1da-471f-862f-3bf78867d4c2?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Inverse-and-Edit introduces a cycle-consistency optimization method that enhances image inversion and editing quality in distilled models, achieving results comparable to full-step diffusion models but with significantly reduced computational cost.

## Concerns

### [A.I. Is Starting to Wear Down Democracy](https://substack.com/redirect/2e412bad-0c25-49ab-9570-a3fed163c547?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Generative AI is increasingly influencing elections by spreading misleading content, amplifying divisions, and affecting outcomes, as seen in recent cases in Europe.

### [Authors call on publishers to limit their use of AI](https://substack.com/redirect/549ac225-5a50-4deb-9c7d-31715074bf17?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Authors are urging publishers to limit AI use in the industry, emphasizing the importance of human creativity and fair compensation for writers.

## Policy

### [Judge Rejects Authors’ Claim That Meta AI Training Violated Copyrights](https://substack.com/redirect/fbc34f00-30c0-4f68-b6d7-69e4b90598e0?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Judge Vincent Chhabria ruled that Meta's use of copyrighted books to train its Llama language model constituted "fair use," dismissing the authors' claims of copyright violation due to lack of evidence of market harm.

### [Germany tells Apple, Google to block DeepSeek as the Chinese AI app faces rising pressure in Europe](https://substack.com/redirect/5630e31e-4387-4b9a-82d3-1b519ffee669?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Germany's data protection watchdog has accused DeepSeek of unlawfully transferring user data to China and urged Apple and Google to block the app, potentially leading to an EU-wide ban.

### [Denmark to tackle deepfakes by giving people copyright to their own features](https://substack.com/redirect/322541f2-5974-4245-8830-980d1c171102?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Denmark plans to amend copyright law to give individuals control over their digital likenesses, aiming to combat the misuse of AI-generated deepfakes and set a precedent for other European countries.

### [How Some of China’s Top AI Thinkers Built Their Own AI Safety Institute](https://substack.com/redirect/8de90169-6d09-4fa5-b0af-f9e2d0bc3094?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

China's AI Safety and Development Association (CnAISDA) was established to engage in international AI safety governance, reflecting China's evolving focus on balancing AI innovation with safety concerns and its integration into global AI safety discussions.

### [Republicans scrap deal in 'big, beautiful bill' to lower restrictions on states' AI regulations](https://substack.com/redirect/f2f54816-5da7-4e16-8b50-07c1dd2aafa9?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

A deal that had been reached between Sens. Marsha Blackburn, R-Tenn., and Ted Cruz, R-Texas, over how states can regulate artificial intelligence has been pulled from President Donald Trump's "big, beautiful" bill.

## Explainers

### [How Do You Teach Computer Science in the A.I. Era?](https://substack.com/redirect/da3d31b9-5370-4199-9c19-fec6060e3486?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Carnegie Mellon University is re-evaluating its computer science curriculum to address the challenges posed by the rapid advancement of generative AI technologies like ChatGPT.

### [My Couples Retreat With 3 AI Chatbots and the Humans Who Love Them](https://substack.com/redirect/05472f16-dd00-45ee-9d0a-4ab78b566e7e?j=eyJ1IjoiMWk0amIyIn0.7x6p5Pl7EFTcZDatxOXYMWIk9mpaj9qIET7MZkN41Nc)

Exploring the growing phenomenon of human-AI romantic relationships, the article highlights how AI companions like Xia are becoming emotionally significant partners for people like Damien, who find solace and connection in these digital relationships.
```

<END_EXAMPLE_OUTPUT>

# EXAMPLE 2:

## Input Newsletter:

<START_EXAMPLE_INPUT>

```md
![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzA0MjI0NTUwLjMuNzVjYWNhZjRiYzVjMWZkYUBtZy1kMS5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQxLnN1YnN0YWNrLmNvbSIsInAiOjE2NzU1NTA0MCwidCI6InBvZGNhc3QiLCJhIjoiZXZlcnlvbmUiLCJzIjoxMTAzNTgsImMiOiJwb3N0IiwiZiI6dHJ1ZSwicG9zaXRpb24iOiJ0b3AiLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MTc1NDI2MTIzNCwiaXNzIjoicHViLTAiLCJzdWIiOiJlbyJ9.LscwrGfExW4CJS86hu4Pn6RdIQGN_0SQIhKkz1U7ik8)

Google is bringing Gemini CLI to developers’ terminals, Anthropic now lets you make apps right from its Claude AI chatbot, and more!

͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­͏   ­

Forwarded this email? [Subscribe here](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3N1YnNjcmliZT91dG1fc291cmNlPWVtYWlsJnV0bV9jYW1wYWlnbj1lbWFpbC1zdWJzY3JpYmUmcj01czgzb3ombmV4dD1odHRwcyUzQSUyRiUyRmxhc3R3ZWVraW4uYWklMkZwJTJGbHdpYWktcG9kY2FzdC0yMTQtZ2VtaW5pLWNsaS1pby1kcmFtYSIsInAiOjE2NzU1NTA0MCwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTY2OTIzNCwiZXhwIjoyMDY3MjQ1MjM0LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.w3tjKwk6xlwbz0KjTsIOdhcf2m0rwKAb6Q9LcZlys4Y?) for more

[![](https://substackcdn.com/image/fetch/$s_!xT4S!,w_1100,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f4944be-2d39-4340-a41c-3ca79f17665a_2400x800.png)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3AvbHdpYWktcG9kY2FzdC0yMTQtZ2VtaW5pLWNsaS1pby1kcmFtYT91dG1fY2FtcGFpZ249ZW1haWwtaGFsZi1wb3N0JnI9NXM4M296JnRva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTnpVMU5UQTBNQ3dpYVdGMElqb3hOelV4TmpZNU1qTTBMQ0psZUhBaU9qRTNOVFF5TmpFeU16UXNJbWx6Y3lJNkluQjFZaTB4TVRBek5UZ2lMQ0p6ZFdJaU9pSndiM04wTFhKbFlXTjBhVzl1SW4wLkdoay1Gand2VXJVNGlBcUVPZHBKYmFxeHhzWU1iSHFldmM3YV9hZDJmeGciLCJwIjoxNjc1NTUwNDAsInMiOjExMDM1OCwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MjA2NzI0NTIzNCwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.uu6nCJZtOQR5KmliPL7Z8bkwWvnAARFtQ3g15sO_f-Y?)

Hello from Last Week in AI! Thank you for being a subscriber :)

If you like our stuff, consider following us on [Twitter](https://substack.com/redirect/3329ec5f-36d5-48bb-94d4-e90cf0f03710?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8), checking out our [podcast](https://substack.com/redirect/8efae497-2d0c-4041-bfc2-0b7511f8a04e?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8), and sharing the newsletter with friends. Oh, and consider getting a paid subscription.

[Get 20% off forever](https://substack.com/redirect/092bcbc1-4809-44bd-ab56-2029b9d3dd06?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

If you would like to become a sponsor for the newsletter, podcast, or both, please fill out [this form](https://substack.com/redirect/2a35079d-0ccd-460a-89d5-f6bd4c14a894?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8).

---

[![Last Week in AI](https://substackcdn.com/image/youtube/w_728,c_limit/HSC9VZjK3OU)  
\
Podcast  
\
LWiAI Podcast #214 - Gemini C…  
\
0:001:33:32![](https://substackcdn.com/image/fetch/$s_!x5iK!,w_48,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FPlayIconRounded%3Fv%3D4%26height%3D48%26fill%3Drgba%28255%252C255%252C255%252C0.8%29%26stroke%3Dnone%26strokeWidth%3D3.6)](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=podcast-email&play_audio=true&r=5s83oz&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjE3NTQyNjEyMzQsImlzcyI6InB1Yi0xMTAzNTgiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Ghk-FjwvUrU4iAqEOdpJbaqxxsYMbHqevc7a_ad2fxg&utm_source=substack&utm_medium=email&utm_content=play_card#play)

[![](https://substackcdn.com/image/fetch/$s_!iFbw!,w_32,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FHeadphonesIcon%3Fv%3D4%26height%3D32%26stroke%3D%2523ffffff%26strokeWidth%3D2)Listen now](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=podcast-email&play_audio=true&r=5s83oz&utm_campaign=email-play-on-substack&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjE3NTQyNjEyMzQsImlzcyI6InB1Yi0xMTAzNTgiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Ghk-FjwvUrU4iAqEOdpJbaqxxsYMbHqevc7a_ad2fxg&utm_content=listen_now_button)

# [LWiAI Podcast #214 - Gemini CLI, io drama, AlphaGenome](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjE3NTQyNjEyMzQsImlzcyI6InB1Yi0xMTAzNTgiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Ghk-FjwvUrU4iAqEOdpJbaqxxsYMbHqevc7a_ad2fxg)

### Google is bringing Gemini CLI to developers’ terminals, Anthropic now lets you make apps right from its Claude AI chatbot, and more!

[Last Week in AI](https://substack.com/@lastweekinai)

Jul 4

[![](https://substackcdn.com/image/fetch/$s_!QAnE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9ef58ddc-993f-40a5-a130-df80b858aeae_512x512.jpeg)](https://substack.com/@lastweekinai)

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MTc1NDI2MTIzNCwiaXNzIjoicHViLTExMDM1OCIsInN1YiI6InJlYWN0aW9uIn0.AD24IkTruuK5aFHpLeXtSgmtu6jv7_JDZVUrmIElLrY&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjE3NTQyNjEyMzQsImlzcyI6InB1Yi0xMTAzNTgiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Ghk-FjwvUrU4iAqEOdpJbaqxxsYMbHqevc7a_ad2fxg&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!_L14!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideShare2%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=substack&utm_medium=email&utm_content=share&utm_campaign=email-share&action=share&triggerShare=true&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjE3NTQyNjEyMzQsImlzcyI6InB1Yi0xMTAzNTgiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Ghk-FjwvUrU4iAqEOdpJbaqxxsYMbHqevc7a_ad2fxg)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbGFzdHdlZWtpbmFpL3AvbHdpYWktcG9kY2FzdC0yMTQtZ2VtaW5pLWNsaS1pby1kcmFtYT91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9NXM4M296JnRva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTnpVMU5UQTBNQ3dpYVdGMElqb3hOelV4TmpZNU1qTTBMQ0psZUhBaU9qRTNOVFF5TmpFeU16UXNJbWx6Y3lJNkluQjFZaTB4TVRBek5UZ2lMQ0p6ZFdJaU9pSndiM04wTFhKbFlXTjBhVzl1SW4wLkdoay1Gand2VXJVNGlBcUVPZHBKYmFxeHhzWU1iSHFldmM3YV9hZDJmeGciLCJwIjoxNjc1NTUwNDAsInMiOjExMDM1OCwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MjA2NzI0NTIzNCwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.BSaBuCDvUT0Rg8PXyvmAQISsqeNNuUpUQ1l_B8HJe6Q?&utm_source=substack&utm_medium=email)

[READ IN APP![](https://substackcdn.com/image/fetch/$s_!ET-_!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideArrowUpRight%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)](https://open.substack.com/pub/lastweekinai/p/lwiai-podcast-214-gemini-cli-io-drama?utm_source=email&redirect=app-store&utm_campaign=email-read-in-app)

[![](https://substackcdn.com/image/youtube/w_728,c_limit/l_youtube_play_qyqt8q,w_120/HSC9VZjK3OU)](https://substack.com/redirect/28a4668f-a1ed-4cd5-8c18-ddfd30a58890?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Our 214th episode with a summary and discussion of last week's big AI news!  
Recorded on 06/28/2025

Hosted by [Andrey Kurenkov](https://substack.com/redirect/e7a6708f-7814-4835-900a-f2d265eb4f1a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) and [Jeremie Harris](https://substack.com/redirect/571e1d73-2abd-42cf-bd4a-a5835d3abaaf?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8).  
Feel free to email us your questions and feedback at [contact@lastweekinai.com](https://substack.com/redirect/e1da7c2a-c9c1-40c6-bd16-6c29ad523c6f?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) and/or [hello@gladstone.ai](https://substack.com/redirect/bcb80f30-4911-4604-896d-8af8bd953f82?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

In this episode:

- Meta's hiring of key engineers from OpenAI and Thinking Machines Lab securing a $2 billion seed round with a valuation of $10 billion.
- DeepMind introduces Alpha Genome, significantly advancing genomic research with a model comparable to Alpha Fold but focused on gene functions.
- Taiwan imposes technology export controls on Huawei and SMIC, while Getty drops key copyright claims against Stability AI in a groundbreaking legal case.
- A new DeepMind research paper introduces a transformative approach to cognitive debt in AI tasks, utilizing EEG to assess cognitive load and recall in essay writing with LLMs.

Timestamps + Links:

- (00:00:10) Intro / Banter
- (00:01:22) News Preview
- (00:02:15) Response to listener comments

Tools &amp; Apps

- (00:06:18) [Google is bringing Gemini CLI to developers’ terminals](https://substack.com/redirect/931c246e-25ac-4a04-8720-b12ab2efbe9a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:12:09) [Anthropic now lets you make apps right from its Claude AI chatbot](https://substack.com/redirect/6f490198-f892-4081-8645-945897e193b2?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Applications &amp; Business

- (00:15:54) [Sam Altman takes his ‘io’ trademark battle public](https://substack.com/redirect/2fd80951-2298-4e92-a38f-ccb8e3a5bff0?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:21:35) [Huawei Matebook Contains Kirin X90, using SMIC 7nm (N+2) Technology](https://substack.com/redirect/af19acc5-e542-430d-9758-e6d5f0889b89?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:26:05) [AMD deploys its first Ultra Ethernet ready network card — Pensando Pollara provides up to 400 Gbps performance](https://substack.com/redirect/30afe534-203f-4db0-8413-9758d8df8baa?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:31:21) [Amazon joins the big nuclear party, buying 1.92 GW for AWS](https://substack.com/redirect/93ed137a-d3d3-4aec-8e3d-f43a690e67fa?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:33:20) [Nvidia goes nuclear — company joins Bill Gates in backing TerraPower, a company building nuclear reactors for powering data centers](https://substack.com/redirect/62fee9b9-13f2-45dc-a531-7e1a30a6ec4a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:36:18) [Mira Murati’s Thinking Machines Lab closes on $2B at $10B valuation](https://substack.com/redirect/97c93d49-81f4-4da3-9806-27165d9801b9?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:41:02) [Meta hires key OpenAI researcher to work on AI reasoning models](https://substack.com/redirect/e49e3d25-eae9-4346-8617-10b755de6bb9?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Research &amp; Advancements

- (00:49:46) [Google’s new AI will help researchers understand how our genes work](https://substack.com/redirect/f344e64c-415a-4649-8c46-18c118b91ed4?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:55:13) [Direct Reasoning Optimization: LLMs Can Reward And Refine Their Own Reasoning for Open-Ended Tasks](https://substack.com/redirect/e1c9bc27-749e-457d-aae3-c11a7a235e25?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:01:54) [Farseer: A Refined Scaling Law in Large Language Models](https://substack.com/redirect/1b86fca4-29da-4ca2-8d28-41da4d86b144?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:06:28) [LLM-First Search: Self-Guided Exploration of the Solution Space](https://substack.com/redirect/24c335c1-1e89-4226-96be-211f4d2b875b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Policy &amp; Safety

- (01:11:20) [Unsupervised Elicitation of Language Models](https://substack.com/redirect/fcfe287b-7244-4331-adf3-e4e1ec307f94?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:16:04) [Taiwan Imposes Technology Export Controls on Huawei, SMIC](https://substack.com/redirect/7f1fc6d1-ced4-4679-bd17-ca48ca4916ab?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:18:22) [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://substack.com/redirect/2614eb14-d44a-42c2-b5af-753f9fd0fb2f?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Synthetic Media &amp; Art

- (01:23:41) [Judge Rejects Authors’ Claim That Meta AI Training Violated Copyrights](https://substack.com/redirect/8310e133-3c39-4104-bb98-445c5ec9be68?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:29:46) [Getty drops key copyright claims against Stability AI, but UK lawsuit continues](https://substack.com/redirect/7bae8660-4453-43c2-aec9-de5a7521e0dd?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

_You’re a free subscriber to_ [Last Week in AI](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpP3V0bV9jYW1wYWlnbj1lbWFpbC1ob21lJnI9NXM4M296IiwicCI6MTY3NTU1MDQwLCJzIjoxMTAzNTgsImYiOnRydWUsInUiOjM0OTczODE2MywiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjIwNjcyNDUyMzQsImlzcyI6InB1Yi0wIiwic3ViIjoibGluay1yZWRpcmVjdCJ9.0UWHuSZb1sdpY9sdnVB1--DjILU6Su7dAI2BZgyEVks?)_. For the full experience, [become a paying subscriber](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZsYXN0d2Vla2luLmFpJTJGcCUyRmx3aWFpLXBvZGNhc3QtMjE0LWdlbWluaS1jbGktaW8tZHJhbWEmcj01czgzb3omdG9rZW49ZXlKMWMyVnlYMmxrSWpvek5EazNNemd4TmpNc0ltbGhkQ0k2TVRjMU1UWTJPVEl6TkN3aVpYaHdJam94TnpVME1qWXhNak0wTENKcGMzTWlPaUp3ZFdJdE1URXdNelU0SWl3aWMzVmlJam9pWTJobFkydHZkWFFpZlEueTZNRlg1QVI5UlJyQ2xIc3pJbmMxZEJJQ05aRTM5RzhUc2xaQmZsZkN5SSIsInAiOjE2NzU1NTA0MCwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTY2OTIzNCwiZXhwIjoyMDY3MjQ1MjM0LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.2pxaxNrAxQUCmcoU6YBkYkU4_q_PlGcmyV1zo2IVCVE?)._

[Upgrade to paid](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL3N1YnNjcmliZT91dG1fc291cmNlPXBvc3QmdXRtX2NhbXBhaWduPWVtYWlsLWNoZWNrb3V0Jm5leHQ9aHR0cHMlM0ElMkYlMkZsYXN0d2Vla2luLmFpJTJGcCUyRmx3aWFpLXBvZGNhc3QtMjE0LWdlbWluaS1jbGktaW8tZHJhbWEmcj01czgzb3omdG9rZW49ZXlKMWMyVnlYMmxrSWpvek5EazNNemd4TmpNc0ltbGhkQ0k2TVRjMU1UWTJPVEl6TkN3aVpYaHdJam94TnpVME1qWXhNak0wTENKcGMzTWlPaUp3ZFdJdE1URXdNelU0SWl3aWMzVmlJam9pWTJobFkydHZkWFFpZlEueTZNRlg1QVI5UlJyQ2xIc3pJbmMxZEJJQ05aRTM5RzhUc2xaQmZsZkN5SSIsInAiOjE2NzU1NTA0MCwicyI6MTEwMzU4LCJmIjp0cnVlLCJ1IjozNDk3MzgxNjMsImlhdCI6MTc1MTY2OTIzNCwiZXhwIjoyMDY3MjQ1MjM0LCJpc3MiOiJwdWItMCIsInN1YiI6ImxpbmstcmVkaXJlY3QifQ.2pxaxNrAxQUCmcoU6YBkYkU4_q_PlGcmyV1zo2IVCVE?&utm_medium=email&utm_source=subscribe-widget&utm_content=167555040)

If you would like to become a sponsor for the newsletter, podcast, or both, please fill out [this form](https://substack.com/redirect/2a35079d-0ccd-460a-89d5-f6bd4c14a894?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8).

[![](https://substackcdn.com/image/fetch/$s_!PeVs!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideHeart%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Like](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=substack&isFreemail=true&submitLike=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwicmVhY3Rpb24iOiLinaQiLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MTc1NDI2MTIzNCwiaXNzIjoicHViLTExMDM1OCIsInN1YiI6InJlYWN0aW9uIn0.AD24IkTruuK5aFHpLeXtSgmtu6jv7_JDZVUrmIElLrY&utm_medium=email&utm_campaign=email-reaction&r=5s83oz)

[![](https://substackcdn.com/image/fetch/$s_!x1tS!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FLucideComments%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Comment](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=substack&utm_medium=email&isFreemail=true&comments=true&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjE3NTQyNjEyMzQsImlzcyI6InB1Yi0xMTAzNTgiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Ghk-FjwvUrU4iAqEOdpJbaqxxsYMbHqevc7a_ad2fxg&r=5s83oz&utm_campaign=email-half-magic-comments&action=post-comment&utm_source=substack&utm_medium=email)

[![](https://substackcdn.com/image/fetch/$s_!5EGt!,w_36,c_scale,f_png,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Ficon%2FNoteForwardIcon%3Fv%3D4%26height%3D36%26fill%3Dnone%26stroke%3D%2523808080%26strokeWidth%3D2)Restack](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9vcGVuLnN1YnN0YWNrLmNvbS9wdWIvbGFzdHdlZWtpbmFpL3AvbHdpYWktcG9kY2FzdC0yMTQtZ2VtaW5pLWNsaS1pby1kcmFtYT91dG1fc291cmNlPXN1YnN0YWNrJnV0bV9tZWRpdW09ZW1haWwmdXRtX2NhbXBhaWduPWVtYWlsLXJlc3RhY2stY29tbWVudCZhY3Rpb249cmVzdGFjay1jb21tZW50JnI9NXM4M296JnRva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTnpVMU5UQTBNQ3dpYVdGMElqb3hOelV4TmpZNU1qTTBMQ0psZUhBaU9qRTNOVFF5TmpFeU16UXNJbWx6Y3lJNkluQjFZaTB4TVRBek5UZ2lMQ0p6ZFdJaU9pSndiM04wTFhKbFlXTjBhVzl1SW4wLkdoay1Gand2VXJVNGlBcUVPZHBKYmFxeHhzWU1iSHFldmM3YV9hZDJmeGciLCJwIjoxNjc1NTUwNDAsInMiOjExMDM1OCwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MjA2NzI0NTIzNCwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.BSaBuCDvUT0Rg8PXyvmAQISsqeNNuUpUQ1l_B8HJe6Q?&utm_source=substack&utm_medium=email)

© 2025 Skynet Today  
548 Market Street PMB 72296, San Francisco, CA 94104  
[Unsubscribe](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9sYXN0d2Vla2luLmFpL2FjdGlvbi9kaXNhYmxlX2VtYWlsP3Rva2VuPWV5SjFjMlZ5WDJsa0lqb3pORGszTXpneE5qTXNJbkJ2YzNSZmFXUWlPakUyTnpVMU5UQTBNQ3dpYVdGMElqb3hOelV4TmpZNU1qTTBMQ0psZUhBaU9qRTNPRE15TURVeU16UXNJbWx6Y3lJNkluQjFZaTB4TVRBek5UZ2lMQ0p6ZFdJaU9pSmthWE5oWW14bFgyVnRZV2xzSW4wLjRHSkJUaF8tOERodllCWWpkT0ZCNExpRTJ6T2hXZEhEX2k2a2F1S3VRRUEiLCJwIjoxNjc1NTUwNDAsInMiOjExMDM1OCwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MjA2NzI0NTIzNCwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.yRCA5CTtJtD0KN_gEiw3Br9KM9qnAeex9fowBNKWJzU?)

[![Get the app](https://substackcdn.com/image/fetch/$s_!IzGP!,w_262,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fgeneric-app-button%402x.png)](https://substack.com/redirect/19320196-e2bb-4982-80d2-8d6caa9be3e5?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)[![Start writing](https://substackcdn.com/image/fetch/$s_!LkrL!,w_270,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack.com%2Fimg%2Femail%2Fpublish-button%402x.png)](https://substack.com/redirect/2/eyJlIjoiaHR0cHM6Ly9zdWJzdGFjay5jb20vc2lnbnVwP3V0bV9zb3VyY2U9c3Vic3RhY2smdXRtX21lZGl1bT1lbWFpbCZ1dG1fY29udGVudD1mb290ZXImdXRtX2NhbXBhaWduPWF1dG9maWxsZWQtZm9vdGVyJmZyZWVTaWdudXBFbWFpbD1zdW1pdHVwLmRldkBnbWFpbC5jb20mcj01czgzb3oiLCJwIjoxNjc1NTUwNDAsInMiOjExMDM1OCwiZiI6dHJ1ZSwidSI6MzQ5NzM4MTYzLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MjA2NzI0NTIzNCwiaXNzIjoicHViLTAiLCJzdWIiOiJsaW5rLXJlZGlyZWN0In0.6_3FNTiu6iUi5DPD5QEu18_QeRqqN7cJ2-0ydQB7RTM?)

![](https://eotrx.substackcdn.com/open?token=eyJtIjoiPDIwMjUwNzA0MjI0NTUwLjMuNzVjYWNhZjRiYzVjMWZkYUBtZy1kMS5zdWJzdGFjay5jb20-IiwidSI6MzQ5NzM4MTYzLCJyIjoic3VtaXR1cC5kZXZAZ21haWwuY29tIiwiZCI6Im1nLWQxLnN1YnN0YWNrLmNvbSIsInAiOjE2NzU1NTA0MCwidCI6InBvZGNhc3QiLCJhIjoiZXZlcnlvbmUiLCJzIjoxMTAzNTgsImMiOiJwb3N0IiwiZiI6dHJ1ZSwicG9zaXRpb24iOiJib3R0b20iLCJpYXQiOjE3NTE2NjkyMzQsImV4cCI6MTc1NDI2MTIzNCwiaXNzIjoicHViLTAiLCJzdWIiOiJlbyJ9.GUYmRWVXnm0wnNtyZ_PW4hb3KddEpItHsQF6lx9hwgQ)![](https://email.mg-d1.substack.com/o/eJxE0Emq5DAMxvHTPO86OJ6z8FmCLCtpU4kdPFST2zc1wNt-gj8_hNBpL_X2V2mdRS-XwB0aRn62ejZmEdIwOiEd606ZKnSKK_Tfq3JCs79exBBF3JyTwLVEaZ0R5HCzhi9bsIIlL7jQ3HIlhNKaT3KyGgFhUwE1zluEH8XP_U-cpzZC64CPCcvJUlu3Sm-C73UQe0lXGDFRRvL0pHqX_J1T9LOxWmuu-Gfp90X-KhGhdXaNsGI5z5FTv1fKEA6K3-oIR0LoqeR3ZeZSO1Z9G2fq45oiPX8U31-MN6uNEMsJKfsDWv9H9EgZEuufR45G9ZWRarHSzUaypxf_AwAA___GBHj5)
```

<END_EXAMPLE_INPUT>

## Output Cleaned Newsletter:

<START_EXAMPLE_OUTPUT>

```md
Google is bringing Gemini CLI to developers’ terminals, Anthropic now lets you make apps right from its Claude AI chatbot, and more!

Hello from Last Week in AI! Thank you for being a subscriber :)

---

# [LWiAI Podcast #214 - Gemini CLI, io drama, AlphaGenome](https://substack.com/app-link/post?publication_id=110358&post_id=167555040&utm_source=post-email-title&utm_campaign=email-post-title&isFreemail=true&r=5s83oz&token=eyJ1c2VyX2lkIjozNDk3MzgxNjMsInBvc3RfaWQiOjE2NzU1NTA0MCwiaWF0IjoxNzUxNjY5MjM0LCJleHAiOjE3NTQyNjEyMzQsImlzcyI6InB1Yi0xMTAzNTgiLCJzdWIiOiJwb3N0LXJlYWN0aW9uIn0.Ghk-FjwvUrU4iAqEOdpJbaqxxsYMbHqevc7a_ad2fxg)

### Google is bringing Gemini CLI to developers’ terminals, Anthropic now lets you make apps right from its Claude AI chatbot, and more!

[Last Week in AI](https://substack.com/@lastweekinai)

Jul 4

[![](https://substackcdn.com/image/youtube/w_728,c_limit/l_youtube_play_qyqt8q,w_120/HSC9VZjK3OU)](https://substack.com/redirect/28a4668f-a1ed-4cd5-8c18-ddfd30a58890?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Our 214th episode with a summary and discussion of last week's big AI news!  
Recorded on 06/28/2025

Hosted by [Andrey Kurenkov](https://substack.com/redirect/e7a6708f-7814-4835-900a-f2d265eb4f1a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) and [Jeremie Harris](https://substack.com/redirect/571e1d73-2abd-42cf-bd4a-a5835d3abaaf?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8).  
Feel free to email us your questions and feedback at [contact@lastweekinai.com](https://substack.com/redirect/e1da7c2a-c9c1-40c6-bd16-6c29ad523c6f?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8) and/or [hello@gladstone.ai](https://substack.com/redirect/bcb80f30-4911-4604-896d-8af8bd953f82?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

In this episode:

- Meta's hiring of key engineers from OpenAI and Thinking Machines Lab securing a $2 billion seed round with a valuation of $10 billion.
- DeepMind introduces Alpha Genome, significantly advancing genomic research with a model comparable to Alpha Fold but focused on gene functions.
- Taiwan imposes technology export controls on Huawei and SMIC, while Getty drops key copyright claims against Stability AI in a groundbreaking legal case.
- A new DeepMind research paper introduces a transformative approach to cognitive debt in AI tasks, utilizing EEG to assess cognitive load and recall in essay writing with LLMs.

Timestamps + Links:

- (00:00:10) Intro / Banter
- (00:01:22) News Preview
- (00:02:15) Response to listener comments

Tools &amp; Apps

- (00:06:18) [Google is bringing Gemini CLI to developers’ terminals](https://substack.com/redirect/931c246e-25ac-4a04-8720-b12ab2efbe9a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:12:09) [Anthropic now lets you make apps right from its Claude AI chatbot](https://substack.com/redirect/6f490198-f892-4081-8645-945897e193b2?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Applications &amp; Business

- (00:15:54) [Sam Altman takes his ‘io’ trademark battle public](https://substack.com/redirect/2fd80951-2298-4e92-a38f-ccb8e3a5bff0?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:21:35) [Huawei Matebook Contains Kirin X90, using SMIC 7nm (N+2) Technology](https://substack.com/redirect/af19acc5-e542-430d-9758-e6d5f0889b89?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:26:05) [AMD deploys its first Ultra Ethernet ready network card — Pensando Pollara provides up to 400 Gbps performance](https://substack.com/redirect/30afe534-203f-4db0-8413-9758d8df8baa?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:31:21) [Amazon joins the big nuclear party, buying 1.92 GW for AWS](https://substack.com/redirect/93ed137a-d3d3-4aec-8e3d-f43a690e67fa?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:33:20) [Nvidia goes nuclear — company joins Bill Gates in backing TerraPower, a company building nuclear reactors for powering data centers](https://substack.com/redirect/62fee9b9-13f2-45dc-a531-7e1a30a6ec4a?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:36:18) [Mira Murati’s Thinking Machines Lab closes on $2B at $10B valuation](https://substack.com/redirect/97c93d49-81f4-4da3-9806-27165d9801b9?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:41:02) [Meta hires key OpenAI researcher to work on AI reasoning models](https://substack.com/redirect/e49e3d25-eae9-4346-8617-10b755de6bb9?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Research &amp; Advancements

- (00:49:46) [Google’s new AI will help researchers understand how our genes work](https://substack.com/redirect/f344e64c-415a-4649-8c46-18c118b91ed4?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (00:55:13) [Direct Reasoning Optimization: LLMs Can Reward And Refine Their Own Reasoning for Open-Ended Tasks](https://substack.com/redirect/e1c9bc27-749e-457d-aae3-c11a7a235e25?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:01:54) [Farseer: A Refined Scaling Law in Large Language Models](https://substack.com/redirect/1b86fca4-29da-4ca2-8d28-41da4d86b144?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:06:28) [LLM-First Search: Self-Guided Exploration of the Solution Space](https://substack.com/redirect/24c335c1-1e89-4226-96be-211f4d2b875b?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Policy &amp; Safety

- (01:11:20) [Unsupervised Elicitation of Language Models](https://substack.com/redirect/fcfe287b-7244-4331-adf3-e4e1ec307f94?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:16:04) [Taiwan Imposes Technology Export Controls on Huawei, SMIC](https://substack.com/redirect/7f1fc6d1-ced4-4679-bd17-ca48ca4916ab?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:18:22) [Your Brain on ChatGPT: Accumulation of Cognitive Debt when Using an AI Assistant for Essay Writing Task](https://substack.com/redirect/2614eb14-d44a-42c2-b5af-753f9fd0fb2f?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

Synthetic Media &amp; Art

- (01:23:41) [Judge Rejects Authors’ Claim That Meta AI Training Violated Copyrights](https://substack.com/redirect/8310e133-3c39-4104-bb98-445c5ec9be68?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)
- (01:29:46) [Getty drops key copyright claims against Stability AI, but UK lawsuit continues](https://substack.com/redirect/7bae8660-4453-43c2-aec9-de5a7521e0dd?j=eyJ1IjoiNXM4M296In0.tGNGSdtmlCx12UO5VTFY50vjzjDXKZsMTxKEYVZUdc8)

© 2025 Skynet Today  
548 Market Street PMB 72296, San Francisco, CA 94104
```

<END_EXAMPLE_OUTPUT>
