# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProcessOrder(Document):
	pass
	def recalculate(self):
		if self.docstatus==1:
			tin=0
			tou=0
			for row in self.batch_list:
				tin = tin + row.total
				tou = tou + row.output
				row.recovery = ( row.output / row.total)*100
			if tin and tou:
				self.recovery = (tou/tin)*100
			self.output=tou
			self.input=tin