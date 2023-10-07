import json
from flask import Flask, jsonify, request
import time
import pinVariables as pin

# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(pin.alertBulbPin,GPIO.OUT)
# GPIO.setup(pin.sirenPin,GPIO.OUT)
# GPIO.setup(pin.ignitorPin,GPIO.OUT)
# GPIO.setup(pin.servoPin, GPIO.OUT)
# sevo = GPIO.PWM(pin.servoPin, 50)


app= Flask(__name__)

@app.route('/',methods=['GET'])
def get_home():
    response = {"message":"Welcome to Electronics Division Backend!!",
                "status":200}
    return jsonify(response)

#................Alert System ........................................................
@app.route('/alert/bulb/start',methods=['GET'])
def startAlertBulb():
    try:
        # GPIO.output(pin.alertBulbPin,GPIO.HIGH)
        response = {"message":"Alert Bulb Started!!",
                "status":200}
        return jsonify(response),200
    except:
        error = {"message":"Could not start Alert Bulb!!",
                "status":400}
        return jsonify(error),400

@app.route('/alert/bulb/stop',methods=['GET'])
def stopAlertBulb():
    try:
        # GPIO.output(pin.alertBulbPin,GPIO.LOW)
        response = {"message":"Alert Bulb Stopped!!",
                "status":200}
        return jsonify(response),200
    except:
        error = {"message":"Could not stop Alert Bulb!!",
                "status":400}
        return jsonify(error),400

@app.route('/alert/siren/start',methods=['GET'])
def startAlertSiren():
    try:
        # GPIO.output(pin.sirenPin,GPIO.HIGH)
        response = {"message":"Alert Siren Started!!",
                "status":200}
        return jsonify(response),200
    except:
        error = {"message":"Could not start Alert Siren!!",
                "status":400}
        return jsonify(error),400
    
@app.route('/alert/siren/stop',methods=['GET'])
def startAlertSystem():
    try:
        # GPIO.output(pin.sirenPin,GPIO.HIGH)
        response = {"message":"Alert Siren Stopped!!",
                "status":200}
        return jsonify(response),200
    except:
        error = {"message":"Could not stop Alert Siren!!",
                "status":400}
        return jsonify(error),400

#........................Ignitor and Servo....................................
@app.route('/ignitor/start',methods=['GET'])
def startIgnition():
    try:
        # GPIO.output(pin.ignitorPin,GPIO.LOW)
        response = {"message":"Ignitor Started!!",
                "status":200}
        return jsonify(response),200
    except:
        error = {"message":"Could not start Ignitor",
                "status":400}
        return jsonify(error),400

@app.route('/ignitor/start',methods=['GET'])
def stopIgnition():
    try:
        # GPIO.output(pin.ignitorPin,GPIO.HIGH)
        response = {"message":"Ignitor Stopped!!",
                "status":200}
        return jsonify(response),200
    except:
        error = {"message":"Could not stop Ignitor",
                "status":400}
        return jsonify(error),400
    
@app.route('/retract-servo',methods=['GET'])
def stopIgnition():
    try:
        # servo.start(8)
        # servo.changeDutyCycle(2)
        # time.sleep(0.2)
        # servo.stop()
        # GPIO.output(pin.ignitorPin,GPIO.HIGH)

        response = {"message":"Ignitor Retracted!!",
                "status":200}
        return jsonify(response),200
    except:
        error = {"message":"Could not retract Ignitor",
                "status":400}
        return jsonify(error),400
    

if __name__ == '__main__':
    app.run(port = 5000)