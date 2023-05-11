# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIaConfigsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'ia_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'node_id': 'node_id',
        'ia_id': 'ia_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, node_id=None, ia_id=None, offset=None, limit=None):
        """ListIaConfigsRequest

        The model defined in huaweicloud sdk

        :param node_id: 边缘节点ID
        :type node_id: str
        :param ia_id: 边侧第三方应用的模块ID
        :type ia_id: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页记录数，取值范围为非负整数，默认值为10
        :type limit: int
        """
        
        

        self._node_id = None
        self._ia_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.node_id = node_id
        self.ia_id = ia_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def node_id(self):
        """Gets the node_id of this ListIaConfigsRequest.

        边缘节点ID

        :return: The node_id of this ListIaConfigsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this ListIaConfigsRequest.

        边缘节点ID

        :param node_id: The node_id of this ListIaConfigsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def ia_id(self):
        """Gets the ia_id of this ListIaConfigsRequest.

        边侧第三方应用的模块ID

        :return: The ia_id of this ListIaConfigsRequest.
        :rtype: str
        """
        return self._ia_id

    @ia_id.setter
    def ia_id(self, ia_id):
        """Sets the ia_id of this ListIaConfigsRequest.

        边侧第三方应用的模块ID

        :param ia_id: The ia_id of this ListIaConfigsRequest.
        :type ia_id: str
        """
        self._ia_id = ia_id

    @property
    def offset(self):
        """Gets the offset of this ListIaConfigsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListIaConfigsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListIaConfigsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListIaConfigsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListIaConfigsRequest.

        每页记录数，取值范围为非负整数，默认值为10

        :return: The limit of this ListIaConfigsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIaConfigsRequest.

        每页记录数，取值范围为非负整数，默认值为10

        :param limit: The limit of this ListIaConfigsRequest.
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
        if not isinstance(other, ListIaConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
