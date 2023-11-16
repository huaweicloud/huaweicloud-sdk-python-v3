# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'severity': 'SecurityRuleSeverity',
        'cve': 'SecurityRuleCve'
    }

    attribute_map = {
        'severity': 'severity',
        'cve': 'cve'
    }

    def __init__(self, severity=None, cve=None):
        """SecurityRule

        The model defined in huaweicloud sdk

        :param severity: 
        :type severity: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRuleSeverity`
        :param cve: 
        :type cve: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRuleCve`
        """
        
        

        self._severity = None
        self._cve = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if cve is not None:
            self.cve = cve

    @property
    def severity(self):
        """Gets the severity of this SecurityRule.

        :return: The severity of this SecurityRule.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRuleSeverity`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this SecurityRule.

        :param severity: The severity of this SecurityRule.
        :type severity: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRuleSeverity`
        """
        self._severity = severity

    @property
    def cve(self):
        """Gets the cve of this SecurityRule.

        :return: The cve of this SecurityRule.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRuleCve`
        """
        return self._cve

    @cve.setter
    def cve(self, cve):
        """Sets the cve of this SecurityRule.

        :param cve: The cve of this SecurityRule.
        :type cve: :class:`huaweicloudsdkcodeartspipeline.v2.SecurityRuleCve`
        """
        self._cve = cve

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
        if not isinstance(other, SecurityRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
