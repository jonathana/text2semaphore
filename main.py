#!/usr/bin/env python
# The MIT License
# 
# Copyright (c) 2010 Jonathan M. Altman
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__author__ = 'Jonathan M. Altman'

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

		if self.request.accept.first_match(['text/html', 'text/plain']) == 'text/plain':
			self.response.headers['Content-Type'] = 'text/plain'
			self.response.out.write(output_text)
			return
		else:
			pass
		template_values = {
			'app_title': app_title
			, 'input_text': input_text
			, 'output_text': output_text
		}
		path = os.path.join(os.path.dirname(__file__), 'templates/text2semaphore.html')
		self.response.out.write(template.render(path, template_values))

def main():
	application = webapp.WSGIApplication([(r'/(\w*)', MainHandler)], debug=False)
	util.run_wsgi_app(application)


if __name__ == '__main__':
	main()
