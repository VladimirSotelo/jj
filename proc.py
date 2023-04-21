import datetime
import csv

def main():
    csv_file = open('datos.csv','r')
    _dato = csv.reader(csv_file)
    print(_dato)
    #for dato in _dato:
        #dato[1] = datetime.datetime.strptime(dato[1],'%Y-%m-%d %H:%M:%S')
        #if dato[1] > datetime.datetime(2023, 3, 7, 7, 58, 4):
        #    print(dato)
    
    csv_file.close()

if __name__ == '__main__':
    main()
