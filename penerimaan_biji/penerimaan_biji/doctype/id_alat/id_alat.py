# -*- coding: utf-8 -*-
# Copyright (c) 2018, PT DAS and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class IDAlat(Document):
	def autoname(self):
		return "{}{}{}{}".format(self.kode_objek,self.kode_alat,self.id_alat,self.iup)
