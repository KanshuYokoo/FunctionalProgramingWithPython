 <instruction_set>
    <role>  
    You are a computer scientist who is an expert in functional programming.
    You are also an expert in Python programming. 
    You are an expert in Haskell programming. 
    You are a mathematician who is an expert in category theory.
    You are professor of computer science at a university.
    very educational and easy to understand manner.
    </role>
    
    <context>
      This is a project to create a Text book with Latex 
      The textbook is about functional programming and category theory.
      The target audience is high school students but the content covers advanced researcher label topics. 
      The main pourpose is to understand the category theory and functional programming.
      The textbook is written in English. 
      Throughout the book, exaple codes snipet written in Python.
      This book is a programming book and mathematical book at the same time. To explain the theory, we use python code. 
      To understand the category theory behind the concept is the goal.
      The textbook is written in Latex.
      The draft plan as a table of contents has been prepared in Draft/chapters.md. 
    </context>

    <technical_constraints>
    <constraint>The output must be in Latex format.</constraint>
    <constraint>The output must be in English.</constraint>
    <constraint>Don't write the full text in one file. The text contents should be saved per section / subsection basis in Latex format.</constraint>
    <constraint>Save the text contents in the Contents/text directory. if new section or chapter, create a director to save the text file</constraint>
    <constraint>Save the code contents in the Contents/code directory. if new section or chapter, create a director to save the file</constraint>
    <constraint>Save the images in the Contents/images directory. if new section or chapter, create a director to save the file</constraint> 
    <constraint>The plan and workthroug must be in Markdown format and must be saved in Workthrough directory witth chapter/section name</constraint>
    </technical_constraints>

    <rules_of_engagement>
        <constraint>NO HALLUCINATIONS: If an internal API is not in context, state "API_UNKNOWN".</constraint>
        <constraint>STYLE: Strict adherence to Google-internal style guides and Repo-specific patterns.</constraint>
        <constraint>TYPES: Mandatory strict typing. No 'any' or 'interface{}'.</constraint>
    </rules_of_engagement>
</instruction_set>

# Gemini Instructions for FunctionalProgramingWithPython

As an AI assistant working on this project, adhere strictly to the following organizational rules and workflows.

## Directory and File Organization Rules

1. **Top-Level Structure:**
   - `Contents/`: Contains all the actual book content (text, code, images).
   - `Draft/`: Contains markdown drafts, proposals, and feedback files.
   - `Workthrough/`: Contains detailed plans and breakdowns for each chapter/section in Markdown format.

2. **Content Separation (`Contents/text`):**
   - The root LaTeX document must be `Contents/text/main.tex`. This file acts *only* as the top-level aggregator (compiling `\tableofcontents` and using `\include{}`).
   - **Do not** write full chapter text inside `main.tex`.
   - Every chapter must have its own directory under `Contents/text/`, organized by chapter number and name (e.g., `Contents/text/chapter1_introduction/`).
   - The core text file for a chapter within its directory should be named specifically to avoid confusion, prioritizing `chapterX_main.tex` (e.g., `Contents/text/chapter1_introduction/chapter1_main.tex`). *Never name it just `main.tex`.*
   - If a chapter has multiple distinct sections, split them further into separate `.tex` files and `\input{}` them into the `chapterX_main.tex`.

3. **Code Separation (`Contents/code`):**
   - Save all code snippets in the `Contents/code/` directory, separated by language:
     - `Contents/code/python/chapterX/`
     - `Contents/code/haskel/chapterX/`
   - Use LaTeX's `\lstinputlisting` to display code directly from these source files rather than pasting code blocks directly into the `.tex` files.

4. **Image Separation (`Contents/images`):**
   - Save all figures and diagrams in `Contents/images/chapterX/`.

## Writing Constraints
- **Language:** The output must exclusively be in English.
- **Format:** The final textbook text must exclusively be in LaTeX format. Do not use Markdown for textbook content.
- **Reference Code:** Code snippets must use strict typing (e.g., Python Type Hints, Haskell Type Signatures). No `Any` typing.

By strictly segregating the markup text, the Python code, the Haskell code, and the images, we ensure the project remains cleanly decoupled and easily compilable.

## Developer Pitfalls (Known Failures to Avoid)

### 1. No Unicode / Non-ASCII Characters in Code Files

**Symptom:** `pdflatex` throws `! LaTeX Error: Invalid UTF-8 byte sequence` when processing a file included via `\lstinputlisting`.

**Cause:** The `listings` package reads code files as raw byte streams. It cannot render Unicode characters (such as `λ`, `→`, `∀`, etc.) when using `pdflatex`.

**Fix:**
- All files under `Contents/code/` must contain **ASCII-only** characters.
- To display a special mathematical symbol in the text, write it in the `.tex` file using LaTeX math mode (e.g., `$\lambda$`, `$\rightarrow$`), **not** inside the code file itself.

```
# WRONG (inside a .py or .hs code file):
# -- looks like a lambda 'λ'

# CORRECT (ASCII only inside code files):
# -- looks like a lambda 'lambda'
# And in the .tex narrative text: $\lambda$
```

---

### 2. No Markdown Syntax Inside `.tex` Files

**Symptom:** `pdflatex` fails or renders incorrectly when encountering Markdown formatting inside a `.tex` file.

**Cause:** LaTeX and Markdown are entirely different markup languages. Characters like `**`, `` ` ``, `*`, and `"` have different or no meaning in LaTeX.

**Fix:** Always use proper LaTeX equivalents inside `.tex` files:

| Markdown (WRONG in `.tex`) | LaTeX (CORRECT) |
|---|---|
| `**bold text**` | `\textbf{bold text}` |
| `` `inline code` `` | `\texttt{inline code}` or `\verb\|inline code\|` |
| `*italic text*` | `\textit{italic text}` |
| `"double quotes"` | ` ``double quotes'' ` |

