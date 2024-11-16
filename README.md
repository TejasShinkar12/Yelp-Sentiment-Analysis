<p align="center"><h1 align="center">YELP-SENTIMENT-ANALYSIS</h1></p>
<p align="center">
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/TejasShinkar12/Yelp-Sentiment-Analysis?style=flat&logo=opensourceinitiative&logoColor=white&color=24bcc9" alt="license">
	<img src="https://img.shields.io/github/last-commit/TejasShinkar12/Yelp-Sentiment-Analysis?style=flat&logo=git&logoColor=white&color=24bcc9" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/TejasShinkar12/Yelp-Sentiment-Analysis?style=flat&color=24bcc9" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/TejasShinkar12/Yelp-Sentiment-Analysis?style=flat&color=24bcc9" alt="repo-language-count">
</p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
	<img src="https://img.shields.io/badge/sklearn-F7931E.svg?style=flat&logo=scikitlearn&logoColor=white" alt="sklearn">
	<img src="https://img.shields.io/badge/keras-D00000.svg?style=flat&logo=Keras&logoColor=white" alt="keras">
	</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

This focuses on performing sentiment analysis on Yelp reviews and building a predictive model for review ratings. The objective is to analyze the sentiment of customer reviews, categorize them as positive or negative, and predict review ratings (high or low). It leverages natural language processing (NLP) techniques, such as tokenization, text preprocessing, and sentiment analysis, to extract valuable insights from text data.

Sentiment analysis is initially performed using the TextBlob package, which provides a sentiment polarity score for each review. A Naive Bayes model is then trained using the IMDB movie review dataset, which is applied to the Yelp reviews for sentiment classification. The model's accuracy in predicting the sentiment of Yelp reviews is evaluated and compared against the actual ratings.

---

## 👾 Features

<details open>
<summary> 🧹 Data Cleaning & Preprocessing: </summary> 
Loads and preprocesses the Yelp dataset by selecting relevant columns (text and review_stars). Adds a new high_low column to categorize reviews into high ratings (>=4 stars) and low ratings (<4 stars). Cleans the text column by removing punctuation, converting to lowercase, and replacing newline characters.

</details>
<br>
<details open>
<summary> 📊 Sentiment Analysis with TextBlob: </summary> 
    Utilizes TextBlob to calculate a sentiment polarity score for each review.
    The polarity score ranges from -1 (negative sentiment) to +1 (positive sentiment), with the score being stored in a new column textblob_sentiment.

</details>
<br>
<details open>
<summary> 🌥️ Visualization of Frequent Words: </summary> 
Generates word clouds for both high and low-rated reviews to visually represent the most frequent words in each category.
Word clouds help in understanding the common themes and sentiments associated with reviews.
</details>
<br>
<details open>
<summary> 🤖 Model Training with IMDB Dataset: </summary> 
Trains a Naive Bayes classifier on the IMDB dataset, using TfidfVectorizer for text vectorization.
The model is evaluated on the IMDB test set, achieving an accuracy of 83.93%.
</details>
<br>
<details open>
<summary> 🧠 Application of the Trained Model on Yelp Data: </summary> 
Applies the trained Naive Bayes model to predict the sentiment of Yelp reviews based on the text.
Compares the model’s predictions with the high_low ratings column to evaluate model performance.
Achieves a sentiment prediction accuracy of 79.2% on Yelp reviews.
</details>
<br>
<details open>
<summary> 📈 Evaluation of Sentiment Accuracy: </summary> 
The accuracy of the model’s sentiment predictions is compared with the actual ratings (high_low) to assess its performance.
The model achieves an accuracy of 79.2% in predicting the sentiment of Yelp reviews, showcasing the model's effectiveness on real-world review data.
</details>

---

## 📷 Visualizations
### Topic Modeling Results: Topic Distribution and Term Relevance
![Topic Modeling](https://kappa.lol/N8ENP)

### Low rating word cloud
![alt text](https://kappa.lol/59PW_)

### High rating word cloud
![alt text](https://kappa.lol/w6klh)
---

## 📁 Project Structure

```sh
└── Yelp-Sentiment-Analysis/
    ├── LICENSE
    ├── Notebooks
    │   ├── .ipynb_checkpoints
    │   ├── Data Preprocessing.ipynb
    │   ├── Natural Language Processing.ipynb
    │   └── Sentiment_Analysis_and_Model_Building.ipynb
    ├── README.md
    └── yelp_dataset
        ├── Dataset_User_Agreement.pdf
        ├── yelp_data.csv
        └── yelp_data_cleaned.csv
```

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/TejasShinkar12/Yelp-Sentiment-Analysis/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/TejasShinkar12/Yelp-Sentiment-Analysis/issues)**: Submit bugs found or log feature requests for the `Yelp-Sentiment-Analysis` project.
- **💡 [Submit Pull Requests]()**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/TejasShinkar12/Yelp-Sentiment-Analysis
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/TejasShinkar12/Yelp-Sentiment-Analysis/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=TejasShinkar12/Yelp-Sentiment-Analysis">
   </a>
</p>
</details>

---

## ⌛Dataset
- [Yelp Dataset](https://www.yelp.com/dataset) – The valuable Yelp dataset, which formed the foundation for the analysis and model-building process.
---

## 🎗 License

This project is protected under the [MIT](https://github.com/TejasShinkar12/Yelp-Sentiment-Analysis?tab=MIT-1-ov-file#readme) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.


---

## 🙌 Acknowledgments

- [YouTube](https://youtu.be/dowagyrMtnU) - This video by [Alex Teboul](https://www.youtube.com/@acteboul17) which inspired and guided me for this project

---
