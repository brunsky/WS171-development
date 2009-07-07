#!/usr/bin/env python
#
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the"License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "ASIS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import wsgiref.handlers
from google.appengine.ext import zipserve
from google.appengine.ext import webapp
import memcache_zipserve


class MainHandler(webapp.RequestHandler):

  def get(self):
    self.response.out.write('Hello world!')

def main():
  application = webapp.WSGIApplication([('/(.*)', memcache_zipserve.create_handler([['0.zip', 'app.yaml'],
['1.zip', 'guide/samples/ApiDemos/src/com/example/android/apis/app/ForwardTarget.html'],
['2.zip', 'images/dialog_list.png'],
['3.zip', 'images/widget_design/Music_widget_button_states.psd'],
['4.zip', 'reference/android/database/MatrixCursor.html'],
['5.zip', 'reference/android/test/suitebuilder/TestSuiteBuilder.FailedToCreateTests.html'],
['6.zip', 'reference/android/widget/ProgressBar.html'],
['7.zip', 'reference/java/nio/ByteOrder.html'],
['8.zip', 'reference/java/util/concurrent/locks/ReentrantReadWriteLock.WriteLock.html'],
['9.zip', 'reference/org/apache/http/impl/cookie/NetscapeDraftSpec.html'],
['10.zip', 'shareables/icon_templates-v1.0.zip'],
['11.zip', 'shareables/icon_templates-v1.0/launcher/Launcher-template-250.ai'],
])),
],
debug=False)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()