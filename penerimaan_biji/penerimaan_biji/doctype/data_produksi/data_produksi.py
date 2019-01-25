# -*- coding: utf-8 -*-
# Copyright (c) 2019, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class DialyData(Document):
	pass
	def on_submit(self):
		batch = frappe.get_doc("Kode Batch",self.batch)
		batch.total = batch.total+self.qty
		batch.ton_def=batch.sn_def*batch.total
		batch.ton_tak=batch.sn_tak*batch.total
		batch.ton_est=batch.sn_est*batch.total
		batch.save(ignore_permissions=True)
	def on_cancel(self):
		batch = frappe.get_doc("Kode Batch",self.batch)
		batch.total = batch.total-self.qty
		batch.ton_def=batch.sn_def*batch.total
		batch.ton_tak=batch.sn_tak*batch.total
		batch.ton_est=batch.sn_est*batch.total
		batch.save(ignore_permissions=True)
