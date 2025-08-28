# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityPoliciesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'security_policies': 'list[SecurityPolicy]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'security_policies': 'security_policies',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, security_policies=None, request_id=None, page_info=None):
        r"""ListSecurityPoliciesResponse

        The model defined in huaweicloud sdk

        :param security_policies: **参数解释**：自定义安全策略列表返回对象。
        :type security_policies: list[:class:`huaweicloudsdkelb.v3.SecurityPolicy`]
        :param request_id: **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        
        super(ListSecurityPoliciesResponse, self).__init__()

        self._security_policies = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if security_policies is not None:
            self.security_policies = security_policies
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def security_policies(self):
        r"""Gets the security_policies of this ListSecurityPoliciesResponse.

        **参数解释**：自定义安全策略列表返回对象。

        :return: The security_policies of this ListSecurityPoliciesResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v3.SecurityPolicy`]
        """
        return self._security_policies

    @security_policies.setter
    def security_policies(self, security_policies):
        r"""Sets the security_policies of this ListSecurityPoliciesResponse.

        **参数解释**：自定义安全策略列表返回对象。

        :param security_policies: The security_policies of this ListSecurityPoliciesResponse.
        :type security_policies: list[:class:`huaweicloudsdkelb.v3.SecurityPolicy`]
        """
        self._security_policies = security_policies

    @property
    def request_id(self):
        r"""Gets the request_id of this ListSecurityPoliciesResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :return: The request_id of this ListSecurityPoliciesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListSecurityPoliciesResponse.

        **参数解释**：请求ID。  **取值范围**：由数字、小写字母和中划线（-）组成的字符串，自动生成。

        :param request_id: The request_id of this ListSecurityPoliciesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        r"""Gets the page_info of this ListSecurityPoliciesResponse.

        :return: The page_info of this ListSecurityPoliciesResponse.
        :rtype: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListSecurityPoliciesResponse.

        :param page_info: The page_info of this ListSecurityPoliciesResponse.
        :type page_info: :class:`huaweicloudsdkelb.v3.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListSecurityPoliciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
