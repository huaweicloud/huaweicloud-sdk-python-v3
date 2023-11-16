# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyRequest:

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
        'policy_name': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'policy_name': 'policy_name'
    }

    def __init__(self, offset=None, limit=None, policy_name=None):
        """ListPolicyRequest

        The model defined in huaweicloud sdk

        :param offset: 开始查询的偏移量,默认值:0
        :type offset: int
        :param limit: 每页显示的条目数量,默认值:2000
        :type limit: int
        :param policy_name: 策略名
        :type policy_name: str
        """
        
        

        self._offset = None
        self._limit = None
        self._policy_name = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if policy_name is not None:
            self.policy_name = policy_name

    @property
    def offset(self):
        """Gets the offset of this ListPolicyRequest.

        开始查询的偏移量,默认值:0

        :return: The offset of this ListPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPolicyRequest.

        开始查询的偏移量,默认值:0

        :param offset: The offset of this ListPolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPolicyRequest.

        每页显示的条目数量,默认值:2000

        :return: The limit of this ListPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPolicyRequest.

        每页显示的条目数量,默认值:2000

        :param limit: The limit of this ListPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def policy_name(self):
        """Gets the policy_name of this ListPolicyRequest.

        策略名

        :return: The policy_name of this ListPolicyRequest.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this ListPolicyRequest.

        策略名

        :param policy_name: The policy_name of this ListPolicyRequest.
        :type policy_name: str
        """
        self._policy_name = policy_name

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
        if not isinstance(other, ListPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
