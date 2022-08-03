#!/usr/bin/python3
""" lockboxes challenge """


def check_box(dic_box):
    """ check if there are any open boxes """
    list_keys = []
    for k, v in dic_box.items():
        if "t" in v:
            list_keys = v["t"]
            for i in list_keys:
                if dic_box[i] != "ok" and "f" in dic_box[i]:
                    dic_box[i]["t"] = dic_box[i]["f"]
                    del dic_box[i]["f"]
            dic_box[k] = "ok"


def canUnlockAll(boxes):
    """ function that unlocks boxes """
    status = True
    number_boxes = len(boxes)
    count = 0
    dic_box = {0: {"t": boxes[0]}}
    for i in range(1, number_boxes):
        dic_box[i] = {"f": boxes[i]}
    while count <= number_boxes:
        count += 1
        check_box(dic_box)
    for k, v in dic_box.items():
        if v != "ok":
            status = False
    return status
