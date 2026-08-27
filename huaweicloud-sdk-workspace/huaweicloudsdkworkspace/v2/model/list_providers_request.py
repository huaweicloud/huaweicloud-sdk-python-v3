# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProvidersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'group_id': 'str',
        'status': 'str',
        'provider_type': 'str',
        'name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'group_id': 'group_id',
        'status': 'status',
        'provider_type': 'provider_type',
        'name': 'name'
    }

    def __init__(self, limit=None, offset=None, group_id=None, status=None, provider_type=None, name=None):
        r"""ListProvidersRequest

        The model defined in huaweicloud sdk

        :param limit: 每页数量，默认10，最大100。
        :type limit: int
        :param offset: 偏移量，默认0。
        :type offset: int
        :param group_id: 按分组筛选（关联查询）。
        :type group_id: str
        :param status: 状态筛选（connected-已连接，disconnected-已断开，unverified-未验证）。
        :type status: str
        :param provider_type: 供应商类型筛选。
        :type provider_type: str
        :param name: 名称模糊搜索。
        :type name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._group_id = None
        self._status = None
        self._provider_type = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if group_id is not None:
            self.group_id = group_id
        if status is not None:
            self.status = status
        if provider_type is not None:
            self.provider_type = provider_type
        if name is not None:
            self.name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListProvidersRequest.

        每页数量，默认10，最大100。

        :return: The limit of this ListProvidersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProvidersRequest.

        每页数量，默认10，最大100。

        :param limit: The limit of this ListProvidersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListProvidersRequest.

        偏移量，默认0。

        :return: The offset of this ListProvidersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProvidersRequest.

        偏移量，默认0。

        :param offset: The offset of this ListProvidersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def group_id(self):
        r"""Gets the group_id of this ListProvidersRequest.

        按分组筛选（关联查询）。

        :return: The group_id of this ListProvidersRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ListProvidersRequest.

        按分组筛选（关联查询）。

        :param group_id: The group_id of this ListProvidersRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def status(self):
        r"""Gets the status of this ListProvidersRequest.

        状态筛选（connected-已连接，disconnected-已断开，unverified-未验证）。

        :return: The status of this ListProvidersRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListProvidersRequest.

        状态筛选（connected-已连接，disconnected-已断开，unverified-未验证）。

        :param status: The status of this ListProvidersRequest.
        :type status: str
        """
        self._status = status

    @property
    def provider_type(self):
        r"""Gets the provider_type of this ListProvidersRequest.

        供应商类型筛选。

        :return: The provider_type of this ListProvidersRequest.
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        r"""Sets the provider_type of this ListProvidersRequest.

        供应商类型筛选。

        :param provider_type: The provider_type of this ListProvidersRequest.
        :type provider_type: str
        """
        self._provider_type = provider_type

    @property
    def name(self):
        r"""Gets the name of this ListProvidersRequest.

        名称模糊搜索。

        :return: The name of this ListProvidersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListProvidersRequest.

        名称模糊搜索。

        :param name: The name of this ListProvidersRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListProvidersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
