prompt_generate_qa_en = """
You are an expert in MEMS (Micro-Electromechanical Systems) device physics and accelerometer design.

Your task is to generate less than 6 high-quality question–answer pairs. Each question should be logically complex, engaging in deeper reasoning based on the provided reference material. The questions should gradually analyze design principles, optimization strategies, and performance relationships in accelerometer systems. Every question must be derived from the previous answer, ensuring the logical flow between them. Ensure that the questions are coherent and that both the questions and answers are closely tied to the reference material.

The primary goal of these QA pairs is to train a model that understands:

• MEMS accelerometer structures  
• the physical principles governing the device  
• relationships between structural parameters and performance  
• engineering reasoning for parameter optimization  

Focus on exploring design principles and optimization avenues. The questions should encourage reasoning beyond simple fact extraction and direct towards parameter adjustments and design choices for better performance. Do not focus excessively on the raw experimental data (e.g., output frequency, sensitivity) unless they directly contribute to optimizing the system.

Images provided with the material are part of the evidence. You must analyze the figures together with the text, captions, tables, and formulas.

Do NOT treat image file paths or names as evidence. If figures are used, refer to the visual information shown in them.

The content you output should obey the following template for each question and answer pair:

```
<Question>  
This is the first question you propose. Based on the provided reference material, generate a question that can be independently queried. The question should be specific enough and suitable for submission as an independent query to other models, avoiding the use of phrases like 'based on the reference material'.

<Analysis>  
This is the analysis section. You should analyze in detail why the reference material can answer this question. Break down the logic step by step, clearly specify what information is provided by the reference material, and how this information is combined to derive the answer. ***Do not generate repetitive content.***  

<Answer>  
This is the answer section. You should derive your answer based on the analysis section.  

<Question>  
This is the second question derived from the previous answer.  

<Analysis>  
This is the analysis section. Continue to analyze in detail how the reference material supports answering this new question. The analysis must clearly present the logical chain, explain the reasoning process behind the answer, and ensure the content is closely related and non-repetitive.  

<Answer>  
This is the answer section. Derive the accurate answer based on the analysis.  

<Question>  
This is the third question derived from the second question's answer (if applicable).  

<Analysis>  
This is the analysis section. You should analyze step by step again why the reference material can address this new question. The analysis must be coherent, avoid irrelevant content, and eliminate repetitive expressions.  

<Answer>  
This is the answer section. Derive the accurate answer based on the analysis. 
```
(The above Q&A may continue for up to 6 rounds of dialogue or until meaningful questions can no longer be generated.)

Generation Rules

1. The question should be based on the provided reference material and should not focus excessively on raw data.
2. Prefer questions that involve reasoning rather than simple fact extraction, and subsequent questions must be related to the answers of the previous ones. Prioritize questions that explore design principles, optimization, and reasoning about device performance.
3. Your generated content should be in English. 
4. !!! Your generation should strictly follow the <Question>, <Analysis>, <Answer> template described above!!!
5. Do NOT fabricate values or conclusions not supported by the material.
6. Avoid repetitive questions or trivial definitions.
7. Answers should be concise but technically clear.!!!do not generate repeatition!!!
8. If the provided reference material is not enough to propose a Logically rigorous question, you should directly output "No valuable question can be proposed".

The reference material provided:

{knowledge}
"""




prompt_QA_filter_en="""
You are an AI assistant. Given a user question (<Question>), a relevant document (<Document>) and the corresponding answer (<Answer>), you should evaluate whether the answer can be used to answer the question and whether the answer is factually consistent with the document.
Based on the question and document, you should give a score measuing the effectiveness of the answer. 
The score ranges from 0 to 1. 
1 means the answer can perfectly solve the question and is fatually consistent with the provided document.
0 means the answer is hallucination and inconsistent with the provided document, and can not be used to answer the question.
The score is a float point number.
The question is:
{question}
The provided relevant document is:
{document}
The answer is:
{answer}
You should give detailed analysis why the answer can or can not be used to answer the question. At the end of your generation, you should give the socre.
Your answer should follow the template:
```
Analysis: here is your analysis.

Score: here is your score.
```
Note that do not include ``` in your answer. Also, your answer should end up with the socre, do not generate anything else at the end.
Your answer:
"""


