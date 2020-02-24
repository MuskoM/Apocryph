import wget
import requests
import tempfile
import os
import PyPDF2
from bs4 import BeautifulSoup
from pdf2image import convert_from_path


class PlanScraperForApocryph:
    """
    A custom class for scraping data from university site
    """
    def __init__(self):
        self.url = 'https://degra.wi.pb.edu.pl/rozklady/rozklad.php?page=st'
        self.download_path = 'Plans/plan.pdf'
        self.save_path = 'Plans/PlanJPGS'

    def get_plan(self):
        """
        Converts the downloaded pdf containing a plan to JPG and saves it in Plans/PlanJPGS
        :return: None
        """
        wget.download('https://degra.wi.pb.edu.pl/rozklady/doc/isi4.pdf?id=1661694339126998006', self.download_path)
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(self.download_path, output_file=path, last_page=1,first_page=0)

        base_filename = os.path.splitext(os.path.basename(self.download_path))[0] + '.jpg'

        for page in images_from_path:
            page.save(os.path.join(self.save_path, base_filename), 'JPEG')

        os.remove('Plans/plan.pdf')

    def fresh_plans(self, new):
        """
        :param new display new plans only
        :return: dict containing new plans for students
        """
        resp = requests.get(self.url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        if not new:
            new_plans = soup.select('a')[13:16]
        else:
            new_plans = soup.select('.swiezy')[13:16]
        fresh_plans = []
        for plan in new_plans:
            link = 'https://degra.wi.pb.edu.pl/rozklady' + plan.get('href', None)
            fresh_plans.append({'semestr':plan.getText(), 'link': link})
        print(fresh_plans)
        return fresh_plans

    def get_plan_link(self):
        resp = requests.get(self.url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = soup.select('body a')[14:15]
        pdf_link = 'https://degra.wi.pb.edu.pl/rozklady' + links[0].get('href')[1:]
        return pdf_link