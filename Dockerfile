FROM nginx:1.14

RUN apt-get -y update && apt-get install -y build-essential python python-dev \
python-pip python-sphinx

RUN pip install appdirs sphinxcontrib-napoleon

RUN useradd -m tempuser

COPY . /home/tempuser/python-app

RUN chown -R tempuser:tempuser /home/tempuser/python-app

WORKDIR /home/tempuser/python-app/docs

RUN make html

RUN cp -r ./_build/html/* /usr/share/nginx/html/

CMD tail -f /dev/null
