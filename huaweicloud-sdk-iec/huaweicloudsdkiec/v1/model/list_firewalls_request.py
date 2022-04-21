# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFirewallsRequest:

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
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, limit=None, offset=None, id=None, name=None):
        """ListFirewallsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页返回的个数  取值范围：0~1000
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param id: 通过ID过滤网络ACL。
        :type id: str
        :param name: 通过name模糊匹配网络ACL。
        :type name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._id = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def limit(self):
        """Gets the limit of this ListFirewallsRequest.

        每页返回的个数  取值范围：0~1000

        :return: The limit of this ListFirewallsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListFirewallsRequest.

        每页返回的个数  取值范围：0~1000

        :param limit: The limit of this ListFirewallsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListFirewallsRequest.

        查询的偏移量。

        :return: The offset of this ListFirewallsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListFirewallsRequest.

        查询的偏移量。

        :param offset: The offset of this ListFirewallsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def id(self):
        """Gets the id of this ListFirewallsRequest.

        通过ID过滤网络ACL。

        :return: The id of this ListFirewallsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListFirewallsRequest.

        通过ID过滤网络ACL。

        :param id: The id of this ListFirewallsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListFirewallsRequest.

        通过name模糊匹配网络ACL。

        :return: The name of this ListFirewallsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListFirewallsRequest.

        通过name模糊匹配网络ACL。

        :param name: The name of this ListFirewallsRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListFirewallsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
