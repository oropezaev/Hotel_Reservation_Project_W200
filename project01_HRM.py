# Hotel Reservation Project 1 - W200 Fall 2019 Ernesto V. Oropeza
import sys
import random
import datetime as dt
import time
import json

def pick(in_list = None):
    """Return a value from a list with user interaction"""
    if in_list == None or in_list == []:
        print('There is not item in your list!!!')
        return None
    else:
        cont = 0
        for k in in_list:
            print('Index: {} - Item: {}'.format(cont,k))
            cont += 1
        print('\n')
        while True:
            try:
                ans = input('Do you want to pick any item? (y or n)')
                if ans.lower() != 'y' and ans.lower() != 'n':
                    raise Exception('Please select y or n')
                break
            except Exception as err:
                print(err)
        if ans == 'n':
            print('There is not selection!!!')
            return None
        else:
            while True:
                try:
                    idx = int(input('Please enter index from 0 to '+ str(len(in_list)-1) +': '))
                    if idx not in range(len(in_list)):
                        raise Exception('Index range is 0 to {}'. format(len(in_list)-1))
                    break
                except ValueError:
                    print('Input only numbers please!!!')
                except Exception as err:
                    print(err)
            return in_list[idx]

def datein(checkin = None):
    "Return a input date in a string format mm/dd/yyyy to a datetime python type "
    if checkin == None:
        checkin = input("Enter Checkin date (mm/dd/yyyy Format): ")
    while True:
        try:
            if checkin.count('/') != 2:
                raise Exception ('Please use the following format mm/dd/yyyy')
            datein = checkin.split('/')
            if len(datein[2]) != 4:
                raise Exception ('Please use the following format mm/dd/yyyy')
            if len(datein[0]) != 2:
                raise Exception ('Please use the following format mm/dd/yyyy')
            if len(datein[1]) != 2:
                raise Exception ('Please use the following format mm/dd/yyyy')
            checkin = dt.date(int(datein[2]),int(datein[0]),int(datein[1]))
            break
        except ValueError as err:
            print(str(err),' The date you are trying to enter is ',checkin)
            checkin = input("Enter Checkin date (mm/dd/yyyy Format): ")
        except Exception as err:
            print(str(err),' The date you are trying to enter is ',checkin)
            checkin = input("Enter Checkin date (mm/dd/yyyy Format): ")
    return checkin

class reservation:
    """Handle the information of a reservation. The arguments are: reservation number, name, check-in
       date, number of nights to stay and date when the reservation was made. Reservation number and
        date of the reservation are automatically asigned if not specified"""
    def __init__(self,rno= None, name=None, checkin=None, nights=None, resdate = None):
        """Initializes the class reservation"""
        self.name = name
        if nights == None:
            self.nights = nights
        else:
            self.nights = int(nights)
        if checkin == None:
            self.checkin = None
        else:
            self.checkin = datein(checkin)
        if resdate == None:
            self.resdate = dt.date.today()
        else:
            self.resdate = datein(resdate)
        if rno == None:
            dayr = str(self.resdate).split('-')
            self.rno = dayr[1] + dayr[2] + str(random.randint(1000,9999))
        else:
            self.rno = rno

    def create(self):
        """User interactive reservation class creator. Only input are name, check-in date
           and number of nights of the stay. Reservation number is randomly assigned and
           reservation date is the date when it is created."""
        if self.name is None:
            self.name = input("Enter Name on the reservation: ")
        if self.checkin is None:
            while True:
               try:
                   self.checkin = datein()
                   if self.checkin < dt.date.today():
                       raise Exception('Error: Past date. Pick any date from today!!! ')
                   break
               except Exception as err:
                   print(err)
        if self.nights is None:
            self.nights = int(input("Enter number of nights on the stay: "))
        print('Reservation has been created as:\n',self)

    def update(self,name=None,nights=None,checkin=None):
        """User interactive class reservation update"""
        if name == None:
            print('Name on the reservation is: {}'.format(self.name))
            ans = input('Do you want to change it? (y or n): ')
            while len(ans) !=1 or ans.lower() not in 'yn':
                print('Please type (y) for yes and (n) for no')
                ans = input('Do you want to change it? (y or n): ')
                continue
            if ans.lower() == 'y':
                self.name = input("Enter new name on the reservation: ")
        else:
            self.name = name
        if nights == None:
            print('The reservation is for {} nights'.format(self.nights))
            ans = input('Do you want to change it? (y or n): ')
            while len(ans) !=1 or ans.lower() not in 'yn':
                print('Please type (y) for yes and (n) for no')
                ans = input('Do you want to change it? (y or n): ')
                continue
            if ans.lower() == 'y':
                self.nights = int(input("Enter new number of nights on the reservation: "))      #Check input
        else:
            self.nights =int(nights)
        if checkin == None:
            print('The reservation check-in is {}'.format(self.checkin))
            ans = input('Do you want to change it? (y or n): ')
            while len(ans) !=1 or ans.lower() not in 'yn':
                print('Please type (y) for yes and (n) for no')
                ans = input('Do you want to change it? (y or n): ')
                continue
            if ans.lower() == 'y':
                while True:
                    try:
                        self.checkin = datein()
                        if self.checkin < dt.date.today():
                            raise Exception ('Error: Past date. Pick any date from today!!! ')
                        break
                    except Exception as err:
                        print(err)
        else:
            while True:
                try:
                    self.checkin = datein(checkin)
                    if self.checkin < dt.date.today():
                        raise Exception ('Error: Past date. Pick any date from today!!! ')
                    break
                except Exception as err:
                    print(err)
        print('\nReservation has been updated as:\n',self)

    def __str__(self):
        return '\nReservation number: {}\nName on reservation: {}\nDate of the reservation: {} \
                  \nNumber of nights {}\nCheck-in date: {}\n'. format(self.rno, self.name, self.resdate, self.nights, self.checkin)

    def __repr__(self):
        return self.__str__()

