from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from gooey import Gooey, GooeyParser


def download_content(name_list, geckopath):
    """
    Function takes a list of words and downloads random pretty gifs of the words from 
    https://textanim.com/

    """

    caps = DesiredCapabilities().FIREFOX.copy()
    caps["pageLoadStrategy"] = "eager"  ##  interactive

    browser = webdriver.Firefox(
        desired_capabilities=caps, executable_path=geckopath
    )
    browser.get("https://textanim.com/")

    search_form = browser.find_element_by_id("p0")
    # generate = browser.find_element_by_xpath("/html/body/center[2]/div/div[3]/span/div[2]/a")

    if isinstance(name_list, str):
        texture = "icone{}".format(randint(0, 387))
        search_form.clear()
        search_form.send_keys(name_list)
        browser.implicitly_wait(30)
        browser.implicitly_wait(2)
        WebDriverWait(browser, 1000000).until(
            EC.element_to_be_clickable((By.ID, texture))
        ).click()

        WebDriverWait(browser, 1000000).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/center[2]/div/div[3]/span/div[2]/a")
            )
        ).click()

        WebDriverWait(browser, 1000000).until(
            EC.element_to_be_clickable(
                (By.XPATH, "/html/body/center[1]/div[1]/span/a[1] ")
            )
        ).click()
        browser.implicitly_wait(10)
    else:
        for value in name_list:
            texture = "icone{}".format(randint(0, 387))

            search_form.clear()
            search_form.send_keys(value)

            browser.implicitly_wait(2)
            browser.implicitly_wait(30)

            WebDriverWait(browser, 1000000).until(
                EC.element_to_be_clickable((By.ID, texture))
            ).click()
            font_selection = "/html/body/center[2]/div/div[2]/table/tbody/tr[1]/td[1]/form/div[3]/select/option[{}]".format(randint(1,36))
 
            WebDriverWait(browser, 1000000).until(
                EC.element_to_be_clickable(
                    (By.XPATH, font_selection)
                )
            ).click()

            WebDriverWait(browser, 1000000).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/center[2]/div/div[3]/span/div[2]/a")
                )
            ).click()

            WebDriverWait(browser, 1000000).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/center[1]/div[1]/span/a[1] ")
                )
            ).click()

    browser.close()
    # quit()



@Gooey(
    program_name="NENE Word Art",
    default_size=[600, 600],
    image_dir='./images',
    menu=[{
        'name': 'About',
        'items': [{
                'type': 'AboutDialog',
                'menuTitle': 'About Us',
                'name': 'NENE Word Art',
                'description': 'Simple interface to make batch colored gifs based on https://textanim.com/ ',
                'version': '1.0',
                'copyright': '2020',
                'website': 'http://marijani.rf.gd',
                'developer': 'marijani101',
                'license': 'CC-BY'
            },{
                'type': 'MessageDialog',
                'menuTitle': 'Critical Information',
                'caption': 'Dont forget to download firefox web driver',
                'message': 'The program works using firefox geckodriver. if it doesnt start or spits out random erros, make sure u have installed firefox gecko at C:\geckodriver\geckodriver.exe '
            }]
        }]
)
    

def main():
    settings_msg = "Tool for creating and downloading text word art"
    parser = GooeyParser(description=settings_msg)
    subs = parser.add_subparsers(help="commands", dest="command")
    curl_parser = subs.add_parser(
        "curl", help="curl is a tool to transfer data from or to a server"
    )
    curl_parser.add_argument('Path',
                             help='Path to GeckoDriver',
                             type=str, widget='FileChooser', default = r"C:\geckodriver\geckodriver.exe")
    verbosity = curl_parser.add_mutually_exclusive_group()

    verbosity.add_argument(
        "--Word", help="Convert Word to Word-Art", default="karibu tanzania"
    )
    verbosity.add_argument(
        "--Textfile",
        help="Text File containing list of words",
        type=str,
        widget="FileChooser",
    )
    args = parser.parse_args()

    wordlist = []

    if args.Textfile:
        f = open(args.Textfile, "r")
        for x in f:
            x = x.rstrip()
            wordlist.append(x)
        print(wordlist)
        download_content(wordlist)
    elif args.Word:
        download_content(args.Word, args.Path)
    print("The word {} has been created".format(args.Word))
    print("The image has been downloaded in your downloads folder")


if __name__ == "__main__":
    main()
