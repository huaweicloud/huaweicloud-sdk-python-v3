# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRemoteModelsReq:

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
        'base_url': 'str',
        'custom_config': 'ProviderCustomConfig',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'id': 'id',
        'provider_type': 'provider_type',
        'provider_id': 'provider_id',
        'api_key': 'api_key',
        'base_url': 'base_url',
        'custom_config': 'custom_config',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, id=None, provider_type=None, provider_id=None, api_key=None, base_url=None, custom_config=None, limit=None, offset=None):
        r"""ListRemoteModelsReq

        The model defined in huaweicloud sdk

        :param id: 供应商主键ID。传入时，其他空字段从数据库已保存的供应商记录中补充。
        :type id: str
        :param provider_type: 供应商类型。
        :type provider_type: str
        :param provider_id: 供应商id。
        :type provider_id: str
        :param api_key: 供应商API Key（SCC加密存储）。
        :type api_key: str
        :param base_url: 供应商base_url。
        :type base_url: str
        :param custom_config: 
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        :param limit: 每页数量，默认20，最大100。
        :type limit: int
        :param offset: 偏移量，从0开始。
        :type offset: int
        """
        
        

        self._id = None
        self._provider_type = None
        self._provider_id = None
        self._api_key = None
        self._base_url = None
        self._custom_config = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if provider_type is not None:
            self.provider_type = provider_type
        if provider_id is not None:
            self.provider_id = provider_id
        if api_key is not None:
            self.api_key = api_key
        if base_url is not None:
            self.base_url = base_url
        if custom_config is not None:
            self.custom_config = custom_config
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def id(self):
        r"""Gets the id of this ListRemoteModelsReq.

        供应商主键ID。传入时，其他空字段从数据库已保存的供应商记录中补充。

        :return: The id of this ListRemoteModelsReq.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListRemoteModelsReq.

        供应商主键ID。传入时，其他空字段从数据库已保存的供应商记录中补充。

        :param id: The id of this ListRemoteModelsReq.
        :type id: str
        """
        self._id = id

    @property
    def provider_type(self):
        r"""Gets the provider_type of this ListRemoteModelsReq.

        供应商类型。

        :return: The provider_type of this ListRemoteModelsReq.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this ListRemoteModelsReq.

        供应商类型。

        :param provider_type: The provider_type of this ListRemoteModelsReq.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ListRemoteModelsReq.

        供应商id。

        :return: The provider_id of this ListRemoteModelsReq.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ListRemoteModelsReq.

        供应商id。

        :param provider_id: The provider_id of this ListRemoteModelsReq.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def api_key(self):
        r"""Gets the api_key of this ListRemoteModelsReq.

        供应商API Key（SCC加密存储）。

        :return: The api_key of this ListRemoteModelsReq.
        :rtype: str
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        r"""Sets the api_key of this ListRemoteModelsReq.

        供应商API Key（SCC加密存储）。

        :param api_key: The api_key of this ListRemoteModelsReq.
        :type api_key: str
        """
        self._api_key = api_key

    @property
    def base_url(self):
        r"""Gets the base_url of this ListRemoteModelsReq.

        供应商base_url。

        :return: The base_url of this ListRemoteModelsReq.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this ListRemoteModelsReq.

        供应商base_url。

        :param base_url: The base_url of this ListRemoteModelsReq.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def custom_config(self):
        r"""Gets the custom_config of this ListRemoteModelsReq.

        :return: The custom_config of this ListRemoteModelsReq.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        return self._custom_config

    @custom_config.setter
    def custom_config(self, custom_config):
        r"""Sets the custom_config of this ListRemoteModelsReq.

        :param custom_config: The custom_config of this ListRemoteModelsReq.
        :type custom_config: :class:`huaweicloudsdkworkspace.v2.ProviderCustomConfig`
        """
        self._custom_config = custom_config

    @property
    def limit(self):
        r"""Gets the limit of this ListRemoteModelsReq.

        每页数量，默认20，最大100。

        :return: The limit of this ListRemoteModelsReq.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRemoteModelsReq.

        每页数量，默认20，最大100。

        :param limit: The limit of this ListRemoteModelsReq.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListRemoteModelsReq.

        偏移量，从0开始。

        :return: The offset of this ListRemoteModelsReq.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRemoteModelsReq.

        偏移量，从0开始。

        :param offset: The offset of this ListRemoteModelsReq.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListRemoteModelsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
