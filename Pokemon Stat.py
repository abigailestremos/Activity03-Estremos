import calculator_script_1_stat as totalhp
import calculator_script_1_stat as totalatk
import calculator_script_1_stat as totaldef
import calculator_script_1_stat as totsatk
import calculator_script_1_stat as totsdef
import calculator_script_1_stat as totalspd
import calculator_script_2_ev as evatk
import calculator_script_2_ev as evdef
import calculator_script_2_ev as evsatk
import calculator_script_2_ev as evsdef
import calculator_script_2_ev as evspd

# Nature Library
nature_list = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty", "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful", "Quirky"]


print("Choose A Calculator")
print("  ")
print("1. Stat Calculator \n2. EV Calculator \n3.Exit")
choose = int(input("Select Mode: "))
match choose:
        
    case 1:
        print("1. Pokemon's HP \n2. Pokemon's Other Stat")
        statch = input(("Select the Function you will use: "))
        while statch != "1" and statch != "2":
            print("Invalid input, Try again!")
            statch = input(("Select the Function you will use: "))


        if statch == "1":
            level = int(input("\nLevel: "))
            while level > 100:
                print("Maxium value is 100")
                level = input(input("LEVEL: "))
            hp = int(input("HP: "))

            iv = int(input("IV: "))
            while iv > 31:
                print("Given value is only between 0 - 31 only")
                iv = int(input("IV: "))

            ev = int(input("EV: "))
            while ev > 255:
                print("Given value is only between 0 - 255 only")
                ev = int(input("EV: "))

            print("\n")
            print("HP =", totalhp.PokemonSTAT.tothpReturnWithParams(hp,iv,ev,level), end='\n\n')
            print("\nSystem Terminated")


        elif statch == "2":
            poke = input("\nEnter your Pokemon Name: ")
            level = int(input("Enter your Pokemon Level: "))
            # NATURE's code
            nature = input("Nature: ")
            while nature not in nature_list:
                print("\nIncorrect Input of Pokemon Nature, Please Try again!")
                nature = input("Nature: ")
            # ATK's code
            baseatk = int(input("\nATK: "))
            iv_atk = int(input("IV: "))
            while iv_atk > 31:
                print("IV value Only between 0 and 31 only.")
                iv_atk = int(input("IV: "))
            
            ev_atk = int(input("EV: "))
            while ev_atk > 255:
                print("EV value Only between 0 and 255 only.")
                ev_atk = int(input("EV: "))
            # DEF's code
            basedef = int(input("\nDEF: "))
            iv_def = int(input("IV: "))
            while iv_def > 31:
                print("IV value Only between 0 and 31 only.")
                iv_def = int(input("IV: "))
            
            ev_def = int(input("EV: "))
            while ev_def > 255:
                print("EV value Only between 0 and 255 only.")
                ev_def = int(input("EV: "))
            # SP ATK's code
            basesatk = int(input("\nSP. ATK: "))
            iv_satk = int(input("IV: "))
            while iv_satk > 31:
                print("IV value Only between 0 and 31 only.")
                iv_satk = int(input("IV: "))
            
            ev_satk = int(input("EV: "))
            while ev_satk > 255:
                print("EV value Only between 0 and 255 only.")
                ev_satk = int(input("EV: "))
            # SP DEF's code
            basesdef = int(input("\nSP. DEF: "))
            iv_sdef = int(input("IV: "))
            while iv_atk > 31:
                print("IV value Only between 0 and 31 only.")
                iv_sdef = int(input("IV: "))
            
            ev_sdef = int(input("EV: "))
            while ev_sdef > 255:
                print("EV value Only between 0 and 255 only.")
                ev_sdef = int(input("EV: "))
            # SPD's code
            basespd = int(input("\nSPD: "))
            iv_spd = int(input("IV: "))
            while iv_spd > 31:
                print("IV value Only between 0 and 31 only.")
                iv_spd = int(input("IV: "))
            
            ev_spd = int(input("EV: "))
            while ev_spd > 255:
                print("EV value Only between 0 and 255 only.")
                ev_spd = int(input("EV: "))

            
            print("\n")
            print("Pokemon", poke, "a Lvl.", level, "with", nature, "nature, Overall Stats:")
            # Total's code
            print("\nATK =", totalatk.PokemonSTAT.totatkReturnWithParams(level,baseatk,iv_atk,ev_atk,nature), end='\n\n')
            print("DEF =", totaldef.PokemonSTAT.totdefReturnWithParams(level,basedef,iv_def,ev_def,nature), end='\n\n')
            print("SP. ATK =", totsatk.PokemonSTAT.totsatkReturnWithParams(level,basesatk,iv_satk,ev_satk,nature), end='\n\n')
            print("SP. DEF =", totsdef.PokemonSTAT.totsdefReturnWithParams(level,basesdef,iv_sdef,ev_sdef,nature), end='\n\n')
            print("SPD =", totalspd.PokemonSTAT.totspdReturnWithParams(level,basespd,iv_spd,ev_spd,nature), end='\n\n')
            print("\nSystem Terminated")
    #Overall stat 
    case 2:
        print("\n")
        base = int(input("Actual STAT: "))
        stat = int(input("Increase STAT: "))
        level = int(input("Selected LEVEL: "))
        while level > 100:
            print("Maxium value is 100 only")
            level = input(input("Select LEVEL: "))
        nature = input("Nature: ")
        while nature not in nature_list:
            print("\nIncorrect Input of Pokemon Nature, Please Try again!")
            nature = input("Nature: ")
        iv = int(input("IV: "))
        ev = int(input("EV: "))
        
        print("\nEFFORT VALUES NEEDED IN:")
        print("\nATK =", evatk.PokemonEV.evatkReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("DEF =", evdef.PokemonEV.evdefReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SP ATK =", evsatk.PokemonEV.evsatkReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SP DEF =", evsdef.PokemonEV.evsdefReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("SPD =", evspd.PokemonEV.evspdReturnWithParams(base,stat,level,nature,iv,ev), end='\n\n')
        print("\nSystem Terminated")
    case 3:
        exit()    

    case default:
        print("Invalid Input, System Terminated.")

        class PokemonSTAT():
    def tothpReturnWithParams(hp,iv,ev,level):
        temphp = ((2*hp+iv+(ev/4)*level) / 100) + level + 10
        if temphp > 510:
            temphp = 510

        else:
            temphp = temphp

        tothp = "{:.2f}".format(temphp)

        return tothp

    def totatkReturnWithParams(baseatk,iv_atk,ev_atk,level,nature):
        tempatk = ((2*baseatk+iv_atk+(ev_atk/4)*level)+5)

        if nature == "Lonely" or nature == "Adamant" or nature == "Naughty" or nature == "Brave":
            tempatk = tempatk * 1.1

        elif nature == "Bold" or nature == "Modest" or nature == "Calm" or nature == "Timid":
            tempatk = tempatk * 0.9

        if tempatk > 510:
            tempatk = 510

        totatk = "{:.2f}".format(tempatk)

        return totatk

    def totdefReturnWithParams(basedef,iv_def,ev_def,level,nature):
        tempdef = ((2*basedef+iv_def+(ev_def/4)*level)+5)

        if nature == "Bold" or nature == "Impish" or nature == "Lax" or nature == "Relaxed":
            tempdef = tempdef * 1.1

        elif nature == "Lonely" or nature == "Mild" or nature == "Gentle" or nature == "Hasty":
            tempdef = tempdef * 0.9

        if tempdef > 510:
            tempdef = 510

        totdef = "{:.2f}".format(tempdef)

        return totdef

    def totsatkReturnWithParams(basesatk,iv_satk,ev_satk,level,nature):
        tempsatk = ((2*basesatk+iv_satk+(ev_satk/4)*level)+5)

        if nature == "Modest" or nature == "Mild" or nature == "Rash" or nature == "Quiet":
            tempsatk = tempsatk * 1.1    

        elif nature == "Adamant" or nature == "Impish" or nature == "Careful" or nature == "Jolly":
            tempsatk = tempsatk * 0.9

        if tempsatk > 510:
            tempsatk = 510

        totsatk = "{:.2f}".format(tempsatk)

        return totsatk

    def totsdefReturnWithParams(basesdef,iv_sdef,ev_sdef,level,nature):
        tempsdef = ((2*basesdef+iv_sdef+(ev_sdef/4)*level)+5)

        if nature == "Calm" or nature == "Gentle" or nature == "Careful" or nature == "Sassy":
            tempsdef = tempsdef * 1.1

        elif nature == "Naughty" or nature == "Lax" or nature == "Rash" or nature == "Naive":
            tempsdef = tempsdef * 0.9

        if tempsdef > 510:
            tempsdef = 510

        totsdef = "{:.2f}".format(tempsdef)

        return totsdef

    def totspdReturnWithParams(basespd,iv_spd,ev_spd,level,nature):
        tempspd = ((2*basespd+iv_spd+(ev_spd/4)*level)+5)

        if nature == "Timid" or nature == "Hasty" or nature == "Jolly" or nature == "Naive":
            tempspd = tempspd * 1.1

        elif nature == "Brave" or nature == "Relaxed" or nature == "Quiet" or nature == "Sassy":
            tempspd = tempspd * 0.9
        
        if tempspd > 510:
            tempspd = 510

        totspd = "{:.2f}".format(tempspd)

        return totspd

        class PokemonEV():
    def evatkReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Lonely" or nature == "Adamant" or nature == "Naughty" or nature == "Brave":
            tempatk = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Bold" or nature == "Modest" or nature == "Calm" or nature == "Timid":
            tempatk = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        else:
            tempatk = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        evatk = "{:.2f}".format(tempatk)

        return evatk

    def evdefReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Bold" or nature == "Impish" or nature == "Lax" or nature == "Relaxed":
            tempdef = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Lonely" or nature == "Mild" or nature == "Gentle" or nature == "Hasty":
            tempdef = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        else:
            tempdef = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        evdef = "{:.2f}".format(tempdef)

        return evdef

    def evsatkReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Modest" or nature == "Mild" or nature == "Rash" or nature == "Quiet":
            tempsatk = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4   

        elif nature == "Adamant" or nature == "Impish" or nature == "Careful" or nature == "Jolly":
            tempsatk = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        else:
            tempsatk = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        evsatk = "{:.2f}".format(tempsatk)

        return evsatk

    def evsdefReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Calm" or nature == "Gentle" or nature == "Careful" or nature == "Sassy":
            tempsdef = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Naughty" or nature == "Lax" or nature == "Rash" or nature == "Naive":
            tempsdef = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        else:
            tempsdef = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        evsdef = "{:.2f}".format(tempsdef)

        return evsdef

    def evspdReturnWithParams(base,stat,level,nature,iv,ev):
        D_temp = ( ( 2 * base * iv + ( ev / 4 ) ) * level / 100)
        if D_temp > 510:
            D = 510
        else:
            D = D_temp
        if nature == "Timid" or nature == "Hasty" or nature == "Jolly" or nature == "Naive":
            tempspd = ( ( ( ( stat / 1.1 ) - ( D ) ) * 400 / level ) / 4 ) * 4

        elif nature == "Brave" or nature == "Relaxed" or nature == "Quiet" or nature == "Sassy":
            tempspd = ( ( ( ( stat / 0.9 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        else:
            tempspd = ( ( ( ( stat / 1 ) - ( D ) ) * 400 / level ) / 4 ) * 4
        
        evspd = "{:.2f}".format(tempspd)
        
        return evspd