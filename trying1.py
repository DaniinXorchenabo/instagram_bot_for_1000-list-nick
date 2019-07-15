import sys
import main_window_design 
import input_insta_window_design
import change_victim_design
import change_victim_design_1
import users_activites_expectation_design
import users_activites_checking_design
import users_activites_checking_design_no
import login_design_no
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QPushButton, QGroupBox, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QObject
from time import sleep
import threading
from instapy import InstaPy
from instapy import smart_run



class Communicate(QObject):

    closeApp = pyqtSignal()
    
    
class instogrammAPI(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.users_dict = dict()
        self.users_dict_comments = dict()
        # login credentials

        insta_username = 'daniakhorze'
        insta_password = 'Ll154105'
        self.ranning = True
        self.comments = ['Nice shot! @{}',
                'I love your profile! @{}',
                'Your feed is an inspiration :thumbsup:',
                'Just incredible :open_mouth:',
                'What camera did you use @{}?',
                'Love your posts @{}',
                'Looks awesome @{}',
                'Getting inspired by you @{}',
                ':raised_hands: Yes!',
                'I can feel your passion @{} :muscle:']
        
        # get an InstaPy session!
        # set headless_browser=True to run InstaPy in the background
        self.session = InstaPy(username=insta_username,
                          password=insta_password,
                          headless_browser=False) 
        self.go_functhion = self.pass_pass
        self.change_fun = False
        self.mass_for_fun = ["", ""]
        self.output_class = None
        
    def run(self):
        with smart_run(self.session):
            while self.ranning:
                
                #print("&&", end=" ")
                if self.change_fun:
                    print("!!!run", self.mass_for_fun)
                    print("поток ", self.output_class.__class__.__name__)
                    data = self.go_functhion(*self.mass_for_fun[:-1:], trying=self.mass_for_fun[-1])
                    
                    self.change_fun = False
                    self.output_class.output_data = data
                    self.output_class.is_end = True
                    self.reverse_connect()
                    #self.mass_for_fun = ["", ""]
                    self.go_functhion = self.pass_pass
                sleep(0.2)
            print("=====")
        print("@@@@@@")
                    
    def reverse_connect(self):
        print("reverse_connect")
        if self.output_class:
            self.output_class.my_signal.closeApp.emit()
            
            
    def pass_pass(self,*a, **b):
        pass
    
    def check_like(self, username, herf_post_part, trying=False): # тут используетя в качестве  username'а имя пользователя, который хочет зарабатывать деньги
        herf = "https://www.instagram.com/p/" + herf_post_part + "/"
        print(1)
        if trying:
            like_count = self.session.my_get_count_likers(herf) # BteOBM0h6NJ
            like_count =  50 if (len(like_count) != 0) and int(like_count[0].split()[0]) > 50 else int(like_count[0].split()[0])    
            second_set = set(self.session.my_get_listLikerUser(herf, 100))
            print(list(second_set - set(self.users_dict[username][herf_post_part])))
            print(2)
            return (True if username in list(second_set - set(self.users_dict[username][herf_post_part])) else False)
        else:
            print(3)
            like_count = self.session.my_get_count_likers(herf) # BteOBM0h6NJ
            like_count =  50 if (len(like_count) != 0) and int(like_count[0].split()[0]) > 50 else int(like_count[0].split()[0])
            self.users_dict[username] = {herf_post_part : self.session.my_get_listLikerUser(herf, 100)}       #[herf_post_part] = users_dict[username].get(herf_post_part,  session.my_get_listLikerUser(herf, like_count))  
            print(4)
            
    def check_comments(self, username, herf_post_part, trying=False):# тут используетя в качестве  username'а имя пользователя, который хочет зарабатывать деньги
        herf = "https://www.instagram.com/p/" + herf_post_part + "/"
        if trying:
            comments_list = self.session.my_get_usernames_from_comments(herf, daysold=1)
            print(comments_list)
            return username in comments_list
        else:
            self.users_dict_comments[username] = {herf_post_part : self.session.my_get_usernames_from_comments(herf, daysold=1)} 
            
    def go_check_comments(self, username, herf_post_part, output_class,trying=False):
        self.mass_for_fun = [username, herf_post_part, trying]
        self.output_class = output_class
        self.go_functhion  = self.check_comments
        print('^^^^^^^')
        self.change_fun = True
        print("self.change_fun", self.change_fun)
        
        #output_class.is_end = True
        
    def go_check_like(self, username, herf_post_part, output_class, trying=False):
        self.mass_for_fun = [username, herf_post_part, trying]
        self.output_class = output_class
        self.go_functhion  = self.check_like
        print('^^^^^^^')
        self.change_fun = True
        print("self.change_fun", self.change_fun)
        #output_class.is_end = True

class mainWindow(QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.my_signal = Communicate()
        self.my_signal.closeApp.connect(self.fun1_part2)   
        
        self.hellow_text.setPixmap(QPixmap('pic/1/текст.png'))  # 'qr-code.jpg'
        
        self.get_coin.setIcon(QIcon('pic/1/заработать button.png'))
        self.get_coin.setIconSize(QSize(900, 100))
        self.get_coin.clicked.connect(self.get_coin_button_controller)
        
        self.PR_button.setIcon(QIcon('pic/1/заказать продвижение button.png'))
        self.PR_button.setIconSize(QSize(900, 100) )       
        self.PR_button.clicked.connect(self.PR_button_controller)
        self.output_data = ""
        self.is_end = False
    def get_coin_button_controller(self):
        print("идём платить деньги")
        self.hide()
        input_insta_window.show()
        #self.groupBox.visible(False)
        #sleep(5)
        #self.show()
        #self.groupBox.grid()
    def PR_button_controller(self):
        print("идём покупать пиар")
    
    def fun1_part2(self): 
        pass
    
    
class inputInstaWindow(QMainWindow, input_insta_window_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.my_signal = Communicate()
        self.my_signal.closeApp.connect(self.fun1_part2)        
        
        self.input_insta_text.setPixmap(QPixmap('pic/2/Введи свой логин в instagram.png'))  # 'qr-code.jpg'
        #self.input_insta_text.setPixmap(QPixmap('pic/2/проверить button.png'))
        self.input_instagramm.textEdited['QString'].connect(self.input_insta_controller)
        self.input_text = ""
        self.check_login_insta_button.setIcon(QIcon('pic/2/проверить button.png'))
        self.check_login_insta_button.setIconSize(QSize(400, 100))
        self.check_login_insta_button.clicked.connect(self.change_login_insta_button_controller)    
        f = open("des/try0.css", 'r')
        self.f1 = f.read()
        f.close()
        self.error_akk.setStyleSheet(self.f1 + 'color: rgba(255,0,0,0);}')
        self.output_data = ""
        self.is_end = False
        
    def change_login_insta_button_controller(self):
        print("----")
        #y = 
        #sleep(1)
        go_loding.show()
        logic = inst_obj.session.check_acc_instagram(str(self.input_text))
        if logic:  # inst_obj.check_acc_instagram(str(self.input_text)):
            
            print("----yes")
            self.error_akk.setStyleSheet(self.f1 + 'color: rgba(255,0,0,0);}')
            username_session[0] = str(self.input_text)
            print("username_session[0]", username_session[0])
            self.hide()
            change_victim_windiw.show()
        else:
            print("----no")
            self.error_akk.setStyleSheet(self.f1 + 'color: rgba(255,0,0,255);}')
        print("change_login_insta_button_controller")
        go_loding.hide()
        
    def show_this_windows(self):
        self.show()
        #self.change_victim_windiw()
    def input_insta_controller(self, string):
        self.input_text = string
        print("--" + string)
    def fun1_part2(self): 
        pass

class changeVictimWindiw(QMainWindow, change_victim_design_1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.my_signal = Communicate()
        self.my_signal.closeApp.connect(self.fun1_part2)        
        
        f = open("des/try1.css", 'r')
        f1 = f.read()
        print(str(f1))
        
        self.found_like.setObjectName("find_all")
        self.rectangle_4.setObjectName("rectangle")
        self.find_all_3.setObjectName("change_text")
        self.label.setObjectName("find_all")
        #self.task1.setObjectName("tasks")
        self.button_task1.clicked.connect(self.fun1)
        self.button_task2.clicked.connect(self.fun2)
        self.button_task3.clicked.connect(self.fun3)
        
        self.task2.setObjectName("tasks")
        self.task3.setObjectName("tasks")
        self.inst_login.setText(who_is_PR[0])
        self.inst_login2.setText(who_is_PR[1])
        self.inst_login2.setObjectName("inst_login")
        self.inst_login3.setObjectName("inst_login")
        self.heart2.setObjectName("heart")
        self.heart3.setObjectName("heart")
        self.prise2.setObjectName("prise")
        self.prise3.setObjectName("prise")
        self.ended_session_2.setObjectName("ended_session")
        self.ended_session_text_2.setObjectName("ended_session_text")
        self.centralwidget.setStyleSheet(f1)
        self.widget.setStyleSheet(f1)
        self.change_text.setStyleSheet(f1)
        self.change_text.setStyleSheet(f1)
        self.find_all.setStyleSheet(f1)
        self.rectangle.setStyleSheet(f1)
        self.big_rect.setStyleSheet(f1)
        self.tasks.setStyleSheet(f1)
        self.insta_img1.setStyleSheet(f1)
        self.insta_img2.setStyleSheet(f1)
        self.insta_img3.setStyleSheet(f1)
        self.inst_login.setStyleSheet(f1)
        self.heart.setStyleSheet(f1)
        self.prise.setStyleSheet(f1)
        self.tasks.clicked.connect(self.fun1)
        self.task2.clicked.connect(self.fun2)
        self.task3.clicked.connect(self.fun3)  
        self.ended_session.setStyleSheet(f1)
        self.ended_session_text.setStyleSheet(f1)
        self.output_data = ""
        self.is_end = False
        self.button_session.clicked.connect(self.return_for_start)
        self.give_coins_button.clicked.connect(self.give_coins)
        
    def return_for_start(self):
        self.hide()
        main_window.show()
        
    def give_coins(self):
        print("coin given", coin[0])
        coin[0] = 0
        
        
    def fun1_part2(self):  
        print('909090===')
        self.is_end = False
        print("1")
        goin.show()
        go_loding.hide()
        
        
        
    def fun1(self):
        try:
            #go_loding.set_connect_between(goin)
            go_loding.show()
            self.setEnabled(False)
            goin.who_is_post("Like")
            #print("username_session[0]--", username_session[0])
            inst_obj.go_check_like(username_session[0], who_is_PR_herf[0], self)

        except Exception as e:
            print("-------", e)
        
    def fun2(self):
        try:
           
            print("username_session[0]-", who_is_PR_herf[0])
            self.setEnabled(False)        
            #self.setVisible(False)
            goin.who_is_post("Comm")
            goin.show()
            print("2")
        except Exception as e:
            print("-------", e)
            
    def fun3(self):
        
        self.setEnabled(False)
        goin.show()
        print("3")        
        
class usersActivitesExpectation(QMainWindow, users_activites_expectation_design.Ui_MainWindow): # пассивное окно 
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.my_signal = Communicate()
        self.my_signal.closeApp.connect(self.fun1_part2)        
        
        self.gone_session_button.clicked.connect(self.fun1)
        f = open("des/try2.css", 'r')
        f1 = f.read()
        print(str(f1))        
        self.done_session.setStyleSheet(f1)#.setPixmap(QPixmap('pic/1/проверить button.png'))
        f.close()
        self.parametr = "none"
        self.output_data = ""
        self.is_end = False
        
    def fun1(self):
        #go_loding.set_connect_between()
        go_loding.show()
        self.hide()
        go_loding.who_is_post(self.parametr, is_choice=True)

        
    def who_is_post(self, param):
        self.parametr = param

    def fun1_part2(self): 
        print("gnov")
        go_loding.hide()


class ckeckAktivity(QMainWindow, users_activites_checking_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        
        self.my_signal = Communicate()
        self.my_signal.closeApp.connect(self.fun1_part2)        
        
        self.gone_session_button.clicked.connect(self.fun1)
        f = open("des/try3.css", 'r')
        f1 = f.read()
        print(str(f1))        
        self.done_session.setStyleSheet(f1)#.setPixmap(QPixmap('pic/1/проверить button.png'))
        f.close()
        self.ok_img.setStyleSheet(f1)
        self.you_finish_ckecking_text.setStyleSheet(f1)
        self.parametr = ""
        self.output_data = ""
        self.is_end = False
        
    def fun1(self):
        self.hide()
        change_victim_windiw.setEnabled(True)      
        print("gnov")
        
    def fun1_part2(self): 
        pass    


class ckeckAktivityNo(QMainWindow, users_activites_checking_design_no.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)   
        
        self.my_signal = Communicate()
        self.my_signal.closeApp.connect(self.fun1_part2)        
        
        self.gone_session_button.clicked.connect(self.fun1)
        f = open("des/try3.css", 'r')
        f1 = f.read()
        print(str(f1))        
        self.done_session.setStyleSheet(f1)#.setPixmap(QPixmap('pic/1/проверить button.png'))
        f.close()
        self.noImg.setStyleSheet(f1)
        self.you_finish_ckecking_text.setStyleSheet(f1)
        self.parametr = ""
        self.output_data = ""
        self.is_end = False
        
    def fun1(self):
        self.hide()
        change_victim_windiw.setEnabled(True)      
        print("gnov")
        
    def fun1_part2(self): 
        pass        
   
                
                
class goLoding(QMainWindow, login_design_no.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.my_signal = Communicate()
        self.my_signal.closeApp.connect(self.fun1_part2)        
        
        f = open("des/try3.css", 'r')
        f1 = f.read()  
        f.close()
        self.login_img.setStyleSheet(f1)#.setPixmap(QPixmap('pic/1/проверить button.png'))
        self.next_obj = None
        self.output_data = False
        self.is_end = False
        self.is_choice = False
        self.prise = 0
        
    def who_is_post(self, param, is_choice=False):
        self.is_choice = is_choice
        self.parametr = param 
        logic = None
        if param == "Like":
            inst_obj.go_check_like(username_session[0], who_is_PR_herf[0],self,  trying=True)
            self.prise = 0.5
        elif param == "Comm":
            try:
                inst_obj.go_check_comments(username_session[0], who_is_PR_herf[1], self, trying=True)
                self.prise = 1
            except Exception as e:
                print("-**-----", e)
              
    def go_to_window(self, to_window):
        self.next_obj = to_window
        
    def fun1_part2(self): 
        if self.is_end:
            self.is_end = False
            if self.is_choice:
                if self.output_data:
                    ckeck_aktivity.show()
                    coin[0] += self.prise
                    change_victim_windiw.coin_text.setText(str(coin[0]) + " руб.")
                else:
                    ckeck_aktivity_no.show()
            
            self.hide()
            self.setEnabled(True)             
            '''if self.next_obj.__class__.__name__ in ["ckeckAktivity", "ckeckAktivityNo"]:
                if self.output_data:
                    
                   
            else:
            '''

        
coin = [0]
who_is_PR = ["robinnlike", "1000listnick"]
who_is_PR_herf = ["BzVEqzbiY75", "BzBEnjnCLxd"]
username_session = ['']
inst_obj = instogrammAPI()       
app = QApplication(sys.argv)
main_window = mainWindow()
goin = usersActivitesExpectation()
input_insta_window = inputInstaWindow()
change_victim_windiw = changeVictimWindiw()
ckeck_aktivity = ckeckAktivity()
ckeck_aktivity_no = ckeckAktivityNo()
go_loding = goLoding()

inst_obj.start()
#y = inst_obj.session.check_acc_instagram(str("gcgygv"))
main_window.show()
#inst_obj.ranning = False
sys.exit(app.exec_())

