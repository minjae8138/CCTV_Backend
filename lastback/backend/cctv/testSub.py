import paho.mqtt.client as mqtt;
import PIL
import PIL.Image as pilimg
from PIL import Image
import datetime
import ast
import os

from regi import face
import regi.yolo.yolo_model as yolo
from regi import db_user
from regi.fcm_notification import send_to_firebase_cloud_messaging

sensor = [0,0]

def on_connect(client, userdata, flags, rc):
    print("connect.." + str(rc));
    if rc == 0:  # 0이 정상 연결 -> 구독신청
        client.subscribe("mydata/whoareyou/#");  # Topic명
    else:
        print("연결 실패");

def on_message(client, userdata, msg):
    global sensor
    date_time = datetime.datetime.now()
    filePath = 'C:/Users/shi95/PycharmProjects/lastback3/backend/whoareyou/rasberry/' + '3.jpg'  # 이곳에 사진을 저장할 절대경로를 적으세요
    if msg.topic == 'mydata/whoareyou/getimage':
        data = ast.literal_eval(msg.payload.decode())
        frame = data[0]
        filename = data[1]
        filePath = 'C:/Users/shi95/PycharmProjects/lastback3/backend/whoareyou/rasberry/' + filename  # 이곳에 사진을 저장할 절대경로를 적으세요
        f = open(filePath, "wb");
        f.write(frame);
        f.close();
        print('사진저장완료')
        print(filename)
        keypad_touched_time = 0
        doorhandle_touched_time = 0
    elif msg.topic == 'mydata/whoareyou/getkeypad':
        data = ast.literal_eval(msg.payload.decode())
        keypad_touched_time = data[1]
        sensor[0] = 1
        print('방문자가 키패드를 만졌습니다!!!!!!!' + keypad_touched_time)
    elif msg.topic == 'mydata/whoareyou/getdoorhandle':
        data = ast.literal_eval(msg.payload.decode())
        doorhandle_touched_time = data[1]
        sensor[1] = 1
        print('방문자가 문고리를 돌렸습니다!!!!!!!'+doorhandle_touched_time)
        # print(keypad_touched_time)
    #face4
    setList = yolo.obj()
    # deepface
    f_category, user_id = face.face_recognition(filePath)
    # 센서
    #sensor = [keypad_touched_time, doorhandle_touched_time]
    # 위험도
    danger = yolo.danger(setList, f_category, sensor)
    print("da",danger)
    if danger  and int(danger) > 0 :
        send_to_firebase_cloud_messaging()
    print('d',danger)
    print('f',f_category)

    if filePath and danger and f_category and user_id :
        log_data = (filePath, date_time, int(danger), int(f_category),0, int(user_id))
        print('logggggggggg',log_data)
        db_user.insert_log(log_data)

    return danger

mqttClient = mqtt.Client();
mqttClient.on_connect = on_connect;
mqttClient.on_message = on_message;
mqttClient.connect("192.168.0.63", 1883, 60);
