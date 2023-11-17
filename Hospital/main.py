import cv2

import os

import time
start_time=time.time()
test_original=[]
test_original = cv2.imread("right_eye.bmp")
cv2.imshow("Original", cv2.resize(test_original, None, fx=1, fy=1))
cv2.waitKey(0)
cv2.destroyAllWindows()
count=0
x=False
for file in [file for file in os.listdir("final")]:
    iris_database_image = cv2.imread("./final/" + file)

    sift = cv2.SIFT_create()

    keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(iris_database_image, None)

    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                                    dict()).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []
    for p, q in matches:
        if p.distance < 0.1 * q.distance:
            match_points.append(p)
        keypoints = 0
        if len(keypoints_1) <= len(keypoints_2):
            keypoints = len(keypoints_1)
        else:
            keypoints = len(keypoints_2)
        if (len(match_points) / keypoints) > 0.95:
            s=1
            print("The input Iris image is matched!!")
            print("percentage(%) of match: ", len(match_points) / keypoints * 100)
            b=time.time()-start_time
            print("the total time taken is :{} Seconds".format(b))
            result = cv2.drawMatches(test_original, keypoints_1, iris_database_image,
                                    keypoints_2, match_points, None)
            result = cv2.resize(result, None, fx=1, fy=1)
            cv2.imshow("result", result)
            cv2.waitKey(10000)
            cv2.destroyAllWindows()
            x=True
            count+=1
            break
    if x:
        break
else:
    print("The input Iris image is not matched!!")

if s==1:







    import socket
    import time
    import struct

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the UR robot
    ip_address = "192.168.168.42"  # replace with the IP address of your robot
    port = 30002  # the default port for sending URScript commands
    port2 = 63352
    port3 = 30003
    s.connect((ip_address, port))


    # define a function to convert degrees to radians
    def deg_to_rad(degrees):
        return degrees * 3.14159 / 180.0


    def check():
        import socket
        import time
        import struct
        ip_address = "192.168.168.42"  # replace with the IP address of your robot
        port = 30002  # the default port for sending URScript commands
        port2 = 63352
        port3 = 30003
        print("starting Program")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((ip_address, port3))
        time.sleep(1.00)
        print(" ")
        packet_1 = s.recv(4)

        packet_2 = s.recv(8)

        packet_3 = s.recv(48)

        packet_4 = s.recv(48)
        packet_5 = s.recv(48)
        packet_6 = s.recv(48)
        packet_7 = s.recv(48)
        packet_8 = s.recv(48)
        packet_9 = s.recv(48)
        packet_10 = s.recv(48)
        packet_11 = s.recv(48)

        packet_12 = s.recv(8)
        x = struct.unpack('!d', packet_12)[0]

        v = x * 10
        g = int(v)
        x = float(g) / 10

        print('X= ', x)

        packet_13 = s.recv(8)
        y = struct.unpack('!d', packet_13)[0]
        v = y * 10
        g = int(v)
        y = float(g) / 10
        print('Y= ', y)

        packet_14 = s.recv(8)
        z = struct.unpack('!d', packet_14)[0]
        v = z * 10
        g = int(v)
        z = float(g) / 10
        print('Z= ', z)

        packet_15 = s.recv(8)
        Rx = struct.unpack('!d', packet_15)[0]
        v = Rx * 10
        g = int(v)
        Rx = float(g) / 10
        print('Rx= ', Rx)

        packet_16 = s.recv(8)
        Ry = struct.unpack('!d', packet_16)[0]
        v = Ry * 10
        g = int(v)
        Ry = float(g) / 10
        print('Ry= ', Ry)

        packet_17 = s.recv(8)
        Rz = struct.unpack('!d', packet_17)[0]
        v = Rz * 10
        g = int(v)
        Rz = float(g) / 10
        print('Rz= ', Rz)

        # s.close()
        i = 0
        while i == 0:
            print("t")
            if (0.3 == x) & (-0.2 == y) & (0.1 == z) & (0.0 == Rx) & (3.1 == Ry) & (0.0 == Rz):  # your

                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip_address, port2))
                time.sleep(1)
                s.sendall(b'SET POS 110\n')
                s.close()
                i = 1
            elif (-0.4 == x) & (-0.1 == y) & (0.0 == z) & (3.0 == Rx) & (0.0 == Ry) & (0.0 == Rz):  # your

                s.close()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip_address, port2))
                time.sleep(1)
                s.sendall(b'SET POS 0\n')
                s.close()
                i = 1

        time.sleep(1.5)


    # define the joint angles for the robot arm
    joint_angles = [0, -90, 0, -90, 0, 0]  # replace with the desired joint angles in degrees

    # convert the joint angles from degrees to radians
    joint_angles = [deg_to_rad(angle) for angle in joint_angles]

    # send a command to move the robot's arm to the desired joint angles
    command = "movej(%s, a=1, v=1)\n" % (joint_angles)
    s.send(command.encode())

    # wait for the robot to finish moving
    time.sleep(6.5)
    # s.close()
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((ip_address, port))
    # define the new joint angles for the robot arm
    joint_angles = [-13.36, -112.05, -46.44, -110.54, 92.86, 75.48]  # replace with the new joint angles in degrees

    # convert the joint angles from degrees to radians
    joint_angles = [deg_to_rad(angle) for angle in joint_angles]
    #
    # # send a command to move the robot's arm to the new joint angles
    command = "movej(%s, a=1, v=1)\n" % (joint_angles)
    s.send(command.encode())
    #
    # # wait for the robot to finish moving
    time.sleep(5.5)
    joint_angles = [-13.34, -115.79, -50.11, -107.10, 89.99, 75.44]
    joint_angles = [deg_to_rad(angle) for angle in joint_angles]
    command = "movej(%s, a=0.2, v=0.2)\n" % (joint_angles)
    s.send(command.encode())
    s.close()

    check()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))

    joint_angles = [0, -90, 0, -90, 0, 0]
    joint_angles = [deg_to_rad(angle) for angle in joint_angles]
    command = "movej(%s, a=1, v=1)\n" % (joint_angles)
    s.send(command.encode())
    time.sleep(7)
    joint_angles = [-5.20, -49.08, 48.40, -93.37, -84.99, 88.48]
    joint_angles = [deg_to_rad(angle) for angle in joint_angles]
    command = "movej(%s, a=1, v=1)\n" % (joint_angles)
    s.send(command.encode())
    time.sleep(7)
    joint_angles = [-4.99, -46.10, 48.51, -95.49, -84.90, 88.48]
    joint_angles = [deg_to_rad(angle) for angle in joint_angles]
    command = "movej(%s, a=0.2, v=0.2)\n" % (joint_angles)
    s.send(command.encode())
    time.sleep(2)
    check()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip_address, port))

    joint_angles = [0, -90, 0, -90, 0, 0]
    joint_angles = [deg_to_rad(angle) for angle in joint_angles]
    command = "movej(%s, a=1, v=1)\n" % (joint_angles)
    s.send(command.encode())

    # s.close()
    # # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # # s.connect((ip_address, port2))
    # # s.sendall(b'SET POS 0\n')
    # # close the socket
    # s.close()
