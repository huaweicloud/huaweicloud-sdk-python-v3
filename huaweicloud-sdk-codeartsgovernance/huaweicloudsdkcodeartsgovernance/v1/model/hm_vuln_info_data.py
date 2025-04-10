# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HmVulnInfoData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report': 'list[HmVulnInfoDataReport]'
    }

    attribute_map = {
        'report': 'report'
    }

    def __init__(self, report=None):
        r"""HmVulnInfoData

        The model defined in huaweicloud sdk

        :param report: 报告
        :type report: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HmVulnInfoDataReport`]
        """
        
        

        self._report = None
        self.discriminator = None

        if report is not None:
            self.report = report

    @property
    def report(self):
        r"""Gets the report of this HmVulnInfoData.

        报告

        :return: The report of this HmVulnInfoData.
        :rtype: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HmVulnInfoDataReport`]
        """
        return self._report

    @report.setter
    def report(self, report):
        r"""Sets the report of this HmVulnInfoData.

        报告

        :param report: The report of this HmVulnInfoData.
        :type report: list[:class:`huaweicloudsdkcodeartsgovernance.v1.HmVulnInfoDataReport`]
        """
        self._report = report

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
        if not isinstance(other, HmVulnInfoData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
