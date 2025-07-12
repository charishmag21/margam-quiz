# Project Introduction

## What is this project?

This project is an **AI-powered pipeline for personalized learning and assessment,** built to turn any PDF textbook into a smart, adaptive learning experience.  
It leverages state-of-the-art Large Language Models (LLMs), such as Gemini, to **automatically generate:**
- A curriculum skeleton from the textbook
- High-quality, topic-aligned MCQ quizzes
- Personalized learning paths (with pacing and review zones)
- Custom, student-ready revision notes for each learner

**No manual annotation or curation required**—the pipeline does it all, starting from the raw PDF.

--------------------------------

## What is the output?

- **Auto-structured learning path:** A hierarchical curriculum, organized by chapters, subsections, and subtopics, extracted directly from your textbook.
- **Quiz bank:** A set of multiple-choice questions (MCQs) for every topic, mapped to relevant textbook content.
- **Personalized learning plan:** A recommended study schedule and review strategy, unique to each learner based on their quiz and aptitude results.
- **Adaptive study notes:** Paraphrased, revision-ready content for each topic, tailored to the learner’s pace and skill level.

All outputs are in **machine-readable JSON**—ready for web, app, or dashboard integration.

--------------------------------

## What phases are involved?

The solution is modular, with four major phases:

1. **Curriculum Extraction:**  
   Chunk the PDF and build a structured curriculum skeleton using the LLM.

2. **Quiz Generation & Assessment:**  
   Match curriculum topics to textbook content, generate MCQs, and assess user knowledge and speed.

3. **Personalized Learning Path Creation:**  
   Analyze quiz results to assign each user a “learning zone,” estimate time for each topic, and recommend a pacing strategy.

4. **Personalized Content Delivery:**  
   Paraphrase relevant textbook content for every topic, adapting style and depth to the learner’s needs—ensuring all topics are covered, never skipped.

--------------------------------

## Folder Structure Overview

This project uses a clear, modular folder structure to separate each phase of the pipeline and its outputs. Here’s what each folder is for:


### `files/`
**Contains:**  
Raw input PDFs (the textbooks or documents you want to process).

**Details:**  
- Place any new textbook or content PDF here to run it through the pipeline.
- Examples: `science-textbook-grade-5.pdf`, `mi-intro.pdf`, `sql.pdf`.

### `quiz_files/`
**Contains:**  
All quiz generation outputs—question banks and sampled quizzes.

**Details:**  
- `quiz_output_5th.json`: All MCQs generated for the 5th grade science PDF.
- `filtered_quiz_5th.json`: A sampled quiz (e.g., for a particular user test).
- Similarly named files for other documents or test scenarios.

### `path/`
**Contains:**  
All learning path structures, both generic and user-personalized.

**Details:**  
- `learning_path_skeleton_5th.json`: The initial, auto-generated curriculum structure for grade 5 science.
- `learning_path_personalized_5th.json`: The path tailored to a specific user (with pacing and review recommendations).
- Other skeleton and personalized path files for different content domains (SQL, ML, etc).


### `content/`
**Contains:**  
Personalized study notes for learners, generated for each user zone and scenario.

**Details:**  
- Files like `personalized_content_plan_5th.json` contain all the revision notes for the 5th grade science PDF, adapted to the specific user’s learning zone (e.g., fast-learner, advanced).
- Additional files (e.g., `personalized_content_plan_advanced.json`) are alternate plans for different user profiles or demo scenarios.


### Root Directory
- **Notebooks:**  
  - `content.ipynb`, `path.ipynb`, `quiz.ipynb`, `test_langraph.ipynb`:  
    Jupyter notebooks for each phase of the pipeline (content generation, learning path, quiz, testing).
- **Config/Secrets:**  
  - `api_key_paid.txt`: Stores your Gemini API key (private—never commit this to public repos!).

## Notebooks Overview

Each notebook in this project corresponds to a key stage in the pipeline.  
You can run these step-by-step, or use them for experimentation and debugging.

### `test_langraph.ipynb`
**Purpose:**  
- **Experiments, Testing, and Pipeline Prototyping**
- Used for quick prototyping, testing new features, and exploring different chunking or LLM strategies.
- Not required for core pipeline, but useful for development and debugging.


### `quiz.ipynb`
**Purpose:**  
- **Quiz Generation and User Assessment**
- Maps each topic in the curriculum to its most relevant chunk(s) of textbook content.
- Uses Gemini to generate MCQs for each topic.
- Samples or simulates quiz results to estimate learner’s strengths and weaknesses.
- Outputs: Question bank and sampled/simulated quiz results.


