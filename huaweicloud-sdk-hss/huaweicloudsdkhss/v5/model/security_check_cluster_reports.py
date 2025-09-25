# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityCheckClusterReports:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'report_id': 'str',
        'cluster_name': 'str',
        'cluster_id': 'str',
        'cluster_category': 'str',
        'severity': 'str',
        'local_image_vul_num': 'int',
        'risk_config_num': 'int',
        'privileged_container_num': 'int',
        'scan_time': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'cluster_category': 'cluster_category',
        'severity': 'severity',
        'local_image_vul_num': 'local_image_vul_num',
        'risk_config_num': 'risk_config_num',
        'privileged_container_num': 'privileged_container_num',
        'scan_time': 'scan_time'
    }

    def __init__(self, report_id=None, cluster_name=None, cluster_id=None, cluster_category=None, severity=None, local_image_vul_num=None, risk_config_num=None, privileged_container_num=None, scan_time=None):
        r"""SecurityCheckClusterReports

        The model defined in huaweicloud sdk

        :param report_id: **参数解释**： 体检报告ID **取值范围**： 不涉及 
        :type report_id: str
        :param cluster_name: **参数解释**： 集群名称 **取值范围**： 不涉及 
        :type cluster_name: str
        :param cluster_id: **参数解释**： 集群ID **取值范围**： 不涉及 
        :type cluster_id: str
        :param cluster_category: **参数解释**： 集群类型 **取值范围**： - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 
        :type cluster_category: str
        :param severity: **参数解释**： 风险级别 **取值范围**： - Security：无风险 - Insecurity：有风险 
        :type severity: str
        :param local_image_vul_num: **参数解释**： 本地镜像漏洞风险数量 **取值范围**： 不涉及 
        :type local_image_vul_num: int
        :param risk_config_num: **参数解释**： 基线风险数量 **取值范围**： 不涉及 
        :type risk_config_num: int
        :param privileged_container_num: **参数解释**： 特权容器告警数量 **取值范围**： 不涉及 
        :type privileged_container_num: int
        :param scan_time: **参数解释**： 最新检测时间 **取值范围**： 不涉及 
        :type scan_time: int
        """
        
        

        self._report_id = None
        self._cluster_name = None
        self._cluster_id = None
        self._cluster_category = None
        self._severity = None
        self._local_image_vul_num = None
        self._risk_config_num = None
        self._privileged_container_num = None
        self._scan_time = None
        self.discriminator = None

        if report_id is not None:
            self.report_id = report_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_category is not None:
            self.cluster_category = cluster_category
        if severity is not None:
            self.severity = severity
        if local_image_vul_num is not None:
            self.local_image_vul_num = local_image_vul_num
        if risk_config_num is not None:
            self.risk_config_num = risk_config_num
        if privileged_container_num is not None:
            self.privileged_container_num = privileged_container_num
        if scan_time is not None:
            self.scan_time = scan_time

    @property
    def report_id(self):
        r"""Gets the report_id of this SecurityCheckClusterReports.

        **参数解释**： 体检报告ID **取值范围**： 不涉及 

        :return: The report_id of this SecurityCheckClusterReports.
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        r"""Sets the report_id of this SecurityCheckClusterReports.

        **参数解释**： 体检报告ID **取值范围**： 不涉及 

        :param report_id: The report_id of this SecurityCheckClusterReports.
        :type report_id: str
        """
        self._report_id = report_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this SecurityCheckClusterReports.

        **参数解释**： 集群名称 **取值范围**： 不涉及 

        :return: The cluster_name of this SecurityCheckClusterReports.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this SecurityCheckClusterReports.

        **参数解释**： 集群名称 **取值范围**： 不涉及 

        :param cluster_name: The cluster_name of this SecurityCheckClusterReports.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this SecurityCheckClusterReports.

        **参数解释**： 集群ID **取值范围**： 不涉及 

        :return: The cluster_id of this SecurityCheckClusterReports.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this SecurityCheckClusterReports.

        **参数解释**： 集群ID **取值范围**： 不涉及 

        :param cluster_id: The cluster_id of this SecurityCheckClusterReports.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_category(self):
        r"""Gets the cluster_category of this SecurityCheckClusterReports.

        **参数解释**： 集群类型 **取值范围**： - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 

        :return: The cluster_category of this SecurityCheckClusterReports.
        :rtype: str
        """
        return self._cluster_category

    @cluster_category.setter
    def cluster_category(self, cluster_category):
        r"""Sets the cluster_category of this SecurityCheckClusterReports.

        **参数解释**： 集群类型 **取值范围**： - CCE：CCE Standard集群 - Turbo：CCE Turbo集群 

        :param cluster_category: The cluster_category of this SecurityCheckClusterReports.
        :type cluster_category: str
        """
        self._cluster_category = cluster_category

    @property
    def severity(self):
        r"""Gets the severity of this SecurityCheckClusterReports.

        **参数解释**： 风险级别 **取值范围**： - Security：无风险 - Insecurity：有风险 

        :return: The severity of this SecurityCheckClusterReports.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this SecurityCheckClusterReports.

        **参数解释**： 风险级别 **取值范围**： - Security：无风险 - Insecurity：有风险 

        :param severity: The severity of this SecurityCheckClusterReports.
        :type severity: str
        """
        self._severity = severity

    @property
    def local_image_vul_num(self):
        r"""Gets the local_image_vul_num of this SecurityCheckClusterReports.

        **参数解释**： 本地镜像漏洞风险数量 **取值范围**： 不涉及 

        :return: The local_image_vul_num of this SecurityCheckClusterReports.
        :rtype: int
        """
        return self._local_image_vul_num

    @local_image_vul_num.setter
    def local_image_vul_num(self, local_image_vul_num):
        r"""Sets the local_image_vul_num of this SecurityCheckClusterReports.

        **参数解释**： 本地镜像漏洞风险数量 **取值范围**： 不涉及 

        :param local_image_vul_num: The local_image_vul_num of this SecurityCheckClusterReports.
        :type local_image_vul_num: int
        """
        self._local_image_vul_num = local_image_vul_num

    @property
    def risk_config_num(self):
        r"""Gets the risk_config_num of this SecurityCheckClusterReports.

        **参数解释**： 基线风险数量 **取值范围**： 不涉及 

        :return: The risk_config_num of this SecurityCheckClusterReports.
        :rtype: int
        """
        return self._risk_config_num

    @risk_config_num.setter
    def risk_config_num(self, risk_config_num):
        r"""Sets the risk_config_num of this SecurityCheckClusterReports.

        **参数解释**： 基线风险数量 **取值范围**： 不涉及 

        :param risk_config_num: The risk_config_num of this SecurityCheckClusterReports.
        :type risk_config_num: int
        """
        self._risk_config_num = risk_config_num

    @property
    def privileged_container_num(self):
        r"""Gets the privileged_container_num of this SecurityCheckClusterReports.

        **参数解释**： 特权容器告警数量 **取值范围**： 不涉及 

        :return: The privileged_container_num of this SecurityCheckClusterReports.
        :rtype: int
        """
        return self._privileged_container_num

    @privileged_container_num.setter
    def privileged_container_num(self, privileged_container_num):
        r"""Sets the privileged_container_num of this SecurityCheckClusterReports.

        **参数解释**： 特权容器告警数量 **取值范围**： 不涉及 

        :param privileged_container_num: The privileged_container_num of this SecurityCheckClusterReports.
        :type privileged_container_num: int
        """
        self._privileged_container_num = privileged_container_num

    @property
    def scan_time(self):
        r"""Gets the scan_time of this SecurityCheckClusterReports.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :return: The scan_time of this SecurityCheckClusterReports.
        :rtype: int
        """
        return self._scan_time

    @scan_time.setter
    def scan_time(self, scan_time):
        r"""Sets the scan_time of this SecurityCheckClusterReports.

        **参数解释**： 最新检测时间 **取值范围**： 不涉及 

        :param scan_time: The scan_time of this SecurityCheckClusterReports.
        :type scan_time: int
        """
        self._scan_time = scan_time

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
        if not isinstance(other, SecurityCheckClusterReports):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
