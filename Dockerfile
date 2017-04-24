FROM continuumio/miniconda3

MAINTAINER Brynjar Smári Bjarnason <binni@binnisb.com>

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Set the ENTRYPOINT to use bash
# (this is also where you’d set SHELL,
# if your version of docker supports this)
ENTRYPOINT ["/bin/bash", "-c" ]

# Use the environment.yml to create the conda environment.
ADD environment.yml /tmp/environment.yml

WORKDIR /tmp

RUN ["conda", "env", "create" ]

ENV PATH /opt/conda/envs/test_stuff/bin:$PATH

ADD . /code

# Use bash to source our new environment for setting up
# private dependencies—note that /bin/bash is called in
# exec mode directly
WORKDIR /code
RUN ["/bin/bash", "-c", "python setup.py install" ]
ENTRYPOINT ["/bin/bash", "-c" ]
