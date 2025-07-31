# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTaskResourcesResponseInfoScanDetailList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'scan_type': 'str',
        'status': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'scan_type': 'scan_type',
        'status': 'status',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, scan_type=None, status=None, failed_reason=None):
        r"""ListTaskResourcesResponseInfoScanDetailList

        The model defined in huaweicloud sdk

        :param scan_type: 扫描项类型，包含如下   - cluster_vul：集群漏洞   - risk_assessment：风险评估   - benchmark：安全合规
        :type scan_type: str
        :param status: 扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败
        :type status: str
        :param failed_reason: 扫描失败的原因
        :type failed_reason: str
        """
        
        

        self._scan_type = None
        self._status = None
        self._failed_reason = None
        self.discriminator = None

        if scan_type is not None:
            self.scan_type = scan_type
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def scan_type(self):
        r"""Gets the scan_type of this ListTaskResourcesResponseInfoScanDetailList.

        扫描项类型，包含如下   - cluster_vul：集群漏洞   - risk_assessment：风险评估   - benchmark：安全合规

        :return: The scan_type of this ListTaskResourcesResponseInfoScanDetailList.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        r"""Sets the scan_type of this ListTaskResourcesResponseInfoScanDetailList.

        扫描项类型，包含如下   - cluster_vul：集群漏洞   - risk_assessment：风险评估   - benchmark：安全合规

        :param scan_type: The scan_type of this ListTaskResourcesResponseInfoScanDetailList.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def status(self):
        r"""Gets the status of this ListTaskResourcesResponseInfoScanDetailList.

        扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :return: The status of this ListTaskResourcesResponseInfoScanDetailList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTaskResourcesResponseInfoScanDetailList.

        扫描状态，包含如下：   - scanning：扫描中   - success：扫描成功   - failed：扫描失败

        :param status: The status of this ListTaskResourcesResponseInfoScanDetailList.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this ListTaskResourcesResponseInfoScanDetailList.

        扫描失败的原因

        :return: The failed_reason of this ListTaskResourcesResponseInfoScanDetailList.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this ListTaskResourcesResponseInfoScanDetailList.

        扫描失败的原因

        :param failed_reason: The failed_reason of this ListTaskResourcesResponseInfoScanDetailList.
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
        if not isinstance(other, ListTaskResourcesResponseInfoScanDetailList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
