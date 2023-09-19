from limesurveyrc2api.limesurvey import LimeSurvey

url = "https://pb.utfpr.edu.br/geppadem/alimentario/index.php/admin/remotecontrol"
username = "ppgdr-pb@utfpr.edu.br"
password = "5MnVpxad273a"

# Open a session.
api = LimeSurvey(url=url, username=username)
api.open(password=password)

# Get a list of surveys the admin can see, and print their IDs.
result = api.survey.list_surveys()
for survey in result:
    print(survey.get("sid"))

# Close the session.
api.close()