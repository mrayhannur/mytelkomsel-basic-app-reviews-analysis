# MyTelkomsel Basic App Google Play Store (Bahasa) Reviews Analysis

## Background
A little background about this project, I was interested in working on this project because the company that owns this application is one of my dream places to work. As I write this, I am preparing this project as one of my portfolios to apply for an internship position at the company. Data was collected by scraping with the _google-play-scraper_ Python library, I aimed to explore the data while finding valuable insights from it. And then, I built a Dashboard using Tableau to make analysis easier.

## What is in my project
This project consist of 4 parts:
1) Scraping Data using  _google-play-scraper_ Python library
2) Preprocessing & Doing Exploration Data Analysis (EDA)
3) Build a Dashboard with Tableau

## Dataset
The data collected was almost 50k rows. The columns in the data include:
1. reviewId: A unique identifier assigned to each review.
2. userName: The name or alias of the user who submitted the review.
3. userImage: A URL or path to the profile image of the user.
4. content: The text of the review itself, containing the user's feedback, opinions, and experiences with the app.
5. scores: A numerical rating given by the user, typically on a scale (1 to 5 stars), reflecting their overall satisfaction with the app.
6. thumbsUpCount: The number of users who found the review helpful or positive, indicating its perceived value to the community.
7. reviewCreatedVersion: The version of the app at the time the review was written, which helps contextualize the feedback based on app updates.
8. at: The timestamp indicating when the review was submitted, providing a chronological context for the feedback.
9. appVersion: The specific version of the app that the user reviewed, which can be important for understanding issues related to particular updates.

## Insights
1. The **average score/rating is 2.57**, with a **Positive Score Rate (values ​​4 & 5) only 36.65%**, indicating that most users give unsatisfactory ratings.
2. The distribution of the number of ratings collected shows that the values ​​1 and 5 dominate, while the rest are relatively few, indicating a **polarization in the user experience**.
3. The app version with the highest average was 3.0.2, which scored 4.29, higher than the current version (3.1.0) which only scored 3.15.
4. The average monthly score trend fluctuates, while the trend in the number of reviews obtained tends to be stable, reflecting uncertainty in user satisfaction even though interest in the application remains consistent.

## Tableau Dashboard
All the insights can be viewed ![here](https://public.tableau.com/shared/WCNDRNN8M?:display_count=n&:origin=viz_share_link)
![alt text](https://github.com/mrayhannur/mytelkomsel-basic-app-reviews-analysis/blob/main/screenshot%20dashboard%20tableau.png)

## Things Can Be Improved
Explore the data further using Machine Learning.
