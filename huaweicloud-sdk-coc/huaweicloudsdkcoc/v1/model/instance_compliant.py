# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceCompliant:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compliant_summary': 'CompliantSummary',
        'non_compliant_summary': 'NonCompliantSummary',
        'execution_summary': 'ExecutionSummary',
        'id': 'str',
        'enterprise_project_id': 'str',
        'name': 'str',
        'instance_id': 'str',
        'node_id': 'str',
        'ip': 'str',
        'eip': 'str',
        'region': 'str',
        'group': 'str',
        'report_scene': 'str',
        'cce_info_id': 'str',
        'status': 'str',
        'baseline_id': 'str',
        'baseline_name': 'str',
        'rule_type': 'str',
        'operating_system': 'str'
    }

    attribute_map = {
        'compliant_summary': 'compliant_summary',
        'non_compliant_summary': 'non_compliant_summary',
        'execution_summary': 'execution_summary',
        'id': 'id',
        'enterprise_project_id': 'enterprise_project_id',
        'name': 'name',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'ip': 'ip',
        'eip': 'eip',
        'region': 'region',
        'group': 'group',
        'report_scene': 'report_scene',
        'cce_info_id': 'cce_info_id',
        'status': 'status',
        'baseline_id': 'baseline_id',
        'baseline_name': 'baseline_name',
        'rule_type': 'rule_type',
        'operating_system': 'operating_system'
    }

    def __init__(self, compliant_summary=None, non_compliant_summary=None, execution_summary=None, id=None, enterprise_project_id=None, name=None, instance_id=None, node_id=None, ip=None, eip=None, region=None, group=None, report_scene=None, cce_info_id=None, status=None, baseline_id=None, baseline_name=None, rule_type=None, operating_system=None):
        r"""InstanceCompliant

        The model defined in huaweicloud sdk

        :param compliant_summary: 
        :type compliant_summary: :class:`huaweicloudsdkcoc.v1.CompliantSummary`
        :param non_compliant_summary: 
        :type non_compliant_summary: :class:`huaweicloudsdkcoc.v1.NonCompliantSummary`
        :param execution_summary: 
        :type execution_summary: :class:`huaweicloudsdkcoc.v1.ExecutionSummary`
        :param id: id
        :type id: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param name: 节点名称
        :type name: str
        :param instance_id: 节点ID
        :type instance_id: str
        :param node_id: cce集群节点ID
        :type node_id: str
        :param ip: 节点IP
        :type ip: str
        :param eip: 弹性公网ip
        :type eip: str
        :param region: 区域
        :type region: str
        :param group: 分组
        :type group: str
        :param report_scene: 报告场景(CCE,ECS)
        :type report_scene: str
        :param cce_info_id: cce 集群信息id
        :type cce_info_id: str
        :param status: 合规性状态
        :type status: str
        :param baseline_id: 基线id
        :type baseline_id: str
        :param baseline_name: 基线名称
        :type baseline_name: str
        :param rule_type: 基线规则类型
        :type rule_type: str
        :param operating_system: 操作系统
        :type operating_system: str
        """
        
        

        self._compliant_summary = None
        self._non_compliant_summary = None
        self._execution_summary = None
        self._id = None
        self._enterprise_project_id = None
        self._name = None
        self._instance_id = None
        self._node_id = None
        self._ip = None
        self._eip = None
        self._region = None
        self._group = None
        self._report_scene = None
        self._cce_info_id = None
        self._status = None
        self._baseline_id = None
        self._baseline_name = None
        self._rule_type = None
        self._operating_system = None
        self.discriminator = None

        if compliant_summary is not None:
            self.compliant_summary = compliant_summary
        if non_compliant_summary is not None:
            self.non_compliant_summary = non_compliant_summary
        if execution_summary is not None:
            self.execution_summary = execution_summary
        if id is not None:
            self.id = id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if name is not None:
            self.name = name
        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if ip is not None:
            self.ip = ip
        if eip is not None:
            self.eip = eip
        if region is not None:
            self.region = region
        if group is not None:
            self.group = group
        if report_scene is not None:
            self.report_scene = report_scene
        if cce_info_id is not None:
            self.cce_info_id = cce_info_id
        if status is not None:
            self.status = status
        if baseline_id is not None:
            self.baseline_id = baseline_id
        if baseline_name is not None:
            self.baseline_name = baseline_name
        if rule_type is not None:
            self.rule_type = rule_type
        if operating_system is not None:
            self.operating_system = operating_system

    @property
    def compliant_summary(self):
        r"""Gets the compliant_summary of this InstanceCompliant.

        :return: The compliant_summary of this InstanceCompliant.
        :rtype: :class:`huaweicloudsdkcoc.v1.CompliantSummary`
        """
        return self._compliant_summary

    @compliant_summary.setter
    def compliant_summary(self, compliant_summary):
        r"""Sets the compliant_summary of this InstanceCompliant.

        :param compliant_summary: The compliant_summary of this InstanceCompliant.
        :type compliant_summary: :class:`huaweicloudsdkcoc.v1.CompliantSummary`
        """
        self._compliant_summary = compliant_summary

    @property
    def non_compliant_summary(self):
        r"""Gets the non_compliant_summary of this InstanceCompliant.

        :return: The non_compliant_summary of this InstanceCompliant.
        :rtype: :class:`huaweicloudsdkcoc.v1.NonCompliantSummary`
        """
        return self._non_compliant_summary

    @non_compliant_summary.setter
    def non_compliant_summary(self, non_compliant_summary):
        r"""Sets the non_compliant_summary of this InstanceCompliant.

        :param non_compliant_summary: The non_compliant_summary of this InstanceCompliant.
        :type non_compliant_summary: :class:`huaweicloudsdkcoc.v1.NonCompliantSummary`
        """
        self._non_compliant_summary = non_compliant_summary

    @property
    def execution_summary(self):
        r"""Gets the execution_summary of this InstanceCompliant.

        :return: The execution_summary of this InstanceCompliant.
        :rtype: :class:`huaweicloudsdkcoc.v1.ExecutionSummary`
        """
        return self._execution_summary

    @execution_summary.setter
    def execution_summary(self, execution_summary):
        r"""Sets the execution_summary of this InstanceCompliant.

        :param execution_summary: The execution_summary of this InstanceCompliant.
        :type execution_summary: :class:`huaweicloudsdkcoc.v1.ExecutionSummary`
        """
        self._execution_summary = execution_summary

    @property
    def id(self):
        r"""Gets the id of this InstanceCompliant.

        id

        :return: The id of this InstanceCompliant.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this InstanceCompliant.

        id

        :param id: The id of this InstanceCompliant.
        :type id: str
        """
        self._id = id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this InstanceCompliant.

        企业项目id

        :return: The enterprise_project_id of this InstanceCompliant.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this InstanceCompliant.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this InstanceCompliant.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this InstanceCompliant.

        节点名称

        :return: The name of this InstanceCompliant.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InstanceCompliant.

        节点名称

        :param name: The name of this InstanceCompliant.
        :type name: str
        """
        self._name = name

    @property
    def instance_id(self):
        r"""Gets the instance_id of this InstanceCompliant.

        节点ID

        :return: The instance_id of this InstanceCompliant.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this InstanceCompliant.

        节点ID

        :param instance_id: The instance_id of this InstanceCompliant.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this InstanceCompliant.

        cce集群节点ID

        :return: The node_id of this InstanceCompliant.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this InstanceCompliant.

        cce集群节点ID

        :param node_id: The node_id of this InstanceCompliant.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def ip(self):
        r"""Gets the ip of this InstanceCompliant.

        节点IP

        :return: The ip of this InstanceCompliant.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this InstanceCompliant.

        节点IP

        :param ip: The ip of this InstanceCompliant.
        :type ip: str
        """
        self._ip = ip

    @property
    def eip(self):
        r"""Gets the eip of this InstanceCompliant.

        弹性公网ip

        :return: The eip of this InstanceCompliant.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this InstanceCompliant.

        弹性公网ip

        :param eip: The eip of this InstanceCompliant.
        :type eip: str
        """
        self._eip = eip

    @property
    def region(self):
        r"""Gets the region of this InstanceCompliant.

        区域

        :return: The region of this InstanceCompliant.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this InstanceCompliant.

        区域

        :param region: The region of this InstanceCompliant.
        :type region: str
        """
        self._region = region

    @property
    def group(self):
        r"""Gets the group of this InstanceCompliant.

        分组

        :return: The group of this InstanceCompliant.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this InstanceCompliant.

        分组

        :param group: The group of this InstanceCompliant.
        :type group: str
        """
        self._group = group

    @property
    def report_scene(self):
        r"""Gets the report_scene of this InstanceCompliant.

        报告场景(CCE,ECS)

        :return: The report_scene of this InstanceCompliant.
        :rtype: str
        """
        return self._report_scene

    @report_scene.setter
    def report_scene(self, report_scene):
        r"""Sets the report_scene of this InstanceCompliant.

        报告场景(CCE,ECS)

        :param report_scene: The report_scene of this InstanceCompliant.
        :type report_scene: str
        """
        self._report_scene = report_scene

    @property
    def cce_info_id(self):
        r"""Gets the cce_info_id of this InstanceCompliant.

        cce 集群信息id

        :return: The cce_info_id of this InstanceCompliant.
        :rtype: str
        """
        return self._cce_info_id

    @cce_info_id.setter
    def cce_info_id(self, cce_info_id):
        r"""Sets the cce_info_id of this InstanceCompliant.

        cce 集群信息id

        :param cce_info_id: The cce_info_id of this InstanceCompliant.
        :type cce_info_id: str
        """
        self._cce_info_id = cce_info_id

    @property
    def status(self):
        r"""Gets the status of this InstanceCompliant.

        合规性状态

        :return: The status of this InstanceCompliant.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceCompliant.

        合规性状态

        :param status: The status of this InstanceCompliant.
        :type status: str
        """
        self._status = status

    @property
    def baseline_id(self):
        r"""Gets the baseline_id of this InstanceCompliant.

        基线id

        :return: The baseline_id of this InstanceCompliant.
        :rtype: str
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        r"""Sets the baseline_id of this InstanceCompliant.

        基线id

        :param baseline_id: The baseline_id of this InstanceCompliant.
        :type baseline_id: str
        """
        self._baseline_id = baseline_id

    @property
    def baseline_name(self):
        r"""Gets the baseline_name of this InstanceCompliant.

        基线名称

        :return: The baseline_name of this InstanceCompliant.
        :rtype: str
        """
        return self._baseline_name

    @baseline_name.setter
    def baseline_name(self, baseline_name):
        r"""Sets the baseline_name of this InstanceCompliant.

        基线名称

        :param baseline_name: The baseline_name of this InstanceCompliant.
        :type baseline_name: str
        """
        self._baseline_name = baseline_name

    @property
    def rule_type(self):
        r"""Gets the rule_type of this InstanceCompliant.

        基线规则类型

        :return: The rule_type of this InstanceCompliant.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this InstanceCompliant.

        基线规则类型

        :param rule_type: The rule_type of this InstanceCompliant.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def operating_system(self):
        r"""Gets the operating_system of this InstanceCompliant.

        操作系统

        :return: The operating_system of this InstanceCompliant.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this InstanceCompliant.

        操作系统

        :param operating_system: The operating_system of this InstanceCompliant.
        :type operating_system: str
        """
        self._operating_system = operating_system

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
        if not isinstance(other, InstanceCompliant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
