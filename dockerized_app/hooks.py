# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dockerized_app"
app_title = "how to dockerized frappe app "
app_publisher = "anvilerp.com"
app_description = "how to dockerized frappe app "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@anvilerp.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dockerized_app/css/dockerized_app.css"
# app_include_js = "/assets/dockerized_app/js/dockerized_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/dockerized_app/css/dockerized_app.css"
# web_include_js = "/assets/dockerized_app/js/dockerized_app.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dockerized_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dockerized_app.install.before_install"
# after_install = "dockerized_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dockerized_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dockerized_app.tasks.all"
# 	],
# 	"daily": [
# 		"dockerized_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"dockerized_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dockerized_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dockerized_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dockerized_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dockerized_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dockerized_app.task.get_dashboard_data"
# }

