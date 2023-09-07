# Pride and Prejudice Text Analysis

## Description

In this project, we create a script to analyze the text of the novel "Pride and Prejudice" by Jane Austen, which can be downloaded as a plain text file from [Project Gutenberg](https://www.gutenberg.org/ebooks/1342). The script produces various statistics about the book, including:

- Total word count
- Total character count
- Average word length
- Average sentence length
- Word distribution with frequency counts of all words
- Top 10 longest words

Additionally, we create a word cloud visualization of the top 200 words in "Pride and Prejudice" using the open-source `wordcloud` module.

### Data Preparation

Before analysis, it's essential to note that Project Gutenberg e-books contain additional text at the beginning and end, such as licensing information, which is not part of the book itself. We'll remove this extra text from our copy of the book before analysis.

### Word Cloud Visualization

We'll use the `wordcloud` module's `WordCloud` class to create and configure a word cloud visualization. The top 200 words in "Pride and Prejudice" will be visualized in a word cloud. You can find the `wordcloud` module [here](https://github.com/amueller/word_cloud).

## Usage

1. Download the text-file version of "Pride and Prejudice" from [Project Gutenberg](https://www.gutenberg.org/ebooks/1342).

2. Run the script to perform the following tasks:
   - Calculate word and character counts.
   - Determine average word and sentence lengths.
   - Generate word frequency counts and list the top 10 longest words.
   - Create a word cloud visualization of the top 200 words in "Pride and Prejudice."

3. Review the results to gain insights into the text of the novel.
