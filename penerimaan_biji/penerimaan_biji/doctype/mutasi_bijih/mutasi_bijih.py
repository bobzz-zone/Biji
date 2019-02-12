# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import now , add_days
class MutasiBijih(Document):
	def validate(self):
		data = frappe.db.sql("select name , aktivitas from `tabMutasi Bijih` order by date desc limit 0,1")
		last = "Penerimaan"
		num = 0
		for row in data:
			last = data[1]
			num++
		reason = "Ada Aktifitas Sebelumya , Sehingga hanya bisa melakukan Pengiriman"
		if num > 0 && last == "Penerimaan":
			reason= "Ada Pengiriman"
		elif num > 0 :
			reason= "Ada Penerimaan"
		if last == self.aktivitas:
			frappe.throw("Tidak bisa melakukan {} karena belum {}".format(last,reason))
	def on_submit(self):
		batch=frappe.get_doc("Kode Batch",self.batch)
		if self.sn_tak :
			batch.sn_tak = self.berat_ore * self.sn_tak / self.qty
		if self.sn_def:
			batch.sn_def = self.berat_ore * self.sn_def / self.qty
		batch.tak_percent = self.sn_tak
		batch.def_percent = self.sn_def
		batch.update()
