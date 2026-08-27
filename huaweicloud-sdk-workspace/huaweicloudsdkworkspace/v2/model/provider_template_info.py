# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProviderTemplateInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_type': 'str',
        'provider_id': 'str',
        'base_url': 'str',
        'custom_config': 'ProviderCustomConfig',
        'api_type': 'ApiType'
    }

    attribute_map = {
        'provider_type': 'provider_type',
        'provider_id': 'provider_id',
        'base_url': 'base_url',
        'custom_config': 'custom_config',
        'api_type': 'api_type'
    }

    def __init__(self, provider_type=None, provider_id=None, base_url=None, custom_config=None, api_type=None):
        r"""ProviderTemplateInfo

        The model defined in huaweicloud sdk

        :param provider_type: 模板唯一标识（供应商类型）。
        :type provider_type: str
        :param provider_id: 供应商id。
        :type provider_id: str
        :param base_url: 供应商base_url。
        :type base_url: str
        :param custom_config: 
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        :param api_type: 
        :type api_type: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        
        

        self._provider_type = None
        self._provider_id = None
        self._base_url = None
        self._custom_config = None
        self._api_type = None
        self.discriminator = None

        if provider_type is not None:
            self.provider_type = provider_type
        if provider_id is not None:
            self.provider_id = provider_id
        if base_url is not None:
            self.base_url = base_url
        if custom_config is not None:
            self.custom_config = custom_config
        if api_type is not None:
            self.api_type = api_type

    @property
    def provider_type(self):
        r"""Gets the provider_type of this ProviderTemplateInfo.

        模板唯一标识（供应商类型）。

        :return: The provider_type of this ProviderTemplateInfo.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this ProviderTemplateInfo.

        模板唯一标识（供应商类型）。

        :param provider_type: The provider_type of this ProviderTemplateInfo.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ProviderTemplateInfo.

        供应商id。

        :return: The provider_id of this ProviderTemplateInfo.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ProviderTemplateInfo.

        供应商id。

        :param provider_id: The provider_id of this ProviderTemplateInfo.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def base_url(self):
        r"""Gets the base_url of this ProviderTemplateInfo.

        供应商base_url。

        :return: The base_url of this ProviderTemplateInfo.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this ProviderTemplateInfo.

        供应商base_url。

        :param base_url: The base_url of this ProviderTemplateInfo.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def custom_config(self):
        r"""Gets the custom_config of this ProviderTemplateInfo.

        :return: The custom_config of this ProviderTemplateInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        return self._custom_config

    @custom_config.setter
    def custom_config(self, custom_config):
        r"""Sets the custom_config of this ProviderTemplateInfo.

        :param custom_config: The custom_config of this ProviderTemplateInfo.
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        self._custom_config = custom_config

    @property
    def api_type(self):
        r"""Gets the api_type of this ProviderTemplateInfo.

        :return: The api_type of this ProviderTemplateInfo.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this ProviderTemplateInfo.

        :param api_type: The api_type of this ProviderTemplateInfo.
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
        if not isinstance(other, ProviderTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
