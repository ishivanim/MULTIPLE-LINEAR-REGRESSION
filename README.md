# Multiple Linear Regression with PCA - Student Performance Dataset

## Project Overview

    This project showcases a multiple linear regression model built from scratch to analyze and predict student performance. The dataset includes a variety of features related to students' academic and personal backgrounds. To incorporate all relevant features and reduce dimensionality, Principal Component Analysis (PCA) was applied.

## Dataset

    ### Source: Student performance dataset

    ### Features: Various academic and socio-demographic attributes

    ### Target: Final performance/grades of students

## Implementation Steps

    Data Preprocessing

    Cleaned and prepared the dataset for modeling.

    Applied Principal Component Analysis (PCA) to reduce dimensions and capture maximum variance.

    Model Development

    Wrote the multiple linear regression model from scratch.

    Split the dataset into training and testing sets using train_test_split from scikit-learn.

    Model Evaluation

    Evaluated the model using:

    R² Score: To assess the goodness of fit.

    Mean Squared Error (MSE): To evaluate prediction accuracy.

## Results

    Demonstrated the relationship between multiple features and student performance.

    The PCA helped improve performance and reduce redundancy.

    The metrics provided insight into the model's effectiveness.

## How to Run

    # Clone the repository
        git clone <repo-url>
        cd <repo-folder>

## Run the script (replace with your filename)
    python multiple_linear_regression.py

## Dependencies

    pip install numpy pandas matplotlib scikit-learn

## Concepts Used

    Multiple Linear Regression

    Principal Component Analysis (PCA)

    Model Evaluation Metrics (R² Score, MSE)

    Data Splitting with train_test_split

## Author

    Shivani Lange

## License

    This project is open-source and available for modification and reuse.

