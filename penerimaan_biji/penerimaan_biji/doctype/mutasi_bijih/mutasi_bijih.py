# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now , add_days
class MutasiBijih(Document):
	def on_submit2(self):
		batch=frappe.get_doc("Kode Batch",self.batch)
		batch.closing = add_days(self.date,-1)
		batch.update()
