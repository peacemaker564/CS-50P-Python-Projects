def main():
    spacecraft = {"name":"James Webb Telescope"} #Distance is in AU, astronomical units.
    spacecraft["distance"] = 0.01
    print (create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ================== Report ==================

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU


    ============================================

main()
