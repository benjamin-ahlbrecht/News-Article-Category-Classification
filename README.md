# New Article Category Classification

Contextual Advertising describes the process of targeting advertisements to users based on the context of a given website's contents. Here, we tackle this issue using a variety of machine-learning models and a DistilBERT deep-learning model. Decision Trees, Random Forests, and Multinomial Logistic Regression are utilized to make contextual advertising decisions based on pre-processed text data. DistilBERT uses pre-embedded word vectors to help make more rigorous classifications.

## Deployment

This work can be found as a project on my personal site. To find out more about the models, how they perform, were evaluated, and to interact with the DistilBERT model, please visit [`benjamin-ahlbrecht.dev/projects/contextual-advertising`](https://benjamin-ahlbrecht.dev/projects/contextual-advertising).

## Data

We use the [News Category Dataset](https://www.kaggle.com/datasets/rmisra/news-category-dataset) by Rishabh Misra. This contains approximately 210,000 news headlines between 2012 and 2022 from the [Huffington Post](https://www.huffpost.com/). For more information, see the articles below:

```
1. Misra, Rishabh. "News Category Dataset." arXiv preprint arXiv:2209.11429 (2022).
2. Misra, Rishabh and Jigyasa Grover. "Sculpting Data for ML: The first act of Machine Learning." ISBN 9798585463570 (2021).
```

## Usage

To run the Jupyter Notebook yourself, I recommend to use the Kaggle Environment found [here](https://www.kaggle.com/code/benjaminahlbrecht/contextual-advertising-using-ml-dl).

The Article can be locally hosted using [FastAPI](https://fastapi.tiangolo.com/). Begin by cloning the repository:

```bash
# Via SSH
git clone git@gitlab.com:BAhlbrecht/contextual-advertising-ml-dl.git

# Via HTTPS
git clone https://gitlab.com/BAhlbrecht/contextual-advertising-ml-dl.git
```

Next, navigate to the `/app/` directory:

```bash
cd contextual-advertising-using-machine-and-deep-learning/app
```

Finally, you can use [Uvicorn](https://www.uvicorn.org/) to host the application locally:

```bash
uvicorn app:app --reload
```
