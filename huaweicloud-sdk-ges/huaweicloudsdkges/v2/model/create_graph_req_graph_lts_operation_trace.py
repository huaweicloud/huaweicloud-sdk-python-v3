# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGraphReqGraphLtsOperationTrace:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_audit': 'bool',
        'audit_log_group_name': 'str'
    }

    attribute_map = {
        'enable_audit': 'enable_audit',
        'audit_log_group_name': 'audit_log_group_name'
    }

    def __init__(self, enable_audit=None, audit_log_group_name=None):
        """CreateGraphReqGraphLtsOperationTrace

        The model defined in huaweicloud sdk

        :param enable_audit: 是否开启图审计，默认“false”。
        :type enable_audit: bool
        :param audit_log_group_name: LTS日志组名称。
        :type audit_log_group_name: str
        """
        
        

        self._enable_audit = None
        self._audit_log_group_name = None
        self.discriminator = None

        if enable_audit is not None:
            self.enable_audit = enable_audit
        if audit_log_group_name is not None:
            self.audit_log_group_name = audit_log_group_name

    @property
    def enable_audit(self):
        """Gets the enable_audit of this CreateGraphReqGraphLtsOperationTrace.

        是否开启图审计，默认“false”。

        :return: The enable_audit of this CreateGraphReqGraphLtsOperationTrace.
        :rtype: bool
        """
        return self._enable_audit

    @enable_audit.setter
    def enable_audit(self, enable_audit):
        """Sets the enable_audit of this CreateGraphReqGraphLtsOperationTrace.

        是否开启图审计，默认“false”。

        :param enable_audit: The enable_audit of this CreateGraphReqGraphLtsOperationTrace.
        :type enable_audit: bool
        """
        self._enable_audit = enable_audit

    @property
    def audit_log_group_name(self):
        """Gets the audit_log_group_name of this CreateGraphReqGraphLtsOperationTrace.

        LTS日志组名称。

        :return: The audit_log_group_name of this CreateGraphReqGraphLtsOperationTrace.
        :rtype: str
        """
        return self._audit_log_group_name

    @audit_log_group_name.setter
    def audit_log_group_name(self, audit_log_group_name):
        """Sets the audit_log_group_name of this CreateGraphReqGraphLtsOperationTrace.

        LTS日志组名称。

        :param audit_log_group_name: The audit_log_group_name of this CreateGraphReqGraphLtsOperationTrace.
        :type audit_log_group_name: str
        """
        self._audit_log_group_name = audit_log_group_name

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
        if not isinstance(other, CreateGraphReqGraphLtsOperationTrace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
