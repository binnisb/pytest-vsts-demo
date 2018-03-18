FROM continuumio/miniconda3

MAINTAINER Brynjar Smári Bjarnason <binni@binnisb.com>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Set the ENTRYPOINT to use bash
# (this is also where you’d set SHELL,
# if your version of docker supports this)
ENTRYPOINT ["/bin/bash", "-c" ]

# Use the environment.yml to create the conda environment.
ADD environment.yml /tmp/environment.yml

ADD . /code

WORKDIR /code

RUN conda env update --quiet -n base --file=/tmp/environment.yml && \
    /opt/conda/bin/pip install . && \
    conda clean -tipsy
