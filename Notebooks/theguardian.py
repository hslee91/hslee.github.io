import os
import re
import csv
import signal
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def TheGuardian(url, article):
    """The Guardian scraping script
    Returns the title, data, content and comments in csv file
    """
    path = os.getcwd()
    print path

    # Create new instance
    browser = webdriver.PhantomJS(executable_path="{}/phantomjs-2.1.1-macosx/bin/phantomjs".format(path))

    # Go to website
    count = 5
    timeout = 20
    while count > 0:
        browser.get(url)
        count -= 1
        try:
            print "Trying to connect to the webpage"
            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '//div[@class="meta__numbers"]')))
        except TimeoutException:
            print "Timed out waiting for page to load"
            browser.close()
            browser.quit()
        else:
            break

    print "Connected"

    soup = BeautifulSoup(browser.page_source, "lxml")
    headline_1 = soup.find_all("h1", {"class": "content__headline "})
    for item in headline_1:
        article_id = (item.text).strip("\n").encode("utf-8")

    if len(headline_1) == 0:
        headline_2 = soup.find_all("h1", {"articleprop": "headline"})
        for item in headline_2:
            article_id = (item.text).encode("utf-8")

    text = ""
    content = soup.find_all("p")
    for item in content:
        if re.search("\s*...we have a small favour to ask", item.text, re.MULTILINE):
            break
        else:
            text = text + item.text

    article_date = (re.search("\w{3}\s\d+\s\w{3}\s\d+", text)).group(0)
    article_content = (" ".join(text.split("\n")[-1:])).encode("utf-8")

    # Accessing one by one every comments page
    # Expand comments side

    comments_button = browser.find_element_by_xpath('//a[@data-link-name="Comment count"]')
    comments_button.click()
    dropdown = browser.find_element_by_xpath('//button[@data-toggle="popup--comments-threading"]')
    dropdown.click()
    expanded = browser.find_element_by_xpath('//button[@data-threading="expanded"]')
    expanded.click()
    WebDriverWait(browser, timeout).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                 '//span[@itemprop="givenName"]')))
    users = []
    comments = []
    pagination = 1
    next_page = True
    while next_page:
        try:
            pagination += 1

            # Retrieve users name
            # all_users = soup.find_all("span", {"itemprop": "givenName"})
            all_users = browser.find_elements_by_xpath('//div[@class="d-comment__meta"]/div/span[1]')
            for elem in all_users:
                users.append((elem.text).encode("utf-8"))

            # Retrieve all comments
            all_comments = browser.find_elements_by_xpath('//div[@class="d-comment__content"]')
            for elem in all_comments:
                comm = ("".join((elem.text).split("\n")[2:-4])).encode("utf-8")
                comments.append(comm)

            next_page = browser.find_element_by_xpath('//a[@data-page="{}"]'.format(pagination))
            next_page.click()
            WebDriverWait(browser, timeout).until(EC.visibility_of_all_elements_located((By.XPATH,
                                                                                         '//span[@itemprop="givenName"]')))
            print "STILL GETTING COMMENTS..."
        except Exception as e:
            next_page = False
    browser.close()
    browser.service.process.send_signal(signal.SIGTERM)
    browser.quit()

# Write to CSV
    csv_file = csv.writer(open('{}/TheGuardianArticle{}.csv'.format(path, article), 'w+'), delimiter="|")
    csv_file.writerow(['Article_ID', 'Article_DATE', 'Article_CONTENT', 'Comment_ID', 'Comment'])
    comment_nr = 0
    for elem in users:
        csv_file.writerow([article_id, article_date, article_content, elem, comments[comment_nr]])
        comment_nr += 1
        article_id = " "
        article_date = " "
        article_content = " "


if __name__ == '__main__':
    path = os.getcwd()
    # The file from which the script takes URLs.. Modify it as u please
    with open('{}/url_gur.txt'.format(path), 'r') as f:
        article = 0
        for line in f:
            article += 1
            TheGuardian(line, article)
