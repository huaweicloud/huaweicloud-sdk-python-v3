# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateSecurityGroupRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_group_rules': 'list[SecurityGroupRule]',
        'request_id': 'str'
    }

    attribute_map = {
        'security_group_rules': 'security_group_rules',
        'request_id': 'request_id'
    }

    def __init__(self, security_group_rules=None, request_id=None):
        """BatchCreateSecurityGroupRulesResponse

        The model defined in huaweicloud sdk

        :param security_group_rules: 批量创建安全组规则的响应体
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v3.SecurityGroupRule`]
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(BatchCreateSecurityGroupRulesResponse, self).__init__()

        self._security_group_rules = None
        self._request_id = None
        self.discriminator = None

        if security_group_rules is not None:
            self.security_group_rules = security_group_rules
        if request_id is not None:
            self.request_id = request_id

    @property
    def security_group_rules(self):
        """Gets the security_group_rules of this BatchCreateSecurityGroupRulesResponse.

        批量创建安全组规则的响应体

        :return: The security_group_rules of this BatchCreateSecurityGroupRulesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.SecurityGroupRule`]
        """
        return self._security_group_rules

    @security_group_rules.setter
    def security_group_rules(self, security_group_rules):
        """Sets the security_group_rules of this BatchCreateSecurityGroupRulesResponse.

        批量创建安全组规则的响应体

        :param security_group_rules: The security_group_rules of this BatchCreateSecurityGroupRulesResponse.
        :type security_group_rules: list[:class:`huaweicloudsdkvpc.v3.SecurityGroupRule`]
        """
        self._security_group_rules = security_group_rules

    @property
    def request_id(self):
        """Gets the request_id of this BatchCreateSecurityGroupRulesResponse.

        请求ID

        :return: The request_id of this BatchCreateSecurityGroupRulesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this BatchCreateSecurityGroupRulesResponse.

        请求ID

        :param request_id: The request_id of this BatchCreateSecurityGroupRulesResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, BatchCreateSecurityGroupRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
