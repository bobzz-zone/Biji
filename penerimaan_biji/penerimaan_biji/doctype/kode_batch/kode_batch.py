# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.naming import make_autoname
from frappe.utils import now , now_datetime
class KodeBatch(Document):
	def validate(self):
		if self.status=="Closed":
			frappe.throw("Data Batch Sudah Tidak Boleh di Update")
	def autoname(self):
		today=now_datetime()
		if self.no > 999 :
			frappe.throw("No Batch Tidak boleh lebih dari 999")
		if self.no == 0 :
			frappe.throw("No Batch Tidak boleh 0")
		self.name="{}{}{:0>3d}".format(self.s_loc,today.strftime('%y'),self.no)
	def calculate(self):
		posisi = "Estimasi"
		if self.sn_est and self.sn_est>0:
			self.ton_est=self.sn_est*self.total
		else:
			self.ton_est=0

		if self.sn_tak and self.sn_tak>0:
			self.ton_tak=self.sn_tak*self.total
			posisi="Taksasi"
		else:
			self.ton_tak=0

		if self.sn_def and self.sn_def>0:
			self.ton_def=self.sn_def*self.total
			posisi="Definitif"
		else:
			self.ton_def=0
		self.posisi=posisi
		if self.status=="Open":
			self.total_final=self.ton_est
@frappe.whitelist()
def close_batch(name):
	doc = frappe.get_doc("Kode Batch",name)
	#doc.closing = now()
	doc.status = "Closed"
	doc.save()
	frappe.db.sql("""update `tabData Produksi` set status = "Closed" where batch = "{}" """.format(name))
def update_posisi():
	list_batch = frappe.db.sql("""select name from `tabKode Batch` where docstatus!=2 """,as_list=1)
	for row in list_batch:
		data = frappe.get_doc("Kode Batch",row[0])
		data.calculate()
		data.save(ignore_permissions=1)
def patch():
	data = frappe.db.sql("select name , sn_tak, ton_tak from `tabKode Batch` where sn_tak>0 and (ton_tak is null or ton_tak=0)",as_list=1)
	for row in data:
		print(row[0])
		frappe.db.sql("""update `tabData Produksi` set total=(qty*{}) , sn_tak={} where batch="{}" and (sn_tak is null or sn_tak=0) and (sn_def is null or sn_def=0) 
			""".format(row[1],row[1],row[0]))
		frappe.db.sql("""update `tabData Produksi` set sn_tak={} where batch="{}" and (sn_tak is null or sn_tak=0) and sn_def>0 
			""".format(row[1],row[0]))
	for row in data:
		detail = frappe.db.sql("""select sum(qty*sn_tak) from `tabData Produksi` where batch="{}" """.format(row[0]),as_list=1)
		for a in detail:
			frappe.db.sql("""update `tabKode Batch` set ton_tak={} where name="{}" """.format(a[0],row[0]))

