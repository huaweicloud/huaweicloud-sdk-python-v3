# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConnectorsRequest:

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
        'scope': 'str',
        'category': 'str',
        'name': 'str',
        'operation_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'scope': 'scope',
        'category': 'category',
        'name': 'name',
        'operation_type': 'operation_type'
    }

    def __init__(self, offset=None, limit=None, scope=None, category=None, name=None, operation_type=None):
        """ShowConnectorsRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param scope: 连接器分类:onboard：查询所有的上架的、custom：自己创建的连接器
        :type scope: str
        :param category: 连接器种类（连接器市场的tab分类）
        :type category: str
        :param name: CustomConnectors的名字
        :type name: str
        :param operation_type: operation条件过滤
        :type operation_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._scope = None
        self._category = None
        self._name = None
        self._operation_type = None
        self.discriminator = None

        self.offset = offset
        self.limit = limit
        if scope is not None:
            self.scope = scope
        if category is not None:
            self.category = category
        if name is not None:
            self.name = name
        if operation_type is not None:
            self.operation_type = operation_type

    @property
    def offset(self):
        """Gets the offset of this ShowConnectorsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :return: The offset of this ShowConnectorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowConnectorsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0

        :param offset: The offset of this ShowConnectorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowConnectorsRequest.

        每页显示的条目数量

        :return: The limit of this ShowConnectorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowConnectorsRequest.

        每页显示的条目数量

        :param limit: The limit of this ShowConnectorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def scope(self):
        """Gets the scope of this ShowConnectorsRequest.

        连接器分类:onboard：查询所有的上架的、custom：自己创建的连接器

        :return: The scope of this ShowConnectorsRequest.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ShowConnectorsRequest.

        连接器分类:onboard：查询所有的上架的、custom：自己创建的连接器

        :param scope: The scope of this ShowConnectorsRequest.
        :type scope: str
        """
        self._scope = scope

    @property
    def category(self):
        """Gets the category of this ShowConnectorsRequest.

        连接器种类（连接器市场的tab分类）

        :return: The category of this ShowConnectorsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ShowConnectorsRequest.

        连接器种类（连接器市场的tab分类）

        :param category: The category of this ShowConnectorsRequest.
        :type category: str
        """
        self._category = category

    @property
    def name(self):
        """Gets the name of this ShowConnectorsRequest.

        CustomConnectors的名字

        :return: The name of this ShowConnectorsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowConnectorsRequest.

        CustomConnectors的名字

        :param name: The name of this ShowConnectorsRequest.
        :type name: str
        """
        self._name = name

    @property
    def operation_type(self):
        """Gets the operation_type of this ShowConnectorsRequest.

        operation条件过滤

        :return: The operation_type of this ShowConnectorsRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ShowConnectorsRequest.

        operation条件过滤

        :param operation_type: The operation_type of this ShowConnectorsRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

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
        if not isinstance(other, ShowConnectorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
