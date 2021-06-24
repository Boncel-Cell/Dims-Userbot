# DIMS USERBOT
FROM koala21/kampangbot:buster

#
# DIMS
#
RUN git clone -b main https://github.com/Boncel-Cell/kontoll /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Boncel-Cell/kontoll/main/requirements.txt

CMD ["python3","-m","userbot"]
