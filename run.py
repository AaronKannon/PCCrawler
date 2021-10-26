import core.interface as run
import core.constants as const

def main():
    try:
        for site in const.URLS:
            run.crawl_one_site(site)
    except Exception as e:
        if 'in PATH' in str(e):
            print(
                'You are trying to run the bot from command line \n'
                'Please add to PATH your Selenium Drivers \n'
                'Windows: \n'
                '   set PATH=%PATH%;C:path-to-your-folder \n \n'
                'Linux: \n'
                '   PATH=$PATH:C:/path/toyour/folder/ \n'
            )
        else:
            raise



if __name__ == '__main__':
    main()
