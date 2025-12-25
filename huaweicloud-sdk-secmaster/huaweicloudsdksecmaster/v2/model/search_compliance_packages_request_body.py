# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchCompliancePackagesRequestBody:

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
        'name': 'str',
        'description': 'str',
        'type': 'int',
        'state': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'state': 'state'
    }

    def __init__(self, limit=None, offset=None, name=None, description=None, type=None, state=None):
        r"""SearchCompliancePackagesRequestBody

        The model defined in huaweicloud sdk

        :param limit: 分页大小
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param name: 遵从包名称
        :type name: str
        :param description: 遵从包描述
        :type description: str
        :param type: 表示该遵从包的类型 0：内置 1: 自定义
        :type type: int
        :param state: 表示该遵从包的状态 0：停用 1: 启用
        :type state: int
        """
        
        

        self._limit = None
        self._offset = None
        self._name = None
        self._description = None
        self._type = None
        self._state = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if state is not None:
            self.state = state

    @property
    def limit(self):
        r"""Gets the limit of this SearchCompliancePackagesRequestBody.

        分页大小

        :return: The limit of this SearchCompliancePackagesRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchCompliancePackagesRequestBody.

        分页大小

        :param limit: The limit of this SearchCompliancePackagesRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this SearchCompliancePackagesRequestBody.

        偏移量

        :return: The offset of this SearchCompliancePackagesRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchCompliancePackagesRequestBody.

        偏移量

        :param offset: The offset of this SearchCompliancePackagesRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this SearchCompliancePackagesRequestBody.

        遵从包名称

        :return: The name of this SearchCompliancePackagesRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SearchCompliancePackagesRequestBody.

        遵从包名称

        :param name: The name of this SearchCompliancePackagesRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this SearchCompliancePackagesRequestBody.

        遵从包描述

        :return: The description of this SearchCompliancePackagesRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SearchCompliancePackagesRequestBody.

        遵从包描述

        :param description: The description of this SearchCompliancePackagesRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        r"""Gets the type of this SearchCompliancePackagesRequestBody.

        表示该遵从包的类型 0：内置 1: 自定义

        :return: The type of this SearchCompliancePackagesRequestBody.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SearchCompliancePackagesRequestBody.

        表示该遵从包的类型 0：内置 1: 自定义

        :param type: The type of this SearchCompliancePackagesRequestBody.
        :type type: int
        """
        self._type = type

    @property
    def state(self):
        r"""Gets the state of this SearchCompliancePackagesRequestBody.

        表示该遵从包的状态 0：停用 1: 启用

        :return: The state of this SearchCompliancePackagesRequestBody.
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this SearchCompliancePackagesRequestBody.

        表示该遵从包的状态 0：停用 1: 启用

        :param state: The state of this SearchCompliancePackagesRequestBody.
        :type state: int
        """
        self._state = state

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
        if not isinstance(other, SearchCompliancePackagesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
