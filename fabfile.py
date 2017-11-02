# http: // advanced - python.readthedocs.io / en / latest / fabric.html

import fabric.api

fabric.api.env.user = 'cs1150263'
fabric.api.env.hosts = ['palasi.cse.iitd.ac.in']

def run_script():

    fabric.api.put('helper.py', '/tmp')
    fabric.api.run('python /tmp/helper.py ip mac name comments path')
    