### `path.ipynb`
**Purpose:**  
- **Curriculum Extraction and Learning Path Planning**
- Chunks the input PDF and builds the curriculum skeleton (hierarchical structure of chapters, sections, and topics).
- Assigns “pace” (estimated study time) and “review needed” flags to each topic, based on user’s quiz/aptitude results.
- Outputs: Curriculum skeleton and personalized learning path as JSON.


### `content.ipynb`
**Purpose:**  
- **Personalized Content Delivery**
- For each topic in the learning path, finds the matching textbook content.
- Uses the LLM to paraphrase and adapt the explanation style according to the learner’s “user zone” (fast/slow, beginner/advanced).
- Generates the full set of revision-ready notes, tailored to the user.
- Outputs: `personalized_content_plan_5th.json` and similar files.


> **Tip:**  
Run the notebooks in the order: `test_langraph.ipynb` -> `quiz.ipynb` -> `path.ipynb` -> `content.ipynb`


## Technologies & Frameworks Used

This project brings together powerful modern tools for document processing, natural language understanding, and rapid prototyping. Here’s what powers the pipeline:


### Language Models (LLMs)
- **Google Gemini (Generative AI via LangChain)**
  - Used for curriculum extraction, quiz/question generation, topic classification, and paraphrasing personalized study notes.


### Orchestration and Pipelines
- **LangChain**
  - Orchestrates complex multi-step language model workflows and chains.
  - Supports prompt templates, parsing, and output management.
- **LangGraph**
  - Used for defining and running more complex, stateful workflows (for prototyping or future scalability).

### Project & API Management
- **LangSmith**
  - For tracking and tracing LLM runs and experiments.
- **API Key Management**
  - Sensitive keys are loaded from file, not hard-coded, for basic security.


### Document Processing
- **PyMuPDF (via `langchain_community.document_loaders.PyMuPDFLoader`)**
  - Loads and extracts text from PDF files.
  - Enables chunking and content matching.


### Data Science & Utilities
- **Pandas**
  - For tabular data manipulation, summaries, and analysis of learning paths or quiz results.
- **Python Standard Libraries**
  - `os`, `json`, `re`, `concurrent.futures`, `random`, `collections`, `typing`
  - Used for environment/config handling, fuzzy text matching, multi-threading, and utility functions.


### Interactive Development
- **Jupyter Notebooks**
  - Each phase of the pipeline is implemented as a notebook for easy experimentation, parameter tuning, and debugging.
- **Markdown**
  - For documentation and code annotation.


##  How to Run the Pipeline

You can process any PDF textbook from start to finish in four main steps, using the provided Jupyter notebooks.  
Each notebook corresponds to a phase in the pipeline and produces outputs for the next phase.


### 1. Prepare Your Input

- Place your input PDF(s) in the `files/` directory (e.g., `files/science-textbook-grade-5.pdf`).
- Make sure you have your Gemini API key in `api_key_paid.txt` (never commit this file to public repos).


### 2. Step 1: Curriculum Extraction

**Notebook:** `test_langraph.ipynb`  
- This notebook will:
  - Chunk your PDF into small sections.
  - Use the LLM to generate a curriculum skeleton (chapters, sections, topics).
  - Output: `path/learning_path_skeleton_*.json`


### 3. Step 2: Quiz Generation & User Assessment

**Notebook:** `quiz.ipynb`  
- This notebook will:
  - Map each topic in the curriculum to its matching textbook chunk(s).
  - Generate MCQs for every topic using the LLM.
  - Optionally, simulate or record a user’s quiz answers.
  - Output: `quiz_files/quiz_output_*.json` and `quiz_files/filtered_quiz_*.json`


### 4. Step 3: Personalized Learning Path Creation

**Notebook:** `path.ipynb` (continued)  
- This notebook will:
  - Use the quiz results and user aptitude to assign a learning zone (e.g., fast-learner, advanced).
  - Estimate study pace for every topic, and flag areas needing review.
  - Output: `path/learning_path_personalized_*.json`


### 5. Step 4: Personalized Content Delivery

**Notebook:** `content.ipynb`  
- This notebook will:
  - For each topic, match the most relevant PDF content.
  - Use the LLM to paraphrase and adapt content to the user’s zone and topic difficulty.
  - Generate fully personalized, revision-ready study notes for the learner.
  - Output: `content/personalized_content_plan_*.json`


### 6. Inspect the Outputs

- Each phase outputs easy-to-use JSON files in their respective folders (`path/`, `quiz_files/`, `content/`).
- These outputs can be used directly in web apps, dashboards, or for review.



**That’s it! Add your PDFs, follow the notebooks, and your personalized AI learning content is ready!**
