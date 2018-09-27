import os
from lib.colors import Colors

VERSION = "1.0"

def banner():
    os.system("clear")
    print(Colors.BOLD +
    """
      _________                                   _________            .___      
     /   _____/ ____  __ _________   ____  ____   \_   ___ \  ____   __| _/____  
     \_____  \ /  _ \|  |  \_  __ \_/ ___\/ __ \  /    \  \/ /  _ \ / __ |/ __ \ 
     /        (  <_> )  |  /|  | \/\  \__\  ___/  \     \___(  <_> ) /_/ \  ___/ 
    /_______  /\____/|____/ |__|    \___  >___  >  \______  /\____/\____ |\___  >
            \/                          \/    \/          \/            \/    \/ 
                                    ________                                                                     
                                    \_____  \                                                                    
                                     /  ____/                                                                    
                                    /       \                                                                    
                                    \_______ \                                                                   
                                            \/                                                                   
            ________  .__        __  .__                                                 
            \______ \ |__| _____/  |_|__| ____   ____ _____ _______ ___.__.              
             |    |  \|  |/ ___\   __\  |/  _ \ /    \\__  \\_  __ <   |  |              
             |    `   \  \  \___|  | |  (  <_> )   |  \/ __ \|  | \/\___  |              
            /_______  /__|\___  >__| |__|\____/|___|  (____  /__|   / ____|              
                    \/        \/                    \/     \/       \/       
                                                                       v""" + VERSION + """
                                                                       
       ==[A tool to convert source code into dictionary to perform fuzzing]==
                               Made with ❤️  in Spain                          
                       
                ======= Javier Olmedo - https://hackpuntes.com =======
                [*] Facebook: https://facebook.com/hackpuntes       [*]
                [*] Twitter:  https://twitter.com/jjavierolmedo     [*]
                [*] LinkedIn: https://linkedin.com/in/jjavierolmedo [*]
                [*] GitHub:   https://github.com/JavierOlmedo       [*]
                =======================================================
    """ + Colors.DEFAULT)