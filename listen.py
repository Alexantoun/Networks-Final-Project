import datetime, socket   #low level networking interface for python
                #supports bluetooth protocols tojo
import csv

def parse_input(s1: str, s2: str, s3: str) -> list:
    l = list()
    x = datetime.datetime.now()
    l.append(x.strftime('%X'))
    #ButtonStatus
    if(s1[0] == 'b'):
        l.append(s1[1:])
    elif(s2[0] == 'b'):
        l.append(s2[1:])
    elif(s3[0] == 'b'):
        l.append(s3[1:])
    #Temperature
    if(s1[0] == 'c'):   
        l.append(s1[1:])
    elif(s2[0] == 'c'):
        l.append(s2[1:])
    elif(s3[0] == 'c'):
        l.append(s3[1:])
    #Humidity 
    if(s1[0] == 'h'):
        l.append(s1[1:])
    elif(s2[0] == 'h'):
        l.append(s2[1:])
    elif(s3[0] == 'h'):
        l.append(s3[1:])
    if (len(l)==4):
        return l
    else:
        print("Error in parse_input")
        print(l)
        return []


# def write_to_csv(l :list, writer):
#     print(f'current list: {l}')
#     if(len(l)!=3):
#         return
#     if(l[0]=='False' or l[0]=='True'):
#         if(l[-1]=='False' or l[-1]=='True'):
#             return

#         writer.writerow(l)
#         print(l)
#         l.clear()
        
#         return

#     elif(l[-1]=='False' or l[-1]=='True'):
#         new_l = []
#         for x in l:
#             if(x=='False' or x=='True'):
#                 new_l = [x] + new_l
#             else:
#                 new_l = new_l + [x]

#         writer.writerow(l)
#         print(l)
#         l = []
        
#         return
        


def main():
    host = "192.168.1.6" #input("Enter my IP: ")
    port = 2345
    recieved = ""
    arduinoList = list()
    t = 0
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #like s = socket.socket... except automatically handles closing
        s.bind((host,port)) #Binding to this host and port
        while True:
            if t > 10:
                break
            s.listen()  #returns a positive integer for success, negative for an issue
            print("Waiting for connection...")
            conn, addr = s.accept() #waiting loop, waiting to accept a new connection
            print(f"Recieved connection om {addr}")
            x=0
            while True:
                if t > 30:
                    break
                data = conn.recv(1024)
                recieved = data.decode()
                #print(f"{recieved}\n")  #if this fails then change recieved to data.decode
                if recieved=="close\r\n":
                    break   #Go back to wait-for-connection state
                arduinoList.append(recieved)
                t += 1
                x += 1
                if x==3:
                    arduinoList = parse_input(*arduinoList)
                    x = 0
                    if(len(arduinoList) == 4):
                        writer.writerow(arduinoList)
                    print(arduinoList)
                    arduinoList.clear() 

print("Listener Running")
header = ['TimeStamp', 'Button', 'Temp-C', 'Humidity-%']
# file = open('Arduino Data.csv', 'w'a
with open('arduinoData.csv', 'a') as f:    
    writer = csv.writer(f)
    writer.writerow(header)
    main()    
    f.close()
print("Done listening")

    