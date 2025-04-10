# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CompliantSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliant_count': 'int',
        'severity_summary': 'SeveritySummary'
    }

    attribute_map = {
        'compliant_count': 'compliant_count',
        'severity_summary': 'severity_summary'
    }

    def __init__(self, compliant_count=None, severity_summary=None):
        r"""CompliantSummary

        The model defined in huaweicloud sdk

        :param compliant_count: 合规补丁数量
        :type compliant_count: int
        :param severity_summary: 
        :type severity_summary: :class:`huaweicloudsdkcoc.v1.SeveritySummary`
        """
        
        

        self._compliant_count = None
        self._severity_summary = None
        self.discriminator = None

        if compliant_count is not None:
            self.compliant_count = compliant_count
        if severity_summary is not None:
            self.severity_summary = severity_summary

    @property
    def compliant_count(self):
        r"""Gets the compliant_count of this CompliantSummary.

        合规补丁数量

        :return: The compliant_count of this CompliantSummary.
        :rtype: int
        """
        return self._compliant_count

    @compliant_count.setter
    def compliant_count(self, compliant_count):
        r"""Sets the compliant_count of this CompliantSummary.

        合规补丁数量

        :param compliant_count: The compliant_count of this CompliantSummary.
        :type compliant_count: int
        """
        self._compliant_count = compliant_count

    @property
    def severity_summary(self):
        r"""Gets the severity_summary of this CompliantSummary.

        :return: The severity_summary of this CompliantSummary.
        :rtype: :class:`huaweicloudsdkcoc.v1.SeveritySummary`
        """
        return self._severity_summary

    @severity_summary.setter
    def severity_summary(self, severity_summary):
        r"""Sets the severity_summary of this CompliantSummary.

        :param severity_summary: The severity_summary of this CompliantSummary.
        :type severity_summary: :class:`huaweicloudsdkcoc.v1.SeveritySummary`
        """
        self._severity_summary = severity_summary

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
        if not isinstance(other, CompliantSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
