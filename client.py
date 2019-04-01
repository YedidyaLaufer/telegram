#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyrogram import Client, Filters
import requests
import re

__author__ = 'ידידיה לאופר'
__version__ = '1.1.0'

app = Client("Yedidya Laufer")
upload_url = 'https://upload.cdncv.net/upload/01'
download_url = "https://cloudvideo.tv/"
video_types = ['avi', 'mkv', 'mpg', 'mpeg', 'vob', 'wmv', 'flv', 'mp4', 'mov', 'm4v', 'm2v', 'divx', 'xvid', '3gp',
               'webm', 'ogv', 'ogg', 'ts']


@app.on_message(Filters.document)
def my_handler(client, message):
    pass
    if message.document:
        print("got document")
        if is_movie(message.document.file_name):
            print("is movie", message.document.file_name)
            # print(dir(message.document))
            message.reply("""קיבלתי👍
מתחיל להוריד...📥""")
            down_path = client.download_media(message=message, progress=progress)
            if down_path is None:
                print("error in download")
                breakpoint()
            print("downloaded")
            message.reply("""ההורדה הסתיימה👌
מעלה לצפיה ישירה⬆️""")
            name = down_path.split('\\')[-1]
            link = upload_file(down_path, name)
            message.reply("""הנה קישור לסרט שלך
בצפיה ישירה ⛓""" + '\n' + link)
            # print(down_path)
        else:
            message.reply("""מצטער,😕
זה לא קובץ של סרט🤷🏼‍♂️""")


def is_movie(st):
    end = st.split('.')[-1]
    if end in video_types:
        return True
    return False


def upload_file(file_path, file_name):
    fil = open(file_path, 'rb')
    multipart_form_data = {'file': (file_name, fil)}

    response = requests.post(url=upload_url, files=multipart_form_data)

    a = re.search('textarea name="fn"\>.+?\<', response.text)
    return download_url + a.group().split('textarea name="fn">')[-1][:-1]


def progress(client, current, total):
    print('{} out of {}'.format(current, total))


app.run()
