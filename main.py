from fastapi import FastAPI
from datetime import datetime

storage = FastAPI(title='MY FASTAPI')

@storage.get('/')
def index():
  return "My name is Bajo, This is my first API"

@storage.get('/today')
def today():
  return str(datetime.now())

@storage.get('/mynames')
def names(first_name: bool = False, last_name: bool = False, full_name: bool = False):
  full_names = ''
  if first_name:
    full_names += 'Bajo'
  if last_name:
    full_names += 'Ngabonziza'
  if full_name:
    full_names = 'Bajo Ngabonziza'
  
  return full_names
  