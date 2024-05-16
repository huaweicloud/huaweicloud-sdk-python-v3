# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HostVulnItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'port': 'str',
        'title': 'str',
        'sa_id': 'str',
        'vuln_id': 'str',
        'severity': 'str',
        'topic': 'str',
        'description': 'str',
        'solution': 'str',
        'fix_advisory': 'str',
        'fix_cmd': 'str',
        'cve_list': 'list[HostVulnItemCveList]',
        'ref_link_list': 'list[str]',
        'component_list': 'list[HostVulnItemComponentList]',
        'vul_detect_result': 'str',
        'cvss_score': 'str',
        'cvss_version': 'str',
        'cvss_vector': 'str',
        'is_ignore': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'port': 'port',
        'title': 'title',
        'sa_id': 'sa_id',
        'vuln_id': 'vuln_id',
        'severity': 'severity',
        'topic': 'topic',
        'description': 'description',
        'solution': 'solution',
        'fix_advisory': 'fix_advisory',
        'fix_cmd': 'fix_cmd',
        'cve_list': 'cve_list',
        'ref_link_list': 'ref_link_list',
        'component_list': 'component_list',
        'vul_detect_result': 'vul_detect_result',
        'cvss_score': 'cvss_score',
        'cvss_version': 'cvss_version',
        'cvss_vector': 'cvss_vector',
        'is_ignore': 'is_ignore'
    }

    def __init__(self, type=None, port=None, title=None, sa_id=None, vuln_id=None, severity=None, topic=None, description=None, solution=None, fix_advisory=None, fix_cmd=None, cve_list=None, ref_link_list=None, component_list=None, vul_detect_result=None, cvss_score=None, cvss_version=None, cvss_vector=None, is_ignore=None):
        """HostVulnItem

        The model defined in huaweicloud sdk

        :param type: 漏洞类型
        :type type: str
        :param port: 扫描端口号
        :type port: str
        :param title: 漏洞标题
        :type title: str
        :param sa_id: 漏洞公告ID
        :type sa_id: str
        :param vuln_id: 漏洞ID
        :type vuln_id: str
        :param severity: 漏洞风险等级:   * high - 高风险   * medium - 中风险   * low - 低风险   * hint - 提示 
        :type severity: str
        :param topic: 漏洞摘要
        :type topic: str
        :param description: 漏洞描述
        :type description: str
        :param solution: 漏洞提示建议
        :type solution: str
        :param fix_advisory: 漏洞修复建议
        :type fix_advisory: str
        :param fix_cmd: 漏洞修复指令
        :type fix_cmd: str
        :param cve_list: CVE漏洞列表
        :type cve_list: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostVulnItemCveList`]
        :param ref_link_list: 参考信息链接列表
        :type ref_link_list: list[str]
        :param component_list: 内容列表
        :type component_list: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostVulnItemComponentList`]
        :param vul_detect_result: 检查结果
        :type vul_detect_result: str
        :param cvss_score: CVSS分数信息
        :type cvss_score: str
        :param cvss_version: CVSS版本信息
        :type cvss_version: str
        :param cvss_vector: CVSS向量信息
        :type cvss_vector: str
        :param is_ignore: 是否误报
        :type is_ignore: bool
        """
        
        

        self._type = None
        self._port = None
        self._title = None
        self._sa_id = None
        self._vuln_id = None
        self._severity = None
        self._topic = None
        self._description = None
        self._solution = None
        self._fix_advisory = None
        self._fix_cmd = None
        self._cve_list = None
        self._ref_link_list = None
        self._component_list = None
        self._vul_detect_result = None
        self._cvss_score = None
        self._cvss_version = None
        self._cvss_vector = None
        self._is_ignore = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if port is not None:
            self.port = port
        if title is not None:
            self.title = title
        if sa_id is not None:
            self.sa_id = sa_id
        if vuln_id is not None:
            self.vuln_id = vuln_id
        if severity is not None:
            self.severity = severity
        if topic is not None:
            self.topic = topic
        if description is not None:
            self.description = description
        if solution is not None:
            self.solution = solution
        if fix_advisory is not None:
            self.fix_advisory = fix_advisory
        if fix_cmd is not None:
            self.fix_cmd = fix_cmd
        if cve_list is not None:
            self.cve_list = cve_list
        if ref_link_list is not None:
            self.ref_link_list = ref_link_list
        if component_list is not None:
            self.component_list = component_list
        if vul_detect_result is not None:
            self.vul_detect_result = vul_detect_result
        if cvss_score is not None:
            self.cvss_score = cvss_score
        if cvss_version is not None:
            self.cvss_version = cvss_version
        if cvss_vector is not None:
            self.cvss_vector = cvss_vector
        if is_ignore is not None:
            self.is_ignore = is_ignore

    @property
    def type(self):
        """Gets the type of this HostVulnItem.

        漏洞类型

        :return: The type of this HostVulnItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HostVulnItem.

        漏洞类型

        :param type: The type of this HostVulnItem.
        :type type: str
        """
        self._type = type

    @property
    def port(self):
        """Gets the port of this HostVulnItem.

        扫描端口号

        :return: The port of this HostVulnItem.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this HostVulnItem.

        扫描端口号

        :param port: The port of this HostVulnItem.
        :type port: str
        """
        self._port = port

    @property
    def title(self):
        """Gets the title of this HostVulnItem.

        漏洞标题

        :return: The title of this HostVulnItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this HostVulnItem.

        漏洞标题

        :param title: The title of this HostVulnItem.
        :type title: str
        """
        self._title = title

    @property
    def sa_id(self):
        """Gets the sa_id of this HostVulnItem.

        漏洞公告ID

        :return: The sa_id of this HostVulnItem.
        :rtype: str
        """
        return self._sa_id

    @sa_id.setter
    def sa_id(self, sa_id):
        """Sets the sa_id of this HostVulnItem.

        漏洞公告ID

        :param sa_id: The sa_id of this HostVulnItem.
        :type sa_id: str
        """
        self._sa_id = sa_id

    @property
    def vuln_id(self):
        """Gets the vuln_id of this HostVulnItem.

        漏洞ID

        :return: The vuln_id of this HostVulnItem.
        :rtype: str
        """
        return self._vuln_id

    @vuln_id.setter
    def vuln_id(self, vuln_id):
        """Sets the vuln_id of this HostVulnItem.

        漏洞ID

        :param vuln_id: The vuln_id of this HostVulnItem.
        :type vuln_id: str
        """
        self._vuln_id = vuln_id

    @property
    def severity(self):
        """Gets the severity of this HostVulnItem.

        漏洞风险等级:   * high - 高风险   * medium - 中风险   * low - 低风险   * hint - 提示 

        :return: The severity of this HostVulnItem.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this HostVulnItem.

        漏洞风险等级:   * high - 高风险   * medium - 中风险   * low - 低风险   * hint - 提示 

        :param severity: The severity of this HostVulnItem.
        :type severity: str
        """
        self._severity = severity

    @property
    def topic(self):
        """Gets the topic of this HostVulnItem.

        漏洞摘要

        :return: The topic of this HostVulnItem.
        :rtype: str
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this HostVulnItem.

        漏洞摘要

        :param topic: The topic of this HostVulnItem.
        :type topic: str
        """
        self._topic = topic

    @property
    def description(self):
        """Gets the description of this HostVulnItem.

        漏洞描述

        :return: The description of this HostVulnItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HostVulnItem.

        漏洞描述

        :param description: The description of this HostVulnItem.
        :type description: str
        """
        self._description = description

    @property
    def solution(self):
        """Gets the solution of this HostVulnItem.

        漏洞提示建议

        :return: The solution of this HostVulnItem.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        """Sets the solution of this HostVulnItem.

        漏洞提示建议

        :param solution: The solution of this HostVulnItem.
        :type solution: str
        """
        self._solution = solution

    @property
    def fix_advisory(self):
        """Gets the fix_advisory of this HostVulnItem.

        漏洞修复建议

        :return: The fix_advisory of this HostVulnItem.
        :rtype: str
        """
        return self._fix_advisory

    @fix_advisory.setter
    def fix_advisory(self, fix_advisory):
        """Sets the fix_advisory of this HostVulnItem.

        漏洞修复建议

        :param fix_advisory: The fix_advisory of this HostVulnItem.
        :type fix_advisory: str
        """
        self._fix_advisory = fix_advisory

    @property
    def fix_cmd(self):
        """Gets the fix_cmd of this HostVulnItem.

        漏洞修复指令

        :return: The fix_cmd of this HostVulnItem.
        :rtype: str
        """
        return self._fix_cmd

    @fix_cmd.setter
    def fix_cmd(self, fix_cmd):
        """Sets the fix_cmd of this HostVulnItem.

        漏洞修复指令

        :param fix_cmd: The fix_cmd of this HostVulnItem.
        :type fix_cmd: str
        """
        self._fix_cmd = fix_cmd

    @property
    def cve_list(self):
        """Gets the cve_list of this HostVulnItem.

        CVE漏洞列表

        :return: The cve_list of this HostVulnItem.
        :rtype: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostVulnItemCveList`]
        """
        return self._cve_list

    @cve_list.setter
    def cve_list(self, cve_list):
        """Sets the cve_list of this HostVulnItem.

        CVE漏洞列表

        :param cve_list: The cve_list of this HostVulnItem.
        :type cve_list: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostVulnItemCveList`]
        """
        self._cve_list = cve_list

    @property
    def ref_link_list(self):
        """Gets the ref_link_list of this HostVulnItem.

        参考信息链接列表

        :return: The ref_link_list of this HostVulnItem.
        :rtype: list[str]
        """
        return self._ref_link_list

    @ref_link_list.setter
    def ref_link_list(self, ref_link_list):
        """Sets the ref_link_list of this HostVulnItem.

        参考信息链接列表

        :param ref_link_list: The ref_link_list of this HostVulnItem.
        :type ref_link_list: list[str]
        """
        self._ref_link_list = ref_link_list

    @property
    def component_list(self):
        """Gets the component_list of this HostVulnItem.

        内容列表

        :return: The component_list of this HostVulnItem.
        :rtype: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostVulnItemComponentList`]
        """
        return self._component_list

    @component_list.setter
    def component_list(self, component_list):
        """Sets the component_list of this HostVulnItem.

        内容列表

        :param component_list: The component_list of this HostVulnItem.
        :type component_list: list[:class:`huaweicloudsdkcodeartsinspector.v3.HostVulnItemComponentList`]
        """
        self._component_list = component_list

    @property
    def vul_detect_result(self):
        """Gets the vul_detect_result of this HostVulnItem.

        检查结果

        :return: The vul_detect_result of this HostVulnItem.
        :rtype: str
        """
        return self._vul_detect_result

    @vul_detect_result.setter
    def vul_detect_result(self, vul_detect_result):
        """Sets the vul_detect_result of this HostVulnItem.

        检查结果

        :param vul_detect_result: The vul_detect_result of this HostVulnItem.
        :type vul_detect_result: str
        """
        self._vul_detect_result = vul_detect_result

    @property
    def cvss_score(self):
        """Gets the cvss_score of this HostVulnItem.

        CVSS分数信息

        :return: The cvss_score of this HostVulnItem.
        :rtype: str
        """
        return self._cvss_score

    @cvss_score.setter
    def cvss_score(self, cvss_score):
        """Sets the cvss_score of this HostVulnItem.

        CVSS分数信息

        :param cvss_score: The cvss_score of this HostVulnItem.
        :type cvss_score: str
        """
        self._cvss_score = cvss_score

    @property
    def cvss_version(self):
        """Gets the cvss_version of this HostVulnItem.

        CVSS版本信息

        :return: The cvss_version of this HostVulnItem.
        :rtype: str
        """
        return self._cvss_version

    @cvss_version.setter
    def cvss_version(self, cvss_version):
        """Sets the cvss_version of this HostVulnItem.

        CVSS版本信息

        :param cvss_version: The cvss_version of this HostVulnItem.
        :type cvss_version: str
        """
        self._cvss_version = cvss_version

    @property
    def cvss_vector(self):
        """Gets the cvss_vector of this HostVulnItem.

        CVSS向量信息

        :return: The cvss_vector of this HostVulnItem.
        :rtype: str
        """
        return self._cvss_vector

    @cvss_vector.setter
    def cvss_vector(self, cvss_vector):
        """Sets the cvss_vector of this HostVulnItem.

        CVSS向量信息

        :param cvss_vector: The cvss_vector of this HostVulnItem.
        :type cvss_vector: str
        """
        self._cvss_vector = cvss_vector

    @property
    def is_ignore(self):
        """Gets the is_ignore of this HostVulnItem.

        是否误报

        :return: The is_ignore of this HostVulnItem.
        :rtype: bool
        """
        return self._is_ignore

    @is_ignore.setter
    def is_ignore(self, is_ignore):
        """Sets the is_ignore of this HostVulnItem.

        是否误报

        :param is_ignore: The is_ignore of this HostVulnItem.
        :type is_ignore: bool
        """
        self._is_ignore = is_ignore

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
        if not isinstance(other, HostVulnItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
