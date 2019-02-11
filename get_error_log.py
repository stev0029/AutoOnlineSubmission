import submission_session as sess
import scrapers

sess.login('stev0029', 'stev0029')
problem_page = sess.problem_page('9101')
token = scrapers.get_token(problem_page.text)

a = sess.change_email('\u0008@a.aa')
print(a.text)

# for i in range(100):
#     a = sess.upload_submission('9101', token, 'Add2Integers.java', 'out/Add2Integers.java')
#     print(a)

sess.logout()