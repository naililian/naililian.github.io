
import re
from pathlib import Path
import sys

sys.path.append( "C:/Program Files (x86)/Toon Boom Animation/Toon Boom Harmony 25 Premium/win64/bin/python-packages" ) 

from ToonBoom import harmony

nodes_data_scn = "E:/Toon Boom/TB_Scripts/HarmonyScenes/DATAANALYSE/nodes_data_attributes/nodes_data_attributes.xstage"

harmony.open_project(nodes_data_scn) 
sess = harmony.session()                                     #Get access to the Harmony session, this class.
actions = sess.actions 
                                      #Get actions handler.
for responder in actions.responders:
  print( responder )
  action_list = actions.actions(responder)
  for action in action_list:
     print( "   %s"%(action) ) 




from ToonBoom import harmony
sess = harmony.session()                                     #Get access to the Harmony session, this class.
actions = sess.actions 
                                      #Get actions handler.
for responder in actions.responders:
  print( responder )
  action_list = actions.actions(responder)
  for action in action_list:
     print( "   %s"%(action) ) 