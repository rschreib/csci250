#Name: Robert Schreibman
#Date: Feb 22, 2018
#Class: csci250 - Sensors
#Description: This sample file is for Lab4 - and intended as a bare-bones structure to
#       work with the I2C and the accelerometer. Once the device is wired and RPi
#       running, this code should work as is. Students are tasked to modify this
#       code to an object-oriented solution for credit.
import smbus 
import time

# Get I2C bus - initial bus to channel 1
bus = smbus.SMBus(1) 

#Accelerometer class with default values (0,0,0)
class Accelerometer:
    calibrated = 2
    x_cal = [0,0,0]
    y_cal = [0,0,0]
    z_cal = [0,0,0]
    x_offset,y_offset,z_offset = 0,0,0
    def average(self):
        x_avg = sum(self.x_cal) / float(len(self.x_cal))
        y_avg = sum(self.y_cal) / float(len(self.y_cal))
        z_avg = sum(self.z_cal) / float(len(self.z_cal))
        return x_avg,y_avg,z_avg
    def calibrateNumbers(self):
        if (self.calibrated == 0):
            x_offset,y_offset,z_offset = average(self)
        else:
            self.x_cal[2-self.calibrated] = self.x
            self.y_cal[2-self.calibrated] = self.y
            self.z_cal[2-self.calibrated] = self.z
            self.calibrated -= 1
    def __init__(self, x=0, y=0, z=0):
        self.x=x - self.x_offset  #tries to zero out the recorded values while device is not tilted
        self.y=y - self.y_offset
        self.z=z - self.z_offset
        self.calibrateNumbers()
    def printData(self):
        print("Acceleration in x is",self.x)
        print("Acceleration in y is",self.y)
        print("Acceleration in z is",self.z)
    def printCoord(self):
        print("({},{},{})".format(self.x,self.y,self.z))
    def myPrint(self,arr):
        myString = "( "
        for i in range(len(arr)):
            myString += arr[i] + ' '
        myString += ")"
        return(myString)
    def __repr__(self):
        print(self.x_offset," ",self.y_offset," ",self.z_offset,"fuck")
        print(self.x_cal[0]," ",self.y_cal[1]," ",self.z_cal[2],"damn")
        return "({},{},{})".format(self.x,self.y,self.z)

    
try:
    arr = []
    while True:
        #Parameters for write_byte_data
        #1. Address of the device
        #2. Communication data - active mode control register
        #3. Our data - 0 (standby mode) or 1 (active)
        bus.write_byte_data(0x1D, 0x2A, 1) 
        time.sleep(0.5)

        #Read from the status register, real-time status register 0x00
        #Data returned will be an array
        #Contents of 7 bytes read and stored in data array represent:
        #status (ignore), MSBx, LSBx, MSBy, LSBy, MSBz, LSBz
        data = bus.read_i2c_block_data(0x1D, 0x00, 7) 

        #put register in standbye mode
        bus.write_byte_data(0x1D, 0x2A, 0)
        time.sleep(0.5)

        MSB_x = data[1]
        LSB_x = data[2]
        MSB_y = data[3]
        LSB_y = data[4]
        MSB_z = data[5]
        LSB_z = data[6]
        numberOfBits = 16
        xAccl = (MSB_x * 256 + LSB_x) / numberOfBits
        yAccl = (MSB_y * 256 + LSB_y) / numberOfBits
        zAccl = (MSB_z * 256 + LSB_z) / numberOfBits
        
        if xAccl > 2047:
            xAccl -= 4096
        if yAccl > 2047:
            yAccl -= 4096
        if zAccl > 2047:
            zAccl -= 4096
        #print("x: ",xAccl," y: ",yAccl," z: ",zAccl)
        #print(data)

        #created class Acceleromter that stores the x, y, z coordinates
        #inside the instance point. The instance is then appended to the
        #array arr. Member functions are then called to print the data
        point = Accelerometer(xAccl,yAccl,zAccl)
        point.calibrateNumbers()
        arr.append(point)
        point.printData()
        point.printCoord()
        #print(point.myPrint(['4','5','6','7','8','9']))
        print(point)

        
#capture the control c and exit cleanly
except(KeyboardInterrupt, SystemExit): 
    print("User requested exit... bye!")
    
#Sample modified from https://www.controleverything.com/content/Accelorometer?sku=MMA8452Q_I2CS#tabs-0-product_tabset-2
