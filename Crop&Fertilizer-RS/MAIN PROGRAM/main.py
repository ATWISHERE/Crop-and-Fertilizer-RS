def main():
    print("*****************************************************")
    print("        WELCOME TO CROP RECOMMENDATION SYSTEM        ")
    print("*****************************************************")
    # Take input for the recommendation type
    print("What recommendation do you want?")
    print("1. Crop Recommendation")
    print("2. Fertilizer Recommendation")
    print("3. Both")
    choice = input("Enter your choice (1/2/3): ")

    match choice:
        case "1":
            import Crop
            N=float(input("Enter Nitrogen N: "))
            P=float(input("Enter Phosphorous P: "))
            K=float(input("Enter Potassium K: "))
            temp=float(input("Enter Temperature T(°C): "))
            hum=float(input("Enter Humidity H (%): "))
            ph=float(input("Enter pH Value of Soil ph: "))
            rain=float(input("Enter rainfall (mm): "))
            
            result= Crop.crop_rec(N,P,K,temp,hum,ph,rain)
            print(result)
        case  "2":
            import Fertilizer
            temp=float(input("Enter Temperature T(°C): "))
            hum=float(input("Enter Humidity H (%): "))
            Mois = float(input("Enter Moisture M: "))
            Stype = float(input("Enter Soil Type \n1.Sandy\n2.Loamy\n3.Black\n4.Red\n5.Clayey\nST: "))
            Ctype = float(input("Enter Crop Type\n1.Maize\n2.Sugarcane\n3.Cotton\n4.Tobacco\n5.Paddy\n6.Barley\n7.Wheat\n8.MilletsOil seeds\n9.Pulses\n10.Ground Nuts' CT: "))
            N = float(input("Enter Nitrogen N: "))
            K = float(input("Enter Potassium K: "))
            P = float(input("Enter Phosphorous P: "))
           
            result=Fertilizer.fert_rec(temp,hum,Mois,Stype,Ctype,N,K,P)
            print(result)
        case "3":
            import Crop
            N=float(input("Enter Nitrogen N: "))
            P=float(input("Enter Phosphorous P: "))
            K=float(input("Enter Potassium K: "))
            temp=float(input("Enter Temperature T(°C): "))
            hum=float(input("Enter Humidity H (%): "))
            ph=float(input("Enter pH Value of Soil ph: "))
            rain=float(input("Enter rainfall (mm): "))
            
            result= Crop.crop_rec(N,P,K,temp,hum,ph,rain)
            print(result)
        
            import Fertilizer
            temp=float(input("Enter Temperature T(°C): "))
            hum=float(input("Enter Humidity H (%): "))
            Mois = float(input("Enter Moisture M: "))
            Stype = float(input("Enter Soil Type \n1.Sandy\n2.Loamy\n3.Black\n4.Red\n5.Clayey\nST: "))
            Ctype = float(input("Enter Crop Type\n1.Maize\n2.Sugarcane\n3.Cotton\n4.Tobacco\n5.Paddy\n6.Barley\n7.Wheat\n8.MilletsOil seeds\n9.Pulses\n10.Ground Nuts' CT: "))
            N = float(input("Enter Nitrogen N: "))
            K = float(input("Enter Potassium K: "))
            P = float(input("Enter Phosphorous P: "))
           
            result=Fertilizer.fert_rec(temp,hum,Mois,Stype,Ctype,N,K,P)
            print(result)
        case _:
            print("Invalid choice. Please select 1, 2, or 3.")
    print("\nThank you for using the CROP RECOMMENDATION SYSTEM BY Abdul Tarique Warsi. Goodbye!\n  ")

if __name__ == "__main__":
    main()
         
       



    

    

