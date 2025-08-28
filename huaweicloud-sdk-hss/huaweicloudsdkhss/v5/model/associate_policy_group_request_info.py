# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociatePolicyGroupRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_policy_group_id': 'str',
        'operate_all': 'bool',
        'deploy_type': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'target_policy_group_id': 'target_policy_group_id',
        'operate_all': 'operate_all',
        'deploy_type': 'deploy_type',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, target_policy_group_id=None, operate_all=None, deploy_type=None, host_id_list=None):
        r"""AssociatePolicyGroupRequestInfo

        The model defined in huaweicloud sdk

        :param target_policy_group_id: **参数解释**: 部署的目标策略组ID **约束限制**: 需查询ListPolicyGroup接口，仅支持传其返回参数data_list中support_version等于hss.version.premium或hss.version.container.enterprise的group_id **取值范围**: 只能由英文字母、数字及“-”组成，字符长度36-64位 **默认取值**: 不涉及 
        :type target_policy_group_id: str
        :param operate_all: **参数解释**: 是否要对全量主机/pod实例/工作负载/集群部署策略，如果为true的话，会自动筛选符合策略组支持版本和操作系统版本的全量主机/pod实例/工作负载/集群部署策略，不需填写host_id_list，如果为false的话，需要填写host_id_list **约束限制**: 不涉及 **取值范围**: - true: 自动筛选符合策略组支持版本和操作系统版本的全量主机/pod实例/工作负载/集群部署策略，不需填写host_id_list。 - false: 非全量部署，仅对指定的主机/pod实例/工作负载/集群部署策略，需要填写host_id_list。  **默认取值**: 不涉及 
        :type operate_all: bool
        :param deploy_type: **参数解释**: 需要部署策略组的实例类型（预留字段） **约束限制**: 不涉及 **取值范围**: - host: 主机。 - pod: pod实例。 - workload: 工作负载。 - cluster: 集群。  **默认取值**: host 
        :type deploy_type: str
        :param host_id_list: **参数解释**: 需要部署策略组的已开启旗舰版或容器版防护的主机/pod实例/负载/集群ID列表 **约束限制**: 需查询ListHostStatus接口，仅支持传其返回参数data_list中version等于hss.version.premium或hss.version.container.enterprise的host_id **取值范围**: 最少0条，最多10000条 **默认取值**: 不涉及 
        :type host_id_list: list[str]
        """
        
        

        self._target_policy_group_id = None
        self._operate_all = None
        self._deploy_type = None
        self._host_id_list = None
        self.discriminator = None

        self.target_policy_group_id = target_policy_group_id
        if operate_all is not None:
            self.operate_all = operate_all
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if host_id_list is not None:
            self.host_id_list = host_id_list

    @property
    def target_policy_group_id(self):
        r"""Gets the target_policy_group_id of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 部署的目标策略组ID **约束限制**: 需查询ListPolicyGroup接口，仅支持传其返回参数data_list中support_version等于hss.version.premium或hss.version.container.enterprise的group_id **取值范围**: 只能由英文字母、数字及“-”组成，字符长度36-64位 **默认取值**: 不涉及 

        :return: The target_policy_group_id of this AssociatePolicyGroupRequestInfo.
        :rtype: str
        """
        return self._target_policy_group_id

    @target_policy_group_id.setter
    def target_policy_group_id(self, target_policy_group_id):
        r"""Sets the target_policy_group_id of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 部署的目标策略组ID **约束限制**: 需查询ListPolicyGroup接口，仅支持传其返回参数data_list中support_version等于hss.version.premium或hss.version.container.enterprise的group_id **取值范围**: 只能由英文字母、数字及“-”组成，字符长度36-64位 **默认取值**: 不涉及 

        :param target_policy_group_id: The target_policy_group_id of this AssociatePolicyGroupRequestInfo.
        :type target_policy_group_id: str
        """
        self._target_policy_group_id = target_policy_group_id

    @property
    def operate_all(self):
        r"""Gets the operate_all of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 是否要对全量主机/pod实例/工作负载/集群部署策略，如果为true的话，会自动筛选符合策略组支持版本和操作系统版本的全量主机/pod实例/工作负载/集群部署策略，不需填写host_id_list，如果为false的话，需要填写host_id_list **约束限制**: 不涉及 **取值范围**: - true: 自动筛选符合策略组支持版本和操作系统版本的全量主机/pod实例/工作负载/集群部署策略，不需填写host_id_list。 - false: 非全量部署，仅对指定的主机/pod实例/工作负载/集群部署策略，需要填写host_id_list。  **默认取值**: 不涉及 

        :return: The operate_all of this AssociatePolicyGroupRequestInfo.
        :rtype: bool
        """
        return self._operate_all

    @operate_all.setter
    def operate_all(self, operate_all):
        r"""Sets the operate_all of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 是否要对全量主机/pod实例/工作负载/集群部署策略，如果为true的话，会自动筛选符合策略组支持版本和操作系统版本的全量主机/pod实例/工作负载/集群部署策略，不需填写host_id_list，如果为false的话，需要填写host_id_list **约束限制**: 不涉及 **取值范围**: - true: 自动筛选符合策略组支持版本和操作系统版本的全量主机/pod实例/工作负载/集群部署策略，不需填写host_id_list。 - false: 非全量部署，仅对指定的主机/pod实例/工作负载/集群部署策略，需要填写host_id_list。  **默认取值**: 不涉及 

        :param operate_all: The operate_all of this AssociatePolicyGroupRequestInfo.
        :type operate_all: bool
        """
        self._operate_all = operate_all

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 需要部署策略组的实例类型（预留字段） **约束限制**: 不涉及 **取值范围**: - host: 主机。 - pod: pod实例。 - workload: 工作负载。 - cluster: 集群。  **默认取值**: host 

        :return: The deploy_type of this AssociatePolicyGroupRequestInfo.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 需要部署策略组的实例类型（预留字段） **约束限制**: 不涉及 **取值范围**: - host: 主机。 - pod: pod实例。 - workload: 工作负载。 - cluster: 集群。  **默认取值**: host 

        :param deploy_type: The deploy_type of this AssociatePolicyGroupRequestInfo.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 需要部署策略组的已开启旗舰版或容器版防护的主机/pod实例/负载/集群ID列表 **约束限制**: 需查询ListHostStatus接口，仅支持传其返回参数data_list中version等于hss.version.premium或hss.version.container.enterprise的host_id **取值范围**: 最少0条，最多10000条 **默认取值**: 不涉及 

        :return: The host_id_list of this AssociatePolicyGroupRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this AssociatePolicyGroupRequestInfo.

        **参数解释**: 需要部署策略组的已开启旗舰版或容器版防护的主机/pod实例/负载/集群ID列表 **约束限制**: 需查询ListHostStatus接口，仅支持传其返回参数data_list中version等于hss.version.premium或hss.version.container.enterprise的host_id **取值范围**: 最少0条，最多10000条 **默认取值**: 不涉及 

        :param host_id_list: The host_id_list of this AssociatePolicyGroupRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, AssociatePolicyGroupRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
