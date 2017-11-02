import fileinput
import sys, os

def change(ip, mac, name, comments, path):

    done = False
    data = ip + " " + mac + " " + name + " " + comments
    for line in fileinput.input(os.getcwd() + "/" + path, inplace=True):
        if ip in line:
            print data
            done = True

        else:
            if mac in line:
                print data
                done = True

            else:
                print line.replace('\n', '')

    if done is False:
        file = open(os.getcwd() + "/" + path, "a")
        file.writelines(data + '\n')
        file.close()

if __name__ == "__main__":

    ip = sys.argv[1]
    mac = sys.argv[2]
    name = sys.argv[3]
    comments = sys.argv[4]
    path = sys.argv[5]

    # file = open('b.txt', 'w')
    # file.writelines(ip + " " + mac + " " + name + " " + comments)
    # file.close()
    
    change(ip, mac, name, comments, path)