class hotel:
    """Handles and shows the hotel data base"""
    def __init__(self):
        self.h_dict = {}

    def open_hotel(self,hotel_ex):
        self.h_dict = hotel_ex

    def read_hotel(self,filein = None):
        """Read a JSON file of the hotel information"""
        if filein == None:
            print("There is not file input. Creating a defult hotel (10 rooms and 2 floors)")
            self.auto_build()
            return None
        else:
            try:
                fid = open(filein,'r')
                file_dict = json.load(fid)
                fid.close()
                room_list = list(file_dict.keys())
                for room in room_list:
                    res_list = file_dict[room].get('reservations')
                    n = len(res_list)
                    for k in range(n):
                        r = res_list.pop(0)
                        res = reservation(r[0],r[1],r[2],r[3],r[4])
                        file_dict[room]['reservations'].append(res)
                self.open_hotel(file_dict)
            except FileNotFoundError as err:
                print('Error: input file not found. Creating a defult hotel (10 rooms and 2 floors)')
                self.auto_build()
            except UnicodeDecodeError as err:
                print('Error: input file not .json file. Creating a defult hotel (10 rooms and 2 floors)')
                self.auto_build()
            return None

    def write_hotel(self, fileout = None):
        """Write a JSON file of the hotel information"""
        if fileout == None:
            rn = dt.datetime.now()
            fnum = str(rn.month) + str(rn.day) + str(rn.year) + str(rn.hour) + str(rn.minute)  + str(rn.second)
            fileout = 'hotel_defult_'+fnum+'.json'
            print("No potput file specified. Writing a defult .json file as:\n"+fileout)
        room_list = list(self.h_dict.keys()) #Reservations class to list
        for room in room_list:
            res_list = self.h_dict[room].get('reservations')
            n = len(res_list)
            for k in range(n):
                r = res_list.pop(0)
                d = str(r.checkin)
                dl =d.split('-')
                checkin =dl[1]+'/'+dl[2]+'/'+dl[0]
                d = str(r.resdate)
                dl =d.split('-')
                resdate = dl[1]+'/'+dl[2]+'/'+dl[0]
                ltup = (r.rno,r.name,checkin,str(r.nights),resdate)
                lr =list(ltup)
                res_list.append(lr)
            self.h_dict[room]['reservations'] = res_list
        fid = open(fileout,"w")
        out_json = json.dumps(self.h_dict)
        fid.write(out_json)
        fid.close()

    def auto_build(self,nroom = 10, floors = 2):
        d=10**len(str(nroom))
        for k in range(floors):
            for j in range(nroom):
                self.h_dict[str((k+1)*d+j+1)]={'amenity': [],'reservations': [], 'floor': k+1}

    def amenity_in(self,am_dict = {}):
        if am_dict == {}:
            print('There is no amenity to add to your hotel!!!')
        else:
            am_tuple = list(am_dict.items())
            for k in am_tuple:
                for j in k[1]:
                    self.h_dict[j]['amenity'].append(k[0])

    def insert_reservation(self,res):
        """Assigns a reservation to a room"""
        room_list = search.room_date(self, res.checkin, res.nights)
        if room_list == []:
            print('There are not rooms available for the dates\n')
            return
        else:
            idx = random.randint(0,len(room_list)-1)
            self.insert_res([(room_list[idx],res)])
        print('Rreservation Succesfully assigned to room {}'.format(room_list[idx]))

    def insert_res(self,res_asind = []): #res_assed is a list with tuples (room and reservation assigned)
        """Insert a list of reservations in the specified room
        Return same input list that is empty if all reservations succesfully inserted or
        with the reservations that had date conflict to be inserted in the respective room"""
        res_out= res_asind.copy()
        for k in res_asind:
            res_list = self.h_dict[k[0]].get('reservations')
            checkin = k[1].checkin
            checkout = k[1].checkin + dt.timedelta(days=k[1].nights)
            available = True
            for res in res_list:
                if checkin >= res.checkin and checkin < res.checkin + dt.timedelta(days=res.nights):
                    available = False
                    break
                elif checkout > res.checkin and checkout <= res.checkin + dt.timedelta(days=res.nights):
                    available = False
                    break
            if available:
                self.h_dict[k[0]]['reservations'].append(k[1])
                res_out.pop(0)
                print('Reservation number {} succesfully assigned to room {}.'.format(k[1].rno,k[0]))
            else:
                print('Room {} is not available for {}'.format(k[1].checkin))
        return res_out

    def cancel_res(self,res_asind = []):           #res_list is a list of reservation to cancel fro
        """Removed a reservation from the hotel where the assigned room is known"""
        for k in res_asind:
            try:
                idx = self.h_dict[k[0]]['reservations'].index(k[1])
                res = self.h_dict[k[0]]['reservations'].pop(idx)
                print('Reservation number '+str(res.rno)+' succesfully canceled')
            except ValueError as err:
                      err = 'Reservation number '+str(res4.rno)+' not found in room '+k[0]
                      print(err)

    def __str__(self):
        room_list = list(self.h_dict.keys())
        output='{r:<10}{a:<20}{rn:<20}{ch:<20}\n'.format(r='Room',a='Amenities',rn='Reservation Number',ch='Check-in Date')
        while room_list != []:
            room = room_list.pop(0)
            ameni_list = self.h_dict[room].get('amenity')
            res_list = self.h_dict[room].get('reservations')
            na = len(ameni_list)
            nr = len(res_list)
            if nr >= na:
                nn = nr
            else:
                nn = na
            if nn == 0:
                output += '{r:<10}{a:<20}{rn:<20}{ch:<20}\n'.format(r=room,a='',rn='',ch='')
            for k in range(nn):
                if k > 0:
                    nroom = ''
                else:
                    nroom = room
                if k > nr-1:
                    nres = ''
                else:
                    nres1 = res_list[k].rno
                    td = str(res_list[k].checkin)
                    tdl = td.split('-')
                    td = tdl[1]+'/'+tdl[2]+'/'+tdl[0]
                    nres2 = td
                if k > na-1:
                    ameni = ''
                else:
                    ameni = ameni_list[k]
                output += '{r:<10}{a:<20}{rn:<20}{ch:<20}\n'.format(r=nroom,a=ameni,rn=nres1,ch=nres2)
            output += '-'*70+'\n'
        return output

    def __repr__(self):
        return self.__str__()

