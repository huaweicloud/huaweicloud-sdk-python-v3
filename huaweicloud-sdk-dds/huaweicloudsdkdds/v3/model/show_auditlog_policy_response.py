# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowAuditlogPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keep_days': 'int',
        'audit_scope': 'str',
        'audit_types': 'list[str]'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'audit_scope': 'audit_scope',
        'audit_types': 'audit_types'
    }

    def __init__(self, keep_days=None, audit_scope=None, audit_types=None):
        """ShowAuditlogPolicyResponse - a model defined in huaweicloud sdk"""
        
        super(ShowAuditlogPolicyResponse, self).__init__()

        self._keep_days = None
        self._audit_scope = None
        self._audit_types = None
        self.discriminator = None

        if keep_days is not None:
            self.keep_days = keep_days
        if audit_scope is not None:
            self.audit_scope = audit_scope
        if audit_types is not None:
            self.audit_types = audit_types

    @property
    def keep_days(self):
        """Gets the keep_days of this ShowAuditlogPolicyResponse.

        审计日志保存天数，审计日志策略关闭时为0。

        :return: The keep_days of this ShowAuditlogPolicyResponse.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this ShowAuditlogPolicyResponse.

        审计日志保存天数，审计日志策略关闭时为0。

        :param keep_days: The keep_days of this ShowAuditlogPolicyResponse.
        :type: int
        """
        self._keep_days = keep_days

    @property
    def audit_scope(self):
        """Gets the audit_scope of this ShowAuditlogPolicyResponse.

        审计范围。

        :return: The audit_scope of this ShowAuditlogPolicyResponse.
        :rtype: str
        """
        return self._audit_scope

    @audit_scope.setter
    def audit_scope(self, audit_scope):
        """Sets the audit_scope of this ShowAuditlogPolicyResponse.

        审计范围。

        :param audit_scope: The audit_scope of this ShowAuditlogPolicyResponse.
        :type: str
        """
        self._audit_scope = audit_scope

    @property
    def audit_types(self):
        """Gets the audit_types of this ShowAuditlogPolicyResponse.

        审计类型。

        :return: The audit_types of this ShowAuditlogPolicyResponse.
        :rtype: list[str]
        """
        return self._audit_types

    @audit_types.setter
    def audit_types(self, audit_types):
        """Sets the audit_types of this ShowAuditlogPolicyResponse.

        审计类型。

        :param audit_types: The audit_types of this ShowAuditlogPolicyResponse.
        :type: list[str]
        """
        self._audit_types = audit_types

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAuditlogPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
