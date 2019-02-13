import scrapers
import solution
import submission_session as sess

sess.login('stev0029', 'stev0029')
main_page = sess.main_page()

for problemNo in scrapers.get_all_problemNo(main_page):
    # Using the problem page to scrape required `class_name` and `case_outputs`
    problem_page = sess.problem_page(problemNo)
    class_name = scrapers.get_class_name(problem_page)
    case_outputs = scrapers.get_outputs(problem_page)

    # Make the solution file
    source_name, source_path = solution.make(class_name, case_outputs)

    # Submit
    token = scrapers.get_token(problem_page)
    submission_id = sess.upload_submission(problemNo, token,
                                           source_name, source_path)

    print(submission_id)

sess.logout()
