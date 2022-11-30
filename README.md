# Project Template

_Project Template_ serves as the base for any machine-learning, AI, or other data-oriented project on my (in development) personal site, found on GitLab [here](https://gitlab.com/ahlbrecht-machine-learning/site). It is built to be served as a micro-service in the form of a single Docker container.

We provide a [FastAPI](https://fastapi.tiangolo.com/) backend, which is connected to a relatively simple JavaScript and HTML/CSS front-end.

This template is incomplete and is subject to heavy change in the upcoming weeks or months. As such, usage is limited.

## Installation and Usage

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
./project-template
├── app
│   ├── app.py
│   ├── html
│   │   ├── index.html
│   │   └── template.html
│   ├── __init__.py
│   ├── scripts
│   │   ├── progress-bar.js
│   │   └── table-of-contents.js
│   └── static
│       └── styles.css
├── data
├── models
├── README.md
└── src
    └── main.py
/
```

Each sibling directory is meant to serve its own purpose:

- `app` is the directory containing our local FastAPI application. It is a pruned version of the full application found on my [personal site](https://gitlab.com/ahlbrecht-machine-learning/site). Thus, it is meant to allow the user to preview work with HTML and CSS styling as it would be viewed online.
  - To view changes, launch the application with Uvicorn and edit `app/html/index.html`.
- `data` is meant to hold training data used in data analysis, visualization, or model training.
- `models` can be used to physically store machine-learning models. If you wish to deploy models as a docker image, I recommend dockerizing the model and utilizing [Typer](https://typer.tiangolo.com/) to interface with it from the command line.
- `src` is where project development occurs. `main.py` is the main interface for our machine-learning application.
