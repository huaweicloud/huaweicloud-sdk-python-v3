# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulScanTaskHostInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'asset_value': 'str',
        'scan_status': 'str',
        'failed_reasons': 'list[VulScanTaskHostInfoFailedReasons]',
        'vul_scan_details': 'list[VulScanTaskHostInfoVulScanDetails]'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'asset_value': 'asset_value',
        'scan_status': 'scan_status',
        'failed_reasons': 'failed_reasons',
        'vul_scan_details': 'vul_scan_details'
    }

    def __init__(self, host_id=None, host_name=None, public_ip=None, private_ip=None, asset_value=None, scan_status=None, failed_reasons=None, vul_scan_details=None):
        r"""VulScanTaskHostInfo

        The model defined in huaweicloud sdk

        :param host_id: **参数解释**: 主机ID **取值范围**: 字符长度1-128位 
        :type host_id: str
        :param host_name: **参数解释**: 主机名称 **取值范围**: 字符长度0-128位 
        :type host_name: str
        :param public_ip: **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128位 
        :type public_ip: str
        :param private_ip: **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128位 
        :type private_ip: str
        :param asset_value: **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 
        :type asset_value: str
        :param scan_status: **参数解释**: 主机的扫描状态 **取值范围**: - scanning：扫描中 - success：扫描成功 - failed：扫描失败 
        :type scan_status: str
        :param failed_reasons: **参数解释**: 漏洞扫描失败的原因列表（即将废弃，建议使用“vul_scan_details”字段） **取值范围**: 最小值0，最大值2147483647 
        :type failed_reasons: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoFailedReasons`]
        :param vul_scan_details: **参数解释**: 该主机的扫描详情信息列表 **取值范围**: 最小值0，最大值2147483647 
        :type vul_scan_details: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoVulScanDetails`]
        """
        
        

        self._host_id = None
        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._asset_value = None
        self._scan_status = None
        self._failed_reasons = None
        self._vul_scan_details = None
        self.discriminator = None

        if host_id is not None:
            self.host_id = host_id
        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if asset_value is not None:
            self.asset_value = asset_value
        if scan_status is not None:
            self.scan_status = scan_status
        if failed_reasons is not None:
            self.failed_reasons = failed_reasons
        if vul_scan_details is not None:
            self.vul_scan_details = vul_scan_details

    @property
    def host_id(self):
        r"""Gets the host_id of this VulScanTaskHostInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-128位 

        :return: The host_id of this VulScanTaskHostInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this VulScanTaskHostInfo.

        **参数解释**: 主机ID **取值范围**: 字符长度1-128位 

        :param host_id: The host_id of this VulScanTaskHostInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this VulScanTaskHostInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-128位 

        :return: The host_name of this VulScanTaskHostInfo.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this VulScanTaskHostInfo.

        **参数解释**: 主机名称 **取值范围**: 字符长度0-128位 

        :param host_name: The host_name of this VulScanTaskHostInfo.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this VulScanTaskHostInfo.

        **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128位 

        :return: The public_ip of this VulScanTaskHostInfo.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this VulScanTaskHostInfo.

        **参数解释**: 弹性公网IP地址 **取值范围**: 字符长度0-128位 

        :param public_ip: The public_ip of this VulScanTaskHostInfo.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this VulScanTaskHostInfo.

        **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128位 

        :return: The private_ip of this VulScanTaskHostInfo.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this VulScanTaskHostInfo.

        **参数解释**: 私有IP地址 **取值范围**: 字符长度0-128位 

        :param private_ip: The private_ip of this VulScanTaskHostInfo.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def asset_value(self):
        r"""Gets the asset_value of this VulScanTaskHostInfo.

        **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :return: The asset_value of this VulScanTaskHostInfo.
        :rtype: str
        """
        return self._asset_value

    @asset_value.setter
    def asset_value(self, asset_value):
        r"""Sets the asset_value of this VulScanTaskHostInfo.

        **参数解释**: 主机的资产重要性 **取值范围**: - important：重要资产 - common：一般资产 - test：测试资产 

        :param asset_value: The asset_value of this VulScanTaskHostInfo.
        :type asset_value: str
        """
        self._asset_value = asset_value

    @property
    def scan_status(self):
        r"""Gets the scan_status of this VulScanTaskHostInfo.

        **参数解释**: 主机的扫描状态 **取值范围**: - scanning：扫描中 - success：扫描成功 - failed：扫描失败 

        :return: The scan_status of this VulScanTaskHostInfo.
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        r"""Sets the scan_status of this VulScanTaskHostInfo.

        **参数解释**: 主机的扫描状态 **取值范围**: - scanning：扫描中 - success：扫描成功 - failed：扫描失败 

        :param scan_status: The scan_status of this VulScanTaskHostInfo.
        :type scan_status: str
        """
        self._scan_status = scan_status

    @property
    def failed_reasons(self):
        r"""Gets the failed_reasons of this VulScanTaskHostInfo.

        **参数解释**: 漏洞扫描失败的原因列表（即将废弃，建议使用“vul_scan_details”字段） **取值范围**: 最小值0，最大值2147483647 

        :return: The failed_reasons of this VulScanTaskHostInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoFailedReasons`]
        """
        return self._failed_reasons

    @failed_reasons.setter
    def failed_reasons(self, failed_reasons):
        r"""Sets the failed_reasons of this VulScanTaskHostInfo.

        **参数解释**: 漏洞扫描失败的原因列表（即将废弃，建议使用“vul_scan_details”字段） **取值范围**: 最小值0，最大值2147483647 

        :param failed_reasons: The failed_reasons of this VulScanTaskHostInfo.
        :type failed_reasons: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoFailedReasons`]
        """
        self._failed_reasons = failed_reasons

    @property
    def vul_scan_details(self):
        r"""Gets the vul_scan_details of this VulScanTaskHostInfo.

        **参数解释**: 该主机的扫描详情信息列表 **取值范围**: 最小值0，最大值2147483647 

        :return: The vul_scan_details of this VulScanTaskHostInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoVulScanDetails`]
        """
        return self._vul_scan_details

    @vul_scan_details.setter
    def vul_scan_details(self, vul_scan_details):
        r"""Sets the vul_scan_details of this VulScanTaskHostInfo.

        **参数解释**: 该主机的扫描详情信息列表 **取值范围**: 最小值0，最大值2147483647 

        :param vul_scan_details: The vul_scan_details of this VulScanTaskHostInfo.
        :type vul_scan_details: list[:class:`huaweicloudsdkhss.v5.VulScanTaskHostInfoVulScanDetails`]
        """
        self._vul_scan_details = vul_scan_details

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VulScanTaskHostInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
