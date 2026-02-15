"""
Generate actions.md documentation - RUN THIS FROM HARMONY'S SCRIPT EDITOR

This script must be executed from within Harmony's GUI Script Editor because
the actions API requires an active GUI session with responders initialized.

Instructions:
1. Open Toon Boom Harmony (any project)
2. Go to Windows > Script Editor (or press F8)
3. Copy and paste this entire script into the Script Editor
4. Click "Run" or press Ctrl+Enter
5. The actions.md file will be generated in the docs folder
"""

import re
from pathlib import Path
import sys

def generate_actions_markdown():
    """Generate markdown report of all actions grouped by responder in a table format."""
    
    try:
        from ToonBoom import harmony
        
        md_content = []
        
        # Get Harmony session and actions
        sess = harmony.session()
        actions = sess.actions
        
        # Get all responders
        responders = actions.responders
        print(f"Found {len(responders)} responders")
        
        if len(responders) == 0:
            print("\nERROR: No responders found!")
            print("This script must be run from within Harmony's GUI Script Editor.")
            print("The actions API is not available when Harmony is opened programmatically.")
            return False
        
        # Sort them alphabetically
        responders_sorted = sorted(responders)
        
        md_content.append("# Actions\n")
        md_content.append("You'll find all the information about Harmony actions organized by responder.\n")
        md_content.append("\n!!! info \"GUI Interaction\"\n")
        md_content.append("    Actions are GUI commands that can be triggered through Harmony's interface.\n")
        md_content.append("    They correspond to menu items, toolbar buttons, and keyboard shortcuts.\n")
        
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
        
        # Output path - when running from Script Editor, __file__ is not available
        # Using direct path to the documentation folder
        output_path = Path("E:/Scripts/GITHUB_REPO/naililian.github.io/Python_Harmony/docs/actions.md")
        
        # Ensure the directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(md_content))
        
        print(f"\n{'='*60}")
        print(f"SUCCESS! Report generated: {output_path.absolute()}")
        print(f"Total responders: {len(responders_sorted)}")
        print(f"Total sections: {len([line for line in md_content if line.startswith('##')])}")
        print(f"{'='*60}")
        
        return True
        
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# Run the function
if __name__ == "__main__":
    print("="*60)
    print("Harmony Actions Documentation Generator")
    print("="*60)
    print()
    
    success = generate_actions_markdown()
    
    if not success:
        print("\n" + "="*60)
        print("INSTRUCTIONS:")
        print("="*60)
        print("1. Open Toon Boom Harmony")
        print("2. Open any project")
        print("3. Go to Windows > Script Editor (F8)")
        print("4. Copy this entire script into the editor")
        print("5. Click Run")
        print("="*60)
