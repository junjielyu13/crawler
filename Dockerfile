FROM python:3.9.13-bullseye

# Copy composer.lock and composer.json 
COPY composer.lock composer.json /var/www/


RUN pip install Django \
    && pip install flask \
    && pip isntall psycopg2 \
    && pip install urllib3 \
    && pip install bs4 \
    && pip install scrapy \
    && pip install selenium \
    && pip install numpy 

# set working directory
WORKDIR /var/www

# Copy existing application directory contents
COPY . /var/www/

# Change current user to www
USER www

# Expose port 9000 abd start python server
EXPOSE 9000
CMD ["python"]