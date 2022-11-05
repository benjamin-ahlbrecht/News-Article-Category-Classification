# Project Template

_Project Template_ serves as the base for any machine-learning, AI, or other data-oriented project on my (in development) personal site, found on GitLab [here](https://gitlab.com/ahlbrecht-machine-learning/site). It is built to be served as a micro-service in the form of a single Docker container.

We provide a [FastAPI](https://fastapi.tiangolo.com/) backend, which is connected to a relatively simple JavaScript and HTML/CSS front-end.

This template is incomplete and is subject to heavy change in the upcoming weeks or months. As such, usage is limited.

## Usage

To use the _Project Template_, begin by forking or cloning the repository with SSH or HTTPS:

```bash
# Via SSH
git clone git@gitlab.com:ahlbrecht-machine-learning/project-template.git
cd 'project-template/app'
```

```bash
# Via HTTPS
git clone https://gitlab.com/ahlbrecht-machine-learning/project-template.git
cd 'project-template/app'
```

To deploy the web server locally, we use [Uvicorn](https://www.uvicorn.org/) but other options may work as-well. Uvicorn can be installed via `pip` as

```bash
pip install uvicorn
```

To begin development on the project, we can simply call uvicorn on `project-template/app/main.py`:

```bash
uvicorn main:app --reload
```

The `--reload` flag ensures that the API is restarted whenever a change is made in the repository. This helps to track immediate changes to the application. When the API is complete, however, it is preferable to run Uvicorn without the `--reload` flag:

```bash
uvicorn main:app --host='localhost' --port='8000'
```

## Project Development

When working on a project, there are a few considerations to keep in mind. Consider the repository file structure below:

```bash
./project-template/app
├── __init__.py
├── main.py
├── README.md
├── scripts
│   ├── progress-bar.js
│   └── table-of-contents.js
├── static
│   └── styles.css
└── templates
    └── projects
        ├── project.html
        └── template.html
```

`main.py` is the primary location of the Python API: our project back-end. This contains all API routing information and is meant to be utilized for interfacing with project models, visualizations, or results.

`main.py` also maintains a path to our front-end HTML: `templates/projects/project.html`. Here, you can build interfaces to show-case, explain, and interact with your project. The HTML connects to the CSS style sheet found in `static/styles.css` and utilizes simple JavaScript functionality found in `scripts/*`.

It is important to note that `main.py` is best used as the API router. Separate application code can be created elsewhere. For instance, if you have a series of Python scripts encapsulating a machine-learning pipeline, it would be preferable to store them together as a sibling of the `/app` directory:

```bash
.
├── app
│   └── ...
│
├── pipeline
│   ├── data-exploration.py
│   ├── data-ingestion.py
│   ├── data-preprocess.py
│   ├── __init__.py
│   ├── models.py
│   └── pipeline.ipynb
└── README.md
```

Pipeline functions can then be directly called within the API to process requests, avoding a cluttered `main.py`.
