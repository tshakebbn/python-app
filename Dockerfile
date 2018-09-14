FROM nginx:1.14

RUN apt-get -y update && apt-get install -y build-essential python python-dev \
python-pip doxygen

RUN pip install appdirs doxypypy

RUN useradd -m tempuser

COPY . /home/tempuser/python-app

RUN chown -R tempuser:tempuser /home/tempuser/python-app

WORKDIR /home/tempuser/python-app/

USER tempuser

RUN python setup.py build

RUN python setup.py test

USER root

RUN python setup.py install

USER tempuser

RUN doxygen Doxyfile

USER root

RUN cp -r ./docs/html/* /usr/share/nginx/html/

