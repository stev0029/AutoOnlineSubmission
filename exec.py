import scrapers
import solution
import submission_session as sess

sess.login('stev0029', 'stev0029')
main_page = sess.main_page()

for problemNo in scrapers.get_all_problemNo(main_page):
    problem_page = sess.problem_page(problemNo)
    class_name = scrapers.get_class_name(problem_page)

    replacement_table = solution.replacement_table(problem_page)
    source_name, source_path = solution.make(class_name, replacement_table)
    
    # Submit
    token = scrapers.get_token(problem_page)
    submission_id = sess.upload_submission(problemNo, token, source_name, source_path)

    print(submission_id)

sess.logout()