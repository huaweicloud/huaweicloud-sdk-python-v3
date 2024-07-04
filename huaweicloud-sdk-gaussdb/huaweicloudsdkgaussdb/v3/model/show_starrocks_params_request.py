# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStarrocksParamsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'node_type': 'str',
        'offset': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'node_type': 'node_type',
        'offset': 'offset',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, node_type=None, offset=None, limit=None, x_language=None):
        """ShowStarrocksParamsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param node_type: 节点类型。取值范围: - be - fe
        :type node_type: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为100，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._node_type = None
        self._offset = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.node_type = node_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowStarrocksParamsRequest.

        实例ID，严格匹配UUID规则。

        :return: The instance_id of this ShowStarrocksParamsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowStarrocksParamsRequest.

        实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ShowStarrocksParamsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_type(self):
        """Gets the node_type of this ShowStarrocksParamsRequest.

        节点类型。取值范围: - be - fe

        :return: The node_type of this ShowStarrocksParamsRequest.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this ShowStarrocksParamsRequest.

        节点类型。取值范围: - be - fe

        :param node_type: The node_type of this ShowStarrocksParamsRequest.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def offset(self):
        """Gets the offset of this ShowStarrocksParamsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowStarrocksParamsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowStarrocksParamsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowStarrocksParamsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowStarrocksParamsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowStarrocksParamsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowStarrocksParamsRequest.

        查询记录数。默认为100，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowStarrocksParamsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ShowStarrocksParamsRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ShowStarrocksParamsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowStarrocksParamsRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ShowStarrocksParamsRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ShowStarrocksParamsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
