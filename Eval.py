class Eval(webapp2.RequestHandler):
	def get(self):
		try:
			q=self.request.get('q')
			code=eval(compile(q,'<string>', 'eval', __future__.division.compiler_flag))
			self.response.write('{'+q+'}{'+str(code)+'}')
		except:
			self.response.write('{'+q+'}{URL Encode/Decode Error, Escape specl chars}')
