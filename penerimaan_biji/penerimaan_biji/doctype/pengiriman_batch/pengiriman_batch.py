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
		ton=0
		for row in self.batch_list:
			batch=frappe.get_doc("Kode Batch",row.batch)
			total = row.total
			ton=row.ton
			if batch.jalan==1 or batch.used==1 or batch.status=="Open":
				frappe.throw("Batch {} Tidak bisa di lakukan pengiriman".format(batch.name))
		self.total_qty=total
		self.input=ton
	def on_cancel(self):
		frappe.throw("Dokumen tidak dapat di batalkan")
		# pass
	def on_submit(self):
		total = 0
		qty=0
		for row in self.batch_list:
			qty = row.total
			total = row.ton
			batch=frappe.get_doc("Kode Batch",row.batch)
			batch.jalan=1
			batch.lokasi_temp=self.lokasi
			batch.jalan_temp=self.s_loc
			batch.type_temp=self.type
			#batch.calculate()
			batch.save(ignore_permissions=1)
		self.input=total
		self.total_qty = qty