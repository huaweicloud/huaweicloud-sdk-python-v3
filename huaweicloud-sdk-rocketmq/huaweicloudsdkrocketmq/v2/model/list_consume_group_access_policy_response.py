# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConsumeGroupAccessPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'policies': 'list[ListAccessPolicyRespPolicies]',
        'total': 'float',
        'name': 'str'
    }

    attribute_map = {
        'policies': 'policies',
        'total': 'total',
        'name': 'name'
    }

    def __init__(self, policies=None, total=None, name=None):
        """ListConsumeGroupAccessPolicyResponse

        The model defined in huaweicloud sdk

        :param policies: 用户列表。
        :type policies: list[:class:`huaweicloudsdkrocketmq.v2.ListAccessPolicyRespPolicies`]
        :param total: 总用户个数。
        :type total: float
        :param name: 主题或消费组名称。
        :type name: str
        """
        
        super(ListConsumeGroupAccessPolicyResponse, self).__init__()

        self._policies = None
        self._total = None
        self._name = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies
        if total is not None:
            self.total = total
        if name is not None:
            self.name = name

    @property
    def policies(self):
        """Gets the policies of this ListConsumeGroupAccessPolicyResponse.

        用户列表。

        :return: The policies of this ListConsumeGroupAccessPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.ListAccessPolicyRespPolicies`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ListConsumeGroupAccessPolicyResponse.

        用户列表。

        :param policies: The policies of this ListConsumeGroupAccessPolicyResponse.
        :type policies: list[:class:`huaweicloudsdkrocketmq.v2.ListAccessPolicyRespPolicies`]
        """
        self._policies = policies

    @property
    def total(self):
        """Gets the total of this ListConsumeGroupAccessPolicyResponse.

        总用户个数。

        :return: The total of this ListConsumeGroupAccessPolicyResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListConsumeGroupAccessPolicyResponse.

        总用户个数。

        :param total: The total of this ListConsumeGroupAccessPolicyResponse.
        :type total: float
        """
        self._total = total

    @property
    def name(self):
        """Gets the name of this ListConsumeGroupAccessPolicyResponse.

        主题或消费组名称。

        :return: The name of this ListConsumeGroupAccessPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListConsumeGroupAccessPolicyResponse.

        主题或消费组名称。

        :param name: The name of this ListConsumeGroupAccessPolicyResponse.
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
        if not isinstance(other, ListConsumeGroupAccessPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
