# Environment setup
You will need Python on your machine.

1. Create a virtual environment
    ```bash
    python3 -m venv ENV
    ```
2. Activate the virtual environment
    - For Windows:
      ```bash
      .\ENV\Scripts\activate
      ```
    - For macOS and Linux:
      ```bash
      source ENV/bin/activate
      ```
3. Upgrade pip
    ```bash
    python -m pip install --upgrade pip
    ```
3. Install packages
    ```bash
    pip install -r requirements.txt
    ```

# Pull a new project phase
Make sure to commit all your current changes before the following steps.
```bash
git checkout -b UCR-CS182-main main
git pull https://github.com/UCR-CS182/<project_template_repo>.git main
git checkout main
git merge --no-ff UCR-CS182-main
git push origin main
```

# Running tests on your local machine
Make sure your virtual environment is avtivated.

Change directory to your project root directory before starting.

```bash
python -m PathExtractor.<filename_without_extension_of_module_under_test>
```
or
```bash
pytest tests/
```
