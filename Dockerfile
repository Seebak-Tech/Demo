FROM python:3.9

ARG YOUR_ENV=production

# Add user admin
RUN useradd -m -s /bin/bash admin && \
    usermod -aG sudo admin && \
    passwd -d admin 

USER admin

# Declare environment variables
ENV YOUR_ENV=${YOUR_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.6 \
    PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin \
    PATH=$PATH:/usr/bin:/sbin:/bin:/home/admin/.local/bin \
    PYTHONPATH=/demo

# Copy only requirements to cache them in docker layer
WORKDIR /demo

# Creating folders, and files for a project:
COPY --chown=admin demo/ /demo/demo
COPY --chown=admin notebooks/ /demo/notebooks
COPY --chown=admin poetry.lock pyproject.toml /demo/

# Project initialization:
RUN pip install "poetry==$POETRY_VERSION" --user \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
#   && poetry install $(test "$YOUR_ENV" == production && echo "--no-dev") --no-interaction --no-ansi

# Expose port for jupyter lab
EXPOSE 8889

# Start Jupyter lab
ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--port=8889"]
