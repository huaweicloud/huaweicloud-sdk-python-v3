# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulScanTaskHostInfoScanVulList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_id': 'str',
        'vul_name': 'str',
        'status': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'status': 'status',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, vul_id=None, vul_name=None, status=None, failed_reason=None):
        r"""VulScanTaskHostInfoScanVulList

        The model defined in huaweicloud sdk

        :param vul_id: 漏洞id
        :type vul_id: str
        :param vul_name: 漏洞名称
        :type vul_name: str
        :param status: 该漏洞的扫描状态，包含如下：   - scanning : 扫描中   - success : 扫描成功   - failed : 扫描失败
        :type status: str
        :param failed_reason: 该漏洞扫描失败的原因，只有扫描失败的漏洞有该字段
        :type failed_reason: str
        """
        
        

        self._vul_id = None
        self._vul_name = None
        self._status = None
        self._failed_reason = None
        self.discriminator = None

        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def vul_id(self):
        r"""Gets the vul_id of this VulScanTaskHostInfoScanVulList.

        漏洞id

        :return: The vul_id of this VulScanTaskHostInfoScanVulList.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this VulScanTaskHostInfoScanVulList.

        漏洞id

        :param vul_id: The vul_id of this VulScanTaskHostInfoScanVulList.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this VulScanTaskHostInfoScanVulList.

        漏洞名称

        :return: The vul_name of this VulScanTaskHostInfoScanVulList.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this VulScanTaskHostInfoScanVulList.

        漏洞名称

        :param vul_name: The vul_name of this VulScanTaskHostInfoScanVulList.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def status(self):
        r"""Gets the status of this VulScanTaskHostInfoScanVulList.

        该漏洞的扫描状态，包含如下：   - scanning : 扫描中   - success : 扫描成功   - failed : 扫描失败

        :return: The status of this VulScanTaskHostInfoScanVulList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulScanTaskHostInfoScanVulList.

        该漏洞的扫描状态，包含如下：   - scanning : 扫描中   - success : 扫描成功   - failed : 扫描失败

        :param status: The status of this VulScanTaskHostInfoScanVulList.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this VulScanTaskHostInfoScanVulList.

        该漏洞扫描失败的原因，只有扫描失败的漏洞有该字段

        :return: The failed_reason of this VulScanTaskHostInfoScanVulList.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this VulScanTaskHostInfoScanVulList.

        该漏洞扫描失败的原因，只有扫描失败的漏洞有该字段

        :param failed_reason: The failed_reason of this VulScanTaskHostInfoScanVulList.
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
        if not isinstance(other, VulScanTaskHostInfoScanVulList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
