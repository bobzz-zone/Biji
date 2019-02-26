# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PengirimanBatch(Document):
	pass
	def validate(self):
		total = 0
		for row in self.batch_list:
			batch=frappe.get_doc("Kode Batch",row.batch)
			total = row.input
			if batch.jalan==1 or batch.used==1 or batch.status=="Open":
				frappe.throw("{} Tidak bisa di lakukan pengiriman".fomat(batch.name))
		self.input=total
		
	def on_cancel(self):
		frappe.throw("Dokumen tidak dapat di batalkan")
	def on_submit(self):
		total = 0
		for row in self.batch_list:
			total = row.input
			batch=frappe.get_doc("Kode Batch",row.batch)
			batch.jalan=1
			batch.save(ignore_permissions=1)
		self.input=total