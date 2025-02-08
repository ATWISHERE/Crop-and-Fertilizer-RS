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
            return
            result= Crop.crop_rec()
            print(result)
        case  "2":
            import Fertilizer
            return
            result=Fertilizer.fert_rec()
            print(result)
        case "3":
            import Crop
            import Fertilizer
            return
            result1= Crop.crop_rec()
            print(result1)
            result2=Fertilizer.fert_rec()
            print(result2)
        case _:
            print("Invalid choice. Please select 1, 2, or 3.")
    print("\nThank you for using the CROP RECOMMENDATION SYSTEM BY Abdul Tarique Warsi. Goodbye!\n  ")

if __name__ == "__main__":
    main()
         
       



    

    