class search(hotel):
    """This class have only methods to handle different seach in the hotel"""
    def look_reservation(self,argin = None,arg_type = 1):
        """Return a list of reservations that match criterion argin is a
           string and argtype integer: (0) number, (1) name, (2) check-in
           date or (3) reservation date. Defult is (1) name. For searching
           by name and reservation number partial text is valid"""
        while True:
            try:
                arg_type = int(input('Search criterion. Type options: (0) by number, (1) by name,'+
                                    ' (2) by check in date and (3) by reservation date: '))
                if arg_type not in range(4):
                    raise Exception('Invalid option. Please enter 0 to 3')
                if arg_type == 0:
                    argin = input('Please enter search number (partial or complete): ')
                elif arg_type == 1:
                    argin = input('Please enter search name (partial or complete): ')
                elif arg_type == 2:
                    argin = input('Please enter search date (mm/dd/2019) format: ')
                    argin = datein(argin)
                    arl = str(argin).split('-')
                    argin = arl[1] + '/' + arl[2]+ '/' + arl[0]
                elif arg_type == 3:
                    argin = input('Please enter search date (mm/dd/2019) format: ')
                    argin = datein(argin)
                    arl = str(argin).split('-')
                    argin = arl[1] + '/' + arl[2]+ '/' + arl[0]
                break
            except ValueError:
                print('Invalid option. Only numbers 0 to 3 acepted')
            except Exception as err:
                print(err)
        res_out=[]
        rooms = list(self.h_dict.keys())
        for room in rooms:
            res_list = self.h_dict[room].get('reservations')
            for res in res_list:
                if arg_type == 0:
                    if argin in res.rno:
                        res_out.append(res)
                elif arg_type == 1:
                    if argin.lower() in res.name.lower():
                        res_out.append(res)
                elif arg_type == 2:
                    argdate = datein(argin)
                    if argdate == res.checkin:
                        res_out.append(res)
                elif arg_type == 3:
                    argdate = datein(argin)
                    if argdate == res.resdate:
                        res_out.append(res)
        if res_out == []:
            print('\nNo reservation matches your criterion: \"{}\"'.format(argin))
            return None
        else:
            print('\n{} reservation(s) founded sucessfully'.format(len(res_out)))
            cont = 0
            for k in res_out:
                print('{} index - Reservation: {}'.format(cont,k))
                cont += 1
            while True:
                try:
                    idx = int(input('Enter index of the reservation that ervation ({} to {})'.format(0,len(res_out)-1)))
                    if idx not in range(len(res_out)):
                        raise Exception('Please select between 0 and {}'.format(len(res_out)))
                    print('You have selected: {}'.format(res_out[idx]))
                    break
                except ValueError:
                    print('No option selected...')
                    return None
                except Exception as err:
                    print(err)

            print('You have selected:\n {}'.format(res_out[idx]))
            return res_out[idx]

    def room_reserved(self,reservin = None):
        """Returns the room number under the input reservation"""
        if reservin == None:
            print('An input reservation is needed it!!!')
        elif str(type(reservin)) != "<class '__main__.reservation'>":
            print('The input has to be a reservation class')
        else:
            rooms = list(self.h_dict.keys())
            for room in rooms:
                res_list = self.h_dict[room].get('reservations')
                for res in res_list:
                    if res.rno == reservin.rno:
                        print('Reservation number {} is assigned to room number {}'.format(reservin.rno,room))
                        return room
        print('No reservation found')
        return None

    def all_rooms(self):
        """Returns a list with all the room numbers in the hotel"""
        rooms_list = list(self.h_dict.keys())
        print('\nThe hotel rooms are:')
        cont = 0
        while rooms_list != []:
            print(rooms_list.pop(0),end =' ')
            cont +=1
            if cont == 10:
                print('\n')
                cont = 0

    def all_amenities(self):
        """Returns a list with all the amenities for all rooms in the hotel"""
        am_list = []
        rooms = list(self.h_dict.keys())
        for room in rooms:
            am_list += self.h_dict[room].get('amenity')
        temp = set(am_list)
        am_list = list(temp)
        print('\nAmenities available are:')
        while am_list != []:
             print(am_list.pop())

    def all_reservations(self):
        """Returns a list with all the reservations in the hotel"""
        res_list = []
        rooms = list(self.h_dict.keys())
        for room in rooms:
            res_list += self.h_dict[room].get('reservations')
        w1 = 'Reservation No'
        w2 = 'Name'
        w3 = 'Date of Reservation'
        w4 = 'Checkin date'
        w5 = 'Nights'
        print('{c1:<25}{c2:<25}{c3:<25}{c4:<25}{c5:<25}'.\
              format(c1 = w1, c2 = w2, c3 = w3, c4 = w4, c5 = w5))
        while res_list != []:
            r = res_list.pop(0)
            rdl = str(r.resdate).split('-')
            rd = rdl[1] + '/' + rdl[2]+ '/' + rdl[0]
            rdl = str(r.checkin).split('-')
            rd2 = rdl[1] + '/' + rdl[2]+ '/' + rdl[0]
            print('{c1:<25}{c2:<25}{c3:<25}{c4:<25}{c5:<25}'.\
                  format(c1 = r.rno, c2 = r.name, c3 = rd,\
                  c5 = str(r.nights), c4 = rd2))
        return None

    def rooms_amenity(self,am_list = []):
        """Returns a list with all rooms that match the desired list of amenities"""
        if am_list == []:
            ameny = input('Please enter desired amenities separated by slash (amenity1/amenity2/...: \n')
            am_list = ameny.split('/')
        rooms = list(self.h_dict.keys())
        room_list = []
        for avar in rooms:
            if all(elem in self.h_dict[avar].get('amenity') for elem in am_list):
                room_list.append(avar)
        if room_list == []:
            print('There is not a room with all your desired amanities')
        else:
            print('\nThe rooms that have your amenities are:')
            while room_list != []:
                 print(room_list.pop())

    def room_date(self,checkin = None, nights = None):
        """Return a list with the available rooms for a check-in date and the number of nights"""
        if checkin is None:
            checkin = datein()
        if nights is None:
            nights = int(input("Enter number of nights on the stay: "))
        checkout = checkin + dt.timedelta(days=nights)
        room_list = []
        rooms = list(self.h_dict.keys())
        for room in rooms:
            res_list = self.h_dict[room].get('reservations')
            available = True
            for res in res_list:
                if checkin >= res.checkin and checkin < res.checkin + dt.timedelta(days=res.nights):
                    available = False
                    break
                elif checkout > res.checkin and checkout <= res.checkin + dt.timedelta(days=res.nights):
                    available = False
                    break
                else:
                    continue
            if available:
                room_list.append(room)
        return room_list

    def past_res(self):
        rooms = list(self.h_dict.keys())
        for room in rooms:
            res_list = self.h_dict[room].get('reservations')
            for res in res_list:
                if res.checkin + dt.timedelta(days=res.nights) < dt.date.today():
                    idx = res_list.index(res)
                    self.h_dict[room]['reservations'].pop(idx)

    def cancel_res(self,reservin = None):
        """Removed a reservation from the hotel where the assigned room is unknown"""
        print(type(reservin),type(reservation()))
        if reservin == None:
            print('An input reservation is needed it!!!')
        elif type(reservin) != type(reservation()):
            print('The input has to be a reservation class')
        else:
            rooms = list(self.h_dict.keys())
            for room in rooms:
                res_list = self.h_dict[room].get('reservations')
                for res in res_list:
                    if res.rno == reservin.rno:
                        idx = res_list.index(res)
                        self.h_dict[room]['reservations'].pop(idx)
                        print('Reservation number '+str(res.rno)+' succesfully canceled')
                        return None
            print('Reservation number '+str(res.rno)+' not found')

    def occupancy(self, date1 = None, date2 = None, room_avail = None):
        """Return a list of tuple with the date and a list with available rooms the corresponding date.
           If no argument pass it will return the porcentage of occupancy on the present date"""
        while True:
            try:
                print('Please enter date range. If just for today press ENTER')
                date1 = input('Initial date in mm/dd/yyyy format:')
                if date1 == '':
                    break
                date1 = datein(date1)
                date2 = input('Final date date in mm/dd/yyyy format:')
                date2 = datein(date2)
                if date2 < date1:
                    raise Exception('Final date is before initial. Please check')
                break
            except Exception as err:
                print(err)
        if date1 == '':
            date1 = dt.date.today()
        if date2 == None:
            date2 = date1
        sw = input('Do you want the number of rooms available per date (instead the rooms). '+
                   'If yes press y')
        if sw.lower() == 'y':
            room_avail = 0
        rooms = list(self.h_dict.keys())
        date_dict = {date1:[]}
        cont=1
        while date1 + dt.timedelta(cont) <= date2:
            date_dict[date1 + dt.timedelta(cont)] = []
            cont += 1
        for room in rooms:
            res_list = self.h_dict[room].get('reservations')
            for res in res_list:
                for k in range(res.nights):
                    if res.checkin + dt.timedelta(k) in list(date_dict):
                        date_dict[res.checkin + dt.timedelta(k)].append(room)
        srooms = set(rooms)
        for date_e in list(date_dict):
            roc = date_dict.get(date_e)
            sroc = set(roc)
            if room_avail == None:
                date_dict[date_e] = list(srooms.difference(sroc))
            else:
                date_dict[date_e] = len(srooms.difference(sroc))
        if room_avail != None:
            print('{dd:<15}{rr:<15}'.format(dd = 'Date', rr = 'Available Rooms'))
            for k,j in date_dict.items():
                print('{dd:<15}{rr:<15}'.format(dd = str(k) , rr = j))
        else:
            print('{dd:<15}{rr:<100}'.format(dd = 'Date', rr = 'Available Rooms'))
            for k,j in date_dict.items():
                room_list = ','.join(j)
                print('{dd:<15}{rr:<100}'.format(dd = str(k) , rr = room_list))
        return date_dict.items()

