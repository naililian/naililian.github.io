"""Attributes of Nodes from Toon Boom Harmony"""
import sys


sys.path.append( "C:/Program Files (x86)/Toon Boom Animation/Toon Boom Harmony 25 Premium/win64/bin/python-packages" ) 


from ToonBoom import harmony

nodes_data_scn = "E:/Toon Boom/TB_Scripts/HarmonyScenes/DATAANALYSE/nodes_data_attributes/nodes_data_attributes.xstage"

harmony.open_project(nodes_data_scn)                
current_session = harmony.session()                                  
project = current_session.project
nodes = project.scene.nodes                                    
print( "Current Project: %s"%(project.project_path) )


def get_attributes():

    nodes = project.scene.nodes

    for node in nodes:

        print('Node Type: ', node.type)
        for attribute in node.attributes:
            print("  --  Main Attribute : %s"%(attribute))
            subattrb_list = attribute.subattributes
            if attribute.subattributes:
                for subattrb in subattrb_list:
                    print("     ---- Subattr :", subattrb)


get_attributes()



