"""
Created by Damilola Gbenle
"""


import tkinter as tk
import shelve  
import numpy as np
from tkinter import messagebox 

#displays first page and makes it global so it can be used anywhere in the code
global root
root = tk.Tk()
#size for the first page 
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

#display text asking user for name
label1 = tk.Label(root, text='Enter your Name')
label1.config(font=('helvetica', 18))
canvas1.create_window(200, 40, window=label1)

#entry box for the first page 
entry1 = tk.Entry (root) 
canvas1.create_window(200, 100, window=entry1,width = 200, height = 30,)
#function that collects user name using the enter key on your keyboard
def user_name1(self):
    user_name()
#function that collects user name using the enter button on display screen
def user_name ():  
    #x1 = username the user enters and i made it global
    global x1
    x1 = entry1.get()
    
    # Our time structure [min, sec, centsec]
    global timer, pattern ,hard, hard_check,text1,pos1,rey
    pos1 = 0
    rey= 0
    hard = [14,13,12,11,10,9,8,7,6,5,4,3,2,1,1,1,1]
    hard_check = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
    timer = [0, hard[pos1], 99]
    text1 = '00:'+str(hard[pos1])+':99'
    
    # The format is padding all the 
    pattern = '{0:02d}:{1:02d}:{2:02d}' 
    
    high = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600]
    #database
    #making the highscore value global so it can displayed if user attained high score
    global high_score
    #creating a database on the system to save highscores of previous users
    r = shelve.open('test.db')
    #checks if the database is empty
    try:
        #if the database isn't empty pick the value and store it as the new high score
        high_score = r['key']
    except:
        #if not create the highscore variable to be 0
        high_score = 0
     #close the database   
    r.close()
    #making value, score and pos(for level) global 
    global value, score, pos
    value = 0
    score = 0
    pos = 0
    
    #this function is incase the user says no and doesnt want to play it closes all pages 
    def no ():
        global x1
        root2= tk.Tk()
        #new page
        dest = tk.Canvas(root2,  width = 400, height = 300,)
        dest.pack()
        
        destlabel = tk.Label(dest,text= 'Thank you ' + x1 +" :(",font=('helvetica', 20),fg='red')
        dest.create_window(200, 40, window=destlabel)
        dest.update()
        dest.after(4000, dest.destroy())
        root2.after(2, root2.destroy())
        root1.after(2, root1.destroy())
    #this function is after the user plays first round and deosn't want to play anymore it closes all pages
    def no2 ():
        global x1,root,root1,root3,root4
        root5= tk.Tk()
        #new page
        dest = tk.Canvas(root5,  width = 400, height = 300,)
        dest.pack()
        
        destlabel = tk.Label(dest,text= 'Thank you ' + x1 +" :(",font=('helvetica', 20),fg='red')
        dest.create_window(200, 40, window=destlabel)
        dest.update()
        dest.after(4000, dest.destroy())
        root5.after(2,root5.destroy())
        root4.after(2, root4.destroy())
     #yes1 is a function that calls the yes function to allow the user play again   
    def yes1():
        global root3,root4
        root4.after(500,root4.destroy())
        yes()
        
    def yes2 ():
        root1.after(500, root1.destroy())
        yes()
    #actual yes function that runs the game
    def yes():
        global value, score, pos, timer
        
        value = 0
        score = 0
        pos = 0
        global state
        state = False
        global root3,root1,k1,k2
        root3= tk.Tk()
        
        ##############################################################
        def reset():
            global timer,hard,pos1
            timer = [0, hard[pos1], 99]
            timeText.configure(text=text1)
        def update_timeText():
            global state
            if state:
                global timer,timeText
                # Every time this function is called, 
                # we will increment 1 centisecond (1/100 of a second)
                timer[2] -= 1

                # Every 100 centisecond is equal to 1 second
                if timer[2] == 0:
                    timer[2] = 99
                    timer[1] -= 1
                if timer[1]<=-1:
                    state=False
                    reset()
                    update_val_text()
                    popup_bonus5()
                    
                    timer[1] = 14
                # We create our time string here
                timeString = pattern.format(timer[0], timer[1], timer[2])
                # Update the timeText Label box with the current time
                if state:
                    timeText.configure(text=timeString)
                # Call the update_timeText() function after 1 centisecond
            yess.after(10, update_timeText)
        def update_btn_text():
            global k1,k2
            if val1["text"] == str(k1) or val2["text"] == str(k2):
                val = np.random.randint(low = -4, high = 7, size = 2)

                k1 = str(val[0])
                k2 = str(val[1])
                val1.configure(text=k1)
                val2.configure(text=k2)
        def update_val_text():
            global value
            yesslabel1.configure(text="Value: "+str(value))
            
        
            
        def popup_bonus():
            global pos,hard, hard_check,text1,pos1,rey
            levelval.configure(text="Level "+str(pos+1))
                        
            if pos == hard_check[rey]:
                pos1+=1
                rey+=1
            
        def clear_text():
            entry2.delete(0,"end")
            
        def popup_bonus2():
            global x1, score, high_score,root4,root1,timer,state,rey
            
            root4= tk.Tk()
            #new page
            newp = tk.Canvas(root4,  width = 400, height = 300)
            newp.pack()
            
            y = tk.Label(newp,text= "Game Over :(" ,font=('helvetica', 15),fg='red')
            newp.create_window(200, 40, window=y)
            
            l = tk.Label(newp, text="Your score is " + str(score),font=('helvetica', 15),fg='blue')
            newp.create_window(200, 80, window=l)
            
            
            ll = tk.Label(newp, text="Thank you "+ x1,font=('helvetica', 15))
            newp.create_window(200, 120, window=ll)
            
            if score > high_score:
                high_score = score
                messagebox.showinfo("Congrats","Congrats!!! \n you have the highest Score")
                s = shelve.open('test.db')
                s['key'] = high_score
                s.close()

            n1 = tk.Label(newp, text='Do you wish to play again '+ x1+"?")
            n1.config(font=('helvetica', 14))
            newp.create_window(200, 160, window=n1)

            bt11 = tk.Button(newp, text="Yes",command=yes1,bg='blue', fg='white', font=('helvetica', 13, 'bold'))
            newp.create_window(155, 200, window=bt11,width = 40, height = 30)

            bt12 = tk.Button(newp, text="No",command=no2,bg='red', fg='white', font=('helvetica', 13, 'bold'))
            newp.create_window(205, 200, window=bt12,width = 40, height = 30)
            
            quit = tk.Button(newp, text="QUIT", fg="red",command=root4.destroy)
            newp.create_window(200, 280, window=quit,width = 90, height = 30)
            
            root3.after(3000,root3.destroy)
            
        def popup_bonus5():
            global x1, score, high_score,root4,root1,timer,state,rey
            
            root4= tk.Tk()
            #new page
            newp = tk.Canvas(root4,  width = 400, height = 300)
            newp.pack()
            
            y = tk.Label(newp,text= "You ran out of time." ,font=('helvetica', 15),fg='red')
            newp.create_window(200, 40, window=y)
            y = tk.Label(newp,text= "Game Over :(" ,font=('helvetica', 15),fg='red')
            newp.create_window(200, 70, window=y)
            
            l = tk.Label(newp, text="Your score is " + str(score),font=('helvetica', 15),fg='blue')
            newp.create_window(200, 100, window=l)
            
            
            ll = tk.Label(newp, text="Thank you "+ x1,font=('helvetica', 15))
            newp.create_window(200, 130, window=ll)
            
            if score > high_score:
                high_score = score
                messagebox.showinfo("Congrats","Congrats!!! \n you have the highest Score")
                s = shelve.open('test.db')
                s['key'] = high_score
                s.close()

            n1 = tk.Label(newp, text='Do you wish to play again '+ x1+"?")
            n1.config(font=('helvetica', 14))
            newp.create_window(200, 170, window=n1)

            bt11 = tk.Button(newp, text="Yes",command=yes1,bg='blue', fg='white', font=('helvetica', 13, 'bold'))
            newp.create_window(155, 210, window=bt11,width = 40, height = 30)

            bt12 = tk.Button(newp, text="No",command=no2,bg='red', fg='white', font=('helvetica', 13, 'bold'))
            newp.create_window(205, 210, window=bt12,width = 40, height = 30)
            
            quit = tk.Button(newp, text="QUIT", fg="red",command=root4.destroy)
            newp.create_window(200, 280, window=quit,width = 90, height = 30)
            
            root3.after(3000,root3.destroy)
        
        def popup_bonus6():
            global x1, score, high_score,root4,root1,timer,state,rey
            
            root4= tk.Tk()
            #new page
            newp = tk.Canvas(root4,  width = 400, height = 300)
            newp.pack()
            
            y = tk.Label(newp,text= "Congratulations!!!" ,font=('helvetica', 15),fg='red')
            newp.create_window(200, 40, window=y)
            y = tk.Label(newp,text= "You have completed the game" ,font=('helvetica', 15),fg='red')
            newp.create_window(200, 70, window=y)
            
            l = tk.Label(newp, text="Your score is " + str(score),font=('helvetica', 15),fg='blue')
            newp.create_window(200, 100, window=l)
            
            
            ll = tk.Label(newp, text="Thank you "+ x1,font=('helvetica', 15))
            newp.create_window(200, 130, window=ll)
            
            if score > high_score:
                high_score = score
                messagebox.showinfo("Congrats","Congrats!!! \n you have the highest Score")
                s = shelve.open('test.db')
                s['key'] = high_score
                s.close()

            n1 = tk.Label(newp, text='Do you wish to play again '+ x1+"?")
            n1.config(font=('helvetica', 14))
            newp.create_window(200, 170, window=n1)

            bt11 = tk.Button(newp, text="Yes",command=yes1,bg='blue', fg='white', font=('helvetica', 13, 'bold'))
            newp.create_window(155, 210, window=bt11,width = 40, height = 30)

            bt12 = tk.Button(newp, text="No",command=no2,bg='red', fg='white', font=('helvetica', 13, 'bold'))
            newp.create_window(205, 210, window=bt12,width = 40, height = 30)
            
            quit = tk.Button(newp, text="QUIT", fg="red",command=root4.destroy)
            newp.create_window(200, 280, window=quit,width = 90, height = 30)
            
            root3.after(3000,root3.destroy)
            
        def popup_bonus3():
            messagebox.showerror("Error", "You have entered an invalid number") 
            
        def popup_bonus4():
            messagebox.showwarning(title="Warning", message="You have entered a wrong number")
            
        def check1(self):
            check()
            
        def check ():
            global value, score, pos, val,k1,k2,timer,state
            state = True
            k = entry2.get()
            clear_text()
            try:
                k = int(k)
                if k == int(k1) or k == int(k2):
                    value+=k
                    if value < 11 and value> -10:
                        score+=5
                        update_btn_text()
                        update_val_text()
                        reset()
                        if score == high[pos]:
                            pos+=1
                            popup_bonus()
                        if score == high[-1]:
                            update_val_text()
                            state = False
                            reset()
                            popup_bonus6()
                    else:
                        update_val_text()
                        state = False
                        reset()
                        popup_bonus2()   
                else:
                    popup_bonus4()
            except:
                popup_bonus3()
        #####################################################################################
        #new page
        yess = tk.Canvas(root3,  width = 400, height = 400)
        yess.pack()
        levelval = tk.Label(yess,text="Level "+str(pos+1),font=('helvetica',25,"bold"),fg='red')
        yess.create_window(200, 25, window=levelval)
        
        #displaying the instruction on the third page on how to play the game
        yesslabel = tk.Label(yess,text="The goal of this game is to make sure the numbers you add",font=('helvetica',10))
        yess.create_window(200, 50, window=yesslabel)
        
        yesslabel=tk.Label(yess,text="does not exceed 10 or go lower than -10. Once you exceed 10 ",font=('helvetica',10))
        yess.create_window(200, 70, window=yesslabel)
        
        yesslabel=tk.Label(yess,text="or go lower Game Over. PS:Time reduces as level increases",font=('helvetica',10))
        yess.create_window(200, 90, window=yesslabel)
        
        global timeText
        timeText = tk.Label(yess, text= "00:00:00", font=("Helvetica", 20,'bold'),fg='grey1')
        yess.create_window(200, 125, window=timeText)
         
           
        #display the value after it has added it everytime
        yesslabel1 = tk.Label(yess,text= "Value: "+ str(value),font=('helvetica', 15),fg='red')
        yess.create_window(200, 160, window=yesslabel1)
        
        #making val(random numbe generated with numpy), k1(1st value in val), k2(2nd value in val) all global
        global val,k1,k2
        #val saves the random numbers generated with numpy
        val = np.random.randint(low = -4, high = 7, size = 2)
        k1 = str(val[0])
        k2 = str(val[1])
      
        #displays the first digit as a button on third page 
        val1 = tk.Button(yess, text= k1, fg="blue",command=None,font=('helvetica', 15, 'bold'))
        yess.create_window(170, 205, window=val1,width = 50, height = 50)
         
        #displays the second digit as a button on third page
        val2 = tk.Button(yess, text=k2, fg="blue",command=None,font=('helvetica', 15, 'bold')) 
        yess.create_window(230, 205, window=val2,width = 50, height = 50)

        #entry box to collect user input of the choice of number they entered
        entry2 = tk.Entry(yess) 
        yess.create_window(200, 255, window=entry2,width = 200, height = 30,)
        
        #enter button to send user input to compute the data
        buttn1 = tk.Button(yess,text='Enter', command=check, bg='blue', fg='white', font=('helvetica', 13, 'bold'))
        yess.create_window(200, 295, window=buttn1)
        #binding enter key on keyboard to do the same as enter button on screen
        entry2.bind('<Return>', check1)
        yess.after(100, update_timeText)
            

        #the quit button on every page so user can quit anytime     
        quit = tk.Button(yess, text="QUIT", fg="red",command=root3.destroy)
        yess.create_window(200, 380, window=quit,width = 90, height = 30)
        root3.mainloop()
    #checking if x1 had a valid entry   
    if x1:
        #make the first letter capital
        x1 = x1.capitalize()
        #create a second page
        global root1
        root1= tk.Tk()
        #destroy the first page after 500 and enter the next page
        root.after(500,root.destroy())
        #new page
        newpage = tk.Canvas(root1,  width = 400, height = 300)
        newpage.pack()
        #label for the second page
        newlabel = tk.Label(newpage,text= 'Welcome ' + x1 ,font=('helvetica', 20),bg='spring green',fg='white')
        newpage.create_window(200, 40, window=newlabel)
        #lable asking a question
        newlabel1 = tk.Label(newpage, text='Do you wish to play a game '+ x1+"?")
        newlabel1.config(font=('helvetica', 14))
        newpage.create_window(200, 120, window=newlabel1)
        
        #button that says yes on the second page
        bt1 = tk.Button(newpage, text="Yes",command=yes2,bg='blue', fg='white', font=('helvetica', 13, 'bold'))
        newpage.create_window(155, 160, window=bt1,width = 40, height = 30)
        #button that says no on the second page
        bt2 = tk.Button(newpage, text="No",command=no,bg='red', fg='white', font=('helvetica', 13, 'bold'))
        newpage.create_window(205, 160, window=bt2,width = 40, height = 30)
        
        #the quit button on every page so user can quit anytime 
        quit = tk.Button(newpage, text="QUIT", fg="red",command=root1.destroy)
        newpage.create_window(200, 280, window=quit,width = 90, height = 30)
        root1.mainloop()
    #else statement that displays error message if user didnt enter any value 
    else:
        label3 = tk.Label(root, text= 'Invalid Entry',font=('helvetica', 12),bg='red')
        canvas1.create_window(200, 230, window=label3)
    

# enter button on the first page asking for user name    
button1 = tk.Button(canvas1, text='Enter', command=user_name, bg='blue', fg='white', font=('helvetica', 13, 'bold'))
canvas1.create_window(200, 170, window=button1)
#binding enter key on keyboard to do the same as enter button on screen
entry1.bind('<Return>', user_name1)


#the quit button on every page so user can quit anytime 
quit = tk.Button(root, text="QUIT", fg="red",command=root.destroy)
canvas1.create_window(200, 280, window=quit,width = 90, height = 30)

root.mainloop()