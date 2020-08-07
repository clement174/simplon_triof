import os
import json
import random
import requests


def open_waste_slot():
    """
        open the machine so that
        an user can enter the machine

    :return:
    """

    send_command_to_machine("open_waste_slot")
    return True


def close_waste_slot():
    """
    close the waste box for user safety
    :return:
    """

    send_command_to_machine("close_waste_slot")
    return True


def process_waste(waste_type):
    """
    move the good slot and shredd the waste
    :return:
    """

    move_container(waste_type)
    was_sucessful = shred_waste()

    return was_sucessful


def move_container(waste_type):

    GLASS = 0
    METAL = 1
    PLASTIC = 2
    TRASH = 3
    command_name = "move_container"

    if waste_type == "glass":
        send_command_to_machine(command_name, GLASS)
    elif waste_type == "metal":
        send_command_to_machine(command_name, METAL)
    elif waste_type == "plastic":
        send_command_to_machine(command_name, PLASTIC)
    else:
        send_command_to_machine(command_name, TRASH)

    return True


def send_command_to_machine(command_name, value=None):
    """
    simulate command sending to rasberry pi
    do nothing to work even if the machine is not connected

    :param command_name:
    :param value:
    :return:
    """
    return True



def shred_waste():

    send_command_to_machine("shred_waste")

    return True


def take_trash_picture():
    """
        function simulating the picture taking
        inside the machine. 

        Call this function to ask the machine to 
        take picture of the trash

        return : np array of the picture
    """

    send_command_to_machine("take_picture")

    paths = os.listdir('camera')
    path = random.choice(paths)

    return os.path.join("./camera", path)

def classify_waste(trash_picture, api_key):

    # request to azure custom vision
    url = "https://projet-integration-flask.cognitiveservices.azure.com/customvision/v3.0/Prediction/59707176-85d0-4dc2-beac-8df8846b917f/classify/iterations/Iteration1/image"
    header = {
        "Prediction-Key": api_key,
        "Content-Type": "application/octet-stream"
    }
    with open(trash_picture,  'rb') as f:
        r = requests.post(url=url, headers=header, data=f.read())
        predictions = json.loads(r.content)['predictions']

    label_pred = predictions[0]['tagName']

    return label_pred
