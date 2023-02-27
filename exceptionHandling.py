
import logging
# logging module
# -> is a means of tracking events that happen when some software runs.
# level of logging -> debug, info, warning, error, critical


 # ref : NeuralNine
# Advanced exception Handling
# ---------------------------------------------------------
# try & except block
# better to have a general exception
def tryAndException():

    num = [0,1,2,3,4,5,"Hello","world"]
    for i in range(len(num)):
        try:
            print(10/num[i])
            print(int("What"))

        except ValueError as e :
            print("valueError")

        except ZeroDivisionError as e:
            print("zeroError")

        except Exception as e:
            logging.exception(e)



def multipleException():

    test_list = [1,2,"Better",4,6,8,"Good"]

    for i in test_list:
        try:
            print(i/10)
            #raise AttributeError # it will go in exception

        except (ValueError, ZeroDivisionError) as e:
            print("Value/Zero Error")

        except AttributeError as e :
            print("AttributeError")
            

        except Exception as e :
            print("Found the error")
            break
        else:
            #No exception will run this else block
            print("No exception")

        finally:
            #execute every time even it has error or not
            print("OK")
        

#multipleException()
# ---------------------------------------------------------