# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulScanTaskHostInfoVulScanDetails:

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
        'status': 'str',
        'failed_reason': 'str',
        'scan_vul_list': 'list[VulScanTaskHostInfoScanVulList]'
    }

    attribute_map = {
        'vul_type': 'vul_type',
        'status': 'status',
        'failed_reason': 'failed_reason',
        'scan_vul_list': 'scan_vul_list'
    }

    def __init__(self, vul_type=None, status=None, failed_reason=None, scan_vul_list=None):
        r"""VulScanTaskHostInfoVulScanDetails

        The model defined in huaweicloud sdk

        :param vul_type: 扫描的漏洞类型，包含如下：   - linux_vul : linux漏洞   - windows_vul : windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞
        :type vul_type: str
        :param status: 该类型漏洞的扫描状态，包含如下：   - scanning : 扫描中   - success : 扫描成功   - failed : 扫描失败
        :type status: str
        :param failed_reason: 扫描失败的原因，只有扫描失败的漏洞类型有该字段
        :type failed_reason: str
        :param scan_vul_list: 扫描的漏洞列表，只有漏洞类型为应急漏洞有该字段
        :type scan_vul_list: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoScanVulList`]
        """
        
        

        self._vul_type = None
        self._status = None
        self._failed_reason = None
        self._scan_vul_list = None
        self.discriminator = None

        if vul_type is not None:
            self.vul_type = vul_type
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if scan_vul_list is not None:
            self.scan_vul_list = scan_vul_list

    @property
    def vul_type(self):
        r"""Gets the vul_type of this VulScanTaskHostInfoVulScanDetails.

        扫描的漏洞类型，包含如下：   - linux_vul : linux漏洞   - windows_vul : windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :return: The vul_type of this VulScanTaskHostInfoVulScanDetails.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this VulScanTaskHostInfoVulScanDetails.

        扫描的漏洞类型，包含如下：   - linux_vul : linux漏洞   - windows_vul : windows漏洞   - web_cms : Web-CMS漏洞   - app_vul : 应用漏洞   - urgent_vul : 应急漏洞

        :param vul_type: The vul_type of this VulScanTaskHostInfoVulScanDetails.
        :type vul_type: str
        """
        self._vul_type = vul_type

    @property
    def status(self):
        r"""Gets the status of this VulScanTaskHostInfoVulScanDetails.

        该类型漏洞的扫描状态，包含如下：   - scanning : 扫描中   - success : 扫描成功   - failed : 扫描失败

        :return: The status of this VulScanTaskHostInfoVulScanDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulScanTaskHostInfoVulScanDetails.

        该类型漏洞的扫描状态，包含如下：   - scanning : 扫描中   - success : 扫描成功   - failed : 扫描失败

        :param status: The status of this VulScanTaskHostInfoVulScanDetails.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this VulScanTaskHostInfoVulScanDetails.

        扫描失败的原因，只有扫描失败的漏洞类型有该字段

        :return: The failed_reason of this VulScanTaskHostInfoVulScanDetails.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this VulScanTaskHostInfoVulScanDetails.

        扫描失败的原因，只有扫描失败的漏洞类型有该字段

        :param failed_reason: The failed_reason of this VulScanTaskHostInfoVulScanDetails.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def scan_vul_list(self):
        r"""Gets the scan_vul_list of this VulScanTaskHostInfoVulScanDetails.

        扫描的漏洞列表，只有漏洞类型为应急漏洞有该字段

        :return: The scan_vul_list of this VulScanTaskHostInfoVulScanDetails.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoScanVulList`]
        """
        return self._scan_vul_list

    @scan_vul_list.setter
    def scan_vul_list(self, scan_vul_list):
        r"""Sets the scan_vul_list of this VulScanTaskHostInfoVulScanDetails.

        扫描的漏洞列表，只有漏洞类型为应急漏洞有该字段

        :param scan_vul_list: The scan_vul_list of this VulScanTaskHostInfoVulScanDetails.
        :type scan_vul_list: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoScanVulList`]
        """
        self._scan_vul_list = scan_vul_list

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
        if not isinstance(other, VulScanTaskHostInfoVulScanDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
