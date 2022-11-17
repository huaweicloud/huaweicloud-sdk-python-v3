# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMqsInstanceTopicAccessPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'policies': 'list[ShowMqsInstanceTopicAccessPolicyRespPolicies]',
        'total': 'int',
        'size': 'int',
        'operation': 'str'
    }

    attribute_map = {
        'name': 'name',
        'policies': 'policies',
        'total': 'total',
        'size': 'size',
        'operation': 'operation'
    }

    def __init__(self, name=None, policies=None, total=None, size=None, operation=None):
        """ShowMqsInstanceTopicAccessPolicyResponse

        The model defined in huaweicloud sdk

        :param name: topic名称。
        :type name: str
        :param policies: 策略列表。
        :type policies: list[:class:`huaweicloudsdkroma.v2.ShowMqsInstanceTopicAccessPolicyRespPolicies`]
        :param total: 权限策略的总数。
        :type total: int
        :param size: 查询权限策略的数量。
        :type size: int
        :param operation: topic名称。
        :type operation: str
        """
        
        super(ShowMqsInstanceTopicAccessPolicyResponse, self).__init__()

        self._name = None
        self._policies = None
        self._total = None
        self._size = None
        self._operation = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if policies is not None:
            self.policies = policies
        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if operation is not None:
            self.operation = operation

    @property
    def name(self):
        """Gets the name of this ShowMqsInstanceTopicAccessPolicyResponse.

        topic名称。

        :return: The name of this ShowMqsInstanceTopicAccessPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowMqsInstanceTopicAccessPolicyResponse.

        topic名称。

        :param name: The name of this ShowMqsInstanceTopicAccessPolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def policies(self):
        """Gets the policies of this ShowMqsInstanceTopicAccessPolicyResponse.

        策略列表。

        :return: The policies of this ShowMqsInstanceTopicAccessPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.ShowMqsInstanceTopicAccessPolicyRespPolicies`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ShowMqsInstanceTopicAccessPolicyResponse.

        策略列表。

        :param policies: The policies of this ShowMqsInstanceTopicAccessPolicyResponse.
        :type policies: list[:class:`huaweicloudsdkroma.v2.ShowMqsInstanceTopicAccessPolicyRespPolicies`]
        """
        self._policies = policies

    @property
    def total(self):
        """Gets the total of this ShowMqsInstanceTopicAccessPolicyResponse.

        权限策略的总数。

        :return: The total of this ShowMqsInstanceTopicAccessPolicyResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowMqsInstanceTopicAccessPolicyResponse.

        权限策略的总数。

        :param total: The total of this ShowMqsInstanceTopicAccessPolicyResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        """Gets the size of this ShowMqsInstanceTopicAccessPolicyResponse.

        查询权限策略的数量。

        :return: The size of this ShowMqsInstanceTopicAccessPolicyResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ShowMqsInstanceTopicAccessPolicyResponse.

        查询权限策略的数量。

        :param size: The size of this ShowMqsInstanceTopicAccessPolicyResponse.
        :type size: int
        """
        self._size = size

    @property
    def operation(self):
        """Gets the operation of this ShowMqsInstanceTopicAccessPolicyResponse.

        topic名称。

        :return: The operation of this ShowMqsInstanceTopicAccessPolicyResponse.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this ShowMqsInstanceTopicAccessPolicyResponse.

        topic名称。

        :param operation: The operation of this ShowMqsInstanceTopicAccessPolicyResponse.
        :type operation: str
        """
        self._operation = operation

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
        if not isinstance(other, ShowMqsInstanceTopicAccessPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
