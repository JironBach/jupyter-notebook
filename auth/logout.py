"""Tornado handlers for logging out of the notebook.
"""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

from ..base.handlers import IPythonHandler
import sys

class LogoutHandler(IPythonHandler):

    def get(self):
        requests.get("http://localhost:3001/").url#debug
        sys.exit()#debug

        self.clear_login_cookie()
        if self.login_available:
            message = {'info': 'Successfully logged out.'}
        else:
            message = {'warning': 'Cannot log out.  Notebook authentication '
                       'is disabled.'}
        self.write(self.render_template('logout.html',
                    message=message))


default_handlers = [(r"/logout", LogoutHandler)]
