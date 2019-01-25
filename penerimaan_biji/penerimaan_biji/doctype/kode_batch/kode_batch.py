# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class KodeBatch(Document):
	pass
	def on_update_after_submit(self):
		lists = frappe.get_all("Data Produksi",filters={"batch":self.name,"docstatus":("!=",2)})
		for doc in lists:
			doc.sn_est=self.sn_est
			doc.sn_tak=self.sn_tak
			doc.sn_def=self.sn_def
			if doc.sn_def and doc.sn_def >0:
				doc.total=doc.sn_def*doc.qty
			elif doc.sn_tak and doc.sn_tak >0:
				doc.total=doc.sn_tak*doc.qty
			else:
				doc.total=doc.sn_est*doc.qty
			doc.save(ignore_permissions=True)
		self.ton_def=self.sn_def*self.total
		self.ton_tak=self.sn_tak*self.total
		self.ton_est=self.sn_est*self.total