import re
from pathlib import Path
import sys

sys.path.append( "C:/Program Files (x86)/Toon Boom Animation/Toon Boom Harmony 25 Premium/win64/bin/python-packages" ) 

from ToonBoom import harmony

nodes_data_scn = "E:/Toon Boom/TB_Scripts/HarmonyScenes/DATAANALYSE/nodes_data_attributes/nodes_data_attributes.xstage"

harmony.open_project(nodes_data_scn)                
current_session = harmony.session()                                  
project = current_session.project
nodes = project.scene.nodes         

print( "Current Project: %s"%(project.project_path) )



def extract_preview_name(attr_str):
    """Extract preview name from 'Type(Top/PreviewName, Keyword)' format."""
    match = re.search(r'Top/([^,]+)', str(attr_str))
    return match.group(1) if match else "Unknown"

def generate_nodes_types_md(project, output_file="nodes_types.md"):
    """Generate simple markdown report of all nodes with only name and type."""
    
    md_content = []
    nodes = project.scene.nodes
    
    # Group nodes by preview name
    nodes_by_preview = {}
    
    for node in nodes:
        node_type = node.type
        
        if not node.attributes:
            continue
        
        # Extract preview name from the first attribute
        first_attr = node.attributes[0]
        preview_name = extract_preview_name(first_attr)
        
        if preview_name not in nodes_by_preview:
            nodes_by_preview[preview_name] = node_type
    
    # Sort preview names alphabetically
    sorted_names = sorted(nodes_by_preview.keys())

    md_content.append("# Nodes Types\n")
    md_content.append("List of all available nodes and their types.\n")
    
    # Add table header
    md_content.append("| Node Name | Type |")
    md_content.append("|---|---|")
    
    # Add rows for each node
    for preview_name in sorted_names:
        node_type = nodes_by_preview[preview_name]
        # Create anchor link to nodes_attributes.md
        anchor = preview_name.lower().replace(' ', '-').replace('_', '-')
        md_content.append(f"| [{preview_name}](nodes_attributes.md#{anchor}-node) | {node_type} |")
    
    md_content.append("\n")
    
    # Write to file
    output_path = Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_content))
    
    print(f"Nodes types report generated: {output_path.absolute()}")

# Generate nodes types markdown
repo_root = Path(__file__).resolve().parents[1]
nodes_types_output = repo_root / "docs" / "nodes_types.md"
generate_nodes_types_md(project, output_file=nodes_types_output)
