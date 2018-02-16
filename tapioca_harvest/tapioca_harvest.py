# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from requests.auth import HTTPBasicAuth


from .resource_mapping import RESOURCE_MAPPING


class HarvestClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    resource_mapping = RESOURCE_MAPPING
    api_root = 'https://api.harvestapp.com/v2/'

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(HarvestClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params.setdefault('headers', {}).update({
            'Authorization': 'Bearer %s' % api_params.get('token', ''),
            'Harvest-Account-Id': api_params.get('account_id', ''),
            'User-Agent': api_params.get('user_agent', '')
        })

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass

    def response_to_native(self, response):
        if response.content.strip():
            return super(HarvestClientAdapter, self).response_to_native(response)


Harvest = generate_wrapper_from_adapter(HarvestClientAdapter)
