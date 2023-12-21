# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulScanTaskHostInfoFailedReasons:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_type': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'vul_type': 'vul_type',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, vul_type=None, failed_reason=None):
        """VulScanTaskHostInfoFailedReasons

        The model defined in huaweicloud sdk

        :param vul_type: 扫描失败的漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞
        :type vul_type: str
        :param failed_reason: 扫描失败的原因
        :type failed_reason: str
        """
        
        

        self._vul_type = None
        self._failed_reason = None
        self.discriminator = None

        if vul_type is not None:
            self.vul_type = vul_type
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def vul_type(self):
        """Gets the vul_type of this VulScanTaskHostInfoFailedReasons.

        扫描失败的漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :return: The vul_type of this VulScanTaskHostInfoFailedReasons.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        """Sets the vul_type of this VulScanTaskHostInfoFailedReasons.

        扫描失败的漏洞类型，包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :param vul_type: The vul_type of this VulScanTaskHostInfoFailedReasons.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def failed_reason(self):
        """Gets the failed_reason of this VulScanTaskHostInfoFailedReasons.

        扫描失败的原因

        :return: The failed_reason of this VulScanTaskHostInfoFailedReasons.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this VulScanTaskHostInfoFailedReasons.

        扫描失败的原因

        :param failed_reason: The failed_reason of this VulScanTaskHostInfoFailedReasons.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, VulScanTaskHostInfoFailedReasons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
