import wget
import tempfile
import os
import PyPDF2
from pdf2image import convert_from_path


class PlanScraperForApocryph:
    def __init__(self):
        self.url = 'https://degra.wi.pb.edu.pl/rozklady/doc/isi4.pdf?id=1661694339126998006'
        self.download_path = 'Plans/plan.pdf'
        self.save_path = 'Plans/PlanJPGS'
        wget.download(self.url, self.download_path)

    def get_plan(self):
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(self.download_path, output_file=path, last_page=1,first_page=0)

        base_filename = os.path.splitext(os.path.basename(self.download_path))[0] + '.jpg'

        for page in images_from_path:
            page.save(os.path.join(self.save_path, base_filename), 'JPEG')

        os.remove('Plans/plan.pdf')

