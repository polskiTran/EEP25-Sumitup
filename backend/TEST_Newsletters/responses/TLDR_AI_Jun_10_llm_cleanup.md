o3-pro is an incremental improvement over o3, which OpenAI slashed its price by 80%, across science, coding, and business tasks

TLDR

# **TLDR AI 2025-06-11**

# **Headlines & Launches**

[**OpenAI Releases o3-pro (2 minute read)**](https://techcrunch.com/2025/06/10/openai-releases-o3-pro-a-souped-up-version-of-its-o3-ai-reasoning-model/)

o3-pro is an incremental improvement over o3, which OpenAI slashed its price by 80%, across science, coding, and business tasks. It's available to Pro and Team users today, replacing o1-pro.

[**Mistral Launches First AI Reasoning Model (2 minute read)**](https://mistral.ai/news/magistral)

Adding to a string of releases over the last 2 weeks, Mistral has launched an open-source reasoning model, Magistral. It trails proprietary models on major benchmarks, but claims to be 10x faster output and stronger multilingual capabilities.

[**Meta Plans $15B Investment in Scale AI to Build 'Superintelligence' Lab (5 minute read)**](https://www.cnbc.com/2025/06/10/zuckerberg-makes-metas-biggest-bet-on-ai-14-billion-scale-ai-deal.html)

The deal would give Meta a 49% stake in the data-labeling startup and bring over co-founder Alexandr Wang to lead a new "superintelligence" lab aimed at outperforming OpenAI, Anthropic, and Google. The massive investment follows Llama 4's underwhelming launch, but it's unclear if the investment also includes greater access to Scale's training data created for other AI labs in addition to highly sought-after AI research talent.

# **Deep Dives & Analysis**

[**Real-World Engineering at Cursor: Building for 100x Growth (11 minute read)**](https://newsletter.pragmaticengineer.com/p/cursor)

Cursor cofounder Sualeh Asif reveals how the two-year-old startup handles 1M+ queries per second without storing any code on its servers, using Merkle trees for secure indexing. The team survived 100x growth by switching databases during outages (Yugabyte → PostgreSQL → Turbopuffer in hours) and built Anyrun, their Rust-based orchestrator, to manage thousands of GPUs.

[**Speculative Decoding in LLMs (19 minute read)**](https://links.tldrnewsletter.com/DOW4tN)

Perplexity applies speculative decoding to speed up its Sonar models, using lightweight draft models to propose multiple tokens verified by larger LLMs.

[**Towards Adaptive Clinical AI via the Consensus of Expert Model Ensemble (20 minute read)**](https://arxiv.org/abs/2505.23075)

Despite the growing clinical adoption of LLMs, current approaches heavily rely on single model architectures. Consensus Mechanism is a novel framework to overcome risks of obsolescence and rigid dependence on single model systems. Mimicking clinical triage and multidisciplinary clinical decision-making, the Consensus Mechanism implements an ensemble of specialized medical expert agents enabling improved clinical decision making while maintaining robust adaptability.

# **Engineering & Research**

[**Mixed-Chip Clusters Enable Efficient Large-Scale AI Training (42 minute read)**](https://arxiv.org/abs/2505.17548)

Shanghai-based researchers introduced DiTorch and DiComm, which unify programming across diverse chip architectures like NVIDIA and AMD variants, making it possible to train massive models on whatever hardware is available. Their framework achieved 116% efficiency training a 100B model on 1,024 chips with vastly different specs by intelligently assigning memory-hungry pipeline stages to larger-memory hardware. This allows labs without access to thousands of identical cutting-edge GPUs to still pursue frontier AI training by combining older, cheaper, or export-controlled chips into effective "hyper-heterogeneous" clusters.

[**Reinforcement Pre-Training (55 minute read)**](https://arxiv.org/abs/2506.08007)

Reinforcement Pre-Training (RPT) is a new scaling paradigm for large language models (LLMs) and reinforcement learning (RL). It offers a scalable method for leveraging vast amounts of text data for general-purpose RL. RPT significantly improves the large model accuracy of predicting the next tokens. It also provides a strong pre-trained foundation for further reinforcement fine-tuning.

[**JavelinGuard: Low-Cost Transformer Architectures for LLM Security (68 minute read)**](https://www.arxiv.org/abs/2506.07330)

JavelinGuard is a suite of low-cost, high-performance model architectures designed for detecting malicious intent in large language model (LLM) interactions. Each architecture presents unique trade-offs in speed, interpretability, and resource requirements. The architectures are optimized specifically for production deployment. This paper explores the architectures, benchmarking them across nine diverse adversarial datasets, and compares them against leading open-source guardrail models and large decoder-only LLMs.

[**Efficient Multimodal Reasoning with Fewer Tokens (GitHub Repo)**](https://github.com/visresearch/LLaVA-STF/tree/main)

LLaVA-STF compresses vision token sequences by merging adjacent tokens and adds a multi-block token fusion module, enabling 75% token reduction.

# **Miscellaneous**

[**Sam Altman Outlines Path to Superintelligence (5 minute read)**](https://blog.samaltman.com/the-gentle-singularity)

In a rare blog post, Sam Altman declares we've passed the "event horizon" with systems like GPT-4 and o3 that already surpass humans in many ways, predicting agents doing real cognitive work in 2025, novel scientific insights in 2026, and useful robots by 2027. He frames the coming decade as one where scientific breakthroughs compound exponentially through AI-accelerated research.

[**What "Working" Means in the Era of AI Apps (3 minute read)**](https://a16z.com/revenue-benchmarks-ai-apps/)

AI startups are growing rapidly, with the average enterprise achieving over $2 million ARR in the first year. Consumer startups are also gaining traction, outpacing B2B by reaching $4.2 million ARR. The disparity between average and top performers is widening, emphasizing the need for speed and innovation.

[**Reimagining TTS with LLM-Powered Audio Generation (11 minute read)**](https://www.bland.ai/blogs/new-tts-announcement)

Bland AI has reimagined text-to-speech (TTS) technology by using large language models to predict audio directly from text, enhancing expressiveness and contextual understanding. This new system leverages two-channel conversational datasets and specialized audio tokenizers for accurate and nuanced speech generation. It supports advanced capabilities like style transfer, sound effect integration, and multilingual adaptation, setting a new standard for expressive synthetic speech.

# **Quick Links**

[**OpenAI Taps Google Cloud in Unprecedented Deal Despite AI Rivalry (3 minute read)**](https://links.tldrnewsletter.com/qcvzW7)

OpenAI's compute demands have grown so massive it's turning to its biggest search competitor for additional capacity, marking its first major cloud partner outside of Microsoft.

[**OpenAI announces 80% price drop for o3, its most powerful reasoning model (4 minute read)**](https://links.tldrnewsletter.com/s1mlmw)

o3 is now a much more accessible option for developers seeking advanced reasoning capabilities.

[**Monthly alternative data report: OpenAI, Google, Meta, Nvidia, Amazon, Microsoft Anthropic (15 minute read)**](https://www.uncoveralpha.com/p/monthly-alternative-data-report-openai)

This article summarizes some of the most valuable insights from various alternative data providers and research reports, covering AI, semiconductors, ad tech, and the cloud industry.

[**OpenAI's open model is delayed (2 minute read)**](https://techcrunch.com/2025/06/10/openais-open-model-is-delayed/)

OpenAI's open model will be released sometime after June.

[**AI-2027 Response: Inter-AI Tensions, Value Distillation, US Multipolarity, & More (19 minute read)**](https://links.tldrnewsletter.com/4zCEMW)

AI-2027 is a heavily researched and influential attempt at providing a concrete forecast on AI capability development and its potential consequences.

[**Evals now supports tool use (2 minute read)**](https://threadreaderapp.com/thread/1932169029147557924.html)

OpenAI users can now use tools and Structured Outputs when completing eval runs and evaluate tool calls based on the arguments passed and responses returned.

Thanks for reading,
[Andrew Tan](https://twitter.com/andrewztan), [Ali Aminian](https://www.linkedin.com/in/aliiaminian/), [Jacob Turner](https://www.linkedin.com/in/jacob-turner-7521a8198/) & [Sahil Khoja](https://www.linkedin.com/in/sahilkhoja/)