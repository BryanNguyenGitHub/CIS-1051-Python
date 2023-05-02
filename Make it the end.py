nameofMC = input("Hello there, What is your name? ").capitalize()
def actionpart():
    print("Hello", nameofMC, "Welcome to Make It to The End!") 
    

    print("You,", nameofMC, "are part of a special forces called United Secretes and  were assigned to go on a classified mission to the jungle with your team.")
    print("The year is 2023 and you wake up lose in a dense jungle after being knocked unconcious by an impact from a plane crash.")
    print("The plane has collided with something, and it is your objective to make it out alive!.")
    print("However, the plane seems to be mostly intact, but you have no idea what has been damaged, or of the whereabout of your crewmates.")
    print("You want off the jungle and trying to figure what your plan is.")
    print("It appears there is a radio but it is broken.")
    print("There are body of water near the jungle and another solution you have found is buidling a raft to get into sea and escape the jungle.")
    print("You,", nameofMC, "must navigate through the jungle, avoiding dangerous animals and hostile tribes while finding1 material and a way to escape the jungle to return home.")
    action1 = {1:"Scavage the jungle to find materials to fix the radio", 2:"Decide to build a raft to escape the jungle."}
    print(action1)
    choice = input("Action 1 or 2? ")  
    
    while True:
        if choice == '1': 
            print("You have decided to go out in the jungle and find materials to fix the radio")
            print("The jungle is peac  e and quiet, but it is raining really heavily. There are tons of dangerous animals and species but you want to avoid them as possible.")
            print("There are dangerous species everywhere you go but you continue your journy trying to find materials")
            print("While continue your walk, it appears you see some booby traps ahead. The booby trap is a hole that is covered in spikes and posinous strings.")
            print("You are looking to find ways to dodge the trap, and you see planks you can use to walk over, however, you don't know if will hold your weight.")
            print("You see another option either jump over the hole and see if you can make it to the other side. However, the hole is wide enough if you make a mistake.")
            print("You must decide very CAREFULLY. Will you choose to use the plank as a bridge, or risk your life to jump over the whole without falling?")
            action2 = {3:"Use the plank", 4:"Jump over the hole without falling into it."}
            print(action2)
            choice = input("Action 3 or 4? ")
            if choice == "3":
                print("You decided to use the plank as a brdige to walk over the hole.")
                print("You are walking over the plank, but there is an issue.")
                print("The plank was not stable enough and started shaking and sliding due to the mud and wet grass")
                print("The plank started to break and you fell down the hole")
                print("However, you quickly grabbed onto the edge of the hole")
                print("Unfortunately, your grip was not strong enough to so the wet mud and grass made it difficult for you to hold longer for rescue. You have died...")
                return False
               
            elif choice == "4": 
                print("You decided to make a risky jump over the hole.")
                print("")


                print("You make your way to the main airlock which leads to the outside of the spacecraft. This airlock contains spacesuits normally used for spacewalks.The crew quarters are one of the parts of the ship that has artificial gravity.")
                print("This makes spacesuits unusable there, but since the power is out you can freely travel. You put on the space suit and head to the crew quarters.")
                print("Now as you walk into the airlock of the crew quarters you can't see much other than the light provided by the door behind you.")
                print("You turn on the external light of your spacesuit, and continue through the next door.")
                print("Once you reach the otherside your scanners show that the quarters have no oxygen and the pressure is lower than the rest of the ship.")
                print("You are now truly alone in space. The decisions to save the mission solely rely on you.You can continue to search the quarters, or return back to the main floor and contact HQ.")
                action3 = {3: "Search the quarters", 4: "Return to the main floor to contact HQ"}
                print(action3)
                choice = input("Action 3 or 4? ")
                if choice == "3":
          
                    print(action4)
                    choice = input("Action 3 or 4? ")
                    if choice == "3":


                        return False
                    
                    elif choice == "4":
                        print("You exit the airlock the same way you came in and make your way to the flight deck to contact HQ.")
                        print("Upon reaching the flight deck the HQ appears to be unreachable as the communications for your ship seem to have been destroyed.")
                        print("Before entering the quarters you had the option to contact HQ meaning it was destroyed long after what impacted the ship. You now have two options.")
                        action5 = {3: "Attempt to restore communications" , 4: "Figure out what impacted with the ship"}
                        print(action5)
                        choice = input("Action 3 or 4? ")
                        if choice == "3":

                            action6 = {3: 'Head back inside to remove that area of the ship', 4: 'Investigate the object closer'}
                            print(action6)
                            choice = input("Action 3 or 4? ")
                            if choice == "3":
                                print("You move back toward the airlock where you came from.")
                                print("The object on top must have been carrying whatever it was that killed your crewmates.")
                                print("The idea is that if you remove the crew quarters it will bring the object with it.")
                                print("The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates.")
                                print("You open the airlock from the outside and enter the ship.")
                                print("After closing the door you prepare to reenter the space ship again.")
                                print("You know that you are alone.")
                                print("Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.")
                                print("Making your way toward the quarters you can hear something on the inside moving around.")
                                print("It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.")
                                print("As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.\n")
                                action7 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                                print(action7)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                    print("You face the airlock and begin opening the door.")
                                    print("The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                    print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                    print("The door opens into a dark room with no oxygen as you had left it previously.")
                                    print("You step inside looking around for Alex who was crying for help.")
                                    print("There is no one immediately near the door as you would have expected from the cries.")
                                    print("Just as fear, and doubt enter something cries out above you and drops from the ceiling.You have failed your mission.")
                                    return False
                                elif choice == "4":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                    print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.")
                                    print("The decision has already been made, and you pull the lever.")
                                    print("The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                    print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                    print("The threat that was on the ship threatening your life is now gone.")
                                    print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.\n")                    
                                    action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                    print(action10)
                                    choice = input("Action 3 or 4? ")
                                    if choice == "3":
                                        print("You decide that it is best you finish the mission you were sent to accomplish.")
                                        print("The ship is already on path to Mars there is nothing for you to do.")
                                        print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                        print("All you can do now is let the days go by as your ship approaches Mars.")
                                        print("The primary floors of the ship contain enough food and water for a one way trip.")
                                        print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                        print("You have failed your mission, but you did make it to Mars.")
                                        return False
                                    elif choice == "4":
                                        print("You decide that it is best to recourse the ship and head back to Earth.")
                                        print("The complications lie in the fact that you have no contact with the ground.")
                                        print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                        print("All there is to do now is wait out the days back to Earth.")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                        print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                        print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                        return False
                            elif choice == "4":
                                print("You decide to investigate the object that landed on your ship.")
                                print("You make your way across the top of the ship toward the large reflective object.")
                                print("There are no windows doors, or anything that look familiar to your ship.")
                                print("You get up next to the object and it seems like a mirror you can clearly see yourself in the reflection of the object.")
                                print("You begin to search aroundthe side to see if you can find an entry point.")
                                print("There is a hole in the top of the ship leading to the crew quarters.")
                                print("Nearest to this hole look almost like a loading dock of a large cargo plane.You can climb inside and further investigate this object or Head back inside the ship.\n")
                                action8 ={3: "Climb inside to investigate the object further", 4: "Head back inside the ship"}
                                print(action8)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("You climb up the long loading dock being careful not to lose your footing on its reflective surface.")
                                    print("On your way up the tassle attached to you is not long enough to contiunue in.")
                                    print("At this point you have no choice but to release yourself from the tether of your ship. You untether yourself and enter the object.")
                                    print("On the inside the top of the object is just a long flat white light accompanied by the same reflective floor as before.")
                                    print("You walk deeper into the object to see what appears to be an elevated ring with nothing but two large black rings in front of it.")
                                    print("Behind you you hear the sound of the entrance lifting to close the object.You rush back toward the entrance, but are much too late as the object seals shut")
                                    print("Along with the only known exit being shut the ship has no pressurized to normal gravity.")
                                    print("The spacesuit now is heavy and you cannot move unless you take it off. With no other option you begin to remove the suit starting with the helmet.")
                                    print("The air around you appears to be breathable, but as time goes on your eyes begin to feel heavy.The suit is off but your body feels heavier than before.")
                                    print("The air must be knocking you out once again. You fall to the ground. You have failed your mission.\n")
                                    return False
                                elif choice == "4":
                                    print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates.")
                                    print("The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongings you brought onto the ship with you will be lost in space along with the remainof your crewmates.You open the airlock from the outside and enter the ship.After closing the door you prepare to reenter the space ship again. You know that you are alone.Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.Making your way toward the quarters you can hear something on the inside moving around.It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!' Knowing everything you saw on the inside of the crew quarters you now have to make a decision.")
                                    action9 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                                    print(action9)
                                    choice = input("Action 3 or 4? ")
                                    if choice == "3":
                                        print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                        print("You face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                        print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                        print("The door opens into a dark room with no oxygen as you had left it previously.")
                                        print("You step inside looking around for Alex who was crying for help.There is no one immediately near the door as you would have expected from the cries.")
                                        print("Just as fear, and doubt enter something cries out above you and drops from the ceiling. You have failed your mission.")
                                        return False
                                    elif choice == "4":
                                        print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                        print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.The decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                        print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                        print("The threat that was on the ship threatening your life is now gone.")
                                        print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive. All there is to do now is wait out the days back to Earth.")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                        print("This means that all you have to do is wait for the ship to take you home.")
                                        print("This was the only true way to survive.Your comrades died in vein, but your objective is complete.You have passed the mission.")
                                        action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                        print(action10)
                                        choice = input("Action 3 or 4? ")
                                        if choice == "3":
                                            print("You decide that it is best you finish the mission you were sent to accomplish.")
                                            print("The ship is already on path to Mars there is nothing for you to do.")
                                            print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                            print("All you can do now is let the days go by as your ship approaches Mars.")
                                            print("The primary floors of the ship contain enough food and water for a one way trip.")
                                            print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                            print("You have failed your mission, but you did make it to Mars.")
                                            return False
                                        elif choice == "4":
                                            print("You decide that it is best to recourse the ship and head back to Earth.")
                                            print("The complications lie in the fact that you have no contact with the ground.")
                                            print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                            print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                            print("All there is to do now is wait out the days back to Earth.")
                                            print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                            print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                            print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                            return False
                        elif choice == "4":
                            print("You make your way back to the main airlock where you initially got you spacesuit.")
                            print("You open the airlock, close the door behind you and begin to prepare for your spacewalk.")
                            print("There are small clips that you must fasten to the ship to make sure you are not taken too far from the ship.")
                            print("You open the door and make your way into space latching on to the bar above the door you float down and fasten the door behind you.")
                            print("Climbing above the airlock you can now see the top of the ship.")
                            print("The ship is build into layers stacked onto one another with various rooms branching out.")
                            print("The flight deck has 3 large solar sails attatched to it giving the ship the ability to move through space.")
                            print("As long as this stays intact the ship can move through space meaning the rest of the areas are expendable. You make your way past the solar sails to see the impact.")
                            print("There is a diamond shaped object resting on the top of the ship. The object is a silverish color but it appears to almost be fully reflective.")
                            print("While inspecting the object you can also clearly see that the communcations points outside of the research room are completeley destroyed from the impact of the object.")
                            print("This thing must have passed through the cargo bay and into the back of the ship directly hitting the crew quarters.")
                            print("Being that the object is so far back you could drop it into space along with the crew quarters.You also can search the object to find out what it is.\n")
                            action6 = {3: 'Head back inside to remove that area of the ship', 4: 'Investigate the object closer'}
                            print(action6)
                            choice = input("Action 3 or 4?")
                            if choice == "3":
                                print("You move back toward the airlock where you came from.")
                                print("The object on top must have been carrying whatever it was that killed your crewmates.")
                                print("The idea is that if you remove the crew quarters it will bring the object with it.")
                                print("The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates.")
                                print("You open the airlock from the outside and enter the ship.")
                                print("After closing the door you prepare to reenter the space ship again.")
                                print("You know that you are alone.")
                                print("Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.")
                                print("Making your way toward the quarters you can hear something on the inside moving around.")
                                print("It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.")
                                print("As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.\n")
                                action7 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                                print(action7)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                    print("You face the airlock and begin opening the door.")
                                    print("The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                    print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                    print("The door opens into a dark room with no oxygen as you had left it previously.")
                                    print("You step inside looking around for Alex who was crying for help.")
                                    print("There is no one immediately near the door as you would have expected from the cries.")
                                    print("Just as fear, and doubt enter something cries out above you and drops from the ceiling.You have failed your mission.")
                                    return False
                                elif choice == "4":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                    print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.")
                                    print("The decision has already been made, and you pull the lever.")
                                    print("The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                    print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                    print("The threat that was on the ship threatening your life is now gone.")
                                    print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.\n")                    
                                    action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                    print(action10)
                                    choice = input("Action 3 or 4? ")
                                    if choice == "3":
                                        print("You decide that it is best you finish the mission you were sent to accomplish.")
                                        print("The ship is already on path to Mars there is nothing for you to do.")
                                        print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                        print("All you can do now is let the days go by as your ship approaches Mars.")
                                        print("The primary floors of the ship contain enough food and water for a one way trip.")
                                        print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                        print("You have failed your mission, but you did make it to Mars.")
                                        return False
                                    elif choice == "4":
                                        print("You decide that it is best to recourse the ship and head back to Earth.")
                                        print("The complications lie in the fact that you have no contact with the ground.")
                                        print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                        print("All there is to do now is wait out the days back to Earth.")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                        print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                        print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                        return False
                            elif choice == "4":
                                print("You decide to investigate the object that landed on your ship.")
                                print("You make your way across the top of the ship toward the large reflective object.")
                                print("There are no windows doors, or anything that look familiar to your ship.")
                                print("You get up next to the object and it seems like a mirror you can clearly see yourself in the reflection of the object.")
                                print("You begin to search aroundthe side to see if you can find an entry point.")
                                print("There is a hole in the top of the ship leading to the crew quarters.")
                                print("Nearest to this hole look almost like a loading dock of a large cargo plane.You can climb inside and further investigate this object or Head back inside the ship.\n")
                                action8 ={3: "Climb inside to investigate the object further", 4: "Head back inside the ship"}
                                print(action8)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("You climb up the long loading dock being careful not to lose your footing on its reflective surface.")
                                    print("On your way up the tassle attached to you is not long enough to contiunue in.")
                                    print("At this point you have no choice but to release yourself from the tether of your ship. You untether yourself and enter the object.")
                                    print("On the inside the top of the object is just a long flat white light accompanied by the same reflective floor as before.")
                                    print("You walk deeper into the object to see what appears to be an elevated ring with nothing but two large black rings in front of it.")
                                    print("Behind you you hear the sound of the entrance lifting to close the object.You rush back toward the entrance, but are much too late as the object seals shut")
                                    print("Along with the only known exit being shut the ship has no pressurized to normal gravity.")
                                    print("The spacesuit now is heavy and you cannot move unless you take it off. With no other option you begin to remove the suit starting with the helmet.")
                                    print("The air around you appears to be breathable, but as time goes on your eyes begin to feel heavy.The suit is off but your body feels heavier than before.")
                                    print("The air must be knocking you out once again. You fall to the ground. You have failed your mission.\n")
                                    return False
                                elif choice == "4":
                                    print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates.")
                                    print("The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongings you brought onto the ship with you will be lost in space along with the remainof your crewmates.You open the airlock from the outside and enter the ship.After closing the door you prepare to reenter the space ship again. You know that you are alone.Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.Making your way toward the quarters you can hear something on the inside moving around.It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!' Knowing everything you saw on the inside of the crew quarters you now have to make a decision.")
                                    action9 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                                    print(action9)
                                    choice = input("Action 3 or 4? ")
                                    if choice == "3":
                                        print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                        print("You face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                        print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                        print("The door opens into a dark room with no oxygen as you had left it previously.")
                                        print("You step inside looking around for Alex who was crying for help.There is no one immediately near the door as you would have expected from the cries.")
                                        print("Just as fear, and doubt enter something cries out above you and drops from the ceiling. You have failed your mission.")
                                        return False
                                    elif choice == "4":
                                        print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                        print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.The decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                        print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                        print("The threat that was on the ship threatening your life is now gone.")
                                        print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive. All there is to do now is wait out the days back to Earth.")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                        print("This means that all you have to do is wait for the ship to take you home.")
                                        print("This was the only true way to survive.Your comrades died in vein, but your objective is complete.You have passed the mission.")
                                        action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                        print(action10)
                                        choice = input("Action 3 or 4? ")
                                        if choice == "3":
                                            print("You decide that it is best you finish the mission you were sent to accomplish.")
                                            print("The ship is already on path to Mars there is nothing for you to do.")
                                            print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                            print("All you can do now is let the days go by as your ship approaches Mars.")
                                            print("The primary floors of the ship contain enough food and water for a one way trip.")
                                            print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                            print("You have failed your mission, but you did make it to Mars.")
                                            return False
                                        elif choice == "4":
                                            print("You decide that it is best to recourse the ship and head back to Earth.")
                                            print("The complications lie in the fact that you have no contact with the ground.")
                                            print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                            print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                            print("All there is to do now is wait out the days back to Earth.")
                                            print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                            print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                            print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                            return False
            
                elif choice == "4":
                    print("You exit the airlock the same way you came in and make your way to the flight deck to contact HQ.")
                    print("Upon reaching the flight deck the HQ appears to be unreachable as the communications for your ship seem to have been destroyed.")
                    print("Before entering the quarters you had the option to contact HQ meaning it was destroyed long after what impacted the ship. You now have two options.")
                    action5 = {3: "Attempt to restore communications" , 4: "Figure out what impacted with the ship"}
                    print(action5)
                    choice = input("Action 3 or 4? ")
                    if choice == "3":
                        print("You decide that attempted to restore communications with HQ is your best shot at making the right decision.")
                        print("The communications center is structured almost entirely through the research room.")
                        print("You make your way through the main floor toward the research room and begin opening the airlock.")
                        print("After passing through the first door you enter the research room to find that it is intact.")
                        print("The room is filled with various points of study.")
                        print("There are supplies to garden, micropscopes and trays to study potential findings, a water filtration backup, and lastly a communications area.")
                        print("The area is made up of a large box and wires that run along the ship and connect to sattelite points outside.")
                        print("Upon inspection the communications area seems fine along with the rest of the research room as if it had not been impacted.\n")
                        print("The only other option was to check satellite points outside the ship, which also means you will figure out what impacted the ship.")
                        print("You make your way back to the main airlock where you initially got you spacesuit.")
                        print("You open the airlock, close the door behind you and begin to prepare for your spacewalk.")
                        print("There are small clips that you must fasten to the ship to make sure you are not taken too far from the ship.")
                        print("You open the door and make your way into space latching on to the bar above the door you float down and fasten the door behind you.")
                        print("Climbing above the airlock you can now see the top of the ship.")
                        print("The ship is build into layers stacked onto one another with various rooms branching out.")
                        print("The flight deck has 3 large solar sails attatched to it giving the ship the ability to move through space.")
                        print("As long as this stays intact the ship can move through space meaning the rest of the areas are expendable. You make your way past the solar sails to see the impact.")
                        print("There is a diamond shaped object resting on the top of the ship. The object is a silverish color but it appears to almost be fully reflective.")
                        print("While inspecting the object you can also clearly see that the communcations points outside of the research room are completeley destroyed from the impact of the object.")
                        print("This thing must have passed through the cargo bay and into the back of the ship directly hitting the crew quarters.")
                        print("Being that the object is so far back you could drop it into space along with the crew quarters.You also can search the object to find out what it is.\n")
                        action6 = {3: 'Head back inside to remove that area of the ship', 4: 'Investigate the object closer'}
                        print(action6)
                        choice = input("Action 3 or 4? ")
                        if choice == "3":
                            print("You move back toward the airlock where you came from.")
                            print("The object on top must have been carrying whatever it was that killed your crewmates.")
                            print("The idea is that if you remove the crew quarters it will bring the object with it.")
                            print("The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates.")
                            print("You open the airlock from the outside and enter the ship.")
                            print("After closing the door you prepare to reenter the space ship again.")
                            print("You know that you are alone.")
                            print("Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.")
                            print("Making your way toward the quarters you can hear something on the inside moving around.")
                            print("It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.")
                            print("As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.\n")
                            action7 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                            print(action7)
                            choice = input("Action 3 or 4? ")
                            if choice == "3":
                                print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                print("You face the airlock and begin opening the door.")
                                print("The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                print("The door opens into a dark room with no oxygen as you had left it previously.")
                                print("You step inside looking around for Alex who was crying for help.")
                                print("There is no one immediately near the door as you would have expected from the cries.")
                                print("Just as fear, and doubt enter something cries out above you and drops from the ceiling.You have failed your mission.")
                                return False
                            elif choice == "4":
                                print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.")
                                print("The decision has already been made, and you pull the lever.")
                                print("The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                print("The threat that was on the ship threatening your life is now gone.")
                                print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.\n")                    
                                action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                print(action10)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("You decide that it is best you finish the mission you were sent to accomplish.")
                                    print("The ship is already on path to Mars there is nothing for you to do.")
                                    print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                    print("All you can do now is let the days go by as your ship approaches Mars.")
                                    print("The primary floors of the ship contain enough food and water for a one way trip.")
                                    print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                    print("You have failed your mission, but you did make it to Mars.")
                                    return False
                                elif choice == "4":
                                    print("You decide that it is best to recourse the ship and head back to Earth.")
                                    print("The complications lie in the fact that you have no contact with the ground.")
                                    print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                    print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                    print("All there is to do now is wait out the days back to Earth.")
                                    print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                    print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                    print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                    return False
                        elif choice == "4":
                            print("You decide to investigate the object that landed on your ship.")
                            print("You make your way across the top of the ship toward the large reflective object.")
                            print("There are no windows doors, or anything that look familiar to your ship.")
                            print("You get up next to the object and it seems like a mirror you can clearly see yourself in the reflection of the object.")
                            print("You begin to search aroundthe side to see if you can find an entry point.")
                            print("There is a hole in the top of the ship leading to the crew quarters.")
                            print("Nearest to this hole look almost like a loading dock of a large cargo plane.You can climb inside and further investigate this object or Head back inside the ship.\n")
                            action8 ={3: "Climb inside to investigate the object further", 4: "Head back inside the ship"}
                            print(action8)
                            choice = input("Action 3 or 4? ")
                            if choice == "3":
                                print("You climb up the long loading dock being careful not to lose your footing on its reflective surface.")
                                print("On your way up the tassle attached to you is not long enough to contiunue in.")
                                print("At this point you have no choice but to release yourself from the tether of your ship. You untether yourself and enter the object.")
                                print("On the inside the top of the object is just a long flat white light accompanied by the same reflective floor as before.")
                                print("You walk deeper into the object to see what appears to be an elevated ring with nothing but two large black rings in front of it.")
                                print("Behind you you hear the sound of the entrance lifting to close the object.You rush back toward the entrance, but are much too late as the object seals shut")
                                print("Along with the only known exit being shut the ship has no pressurized to normal gravity.")
                                print("The spacesuit now is heavy and you cannot move unless you take it off. With no other option you begin to remove the suit starting with the helmet.")
                                print("The air around you appears to be breathable, but as time goes on your eyes begin to feel heavy.The suit is off but your body feels heavier than before.")
                                print("The air must be knocking you out once again. You fall to the ground. You have failed your mission.\n")
                                return False
                            elif choice == "4":
                                print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates.")
                                print("The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongings you brought onto the ship with you will be lost in space along with the remainof your crewmates.You open the airlock from the outside and enter the ship.After closing the door you prepare to reenter the space ship again. You know that you are alone.Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.Making your way toward the quarters you can hear something on the inside moving around.It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!' Knowing everything you saw on the inside of the crew quarters you now have to make a decision.")
                                action9 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                                print(action9)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                    print("You face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                    print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                    print("The door opens into a dark room with no oxygen as you had left it previously.")
                                    print("You step inside looking around for Alex who was crying for help.There is no one immediately near the door as you would have expected from the cries.")
                                    print("Just as fear, and doubt enter something cries out above you and drops from the ceiling. You have failed your mission.")
                                    return False
                                elif choice == "4":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                    print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.The decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                    print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                    print("The threat that was on the ship threatening your life is now gone.")
                                    print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")
                                    print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive. All there is to do now is wait out the days back to Earth.")
                                    print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                    print("This means that all you have to do is wait for the ship to take you home.")
                                    print("This was the only true way to survive.Your comrades died in vein, but your objective is complete.You have passed the mission.")
                                    action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                    print(action10)
                                    choice = input("Action 3 or 4? ")
                                    if choice == "3":
                                        print("You decide that it is best you finish the mission you were sent to accomplish.")
                                        print("The ship is already on path to Mars there is nothing for you to do.")
                                        print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                        print("All you can do now is let the days go by as your ship approaches Mars.")
                                        print("The primary floors of the ship contain enough food and water for a one way trip.")
                                        print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                        print("You have failed your mission, but you did make it to Mars.")
                                        return False
                                    elif choice == "4":
                                        print("You decide that it is best to recourse the ship and head back to Earth.")
                                        print("The complications lie in the fact that you have no contact with the ground.")
                                        print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                        print("All there is to do now is wait out the days back to Earth.")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                        print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                        print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                        return False

                    elif choice == "4":
                            print("You make your way back to the main airlock where you initially got you spacesuit.")
                            print("You open the airlock, close the door behind you and begin to prepare for your spacewalk.")
                            print("There are small clips that you must fasten to the ship to make sure you are not taken too far from the ship.")
                            print("You open the door and make your way into space latching on to the bar above the door you float down and fasten the door behind you.")
                            print("Climbing above the airlock you can now see the top of the ship.")
                            print("The ship is build into layers stacked onto one another with various rooms branching out.")
                            print("The flight deck has 3 large solar sails attatched to it giving the ship the ability to move through space.")
                            print("As long as this stays intact the ship can move through space meaning the rest of the areas are expendable. You make your way past the solar sails to see the impact.")
                            print("There is a diamond shaped object resting on the top of the ship. The object is a silverish color but it appears to almost be fully reflective.")
                            print("While inspecting the object you can also clearly see that the communcations points outside of the research room are completeley destroyed from the impact of the object.")
                            print("This thing must have passed through the cargo bay and into the back of the ship directly hitting the crew quarters.")
                            print("Being that the object is so far back you could drop it into space along with the crew quarters.You also can search the object to find out what it is.\n")
                            action6 = {3: 'Head back inside to remove that area of the ship', 4: 'Investigate the object closer'}
                            print(action6)
                            choice = input("Action 3 or 4?")
                            if choice == "3":
                                print("You move back toward the airlock where you came from.")
                                print("The object on top must have been carrying whatever it was that killed your crewmates.")
                                print("The idea is that if you remove the crew quarters it will bring the object with it.")
                                print("The only downside to this is that any belongins you brought onto the ship with you will be lost in space along with the remainsof your crewmates.")
                                print("You open the airlock from the outside and enter the ship.")
                                print("After closing the door you prepare to reenter the space ship again.")
                                print("You know that you are alone.")
                                print("Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.")
                                print("Making your way toward the quarters you can hear something on the inside moving around.")
                                print("It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.")
                                print("As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!,' knowing everything you saw on the inside of the crew quarters.\n")
                                action7 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                                print(action7)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                    print("You face the airlock and begin opening the door.")
                                    print("The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                    print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                    print("The door opens into a dark room with no oxygen as you had left it previously.")
                                    print("You step inside looking around for Alex who was crying for help.")
                                    print("There is no one immediately near the door as you would have expected from the cries.")
                                    print("Just as fear, and doubt enter something cries out above you and drops from the ceiling.You have failed your mission.")
                                    return False
                                elif choice == "4":
                                    print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                    print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.")
                                    print("The decision has already been made, and you pull the lever.")
                                    print("The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                    print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                    print("The threat that was on the ship threatening your life is now gone.")
                                    print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.\n")                    
                                    action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                    print(action10)
                                    choice = input("Action 3 or 4? ")
                                    if choice == "3":
                                        print("You decide that it is best you finish the mission you were sent to accomplish.")
                                        print("The ship is already on path to Mars there is nothing for you to do.")
                                        print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                        print("All you can do now is let the days go by as your ship approaches Mars.")
                                        print("The primary floors of the ship contain enough food and water for a one way trip.")
                                        print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                        print("You have failed your mission, but you did make it to Mars.")
                                        return False
                                    elif choice == "4":
                                        print("You decide that it is best to recourse the ship and head back to Earth.")
                                        print("The complications lie in the fact that you have no contact with the ground.")
                                        print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                        print("All there is to do now is wait out the days back to Earth.")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                        print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                        print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                        return False
                            elif choice == "4":
                                print("You decide to investigate the object that landed on your ship.")
                                print("You make your way across the top of the ship toward the large reflective object.")
                                print("There are no windows doors, or anything that look familiar to your ship.")
                                print("You get up next to the object and it seems like a mirror you can clearly see yourself in the reflection of the object.")
                                print("You begin to search aroundthe side to see if you can find an entry point.")
                                print("There is a hole in the top of the ship leading to the crew quarters.")
                                print("Nearest to this hole look almost like a loading dock of a large cargo plane.You can climb inside and further investigate this object or Head back inside the ship.\n")
                                action8 ={3: "Climb inside to investigate the object further", 4: "Head back inside the ship"}
                                print(action8)
                                choice = input("Action 3 or 4? ")
                                if choice == "3":
                                    print("You climb up the long loading dock being careful not to lose your footing on its reflective surface.")
                                    print("On your way up the tassle attached to you is not long enough to contiunue in.")
                                    print("At this point you have no choice but to release yourself from the tether of your ship. You untether yourself and enter the object.")
                                    print("On the inside the top of the object is just a long flat white light accompanied by the same reflective floor as before.")
                                    print("You walk deeper into the object to see what appears to be an elevated ring with nothing but two large black rings in front of it.")
                                    print("Behind you you hear the sound of the entrance lifting to close the object.You rush back toward the entrance, but are much too late as the object seals shut")
                                    print("Along with the only known exit being shut the ship has no pressurized to normal gravity.")
                                    print("The spacesuit now is heavy and you cannot move unless you take it off. With no other option you begin to remove the suit starting with the helmet.")
                                    print("The air around you appears to be breathable, but as time goes on your eyes begin to feel heavy.The suit is off but your body feels heavier than before.")
                                    print("The air must be knocking you out once again. You fall to the ground. You have failed your mission.\n")
                                    return False
                                elif choice == "4":
                                    print("You move back toward the airlock where you came from. The object on top must have been carrying whatever it was that killed your crewmates.")
                                    print("The idea is that if you remove the crew quarters it will bring the object with it. The only downside to this is that any belongings you brought onto the ship with you will be lost in space along with the remainof your crewmates.You open the airlock from the outside and enter the ship.After closing the door you prepare to reenter the space ship again. You know that you are alone.Communications with HQ have been cut entirely, and the only thing left on the ship besides you is whatever hurt your crewmates.Making your way toward the quarters you can hear something on the inside moving around.It is impossible for it to be a crewmate since the oxygen has been gone for so long, so you decide to make your way to the release point.As You are about to release the crew quarters you hear a voice callout 'Help its me Alex!' Knowing everything you saw on the inside of the crew quarters you now have to make a decision.")
                                    action9 = {3: "Open the airlock and save who is calling for help", 4: "Release the crew Quarters regardless of the cries"}
                                    print(action9)
                                    choice = input("Action 3 or 4? ")
                                    if choice == "3":
                                        print("Even with the amount of time the crew quarters was out of power, and what you saw inside you choose to enter.")
                                        print("You face the airlock and begin opening the door. The cries do not let up,and as you pass through to the second door of the airlock the inside goes quiet.")
                                        print("You no longer hear the cries assuming that your crewmate is just waiting for you you begin to open the door.")
                                        print("The door opens into a dark room with no oxygen as you had left it previously.")
                                        print("You step inside looking around for Alex who was crying for help.There is no one immediately near the door as you would have expected from the cries.")
                                        print("Just as fear, and doubt enter something cries out above you and drops from the ceiling. You have failed your mission.")
                                        return False
                                    elif choice == "4":
                                        print("Despite the convincing sounds of a crewmate crying out to you you choose to release the crew quarters.")
                                        print("You make your way to the release point and before you pull the lever the cries grow even louder begging for help.The decision has already been made, and you pull the lever.The ship creates a loud whine as the crew quarters is seperated from the body of the ship.")
                                        print("You make your way to the window of the door that was previously an airlock and watch as the crew quarters, and mysterious shape drift off course of your spacecraft.")
                                        print("The threat that was on the ship threatening your life is now gone.")
                                        print("Your only remaining objective is to survive and finish the trip to Mars or recourse your mission and head back home.")
                                        print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive. All there is to do now is wait out the days back to Earth.")
                                        print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                        print("This means that all you have to do is wait for the ship to take you home.")
                                        print("This was the only true way to survive.Your comrades died in vein, but your objective is complete.You have passed the mission.")
                                        action10 = {3: "Finish the trip to Mars", 4: "Recourse the mission back to Earth"}
                                        print(action10)
                                        choice = input("Action 3 or 4? ")
                                        if choice == "3":
                                            print("You decide that it is best you finish the mission you were sent to accomplish.")
                                            print("The ship is already on path to Mars there is nothing for you to do.")
                                            print("The communications are destroyed beyond repair from the object impacting with the ship.")
                                            print("All you can do now is let the days go by as your ship approaches Mars.")
                                            print("The primary floors of the ship contain enough food and water for a one way trip.")
                                            print("The cargo bay being destroyed in the impact ruined any chances of you being able to inhabit Mars.\nYou will make it to Mars, but you will not survive.\n")
                                            print("You have failed your mission, but you did make it to Mars.")
                                            return False
                                        elif choice == "4":
                                            print("You decide that it is best to recourse the ship and head back to Earth.")
                                            print("The complications lie in the fact that you have no contact with the ground.")
                                            print("There is enough food and water within the primary floors of the ship, but this does not mean the landing will be safe.")
                                            print("Assuming that the HQ is panicked about the loss of connection they may anticipate your return home meaning you will more than likely survive.")
                                            print("All there is to do now is wait out the days back to Earth.")
                                            print("The ship is equipped with solar panels around the flight deck that act as sails powered by sunlight.")
                                            print("This means that all you have to do is wait for the ship to take you home. This was the only true way to survive.")
                                            print("Your comrades died in vein, but your objective is complete. You have passed the mission.")
                                            return False
        elif choice == "2":
            print("You decided to build a raft to escape the jungle")
            print("You went out to the wild jungle and gathered resources to build your raft")
            print("The bad new is that all the woods and trees are wet due to the heavy rainstorm")
            print("There were noises coming from the bush and you started to get worried")
            print("The noise gotten louder and louder and you prepared to defend yourself for whatever happened next")
            print("Who goes there, and come out fight me like a man you said...")
            print("You found a average size rocked and threw it at the bush")
            print("Wait...!! Don't throw that rock at me please sir said the mystery person...")
            print("Unexpectdately, it was only a little kid that was hiding in the bush.")
            print("You think to yourself, do you want to approach this kid or scare him away...")
            action2 = {3:"I will carefully approach the little kidd..", 4:"I should scare him away..."}
            print(action2)
            choice = input("Action 3 or 4? ")
           
            if choice == "3": 
                print("You decided to approach to the kid. You and him started introducing each other and getting each other's name")
                print("The kid said his name was Jack. Jack said he was also had his plane crashed in the jungle long time ago.")
                print("He said he have tried many ways to escape the jungle but it was impossible for him")
                print("Jack is really nice and offered to help you")
                print("Jack is only 12 years old however he was very smart and strong")
                print("There he gave up hope and decided to make the jungle as his new permanent home")
                print("Jack has not found another survivor ever since his crash but now he is happy and well!")
                print("He started to gain hope and trying again to get out of the jungle")
                print("Throughout the conversation, he asked if you can be part of your journey. Jack wanted to help building the raft")
                print("You and Jack continue gathering resources to build the raft and went back to the site of the plane crash")
                print("There you and him made a great team work and finishing up the raft")
                print("After finishing it, you and Jack pushed it to the bay to test it out. The result of it was fantastic!!")
                print("You and Jack packed up your belongings and head to the raft, started paddeling to saftey!")
                print("You and Jack were able to leave the jungle safely. The end!")
                return False 
           
            elif choice == "4":
                print("You decided to scare the little kid away...")
                print("OW..the kid yelled painfully!")
                print("He came out from the bushes and started rubbing his arm which was bruised")
                print("Why did you throw that at me...The kid asked while in pain..")
                print("you said that you thought there was a wild animal hiding in the bushes and got really startled...")
                print("You helped the little kid and started asking for his name...he said his name was Jack")
                print("He was in shocked when he found another person stranded in the jungle..")
                print("you and jack started talking and bonding...however you still keep your gaurd up in case he was still a potential threat")
                print("Jack wanted to tag along on your journey and help with gathering wood. He said he knows the best place to get dry wood..")
                print("You think to yourself...you can use another set of hand to find the dry wood and while looking around there is not a single on sight..")
                print("You can bring jack and he will help you find the dry woods or leave him and walk away..")
                action3 = {3: "I want to bring jack along...", 4: "I will leave him and do not need his help.."}
                print(action3)
                choice = input("Action 3 or 4? ")
                
                
                if choice == "3": 
                    print("You have decided to bring jack along with you, and need of his help to find the dry pieces of wood to build the raft..")
                    print("You started following jack to get the dry pieces of wood. However, there was an incident...a wild animal appeared out of nowwhere...")
                    print("jack was scared and his armed was still bruised from earlier...")
                    print("you started searching your pockets to find if there is anything to use to defend...and you used the ax...")
                    print("you started swinging and yelling at the wild animal...jack threw pebbles at it and the animal ran off")
                    print("Are you okay, jack?...you asked. He replied...yes I am thanks for defending me....")
                    print("it was no problem...glad your safe you said! Then moving on, you and jack continued to find the location of the dry pieces of wood")
                    print("Along the way, you and jack start to get hungry and decide to find some food...")
                    print("Look there are wild berries... we should take some...jack said")
                    print("However, it might be poisonous and not sure if it safe to eat...")
                    print("Do you want to eat the wild berries or continute walking to the locate the dry pieces of wood?")
                    action4 = {3: "I will eat the picked berries", 4: "I will continue walking to the locate the dry pieces of wood.."}
                    print(action4)
                    choice = input("Action 3 or 4? ")
                    
                    if choice == "3": 
                        print("You and jack decided to eat the wild berries..")
                        print("You and jack picked the berries from the bush and start putting it into both of your mouths..")
                        print("The berries were washed throughly...however, there was a small issue...")
                        print("the berries were poisonous, and both you and jack start to get a reaction..")
                        print("Your throat started to swallow up and you cannot breath...Jack on the other hand started itching really hard and breaking out hives")
                        print("It feels like the inside of your throat was closing in and could not let any air flow through...")
                        print("the decision to eat the berries was regretful..however, the condition of you and jack got worsen and started to lose air")
                        print("You and jack passed out on the ground dreary and started to lose breathing...suddenly..both of you died on site..The end!")
                        return False
                  
                  
                    elif choice == "4": 
                        print("you decided to leave Jack behind and walk away...")
                        print("Although, you felt bad about leaving him behind you think to yourself it would add more responsibility taking care of a kid...")
                        print("As you continue to walk and minding your own business...you noticed he started to follow you")
                        print("You just kept on walking and walking hopefully he catches the hint to not folow you anymore..but he did not")
                        print("Jack said...please let me come with you and I will make sure you will find the dry pieces of wood that you are looking for..")
                        print("You started to be more curious and wonder why but nevertheless you were desperate to get those dry pieces of wood")
                        print("You were annoyed that he kept on following you...can you stop following me please you stated!")
                        print("Jack said he has a map to the place...")
                        print("You still do not want Jack to follow you, but he has the map to the location..:")
                        print("You have the option to trick Jack and grab the map then make a run for it...or make him go away still..?")
                        action5 = {3: "I will trick jack into giving me the map and make a run for it" , 4: "Tell him to go away..and never want to see his face again"}
                        print(action5)
                        
                        
                        choice = input("Action 3 or 4? ")
                        if choice == "3":
                            print("you decided to trick jack into giving you the map and making a run for it..")
                            print("You kindly asked to see the map and allowing jack to show you where the location is...")
                            print("you dont want jack to follow...so you told him if you can see it while holding it...")
                            print("Jack was skeptical about it but he trusted you..so he handed you the map..")
                            print("you then took off and ran really fast...Jack was started chasing you..")
                            print("Jack was really fast and so you gotten tired and decided to stop...")
                            print("Hey! why did you run away with my map?...he asked furiously")
                            print("Because I do not want you to come with me and so I would find the location alone without your help")
                            
def replay():
    answer = input("Do you want to replay again? Type: Y/Yes or N/No?\n").capitalize()
    if answer == "Y" or "Yes":
        makeittothened()
    else:
        print("Thanks for playing Making it to The End by the developer, Bryan Nguyen! Have a good day!!")
        
            
def makeittothened():
    actionpart()
    replay()

makeittothened()
