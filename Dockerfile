FROM jupyter/datascience-notebook:latest
USER root

# install R packages for data cleaning
RUN R -e "install.packages(c('tidyverse', 'utils', 'jsonlite', 'glue','devtools','janitor'), repos = 'http://cran.us.r-project.org')"
# install R packages for modelling
RUN R -e "install.packages(c('xgboost', 'lightgbm', 'caret', 'tidymodels', 'keras'), repos = 'http://cran.us.r-project.org')"

# install xgboost, lightgbm, tensorflow
RUN conda update -n base conda && \
    conda install --yes gcc_linux-64&& \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
RUN pip install --quiet --no-cache-dir xgboost && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    pip install lightgbm && \
    pip install --upgrade tensorflow && \
    pip install keras

EXPOSE 8888