# coding: utf-8

RESOURCE_MAPPING = {

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

    # Projects
    'projects': {
        'resource': 'projects',
        'docs': 'https://help.getharvest.com/api-v2/projects-api/projects/projects/#list-all-projects',
        'methods': ['GET', 'POST']
    },
    'project': {
        'resource': 'projects/{project_id}',
        'docs': 'https://help.getharvest.com/api-v2/projects-api/projects/projects/#retrieve-a-project',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # Roles
    'roles': {
        'resource': 'roles',
        'docs': 'https://help.getharvest.com/api-v2/roles-api/roles/roles/#list-all-roles',
        'methods': ['GET', 'POST']
    },
    'role': {
        'resource': 'roles/{role_id}',
        'docs': 'https://help.getharvest.com/api-v2/roles-api/roles/roles/#retrieve-a-role',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # Task Assignment
    'task_assignments': {
        'resource': 'projects/{project_id}/task_assignments',
        'docs': 'https://help.getharvest.com/api-v2/projects-api/projects/task-assignments/#list-all-task-assignments',
        'methods': ['GET', 'POST']
    },
    'task_assignment': {
        'resource': 'projects/{project_id}/task_assignments/{task_assignment_id}',
        'docs': 'https://help.getharvest.com/api-v2/projects-api/projects/task-assignments/#retrieve-a-task-assignment',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # Tasks
    'tasks': {
        'resource': 'tasks',
        'docs': 'https://help.getharvest.com/api-v2/tasks-api/tasks/tasks/#list-all-tasks',
        'methods': ['GET', 'POST']
    },
    'task': {
        'resource': 'tasks/{task_id}',
        'docs': 'https://help.getharvest.com/api-v2/tasks-api/tasks/tasks/#retrieve-a-task',
        'methods': ['GET', 'PATCH', 'DELETE']
    },

    # Time Entries
    'time_entries': {
        'resource': 'time_entries',
        'docs': 'https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/#list-all-time-entries',
        'methods': ['GET', 'POST']
    },
    'time_entry': {
        'resource': 'time_entries/{time_entry_id}',
        'docs': 'https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/#retrieve-a-time-entry',
        'methods': ['GET', 'PATCH', 'DELETE']
    },
    'time_entry_restart': {
        'resource': 'time_entries/{time_entry_id}/restart',
        'docs': 'https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/#restart-a-stopped-time-entry',
        'methods': ['PATCH']
    },
    'time_entry_stop': {
        'resource': 'time_entries/{time_entry_id}/stop',
        'docs': 'https://help.getharvest.com/api-v2/timesheets-api/timesheets/time-entries/#stop-a-running-time-entry',
        'methods': ['PATCH']
    },

    # Users
    'users': {
        'resource': 'users',
        'docs': 'https://help.getharvest.com/api-v2/users-api/users/users/#list-all-users',
        'methods': ['GET', 'POST']
    },
    'user': {
        'resource': 'users/{user_id}',
        'docs': 'https://help.getharvest.com/api-v2/users-api/users/users/#retrieve-a-user',
        'methods': ['GET', 'PATCH', 'DELETE']
    },
    'me': {
        'resource': 'users/me',
        'docs': 'https://help.getharvest.com/api-v2/users-api/users/users/#retrieve-the-currently-authenticated-user',
        'methods': ['GET']
    },

    # User Project Assignments
    'project_assignments': {
        'resource': 'users/{user_id}/project_assignments',
        'docs': 'https://help.getharvest.com/api-v2/users-api/users/project-assignments/#list-all-project-assignments',
        'methods': ['GET']
    },
    'my_project_assignments': {
        'resource': 'users/me/project_assignments',
        'docs': 'https://help.getharvest.com/api-v2/users-api/users/project-assignments/#list-all-project-assignments-for-the-currently-authenticated-user',
        'methods': ['GET']
    },

}
