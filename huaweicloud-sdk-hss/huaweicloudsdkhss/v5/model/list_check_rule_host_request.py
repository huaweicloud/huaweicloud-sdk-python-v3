# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCheckRuleHostRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'check_rule_id': 'str',
        'check_name': 'str',
        'check_type': 'str',
        'standard': 'str',
        'result_type': 'str',
        'cluster_id': 'str',
        'host_name': 'str',
        'host_type': 'str',
        'check_cce': 'bool',
        'policy_group_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'check_rule_id': 'check_rule_id',
        'check_name': 'check_name',
        'check_type': 'check_type',
        'standard': 'standard',
        'result_type': 'result_type',
        'cluster_id': 'cluster_id',
        'host_name': 'host_name',
        'host_type': 'host_type',
        'check_cce': 'check_cce',
        'policy_group_id': 'policy_group_id'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, check_rule_id=None, check_name=None, check_type=None, standard=None, result_type=None, cluster_id=None, host_name=None, host_type=None, check_cce=None, policy_group_id=None):
        r"""ListCheckRuleHostRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param check_rule_id: **参数解释** 具体基线检查项id **约束限制** 不涉及 **取值范围** - 值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules  **默认取值** 不涉及
        :type check_rule_id: str
        :param check_name: **参数解释** 配置检查（基线）的名称，如SSH、CentOS 7、Windows，与check_type相比，会多-PID之类的进程信息，通过具体基线维度查询时，传check_name **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及
        :type check_name: str
        :param check_type: **参数解释** 配置检查（基线）的类型，如SSH、CentOS 7、Windows，通过检查项维度查询时，传check_type **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及
        :type check_type: str
        :param standard: **参数解释** 基线分类 **约束限制** 不涉及 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及
        :type standard: str
        :param result_type: **参数解释** 检测结果类型 **约束限制** 不涉及 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白  **默认取值** 不涉及
        :type result_type: str
        :param cluster_id: **参数解释** 集群ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及
        :type cluster_id: str
        :param host_name: **参数解释** 主机名称或ip **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及
        :type host_name: str
        :param host_type: **参数解释** 主机类型，已废弃 **约束限制** 不涉及 **取值范围** - cce  **默认取值** 不涉及
        :type host_type: str
        :param check_cce: **参数解释**: 是否只筛选cce主机，已废弃 **约束限制**: 不涉及 **取值范围**: -true：是。 -false：否。  **默认取值**: false 
        :type check_cce: bool
        :param policy_group_id: **参数解释** 策略组ID，已废弃 **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及
        :type policy_group_id: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._check_rule_id = None
        self._check_name = None
        self._check_type = None
        self._standard = None
        self._result_type = None
        self._cluster_id = None
        self._host_name = None
        self._host_type = None
        self._check_cce = None
        self._policy_group_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.check_rule_id = check_rule_id
        if check_name is not None:
            self.check_name = check_name
        if check_type is not None:
            self.check_type = check_type
        self.standard = standard
        if result_type is not None:
            self.result_type = result_type
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if host_name is not None:
            self.host_name = host_name
        if host_type is not None:
            self.host_type = host_type
        if check_cce is not None:
            self.check_cce = check_cce
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListCheckRuleHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListCheckRuleHostRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListCheckRuleHostRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListCheckRuleHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListCheckRuleHostRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCheckRuleHostRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListCheckRuleHostRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListCheckRuleHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListCheckRuleHostRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCheckRuleHostRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListCheckRuleHostRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def check_rule_id(self):
        r"""Gets the check_rule_id of this ListCheckRuleHostRequest.

        **参数解释** 具体基线检查项id **约束限制** 不涉及 **取值范围** - 值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules  **默认取值** 不涉及

        :return: The check_rule_id of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._check_rule_id

    @check_rule_id.setter
    def check_rule_id(self, check_rule_id):
        r"""Sets the check_rule_id of this ListCheckRuleHostRequest.

        **参数解释** 具体基线检查项id **约束限制** 不涉及 **取值范围** - 值可以通过这个接口的返回数据获得：/v5/{project_id}/baseline/risk-config/{check_name}/check-rules  **默认取值** 不涉及

        :param check_rule_id: The check_rule_id of this ListCheckRuleHostRequest.
        :type check_rule_id: str
        """
        self._check_rule_id = check_rule_id

    @property
    def check_name(self):
        r"""Gets the check_name of this ListCheckRuleHostRequest.

        **参数解释** 配置检查（基线）的名称，如SSH、CentOS 7、Windows，与check_type相比，会多-PID之类的进程信息，通过具体基线维度查询时，传check_name **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :return: The check_name of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._check_name

    @check_name.setter
    def check_name(self, check_name):
        r"""Sets the check_name of this ListCheckRuleHostRequest.

        **参数解释** 配置检查（基线）的名称，如SSH、CentOS 7、Windows，与check_type相比，会多-PID之类的进程信息，通过具体基线维度查询时，传check_name **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :param check_name: The check_name of this ListCheckRuleHostRequest.
        :type check_name: str
        """
        self._check_name = check_name

    @property
    def check_type(self):
        r"""Gets the check_type of this ListCheckRuleHostRequest.

        **参数解释** 配置检查（基线）的类型，如SSH、CentOS 7、Windows，通过检查项维度查询时，传check_type **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :return: The check_type of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        r"""Sets the check_type of this ListCheckRuleHostRequest.

        **参数解释** 配置检查（基线）的类型，如SSH、CentOS 7、Windows，通过检查项维度查询时，传check_type **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :param check_type: The check_type of this ListCheckRuleHostRequest.
        :type check_type: str
        """
        self._check_type = check_type

    @property
    def standard(self):
        r"""Gets the standard of this ListCheckRuleHostRequest.

        **参数解释** 基线分类 **约束限制** 不涉及 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及

        :return: The standard of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._standard

    @standard.setter
    def standard(self, standard):
        r"""Sets the standard of this ListCheckRuleHostRequest.

        **参数解释** 基线分类 **约束限制** 不涉及 **取值范围** - cn_standard : 等保合规标准 - hw_standard : 云安全实践标准 - cis_standard：通用安全标准  **默认取值** 不涉及

        :param standard: The standard of this ListCheckRuleHostRequest.
        :type standard: str
        """
        self._standard = standard

    @property
    def result_type(self):
        r"""Gets the result_type of this ListCheckRuleHostRequest.

        **参数解释** 检测结果类型 **约束限制** 不涉及 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白  **默认取值** 不涉及

        :return: The result_type of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        r"""Sets the result_type of this ListCheckRuleHostRequest.

        **参数解释** 检测结果类型 **约束限制** 不涉及 **取值范围** - safe             : 已通过 - unhandled        : 未处理 - ignored          : 已忽略 - fixing           : 修复中 - fix-failed       : 修复失败 - verifying        : 验证中 - add_to_whitelist : 已加白  **默认取值** 不涉及

        :param result_type: The result_type of this ListCheckRuleHostRequest.
        :type result_type: str
        """
        self._result_type = result_type

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListCheckRuleHostRequest.

        **参数解释** 集群ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :return: The cluster_id of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListCheckRuleHostRequest.

        **参数解释** 集群ID **约束限制** 不涉及 **取值范围** 字符长度0-64位 **默认取值** 不涉及

        :param cluster_id: The cluster_id of this ListCheckRuleHostRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def host_name(self):
        r"""Gets the host_name of this ListCheckRuleHostRequest.

        **参数解释** 主机名称或ip **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :return: The host_name of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        r"""Sets the host_name of this ListCheckRuleHostRequest.

        **参数解释** 主机名称或ip **约束限制** 不涉及 **取值范围** 不涉及 **默认取值** 不涉及

        :param host_name: The host_name of this ListCheckRuleHostRequest.
        :type host_name: str
        """
        self._host_name = host_name

    @property
    def host_type(self):
        r"""Gets the host_type of this ListCheckRuleHostRequest.

        **参数解释** 主机类型，已废弃 **约束限制** 不涉及 **取值范围** - cce  **默认取值** 不涉及

        :return: The host_type of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._host_type

    @host_type.setter
    def host_type(self, host_type):
        r"""Sets the host_type of this ListCheckRuleHostRequest.

        **参数解释** 主机类型，已废弃 **约束限制** 不涉及 **取值范围** - cce  **默认取值** 不涉及

        :param host_type: The host_type of this ListCheckRuleHostRequest.
        :type host_type: str
        """
        self._host_type = host_type

    @property
    def check_cce(self):
        r"""Gets the check_cce of this ListCheckRuleHostRequest.

        **参数解释**: 是否只筛选cce主机，已废弃 **约束限制**: 不涉及 **取值范围**: -true：是。 -false：否。  **默认取值**: false 

        :return: The check_cce of this ListCheckRuleHostRequest.
        :rtype: bool
        """
        return self._check_cce

    @check_cce.setter
    def check_cce(self, check_cce):
        r"""Sets the check_cce of this ListCheckRuleHostRequest.

        **参数解释**: 是否只筛选cce主机，已废弃 **约束限制**: 不涉及 **取值范围**: -true：是。 -false：否。  **默认取值**: false 

        :param check_cce: The check_cce of this ListCheckRuleHostRequest.
        :type check_cce: bool
        """
        self._check_cce = check_cce

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListCheckRuleHostRequest.

        **参数解释** 策略组ID，已废弃 **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :return: The policy_group_id of this ListCheckRuleHostRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListCheckRuleHostRequest.

        **参数解释** 策略组ID，已废弃 **约束限制** 不涉及 **取值范围** 字符长度0-128位 **默认取值** 不涉及

        :param policy_group_id: The policy_group_id of this ListCheckRuleHostRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

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
        if not isinstance(other, ListCheckRuleHostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
