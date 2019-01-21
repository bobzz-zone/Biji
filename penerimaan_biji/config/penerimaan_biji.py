from frappe import _

def get_data():
	return [
		{
			"label": _("Transaction"),
			"items": [
				{
					"type": "doctype",
					"name": "Data Produksi",
				},
				{
					"type": "doctype",
					"name": "ID Alat",
				},
				{
					"type": "doctype",
					"name": "kode Batch",
				},
			]
		},
		{
			"label": _("Master Data"),
			"items": [
				{
					"type": "doctype",
					"name": "Objek Produksi",
				},
				{
					"type": "doctype",
					"name": "kelas",
				},
				{
					"type": "doctype",
					"label": "Nama Tambang / Kapal",
					"name": "DataSpek",
				},
				{
					"type": "doctype",
					"name": "Unit Produksi",
				},
				{
					"type": "doctype",
					"name": "WASPROD",
				},
				{
					"type": "doctype",
					"label" : "Badan usaha",
					"name": "DataSpek BU",
				},
				{
					"type": "doctype",
					"name": "Lokasi",
				},
				{
					"type": "doctype",
					"name": "Lokasi Kecamatan",
				},
				{
					"type": "doctype",
					"name": "IUP",
				},
				{
					"type": "doctype",
					"name": "Lokasi Penyimpanan",
				},
				{
					"type": "doctype",
					"name": "Satuan Produksi",
				},
				{
					"type": "doctype",
					"name": "uji Kadar",
				},
			]
		},
	]