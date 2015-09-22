# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from requests.auth import HTTPBasicAuth


from resource_mapping import RESOURCE_MAPPING


class HarvestClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(HarvestClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        params['auth'] = HTTPBasicAuth(
            api_params.get('user'), api_params.get('password'))

        params['headers'] = params.get('headers', {})
        params['headers']['Accept'] = 'application/json'

        return params

    def get_iterator_list(self, response_data):
        return response_data

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass

    def response_to_native(self, response):
        if response.content.strip():
            return super(HarvestClientAdapter, self).response_to_native(response)

    def get_api_root(self, api_params):
        return 'https://' + api_params['company_name'] + '.harvestapp.com/'


Harvest = generate_wrapper_from_adapter(HarvestClientAdapter)
