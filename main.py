#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#	 http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class CharDecoder(dict):
	def __missing__(self, key):
		return key

class MainHandler(webapp.RequestHandler):
	charDecoder = CharDecoder({
		"a": "alfa",
		"b": "bravo",
		"c": "charlie",
		"d": "delta",
		"e": "echo",
		"f": "foxtrot",
		"g": "golf",
		"h": "hotel",
		"i": "india",
		"j": "juliett",
		"k": "kilo",
		"l": "lima",
		"m": "mike",
		"n": "november",
		"o": "oscar",
		"p": "papa",
		"q": "quebec",
		"r": "romeo",
		"s": "sierra",
		"t": "tango",
		"u": "uniform",
		"v": "victor",
		"w": "whiskey",
		"x": "xray",
		"y": "yankee",
		"z": "zulu"
	})

	def get(self, input_text):
		app_title = 'Text to semaphore pronunciation'
		output_text = ''
		output_sep = ''
		for c in input_text:
			output_text += output_sep + self.charDecoder[c.lower()]
			if output_sep == '': output_sep = ' '

		template_values = { 'app_title': app_title, 'input_text': input_text, 'output_text': output_text}
		path = os.path.join(os.path.dirname(__file__), 'templates/text2semaphore.html')
		self.response.out.write(template.render(path, template_values))

def main():
	application = webapp.WSGIApplication([(r'/(\w+)', MainHandler)],
										 debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
	main()
