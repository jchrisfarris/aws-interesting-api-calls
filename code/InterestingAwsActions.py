

import yaml

class Action(object):
	"""Represents the API Call"""
	def __init__(self, database, action_name):
		super(Action, self).__init__()
		self.db = database
		self.name = action_name
		# split the action name to get the service and api_call
		(self.service, self.api_call) = action_name.split(':')
		# Load in the rest of the stuff to the namespace
		try: 
			self.__dict__.update(database.action_list[self.service][self.api_call])
		except KeyError as e:
			raise ActionLookupError("Service or API Call {} is not valid".format(e))

class ActionDatabase(object):
	"""Represents the Database of Interesting API Calls"""
	def __init__(self, filename):
		"""loads the file from the local filesystem"""
		super(ActionDatabase, self).__init__()
		self.filename = filename
		if "https://" in filename or "http://" in filename:
			# raise NotImplementedError("HTTP Support not available yet")

			import requests
			r = requests.get(filename)
			if r.status_code == 200:
				try: 
					self.action_list = yaml.load(r.content)
				except yaml.YAMLError as exc:
					# print(exc)
					raise ActionFileParseError("Error parsing {}: {}".format(filename, exc).replace('\n', ' '))
			else:
				raise ActionFileParseError("Got HTTP Code {} requesting {}".format(r.status_code, filename))

		else: # Assume local file
			try:
				with open(filename, 'r') as stream:
					try:
						self.action_list = yaml.load(stream)
					except yaml.YAMLError as exc:
						# print(exc)
						raise ActionFileParseError("Error parsing {}: {}".format(filename, exc).replace('\n', ' '))
			except IOError as e:
				raise ActionFileParseError("Error reading {}: {}".format(filename, e))	

	def get_action(self, action_name):
		"""Returns an Action Object """
		return(Action(self, action_name))

	def by_service(self, service):
		"""Returns a list of Actions fitting the specific service"""
		output = []
		for api_call in self.action_list[service]:
			output.append(service + ":" + api_call)
		return(output)

	def by_severity(self, severity):
		"""Return a list of all api_calls where Severity = <severity>"""
		return(self.__get_actions_by_key__("Severity", severity))

	def by_category(self, category):
		"""Return a list of all api_calls where Category = <category>"""
		return(self.__get_actions_by_key__("Category", category))

	def by_risk(self, risk):
		"""Return a list of all api_calls where Risk = <risk>"""
		return(self.__get_actions_by_key__("Risk", risk))


	def __get_actions_by_key__(self, key, value):
		output = []
		for service in self.action_list:
			# print("Found Service: {}".format(service))
			for api_call in self.action_list[service]:
				# print("\tFound Action: {}".format(api_call))
				if self.action_list[service][api_call][key] == value:
					output.append(service + ":" + api_call)
		return(output)

	def list_services(self):
		return(self.action_list.keys())


	def list_severities(self):
		"""Returns a list of valid severities in the database"""
		return(self.__list_key__("Severity"))

	def list_categories(self):
		"""Returns a list of valid categories in the database"""
		return(self.__list_key__("Category"))

	def list_risks(self):
		"""Returns a list of valid risk types in the database"""
		return(self.__list_key__("Risk"))

	def __list_key__(self, key):
		""" Internal function to return a list of valid keys"""
		api_list = {}
		for service in self.action_list:
			# print("Found Service: {}".format(service))
			for api_call in self.action_list[service]:
				# print("\tFound Action: {}".format(api_call))
				value = self.action_list[service][api_call][key]

				# Added for Python2 / Python3 compat
				# https://stackoverflow.com/a/22679982
				try:
					basestring
				except NameError:
					basestring = str

				if isinstance(value, basestring):
					if value in api_list:
						api_list[value].append(api_call)
					else:
						api_list[value] = [api_call]
				else: 
					for v in value:
						if v in api_list:
							api_list[v].append(api_call)
						else:
							api_list[v] = [api_call]

		output = []
		for k in api_list:
			output.append(k)
		return(output)



class ActionFileParseError(Exception):
	'''Raised when the Action yaml file has a syntax error'''

class ActionLookupError(LookupError):
	'''Raised when the Action requested is not in the database'''		