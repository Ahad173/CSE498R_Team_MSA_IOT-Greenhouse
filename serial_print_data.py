#!/usr/bin/python
import serial
from datetime import datetime 
import csv

if __name__ == '__main__':
    try:
        ser = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
        ser.flush()
    except:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        ser.flush()
    count=1
    print("Working!")
    while True:
        
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            #print(line)
            
            if count >1:
                f=open("Stored_Data.csv","a",newline="")
                w = csv.writer(f)
                data = line.split(";")
                s1=data[0].split("= ")
                s2=data[1].split("= ")
                s3=data[2].split("= ")
                s4=data[3].split("= ")
                s5=data[4].split("= ")
                moisture = int(s3[1])
                ldr = int(s4[1])
                temp = float(s2[1])
                if ldr <= 200:
                    lightStatus = "on"
                else:
                    lightStatus = "off"
                    
                if moisture <500:
                    motorStatus = "off"
                elif moisture >=500 and moisture <750:
                    motorStatus = "off"
                else:
                    motorStatus ="on"
                    
                if temp >= 50:
                    fanStatus = "on"
                else:
                    fanStatus = "off"
                
                date = str(datetime.date(datetime.now()))
                time = str(datetime.time(datetime.now()))
                store=[date,time,s1[1],s2[1],s3[1],s4[1],s5[1],"on",motorStatus, lightStatus,fanStatus]
                w.writerow(store)
                f.close()
                print("Data Stored!")
                print(s1)
                print(s2)
                print(s3)
                print(s4)
                print(s5)
                print(lightStatus)
                
            count = count + 1
            
                
                
        

    
                
                
                
