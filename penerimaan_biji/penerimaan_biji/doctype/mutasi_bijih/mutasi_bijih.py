# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now , add_days
class MutasiBijih(Document):
	def on_submit(self):
		batch=frappe.get_doc("Kode Batch",self.batch)
		if self.sn_tak :
			batch.sn_tak = self.berat_ore * self.sn_tak / self.qty
		if self.sn_def:
			batch.sn_def = self.berat_ore * self.sn_def / self.qty
		batch.update()
