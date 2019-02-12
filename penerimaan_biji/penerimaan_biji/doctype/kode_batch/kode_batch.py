# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils import now
class KodeBatch(Document):
	def validate(self):
		if self.status=="Closed":
			frappe.throw("Data Batch Sudah Tidak Boleh di Update")
	def autoname(self):
		self.name=make_autoname("{}.YY.###".format(self.s_loc),doc=self)
	def on_update_after_submit(self):
		if self.sn_est and self.sn_est>0:
			self.ton_est=self.sn_est*self.total
		else:
			self.ton_est=0

		if self.sn_tak and self.sn_tak>0:
			self.ton_tak=self.sn_tak*self.total
		else:
			self.ton_tak=0

		if self.sn_def and self.sn_def>0:
			self.ton_def=self.sn_def*self.total
		else:
			self.ton_def=0
		if self.status=="Open":
			self.ton_final=self.ton_est
		
		
@frappe.whitelist()
def close_batch(name):
	doc = frappe.get_doc("Kode Batch",name)
	doc.closing = now()
	doc.status = "Closed"
	doc.save()
	frappe.db.sql("""update `tabData Produksi` set status = "Closed" where batch = "{}" """.format(nama))