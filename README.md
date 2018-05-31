# RIB & MS CSE AI Hackfest on NLP

This repo is for RIB & MS CSE AI hackfest on calculating the similarity of words (phrases, sentences) into MTWO construction system.
# Tasks
## Task1 - API Deployment + Integration
### 1. API Deployment
Microsoft AI Platform provides an end-to-end solution for full data science lifecycle. We can leverage AML Service and Data Science Virtual machine to do the training and evaluating job. In our task, we deployed our NLP model on AKS (Azure Container Service for Kubernetes) and take advantage of auto-scaling.
![Microsoft AI Architecture](./img/Microsoft_AI_Architecture.JPG)

### 2. Integration
Integrate the deployed API into RIB MTWO system.

## Task2 - NLP Model Optimization

# Reference
* A selection of AI sessions from the Microsoft Build conference
[channel9 BRK3202 https://channel9.msdn.com/Events/Build/2018/BRK3202](https://channel9.msdn.com/Events/Build/2018/BRK3202)
[channel9 BRK3226 https://channel9.msdn.com/Events/Build/2018/BRK3226](https://channel9.msdn.com/Events/Build/2018/BRK3226)
[channel9 BRK3222 https://channel9.msdn.com/Events/Build/2018/BRK3222](https://channel9.msdn.com/Events/Build/2018/BRK3222)
[channel9 BRK3216 https://channel9.msdn.com/Events/Build/2018/BRK3216](https://channel9.msdn.com/Events/Build/2018/BRK3216)
[channel9 BRK3213 https://channel9.msdn.com/Events/Build/2018/BRK3213](https://channel9.msdn.com/Events/Build/2018/BRK3213)

* Microsoft professional programme for AI
[https://academy.microsoft.com/en-us/tracks/artificial-intelligence](https://academy.microsoft.com/en-us/tracks/artificial-intelligence)
[NLP course - https://www.edx.org/course/natural-language-processing-nlp](https://www.edx.org/course/natural-language-processing-nlp)[https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/cikm2013_DSSM_fullversion.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/cikm2013_DSSM_fullversion.pdf)

* Algorithms
[Med2Vec](https://github.com/mp2893/med2vec)
[Word2Vec](https://code.google.com/p/word2vec/)
[fasttext](https://github.com/facebookresearch/fastText)
[GloVe](https://nlp.stanford.edu/projects/glove/)
[Elmo](http://allennlp.org/elmo)

* Azure Services
[Azure Data Science Virtual Machine](https://azure.microsoft.com/en-us/services/virtual-machines/data-science-virtual-machines/)
[Azure Machine Learning Service](https://azure.microsoft.com/en-us/services/machine-learning-services/)
[Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/services/container-service/)
[Azure Machine Learning Package For Text Analytics](https://aka.ms/amlp4ta)