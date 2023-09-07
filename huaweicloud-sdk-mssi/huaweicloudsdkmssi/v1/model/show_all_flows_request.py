# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllFlowsRequest:

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
        'type': 'str',
        'name': 'str',
        'have_child_flow': 'bool',
        'ids': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type',
        'name': 'name',
        'have_child_flow': 'have_child_flow',
        'ids': 'ids'
    }

    def __init__(self, offset=None, limit=None, type=None, name=None, have_child_flow=None, ids=None):
        """ShowAllFlowsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量，limit大于等于1
        :type limit: int
        :param type: 类型
        :type type: str
        :param name: 流名称，支持模糊查询
        :type name: str
        :param have_child_flow: 是否包含子流程
        :type have_child_flow: bool
        :param ids: ids
        :type ids: str
        """
        
        

        self._offset = None
        self._limit = None
        self._type = None
        self._name = None
        self._have_child_flow = None
        self._ids = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if have_child_flow is not None:
            self.have_child_flow = have_child_flow
        if ids is not None:
            self.ids = ids

    @property
    def offset(self):
        """Gets the offset of this ShowAllFlowsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ShowAllFlowsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowAllFlowsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ShowAllFlowsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowAllFlowsRequest.

        每页显示的条目数量，limit大于等于1

        :return: The limit of this ShowAllFlowsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowAllFlowsRequest.

        每页显示的条目数量，limit大于等于1

        :param limit: The limit of this ShowAllFlowsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ShowAllFlowsRequest.

        类型

        :return: The type of this ShowAllFlowsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowAllFlowsRequest.

        类型

        :param type: The type of this ShowAllFlowsRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ShowAllFlowsRequest.

        流名称，支持模糊查询

        :return: The name of this ShowAllFlowsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAllFlowsRequest.

        流名称，支持模糊查询

        :param name: The name of this ShowAllFlowsRequest.
        :type name: str
        """
        self._name = name

    @property
    def have_child_flow(self):
        """Gets the have_child_flow of this ShowAllFlowsRequest.

        是否包含子流程

        :return: The have_child_flow of this ShowAllFlowsRequest.
        :rtype: bool
        """
        return self._have_child_flow

    @have_child_flow.setter
    def have_child_flow(self, have_child_flow):
        """Sets the have_child_flow of this ShowAllFlowsRequest.

        是否包含子流程

        :param have_child_flow: The have_child_flow of this ShowAllFlowsRequest.
        :type have_child_flow: bool
        """
        self._have_child_flow = have_child_flow

    @property
    def ids(self):
        """Gets the ids of this ShowAllFlowsRequest.

        ids

        :return: The ids of this ShowAllFlowsRequest.
        :rtype: str
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this ShowAllFlowsRequest.

        ids

        :param ids: The ids of this ShowAllFlowsRequest.
        :type ids: str
        """
        self._ids = ids

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
        if not isinstance(other, ShowAllFlowsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
