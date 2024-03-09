import tkinter
from tkinter import ttk
from tkinter import messagebox
import string
import sqlite3

class moshaver(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('My Window')
        self.config(background='#e2dfd8')
        self.crt_menu()
        self.w=moshaver.winfo_screenmmwidth(self)
        self.h=moshaver.winfo_screenheight(self)
        self.geometry(f'{self.w}x{self.h-400}')
        self.btn1=tkinter.Button(text='Add Item',width=20,height=2,command=self.add)
        self.btn1.place(x=126,y=75)
        self.btn2=tkinter.Button(text='Search Item',width=20,height=2,command=self.Search)
        self.btn2.place(x=126,y=225)
        self.btn4=tkinter.Button(text='Update/Delete Item',width=20,height=2,command=self.up_del)
        self.btn4.place(x=126,y=375)
    def crt_menu(self):
        self.menubar = tkinter.Menu(self)
        self.config(menu=self.menubar)

        self.menu_act = tkinter.Menu(self.menubar,tearoff=0)
        self.menu_act.add_command(label='Add Item',command=self.add)
        self.menu_act.add_command(label='Search Item',command=self.Search)
        self.menu_act.add_command(label='Update/ Delete Item',command=self.up_del)

        self.menu_act.add_separator()
        self.menu_act.add_command(label='Exit')
        self.menubar.add_cascade(menu=self.menu_act, label='Action')

        self.menu_th=tkinter.Menu(self.menubar,tearoff=0)
        self.themint=tkinter.IntVar()
        self.menu_th.add_radiobutton(label='Dark',command=self.darkfunc,variable=self.themint,value=1)
        self.menu_th.add_radiobutton(label='Light',variable=self.themint,command=self.lightfunc,value=2)
        self.menubar.add_cascade(menu=self.menu_th, label='Theme')
    def add(self):
        self.add_window=tkinter.Toplevel(self)
        self.add_window.title("Add Item Window")
        self.add_window.geometry('500x700')
        self.add_window.config(background='#e2dfd8')
        self.type_lb=tkinter.Label(self.add_window,text='Type',width=10,height=2,bg='white')
        self.type_lb.place(x=0,y=0,height=40)
        self.radio1_2=tkinter.IntVar()
        self.radio1=tkinter.Radiobutton(self.add_window,text='Rent',background='white',fg='black',width=15,height=2,variable=self.radio1_2,value=1,command=self.disa)
        self.radio1.place(x=75,y=0,width=200)
        self.radio2=tkinter.Radiobutton(self.add_window,text='Buy',background='white',fg='black',width=15,height=2,variable=self.radio1_2,value=2,command=self.disa)
        self.radio2.place(x=258,y=0,width=200)
        self.area=tkinter.Label(self.add_window,text='Area(m)',bg='white',width=12,height=2)
        self.area.place(x=0,y=40)
        self.areentry=tkinter.Entry(self.add_window,width=33,font=43,relief='groove',border=3)
        self.areentry.place(x=90,y=40,height=36)
        self.nof=tkinter.Label(self.add_window,text='Num Of Rooms',bg='white',width=12,height=2)
        self.nof.place(x=0,y=76)
        self.nofentry=tkinter.Entry(self.add_window,width=33,font=40,relief='groove',border=3)
        self.nofentry.place(x=90,y=76,height=36)
        self.ppm=tkinter.Label(self.add_window,text='Price Per Meters',bg='white',width=12,height=2)
        self.ppm.place(x=0,y=112)
        self.ppmentry=tkinter.Entry(self.add_window,width=33,font=40,relief='groove',border=3,state='disabled')
        self.ppmentry.place(x=90,y=112,height=36)
        self.tp=tkinter.Label(self.add_window,text='Total Price',bg='white',width=12,height=2)
        self.tp.place(x=0,y=148)
        self.tpentry=tkinter.Entry(self.add_window,width=33,font=40,relief='groove',border=3,state='disabled')
        self.tpentry.place(x=90,y=148,height=36)
        self.deposit=tkinter.Label(self.add_window,text='Deposit',bg='white',width=12,height=2)
        self.deposit.place(x=0,y=184)
        self.depositentry=tkinter.Entry(self.add_window,width=33,font=40,relief='groove',border=3,state='disabled')
        self.depositentry.place(x=90,y=184,height=36)
        self.mr=tkinter.Label(self.add_window,text='Monthly Rent',bg='white',width=12,height=2)
        self.mr.place(x=0,y=220)
        self.mrentry=tkinter.Entry(self.add_window,width=33,font=40,relief='groove',border=3,state='disabled')
        self.mrentry.place(x=90,y=220,height=36)
        self.address=tkinter.Label(self.add_window,text='Address',bg='white',width=12,height=2)
        self.address.place(x=0,y=256)
        self.zonelist=[i for i in range(1,23)]
        self.zoneint = tkinter.StringVar()
        self.zoneint.set("Select Zone")
        self.zonecombo=ttk.Combobox(self.add_window,values=self.zonelist,textvariable=self.zoneint,font=1)
        self.zonecombo.place(x=90,y=256,height=36,width=180)
        self.zonestr=tkinter.StringVar()
        self.zonestr.set('Select District')

        self.dist = []
        self.dist1 = ["Niavaran",'Tajrish','Pasdaran','Araj','Ozgol','Imam Zade Ghasem','Evin','Baq Ferdows','Jamaran','Chizar','Hesar bo ali','Hekmat','Darabad','Darbamd','Darake','Dezashib','Zaferaniye','Sohanak','Shahrak Daneshgah','shahrak mahalati','Farmaniye','Qeytariye',"Kashanak","Kohsar","Golab Dare","Mahmodiye","Velenjak"]
        self.dist2 = ["Saadat Abad", "Marzdaran", "Tehran Villa", "Shahrak Azmayesh", "Tehransar","Tohid", "Evanak", "Aseman", "Baharood", "Mahalleh", "Darya", "Poonak","Kuye Nasr", "Satarkhan", "Sharif", "Daryane No", "Shahrake Ghods", "Sepehr","Parvaaz", "Shahrara", "Saadeghiye", "Farahzad"]
        self.dist3=["Ararat",  "Ekhtiariyeh", "Amaniye","Zargandeh", "Davoudiye", "Darous", "Seyed Khandan", "Qaba","Gholhak", "Kavousiyeh", "Vanak",'Sadr']
        self.dist4=["Tehranpars Sharqi",'Tehranpars Qarbi', "Pasdaran Zarab Khane",  "Hakimiyeh", "Shams abad", "Ehteshamieh", "Mehrane","Estakhr", "Nobonyad", "Awqaf", "Farjam", "Lavizan", "Saheb Alzaman","Shariati", "Delavarane", "Shahrake Sharifi", "Ghanate Kosar",'Golshan','Kohsar','Kalad','Narmak Shoamli','Elmo sanat','Hossein Abad','Shemiran No','Ghasem Abad']
        self.dist5=["Apadana", "Abazar", "Arme Mahalleh", "AkbarAbad", "Almahdi","Andisheh", "Bagh Feyz", "Baharan Mahalleh", "Poonak Jonobi","Poonak Shomali", "Jannatabad Jonoubi", "Jannatabad Shomali","Jannatabad Markazi", "Hesarak", "Sazman Ab", "Sazman Barnameh Jonobi","Sazman Barnameh Shomali", "Shahin Mahalleh", "Shahre Ziba","Shahran Jonobi","Shahran Shomali", "Shahrak Parvaz", "Shahrak Naft","Boulevard Ferdows Sharq", "Ferdows Gharb Naser Hejazi", "Kan","Kohsar", "Kuye Bime", "Moradabad"]
        self.dist6=["Jahad", "JamalZadeh", "Sanayi", "Vesal Shirazi", "Amirabad","Yousefabad", "Behjat Abad", "Karim Khan", "Saei", "Nezami Ganjavi","Iran Shahr", "Daneshga Tehran", "Nosrat", "Saei", "Sanayi","Fatemi", "Qezel Qale", "Keshavarz", "Valfajr", "Valie Asr"]
        self.dist7=["Aramene", "Amjadiyeh", "Khaghan", "Bahar", "Khajeh Nasir","Hoqooqi", "Khojeh Nazem alMolk", "Dehghan", "Gorgan","Sohravardi", "Baghe Saba", "Sharagh", "Abbas Abad", "Andisheh","Ghasr", "Hashemiye", "Kaj", "Majidieh", "Dabestan","Nezam Abad", "Niloufar", "Shahid Qandi"]
        self.dist8=["Taslihat ", "Tehranpars", "Dardasht", "Zarkesh", "Fadak","Kerman", "Lashkare Sharqi", "Lashkare Gharbi", "Majidiye", "Madaen","Narmak", "Haft Hoz", "Vahidiye", "Majidiye Jonobi"]
        self.dist9=["Azari Khiaban", "Mehrabad Jonobi" ,"Mehrabad Shomali", "30 Metri Jey", "20 Meter Shamshiri","21 Meter Jey", "Ostad Moein", "Pole Bridge", "Emamzade Abdullah", "Dastgheyb","Doctor Hoshiar", "Sarasiab Mehrabad", "Shamshiri", "Fath"]
        self.dist10=["Briank", "Zanjan Jonobi", "Salsabil Jonobi","Salsabil Shomali", "Shabiri","Karun Jonobi","Karun Shomali", "Hashemi", "Haft Chenar", "Soleimani","Komeyl", "Jeyhun"]
        self.dist11=["Azarbayjan", "Agahi", "Eskandari Jonobi", "Amiriye", "Anbar Naft","Jamalzadeh", "Hashem alDowleh", "Jomhuri", "Khoramshahr","Rah Ahan", "Sheikh Hadi", "Abbasi", "Foroosh", "Enghelab Khiaban","Ghalamestan", "Baradaran Javadian", "Makhsoos", "Meydane Hor","Helal Ahmar", "Karagar jonobi", "Dokhaniyat", "Abu Saeed","Vahdat Islami", "Kashan"]
        self.dist12=["Ferdowsi", "Baharestan Mahale", "Darvaze Shemron", "Iran","Pamennar", "Imamzadeh Yahya", "Abshar", "Sangalaj Mahale","Bazaar", "Qiyam", "Takhti", "Herendi Mahale", "Kowsar Mahale","Lalehzar", "Sangalaj",  "Molavi", "Khani Abad"]
        self.dist13=["Shahid Asadi", "Safa", "Zahed Gilani", "Eshraghi", "Dehghan","Nirouye Havayi", "Piroozi", "Hafeziyeh", "Emamat", "Shura","Ashitiani", "Zeinabiyeh", "Sorkhe Hesar"]
        self.dist14=["Sulaymaniyah", "Sad Dastgah", "Chahar Sad Dastgah", "Qasr Firouzeh","Sar Asiab", "Doolab", "Kuye Banke Rahni"]
        self.dist15=["Shahrak Masodiye", "Shahrak Valfajr", "Mesgar Abad", "Moshiriye","Afsariye", "Borujerdi", "Khavaran", "Mahale Tayeb","Khiaban Mansor",  "Atoban Basij", "َAtabak","Imam Ali", "Azadegan", "Khiaban Nabard", "Kianshahr","Sharak Rezvaniye", "Shush"]
        self.dist16=["Nazi Abad", "Javadiyeh", "Yakhchi Abad",  "Customs", "Khiaban Kargar", "Ali Abad", "Navab", "Kooye 17 Shahrivar "]
        self.dist17=["Abuzar Qarbi", "Abuzar Sharqi", "Golchin", "Moqaddam", "Imamzadeh Hasan","Ghaleh Morghi", "Zamzam", "Bolorsazi", "Jalili", "Azari", "Zahtabi", "Baharan"]
        self.dist18=["Tolid Darou", "behdasht", "Khalij Fasr Shomali","Khalij Fasr Jonobi","Yaftabad Shomali", "Yaftabad Jonobi", "Shadabad", "Shamsabad", "Ferdows","Shahid Rajaei", "Saheb al Zaman", "Shahrak Emam Khomeini ", "Sadeghi","Shahrak Valiasr  Jonobi", "17 Shahrivar","Shahrak Valiasr  Shomali"]
        self.dist19=["Nemat Abad", "Abdol Abad", "Shahid Kazemi", "Shahrake Resalat","Shariati", "Khani Abade No", "Bustane Velayat", "Esmail Abad","Esfandiari", "Bostan"]
        self.dist20=["Ebn Babevey", "Estakhr", "aqdasiyeh Shahre Rey","Beheshti", "Taqi Abad", "Javanmard Ghassab", "Hamzeh Abad","Dolat Abad", "Deylaman", "Sartakht", "13 Aban","Shahadat", "Zahir Abad", "Alaein", "Firouzabad", "Mansouriye and Mangol","Vali Abad"]
        self.dist21=["Shahrak Ekbatan ", "Tehransar", "Azadshahr", "Vilashahr", "Vardavard","bozorg rah Fath ", "Shahrak Kazemiye ", "Mahale Pasdaran ","Shahrak Azadi ", "Farhangian ", "Shahrak Esteghlal ","Shahrak Daneshgah Tehran  ", "Chitgar Shomali", "Shahrak Ghazaali"]
        self.dist22=["Shahrak Daneshgah Sharif ", "ShahrakKoohsatan ", "Shahrak Nasim ","Shahrak Negin Gharb ", "Shahrak Chitgar  ", "Shahrak Aseman Sepah ","Shahrak Shahid Kharrazi ", "Shahrak Eskan Sabz ", "Shahrak Moallem ","Shahrak Omid Dezhban ", "Shahrak Amirkabir ", "Shahrak Havaniruz ","Shahrak Shahid Baqeri ","Shahrak Peykan ","Dehkade Olympic ", "Shahrak Rahahan ","Shahrak Cheshmeh ", "Shahrak Sadra  (Jahadgaran)", "Shahrak Laleh ","Zibadasht Bala", "Shahrak Kosar ", "Shahrak Yas ", "Shahrak Sahel ","Zibadasht Payin", "Shahrak Sepah ", "Shahrak Shahab ", "Shahrak Azadshahr ","Shahrak Ati Shahr "]


        self.zonecombo1=ttk.Combobox(self.add_window,font=3,textvariable=self.zonestr,values=self.dist,state='disable')
        self.zonecombo1.place(x=268,y=256,height=36,width=191)
        self.zonecombo.bind("<<ComboboxSelected>>",self.zone_dis)
        self.faddress=tkinter.Label(self.add_window,text='Full Address',bg='white',width=12,height=2)
        self.faddress.place(x=0,y=292)
        self.faddressentry=tkinter.Entry(self.add_window,width=33,font=40,relief='groove',border=3)
        self.faddressentry.place(x=90,y=292,height=36)
        self.floor=tkinter.Label(self.add_window,text='Floor',bg='white',width=12,height=2)
        self.floor.place(x=0,y=328)
        self.floorentry=tkinter.Entry(self.add_window,width=3,relief='groove',border=3,font=1)
        self.floorentry.place(x=90,y=328,height=36)
        self.unit=tkinter.Label(self.add_window,text='Unit',bg='white',width=8,height=2)
        self.unit.place(x=130,y=328)
        self.unitentry=tkinter.Entry(self.add_window,width=3,relief='groove',border=3,font=1)
        self.unitentry.place(x=190,y=328,height=36)
        self.product=tkinter.Label(self.add_window,text='Product Year',bg='white',width=12,height=2)
        self.product.place(x=230,y=328,height=36,width=90)
        self.pro=[i for i in range(1340,1403)]
        self.proint=tkinter.IntVar()
        self.proint.set('Select Product Year')
        self.productcombo=ttk.Combobox(self.add_window,values=self.pro,font=1,width=11,textvariable=self.proint)
        self.productcombo.place(x=316,y=328,height=36)
        self.cabinets=tkinter.IntVar()
        self.cabinet=tkinter.Label(self.add_window,text='Cabinet',bg='white',width=12,height=2)
        self.cabinet.place(x=0,y=364)
        self.cabinetradio1=tkinter.Radiobutton(self.add_window,text='None',background='white',fg='black',width=9,height=2,value=1,variable=self.cabinets)
        self.cabinetradio1.place(x=90,y=364,height=36)
        self.cabinet2=tkinter.Radiobutton(self.add_window,text='MDF',background='white',fg='black',width=9,height=2,value=2,variable=self.cabinets)
        self.cabinet2.place(x=180,y=364,height=36)
        self.cabinet3=tkinter.Radiobutton(self.add_window,text='Chipboard',background='white',fg='black',width=9,height=2,value=3,variable=self.cabinets)
        self.cabinet3.place(x=270,y=364,height=36)
        self.cabinet4=tkinter.Radiobutton(self.add_window,text='High Glass',background='white',fg='black',width=10,height=2,value=4,variable=self.cabinets)
        self.cabinet4.place(x=360,y=364,height=36)
        self.floormat=tkinter.Label(self.add_window,text='Floor Material',bg='white',width=12,height=2)
        self.floormat.place(x=0,y=400)
        self.floormatint=tkinter.IntVar()
        self.floormatradio1=tkinter.Radiobutton(self.add_window,text='None',background='white',fg='black',width=9,height=2,value=1,variable=self.floormatint)
        self.floormatradio1.place(x=90,y=400,height=36)
        self.floormatradio2=tkinter.Radiobutton(self.add_window,text='Ceramic',background='white',fg='black',width=9,height=2,value=2,variable=self.floormatint)
        self.floormatradio2.place(x=180,y=400,height=36)
        self.floormatradio3=tkinter.Radiobutton(self.add_window,text='Parquet',background='white',fg='black',width=9,height=2,value=3,variable=self.floormatint)
        self.floormatradio3.place(x=270,y=400,height=36)
        self.floormatradio4=tkinter.Radiobutton(self.add_window,text='Mosaic',background='white',fg='black',width=10,height=2,value=4,variable=self.floormatint)
        self.floormatradio4.place(x=360,y=400,height=36)
        self.othoption=tkinter.Label(self.add_window,text='Other Options',bg='white',width=12,height=2)
        self.othoption.place(x=0,y=436)
        self.it1=tkinter.IntVar()
        self.it2=tkinter.IntVar()
        self.it3=tkinter.IntVar()
        self.othoption1=tkinter.Checkbutton(self.add_window,text='Basement',background='white',fg='black',width=12,height=2,variable=self.it1,offvalue=0,onvalue=1)
        self.othoption1.place(x=90,y=436,height=36)
        self.othoption2=tkinter.Checkbutton(self.add_window,text='Garage',background='white',fg='black',width=14,height=2,variable=self.it2,offvalue=0,onvalue=1)
        self.othoption2.place(x=200,y=436,height=36)
        self.othoption3=tkinter.Checkbutton(self.add_window,text='Elevator',background='white',fg='black',width=15,height=2,variable=self.it3,offvalue=0,onvalue=1)
        self.othoption3.place(x=325,y=436,height=36)
        self.addbutton=tkinter.Button(self.add_window,text='ADD ITEM',background='green',command=self.addathu)
        self.addbutton.place(x=200,y=490,height=36)



    def Search(self):
        self.srchwin=tkinter.Toplevel(self)
        self.srchwin.title('Search window')
        h=self.winfo_screenheight()
        w=self.winfo_screenwidth()
        self.srchwin.geometry(f'{h-400}x{w-1000}')
        self.srchwin.config(background='#e2dfd8')
        self.labelsrch=tkinter.Label(self.srchwin,text='Type',width=10,height=2,bg='white')
        self.labelsrch.place(x=0, y=0, height=40)
        self.radiosrch1 = tkinter.IntVar()
        self.radiosrch2int=tkinter.IntVar()
        self.radiosrchh1 = tkinter.Checkbutton(self.srchwin, text='Rent', background='white', fg='black', width=15,height=2, variable=self.radiosrch1,offvalue=0,onvalue=1,command=self.chtype)
        self.radiosrchh1.place(x=75, y=0, width=200)
        self.radiosrch2 = tkinter.Checkbutton(self.srchwin, text='Buy', background='white', fg='black', width=15,height=2, variable=self.radiosrch2int,offvalue=0,onvalue=1,command=self.chtype)
        self.radiosrch2.place(x=258, y=0, width=200)
        self.areasrch = tkinter.Label(self.srchwin, text='Area(m)', bg='white', width=12, height=2)
        self.areasrch.place(x=0, y=40)
        self.areentrysr = tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3)
        self.areentrysr.place(x=90, y=41, height=36)
        self.to=tkinter.Label(self.srchwin,text='----',width=4,height=2,bg='white',font=10)
        self.to.place(x=250,y=40,height=36)
        self.arenryse=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3)
        self.arenryse.place(x=298,y=40,height=36)
        self.nofsr=tkinter.Label(self.srchwin,text='Num Of Rooms',width=12,height=2,bg='white')
        self.nofsr.place(x=0, y=73)
        self.nofsrent=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3)
        self.nofsrent.place(x=90,y=74,height=36)
        self.to1 = tkinter.Label(self.srchwin, text='----', width=4, height=2, bg='white', font=10)
        self.to1.place(x=250, y=73, height=36)
        self.nofsrent1=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3)
        self.nofsrent1.place(x=298,y=73,height=36)
        self.ppmsr=tkinter.Label(self.srchwin,text='Price Per Meter',width=12,height=2,bg='white')
        self.ppmsr.place(x=0,y=106)
        self.ppmsren=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.ppmsren.place(x=90,y=106,height=36)
        self.to3=tkinter.Label(self.srchwin,text='----',width=4,height=2,bg='white',font=10)
        self.to3.place(x=250,y=106,height=36)
        self.ppmsren2=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.ppmsren2.place(x=298,y=106,height=36)
        self.tpsr=tkinter.Label(self.srchwin,text='Total Price',width=12,height=2,bg='white')
        self.tpsr.place(x=0,y=139)
        self.tpsren=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.tpsren.place(x=90,y=139,height=36)
        self.to4=tkinter.Label(self.srchwin,text='----',width=4,height=2,bg='white',font=10)
        self.to4.place(x=250,y=139,height=36)
        self.tpsren1=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.tpsren1.place(x=298,y=139,height=36)
        self.depsr=tkinter.Label(self.srchwin,text='Deposit',width=12,height=2,bg='white')
        self.depsr.place(x=0,y=172,height=36)
        self.depsren=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.depsren.place(x=90,y=172,height=36)
        self.to5=tkinter.Label(self.srchwin,text='----',width=4,height=2,bg='white',font=10)
        self.to5.place(x=250,y=172,height=36)
        self.desr1=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.desr1.place(x=298,y=172,height=36)
        self.mrsr=tkinter.Label(self.srchwin,text='Monthly Rent',width=12,height=2,bg='white')
        self.mrsr.place(x=0,y=205)
        self.mrsren=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.mrsren.place(x=90,y=205,height=36)
        self.to6=tkinter.Label(self.srchwin,text='----',width=4,height=2,bg='white',font=10)
        self.to6.place(x=250,y=205,height=36)
        self.mrsren1=tkinter.Entry(self.srchwin, width=14, font=43, relief='groove', border=3,state='disabled')
        self.mrsren1.place(x=298,y=205,height=36)

        self.addresssr = tkinter.Label(self.srchwin, text='Address', bg='white', width=12, height=2)
        self.addresssr.place(x=0, y=239)
        self.zonelistsr = [i for i in range(1, 23)]
        self.zoneintsr = tkinter.StringVar()
        self.zoneintsr.set("Select Zone")
        self.zonecombosr = ttk.Combobox(self.srchwin, values=self.zonelistsr, textvariable=self.zoneintsr, font=1)
        self.zonecombosr.place(x=90, y=239, height=36, width=180)
        self.zonestrsr = tkinter.StringVar()
        self.zonestrsr.set('Select District')

        self.distsr = []
        self.dist1sr = ["Niavaran", 'Tajrish', 'Pasdaran', 'Araj', 'Ozgol', 'Imam Zade Ghasem', 'Evin', 'Baq Ferdows',
                      'Jamaran', 'Chizar', 'Hesar bo ali', 'Hekmat', 'Darabad', 'Darbamd', 'Darake', 'Dezashib',
                      'Zaferaniye', 'Sohanak', 'Shahrak Daneshgah', 'shahrak mahalati', 'Farmaniye', 'Qeytariye',
                      "Kashanak", "Kohsar", "Golab Dare", "Mahmodiye", "Velenjak"]
        self.dist2sr = ["Saadat Abad", "Marzdaran", "Tehran Villa", "Shahrak Azmayesh", "Tehransar", "Tohid", "Evanak",
                      "Aseman", "Baharood", "Mahalleh", "Darya", "Poonak", "Kuye Nasr", "Satarkhan", "Sharif",
                      "Daryane No", "Shahrake Ghods", "Sepehr", "Parvaaz", "Shahrara", "Saadeghiye", "Farahzad"]
        self.dist3sr = ["Ararat", "Ekhtiariyeh", "Amaniye", "Zargandeh", "Davoudiye", "Darous", "Seyed Khandan", "Qaba",
                      "Gholhak", "Kavousiyeh", "Vanak", 'Sadr']
        self.dist4sr = ["Tehranpars Sharqi", 'Tehranpars Qarbi', "Pasdaran Zarab Khane", "Hakimiyeh", "Shams abad",
                      "Ehteshamieh", "Mehrane", "Estakhr", "Nobonyad", "Awqaf", "Farjam", "Lavizan", "Saheb Alzaman",
                      "Shariati", "Delavarane", "Shahrake Sharifi", "Ghanate Kosar", 'Golshan', 'Kohsar', 'Kalad',
                      'Narmak Shoamli', 'Elmo sanat', 'Hossein Abad', 'Shemiran No', 'Ghasem Abad']
        self.dist5sr = ["Apadana", "Abazar", "Arme Mahalleh", "AkbarAbad", "Almahdi", "Andisheh", "Bagh Feyz",
                      "Baharan Mahalleh", "Poonak Jonobi", "Poonak Shomali", "Jannatabad Jonoubi", "Jannatabad Shomali",
                      "Jannatabad Markazi", "Hesarak", "Sazman Ab", "Sazman Barnameh Jonobi", "Sazman Barnameh Shomali",
                      "Shahin Mahalleh", "Shahre Ziba", "Shahran Jonobi", "Shahran Shomali", "Shahrak Parvaz",
                      "Shahrak Naft", "Boulevard Ferdows Sharq", "Ferdows Gharb Naser Hejazi", "Kan", "Kohsar",
                      "Kuye Bime", "Moradabad"]
        self.dist6sr = ["Jahad", "JamalZadeh", "Sanayi", "Vesal Shirazi", "Amirabad", "Yousefabad", "Behjat Abad",
                      "Karim Khan", "Saei", "Nezami Ganjavi", "Iran Shahr", "Daneshga Tehran", "Nosrat", "Saei",
                      "Sanayi", "Fatemi", "Qezel Qale", "Keshavarz", "Valfajr", "Valie Asr"]
        self.dist7sr = ["Aramene", "Amjadiyeh", "Khaghan", "Bahar", "Khajeh Nasir", "Hoqooqi", "Khojeh Nazem alMolk",
                      "Dehghan", "Gorgan", "Sohravardi", "Baghe Saba", "Sharagh", "Abbas Abad", "Andisheh", "Ghasr",
                      "Hashemiye", "Kaj", "Majidieh", "Dabestan", "Nezam Abad", "Niloufar", "Shahid Qandi"]
        self.dist8sr = ["Taslihat ", "Tehranpars", "Dardasht", "Zarkesh", "Fadak", "Kerman", "Lashkare Sharqi",
                      "Lashkare Gharbi", "Majidiye", "Madaen", "Narmak", "Haft Hoz", "Vahidiye", "Majidiye Jonobi"]
        self.dist9sr = ["Azari Khiaban", "Mehrabad Jonobi", "Mehrabad Shomali", "30 Metri Jey", "20 Meter Shamshiri",
                      "21 Meter Jey", "Ostad Moein", "Pole Bridge", "Emamzade Abdullah", "Dastgheyb", "Doctor Hoshiar",
                      "Sarasiab Mehrabad", "Shamshiri", "Fath"]
        self.dist10sr = ["Briank", "Zanjan Jonobi", "Salsabil Jonobi", "Salsabil Shomali", "Shabiri", "Karun Jonobi",
                       "Karun Shomali", "Hashemi", "Haft Chenar", "Soleimani", "Komeyl", "Jeyhun"]
        self.dist11sr = ["Azarbayjan", "Agahi", "Eskandari Jonobi", "Amiriye", "Anbar Naft", "Jamalzadeh",
                       "Hashem alDowleh", "Jomhuri", "Khoramshahr", "Rah Ahan", "Sheikh Hadi", "Abbasi", "Foroosh",
                       "Enghelab Khiaban", "Ghalamestan", "Baradaran Javadian", "Makhsoos", "Meydane Hor",
                       "Helal Ahmar", "Karagar jonobi", "Dokhaniyat", "Abu Saeed", "Vahdat Islami", "Kashan"]
        self.dist12sr = ["Ferdowsi", "Baharestan Mahale", "Darvaze Shemron", "Iran", "Pamennar", "Imamzadeh Yahya",
                       "Abshar", "Sangalaj Mahale", "Bazaar", "Qiyam", "Takhti", "Herendi Mahale", "Kowsar Mahale",
                       "Lalehzar", "Sangalaj", "Molavi", "Khani Abad"]
        self.dist13sr = ["Shahid Asadi", "Safa", "Zahed Gilani", "Eshraghi", "Dehghan", "Nirouye Havayi", "Piroozi",
                       "Hafeziyeh", "Emamat", "Shura", "Ashitiani", "Zeinabiyeh", "Sorkhe Hesar"]
        self.dist14sr = ["Sulaymaniyah", "Sad Dastgah", "Chahar Sad Dastgah", "Qasr Firouzeh", "Sar Asiab", "Doolab",
                       "Kuye Banke Rahni"]
        self.dist15sr = ["Shahrak Masodiye", "Shahrak Valfajr", "Mesgar Abad", "Moshiriye", "Afsariye", "Borujerdi",
                       "Khavaran", "Mahale Tayeb", "Khiaban Mansor", "Atoban Basij", "َAtabak", "Imam Ali", "Azadegan",
                       "Khiaban Nabard", "Kianshahr", "Sharak Rezvaniye", "Shush"]
        self.dist16sr = ["Nazi Abad", "Javadiyeh", "Yakhchi Abad", "Customs", "Khiaban Kargar", "Ali Abad", "Navab",
                       "Kooye 17 Shahrivar "]
        self.dist17sr = ["Abuzar Qarbi", "Abuzar Sharqi", "Golchin", "Moqaddam", "Imamzadeh Hasan", "Ghaleh Morghi",
                       "Zamzam", "Bolorsazi", "Jalili", "Azari", "Zahtabi", "Baharan"]
        self.dist18sr = ["Tolid Darou", "behdasht", "Khalij Fasr Shomali", "Khalij Fasr Jonobi", "Yaftabad Shomali",
                       "Yaftabad Jonobi", "Shadabad", "Shamsabad", "Ferdows", "Shahid Rajaei", "Saheb al Zaman",
                       "Shahrak Emam Khomeini ", "Sadeghi", "Shahrak Valiasr  Jonobi", "17 Shahrivar",
                       "Shahrak Valiasr  Shomali"]
        self.dist19sr = ["Nemat Abad", "Abdol Abad", "Shahid Kazemi", "Shahrake Resalat", "Shariati", "Khani Abade No",
                       "Bustane Velayat", "Esmail Abad", "Esfandiari", "Bostan"]
        self.dist20sr = ["Ebn Babevey", "Estakhr", "aqdasiyeh Shahre Rey", "Beheshti", "Taqi Abad", "Javanmard Ghassab",
                       "Hamzeh Abad", "Dolat Abad", "Deylaman", "Sartakht", "13 Aban", "Shahadat", "Zahir Abad",
                       "Alaein", "Firouzabad", "Mansouriye and Mangol", "Vali Abad"]
        self.dist21sr = ["Shahrak Ekbatan ", "Tehransar", "Azadshahr", "Vilashahr", "Vardavard", "bozorg rah Fath ",
                       "Shahrak Kazemiye ", "Mahale Pasdaran ", "Shahrak Azadi ", "Farhangian ", "Shahrak Esteghlal ",
                       "Shahrak Daneshgah Tehran  ", "Chitgar Shomali", "Shahrak Ghazaali"]
        self.dist22sr = ["Shahrak Daneshgah Sharif ", "ShahrakKoohsatan ", "Shahrak Nasim ", "Shahrak Negin Gharb ",
                       "Shahrak Chitgar  ", "Shahrak Aseman Sepah ", "Shahrak Shahid Kharrazi ", "Shahrak Eskan Sabz ",
                       "Shahrak Moallem ", "Shahrak Omid Dezhban ", "Shahrak Amirkabir ", "Shahrak Havaniruz ",
                       "Shahrak Shahid Baqeri ", "Shahrak Peykan ", "Dehkade Olympic ", "Shahrak Rahahan ",
                       "Shahrak Cheshmeh ", "Shahrak Sadra  (Jahadgaran)", "Shahrak Laleh ", "Zibadasht Bala",
                       "Shahrak Kosar ", "Shahrak Yas ", "Shahrak Sahel ", "Zibadasht Payin", "Shahrak Sepah ",
                       "Shahrak Shahab ", "Shahrak Azadshahr ", "Shahrak Ati Shahr "]

        self.distsr.append(self.dist1sr)
        self.distsr.append(self.dist2sr)
        self.distsr.append(self.dist3sr)
        self.distsr.append(self.dist4sr)
        self.distsr.append(self.dist5sr)
        self.distsr.append(self.dist6sr)
        self.distsr.append(self.dist7sr)
        self.distsr.append(self.dist8sr)
        self.distsr.append(self.dist9sr)
        self.distsr.append(self.dist10sr)
        self.distsr.append(self.dist11sr)
        self.distsr.append(self.dist12sr)
        self.distsr.append(self.dist13sr)
        self.distsr.append(self.dist14sr)
        self.distsr.append(self.dist15sr)
        self.distsr.append(self.dist16sr)
        self.distsr.append(self.dist17sr)
        self.distsr.append(self.dist18sr)
        self.distsr.append(self.dist19sr)
        self.distsr.append(self.dist20sr)
        self.distsr.append(self.dist21sr)
        self.distsr.append(self.dist22sr)

        self.zonecombo1sr = ttk.Combobox(self.srchwin, font=3, textvariable=self.zonestrsr, values=self.distsr)
        self.zonecombo1sr.place(x=269, y=239, height=36, width=191)
        self.zonecombosr.bind("<<ComboboxSelected>>", self.zone_dissr)

        self.prsr=tkinter.Label(self.srchwin, text='Product Year', bg='white', width=12, height=2)
        self.prsr.place(x=0,y=273)

        self.yrsr=[i for i in range(1340,1402)]
        self.prosr = tkinter.IntVar()
        self.prosr.set("Select")
        self.prysr=ttk.Combobox(self.srchwin, values=self.yrsr, font=1,textvariable=self.prosr)
        self.prysr.place(x=90,y=274,height=36,width=162)

        self.tosr=tkinter.Label(self.srchwin,text='----',width=4,height=2,bg='white',font=10,relief='groove')
        self.tosr.place(x=250,y=275,height=36)

        self.yrsr1 = [i for i in range(1340, 1402)]
        self.prosr1=tkinter.IntVar()
        self.prosr1.set('Select')
        self.prysr1=ttk.Combobox(self.srchwin, font=1,values=self.yrsr1,textvariable=self.prosr1)
        self.prysr1.place(x=298,y=274,height=36,width=162)

        self.floorsr = tkinter.Label(self.srchwin, text='Floor', bg='white', width=15, height=2)
        self.floorsr.place(x=0, y=310)
        self.floorentrysr = tkinter.Entry(self.srchwin, width=14, relief='groove', border=3, font=1)
        self.floorentrysr.place(x=90, y=310, height=36)
        self.unitsr = tkinter.Label(self.srchwin, text='Unit', bg='white', width=6, height=2)
        self.unitsr.place(x=250, y=310)
        self.unitentrysr = tkinter.Entry(self.srchwin, width=14, relief='groove', border=3, font=1)
        self.unitentrysr.place(x=298, y=310, height=36)

        self.cabinetssr = tkinter.IntVar()
        self.cabinetsr = tkinter.Label(self.srchwin, text='Cabinet', bg='white', width=12, height=2)
        self.cabinetsr.place(x=0, y=345)
        self.cabinetradio1sr = tkinter.Radiobutton(self.srchwin, text='None', background='white', fg='black', width=9,
                                                  height=2, value=1, variable=self.cabinetssr)
        self.cabinetradio1sr.place(x=90, y=345, height=36)
        self.cabinet2sr = tkinter.Radiobutton(self.srchwin, text='MDF', background='white', fg='black', width=9,
                                             height=2, value=2, variable=self.cabinetssr)
        self.cabinet2sr.place(x=180, y=345, height=36)
        self.cabinet3sr = tkinter.Radiobutton(self.srchwin, text='Chipboard', background='white', fg='black', width=9,
                                             height=2, value=3, variable=self.cabinetssr)
        self.cabinet3sr.place(x=270, y=345, height=36)
        self.cabinet4sr = tkinter.Radiobutton(self.srchwin, text='High Glass', background='white', fg='black',
                                             width=10, height=2, value=4, variable=self.cabinetssr)
        self.cabinet4sr.place(x=361, y=345, height=36)
        self.floormatsr = tkinter.Label(self.srchwin, text='Floor Material', bg='white', width=12, height=2)
        self.floormatsr.place(x=0, y=380)
        self.floormatintsr = tkinter.IntVar()
        self.floormatradio1sr = tkinter.Radiobutton(self.srchwin, text='None', background='white', fg='black', width=9,
                                                   height=2, value=1, variable=self.floormatintsr)
        self.floormatradio1sr.place(x=90, y=380, height=36)
        self.floormatradio2sr = tkinter.Radiobutton(self.srchwin, text='Ceramic', background='white', fg='black',
                                                   width=9, height=2, value=2, variable=self.floormatintsr)
        self.floormatradio2sr.place(x=180, y=380, height=36)
        self.floormatradio3sr = tkinter.Radiobutton(self.srchwin, text='Parquet', background='white', fg='black',
                                                   width=9, height=2, value=3, variable=self.floormatintsr)
        self.floormatradio3sr.place(x=270, y=380, height=36)
        self.floormatradio4sr = tkinter.Radiobutton(self.srchwin, text='Mosaic', background='white', fg='black',
                                                   width=10, height=2, value=4, variable=self.floormatintsr)
        self.floormatradio4sr.place(x=361, y=380, height=36)
        self.othoptionsr = tkinter.Label(self.srchwin, text='Other Options', bg='white', width=12, height=2)
        self.othoptionsr.place(x=0, y=415)
        self.othoption1sr = tkinter.Checkbutton(self.srchwin, text='Basement', background='white', fg='black',
                                               width=12, height=2)
        self.othoption1sr.place(x=90, y=415, height=36)
        self.othoption2sr = tkinter.Checkbutton(self.srchwin, text='Garage', background='white', fg='black', width=14,
                                               height=2)
        self.othoption2sr.place(x=200, y=415, height=36)
        self.othoption3sr = tkinter.Checkbutton(self.srchwin, text='Elevator', background='white', fg='black',
                                               width=15, height=2)
        self.othoption3sr.place(x=326, y=415, height=36)
        self.addbuttonsr=tkinter.Button(self.srchwin,text='SEARCH ITEM',background='green',command=self.btnsrch)
        self.addbuttonsr.place(x=200,y=468,height=36)



    def up_del(self):
        self.updel=tkinter.Toplevel(self)
        self.updel.geometry('500x700')
        self.updel.config(background='#e2dfd8')
        self.updel.title('Update And Delete window')
        self.file_code=tkinter.Label(self.updel,text='File Code',width=10,height=2,bg='white')
        self.file_code.place(x=0,y=0,width=86)
        self.file_codeen=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3)
        self.file_codeen.place(x=87,y=0,height=36,width=336)
        self.typeup=tkinter.Label(self.updel,text='Type',width=10,height=2,bg='white')
        self.typeup.place(x=0,y=36,width=86)
        self.rentbuy=tkinter.IntVar()
        self.rentup=tkinter.Radiobutton(self.updel, text='Rent', background='white', fg='black', width=15,height=2, value=1,variable=self.rentbuy,state='disabled')
        self.rentup.place(x=76,y=36,height=36,width=200)
        self.buyup=tkinter.Radiobutton(self.updel, text='Buy', background='white', fg='black', width=15,height=2, value=2,variable=self.rentbuy,state='disabled')
        self.buyup.place(x=209,y=36,height=36,width=213)
        self.areaup=tkinter.Label(self.updel,text='Area(m)',width=10,height=2,bg='white')
        self.areaup.place(x=0,y=72,width=86)
        self.areenup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.areenup.place(x=87,y=72,height=36,width=336)
        self.norup=tkinter.Label(self.updel,text='Num Of Rooms',width=11,height=2,bg='white')
        self.norup.place(x=0,y=108,width=86)
        self.norrnup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.norrnup.place(x=87,y=108,height=36,width=336)
        self.ppmup=tkinter.Label(self.updel,text='Price Per Meter',width=10,height=2,bg='white')
        self.ppmup.place(x=0,y=144,width=86)
        self.ppmenup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.ppmenup.place(x=87,y=144,height=36,width=336)
        self.tpup=tkinter.Label(self.updel,text='Total Price',width=10,height=2,bg='white')
        self.tpup.place(x=0,y=180,width=86)
        self.tpenup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.tpenup.place(x=87,y=180,width=336,height=36)
        self.depup=tkinter.Label(self.updel,text='Deposit',width=10,height=2,bg='white')
        self.depup.place(x=0,y=216,height=36,width=86)
        self.depenup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.depenup.place(x=87,y=216,height=36,width=336)
        self.mrup=tkinter.Label(self.updel,text='Monthly Rent',width=10,height=2,bg='white')
        self.mrup.place(x=0,y=252,height=36,width=86)
        self.mrenup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.mrenup.place(x=87,y=252,height=36,width=336)
        self.addressup=tkinter.Label(self.updel,text='Address',width=10,height=2,bg='white')
        self.addressup.place(x=0,y=288,height=36,width=86)
        self.zonelistup=[i for i in range(1,23)]
        self.zoneintup=tkinter.IntVar()
        self.zoneintup.set("Select Zone")
        self.addresscomboup=ttk.Combobox(self.updel, font=1,values=self.zonelistup,textvariable=self.zoneintup,state='disabled')
        self.addresscomboup.place(x=87,y=288,height=36,width=168)
        self.zonestrup = tkinter.StringVar()
        self.zonestrup.set('Select District')
        self.distup = []
        self.dist1up = ["Niavaran", 'Tajrish', 'Pasdaran', 'Araj', 'Ozgol', 'Imam Zade Ghasem', 'Evin', 'Baq Ferdows','Jamaran', 'Chizar', 'Hesar bo ali', 'Hekmat', 'Darabad', 'Darbamd', 'Darake', 'Dezashib','Zaferaniye', 'Sohanak', 'Shahrak Daneshgah', 'shahrak mahalati', 'Farmaniye', 'Qeytariye',"Kashanak", "Kohsar", "Golab Dare", "Mahmodiye", "Velenjak"]
        self.dist2up = ["Saadat Abad", "Marzdaran", "Tehran Villa", "Shahrak Azmayesh", "Tehransar", "Tohid", "Evanak","Aseman", "Baharood", "Mahalleh", "Darya", "Poonak", "Kuye Nasr", "Satarkhan", "Sharif","Daryane No", "Shahrake Ghods", "Sepehr", "Parvaaz", "Shahrara", "Saadeghiye", "Farahzad"]
        self.dist3up = ["Ararat", "Ekhtiariyeh", "Amaniye", "Zargandeh", "Davoudiye", "Darous", "Seyed Khandan", "Qaba","Gholhak", "Kavousiyeh", "Vanak", 'Sadr']
        self.dist4up = ["Tehranpars Sharqi", 'Tehranpars Qarbi', "Pasdaran Zarab Khane", "Hakimiyeh", "Shams abad","Ehteshamieh", "Mehrane", "Estakhr", "Nobonyad", "Awqaf", "Farjam", "Lavizan", "Saheb Alzaman","Shariati", "Delavarane", "Shahrake Sharifi", "Ghanate Kosar", 'Golshan', 'Kohsar', 'Kalad','Narmak Shoamli', 'Elmo sanat', 'Hossein Abad', 'Shemiran No', 'Ghasem Abad']
        self.dist5up = ["Apadana", "Abazar", "Arme Mahalleh", "AkbarAbad", "Almahdi", "Andisheh", "Bagh Feyz","Baharan Mahalleh", "Poonak Jonobi", "Poonak Shomali", "Jannatabad Jonoubi","Jannatabad Shomali","Jannatabad Markazi", "Hesarak", "Sazman Ab", "Sazman Barnameh Jonobi","Sazman Barnameh Shomali","Shahin Mahalleh", "Shahre Ziba", "Shahran Jonobi", "Shahran Shomali", "Shahrak Parvaz","Shahrak Naft", "Boulevard Ferdows Sharq", "Ferdows Gharb Naser Hejazi", "Kan", "Kohsar","Kuye Bime", "Moradabad"]
        self.dist6up = ["Jahad", "JamalZadeh", "Sanayi", "Vesal Shirazi", "Amirabad", "Yousefabad", "Behjat Abad","Karim Khan", "Saei", "Nezami Ganjavi", "Iran Shahr", "Daneshga Tehran", "Nosrat", "Saei","Sanayi", "Fatemi", "Qezel Qale", "Keshavarz", "Valfajr", "Valie Asr"]
        self.dist7up = ["Aramene", "Amjadiyeh", "Khaghan", "Bahar", "Khajeh Nasir", "Hoqooqi", "Khojeh Nazem alMolk","Dehghan", "Gorgan", "Sohravardi", "Baghe Saba", "Sharagh", "Abbas Abad", "Andisheh", "Ghasr","Hashemiye", "Kaj", "Majidieh", "Dabestan", "Nezam Abad", "Niloufar", "Shahid Qandi"]
        self.dist8up = ["Taslihat ", "Tehranpars", "Dardasht", "Zarkesh", "Fadak", "Kerman", "Lashkare Sharqi","Lashkare Gharbi", "Majidiye", "Madaen", "Narmak", "Haft Hoz", "Vahidiye", "Majidiye Jonobi"]
        self.dist9up = ["Azari Khiaban", "Mehrabad Jonobi", "Mehrabad Shomali", "30 Metri Jey", "20 Meter Shamshiri","21 Meter Jey", "Ostad Moein", "Pole Bridge", "Emamzade Abdullah", "Dastgheyb","Doctor Hoshiar","Sarasiab Mehrabad", "Shamshiri", "Fath"]
        self.dist10up = ["Briank", "Zanjan Jonobi", "Salsabil Jonobi", "Salsabil Shomali", "Shabiri", "Karun Jonobi","Karun Shomali", "Hashemi", "Haft Chenar", "Soleimani", "Komeyl", "Jeyhun"]
        self.dist11up = ["Azarbayjan", "Agahi", "Eskandari Jonobi", "Amiriye", "Anbar Naft", "Jamalzadeh","Hashem alDowleh", "Jomhuri", "Khoramshahr", "Rah Ahan", "Sheikh Hadi", "Abbasi", "Foroosh","Enghelab Khiaban", "Ghalamestan", "Baradaran Javadian", "Makhsoos", "Meydane Hor","Helal Ahmar", "Karagar jonobi", "Dokhaniyat", "Abu Saeed", "Vahdat Islami", "Kashan"]
        self.dist12up = ["Ferdowsi", "Baharestan Mahale", "Darvaze Shemron", "Iran", "Pamennar", "Imamzadeh Yahya","Abshar", "Sangalaj Mahale", "Bazaar", "Qiyam", "Takhti", "Herendi Mahale", "Kowsar Mahale","Lalehzar", "Sangalaj", "Molavi", "Khani Abad"]
        self.dist13up = ["Shahid Asadi", "Safa", "Zahed Gilani", "Eshraghi", "Dehghan", "Nirouye Havayi", "Piroozi","Hafeziyeh", "Emamat", "Shura", "Ashitiani", "Zeinabiyeh", "Sorkhe Hesar"]
        self.dist14up = ["Sulaymaniyah", "Sad Dastgah", "Chahar Sad Dastgah", "Qasr Firouzeh", "Sar Asiab", "Doolab","Kuye Banke Rahni"]
        self.dist15up = ["Shahrak Masodiye", "Shahrak Valfajr", "Mesgar Abad", "Moshiriye", "Afsariye", "Borujerdi","Khavaran", "Mahale Tayeb", "Khiaban Mansor", "Atoban Basij", "َAtabak", "Imam Ali","Azadegan","Khiaban Nabard", "Kianshahr", "Sharak Rezvaniye", "Shush"]
        self.dist16up = ["Nazi Abad", "Javadiyeh", "Yakhchi Abad", "Customs", "Khiaban Kargar", "Ali Abad", "Navab","Kooye 17 Shahrivar "]
        self.dist17up = ["Abuzar Qarbi", "Abuzar Sharqi", "Golchin", "Moqaddam", "Imamzadeh Hasan", "Ghaleh Morghi","Zamzam", "Bolorsazi", "Jalili", "Azari", "Zahtabi", "Baharan"]
        self.dist18up = ["Tolid Darou", "behdasht", "Khalij Fasr Shomali", "Khalij Fasr Jonobi", "Yaftabad Shomali","Yaftabad Jonobi", "Shadabad", "Shamsabad", "Ferdows", "Shahid Rajaei", "Saheb al Zaman","Shahrak Emam Khomeini ", "Sadeghi", "Shahrak Valiasr  Jonobi", "17 Shahrivar","Shahrak Valiasr  Shomali"]
        self.dist19up = ["Nemat Abad", "Abdol Abad", "Shahid Kazemi", "Shahrake Resalat", "Shariati", "Khani Abade No","Bustane Velayat", "Esmail Abad", "Esfandiari", "Bostan"]
        self.dist20up = ["Ebn Babevey", "Estakhr", "aqdasiyeh Shahre Rey", "Beheshti", "Taqi Abad", "Javanmard Ghassab","Hamzeh Abad", "Dolat Abad", "Deylaman", "Sartakht", "13 Aban", "Shahadat", "Zahir Abad","Alaein", "Firouzabad", "Mansouriye and Mangol", "Vali Abad"]
        self.dist21up = ["Shahrak Ekbatan ", "Tehransar", "Azadshahr", "Vilashahr", "Vardavard", "bozorg rah Fath ","Shahrak Kazemiye ", "Mahale Pasdaran ", "Shahrak Azadi ", "Farhangian ", "Shahrak Esteghlal ","Shahrak Daneshgah Tehran  ", "Chitgar Shomali", "Shahrak Ghazaali"]
        self.dist22up = ["Shahrak Daneshgah Sharif ", "ShahrakKoohsatan ", "Shahrak Nasim ", "Shahrak Negin Gharb ","Shahrak Chitgar  ", "Shahrak Aseman Sepah ", "Shahrak Shahid Kharrazi ","Shahrak Eskan Sabz ","Shahrak Moallem ", "Shahrak Omid Dezhban ", "Shahrak Amirkabir ", "Shahrak Havaniruz ","Shahrak Shahid Baqeri ", "Shahrak Peykan ", "Dehkade Olympic ", "Shahrak Rahahan ","Shahrak Cheshmeh ", "Shahrak Sadra  (Jahadgaran)", "Shahrak Laleh ", "Zibadasht Bala","Shahrak Kosar ", "Shahrak Yas ", "Shahrak Sahel ", "Zibadasht Payin", "Shahrak Sepah ","Shahrak Shahab ", "Shahrak Azadshahr ", "Shahrak Ati Shahr "]


        self.addressdisup1=ttk.Combobox(self.updel, font=1,values=self.distup,textvariable=self.zonestrup,state='disabled')
        self.addressdisup1.place(x=255,y=288,height=36,width=168)
        self.addresscomboup.bind("<<ComboboxSelected>>",self.zone_disup)
        self.faddressup=tkinter.Label(self.updel,text='Full Address',width=10,height=2,bg='white')
        self.faddressup.place(x=0,y=324,height=36,width=86)
        self.faddressenup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.faddressenup.place(x=87,y=324,height=36,width=336)
        self.floorup=tkinter.Label(self.updel,text='Floor',width=10,height=2,bg='white')
        self.floorup.place(x=0,y=360,width=86)
        self.floorenup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.floorenup.place(x=87,y=360,height=36,width=50)
        self.unitup=tkinter.Label(self.updel,text='Unit',width=10,height=2,bg='white')
        self.unitup.place(x=137,y=360,width=52)
        self.unienup=tkinter.Entry(self.updel, width=14, font=43, relief='groove', border=3,state='disabled')
        self.unienup.place(x=189,y=360,height=36,width=50)
        self.pyup=tkinter.Label(self.updel,text='Product Year',width=10,height=2,bg='white')
        self.pyup.place(x=239,y=360,width=70)
        self.pruplist=[i for i in range(1340,1402)]
        self.printt=tkinter.IntVar()
        self.printt.set('Select')
        self.prcombobo=ttk.Combobox(self.updel, font=1,values=self.pruplist,textvariable=self.printt,state='disabled')
        self.prcombobo.place(x=309,y=360,height=36,width=115)
        self.cabinetup=tkinter.Label(self.updel,text='Cabinet Type',width=10,height=2,bg='white')
        self.cabinetup.place(x=0,y=396,width=85)
        self.cabinetintup=tkinter.IntVar()
        self.cabinetradioup1=tkinter.Radiobutton(self.updel, text='None', background='white', fg='black', width=15,height=2, value=1,variable=self.cabinetintup,state='disabled')
        self.cabinetradioup1.place(x=85,y=396,width=80,height=36)
        self.cabinetradioup2 = tkinter.Radiobutton(self.updel, text='MDF', background='white', fg='black', width=15,height=2, value=2,variable=self.cabinetintup,state='disabled')
        self.cabinetradioup2.place(x=165,y=396,width=80,height=36)
        self.cabinetradioup3 = tkinter.Radiobutton(self.updel, text='Chipboard', background='white', fg='black', width=15,height=2, value=3,variable=self.cabinetintup,state='disabled')
        self.cabinetradioup3.place(x=245,y=396,width=80,height=36)
        self.cabinetradioup4 = tkinter.Radiobutton(self.updel, text='High Glass', background='white', fg='black', width=15,height=2, value=4,variable=self.cabinetintup,state='disabled')
        self.cabinetradioup4.place(x=325,y=396,width=98,height=36)
        self.floorup=tkinter.Label(self.updel,text='Floor Material',width=10,height=2,bg='white')
        self.floorup.place(x=0,y=432,width=85)
        self.floorintup = tkinter.IntVar()
        self.floorup1=tkinter.Radiobutton(self.updel, text='None', background='white', fg='black', width=15,height=2, value=1,variable=self.floorintup,state='disabled')
        self.floorup1.place(x=85,y=432,height=36,width=98)
        self.floorup2=tkinter.Radiobutton(self.updel, text='Ceramic', background='white', fg='black', width=15,height=2, value=2,variable=self.floorintup,state='disabled')
        self.floorup2.place(x=165,y=432,height=36,width=98)
        self.floorup3=tkinter.Radiobutton(self.updel, text='Parquet', background='white', fg='black', width=15,height=2, value=3,variable=self.floorintup,state='disabled')
        self.floorup3.place(x=245,y=432,height=36,width=98)
        self.floorup4=tkinter.Radiobutton(self.updel, text='Mosaic', background='white', fg='black', width=15,height=2, value=4,variable=self.floorintup,state='disabled')
        self.floorup4.place(x=325,y=432,height=36,width=98)
        self.othopup=tkinter.Label(self.updel,text='Other Options',width=10,height=2,bg='white')
        self.othopup.place(x=0,y=468,width=85)
        self.chckit1=tkinter.StringVar()
        self.chckit2=tkinter.IntVar()
        self.chckit3=tkinter.IntVar()
        self.othupch1=tkinter.Checkbutton(self.updel, text='Basement', background='white', fg='black',width=12, height=2,variable=self.chckit1,offvalue=0,onvalue=1,state='disabled')
        self.othupch1.place(x=85,y=468,height=36,width=120)
        self.othupch2=tkinter.Checkbutton(self.updel, text='Garage', background='white', fg='black',width=12, height=2,variable=self.chckit2,offvalue=0,onvalue=1,state='disabled')
        self.othupch2.place(x=170,y=468,height=36,width=120)
        self.othupch3=tkinter.Checkbutton(self.updel, text='Elevator', background='white', fg='black',width=12, height=2,variable=self.chckit3,offvalue=0,onvalue=1,state='disabled')
        self.othupch3.place(x=290,y=468,height=36,width=133)
        self.srupbtn=tkinter.Button(self.updel,text='SEARCH',background='green',command=self.srchbtn2)
        self.srupbtn.place(x=60,y=520,height=45,width=300)
        self.upbtnup=tkinter.Button(self.updel,text='UPDATE',background='blue',command=self.btnupdate)
        self.upbtnup.place(x=60,y=570,height=45,width=120)
        self.delbtnup=tkinter.Button(self.updel,text='Delete',background='red',command=self.btndlt)
        self.delbtnup.place(x=240,y=570,height=45,width=120)



    def disa(self):
        if self.radio1_2.get()==2:
            self.depositentry.config(state='disabled')
            self.mrentry.config(state='disabled')
            self.ppmentry.config(state='normal')
        elif self.radio1_2.get()==1:
            self.depositentry.config(state='normal')
            self.mrentry.config(state='normal')
            self.ppmentry.config(state='disabled')
    def zone_dis(self, x):
        distt = self.zonecombo.get()
        if distt == "1":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist1)
        elif distt == "2":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist2)
        elif distt == "3":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist3)
        elif distt == "4":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist4)
        elif distt == "5":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist5)
        elif distt == "6":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist6)
        elif distt == "7":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist7)
        elif distt == "8":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist8)
        elif distt == "9":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist9)
        elif distt == "10":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist10)
        elif distt == '11':
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist11)
        elif distt == "12":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist12)
        elif distt == "13":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist13)
        elif distt == "14":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist14)
        elif distt == "15":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist15)
        elif distt == "16":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist16)
        elif distt == "17":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist17)
        elif distt == "18":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist18)
        elif distt == "19":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist19)
        elif distt == "20":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist20)
        elif distt == "21":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist21)
        elif distt == "22":
            self.zonecombo1.config(state='active')
            self.zonecombo1.config(values=self.dist22)




    def zone_dissr(self, y):
        disttsr = self.zonecombosr.get()
        if disttsr == "1":
            self.zonecombo1sr.config(values=self.dist1sr)
        elif disttsr == "2":
            self.zonecombo1sr.config(values=self.dist2sr)
        elif disttsr == "3":
            self.zonecombo1sr.config(values=self.dist3sr)
        elif disttsr == "4":
            self.zonecombo1sr.config(values=self.dist4sr)
        elif disttsr == "5":
            self.zonecombo1sr.config(values=self.dist5sr)
        elif disttsr == "6":
            self.zonecombo1sr.config(values=self.dist6sr)
        elif disttsr == "7":
            self.zonecombo1sr.config(values=self.dist7sr)
        elif disttsr == "8":
            self.zonecombo1sr.config(values=self.dist8sr)
        elif disttsr == "9":
            self.zonecombo1sr.config(values=self.dist9sr)
        elif disttsr == "10":
            self.zonecombo1sr.config(values=self.dist10sr)
        elif disttsr == '11':
            self.zonecombo1sr.config(values=self.dist11sr)
        elif disttsr == "12":
            self.zonecombo1sr.config(values=self.dist12sr)
        elif disttsr == "13":
            self.zonecombo1sr.config(values=self.dist13sr)
        elif disttsr == "14":
            self.zonecombo1sr.config(values=self.dist14sr)
        elif disttsr == "15":
            self.zonecombo1sr.config(values=self.dist15sr)
        elif disttsr == "16":
            self.zonecombo1sr.config(values=self.dist16sr)
        elif disttsr == "17":
            self.zonecombo1sr.config(values=self.dist17sr)
        elif disttsr == "18":
            self.zonecombo1sr.config(values=self.dist18sr)
        elif disttsr == "19":
            self.zonecombo1sr.config(values=self.dist19sr)
        elif disttsr == "20":
            self.zonecombo1sr.config(values=self.dist20sr)
        elif disttsr == "21":
            self.zonecombo1sr.config(values=self.dist21sr)
        elif disttsr == "22":
            self.zonecombo1sr.config(values=self.dist22sr)

    def zone_disup(self, z):
        disttup = self.addresscomboup.get()
        if disttup == "1":
            self.addressdisup1.config(values=self.dist1up)
        elif disttup == "2":
            self.addressdisup1.config(values=self.dist2up)
        elif disttup == "3":
            self.addressdisup1.config(values=self.dist3up)
        elif disttup == "4":
            self.addressdisup1.config(values=self.dist4up)
        elif disttup == "5":
            self.addressdisup1.config(values=self.dist5up)
        elif disttup == "6":
            self.addressdisup1.config(values=self.dist6up)
        elif disttup == "7":
            self.addressdisup1.config(values=self.dist7up)
        elif disttup == "8":
            self.addressdisup1.config(values=self.dist8up)
        elif disttup == "9":
            self.addressdisup1.config(values=self.dist9up)
        elif disttup == "10":
            self.addressdisup1.config(values=self.dist10up)
        elif disttup == '11':
            self.addressdisup1.config(values=self.dist11up)
        elif disttup == "12":
            self.addressdisup1.config(values=self.dist12up)
        elif disttup == "13":
            self.addressdisup1.config(values=self.dist13up)
        elif disttup == "14":
            self.addressdisup1.config(values=self.dist14up)
        elif disttup == "15":
            self.addressdisup1.config(values=self.dist15up)
        elif disttup == "16":
            self.addressdisup1.config(values=self.dist16up)
        elif disttup == "17":
            self.addressdisup1.config(values=self.dist17up)
        elif disttup == "18":
            self.addressdisup1.config(values=self.dist18up)
        elif disttup == "19":
            self.addressdisup1.config(values=self.dist19up)
        elif disttup == "20":
            self.addressdisup1.config(values=self.dist20up)
        elif disttup == "21":
            self.addressdisup1.config(values=self.dist21up)
        elif disttup == "22":
            self.addressdisup1.config(values=self.dist22up)


    def themdark_switch(self):
        if self.themint.get()==1:
            self.darkfunc()
        else:
            self.lightfunc()

    def bgcolor(self,i,color):
        i.config(background=color)

    def darkfunc(self):
        self.config(background='#18314e')
        for i in self.winfo_children():
            self.bgcolor(i,'#32648f')



    def lightfunc(self):
        self.config(background='#e2dfd8')
        for i in self.winfo_children():
            self.bgcolor(i,'white')
            self.btn1.config(bg='white',fg='black')
            self.btn2.config(bg='white',fg='black')
            self.btn4.config(bg='white',fg='black')


    def addathu(self):
        if self.radio1_2.get()==0:
            messagebox.showerror(title='Error',message='Choice Your type')
            return
        elif self.areentry.get()=='':
            messagebox.showerror(title='Error',message='Area is Empty')
            return

        elif self.nofentry.get()=='':
            messagebox.showerror(title='Error', message='Num Of Rooms is Empty')
            return
        elif self.ppmentry.get()=='' and self.ppmentry.cget('state')!='disabled':
            messagebox.showerror(title='Error', message='Price Per Meter is Empty')
            return


        elif self.depositentry.get()=='' and self.depositentry.cget('state')!='disabled':
            messagebox.showerror(title='Error', message='Deposite is Empty')
            return
        elif self.mrentry.get()=='' and self.mrentry.cget('state')!='disabled':
            messagebox.showerror(title='Error', message='Monthly Rent is Empty')
            return
        elif self.zonecombo.get()=='' or self.zonecombo.get()=='Select Zone':
            messagebox.showerror(title='Error', message='Choice Your Zone')
            return
        elif self.zonecombo1.get()=='' or self.zonecombo1.get()=='Select District':
            messagebox.showerror(title='Error', message='Choice Your Disrtrict')
            return
        elif self.faddressentry.get()=='':
            messagebox.showerror(title='Error', message='Full Address is Empty')
            return
        elif self.floorentry.get()=='':
            messagebox.showerror(title='Error', message='Floor is Empty')
            return
        elif self.unitentry.get()=='':
            messagebox.showerror(title='Error', message='Unit is Empty')
            return
        elif self.productcombo.get()=='' or self.productcombo.get()=='Select Product Year':
            messagebox.showerror(title='Error', message='Choice Product Year')
            return
        elif self.cabinets.get()==0:
            messagebox.showerror(title='Error', message='Choice Cabinet Type')
            return
        elif self.floormatint.get()==0:
            messagebox.showerror(title='Error', message='Choice Floor Material')
            return
        Are1=self.areentry.get()
        nof1=self.nofentry.get()
        ppm1=self.ppmentry.get()
        dp1=self.depositentry.get()
        mr1=self.mrentry.get()
        zone1=self.zonecombo.get()
        distruct1=self.zonecombo1.get()
        floor1=self.floorentry.get()
        unit1=self.unitentry.get()
        pr1=self.productcombo.get()
        if  Are1.isdigit() or Are1 is float:
            pass

        else:
            messagebox.showerror(title='Error', message='There is a problem in Area Field')
            return
        if nof1.isdigit():
            pass

        else:
            messagebox.showerror(title='Error', message='There is a problem in Num Of Rooms Field')
            return
        ppm=self.ppmentry.get()
        area=self.areentry.get()
        if self.ppmentry.cget('state')=='disabled':
            pass
        elif ppm1.isdigit() or ppm1 is float:
            self.tpentry.config(state='normal')
            total=float(ppm)*int(area)
            self.tpentry.insert(tkinter.END,total)
            self.tpentry.config(state='disabled')

        else:
            messagebox.showerror(title='Error', message='There is a problem in Price Per Meter Field')
            return
        if  self.depositentry.cget('state')=='disabled':
            pass
        elif dp1.isdigit():
            pass
        else:
            messagebox.showerror(title='Error', message='There is a problem in Deposit Field')
            return
        if self.mrentry.cget('state')=='disabled':
            pass
        elif mr1.isdigit():
            pass
        else:
            messagebox.showerror(title='Error', message='There is a problem in Monthly Rent Field')
            return
        if zone1.isdigit():
            pass
        else:
            messagebox.showerror(title='Error', message='There is a problem in Zone Field')
            return
        if distruct1=='Select Distruct' or distruct1.isdigit():
            messagebox.showerror(title='Error', message='There is a problem in Distruct Field')
            return
        if floor1.isdigit() :
            pass
        else:
            messagebox.showerror(title='Error', message='There is a problem in Floor Field')
            return
        if unit1.isdigit():
            pass
        else:
            messagebox.showerror(title='Error', message='There is a problem in Unit Field')
            return
        if 1340<=int(pr1)<=1402:
            pass
        else:
            messagebox.showerror(title='Error', message='There is a problem in Product Year Field')
            return
        self.tpentry.config(state='disabled')
        self.zonecombo1.config(state='disabled')

        self.connector = sqlite3.connect('Moshaver_Information.db')
        self.cursor = self.connector.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS information(Type TEXT,Area REAL,Num_Of_Rooms INTEGER,Price_Per_Meter REAL,Total_Price REAL,Deposite REAL,Monthly_Rent REAL,Zone INTEGER,Distruct TEXT,Full_Address TEXT,Floor INTEGER,Unit INTEGER,Product_Year INTEGER,Cabinet_Type TEXT,Floor_Material TEXT,Other_Options TEXT)''')

        type=0
        if self.radio1_2.get()==1:
            type+=1
        elif self.radio1_2.get()==2:
            type+=1
        Area = self.areentry.get()
        Num_Of_Rooms = self.nofentry.get()
        Price_Per_Meter = self.ppmentry.get()
        Total_Price = self.tpentry.get()
        Deposite = self.depositentry.get()
        Monthly_Rent = self.mrentry.get()
        Zone = self.zonecombo.get()
        Distruct = self.zonecombo1.get()
        Address = self.faddressentry.get()
        Floor = self.floorentry.get()
        Unit = self.unitentry.get()
        Product_Year = self.productcombo.get()
        Cabinet_Type =''
        if self.cabinets.get()==1:
            Cabinet_Type+='None'
        elif self.cabinets.get()==2:
            Cabinet_Type+='MDF'
        elif self.cabinets.get()==3:
            Cabinet_Type+='Chipboard'
        elif self.cabinets.get()==4:
            Cabinet_Type+='High Glass'
        Floor_Material = ''
        if self.floormatint.get()==1:
            Floor_Material+='None'
        elif self.floormatint.get()==2:
            Floor_Material+='Ceramic'
        elif self.floormatint.get()==3:
            Floor_Material+='Parquet'
        elif self.floormatint.get()==4:
            Floor_Material+='Mosaic'
        Other_options = ''
        if self.it1.get()==1:
            Other_options+='Basement'
        elif self.it2.get()==1:
            Other_options+='Garage'
        elif self.it3.get()==1:
            Other_options+='Elevator'

        answer=messagebox.askyesno(title='Validation',message='Are you sure that the information is saved?')
        if answer==False:
            return
        elif answer==True:
            self.Insert = '''INSERT INTO information(type, Area, Num_Of_Rooms, Price_Per_Meter, Total_Price, 
                                Deposite, Monthly_Rent, Zone, Distruct, Full_Address, Floor, Unit, Product_Year, 
                                Cabinet_Type, Floor_Material, Other_Options) 
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''

            self.cursor.execute(self.Insert, (type, Area, Num_Of_Rooms, Price_Per_Meter, Total_Price,
                                              Deposite, Monthly_Rent, Zone, Distruct, Address, Floor,
                                              Unit, Product_Year, Cabinet_Type, Floor_Material, Other_options))

            self.connector.commit()
            self.connector.close()

            self.radio1_2.set(0)
            self.areentry.delete(0, tkinter.END)
            self.nofentry.delete(0, tkinter.END)
            self.ppmentry.delete(0, tkinter.END)
            self.tpentry.config(state='normal')
            self.tpentry.delete(0, tkinter.END)
            self.tpentry.config(state='disabled')
            self.depositentry.delete(0, tkinter.END)
            self.mrentry.delete(0, tkinter.END)
            self.zonecombo.set('Select Zone')
            self.zonecombo1.set('Select District')
            self.faddressentry.delete(0, tkinter.END)
            self.floorentry.delete(0, tkinter.END)
            self.unitentry.delete(0, tkinter.END)
            self.productcombo.set('Select Product Year')
            self.cabinets.set(0)
            self.floormatint.set(0)
            self.it1.set(0)
            self.it2.set(0)
            self.it3.set(0)





    def chtype(self):
        if self.radiosrch1.get()==1:
            self.depsren.config(state='normal')
            self.desr1.config(state='normal')
            self.mrsren.config(state='normal')
            self.mrsren1.config(state='normal')

        if self.radiosrch2int.get()==1:
            self.ppmsren.config(state='normal')
            self.ppmsren2.config(state='normal')
            self.tpsren.config(state='normal')
            self.tpsren1.config(state='normal')

        if self.radiosrch1.get()==0:
            self.depsren.config(state='disabled')
            self.desr1.config(state='disabled')
            self.mrsren1.config(state='disabled')
            self.mrsren.config(state='disabled')

        if self.radiosrch2int.get()==0:
            self.ppmsren.config(state='disabled')
            self.ppmsren2.config(state='disabled')
            self.tpsren.config(state='disabled')
            self.tpsren1.config(state='disabled')

    def btnsrch(self):
        searchval=''
        self.connector = sqlite3.connect('Moshaver_Information.db')
        self.cursor=self.connector.cursor()

        searchval = ''
        self.connector = sqlite3.connect('Moshaver_Information.db')
        self.cursor = self.connector.cursor()

        area_min = self.areentrysr.get()
        area_max = self.arenryse.get()
        if len(self.areentrysr.get())>0 and len(self.arenryse.get())>0:
            if area_max.isnumeric() or area_min.isnumeric():
                if area_min and area_max:
                    searchval = f"SELECT * FROM information WHERE Area >= {area_min} AND Area <= {area_max}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
                else:
                    messagebox.showerror(title='Error',message='Not Found')
                    return
            else:
                messagebox.showerror(title='Error',message='Enter a Number in Area Fields')
                return
        else:
            pass

        min_nof=self.nofsrent.get()
        max_nof=self.nofsrent1.get()
        if len(self.nofsrent.get())>0 and len(self.nofsrent1.get())>0:
            if max_nof.isnumeric() or max_nof.isnumeric():
                if min_nof and max_nof:
                    searchval = f"SELECT * FROM information WHERE Num_Of_Rooms >= {min_nof} AND Num_Of_Rooms <= {max_nof}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
                else:
                    messagebox.showerror(title='Error',message='Not Found')
                    return
            else:
                messagebox.showerror(title='Error',message='Enter a Number in Num Of Rooms Fields')
                return
        else:
            pass


        ppm_min=self.ppmsren.get()
        ppm_max=self.ppmsren2.get()
        if len(self.ppmsren.get())>0 and len(self.ppmsren2.get())>0:
            if ppm_min.isnumeric() and ppm_max.isnumeric():
                if ppm_min and ppm_max:
                    searchval = f"SELECT * FROM information WHERE Price_Per_Meter >= {ppm_min} AND Price_Per_Meter <= {ppm_max}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
                else:
                    messagebox.showerror(title='Error',message='Not Found')
                    return
            else:
                messagebox.showerror(title='Error',message='Enter Number in Price Per Meter')
                return
        else:
            pass

        min_tpsren=self.tpsren.get()
        max_tpsren=self.tpsren1.get()
        if len(self.tpsren.get())>0 and len(self.tpsren1.get()):
            if min_tpsren.isnumeric() and max_tpsren.isnumeric():
                if max_tpsren and min_tpsren:
                    searchval = f"SELECT * FROM information WHERE Total_Price >= {min_tpsren} AND Total_Price <= {max_tpsren}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
                else:
                    messagebox.showerror(title='Error',message='Not Found')
                    return
            else:
                messagebox.showerror(title='Error',message='Enter Number in Total Price Field')
                return
        else:
            pass

        min_dep=self.depsren.get()
        max_dep=self.desr1.get()
        if len(self.depsren.get())>0 and len(self.desr1.get())>0:
            if min_dep.isnumeric() and max_dep.isnumeric():
                if min_dep and max_dep:
                    searchval = f"SELECT * FROM information WHERE Deposite >= {min_dep} AND Deposite <= {max_dep}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
                else:
                    messagebox.showerror(title='Error',message='Not Found')
                    return
            else:
                messagebox.showerror(title='Error',message='Enter Number In Deposite Field')
                return
        else:
            pass

        min_mr=self.mrsren.get()
        max_mr=self.mrsren1.get()
        if len(self.mrsren.get())>0 and len(self.mrsren1.get())>0:
            if min_mr.isnumeric() and max_mr.isnumeric():
                if min_mr and max_mr:
                    searchval = f"SELECT * FROM information WHERE Monthly_Rent >= {min_mr} AND Monthly_Rent <= {max_mr}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
                else:
                    messagebox.showerror(title='Error',message='Not Found')
                    return
            else:
                messagebox.showerror(title='Error',message='Enter Number in Monthly Rent')
                return
        else:
            pass

        zone=self.zonecombosr.get()
        dist2=self.zonecombo1sr.get()
        if zone.isnumeric():
            if 0<=int(zone)<=23:
                if zone:
                    searchval = f"SELECT * FROM information WHERE Zone={zone}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
            else:
                messagebox.showerror(title='Error',message='Not Found')
                return
        elif zone=='Select Zone':
            pass
        elif zone!='Select Zone':
            messagebox.showerror(title='Error',message='Select Your Zone')
            return
        else:
            pass



        dis=self.zonecombo1sr.get()
        if dis in self.distsr:
            if dis:
                    searchval = f"SELECT * FROM information WHERE Distruct={dis}"
                    self.cursor.execute(searchval)
                    items = self.cursor.fetchall()
                    self.showitems = tkinter.Toplevel(self)
                    self.showitems.title('Show Items')
                    self.showitems.geometry('700x500')
                    self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                    self.show1.pack(pady=10, padx=10)
                    self.show1.delete(0, tkinter.END)
                    self.show1.insert(0, items)
                    self.connector.commit()
            # elif dis not in self.distsr:
            #     messagebox.showerror(title='Error', message='Select Your Distruct')
            #     return
            else:
                messagebox.showerror(title='Error',message='Not Found')
                return
        elif dis=='Select District':
            pass
        elif dis not in self.distsr:
            messagebox.showerror(title='Error', message='Select Your Distruct')
            return
        else:
            pass



        min_pr=self.prysr.get()
        max_pr=self.prysr1.get()
        if len(max_pr)==0 and len(min_pr)==0 and max_pr.isalpha() and min_pr.isalpha():
            pass
        if max_pr=='Select' and min_pr=='Select':
            pass
        elif max_pr.isnumeric() and 1340<=int(max_pr)<=1402 and min_pr.isnumeric() and 1340<=int(min_pr)<=1402:
            if max_pr and min_pr:
                searchval = f"SELECT * FROM information WHERE Product_Year >= {min_pr} AND Product_Year <= {max_pr}"
                self.cursor.execute(searchval)
                items = self.cursor.fetchall()
                self.showitems = tkinter.Toplevel(self)
                self.showitems.title('Show Items')
                self.showitems.geometry('700x500')
                self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                self.show1.pack(pady=10, padx=10)
                self.show1.delete(0, tkinter.END)
                self.show1.insert(0, items)
                self.connector.commit()
            else:
                messagebox.showerror(title='Error',message='Not Found')
        else:
            messagebox.showerror(title='Error',message='Enter Product Year Field')



        floor=self.floorentrysr.get()
        if floor.isnumeric():
            if floor:
                searchval = f"SELECT * FROM information WHERE Floor={floor}"
                self.cursor.execute(searchval)
                items = self.cursor.fetchall()
                self.showitems = tkinter.Toplevel(self)
                self.showitems.title('Show Items')
                self.showitems.geometry('700x500')
                self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                self.show1.pack(pady=10, padx=10)
                self.show1.delete(0, tkinter.END)
                self.show1.insert(0, items)
                self.connector.commit()
            else:
                messagebox.showerror(title='Error',message='Not Found')
        elif floor=='' or floor==' ':
            pass


        unit=self.unitentrysr.get()
        if unit.isnumeric():
            if unit:
                searchval = f"SELECT * FROM information WHERE Unit={unit}"
                self.cursor.execute(searchval)
                items = self.cursor.fetchall()
                self.showitems = tkinter.Toplevel(self)
                self.showitems.title('Show Items')
                self.showitems.geometry('700x500')
                self.show1 = tkinter.Entry(self.showitems, background='white', fg='black', width=1000, font=110000)
                self.show1.pack(pady=10, padx=10)
                self.show1.delete(0, tkinter.END)
                self.show1.insert(0, items)
                self.connector.commit()
            else:
                messagebox.showerror(title='Error',message='Not Found')
        elif unit=='' or unit==' ':
            pass







    def srchbtn2(self):
        filecode=int(self.file_codeen.get())
        file='Moshaver_Information.db'

        self.connector = sqlite3.connect('Moshaver_Information.db')
        self.cursor = self.connector.cursor()
        self.cursor.execute(f"SELECT * FROM information WHERE rowid=?",(filecode,))
        items = self.cursor.fetchall()
        print(items)

        if items:
            self.rentup.config(state='normal')
            self.buyup.config(state='normal')
            self.rentbuy.set(items)
            self.areenup.config(state='normal')
            self.areenup.delete(0, tkinter.END)
            self.areenup.insert(0,items[0][1])
            self.norrnup.config(state='normal')
            self.norrnup.delete(0,tkinter.END)
            self.norrnup.insert(0,items[0][2])
            self.ppmenup.config(state='normal')
            self.ppmenup.delete(0,tkinter.END)
            self.ppmenup.insert(0,items[0][3])
            self.tpenup.config(state='normal')
            total = int(self.areenup.get()) * int(self.ppmenup.get())
            self.tpenup.delete(0,tkinter.END)
            self.tpenup.insert(0,total)
            self.depenup.config(state='normal')
            self.depenup.delete(0,tkinter.END)
            self.depenup.insert(0,items[0][5])
            self.mrenup.config(state='normal')
            self.mrenup.delete(0,tkinter.END)
            self.mrenup.insert(0,items[0][6])
            self.addresscomboup.config(state='normal')
            self.zoneintup.set(items[0][7])
            self.addressdisup1.config(state='normal')
            self.zonestrup.set(items[0][8])
            self.faddressenup.config(state='normal')
            self.faddressenup.delete(0,tkinter.END)
            self.faddressenup.insert(0,items[0][9])
            self.floorenup.config(state='normal')
            self.floorenup.delete(0,tkinter.END)
            self.floorenup.insert(0,items[0][10])
            self.unienup.config(state='normal')
            self.unienup.delete(0,tkinter.END)
            self.unienup.insert(0,items[0][11])
            self.prcombobo.config(state='normal')
            self.printt.set(items[0][12])
            self.cabinetradioup1.config(state='normal')
            self.cabinetradioup2.config(state='normal')
            self.cabinetradioup3.config(state='normal')
            self.cabinetradioup4.config(state='normal')
            self.cabinetintup.set(items[0][13])
            self.floorup1.config(state='normal')
            self.floorup2.config(state='normal')
            self.floorup3.config(state='normal')
            self.floorup4.config(state='normal')
            self.floorintup.set(items[0][14])
            self.othupch1.config(state='normal')
            self.othupch2.config(state='normal')
            self.othupch3.config(state='normal')
            if self.chckit1.get()==1:
                self.chckit1.set(items[0])
                self.chckit2.set(items[0][15])
                # self.chckit3.set(items[0][15])
            self.file_codeen.config(state='disabled')
            self.connector.commit()
            self.connector.close()
        else:
            messagebox.showerror(title='Not Found',message='File Not Found')

    def btnupdate(self):
        #Type1=self.rentbuy.get()
        Area1=self.areenup.get()
        Num_Of_Rooms1=self.norrnup.get()
        Price_Per_Meter1=self.ppmenup.get()
        Total_Price1=self.tpenup.get()
        Deposite1=self.depenup.get()
        Monthly_Rent1=self.mrenup.get()
        Zone1=self.addresscomboup.get()
        Distruct1=self.addressdisup1.get()
        Address1=self.faddressenup.get()
        Floor1=self.floorenup.get()
        Unit1=self.unienup.get()
        Product_Year1=self.prcombobo.get()
        Cabinet_Type1=self.cabinetintup.set(0)
        Floor_Material1=self.floorintup.set(0)
        Other_options1=''
        if self.chckit1.get()=='Basement':
            Other_options1+='Basement'
        elif self.chckit1.get()=='Garage':
            Other_options1+='Garage'
        elif self.chckit1.get()=='Elevator':
            Other_options1+='Elevator'
        File_Code=self.file_codeen.get()

        ask=messagebox.askyesno(title='Ask',message='Are you sure to update?')

        if ask:
            self.connector = sqlite3.connect('Moshaver_Information.db')
            self.cursor = self.connector.cursor()
            self.cursor.execute(f"UPDATE information SET  Area=?,Num_Of_Rooms=?,Price_Per_Meter=?,"
                            f"Total_Price=?,Deposite=?,Monthly_Rent=?,Zone=?,Distruct=?,Full_Address=?,"
                            f"Floor=?,Unit=?,Product_Year=?,Cabinet_Type=?,Floor_Material=?,Other_Options=? WHERE rowid=?"
                            ,( Area1, Num_Of_Rooms1, Price_Per_Meter1, Total_Price1,
                                Deposite1, Monthly_Rent1, Zone1, Distruct1, Address1, Floor1,
                                Unit1, Product_Year1, Cabinet_Type1, Floor_Material1, Other_options1,File_Code))
            self.connector.commit()
            messagebox.showinfo(title='Show',message='Updated')
        else:
            return


    def btndlt(self):
        File_code=int(self.file_codeen.get())
        if File_code:
            ask=messagebox.askyesno(title='Ask',message='Are you sure to deleted?')
            if ask:
                self.connector=sqlite3.connect('Moshaver_Information.db')
                self.cursor=self.connector.cursor()
                self.cursor.execute(f'DELETE FROM information WHERE rowid=?',(File_code,))
                self.connector.commit()
                messagebox.showinfo(title='Show',message='Deleted')
            else:
                return
        else:
            messagebox.showerror(title='Error',message='Not Found')








def ob():
    window=moshaver()
    window.mainloop()
ob()












