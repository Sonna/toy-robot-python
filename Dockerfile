FROM python:latest

RUN curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
ENV PATH="/root/.pyenv/bin:$PATH"
RUN eval "$(pyenv init -)"
RUN eval "$(pyenv virtualenv-init -)"

# RUN pyenv install 2.6.9
RUN pyenv install 2.7.10
RUN pyenv install 3.2.6
RUN pyenv install 3.3.6
RUN pyenv install 3.4.3
RUN pyenv install 3.5.0
RUN pyenv install 3.6.1

RUN pip install --upgrade virtualenv
RUN pip install tox
