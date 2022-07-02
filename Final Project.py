import  pandas as pd
import matplotlib.pyplot as plt
import csv
import winsound
dr_df=pd.read_csv("S:\\Session 2021-22\\Class 12\\IP\\Project\\dr1.csv",index_col=0)
pa_df=pd.read_csv("S:\\Session 2021-22\\Class 12\\IP\\Project\\patient1.csv",index_col=0)
bills=pd.read_csv("S:\\Session 2021-22\\Class 12\\IP\\Project\\book1.csv",index_col=0)
work=pd.read_csv("S:\\Session 2021-22\\Class 12\\IP\\Project\\workers1.csv",index_col=0)
pd.set_option('display.expand_frame_repr',False)
while True:
    print("="*40)
    print("                        HOSPITAL Management System Project")
    print("="*40)
    print("="*40)
    print("                       Main Menu")
    print("="*40)
    print()
    print("1. Data Analysis")
    print("2. Data Visualisation")
    print('3. Exit Program')
    print()
    MM=int(input("Enter you Choice :- "))
    if MM==1:
        while True:
            print("="*40)
            print("                    Data Analysis Menu")
            print("="*40)
            print()
            print("          1. Reading Doctor File")
            print("          2. Adding new Doctor Detail")
            print("          3.Reading Doctor with new Column Names")
            print("          4. Sort Doctors Details by Name ")
            print("          5.Reading Patient File")
            print("          6. Deleting age column from Patient Table")
            print("          7. Display Pataient Names")
            print("          8.Display All Bills")
            print("          9. Display total Bills")
            print("          10. Incresing Doctor Visit Charge by 200")
            print("          11. Display Records of Workers")
            print("          12. Display Highest Salary being Paid")
            print("          13.Increasing Salary by 400")
            print("          14. Back to Menu")
            DAN=int(input("Enter your choice :- "))
            if DAN==1:
                print("Reading Doctor File")
                print(dr_df)
            elif DAN==2:
                print("Adding new Doctor Detail")
                dr_df=dr_df({'D_ID':'110','D_NAME':'Dr. Geeta','D_AGE':"50",'Department':'Surgery','D_Phone':"98XXXXXX21"}, ignore_index=True)
                print(dr_df)
                dr_df.to_csv("S:\\Session 2021-22\\Class 12\\IP\\Project\\New dr.csv", index=False,header=True)
            elif DAN==3:
                print("Reading Doctor with new Column Names")
                names = ['Doctor_ID','Doctor_Name','Doctor_Age','Department','Doctor_Phone']
                dr_df1=pd.read_csv("S:\Session 2021-22\Class 12\IP\Project\dr1.csv",skiprows=1,names=names,index_col=0)
                print(dr_df1)
            elif DAN==4:
                print("Sorting Doctors Details by Name ")
                dr_df2 =dr_df.sort_values('D_NAME')
                print(dr_df2)
            elif DAN==5:
                print("Reading Patient File")
                print(pa_df)
            elif DAN==6:
                print("Deleting age column from Patient Table")
                del pa_df['P_AGE']
                print(pa_df)
            elif DAN==7:
                print("  Display Pataient Names ")
                print(pa_df['P_NAME'])
            elif DAN==8:
                print("Display All Bills ")
                print(bills)
            elif DAN==9:
                print(" Display total Bills ")
                df=bills['Dr.Visit']+bills['Medicines']+bills['Room']
                print(df)
            elif DAN==10:
                print(" Incresing Doctor Visit Charge by 200 ")
                bills['Dr.Visit']+=200
                print(bills)
            elif DAN==11:
                print("Display Records of Workers ")
                print(work)
            elif DAN==12:
                print(" Display Highest Salary being Paid ")
                print(work.SALARY.max())
            elif DAN==13:
                print("Increasing Salary by 400  ")
                work['SALARY'] +=400
                print(work)
            elif DAN==14:
                print("Going Back To Main Menu ")
                break
            else:
                 print("Enter Right Value")
    elif MM==2:
        while True:
            print("Data Visualization Menu")
            print()
            print("          1. LinePlot")
            print("          2. Bar Plot")
            print("          3.Back to the Main Menu")
            DVM=int(input("Enter your choice :- "))
            x=bills['Medicines']
            y=bills['Room']
            plt.xlabel('Medicines')
            plt.ylabel('Room')
            if DVM==1:
                print(bills)
                print("Line Plot")
                plt.plot(x,y,color='r',linewidth=5,marker='o',markerfacecolor='blue')
                plt.title('Charges of Medicines and Room records')
                plt.grid(True)
                plt.show()
            elif DVM==2:
                print(bills)
                print("Bar_Plot")
                plt.bar(x,y,width=40,facecolor='r',edgecolor='green')
                plt.xticks(fontsize=15, rotation=30)
                plt.show()
            elif DVM==3:
                print("Going back to Main Menu")
                break
            else:
                print("Enter Right Values")
    elif MM==3:
        print('Bye')
        break
    else:
        print("Enter Right Value")
    
    
    
