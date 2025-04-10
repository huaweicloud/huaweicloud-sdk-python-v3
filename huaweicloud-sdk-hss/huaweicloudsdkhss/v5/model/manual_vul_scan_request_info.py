# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ManualVulScanRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manual_scan_type': 'list[str]',
        'batch_flag': 'bool',
        'range_type': 'str',
        'agent_id_list': 'list[str]',
        'urgent_vul_id_list': 'list[str]'
    }

    attribute_map = {
        'manual_scan_type': 'manual_scan_type',
        'batch_flag': 'batch_flag',
        'range_type': 'range_type',
        'agent_id_list': 'agent_id_list',
        'urgent_vul_id_list': 'urgent_vul_id_list'
    }

    def __init__(self, manual_scan_type=None, batch_flag=None, range_type=None, agent_id_list=None, urgent_vul_id_list=None):
        r"""ManualVulScanRequestInfo

        The model defined in huaweicloud sdk

        :param manual_scan_type: 操作类型,包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞
        :type manual_scan_type: list[str]
        :param batch_flag: 是否是批量操作,为true时扫描所有支持的主机
        :type batch_flag: bool
        :param range_type: 扫描主机的范围，包含如下：   -all_host : 扫描全部主机,此类型不需要填写agent_id_list   -specific_host : 扫描指定主机
        :type range_type: str
        :param agent_id_list: 主机列表
        :type agent_id_list: list[str]
        :param urgent_vul_id_list: 扫描的应急漏洞id列表，若为空则扫描所有应急漏洞 包含如下： \&quot;URGENT-CVE-2023-46604   Apache ActiveMQ远程代码执行漏洞\&quot; \&quot;URGENT-HSSVD-2020-1109  Elasticsearch 未授权访问漏洞\&quot; \&quot;URGENT-CVE-2022-26134   Atlassian Confluence OGNL 远程代码执行漏洞（CVE-2022-26134）\&quot; \&quot;URGENT-CVE-2023-22515   Atlassian Confluence Data Center and Server 权限提升漏洞(CVE-2023-22515)\&quot; \&quot;URGENT-CVE-2023-22518   Atlassian Confluence Data Center &amp; Server 授权机制不恰当漏洞(CVE-2023-22518)\&quot; \&quot;URGENT-CVE-2023-28432   MinIO 信息泄露漏洞（CVE-2023-28432）\&quot; \&quot;URGENT-CVE-2023-37582   Apache RocketMQ 远程代码执行漏洞(CVE-2023-37582)\&quot; \&quot;URGENT-CVE-2023-33246   Apache RocketMQ 远程代码执行漏洞(CVE-2023-33246)\&quot; \&quot;URGENT-CNVD-2023-02709  禅道项目管理系统远程命令执行漏洞(CNVD-2023-02709)\&quot; \&quot;URGENT-CVE-2022-36804   Atlassian Bitbucket Server 和 Data Center 命令注入漏洞(CVE-2022-36804)\&quot; \&quot;URGENT-CVE-2022-22965   Spring Framework JDK &gt;&#x3D; 9 远程代码执行漏洞\&quot; \&quot;URGENT-CVE-2022-25845   fastjson &lt;1.2.83 远程代码执行漏洞\&quot; \&quot;URGENT-CVE-2019-14439   Jackson-databind远程命令执行漏洞（CVE-2019-14439）\&quot; \&quot;URGENT-CVE-2020-13933   Apache Shiro身份验证绕过漏洞（CVE-2020-13933）\&quot; \&quot;URGENT-CVE-2020-26217   XStream &lt; 1.4.14 远程代码执行漏洞（CVE-2020-26217）\&quot; \&quot;URGENT-CVE-2021-4034    Linux Polkit 权限提升漏洞预警（CVE-2021-4034）\&quot; \&quot;URGENT-CVE-2021-44228   Apache Log4j2 远程代码执行漏洞（CVE-2021-44228、CVE-2021-45046）\&quot; \&quot;URGENT-CVE-2022-0847    Dirty Pipe - Linux 内核本地提权漏洞（CVE-2022-0847）\&quot;
        :type urgent_vul_id_list: list[str]
        """
        
        

        self._manual_scan_type = None
        self._batch_flag = None
        self._range_type = None
        self._agent_id_list = None
        self._urgent_vul_id_list = None
        self.discriminator = None

        if manual_scan_type is not None:
            self.manual_scan_type = manual_scan_type
        if batch_flag is not None:
            self.batch_flag = batch_flag
        if range_type is not None:
            self.range_type = range_type
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list
        if urgent_vul_id_list is not None:
            self.urgent_vul_id_list = urgent_vul_id_list

    @property
    def manual_scan_type(self):
        r"""Gets the manual_scan_type of this ManualVulScanRequestInfo.

        操作类型,包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :return: The manual_scan_type of this ManualVulScanRequestInfo.
        :rtype: list[str]
        """
        return self._manual_scan_type

    @manual_scan_type.setter
    def manual_scan_type(self, manual_scan_type):
        r"""Sets the manual_scan_type of this ManualVulScanRequestInfo.

        操作类型,包含如下：   -linux_vul : linux漏洞   -windows_vul : windows漏洞   -web_cms : Web-CMS漏洞   -app_vul : 应用漏洞   -urgent_vul : 应急漏洞

        :param manual_scan_type: The manual_scan_type of this ManualVulScanRequestInfo.
        :type manual_scan_type: list[str]
        """
        self._manual_scan_type = manual_scan_type

    @property
    def batch_flag(self):
        r"""Gets the batch_flag of this ManualVulScanRequestInfo.

        是否是批量操作,为true时扫描所有支持的主机

        :return: The batch_flag of this ManualVulScanRequestInfo.
        :rtype: bool
        """
        return self._batch_flag

    @batch_flag.setter
    def batch_flag(self, batch_flag):
        r"""Sets the batch_flag of this ManualVulScanRequestInfo.

        是否是批量操作,为true时扫描所有支持的主机

        :param batch_flag: The batch_flag of this ManualVulScanRequestInfo.
        :type batch_flag: bool
        """
        self._batch_flag = batch_flag

    @property
    def range_type(self):
        r"""Gets the range_type of this ManualVulScanRequestInfo.

        扫描主机的范围，包含如下：   -all_host : 扫描全部主机,此类型不需要填写agent_id_list   -specific_host : 扫描指定主机

        :return: The range_type of this ManualVulScanRequestInfo.
        :rtype: str
        """
        return self._range_type

    @range_type.setter
    def range_type(self, range_type):
        r"""Sets the range_type of this ManualVulScanRequestInfo.

        扫描主机的范围，包含如下：   -all_host : 扫描全部主机,此类型不需要填写agent_id_list   -specific_host : 扫描指定主机

        :param range_type: The range_type of this ManualVulScanRequestInfo.
        :type range_type: str
        """
        self._range_type = range_type

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this ManualVulScanRequestInfo.

        主机列表

        :return: The agent_id_list of this ManualVulScanRequestInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this ManualVulScanRequestInfo.

        主机列表

        :param agent_id_list: The agent_id_list of this ManualVulScanRequestInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

    @property
    def urgent_vul_id_list(self):
        r"""Gets the urgent_vul_id_list of this ManualVulScanRequestInfo.

        扫描的应急漏洞id列表，若为空则扫描所有应急漏洞 包含如下： \"URGENT-CVE-2023-46604   Apache ActiveMQ远程代码执行漏洞\" \"URGENT-HSSVD-2020-1109  Elasticsearch 未授权访问漏洞\" \"URGENT-CVE-2022-26134   Atlassian Confluence OGNL 远程代码执行漏洞（CVE-2022-26134）\" \"URGENT-CVE-2023-22515   Atlassian Confluence Data Center and Server 权限提升漏洞(CVE-2023-22515)\" \"URGENT-CVE-2023-22518   Atlassian Confluence Data Center & Server 授权机制不恰当漏洞(CVE-2023-22518)\" \"URGENT-CVE-2023-28432   MinIO 信息泄露漏洞（CVE-2023-28432）\" \"URGENT-CVE-2023-37582   Apache RocketMQ 远程代码执行漏洞(CVE-2023-37582)\" \"URGENT-CVE-2023-33246   Apache RocketMQ 远程代码执行漏洞(CVE-2023-33246)\" \"URGENT-CNVD-2023-02709  禅道项目管理系统远程命令执行漏洞(CNVD-2023-02709)\" \"URGENT-CVE-2022-36804   Atlassian Bitbucket Server 和 Data Center 命令注入漏洞(CVE-2022-36804)\" \"URGENT-CVE-2022-22965   Spring Framework JDK >= 9 远程代码执行漏洞\" \"URGENT-CVE-2022-25845   fastjson <1.2.83 远程代码执行漏洞\" \"URGENT-CVE-2019-14439   Jackson-databind远程命令执行漏洞（CVE-2019-14439）\" \"URGENT-CVE-2020-13933   Apache Shiro身份验证绕过漏洞（CVE-2020-13933）\" \"URGENT-CVE-2020-26217   XStream < 1.4.14 远程代码执行漏洞（CVE-2020-26217）\" \"URGENT-CVE-2021-4034    Linux Polkit 权限提升漏洞预警（CVE-2021-4034）\" \"URGENT-CVE-2021-44228   Apache Log4j2 远程代码执行漏洞（CVE-2021-44228、CVE-2021-45046）\" \"URGENT-CVE-2022-0847    Dirty Pipe - Linux 内核本地提权漏洞（CVE-2022-0847）\"

        :return: The urgent_vul_id_list of this ManualVulScanRequestInfo.
        :rtype: list[str]
        """
        return self._urgent_vul_id_list

    @urgent_vul_id_list.setter
    def urgent_vul_id_list(self, urgent_vul_id_list):
        r"""Sets the urgent_vul_id_list of this ManualVulScanRequestInfo.

        扫描的应急漏洞id列表，若为空则扫描所有应急漏洞 包含如下： \"URGENT-CVE-2023-46604   Apache ActiveMQ远程代码执行漏洞\" \"URGENT-HSSVD-2020-1109  Elasticsearch 未授权访问漏洞\" \"URGENT-CVE-2022-26134   Atlassian Confluence OGNL 远程代码执行漏洞（CVE-2022-26134）\" \"URGENT-CVE-2023-22515   Atlassian Confluence Data Center and Server 权限提升漏洞(CVE-2023-22515)\" \"URGENT-CVE-2023-22518   Atlassian Confluence Data Center & Server 授权机制不恰当漏洞(CVE-2023-22518)\" \"URGENT-CVE-2023-28432   MinIO 信息泄露漏洞（CVE-2023-28432）\" \"URGENT-CVE-2023-37582   Apache RocketMQ 远程代码执行漏洞(CVE-2023-37582)\" \"URGENT-CVE-2023-33246   Apache RocketMQ 远程代码执行漏洞(CVE-2023-33246)\" \"URGENT-CNVD-2023-02709  禅道项目管理系统远程命令执行漏洞(CNVD-2023-02709)\" \"URGENT-CVE-2022-36804   Atlassian Bitbucket Server 和 Data Center 命令注入漏洞(CVE-2022-36804)\" \"URGENT-CVE-2022-22965   Spring Framework JDK >= 9 远程代码执行漏洞\" \"URGENT-CVE-2022-25845   fastjson <1.2.83 远程代码执行漏洞\" \"URGENT-CVE-2019-14439   Jackson-databind远程命令执行漏洞（CVE-2019-14439）\" \"URGENT-CVE-2020-13933   Apache Shiro身份验证绕过漏洞（CVE-2020-13933）\" \"URGENT-CVE-2020-26217   XStream < 1.4.14 远程代码执行漏洞（CVE-2020-26217）\" \"URGENT-CVE-2021-4034    Linux Polkit 权限提升漏洞预警（CVE-2021-4034）\" \"URGENT-CVE-2021-44228   Apache Log4j2 远程代码执行漏洞（CVE-2021-44228、CVE-2021-45046）\" \"URGENT-CVE-2022-0847    Dirty Pipe - Linux 内核本地提权漏洞（CVE-2022-0847）\"

        :param urgent_vul_id_list: The urgent_vul_id_list of this ManualVulScanRequestInfo.
        :type urgent_vul_id_list: list[str]
        """
        self._urgent_vul_id_list = urgent_vul_id_list

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
        if not isinstance(other, ManualVulScanRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
