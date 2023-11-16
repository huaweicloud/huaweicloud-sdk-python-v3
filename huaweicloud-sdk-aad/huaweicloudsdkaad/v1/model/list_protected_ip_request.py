# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectedIpRequest:

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
        'package_id': 'str',
        'policy_id': 'str',
        'ip': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'package_id': 'package_id',
        'policy_id': 'policy_id',
        'ip': 'ip',
        'tag': 'tag'
    }

    def __init__(self, offset=None, limit=None, package_id=None, policy_id=None, ip=None, tag=None):
        """ListProtectedIpRequest

        The model defined in huaweicloud sdk

        :param offset: 开始查询的偏移量,默认值:0
        :type offset: int
        :param limit: 每页显示的条目数量,默认值:2000
        :type limit: int
        :param package_id: 防护包id
        :type package_id: str
        :param policy_id: 策略id
        :type policy_id: str
        :param ip: 防护ip
        :type ip: str
        :param tag: 本地标签
        :type tag: str
        """
        
        

        self._offset = None
        self._limit = None
        self._package_id = None
        self._policy_id = None
        self._ip = None
        self._tag = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if package_id is not None:
            self.package_id = package_id
        if policy_id is not None:
            self.policy_id = policy_id
        if ip is not None:
            self.ip = ip
        if tag is not None:
            self.tag = tag

    @property
    def offset(self):
        """Gets the offset of this ListProtectedIpRequest.

        开始查询的偏移量,默认值:0

        :return: The offset of this ListProtectedIpRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListProtectedIpRequest.

        开始查询的偏移量,默认值:0

        :param offset: The offset of this ListProtectedIpRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListProtectedIpRequest.

        每页显示的条目数量,默认值:2000

        :return: The limit of this ListProtectedIpRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListProtectedIpRequest.

        每页显示的条目数量,默认值:2000

        :param limit: The limit of this ListProtectedIpRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def package_id(self):
        """Gets the package_id of this ListProtectedIpRequest.

        防护包id

        :return: The package_id of this ListProtectedIpRequest.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id):
        """Sets the package_id of this ListProtectedIpRequest.

        防护包id

        :param package_id: The package_id of this ListProtectedIpRequest.
        :type package_id: str
        """
        self._package_id = package_id

    @property
    def policy_id(self):
        """Gets the policy_id of this ListProtectedIpRequest.

        策略id

        :return: The policy_id of this ListProtectedIpRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this ListProtectedIpRequest.

        策略id

        :param policy_id: The policy_id of this ListProtectedIpRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def ip(self):
        """Gets the ip of this ListProtectedIpRequest.

        防护ip

        :return: The ip of this ListProtectedIpRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this ListProtectedIpRequest.

        防护ip

        :param ip: The ip of this ListProtectedIpRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def tag(self):
        """Gets the tag of this ListProtectedIpRequest.

        本地标签

        :return: The tag of this ListProtectedIpRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ListProtectedIpRequest.

        本地标签

        :param tag: The tag of this ListProtectedIpRequest.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ListProtectedIpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
