# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditRuleScopesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scopes': 'list[RuleScopeInfo]',
        'total': 'int'
    }

    attribute_map = {
        'scopes': 'scopes',
        'total': 'total'
    }

    def __init__(self, scopes=None, total=None):
        """ListAuditRuleScopesResponse

        The model defined in huaweicloud sdk

        :param scopes: 审计范围规则列表
        :type scopes: list[:class:`huaweicloudsdkdbss.v1.RuleScopeInfo`]
        :param total: 总数
        :type total: int
        """
        
        super(ListAuditRuleScopesResponse, self).__init__()

        self._scopes = None
        self._total = None
        self.discriminator = None

        if scopes is not None:
            self.scopes = scopes
        if total is not None:
            self.total = total

    @property
    def scopes(self):
        """Gets the scopes of this ListAuditRuleScopesResponse.

        审计范围规则列表

        :return: The scopes of this ListAuditRuleScopesResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.RuleScopeInfo`]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this ListAuditRuleScopesResponse.

        审计范围规则列表

        :param scopes: The scopes of this ListAuditRuleScopesResponse.
        :type scopes: list[:class:`huaweicloudsdkdbss.v1.RuleScopeInfo`]
        """
        self._scopes = scopes

    @property
    def total(self):
        """Gets the total of this ListAuditRuleScopesResponse.

        总数

        :return: The total of this ListAuditRuleScopesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListAuditRuleScopesResponse.

        总数

        :param total: The total of this ListAuditRuleScopesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListAuditRuleScopesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
