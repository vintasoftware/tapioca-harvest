# coding: utf-8

RESOURCE_MAPPING = {
    # Accounts
    'who_am_i': {
        'resource': 'account/who_am_i',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Accounts.md'
    },

    # Client Contacts
    'contacts': {
        'resource': 'contacts',
        'docs': 'https://help.getharvest.com/api-v2/clients-api/clients/contacts/#list-all-contacts',
        'methods': ['POST', 'GET']
    },
    'contact': {
        'resource': 'contacts/{contact_id}',
        'docs': 'https://help.getharvest.com/api-v2/clients-api/clients/contacts/#retrieve-a-contact',
        'methods': ['PATCH', 'GET', 'DELETE']
    },

    # Clients
    'clients': {
        'resource': 'clients',
        'docs': 'https://help.getharvest.com/api-v2/clients-api/clients/clients/#list-all-clients',
        'methods': ['GET', 'POST']
    },
    'client': {
        'resource': 'clients/{client_id}',
        'docs': 'https://help.getharvest.com/api-v2/clients-api/clients/clients/#retrieve-a-client',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # Company
    'company': {
        'resource': 'company',
        'docs': 'https://help.getharvest.com/api-v2/company-api/company/company/#retrieve-a-company',
        'methods': ['GET']
    },

    # Expense Categories
    'expense_categories': {
        'resource': 'expense_categories',
        'docs': 'https://help.getharvest.com/api-v2/expenses-api/expenses/expense-categories/#list-all-expense-categories',
        'methods': ['GET', 'POST']
    },
    'expense_category': {
        'resource': 'expense_categories/{expense_category_id}',
        'docs': 'https://help.getharvest.com/api-v2/expenses-api/expenses/expense-categories/#retrieve-an-expense-category',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # Expenses
    'expenses': {
        'resource': 'expenses',
        'docs': 'https://help.getharvest.com/api-v2/expenses-api/expenses/expenses/#list-all-expenses',
        'methods': ['GET', 'POST']
    },
    'expense': {
        'resource': 'expenses/{expense_id}',
        'docs': 'https://help.getharvest.com/api-v2/expenses-api/expenses/expenses/#retrieve-an-expense',
        'methods': ['PATCH', 'GET', 'DELETE']
    },

    # Invoice Item Categories
    'invoice_item_categories': {
        'resource': 'invoice_item_categories',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-item-categories/#list-all-invoice-item-categories',
        'methods': ['POST', 'GET']
    },
    'invoice_item_category': {
        'resource': 'invoice_item_categories/{category_id}',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-item-categories/#retrieve-an-invoice-item-category',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # Invoice Messages
    'invoices_messages': {
        'resource': 'invoices/{invoice_id}/messages',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/#list-all-messages-for-an-invoice',
        'methods': ['GET', 'POST']
    },
    'invoices_message': {
        'resource': 'invoices/{invoice_id}/messages/{message_id}',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/#delete-an-invoice-message',
        'methods': ['DELETE']
    },
    'invoices_message_mark_as_sent': {
        'resource': 'invoices/{invoice_id}/messages',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/#mark-a-draft-invoice-as-sent',
        'methods': ['POST']
    },
    'invoices_message_mark_as_closed': {
        'resource': 'invoices/{invoice_id}/messages',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/#mark-an-open-invoice-as-closed',
        'methods': ['POST']
    },
    'invoices_message_re_open': {
        'resource': 'invoices/{invoice_id}/messages',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/#re-open-a-closed-invoice',
        'methods': ['POST']
    },
    'invoices_message_mark_as_draft': {
        'resource': 'invoices/{invoice_id}/messages',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-messages/#mark-an-open-invoice-as-a-draft',
        'methods': ['POST']
    },

    # Invoice Payments
    'invoices_payments': {
        'resource': 'invoices/{invoice_id}/payments',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-payments/#list-all-payments-for-an-invoice',
        'methods': ['GET', 'POST']
    },
    'invoices_payment': {
        'resource': 'invoices/{invoice_id}/payments/{payment_id}',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoice-payments/#delete-an-invoice-payment',
        'methods': ['DELETE']
    },

    # Invoices
    'invoices': {
        'resource': 'invoices',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoices/#list-all-invoices',
        'methods': ['GET', 'POST']
    },
    'invoice': {
        'resource': 'invoices/{invoice_id}',
        'docs': 'https://help.getharvest.com/api-v2/invoices-api/invoices/invoices/#retrieve-an-invoice',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # People
    'users': {
        'resource': 'people',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/People.md',
        'methods': ['GET', 'POST']
    },
    'user': {
        'resource': 'people/{user_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/People.md',
        'methods': ['GET', 'PUT', 'DELETE']
    },
    'user_toggle': {
        'resource': 'people/{user_id}/toggle',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/People.md',
        'methods': ['POST']
    },

    # Projects
    'projects': {
        'resource': 'projects',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Projects.md',
        'methods': ['GET', 'POST']
    },
    'project': {
        'resource': 'projects/{project_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Projects.md',
        'methods': ['GET', 'PUT', 'DELETE']
    },
    'de_activate_project': {
        'resource': 'projects/{project_id}/toggle',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Projects.md',
        'methods': ['PUT']
    },

    # Task Assignment
    'task_assignments': {
        'resource': 'projects/{project_id}/task_assignments',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Task%20Assignment.md',
        'methods': ['GET', 'POST']
    },
    'task_assignment': {
        'resource': 'projects/{project_id}/task_assignments/{task_assignment_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Task%20Assignment.md',
        'methods': ['GET', 'PUT', 'DELETE']
    },
    'task_assignment_add_with_create_new_task': {
        'resource': 'projects/{project_id}/task_assignments/add_with_create_new_task',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Task%20Assignment.md',
        'methods': ['POST']
    },

    # Tasks
    'tasks': {
        'resource': 'tasks',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Tasks.md',
        'methods': ['GET', 'POST']
    },
    'task': {
        'resource': 'tasks/{task_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Tasks.md',
        'methods': ['GET', 'PUT', 'DELETE']
    },
    'task_activate': {
        'resource': 'tasks/{task_id}/activate',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Tasks.md',
        'methods': ['POST']
    },

    # Time Tracking
    'tracking_daily': {
        'resource': 'daily',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
    },
    'tracking_daily_day': {
        'resource': 'daily/{day_of_the_year}/{year}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
    },
    'tracking_daily_day_user': {
        'resource': 'daily/{day_of_the_year}/{year}?of_user={user_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
    },
    'tracking_entry': {
        'resource': 'daily/show/{day_entry_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
    },
    'timer_toggle': {
        'resource': 'daily/timer/{day_entry_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
    },
    'create_tracking_entry': {
        'resource': 'daily/add',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
        'methods': ['POST']
    },
    'delete_tracking_entry': {
        'resource': 'daily/delete/{day_entry_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
        'methods': ['DELETE']
    },
    'update_tracking_entry': {
        'resource': 'daily/update/{day_entry_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20Tracking.md',
        'methods': ['POST']
    },

    # Time and Expense Reporting
    'project_entries': {
        'resource': 'projects/{project_id}/entries',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20and%20Expense%20Reporting.md',
    },
    'user_entries': {
        'resource': 'people/{user_id}/entries',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20and%20Expense%20Reporting.md',
    },
    'user_expenses': {
        'resource': 'people/{user_id}/expenses',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20and%20Expense%20Reporting.md',
    },
    'project_expenses': {
        'resource': 'projects/{project_id}/expenses',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/Time%20and%20Expense%20Reporting.md',
    },

    # User Assignment
    'user_assignments': {
        'resource': 'projects/{project_id}/user_assignments',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/User%20Assignment.md',
        'methods': ['GET', 'POST']
    },
    'user_assignment': {
        'resource': 'projects/{project_id}/user_assignments/{user_assignment_id}',
        'docs': 'https://github.com/harvesthq/api/blob/master/Sections/User%20Assignment.md',
        'methods': ['GET', 'PUT', 'DELETE']
    },
}
