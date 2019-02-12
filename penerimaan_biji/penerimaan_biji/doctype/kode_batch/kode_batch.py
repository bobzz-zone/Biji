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
			self.ton_final = self.ton_est
		else:
			self.ton_est=0

		if self.sn_tak and self.sn_tak>0:
			self.ton_tak=self.sn_tak*self.total
			self.ton_final = self.ton_tak
		else:
			self.ton_tak=0

		if self.sn_def and self.sn_def>0:
			self.ton_def=self.sn_def*self.total
			self.ton_final = self.ton_def
		else:
			self.ton_def=0
		
		
	def on_update_after_submit_old(self):
		lists = frappe.get_all("Data Produksi",filters={"batch":self.name,"docstatus":("!=",2)},fields=["name"])
		for row in lists:
			doc = frappe.get_doc("Data Produksi",row.name)
			doc.sn_est=self.sn_est
			doc.sn_tak=self.sn_tak
			doc.sn_def=self.sn_def
			if doc.sn_def and doc.sn_def >0:
				doc.total=doc.sn_def*doc.qty
			elif doc.sn_tak and doc.sn_tak >0:
				doc.total=doc.sn_tak*doc.qty
			elif doc.sn_est and doc.sn_est >0:
				doc.total=doc.sn_est*doc.qty
			else:
				doc.total=0
			self.ton_final = doc.total
			doc.save(ignore_permissions=True)
		if self.sn_def and self.sn_def>0:
			self.ton_def=self.sn_def*self.total
		else:
			self.ton_def=0
		if self.sn_tak and self.sn_tak>0:
			self.ton_tak=self.sn_tak*self.total
		else:
			self.ton_tak=0
		if self.sn_est and self.sn_est>0:
			self.ton_est=self.sn_est*self.total
		else:
			self.ton_est=0

@frappe.whitelist()
def update_status(name):
	doc = frappe.get_doc("Kode Batch",name)
	doc.closing = now()
	doc.status = "Closed"
	doc.update()
	frappe.db.sql("""update `tabData Produksi` set status = "Closed" where batch = "{}" """.format(nama))