import wget
from bs4 import BeautifulSoup
import requests
import tempfile
import os
import PyPDF2
from pdf2image import convert_from_path
import scrape

scraper = scrape.PlanScraperForApocryph()
scraper.fresh_plans(False)