import fresh_tomatoes
import media

# list of movies to display on page

facing_the_giants = media.Movie("Facing the Giants",
                                "A losing coach with an underdog football team faces their giants of fear and failure on and off the field to surprising results.",
                                "http://bit.ly/2yE5Pc2",
                                "https://www.youtube.com/watch?v=4xneiV7Ru6Q")


courageous = media.Movie ("Courageous",
                          "When a tragedy strikes close to home, four police officers struggle with their faith and their roles as husbands and fathers; together they make a decision that will change all of their lives.",
                          "http://bit.ly/2fKkWNt",
                          "https://www.youtube.com/watch?v=70MVn1q-yyM")

saving_christmas = media.Movie("Saving Christmas",
                            "Kirk is enjoying the annual Christmas party extravaganza thrown by his sister until he realizes he needs to help out Christian, his brother-in-law, who has a bad case of the bah-humbugs.",
                            "http://bit.ly/2wtoO8I",
                            "https://www.youtube.com/watch?v=z5-yA66kaVc")

fireproof = media.Movie("Fireproof",
                        "In an attempt to save his marriage, a firefighter uses a 40-day experiment known as 'The Love Dare'.",
                        "http://bit.ly/2hIK1sx",
                        "https://www.youtube.com/watch?v=YK5-5qf9IQs")

star_trek_beyond = media.Movie("Star Trek Beyond",
                               "The U.S.S. Enterprise crew explores the furthest reaches of uncharted space, where they encounter a new ruthless enemy, who puts them, and everything the Federation stands for, to the test.",
                               "http://bit.ly/2xPkwdr",
                               "https://www.youtube.com/watch?v=XRVD32rnzOw")

star_trek_into_darkness = media.Movie("Star Trek Into Darkness",
                                      "After the crew of the Enterprise find an unstoppable force of terror from within their own organization, Captain Kirk leads a manhunt to a war-zone world to capture a one-man weapon of mass destruction.",
                                      "http://bit.ly/2xMLfts",
                                      "https://www.youtube.com/watch?v=QAEkuVgt6Aw")

rogue_one = media.Movie("Rogue One",
                        "The Rebel Alliance makes a risky move to steal the plans for the Death Star, setting up the epic saga to follow.",
                        "http://bit.ly/2xWnAXd",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

the_force_awakens = media.Movie("Star Wars: The Force Awakens",
                                "Three decades after the Empire's defeat, a new threat arises in the militant First Order. Stormtrooper defector Finn and spare parts scavenger Rey are caught up in the Resistance's search for the missing Luke Skywalker.",
                                "http://bit.ly/2glaive",
                                "https://www.youtube.com/watch?v=sGbxmsDFVnE")
                                                             
                              
#calls list of movies for fresh_tomotoes to display on page
movies = [facing_the_giants, courageous, saving_christmas, fireproof, star_trek_beyond,
          star_trek_into_darkness, rogue_one, the_force_awakens] 

fresh_tomatoes.open_movies_page(movies)

                    
                      
