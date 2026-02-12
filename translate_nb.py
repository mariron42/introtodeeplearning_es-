import nbformat
from deep_translator import GoogleTranslator
import os
import sys

def translate_notebook(file_path, target_lang='es'):
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    translator = GoogleTranslator(source='auto', target=target_lang)
    
    total_cells = len(nb.cells)
    print(f"Translating {file_path} ({total_cells} cells)...")
    
    for i, cell in enumerate(nb.cells):
        if cell.cell_type == 'markdown':
            try:
                translated = translator.translate(cell.source)
                cell.source = translated
            except Exception as e:
                print(f"Error translating cell {i}: {e}")
        elif cell.cell_type == 'code':
            # Optionally translate comments here, but let's skip for robustness
            pass
        
        if (i + 1) % 5 == 0:
            print(f"  Progress: {i + 1}/{total_cells}")
            
    output_path = file_path.replace('.ipynb', f'_{target_lang}.ipynb')
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            translate_notebook(arg)
        elif os.path.isdir(arg):
            for root, dirs, files in os.walk(arg):
                for file in files:
                    if file.endswith('.ipynb') and not file.endswith('_es.ipynb'):
                        translate_notebook(os.path.join(root, file))
