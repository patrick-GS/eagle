# Docker Tag Images, Using Python Slim Buster 3.9
FROM eagleprojects/Ganesha:Buster
# ==========================================
#              USERBOT TELEGRAM
# ==========================================
RUN git clone -b Ganesha-Userbot https://github.com/eagleprojects/Ganesha /home/Ganesha \
    && chmod 777 /home/Ganesha \
    && mkdir /home/Ganesha/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/Ganesha/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/eagleprojects/Ganesha/Ganesha/requirements.txt
WORKDIR /home/Ganesha/

# Finishim
CMD ["bash","./resource/startup/startup.sh"]
