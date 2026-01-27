req_fuel = float(input("Enter no. of litres fuel required to fill the tank:"))
dist=float(input("Enter distance traveled:"))

def fuel_consumed(fuel, distance):
    if fuel < 1:
        print(f"{fuel:.2f} is an Invalid Input")
    elif distance<1:
        print(f"{distance:.2f} is an Invalid Input")
    else:
        lit_dist=(fuel/distance)*100
        print(f"Liters/100KM: {lit_dist:.2f}")
        gall=fuel*0.2642
        mile=dist*0.6214
        mil_gal=mile/gall
        print(f"miles/gallons: {mil_gal:.2f}")


call=fuel_consumed(req_fuel,dist)