# Django Pie-chart app

## Tasks:
1. Get top 50 tags by popularity:
   <p>Used https://api.stackexchange.com/2.2/tags?order=desc&sort=popular&site=stackoverflow&pagesize=50 to retrieve the required tags and the total asked questions in each tags</p>
   
2. Get the percentage of total unanswered questions to total asked questions in each tag:
   <p>For each tag, used the queries like https://api.stackexchange.com/2.2/questions/unanswered?order=desc&sort=activity&tagged={tagname}&site=stackoverflow&filter=total (replacing tagname) to get unanswered questions and therby calculate the percentage</p>
   
3. All the data must be available in DB at all times:
   <p>Upon running the custom command `python manage.py refreshdb` all the data for 50 tags is bulk created or updated in the db in tags_tag table</p>
   
4. Show this data in a bar-graph or a pie-chart:
   <p>Pie chart is displayed on http://127.0.0.1:8000/tags/display/ when running the application locally</p>
   
## Steps to run locally:
1. Clone the repo `https://github.com/ranriy/stackoverflow.git`
2. `cd stackoverflow` (optional - create and activate a virtual environment)
3. Install the requirements `pip install -r requirements.txt`
4. (Not currently required) When changing database run `python manage.py migrate` to apply all migrations and create the tables.
5. Refresh the database values using `python manage.py refreshdb` to get the latest numbers. (Assumption - when required, a cron job can be scheduled to run this command twice a day)
6. Run the application `python manage.py runserver` and navigate to http://127.0.0.1:8000/tags/display/ to view the pie-chart


