name: PyLint
 
on: [push, pull_request]
 
jobs:
  PEP8:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
 
      - name: Setup Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.8
 
      - name: Install Python lint libraries
        run: |
          pip install autopep8 autoflake isort black
      - name: Check for showstoppers
        run: |
          autopep8 --verbose --in-place --recursive --aggressive --aggressive --ignore=W605. *.py
      - name: Remove unused imports and variables
        run: |
          autoflake --in-place --recursive --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports .
      - name: lint with isort and black
        run: |
          isort .
          black .
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: 'pylint: auto fixes'
          commit_options: '--no-verify'
          repository: .
          commit_user_name: AftahBagas
          commit_user_email: aftahbagas21@gmail.com
          commit_author: AftahBagas <aftahbagas21@gmail.com>
