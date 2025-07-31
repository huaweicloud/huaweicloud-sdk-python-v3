# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIacFileRisksResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'risk_id': 'str',
        'rule_id': 'str',
        'risk_name': 'str',
        'risk_level': 'str',
        'risk_category': 'str',
        'risk_num': 'int',
        'last_scan_time': 'int',
        'description': 'str',
        'remediation': 'str',
        'build_instruction': 'str'
    }

    attribute_map = {
        'risk_id': 'risk_id',
        'rule_id': 'rule_id',
        'risk_name': 'risk_name',
        'risk_level': 'risk_level',
        'risk_category': 'risk_category',
        'risk_num': 'risk_num',
        'last_scan_time': 'last_scan_time',
        'description': 'description',
        'remediation': 'remediation',
        'build_instruction': 'build_instruction'
    }

    def __init__(self, risk_id=None, rule_id=None, risk_name=None, risk_level=None, risk_category=None, risk_num=None, last_scan_time=None, description=None, remediation=None, build_instruction=None):
        r"""ListIacFileRisksResponseInfoDataList

        The model defined in huaweicloud sdk

        :param risk_id: 风险id
        :type risk_id: str
        :param rule_id: 风险检测规则id
        :type rule_id: str
        :param risk_name: 风险名称
        :type risk_name: str
        :param risk_level: 风险程度，包含如下   - high ：高危   - medium ：中危   - low ：低危   - tips ：提示
        :type risk_level: str
        :param risk_category: 风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸
        :type risk_category: str
        :param risk_num: 风险数量
        :type risk_num: int
        :param last_scan_time: 最近一次扫描时间
        :type last_scan_time: int
        :param description: 风险描述
        :type description: str
        :param remediation: 风险的处置建议
        :type remediation: str
        :param build_instruction: 存在风险的构建指令
        :type build_instruction: str
        """
        
        

        self._risk_id = None
        self._rule_id = None
        self._risk_name = None
        self._risk_level = None
        self._risk_category = None
        self._risk_num = None
        self._last_scan_time = None
        self._description = None
        self._remediation = None
        self._build_instruction = None
        self.discriminator = None

        if risk_id is not None:
            self.risk_id = risk_id
        if rule_id is not None:
            self.rule_id = rule_id
        if risk_name is not None:
            self.risk_name = risk_name
        if risk_level is not None:
            self.risk_level = risk_level
        if risk_category is not None:
            self.risk_category = risk_category
        if risk_num is not None:
            self.risk_num = risk_num
        if last_scan_time is not None:
            self.last_scan_time = last_scan_time
        if description is not None:
            self.description = description
        if remediation is not None:
            self.remediation = remediation
        if build_instruction is not None:
            self.build_instruction = build_instruction

    @property
    def risk_id(self):
        r"""Gets the risk_id of this ListIacFileRisksResponseInfoDataList.

        风险id

        :return: The risk_id of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._risk_id

    @risk_id.setter
    def risk_id(self, risk_id):
        r"""Sets the risk_id of this ListIacFileRisksResponseInfoDataList.

        风险id

        :param risk_id: The risk_id of this ListIacFileRisksResponseInfoDataList.
        :type risk_id: str
        """
        self._risk_id = risk_id

    @property
    def rule_id(self):
        r"""Gets the rule_id of this ListIacFileRisksResponseInfoDataList.

        风险检测规则id

        :return: The rule_id of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        r"""Sets the rule_id of this ListIacFileRisksResponseInfoDataList.

        风险检测规则id

        :param rule_id: The rule_id of this ListIacFileRisksResponseInfoDataList.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def risk_name(self):
        r"""Gets the risk_name of this ListIacFileRisksResponseInfoDataList.

        风险名称

        :return: The risk_name of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._risk_name

    @risk_name.setter
    def risk_name(self, risk_name):
        r"""Sets the risk_name of this ListIacFileRisksResponseInfoDataList.

        风险名称

        :param risk_name: The risk_name of this ListIacFileRisksResponseInfoDataList.
        :type risk_name: str
        """
        self._risk_name = risk_name

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ListIacFileRisksResponseInfoDataList.

        风险程度，包含如下   - high ：高危   - medium ：中危   - low ：低危   - tips ：提示

        :return: The risk_level of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ListIacFileRisksResponseInfoDataList.

        风险程度，包含如下   - high ：高危   - medium ：中危   - low ：低危   - tips ：提示

        :param risk_level: The risk_level of this ListIacFileRisksResponseInfoDataList.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def risk_category(self):
        r"""Gets the risk_category of this ListIacFileRisksResponseInfoDataList.

        风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸

        :return: The risk_category of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._risk_category

    @risk_category.setter
    def risk_category(self, risk_category):
        r"""Sets the risk_category of this ListIacFileRisksResponseInfoDataList.

        风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸

        :param risk_category: The risk_category of this ListIacFileRisksResponseInfoDataList.
        :type risk_category: str
        """
        self._risk_category = risk_category

    @property
    def risk_num(self):
        r"""Gets the risk_num of this ListIacFileRisksResponseInfoDataList.

        风险数量

        :return: The risk_num of this ListIacFileRisksResponseInfoDataList.
        :rtype: int
        """
        return self._risk_num

    @risk_num.setter
    def risk_num(self, risk_num):
        r"""Sets the risk_num of this ListIacFileRisksResponseInfoDataList.

        风险数量

        :param risk_num: The risk_num of this ListIacFileRisksResponseInfoDataList.
        :type risk_num: int
        """
        self._risk_num = risk_num

    @property
    def last_scan_time(self):
        r"""Gets the last_scan_time of this ListIacFileRisksResponseInfoDataList.

        最近一次扫描时间

        :return: The last_scan_time of this ListIacFileRisksResponseInfoDataList.
        :rtype: int
        """
        return self._last_scan_time

    @last_scan_time.setter
    def last_scan_time(self, last_scan_time):
        r"""Sets the last_scan_time of this ListIacFileRisksResponseInfoDataList.

        最近一次扫描时间

        :param last_scan_time: The last_scan_time of this ListIacFileRisksResponseInfoDataList.
        :type last_scan_time: int
        """
        self._last_scan_time = last_scan_time

    @property
    def description(self):
        r"""Gets the description of this ListIacFileRisksResponseInfoDataList.

        风险描述

        :return: The description of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListIacFileRisksResponseInfoDataList.

        风险描述

        :param description: The description of this ListIacFileRisksResponseInfoDataList.
        :type description: str
        """
        self._description = description

    @property
    def remediation(self):
        r"""Gets the remediation of this ListIacFileRisksResponseInfoDataList.

        风险的处置建议

        :return: The remediation of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._remediation

    @remediation.setter
    def remediation(self, remediation):
        r"""Sets the remediation of this ListIacFileRisksResponseInfoDataList.

        风险的处置建议

        :param remediation: The remediation of this ListIacFileRisksResponseInfoDataList.
        :type remediation: str
        """
        self._remediation = remediation

    @property
    def build_instruction(self):
        r"""Gets the build_instruction of this ListIacFileRisksResponseInfoDataList.

        存在风险的构建指令

        :return: The build_instruction of this ListIacFileRisksResponseInfoDataList.
        :rtype: str
        """
        return self._build_instruction

    @build_instruction.setter
    def build_instruction(self, build_instruction):
        r"""Sets the build_instruction of this ListIacFileRisksResponseInfoDataList.

        存在风险的构建指令

        :param build_instruction: The build_instruction of this ListIacFileRisksResponseInfoDataList.
        :type build_instruction: str
        """
        self._build_instruction = build_instruction

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
        if not isinstance(other, ListIacFileRisksResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
