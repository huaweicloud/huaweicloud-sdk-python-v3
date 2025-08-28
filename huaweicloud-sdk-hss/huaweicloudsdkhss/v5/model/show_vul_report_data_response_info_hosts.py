# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVulReportDataResponseInfoHosts:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_name': 'str',
        'public_ip': 'str',
        'private_ip': 'str',
        'scan_time': 'int',
        'severity_level': 'str',
        'vul_total_num': 'int',
        'host_id': 'str'
    }

    attribute_map = {
        'host_name': 'host_name',
        'public_ip': 'public_ip',
        'private_ip': 'private_ip',
        'scan_time': 'scan_time',
        'severity_level': 'severity_level',
        'vul_total_num': 'vul_total_num',
        'host_id': 'host_id'
    }

    def __init__(self, host_name=None, public_ip=None, private_ip=None, scan_time=None, severity_level=None, vul_total_num=None, host_id=None):
        r"""ShowVulReportDataResponseInfoHosts

        The model defined in huaweicloud sdk

        :param host_name: **参数解释**： 主机名称 **取值范围**： 字符长度1-256位 
        :type host_name: str
        :param public_ip: **参数解释**： 服务器公网ip **取值范围**： 字符长度1-64位 
        :type public_ip: str
        :param private_ip: **参数解释**： 服务器私网ip **取值范围**： 字符长度0-128位 
        :type private_ip: str
        :param scan_time: **参数解释**： 最近扫描时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type scan_time: int
        :param severity_level: **参数解释**： 漏洞风险等级 **取值范围**： - Critical：紧急。 - High：高危。 - Medium：中危。 - Low：低危。 
        :type severity_level: str
        :param vul_total_num: **参数解释**： 漏洞数 **取值范围**： 最小值0，最大值10000000 
        :type vul_total_num: int
        :param host_id: **参数解释**： 主机ID **取值范围**： 字符长度1-128位 
        :type host_id: str
        """
        
        

        self._host_name = None
        self._public_ip = None
        self._private_ip = None
        self._scan_time = None
        self._severity_level = None
        self._vul_total_num = None
        self._host_id = None
        self.discriminator = None

        if host_name is not None:
            self.host_name = host_name
        if public_ip is not None:
            self.public_ip = public_ip
        if private_ip is not None:
            self.private_ip = private_ip
        if scan_time is not None:
            self.scan_time = scan_time
        if severity_level is not None:
            self.severity_level = severity_level
        if vul_total_num is not None:
            self.vul_total_num = vul_total_num
        if host_id is not None:
            self.host_id = host_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 主机名称 **取值范围**： 字符长度1-256位 

        :return: The host_name of this ShowVulReportDataResponseInfoHosts.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 主机名称 **取值范围**： 字符长度1-256位 

        :param host_name: The host_name of this ShowVulReportDataResponseInfoHosts.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def public_ip(self):
        r"""Gets the public_ip of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 服务器公网ip **取值范围**： 字符长度1-64位 

        :return: The public_ip of this ShowVulReportDataResponseInfoHosts.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        r"""Sets the public_ip of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 服务器公网ip **取值范围**： 字符长度1-64位 

        :param public_ip: The public_ip of this ShowVulReportDataResponseInfoHosts.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def private_ip(self):
        r"""Gets the private_ip of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 服务器私网ip **取值范围**： 字符长度0-128位 

        :return: The private_ip of this ShowVulReportDataResponseInfoHosts.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        r"""Sets the private_ip of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 服务器私网ip **取值范围**： 字符长度0-128位 

        :param private_ip: The private_ip of this ShowVulReportDataResponseInfoHosts.
        :type private_ip: str
        """
        self._private_ip = private_ip

    @property
    def scan_time(self):
        r"""Gets the scan_time of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 最近扫描时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The scan_time of this ShowVulReportDataResponseInfoHosts.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 最近扫描时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param scan_time: The scan_time of this ShowVulReportDataResponseInfoHosts.
        :type scan_time: int
        """
        self._scan_time = scan_time

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 漏洞风险等级 **取值范围**： - Critical：紧急。 - High：高危。 - Medium：中危。 - Low：低危。 

        :return: The severity_level of this ShowVulReportDataResponseInfoHosts.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 漏洞风险等级 **取值范围**： - Critical：紧急。 - High：高危。 - Medium：中危。 - Low：低危。 

        :param severity_level: The severity_level of this ShowVulReportDataResponseInfoHosts.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def vul_total_num(self):
        r"""Gets the vul_total_num of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 漏洞数 **取值范围**： 最小值0，最大值10000000 

        :return: The vul_total_num of this ShowVulReportDataResponseInfoHosts.
        :rtype: int
        """
        return self._vul_total_num

    @vul_total_num.setter
    def vul_total_num(self, vul_total_num):
        r"""Sets the vul_total_num of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 漏洞数 **取值范围**： 最小值0，最大值10000000 

        :param vul_total_num: The vul_total_num of this ShowVulReportDataResponseInfoHosts.
        :type vul_total_num: int
        """
        self._vul_total_num = vul_total_num

    @property
    def host_id(self):
        r"""Gets the host_id of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 主机ID **取值范围**： 字符长度1-128位 

        :return: The host_id of this ShowVulReportDataResponseInfoHosts.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ShowVulReportDataResponseInfoHosts.

        **参数解释**： 主机ID **取值范围**： 字符长度1-128位 

        :param host_id: The host_id of this ShowVulReportDataResponseInfoHosts.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, ShowVulReportDataResponseInfoHosts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
