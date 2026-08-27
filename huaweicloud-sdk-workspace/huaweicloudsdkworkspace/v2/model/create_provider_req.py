# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProviderReq:

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
        'api_key': 'str',
        'provider_name': 'str',
        'base_url': 'str',
        'custom_config': 'ProviderCustomConfig',
        'models': 'list[CreateModelReq]',
        'api_type': 'ApiType'
    }

    attribute_map = {
        'provider_type': 'provider_type',
        'provider_id': 'provider_id',
        'api_key': 'api_key',
        'provider_name': 'provider_name',
        'base_url': 'base_url',
        'custom_config': 'custom_config',
        'models': 'models',
        'api_type': 'api_type'
    }

    def __init__(self, provider_type=None, provider_id=None, api_key=None, provider_name=None, base_url=None, custom_config=None, models=None, api_type=None):
        r"""CreateProviderReq

        The model defined in huaweicloud sdk

        :param provider_type: 供应商类型（模板创建时与模板保持一致，自定义时为custom）。
        :type provider_type: str
        :param provider_id: 供应商标识（模板创建时与模板保持一致，自定义时可指定）。
        :type provider_id: str
        :param api_key: 供应商API Key（SCC加密存储）。
        :type api_key: str
        :param provider_name: 供应商名称（租户自定义）。
        :type provider_name: str
        :param base_url: 自定义Base URL。
        :type base_url: str
        :param custom_config: 
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        :param models: 批量创建关联的模型列表。
        :type models: list[:class:`huaweicloudsdkworkspace.v2.CreateModelReq`]
        :param api_type: 
        :type api_type: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        
        

        self._provider_type = None
        self._provider_id = None
        self._api_key = None
        self._provider_name = None
        self._base_url = None
        self._custom_config = None
        self._models = None
        self._api_type = None
        self.discriminator = None

        self.provider_type = provider_type
        self.provider_id = provider_id
        if api_key is not None:
            self.api_key = api_key
        self.provider_name = provider_name
        self.base_url = base_url
        if custom_config is not None:
            self.custom_config = custom_config
        if models is not None:
            self.models = models
        self.api_type = api_type

    @property
    def provider_type(self):
        r"""Gets the provider_type of this CreateProviderReq.

        供应商类型（模板创建时与模板保持一致，自定义时为custom）。

        :return: The provider_type of this CreateProviderReq.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this CreateProviderReq.

        供应商类型（模板创建时与模板保持一致，自定义时为custom）。

        :param provider_type: The provider_type of this CreateProviderReq.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def provider_id(self):
        r"""Gets the provider_id of this CreateProviderReq.

        供应商标识（模板创建时与模板保持一致，自定义时可指定）。

        :return: The provider_id of this CreateProviderReq.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this CreateProviderReq.

        供应商标识（模板创建时与模板保持一致，自定义时可指定）。

        :param provider_id: The provider_id of this CreateProviderReq.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def api_key(self):
        r"""Gets the api_key of this CreateProviderReq.

        供应商API Key（SCC加密存储）。

        :return: The api_key of this CreateProviderReq.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this CreateProviderReq.

        供应商API Key（SCC加密存储）。

        :param api_key: The api_key of this CreateProviderReq.
        :type api_key: str
        """
        self._api_key = api_key

    @property
    def provider_name(self):
        r"""Gets the provider_name of this CreateProviderReq.

        供应商名称（租户自定义）。

        :return: The provider_name of this CreateProviderReq.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this CreateProviderReq.

        供应商名称（租户自定义）。

        :param provider_name: The provider_name of this CreateProviderReq.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def base_url(self):
        r"""Gets the base_url of this CreateProviderReq.

        自定义Base URL。

        :return: The base_url of this CreateProviderReq.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this CreateProviderReq.

        自定义Base URL。

        :param base_url: The base_url of this CreateProviderReq.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def custom_config(self):
        r"""Gets the custom_config of this CreateProviderReq.

        :return: The custom_config of this CreateProviderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        return self._custom_config

    @custom_config.setter
    def custom_config(self, custom_config):
        r"""Sets the custom_config of this CreateProviderReq.

        :param custom_config: The custom_config of this CreateProviderReq.
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        self._custom_config = custom_config

    @property
    def models(self):
        r"""Gets the models of this CreateProviderReq.

        批量创建关联的模型列表。

        :return: The models of this CreateProviderReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.CreateModelReq`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this CreateProviderReq.

        批量创建关联的模型列表。

        :param models: The models of this CreateProviderReq.
        :type models: list[:class:`huaweicloudsdkworkspace.v2.CreateModelReq`]
        """
        self._models = models

    @property
    def api_type(self):
        r"""Gets the api_type of this CreateProviderReq.

        :return: The api_type of this CreateProviderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this CreateProviderReq.

        :param api_type: The api_type of this CreateProviderReq.
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
        if not isinstance(other, CreateProviderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