class hotel_management(object):
    def run(self):
        print('\n','*'*20,' Hotel Reservation Management ','*'*20,'\n\n')
        print('Initiating...Loading the hotel information\n')
        try:
            hfile = sys.argv[1]
        except IndexError:
            hfile = None
        h = hotel()  #This function is to read the current hotel info
        h.read_hotel(hfile)
        print('Hotel information loaded!!!\n')

        search.past_res(h) #Cleaning past reservations

        while True: #Starting User interaction
            print('\nHotel Management Options:\n' + '1 : Hotel Information\n' +
                  '2 : Reservations\n' + '3 : Exit\n')
            while True:
                try:
                    opt = int(input('Please enter your option: '))
                    if opt not in range(1,4):
                        raise Exception ('Invalid option. Please type (1, 2 or 3)')
                    break
                except ValueError:
                    print('Invalid Option. Please type (1, 2 or 3)')
                except Exception as err:
                    print(err)
            if opt == 3: #Saving dictionary and exit
                print('Writing current hotel status..!\n')
                h.write_hotel(hfile)
                print('Exiting Hotel Management..!\n\n')
                return
            if opt == 1: #Hotel Information
                print('Hotel Information Options:\n' +
                     '1 : Hotel Overview (Rooms, Amenities and Reservations)\n' +
                     '2 : View Amenities and Rooms\n' + '3 : Rooms by Amenities\n' +
                     '4 : View Hotel ocupancy by date range\n' +
                     '5 : Current hotel reservations')
                while True:
                    try:
                        opt = int(input('Please enter your option: '))
                        if opt not in range(1,6):
                            raise Exception ('Invalid option. Please type (1, 2, 3, 4 or 5)')
                        break
                    except ValueError:
                        print('Invalid Option. Please type (1, 2, 3, 4 or 5)')
                    except Exception as err:
                        print(err)
                if opt == 1:
                    print(h)
                elif opt == 2:
                    search.all_rooms(h)
                    search.all_amenities(h)
                elif opt ==3:
                    search.all_amenities(h)
                    search.rooms_amenity(h)
                elif opt == 4:
                    search.occupancy(h)
                elif opt == 5:
                    search.all_reservations(h)
                #End of option 1
            elif opt == 2: #Hotel Reservation
                print('Hotel Reservations option:\n' + '1 : Creat new reservation\n' +
                     '2 : Update reservation\n' + '3 : Search reservation\n' +
                     '4 : Cancel reservation\n' + '5 : Change room on the reservation\n')
                while True:
                    try:
                        opt = int(input('Please enter your option: '))
                        if opt not in range(1,6):
                            raise Exception ('Invalid option. Please type (1, 2, 3, 4 or 5)')
                        break
                    except ValueError:
                        print('Invalid Option. Please type (1, 2, 3, 4 or 5)')
                    except Exception as err:
                        print(err)
                if opt == 1:
                    print('Creating a new reservation')
                    res = reservation()
                    res.create()
                    h.insert_reservation(res)
                elif opt ==2:
                    print('Updating existing reservation')
                    res = search.look_reservation(h)
                    res.update()
                elif opt == 3:
                    print('Serching for reservations')
                    res = search.look_reservation(h)
                elif opt == 4:
                    print('Canceling reservation')
                    res = search.look_reservation(h)
                    room = search.room_reserved(h,res)
                    if res == None or room == None:
                        print('No room or reservation to cancel!!!')
                    else:
                        h.cancel_res([(room,res)])
                elif opt == 5:
                    print('Changing room number')
                    res = search.look_reservation(h)
                    room = search.room_reserved(h, res)
                    room_list = search.room_date(h, res.checkin, res.nights)
                    print('The available rooms are:\n')
                    nroom = pick(room_list)
                    if nroom != None:
                        h.cancel_res([(room,res)])
                        h.insert_res([(nroom,res)])
                    #Show the rooms available
                    else:
                        print('Aborting Cancelation...!!!')
                #End of option 2
        return # Main program run()

if __name__ == '__main__': #Run main interface with user
    output = hotel_management().run()
