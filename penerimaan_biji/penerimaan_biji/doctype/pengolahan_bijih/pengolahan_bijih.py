# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint,flt
class PengolahanBijih(Document):
	def validate(self):
		if self.type=="Output":
			data = frappe.db.sql("""select total , output from `tabProcess Order Batch` where parent="{}" and batch="{}" """.format(self.po,self.batch),as_list=1)
			for row in data:
				if row[1] and flt(row[1])>0:
					frappe.throw("Sudah ada Output tidak bisa memasukan output lagi")
	def on_submit(self):
		po=frappe.get_doc("Process Order",self.po)
		if self.type == "Input":
			frappe.db.sql("""update `tabKode Batch` set used = 1 where name={}""".format(self.batch))
			po.append("batch_list",{"doctype":"Process Order Batch","batch":self.batch,"total":self.total})
		if self.type == "Output":
			frappe.db.sql("""update `tabKode Batch` set used = 0 where name={}""".format(self.batch))
			batch=frappe.get_doc("Kode Batch",self.batch)
			batch.ton_final=self.total
			batch.save()
		po.save()
	def on_cancel(self):
		frappe.throw("Dokumen tidak dapat di batalkan")
			