# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyProviderReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'provider_type': 'str',
        'provider_id': 'str',
        'api_key': 'str',
        'api_type': 'ApiType',
        'base_url': 'str',
        'custom_config': 'ProviderCustomConfig',
        'model_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'provider_type': 'provider_type',
        'provider_id': 'provider_id',
        'api_key': 'api_key',
        'api_type': 'api_type',
        'base_url': 'base_url',
        'custom_config': 'custom_config',
        'model_id': 'model_id'
    }

    def __init__(self, id=None, provider_type=None, provider_id=None, api_key=None, api_type=None, base_url=None, custom_config=None, model_id=None):
        r"""VerifyProviderReq

        The model defined in huaweicloud sdk

        :param id: 供应商主键ID。传入时，其他空字段从数据库已保存的供应商记录中补充。
        :type id: str
        :param provider_type: 供应商类型。
        :type provider_type: str
        :param provider_id: 供应商id（从模板实例化后的ID）。
        :type provider_id: str
        :param api_key: 供应商API Key（SCC加密存储）。
        :type api_key: str
        :param api_type: 
        :type api_type: :class:`huaweicloudsdkworkspace.v2.ApiType`
        :param base_url: 供应商base_url。
        :type base_url: str
        :param custom_config: 
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        :param model_id: 用于验证连接的模型ID。调用Chat Completion接口时作为model参数传入。
        :type model_id: str
        """
        
        

        self._id = None
        self._provider_type = None
        self._provider_id = None
        self._api_key = None
        self._api_type = None
        self._base_url = None
        self._custom_config = None
        self._model_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if provider_type is not None:
            self.provider_type = provider_type
        if provider_id is not None:
            self.provider_id = provider_id
        if api_key is not None:
            self.api_key = api_key
        if api_type is not None:
            self.api_type = api_type
        if base_url is not None:
            self.base_url = base_url
        if custom_config is not None:
            self.custom_config = custom_config
        if model_id is not None:
            self.model_id = model_id

    @property
    def id(self):
        r"""Gets the id of this VerifyProviderReq.

        供应商主键ID。传入时，其他空字段从数据库已保存的供应商记录中补充。

        :return: The id of this VerifyProviderReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VerifyProviderReq.

        供应商主键ID。传入时，其他空字段从数据库已保存的供应商记录中补充。

        :param id: The id of this VerifyProviderReq.
        :type id: str
        """
        self._id = id

    @property
    def provider_type(self):
        r"""Gets the provider_type of this VerifyProviderReq.

        供应商类型。

        :return: The provider_type of this VerifyProviderReq.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this VerifyProviderReq.

        供应商类型。

        :param provider_type: The provider_type of this VerifyProviderReq.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def provider_id(self):
        r"""Gets the provider_id of this VerifyProviderReq.

        供应商id（从模板实例化后的ID）。

        :return: The provider_id of this VerifyProviderReq.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this VerifyProviderReq.

        供应商id（从模板实例化后的ID）。

        :param provider_id: The provider_id of this VerifyProviderReq.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def api_key(self):
        r"""Gets the api_key of this VerifyProviderReq.

        供应商API Key（SCC加密存储）。

        :return: The api_key of this VerifyProviderReq.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this VerifyProviderReq.

        供应商API Key（SCC加密存储）。

        :param api_key: The api_key of this VerifyProviderReq.
        :type api_key: str
        """
        self._api_key = api_key

    @property
    def api_type(self):
        r"""Gets the api_type of this VerifyProviderReq.

        :return: The api_type of this VerifyProviderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this VerifyProviderReq.

        :param api_type: The api_type of this VerifyProviderReq.
        :type api_type: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        self._api_type = api_type

    @property
    def base_url(self):
        r"""Gets the base_url of this VerifyProviderReq.

        供应商base_url。

        :return: The base_url of this VerifyProviderReq.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this VerifyProviderReq.

        供应商base_url。

        :param base_url: The base_url of this VerifyProviderReq.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def custom_config(self):
        r"""Gets the custom_config of this VerifyProviderReq.

        :return: The custom_config of this VerifyProviderReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        return self._custom_config

    @custom_config.setter
    def custom_config(self, custom_config):
        r"""Sets the custom_config of this VerifyProviderReq.

        :param custom_config: The custom_config of this VerifyProviderReq.
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        self._custom_config = custom_config

    @property
    def model_id(self):
        r"""Gets the model_id of this VerifyProviderReq.

        用于验证连接的模型ID。调用Chat Completion接口时作为model参数传入。

        :return: The model_id of this VerifyProviderReq.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this VerifyProviderReq.

        用于验证连接的模型ID。调用Chat Completion接口时作为model参数传入。

        :param model_id: The model_id of this VerifyProviderReq.
        :type model_id: str
        """
        self._model_id = model_id

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
        if not isinstance(other, VerifyProviderReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
