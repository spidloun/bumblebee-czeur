
import bumblebee.engine
import bumblebee.output
import bumblebee.util
import os, urllib, datetime

BASE_URL = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt?date=%s"

class Module(bumblebee.engine.Module):
	def __init__(self, engine, config):
		super(Module, self).__init__(engine, config, bumblebee.output.Widget(full_text=self.current_rate))

	def current_rate(self, widget):
		with urllib.request.urlopen(BASE_URL % datetime.date.today().strftime("%d.%m.%Y")) as all_rates:
			eur_rate_line = list(filter(lambda line: "EUR" in line, all_rates.read().decode().split("\n")[2:]))
			eur_rate = eur_rate_line[0].split("|")[4]
			output = u"\uf153 %s" % eur_rate 
			return output