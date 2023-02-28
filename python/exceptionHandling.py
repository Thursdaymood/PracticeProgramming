
import logging
import datetime as dt

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

def learningLoggingOne():
    # logging module
    # -> is a means of tracking events that happen when some software runs.
    #priority low-> High
    # level of logging 
    # debug -> give the detailed info, only when diagnosing problems
    # info -> confirm every things are working as expected
    # warning -> indicate something might occur in future
    # error -> tell when some function isn't able to perform
    # critical -> indicate the program itself may be able to continue running
    # proper for a large programming

    #file with format time
    today = dt.datetime.today()
    filename = f"{today.month:02d}-{today.day:02d}-{today.year}.log"

    #create and configure logger
    logging.basicConfig(level=logging.INFO)

    #this is formatConfig, will write the message in log file
    #logging.basicConfig(filename="mesConfig.log", format="%(asctime)s %(message)s", filemode="w")

    #create an object
    logger = logging.getLogger("Thursdaymood")
    formatter = logging.Formatter("%(asctime)s: %(levelname)s - %(message)s")

    #set/create which file will keep the message log
    file_handler = logging.FileHandler(filename) #create a file.log
    #file_handler = logging.FileHandler("ConfigMes")
    file_handler.setLevel(logging.WARNING) # set this file keep the message only warning level
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.debug("Hey I am debug")
    logger.info("Hey I am Info")
    logger.warning("Hey I am warning")
    logger.warning("What again?!")
#learningLogging()
# ---------------------------------------------------------

# ref : Tech with Tim
#Logging tutorial
def learningLoggingTwo():
    print()

    #set level of configuration
    logging.basicConfig(level=logging.INFO, filename="logRecord.log", filemode="w")

    logging.debug("Debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
    print()

learningLoggingTwo()