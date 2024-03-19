# cleanup_files.py
from django.core.management.base import BaseCommand
from datetime import timedelta, datetime, timezone
import os
from django.conf import settings

class Command(BaseCommand):
  help = 'clean file after 24 hours'

  def handle(self, *args, **kwargs):
    # directory of execution
    directory = 'run/'

    # not remove massccs 
    massccs = 'massccs'

    # Obtenha o tempo atual
    time_new = datetime.now()
    #print(time_new)
    # 24 hours to delete files     
    limit = time_new - timedelta(minutes=1) # timedelta(hours=24)
    #print(limit)

    # Itere sobre os arquivos e remova aqueles que foram criados antes do limite, exceto o arquivo específico
    for file in os.listdir(directory):

      path_file = os.path.join(directory, file)
      #print(path_file)

      info_file = os.stat('run/'+file)
      date_modify_timestamp = info_file.st_mtime
      date_modify = datetime.fromtimestamp(date_modify_timestamp)
      #print(date_modify)
      #print(date_modify - limit)
      
      if date_modify < limit and file != massccs:
        os.remove(path_file)
    
    self.stdout.write(self.style.SUCCESS('Files remove with success, excet {}'.format(massccs)))
