# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProviderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_id': 'str',
        'provider_name': 'str',
        'base_url': 'str',
        'api_key': 'str',
        'custom_config': 'ProviderCustomConfig',
        'api_type': 'ApiType'
    }

    attribute_map = {
        'provider_id': 'provider_id',
        'provider_name': 'provider_name',
        'base_url': 'base_url',
        'api_key': 'api_key',
        'custom_config': 'custom_config',
        'api_type': 'api_type'
    }

    def __init__(self, provider_id=None, provider_name=None, base_url=None, api_key=None, custom_config=None, api_type=None):
        r"""UpdateProviderReq

        The model defined in huaweicloud sdk

        :param provider_id: 供应商标识（模板创建时与模板保持一致，自定义时可指定）。
        :type provider_id: str
        :param provider_name: 供应商名称。
        :type provider_name: str
        :param base_url: 供应商base_url。
        :type base_url: str
        :param api_key: 供应商API Key（SCC加密存储）。
        :type api_key: str
        :param custom_config: 
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        :param api_type: 
        :type api_type: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        
        

        self._provider_id = None
        self._provider_name = None
        self._base_url = None
        self._api_key = None
        self._custom_config = None
        self._api_type = None
        self.discriminator = None

        if provider_id is not None:
            self.provider_id = provider_id
        if provider_name is not None:
            self.provider_name = provider_name
        if base_url is not None:
            self.base_url = base_url
        if api_key is not None:
            self.api_key = api_key
        if custom_config is not None:
            self.custom_config = custom_config
        if api_type is not None:
            self.api_type = api_type

    @property
    def provider_id(self):
        r"""Gets the provider_id of this UpdateProviderReq.

        供应商标识（模板创建时与模板保持一致，自定义时可指定）。

        :return: The provider_id of this UpdateProviderReq.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this UpdateProviderReq.

        供应商标识（模板创建时与模板保持一致，自定义时可指定）。

        :param provider_id: The provider_id of this UpdateProviderReq.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this UpdateProviderReq.

        供应商名称。

        :return: The provider_name of this UpdateProviderReq.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this UpdateProviderReq.

        供应商名称。

        :param provider_name: The provider_name of this UpdateProviderReq.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def base_url(self):
        r"""Gets the base_url of this UpdateProviderReq.

        供应商base_url。

        :return: The base_url of this UpdateProviderReq.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this UpdateProviderReq.

        供应商base_url。

        :param base_url: The base_url of this UpdateProviderReq.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def api_key(self):
        r"""Gets the api_key of this UpdateProviderReq.

        供应商API Key（SCC加密存储）。

        :return: The api_key of this UpdateProviderReq.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this UpdateProviderReq.

        供应商API Key（SCC加密存储）。

        :param api_key: The api_key of this UpdateProviderReq.
        :type api_key: str
        """
        self._api_key = api_key

    @property
    def custom_config(self):
        r"""Gets the custom_config of this UpdateProviderReq.

        :return: The custom_config of this UpdateProviderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        return self._custom_config

    @custom_config.setter
    def custom_config(self, custom_config):
        r"""Sets the custom_config of this UpdateProviderReq.

        :param custom_config: The custom_config of this UpdateProviderReq.
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        self._custom_config = custom_config

    @property
    def api_type(self):
        r"""Gets the api_type of this UpdateProviderReq.

        :return: The api_type of this UpdateProviderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this UpdateProviderReq.

        :param api_type: The api_type of this UpdateProviderReq.
        :type api_type: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        self._api_type = api_type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateProviderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
