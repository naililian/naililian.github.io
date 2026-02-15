import re
from pathlib import Path
import sys

sys.path.append("C:/Program Files (x86)/Toon Boom Animation/Toon Boom Harmony 25 Premium/win64/bin/python-packages")

from ToonBoom import harmony

def generate_actions_markdown(output_file="actions.md"):
    """Generate markdown report of all actions grouped by responder in a table format."""
    
    md_content = []
    
    # Get Harmony session and actions
    sess = harmony.session()
    actions = sess.actions
    
    # Get all responders
    responders = actions.responders
    print(f"Found {len(responders)} responders")
    
    # Sort them alphabetically
    responders_sorted = sorted(responders)
    
    md_content.append("# Actions\n")
    md_content.append("You'll find all the information about Harmony actions organized by responder.\n")
    
    # Process each responder
    for responder in responders_sorted:
        print(f"Processing Responder: {responder}")
        
        # Get actions for this responder
        action_list = actions.actions(responder)
        
        if action_list and len(action_list) > 0:
            # Add responder heading
            md_content.append(f"## {responder}\n")
            
            # Add table header
            md_content.append("| Action |")
            md_content.append("|---|")
            
            # Sort actions alphabetically
            sorted_actions = sorted(action_list)
            print(f"  Found {len(sorted_actions)} actions")
            
            # Add each action to the table
            for action in sorted_actions:
                # Clean up action string
                action_str = str(action).strip()
                if action_str:
                    md_content.append(f"| `{action_str}` |")
            
            md_content.append("\n")
    
    # Write to file
    output_path = Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_content))
    
    print(f"\nReport generated: {output_path.absolute()}")
    print(f"Total sections: {len([line for line in md_content if line.startswith('##')])}")

if __name__ == "__main__":
    # Determine output path relative to script location
    repo_root = Path(__file__).resolve().parents[1]
    output_path = repo_root / "docs" / "actions.md"
    
    # Open a Harmony project (you can modify this path if needed)
    nodes_data_scn = "E:/Toon Boom/TB_Scripts/HarmonyScenes/DATAANALYSE/nodes_data_attributes/nodes_data_attributes.xstage"
    print(f"Opening project: {nodes_data_scn}")
    harmony.open_project(nodes_data_scn)
    print("Project opened successfully!\n")
    
    # Generate the markdown
    generate_actions_markdown(output_path)
