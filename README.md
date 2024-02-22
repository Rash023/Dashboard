<h1 align="center" id="title">Social Media Dashboard</h1>

<p id="description">Social Media Dashboard - the ultimate tool for managing your online presence with ease and efficiency. Seamlessly draft and schedule your posts across multiple platforms all from one centralized hub. Stay on top of your performance with comprehensive analytics tracking likes shares and comments in real-time. With intuitive features and customizable options our Social Media Dashboard is designed to streamline your workflow boost productivity and elevate your social media strategy to new heights. Experience the power of simplified management and insightful analytics with our Social Media Dashboard today.</p>

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   **Drafting and Scheduling Posts:** Users can create and save posts in advance within the dashboard. Flexible scheduling options allow users to set specific dates and times for post publication. Support for multiple social media platforms including but not limited to Facebook Twitter Instagram LinkedIn and Pinterest.
*   **Analytics Dashboard:** Real-time tracking of key engagement metrics such as likes shares comments and overall reach. Customizable reports and visualizations to analyze performance trends over time. Insights into audience demographics.

<h2>🛠️ Installation Steps:</h2>

<p>1. Install the required libraries</p>

```
pip install -r requirements.txt
```

<p>2. Check if the DB is present/If not DB will be Configured</p>

```
python manage.py makemigrations
python manage.py migrate
```

<p>3. Start the App</p>

```
python manage.py runserver
```

## Usage

1. **Home Page**: Access the home page to navigate to different sections of the dashboard.

2. **Schedule Post**:
   - Navigate to the "Schedule Post" section.
   - Fill in the title and description of the post.
   - Click on the submit button to schedule the post.

3. **Analytics**:
   - Navigate to the "Analytics" section.
   - View analytics to track post performance metrics.

4. **Comments**:
   - Navigate to the "Comments" section.
   - Manage comments associated with posts.

5. **Reach**:
   - Navigate to the "Reach" section.
   - Analyze the reach of posts.

6. **User Authentication**:
   - Use the login form to log in with your credentials.
   - If you don't have an account, you can register using the registration form.


## Assumptions

- Each post is associated with an author (defaulted to "John Doe" if not specified).
- Post IDs are incremented based on the count of existing posts.
- User registration requires a unique username and a strong password.
- User authentication is necessary to access features of the dashboard.
  

## Contributing

Feel free to contribute to the development of this dashboard by submitting bug reports, feature requests, or pull requests.


<h2>💻 Built with</h2>

Technologies used in the project:

*   Django
*   Python
*   Plotly
*   Javascript
*   sqllite3
