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

def extract_type_and_keyword(attr_str):
    """Extract Type and Keyword from 'Type(Top/PreviewName, Keyword)' format."""
    attr_str = str(attr_str)
    type_match = re.match(r'(\w+)\(', attr_str)
    keyword_match = re.search(r',\s*([^)]+)\)', attr_str)
    
    attr_type = type_match.group(1) if type_match else "Unknown"
    keyword = keyword_match.group(1) if keyword_match else "Unknown"
    
    return attr_type, keyword

def generate_markdown_report(project, output_file="nodes_report.md"):
    """Generate markdown report of all nodes and their attributes."""
    
    md_content = []
    nodes = project.scene.nodes
    
    for node in nodes:
        node_type = node.type
        print(f"Processing Node Type: {node_type}")
        
        if not node.attributes:
            continue
        
        # Use the preview name from the first attribute as section heading
        first_attr = node.attributes[0]
        preview_name = extract_preview_name(first_attr)
        
        # Add heading
        md_content.append(f"# {preview_name}\n")
        
        # Add table header
        md_content.append("| Level | Parent Keyword | Attribute Type | Attribute Keyword |")
        md_content.append("|---|---|---|---|")
        
        # Process main attributes
        for attribute in node.attributes:
            attr_type, keyword = extract_type_and_keyword(attribute)
            md_content.append(f"| Main |  | {attr_type} | {keyword} |")
            
            # Process sub-attributes
            if attribute.subattributes:
                for subattr in attribute.subattributes:
                    sub_type, sub_keyword = extract_type_and_keyword(subattr)
                    md_content.append(f"| Sub | {keyword} | {sub_type} | {sub_keyword} |")
        
        md_content.append("\n")
    
    # Write to file
    output_path = Path(output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(md_content))
    
    print(f"Report generated: {output_path.absolute()}")

# Call it after get_attributes()
generate_markdown_report(project, output_file="E:/Scripts/PY_HARMONY_DATA/nodes_report.md")