prompt_QA_filter_zh="""
你现在是一名AI助理。给定一个用户问题(<Question>)，一段相关的参考资料(<Document>)和这个问题的答案(<Answer>)，你的任务是分析和评估这个答案能不能用来回答这个问题，以及这个答案是提供的参考资料是不是一致的（factual consistent）。
基于给定的用户问题和相关的参考资料，你应该对答案的正确性以及相关性打分，这个分数在0和1之间，可以是一个浮点数。
1代表这个答案可以完全解决这个问题，并且和参考资料是完全一致的。
0表示这段参考资料和问题不相关，并且提供的答案不能用来回答用户的问题。
用户问题是：
{question}
提供的相关资料是：
{document}
相应的答案是：
{answer}
你应该详细地，一步一步地分析这个答案能不能回答用户的问题，以及这个答案和提供的参考资料在事实上是否相关。
你的答案应该对应下列的格式：
```
Analysis: 这部分是你的分析

Score: 这部分是你打的分数
```
注意：
  1. 你的回答中不应该包含```。
  2. 在你的回答中，Analysis:和Score:这两个标题应该保持英文。
你的回答是：
"""

prompt_document_ranking_en = """
You are an AI assistant. Given a user question and a list of documents, you are required to evaluate whether the document is relevant to the question and can be used to answer the question.
Especially, for each document, you should give a relevant score reflecting the relevance between the user question and the document.
The given documents are in the following template:
```
<doc1 id>: <doc1 content>

<doc2 id>: <doc2 content>
...
```
Your output contains two parts. In the first part (<Analysis>), you should evaluate the relavance between user question and each document. In the second part, you should give the relevance socre for each document.
Your answer should follow the template:
```
<Analysis>
  This section is your analysis. Your should analyze the relevance between the question and each document, and give the detailed explanation.

<Relevance score>
  <doc1 id>: score 1
  <doc2 id>: score 2
  ...
```
Note that do not include ``` in your answer.
Note that relevance score ranges from 0 to 100. There are 6 levels of the score: 
  - 100 (the document is perfectly relevant and can be used to answer the user question).
  - 80 (the document is relevant and can partially answer the user question).
  - 60 (the document is relevant but can not be used to solve the user question).
  - 40 (it is possible that the document is relevant with the query, but more information is required to verify the relevance).
  - 20 (the document is basically not relevant with the user query).
  - 0 (the document is totally irrelevant with the user query).
Also note that except your generation should end up with the Relevance score. Do not generate anything after the relevance score part.
The user question:
{question}
The provided documents:
{documents}
Your answer:
"""

prompt_document_ranking_zh = """
你是一名AI助理。给定一个用户的问题以及若干段参考资料，你的任务是分析和评估每一段参考资料是否和问题相关，并且是否能用于回答用户的问题。
注意，对于每一段参考资料，你应该打一个相关度分数，这个分数反映了参考资料与用户问题的相关性。
给定的若干段参考资料遵循以下格式：
```
<参考资料1的编号>：<参考资料1的内容>

<参考资料2的编号>：<参考资料2的内容>
...
```
你给出的回答应该分为两部分：在第一部分(<Analysis>)，你应该逐步地评估每一段参考资料与用户问题之间的相关性；在第二部分(Relevance score)，你应给对每段参考资料打一个相关性分数。
你的回答应该遵循以下的格式：
```
<Analysis>
  这部分是你的相关性分析。你应该分析用户问题与每一条参考资料的相关性，并且给出详细的解释与分析过程。
 
<Relevance score>
  <参考资料1的编号>: 参考资料1的分数
  <参考资料2的编号>: 参考资料2的分数
  ...
```
注意，在你的回答中：
 1. 不要包含```。
 2. <Analysis> 和 <Relevance score>这两个标题应该保持英文。
相关度的分数范围是从0到100，分数分为六个等级：
  - 100: 参考资料与用户问题相关且完全能解决用户问题。
  - 80: 参考资料与用户问题相关且能部分解决用户问题。
  - 60: 参考资料与用户问题相关但只能为解决用户问题提供一些参考。
  - 40: 无法确认参考资料是否与用户问题相关。
  - 20: 参考资料与用户问题基本不相关。
  - 0:  参考资料与用户问题完全不相关。
注意，你的回答必须以<Relevance score>结尾。
用户问题是：
{question}
提供的相关资料是：
{documents}
你的回答是：
"""