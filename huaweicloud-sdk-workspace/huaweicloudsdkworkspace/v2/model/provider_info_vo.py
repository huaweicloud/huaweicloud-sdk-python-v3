# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProviderInfoVO:

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
        'provider_name': 'str',
        'provider_type': 'str',
        'provider_id': 'str',
        'base_url': 'str',
        'connection_status': 'str',
        'model_count': 'int',
        'group_count': 'int',
        'last_verify_time': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'is_builtin': 'bool',
        'api_type': 'ApiType'
    }

    attribute_map = {
        'id': 'id',
        'provider_name': 'provider_name',
        'provider_type': 'provider_type',
        'provider_id': 'provider_id',
        'base_url': 'base_url',
        'connection_status': 'connection_status',
        'model_count': 'model_count',
        'group_count': 'group_count',
        'last_verify_time': 'last_verify_time',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'is_builtin': 'is_builtin',
        'api_type': 'api_type'
    }

    def __init__(self, id=None, provider_name=None, provider_type=None, provider_id=None, base_url=None, connection_status=None, model_count=None, group_count=None, last_verify_time=None, create_time=None, update_time=None, is_builtin=None, api_type=None):
        r"""ProviderInfoVO

        The model defined in huaweicloud sdk

        :param id: 供应商id。
        :type id: str
        :param provider_name: 供应商名称。
        :type provider_name: str
        :param provider_type: 供应商类型。
        :type provider_type: str
        :param provider_id: 供应商id。
        :type provider_id: str
        :param base_url: 供应商base_url。
        :type base_url: str
        :param connection_status: 连接状态（connected/disconnected/unverified）。
        :type connection_status: str
        :param model_count: 下属模型数量。
        :type model_count: int
        :param group_count: 关联的模型分组数量。
        :type group_count: int
        :param last_verify_time: 最后一次验证时间。
        :type last_verify_time: str
        :param create_time: 创建时间（ISO8601格式，UTC时区）。
        :type create_time: str
        :param update_time: 更新时间（ISO8601格式，UTC时区）。
        :type update_time: str
        :param is_builtin: 是否为内置供应商。
        :type is_builtin: bool
        :param api_type: 
        :type api_type: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        
        

        self._id = None
        self._provider_name = None
        self._provider_type = None
        self._provider_id = None
        self._base_url = None
        self._connection_status = None
        self._model_count = None
        self._group_count = None
        self._last_verify_time = None
        self._create_time = None
        self._update_time = None
        self._is_builtin = None
        self._api_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if provider_name is not None:
            self.provider_name = provider_name
        if provider_type is not None:
            self.provider_type = provider_type
        if provider_id is not None:
            self.provider_id = provider_id
        if base_url is not None:
            self.base_url = base_url
        if connection_status is not None:
            self.connection_status = connection_status
        if model_count is not None:
            self.model_count = model_count
        if group_count is not None:
            self.group_count = group_count
        if last_verify_time is not None:
            self.last_verify_time = last_verify_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if is_builtin is not None:
            self.is_builtin = is_builtin
        if api_type is not None:
            self.api_type = api_type

    @property
    def id(self):
        r"""Gets the id of this ProviderInfoVO.

        供应商id。

        :return: The id of this ProviderInfoVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProviderInfoVO.

        供应商id。

        :param id: The id of this ProviderInfoVO.
        :type id: str
        """
        self._id = id

    @property
    def provider_name(self):
        r"""Gets the provider_name of this ProviderInfoVO.

        供应商名称。

        :return: The provider_name of this ProviderInfoVO.
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        r"""Sets the provider_name of this ProviderInfoVO.

        供应商名称。

        :param provider_name: The provider_name of this ProviderInfoVO.
        :type provider_name: str
        """
        self._provider_name = provider_name

    @property
    def provider_type(self):
        r"""Gets the provider_type of this ProviderInfoVO.

        供应商类型。

        :return: The provider_type of this ProviderInfoVO.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this ProviderInfoVO.

        供应商类型。

        :param provider_type: The provider_type of this ProviderInfoVO.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def provider_id(self):
        r"""Gets the provider_id of this ProviderInfoVO.

        供应商id。

        :return: The provider_id of this ProviderInfoVO.
        :rtype: str
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        r"""Sets the provider_id of this ProviderInfoVO.

        供应商id。

        :param provider_id: The provider_id of this ProviderInfoVO.
        :type provider_id: str
        """
        self._provider_id = provider_id

    @property
    def base_url(self):
        r"""Gets the base_url of this ProviderInfoVO.

        供应商base_url。

        :return: The base_url of this ProviderInfoVO.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        r"""Sets the base_url of this ProviderInfoVO.

        供应商base_url。

        :param base_url: The base_url of this ProviderInfoVO.
        :type base_url: str
        """
        self._base_url = base_url

    @property
    def connection_status(self):
        r"""Gets the connection_status of this ProviderInfoVO.

        连接状态（connected/disconnected/unverified）。

        :return: The connection_status of this ProviderInfoVO.
        :rtype: str
        """
        return self._connection_status

    @connection_status.setter
    def connection_status(self, connection_status):
        r"""Sets the connection_status of this ProviderInfoVO.

        连接状态（connected/disconnected/unverified）。

        :param connection_status: The connection_status of this ProviderInfoVO.
        :type connection_status: str
        """
        self._connection_status = connection_status

    @property
    def model_count(self):
        r"""Gets the model_count of this ProviderInfoVO.

        下属模型数量。

        :return: The model_count of this ProviderInfoVO.
        :rtype: int
        """
        return self._model_count

    @model_count.setter
    def model_count(self, model_count):
        r"""Sets the model_count of this ProviderInfoVO.

        下属模型数量。

        :param model_count: The model_count of this ProviderInfoVO.
        :type model_count: int
        """
        self._model_count = model_count

    @property
    def group_count(self):
        r"""Gets the group_count of this ProviderInfoVO.

        关联的模型分组数量。

        :return: The group_count of this ProviderInfoVO.
        :rtype: int
        """
        return self._group_count

    @group_count.setter
    def group_count(self, group_count):
        r"""Sets the group_count of this ProviderInfoVO.

        关联的模型分组数量。

        :param group_count: The group_count of this ProviderInfoVO.
        :type group_count: int
        """
        self._group_count = group_count

    @property
    def last_verify_time(self):
        r"""Gets the last_verify_time of this ProviderInfoVO.

        最后一次验证时间。

        :return: The last_verify_time of this ProviderInfoVO.
        :rtype: str
        """
        return self._last_verify_time

    @last_verify_time.setter
    def last_verify_time(self, last_verify_time):
        r"""Sets the last_verify_time of this ProviderInfoVO.

        最后一次验证时间。

        :param last_verify_time: The last_verify_time of this ProviderInfoVO.
        :type last_verify_time: str
        """
        self._last_verify_time = last_verify_time

    @property
    def create_time(self):
        r"""Gets the create_time of this ProviderInfoVO.

        创建时间（ISO8601格式，UTC时区）。

        :return: The create_time of this ProviderInfoVO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ProviderInfoVO.

        创建时间（ISO8601格式，UTC时区）。

        :param create_time: The create_time of this ProviderInfoVO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ProviderInfoVO.

        更新时间（ISO8601格式，UTC时区）。

        :return: The update_time of this ProviderInfoVO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ProviderInfoVO.

        更新时间（ISO8601格式，UTC时区）。

        :param update_time: The update_time of this ProviderInfoVO.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def is_builtin(self):
        r"""Gets the is_builtin of this ProviderInfoVO.

        是否为内置供应商。

        :return: The is_builtin of this ProviderInfoVO.
        :rtype: bool
        """
        return self._is_builtin

    @is_builtin.setter
    def is_builtin(self, is_builtin):
        r"""Sets the is_builtin of this ProviderInfoVO.

        是否为内置供应商。

        :param is_builtin: The is_builtin of this ProviderInfoVO.
        :type is_builtin: bool
        """
        self._is_builtin = is_builtin

    @property
    def api_type(self):
        r"""Gets the api_type of this ProviderInfoVO.

        :return: The api_type of this ProviderInfoVO.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ApiType`
        """
        return self._api_type

    @api_type.setter
    def api_type(self, api_type):
        r"""Sets the api_type of this ProviderInfoVO.

        :param api_type: The api_type of this ProviderInfoVO.
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
        if not isinstance(other, ProviderInfoVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
