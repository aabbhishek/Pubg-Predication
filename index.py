#!C:\Program Files\Python36\python.exe -u
import cgitb
cgitb.enable()
print("Content-type: text/html\r\n")

import sys
sys.path.insert(0, 'includes')

from pre_loads import *

# Main HTML code Beggins from here 

print('''	<!DOCTYPE html> <html lang="en"> ''')

print('''<head>''')

# css import #######################################################################################
# 
print(css())


print('''  <title> Pubg DataSet </title> </head> ''')

print('<body>')

#header part ###################################################################################

print(''' 
		<div >
			<nav class="navbar abs-pos navbar-light color-2-rbga col-md-12">
  				<a class="navbar-brand" href="#">Navbar</a>
			</nav>
			<!--<div class="row" >
				<div class="col-xl-12"> 
					<span class="icon-nav-font text-white"><i class="fas fa-bars"></i></span>
				 </div>
			</div>-->
			<div  class="with-full  main-bg text-white" style="height:60%">
				<div id="particles-js">
						
				 		<div class="row ">
					 		<div class="col-xl-12">

									<h1 class="font_max_full font_quz font-weight-bold"><center>PUBG DATA PREDICTION</center></h1>

				 	  		</div>
				 		</div>
					
				</div>
	     	 </div>
	     	 <div class="container margin_none text-white" style="padding:0px !important;">
	     	 	<div class="row">
	     	 		<div class="col-md-12">
	     	 			<div class="color_3">
	     	 				<br>
	     	 				<h2 class="text-font">About Game </h2>
	     	 				<p><b>PlayerUnknown's Battlegrounds</b> (PUBG) is an online multiplayer battle royale game developed and published 
	     	 					by PUBG Corporation, a subsidiary of South Korean video game company Bluehole. The game is based on previous
	     	 				 	mods that were created by Brendan "PlayerUnknown" Greene for other games using the film Battle Royale for 
	     	 				 	inspiration, and expanded into a standalone game under Greene's creative direction. In the game, up to one 
	     	 				 	hundred players parachute onto an island and scavenge for weapons and equipment to kill others while avoiding 
	     	 				 	getting killed themselves. The available safe area of the game's map decreases in size over time, directing 
	     	 				 	surviving players into tighter areas to force encounters. The last player or team standing wins the round.
	     	 				 </p>
	     	 			</div>
	     	 		</div>
	     	 	</div>
	     	 </div>
	    </div> 	 

    


		


	''')


#body #########################################################################################

print()


#fotter part ##################################################################################


print()

#js import ###################################################################################
print('</body>')
print(js())
print('''
<script src="js/particles.min.js"></script>

 <script>
  

particlesJS("particles-js", {
  "particles": {
    "number": {
      "value": 380,
      "density": {
        "enable": true,
        "value_area": 800
      }
    },
    "color": {
      "value": "#ffffff"
    },
    "shape": {
      "type": "circle",
      "stroke": {
        "width": 0,
        "color": "#000000"
      },
      "polygon": {
        "nb_sides": 5
      },
      "image": {
        "src": "img/github.svg",
        "width": 100,
        "height": 100
      }
    },
    "opacity": {
      "value": 0.5,
      "random": false,
      "anim": {
        "enable": false,
        "speed": 1,
        "opacity_min": 0.1,
        "sync": false
      }
    },
    "size": {
      "value": 3,
      "random": true,
      "anim": {
        "enable": false,
        "speed": 40,
        "size_min": 0.1,
        "sync": false
      }
    },
    "line_linked": {
      "enable": true,
      "distance": 150,
      "color": "#ffffff",
      "opacity": 0.4,
      "width": 1
    },
    "move": {
      "enable": true,
      "speed": 6,
      "direction": "none",
      "random": false,
      "straight": false,
      "out_mode": "out",
      "bounce": false,
      "attract": {
        "enable": false,
        "rotateX": 600,
        "rotateY": 1200
      }
    }
  },
  "interactivity": {
    "detect_on": "canvas",
    "events": {
      "onhover": {
        "enable": true,
        "mode": "grab"
      },
      "onclick": {
        "enable": true,
        "mode": "push"
      },
      "resize": true
    },
    "modes": {
      "grab": {
        "distance": 140,
        "line_linked": {
          "opacity": 1
        }
      },
      "bubble": {
        "distance": 400,
        "size": 40,
        "duration": 2,
        "opacity": 8,
        "speed": 3
      },
      "repulse": {
        "distance": 200,
        "duration": 0.4
      },
      "push": {
        "particles_nb": 4
      },
      "remove": {
        "particles_nb": 2
      }
    }
  },
  "retina_detect": true
});

</script> ''')
print(''' 

<script src="js/app.js"></script> 
<script src="js/lib/stats.js"></script>





	''')
print('</html>')
