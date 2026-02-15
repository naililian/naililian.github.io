"""
Diagnostic script to test different methods of accessing Harmony actions API

This script attempts multiple approaches to access actions data:
1. Direct API access (requires GUI)
2. Check for cached/stored actions data
3. Provide alternatives for documentation
"""

import sys
from pathlib import Path

sys.path.append("C:/Program Files (x86)/Toon Boom Animation/Toon Boom Harmony 25 Premium/win64/bin/python-packages")

def test_actions_access():
    """Test if we can access actions API without GUI"""
    
    from ToonBoom import harmony
    
    print("="*70)
    print("Testing Harmony Actions API Access")
    print("="*70)
    
    # Test 1: Try to open project and access actions
    print("\nTest 1: Opening project and accessing actions API...")
    try:
        nodes_data_scn = "E:/Toon Boom/TB_Scripts/HarmonyScenes/DATAANALYSE/nodes_data_attributes/nodes_data_attributes.xstage"
        harmony.open_project(nodes_data_scn)
        print("✓ Project opened successfully")
        
        sess = harmony.session()
        print("✓ Session obtained")
        
        actions = sess.actions
        print("✓ Actions handler obtained")
        
        responders = actions.responders
        print(f"  Responders found: {len(responders)}")
        
        if len(responders) > 0:
            print("\n✓ SUCCESS: Actions API is accessible!")
            print(f"  Found {len(responders)} responders")
            for i, responder in enumerate(sorted(responders)[:5]):
                action_list = actions.actions(responder)
                print(f"    {i+1}. {responder}: {len(action_list)} actions")
            if len(responders) > 5:
                print(f"    ... and {len(responders) - 5} more responders")
            return True
        else:
            print("\n✗ FAILED: No responders found")
            print("  The actions API requires Harmony's GUI to be active.")
    
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
    
    return False

def check_for_existing_data():
    """Check if actions.md already has data"""
    
    print("\n" + "="*70)
    print("Checking for existing actions data")
    print("="*70)
    
    docs_path = Path(__file__).resolve().parents[1] / "docs" / "actions.md"
    
    if docs_path.exists():
        with open(docs_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Count sections (responders)
        sections = content.count('\n## ')
        # Count table rows (actions)
        actions_count = content.count('| `')
        
        print(f"\nFile: {docs_path}")
        print(f"  Responder sections: {sections}")
        print(f"  Action entries: {actions_count}")
        
        if sections > 0:
            print("\n✓ File has data! Current documentation is available.")
            return True
        else:
            print("\n✗ File exists but has no action data.")
    else:
        print(f"\n✗ File not found: {docs_path}")
    
    return False

def provide_solutions():
    """Provide solutions for generating actions documentation"""
    
    print("\n" + "="*70)
    print("SOLUTIONS")
    print("="*70)
    
    print("\nThe Harmony actions API requires an active GUI session.")
    print("Here are your options:\n")
    
    print("Option 1: Run from Harmony's Script Editor (RECOMMENDED)")
    print("-" * 60)
    print("1. Open Toon Boom Harmony (any project)")
    print("2. Press F8 or go to Windows > Script Editor")
    print("3. Open and run: generate_actions_from_gui.py")
    print("4. The script will generate docs/actions.md with all data")
    
    print("\nOption 2: Use existing documentation")
    print("-" * 60)
    print("If you've already run the script once, the actions.md")
    print("file should contain all the documentation data.")
    
    print("\nOption 3: Alternative documentation approach")
    print("-" * 60)
    print("Document actions manually by category/topic rather than")
    print("by technical responder, which may be more user-friendly.")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    has_api_access = test_actions_access()
    has_existing_data = check_for_existing_data()
    
    if not has_api_access:
        provide_solutions()
        
        if not has_existing_data:
            print("\n⚠ RECOMMENDATION: Use generate_actions_from_gui.py from within Harmony")
