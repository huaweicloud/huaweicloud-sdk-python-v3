# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'sort': 'str',
        'type': 'str',
        'name': 'str',
        'vpc_id': 'str',
        'fuzzy_name': 'str',
        'subnet_id': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'type': 'type',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'fuzzy_name': 'fuzzy_name',
        'subnet_id': 'subnet_id'
    }

    def __init__(self, offset=None, limit=None, sort=None, type=None, name=None, vpc_id=None, fuzzy_name=None, subnet_id=None):
        """ListEndpointsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param limit: 每页显示的条目数量，不能小于1或大于1000
        :type limit: int
        :param sort: 指定查询排序
        :type sort: str
        :param type: 指定查询访问端点的类型
        :type type: str
        :param name: 指定查询访问端点的名称
        :type name: str
        :param vpc_id: 指定查询访问端点的vpcId
        :type vpc_id: str
        :param fuzzy_name: 指定查询访问端点的名称,模糊查询
        :type fuzzy_name: str
        :param subnet_id: 指定查询访问端点的SubnetId
        :type subnet_id: str
        """
        
        

        self._offset = None
        self._limit = None
        self._sort = None
        self._type = None
        self._name = None
        self._vpc_id = None
        self._fuzzy_name = None
        self._subnet_id = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if fuzzy_name is not None:
            self.fuzzy_name = fuzzy_name
        if subnet_id is not None:
            self.subnet_id = subnet_id

    @property
    def offset(self):
        """Gets the offset of this ListEndpointsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ListEndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEndpointsRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ListEndpointsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEndpointsRequest.

        每页显示的条目数量，不能小于1或大于1000

        :return: The limit of this ListEndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEndpointsRequest.

        每页显示的条目数量，不能小于1或大于1000

        :param limit: The limit of this ListEndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        """Gets the sort of this ListEndpointsRequest.

        指定查询排序

        :return: The sort of this ListEndpointsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListEndpointsRequest.

        指定查询排序

        :param sort: The sort of this ListEndpointsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def type(self):
        """Gets the type of this ListEndpointsRequest.

        指定查询访问端点的类型

        :return: The type of this ListEndpointsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListEndpointsRequest.

        指定查询访问端点的类型

        :param type: The type of this ListEndpointsRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ListEndpointsRequest.

        指定查询访问端点的名称

        :return: The name of this ListEndpointsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListEndpointsRequest.

        指定查询访问端点的名称

        :param name: The name of this ListEndpointsRequest.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        """Gets the vpc_id of this ListEndpointsRequest.

        指定查询访问端点的vpcId

        :return: The vpc_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this ListEndpointsRequest.

        指定查询访问端点的vpcId

        :param vpc_id: The vpc_id of this ListEndpointsRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def fuzzy_name(self):
        """Gets the fuzzy_name of this ListEndpointsRequest.

        指定查询访问端点的名称,模糊查询

        :return: The fuzzy_name of this ListEndpointsRequest.
        :rtype: str
        """
        return self._fuzzy_name

    @fuzzy_name.setter
    def fuzzy_name(self, fuzzy_name):
        """Sets the fuzzy_name of this ListEndpointsRequest.

        指定查询访问端点的名称,模糊查询

        :param fuzzy_name: The fuzzy_name of this ListEndpointsRequest.
        :type fuzzy_name: str
        """
        self._fuzzy_name = fuzzy_name

    @property
    def subnet_id(self):
        """Gets the subnet_id of this ListEndpointsRequest.

        指定查询访问端点的SubnetId

        :return: The subnet_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this ListEndpointsRequest.

        指定查询访问端点的SubnetId

        :param subnet_id: The subnet_id of this ListEndpointsRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

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
        if not isinstance(other, ListEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
