# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unit': 'str',
        'type': 'str',
        'group_id': 'str',
        'name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'unit': 'unit',
        'type': 'type',
        'group_id': 'group_id',
        'name': 'name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, unit=None, type=None, group_id=None, name=None, offset=None, limit=None):
        """ListGroupsRequest

        The model defined in huaweicloud sdk

        :param unit: 存储用量单位
        :type unit: str
        :param type: 存储类型，有资产存储(取值:AssetStorage)、设备存储(取值:DeviceStorage)两种类型
        :type type: str
        :param group_id: 存储组 ID
        :type group_id: str
        :param name: 存储组名称
        :type name: str
        :param offset: 页码
        :type offset: int
        :param limit: 返回条数限制
        :type limit: int
        """
        
        

        self._unit = None
        self._type = None
        self._group_id = None
        self._name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if unit is not None:
            self.unit = unit
        if type is not None:
            self.type = type
        if group_id is not None:
            self.group_id = group_id
        if name is not None:
            self.name = name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def unit(self):
        """Gets the unit of this ListGroupsRequest.

        存储用量单位

        :return: The unit of this ListGroupsRequest.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ListGroupsRequest.

        存储用量单位

        :param unit: The unit of this ListGroupsRequest.
        :type unit: str
        """
        self._unit = unit

    @property
    def type(self):
        """Gets the type of this ListGroupsRequest.

        存储类型，有资产存储(取值:AssetStorage)、设备存储(取值:DeviceStorage)两种类型

        :return: The type of this ListGroupsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListGroupsRequest.

        存储类型，有资产存储(取值:AssetStorage)、设备存储(取值:DeviceStorage)两种类型

        :param type: The type of this ListGroupsRequest.
        :type type: str
        """
        self._type = type

    @property
    def group_id(self):
        """Gets the group_id of this ListGroupsRequest.

        存储组 ID

        :return: The group_id of this ListGroupsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListGroupsRequest.

        存储组 ID

        :param group_id: The group_id of this ListGroupsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def name(self):
        """Gets the name of this ListGroupsRequest.

        存储组名称

        :return: The name of this ListGroupsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListGroupsRequest.

        存储组名称

        :param name: The name of this ListGroupsRequest.
        :type name: str
        """
        self._name = name

    @property
    def offset(self):
        """Gets the offset of this ListGroupsRequest.

        页码

        :return: The offset of this ListGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListGroupsRequest.

        页码

        :param offset: The offset of this ListGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListGroupsRequest.

        返回条数限制

        :return: The limit of this ListGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGroupsRequest.

        返回条数限制

        :param limit: The limit of this ListGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
