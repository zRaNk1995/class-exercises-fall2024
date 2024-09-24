# README

## Get Situated
On GitHub:
* sync your fork

On your local machine:
* Navigate to your `csci338/class-exercises-fall2024` directory
* Check that everything is already committed and pushed to your remote branch
* Checkout `main`
* Pull down the latest code (`git pull`)
* Create a new branch from main called topic05: `git branch -b topic05`



## Set Up
1. Create a new Poetry project: `poetry init -y`
2. Install the following dependencies with `poetry add`

```
pytest
black
flake8
isort
```

## Run the app and the tests:
Navigate back into the `topic05` directory on the command line. Then type the following:

```bash
poetry run python app/main.py       # runs the app
poetry run pytest -v                # runs the tests
```

Now, open `tests/test_main.py` and take a look at it. Uncomment the tests one by one.
* What do you think the decorators do?
* Why is it important to create test mocks?

## Refactor Your Code

### Organize code for doing math
1. Create a new Python class called `Arithmetic`
2. Move your `add_nums` into `Arithmetic` (and convert it into a method)
3. Fix your tests so that they work again


### Organize code for interacting with the user
1. Create a new Python class called `UserInterface`
2. Move your `add_nums_from_user_input` into `UserInterface` (and convert it into a method)
3. Fix your tests so that they work again


## Static Analysis
1. Run the import sorter check: `poetry run isort . --check-only`
1. Run the import sorter fix: `poetry run isort`
2. Run black `poetry run black .`
3. Run flake8: `poetry run flake8`