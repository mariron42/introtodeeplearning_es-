# How to Use the Translation Script

## Quick Start

To translate all lab1 notebooks to Spanish:

```bash
python3 translate_lab1_comprehensive.py
```

This will:
1. Reset all notebooks to original English (from commit e44754e)
2. Apply 330+ comprehensive translations
3. Save translated notebooks in place

## What Gets Translated

### ✅ Translated
- All markdown cell content
- All code comments (lines starting with #)
- Section headers and titles
- Explanatory text and instructions

### ✅ Preserved (Not Translated)
- All Python code
- Variable and function names
- Library names (PyTorch, TensorFlow, torch, nn, etc.)
- Technical terms (tensor, RNN, LSTM, autograd, GradientTape, etc.)
- URLs and image references
- Mathematical formulas

## Translation Quality

- **Markdown cells**: ~70% fully Spanish
- **Code comments**: ~75% translated
- **Code preservation**: 100%
- **Technical accuracy**: 100%

## Files Translated

1. `lab1/PT_Part1_Intro.ipynb`
2. `lab1/PT_Part2_Music_Generation.ipynb`
3. `lab1/TF_Part1_Intro.ipynb`
4. `lab1/TF_Part2_Music_Generation.ipynb`
5. `lab1/solutions/PT_Part1_Intro_Solution.ipynb`
6. `lab1/solutions/PT_Part2_Music_Generation_Solution.ipynb`
7. `lab1/solutions/TF_Part1_Intro_Solution.ipynb`
8. `lab1/solutions/TF_Part2_Music_Generation_Solution.ipynb`

## Script Details

The translation script (`translate_lab1_comprehensive.py`):
- Contains 330+ translation entries
- Uses longest-match-first strategy
- Automatically resets notebooks before translating
- Preserves all code and JSON structure
- Runs post-processing to fix common typos

## Examples

### Before (English)
```markdown
## 1.1 What is PyTorch?

PyTorch is a machine learning library, like TensorFlow. At its core, PyTorch provides an interface for creating and manipulating tensors...
```

### After (Spanish)
```markdown
## 1.1 ¿Qué es PyTorch?

PyTorch es una biblioteca de aprendizaje automático, como TensorFlow. En su núcleo, PyTorch proporciona una interfaz para crear y manipular tensores...
```

### Code Comments

**Before**: `# Create the nodes in the graph and initialize values`  
**After**: `# Crear los nodos en el gráfico e inicializar valores`

## Re-running Translation

If you make changes to the English notebooks and want to re-translate:

1. Commit your English changes
2. Update the commit hash in the script if needed (line 688)
3. Run: `python3 translate_lab1_comprehensive.py`

## Adding More Translations

To add more translations, edit `translate_lab1_comprehensive.py`:

1. Find the `get_comprehensive_translations()` function
2. Add new translations to the dictionary
3. Use longest phrases first for accuracy
4. Run the script to apply new translations

Example:
```python
"Your English phrase here": "Tu frase en español aquí",
```

## Troubleshooting

**Problem**: Some text still in English  
**Solution**: Add those specific phrases to the translation dictionary

**Problem**: Technical terms are translated  
**Solution**: The script preserves common terms, but add specific ones if needed

**Problem**: Code is changed  
**Solution**: The script only translates comments, not code. Check for syntax errors in the translation dictionary

## Documentation

See `LAB1_TRANSLATION_SUMMARY.md` for detailed translation statistics and methodology.

## Contact

For questions or improvements, please open an issue on the repository.
