import requests
import re
import warnings
import os
import shutil #importer module
import time
print()
print("                       I N I S I A T I N G  S Y S T E M   D O W N L O A D E R")
print("                       ------------------------------------")
time.sleep(0.3)
print("                       Checking system resources ..........")
time.sleep(0.3)
print("                       Starting all the services .........")
time.sleep(0.3)
print("                       Getting IP Address - 192.168.0.129 ")
time.sleep(0.3)
print("                       Connecting to the website ..........")
time.sleep(0.3)
print("                       Getting user profile ..........")
time.sleep(0.3)
print("                       Connecting to the Server ..........")
time.sleep(0.3)
print("                       All Set! System downloader completed.")
time.sleep(0.3)
print("                       Launching the scraper now ..........")
time.sleep(0.5)
print()
print("                  ...... W E L C O M E     G E N I U S ......")
print("                  -------------------------------------------    ")
time.sleep(4)
warnings.filterwarnings("ignore")  # ignore SSL cert errors
MAIN_URL = "https://exampapers.must.ac.ke/"

def getLogger():
    import logging
    logger = logging.getLogger()
    handler2 = logging.StreamHandler()
    handler2.setLevel(logging.CRITICAL)
    FORMAT = logging.Formatter(style='{', fmt="{message}", )
    handler2.setFormatter(FORMAT)
    logger.addHandler(handler2)
    logger.critical('--START--\n2 many requests @ the same time may be perceived as ddos.')
    return logger


def get_all_urls():
    return requests.get(MAIN_URL, verify=False).text.split("et-top-navigation")[1].replace("\n", '')


def get_school():
    len_ = len(schs)
    [print(s, '.' * 3, id.upper(), sep='') for (s, id) in enumerate(schs)]
    schs_selected = []
    print("Select your  school(1 or more school can be selected,,,and should be SPACE  separated VALUES,,++++,,:")
  
    try:
        sch = input("school index: ").split(' ')
        # index_sch=sch.split(' ')
        index_int= [int(index) for index in sch]
        # print(f'{schs[index_int[0]]}  and {schs[index_int[1]]} selected')    
        
        for sch_index in index_int:
            print(f'{index_int}:{schs[sch_index].upper()} selected')
                
            if sch in index_int:  
                break 

            try:
                school_idx = sch_index
                if 0 <= school_idx < len_:
                    schs_selected.append(schs[school_idx])                
            except ValueError:
                        print("OYAH OYAH,,,,,ERROR WRITING FILES")
    except ValueError:
            print("OYAH OYAH,,,,, an Invalid input. Please enter a valid school index. OR an Integer.")
    return schs_selected

def get_year_urls(sch: str, years: list):
    pattern = re.escape(f'<a href="#">{sch.upper()}</a>') + "(.+?)</ul>"
    if sch == 'tvet':  # Adjust for 'tvet' if needed
        pattern = pattern.replace(r"\#", MAIN_URL + sch + "/")
    content = get_all_urls()
    content = re.search(pattern, content).group(1)
    content = [d.split('">') for d in re.findall('(?:href="(.+?)</a>)', content)]

    content_filtered = []
    for item in content:
        for year in years:
            if year in item[0]:
                content_filtered.append(item)
                break
    return content_filtered


def make_dirs(sch, urls: list):
    exams = os.path.join(os.getcwd(), "exams")
    schd = os.path.join(exams, sch)
    for dir_ in (exams, schd):
        try:
            os.mkdir(dir_)
        except OSError:
            if input(f"path {dir_} exists. reuse it? ('y','n') ") == 'n':
                shutil.rmtree(dir_)
                os.mkdir(dir_)
                logger.critical(f"CLEARED {dir_}")
    for url in urls:
        url[1] = re.sub(r"\ ", "_", url[1])
        try:
            os.mkdir(os.path.join(schd, url[1]))
        except OSError:
            pass
    return schd

def keep_existing(fnames:list,path_:str)->None:
    names=os.listdir(path_)
    for x in range(len(fnames)-1,-1,-1):
        name=fnames[x]
        if name[1] in names: 
            fnames.remove(name)
            logger.critical(f"\tfile {name[1]} exists, not downloaded")              

def write_file(x):
    path_, url = x
    try:
        with open(os.path.join(path_, url[1]), "wb") as wrt:
            wrt.write(requests.get(url[0], verify=False).content)
            logger.critical(f"\twrote '{url[1]}'")
    except Exception as e:
        print("\n" * 10, "ERROR", e)


def get_file_names(url: str, target_patterns: list, years: list) -> list:
    # Fetch the content from the URL
    content = requests.get(url, verify=False).text.replace("\n", '')
    
    # Use a regular expression to extract the relevant content
    if match := re.search(r'<div\ class="entry\-content">(.+?)</div', content):
        content = match.group(1)
        
        # Extract URLs from the content and create a list of tuples
        urls = [(d, d.split('/')[-1].replace(" ", "_")) for d in re.findall(r'(?:<p><a\ href=")(.+?)(?:")', content)]
        
        # Filter the URLs based on target patterns and year
        filtered_urls = []
        for url in urls:
            #print(url) Prints all the URLS 
            for pattern in target_patterns:
                
                for year in years:
                    
                    if pattern in url[0] and year in url[0]:
                        filtered_urls.append(url)
                        break
        return filtered_urls if filtered_urls else None
    else:
        return None


def download(path_, urls, target_patterns, years, tpool):
    files = 0
    for url in urls:
        path = os.path.join(path_, url[1])
    
        # Pass the year parameter to get_file_names
        todo = get_file_names(url[0], target_patterns, years)
        
        if todo:
            keep_existing(todo, path)
            logger.critical(f"downloading {url[0]}...")
            tpool.map(write_file, zip(itertools.cycle((path,)), todo))
            files += len(todo)
        else:
            logger.critical(f"No files on {url[0]}")
    return files


if __name__ == "__main__":
    import time,itertools
    from concurrent.futures import ThreadPoolExecutor
    THREAD_C = 32
    executor = ThreadPoolExecutor(max_workers=THREAD_C)
    schs = ['safs', 'sbe', 'sci', 'sea', 'sed', 'shs', 'son', 'spas', 'tvet']
    logger = getLogger()
    logger.critical(f"USING {THREAD_C} threads\n")

    selected_schools = get_school() 
    if selected_schools:   
        files_names=input("Enter the unit code(s) (e.g SMA-3300): ").split()
        target_patterns=[file.upper() for file in files_names]
      
        for file in target_patterns:
            print(f'{file} selected')  
        years_input = input("Enter the year(s)  or 'all' for all years): ").strip() 
        years = years_input.split(" ") if years_input.lower() != 'all' else ["2014", "2015", "2016", "2017", "2018","2019", "2020", "2021", "2022", "2023", "2024"]  # Change the list of years as per your requirement      
        for school in selected_schools:
            timer = time.perf_counter()
            logger.critical(f"\nDownloading exams for {school.upper()} .......")
            urls = get_year_urls(school, years)
            pdir = make_dirs(school, urls)            
            files = download(pdir, urls, target_patterns,years, executor)        
        executor.shutdown(wait=True)
        logger.critical(f"\n{'+' * 3} DONE {'+' * 3} took: {(time.perf_counter() - timer):.2f}s wrote {files} files")

#BBS-3475 CCS-3325 CIT-3476 SMA-3400 SMA-3404 SMA-3405

