# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSystemSecurityPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'system_security_policies': 'list[SystemSecurityPolicy]',
        'request_id': 'str'
    }

    attribute_map = {
        'system_security_policies': 'system_security_policies',
        'request_id': 'request_id'
    }

    def __init__(self, system_security_policies=None, request_id=None):
        """ListSystemSecurityPoliciesResponse

        The model defined in huaweicloud sdk

        :param system_security_policies: 系统安全策略列表。
        :type system_security_policies: list[:class:`huaweicloudsdkelb.v3.SystemSecurityPolicy`]
        :param request_id: 请求ID。  注：自动生成 。
        :type request_id: str
        """
        
        super(ListSystemSecurityPoliciesResponse, self).__init__()

        self._system_security_policies = None
        self._request_id = None
        self.discriminator = None

        if system_security_policies is not None:
            self.system_security_policies = system_security_policies
        if request_id is not None:
            self.request_id = request_id

    @property
    def system_security_policies(self):
        """Gets the system_security_policies of this ListSystemSecurityPoliciesResponse.

        系统安全策略列表。

        :return: The system_security_policies of this ListSystemSecurityPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.SystemSecurityPolicy`]
        """
        return self._system_security_policies

    @system_security_policies.setter
    def system_security_policies(self, system_security_policies):
        """Sets the system_security_policies of this ListSystemSecurityPoliciesResponse.

        系统安全策略列表。

        :param system_security_policies: The system_security_policies of this ListSystemSecurityPoliciesResponse.
        :type system_security_policies: list[:class:`huaweicloudsdkelb.v3.SystemSecurityPolicy`]
        """
        self._system_security_policies = system_security_policies

    @property
    def request_id(self):
        """Gets the request_id of this ListSystemSecurityPoliciesResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this ListSystemSecurityPoliciesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListSystemSecurityPoliciesResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this ListSystemSecurityPoliciesResponse.
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
        if not isinstance(other, ListSystemSecurityPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
