def main():
    spacecraft = {"Name":"James Webb Telescope"} #Distance is in AU, astronomical units.
    spacecraft["Distance"] = 0.01
    create_report(spacecraft)

def create_report(spacecraft):
    print (spacecraft["Name"], spacecraft["Distance"], "AU" , sep = " : ")

main()
