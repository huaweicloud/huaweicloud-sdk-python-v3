# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class V2AgencyPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'display_name': 'str',
        'is_required': 'bool',
        'is_enable': 'bool',
        'description': 'str',
        'action_details': 'list[ActionDetail]',
        'create_time': 'datetime',
        'changed_action_details': 'list[ChangedActionDetail]'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'display_name': 'display_name',
        'is_required': 'is_required',
        'is_enable': 'is_enable',
        'description': 'description',
        'action_details': 'action_details',
        'create_time': 'create_time',
        'changed_action_details': 'changed_action_details'
    }

    def __init__(self, policy_name=None, display_name=None, is_required=None, is_enable=None, description=None, action_details=None, create_time=None, changed_action_details=None):
        r"""V2AgencyPolicy

        The model defined in huaweicloud sdk

        :param policy_name: **参数解释**：权限策略名称，指定授权给AI DataLake服务的权限策略。 **取值范围**：   - AI_DATALAKE_COMMON_POLICY：基础服务相关权限策略。   - AI_DATALAKE_SELF_POLICY：服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。
        :type policy_name: str
        :param display_name: **参数解释**：权限策略名称。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~128个字符。
        :type display_name: str
        :param is_required: **参数解释**：是否是必需的。 **取值范围**：   - true：必需。   - false：非必需。
        :type is_required: bool
        :param is_enable: **参数解释**：是否已开启。只要授权过（策略存在且 effect 为 Allow），即为 true。 **取值范围**：   - true：已开启。   - false：未开启。
        :type is_enable: bool
        :param description: **参数解释**：策略描述。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~128个字符。
        :type description: str
        :param action_details: **参数解释**：权限策略的action详情列表，详细说明该策略包含的权限操作。
        :type action_details: list[:class:`huaweicloudsdkaidatalake.v2.ActionDetail`]
        :param create_time: **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSZ，UTC时间。 
        :type create_time: datetime
        :param changed_action_details: **参数解释**：策略内容与预期不一致时的 action 变更详情列表。只展示需要新增的 action（代码有但 IAM 没有的）。策略内容完全一致或策略完全缺失时返回空数组。
        :type changed_action_details: list[:class:`huaweicloudsdkaidatalake.v2.ChangedActionDetail`]
        """
        
        

        self._policy_name = None
        self._display_name = None
        self._is_required = None
        self._is_enable = None
        self._description = None
        self._action_details = None
        self._create_time = None
        self._changed_action_details = None
        self.discriminator = None

        if policy_name is not None:
            self.policy_name = policy_name
        if display_name is not None:
            self.display_name = display_name
        self.is_required = is_required
        self.is_enable = is_enable
        self.description = description
        self.action_details = action_details
        self.create_time = create_time
        self.changed_action_details = changed_action_details

    @property
    def policy_name(self):
        r"""Gets the policy_name of this V2AgencyPolicy.

        **参数解释**：权限策略名称，指定授权给AI DataLake服务的权限策略。 **取值范围**：   - AI_DATALAKE_COMMON_POLICY：基础服务相关权限策略。   - AI_DATALAKE_SELF_POLICY：服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。

        :return: The policy_name of this V2AgencyPolicy.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this V2AgencyPolicy.

        **参数解释**：权限策略名称，指定授权给AI DataLake服务的权限策略。 **取值范围**：   - AI_DATALAKE_COMMON_POLICY：基础服务相关权限策略。   - AI_DATALAKE_SELF_POLICY：服务自身访问权限策略，用于服务内部资源访问。   - AI_DATALAKE_SMN_POLICY：消息通知功能相关权限策略，用来将系统通知消息转发到SMN。   - AI_DATALAKE_LAKEFORMATION_POLICY：LakeFormation功能相关权限策略。   - AI_DATALAKE_AOM_POLICY：AOM功能相关权限策略。   - AI_DATALAKE_SWR_POLICY：镜像包注册功能相关权限策略。   - AI_DATALAKE_LTS_POLICY：日志功能相关权限策略。   - AI_DATALAKE_VPCEP_POLICY：网络打通功能相关权限策略。   - AI_DATALAKE_DNS_POLICY：DNS相关权限策略。   - AI_DATALAKE_OBS_POLICY：OBS相关权限策略。   - AI_DATALAKE_VPC_POLICY：VPC相关权限策略。   - AI_DATALAKE_DCS_POLICY：DCS相关权限策略。   - AI_DATALAKE_DEW_POLICY：DEW相关权限策略。

        :param policy_name: The policy_name of this V2AgencyPolicy.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def display_name(self):
        r"""Gets the display_name of this V2AgencyPolicy.

        **参数解释**：权限策略名称。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~128个字符。

        :return: The display_name of this V2AgencyPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this V2AgencyPolicy.

        **参数解释**：权限策略名称。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~128个字符。

        :param display_name: The display_name of this V2AgencyPolicy.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def is_required(self):
        r"""Gets the is_required of this V2AgencyPolicy.

        **参数解释**：是否是必需的。 **取值范围**：   - true：必需。   - false：非必需。

        :return: The is_required of this V2AgencyPolicy.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        r"""Sets the is_required of this V2AgencyPolicy.

        **参数解释**：是否是必需的。 **取值范围**：   - true：必需。   - false：非必需。

        :param is_required: The is_required of this V2AgencyPolicy.
        :type is_required: bool
        """
        self._is_required = is_required

    @property
    def is_enable(self):
        r"""Gets the is_enable of this V2AgencyPolicy.

        **参数解释**：是否已开启。只要授权过（策略存在且 effect 为 Allow），即为 true。 **取值范围**：   - true：已开启。   - false：未开启。

        :return: The is_enable of this V2AgencyPolicy.
        :rtype: bool
        """
        return self._is_enable

    @is_enable.setter
    def is_enable(self, is_enable):
        r"""Sets the is_enable of this V2AgencyPolicy.

        **参数解释**：是否已开启。只要授权过（策略存在且 effect 为 Allow），即为 true。 **取值范围**：   - true：已开启。   - false：未开启。

        :param is_enable: The is_enable of this V2AgencyPolicy.
        :type is_enable: bool
        """
        self._is_enable = is_enable

    @property
    def description(self):
        r"""Gets the description of this V2AgencyPolicy.

        **参数解释**：策略描述。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~128个字符。

        :return: The description of this V2AgencyPolicy.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this V2AgencyPolicy.

        **参数解释**：策略描述。 **取值范围**：支持中文字符、英文字母、数字及特殊字符，长度0~128个字符。

        :param description: The description of this V2AgencyPolicy.
        :type description: str
        """
        self._description = description

    @property
    def action_details(self):
        r"""Gets the action_details of this V2AgencyPolicy.

        **参数解释**：权限策略的action详情列表，详细说明该策略包含的权限操作。

        :return: The action_details of this V2AgencyPolicy.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ActionDetail`]
        """
        return self._action_details

    @action_details.setter
    def action_details(self, action_details):
        r"""Sets the action_details of this V2AgencyPolicy.

        **参数解释**：权限策略的action详情列表，详细说明该策略包含的权限操作。

        :param action_details: The action_details of this V2AgencyPolicy.
        :type action_details: list[:class:`huaweicloudsdkaidatalake.v2.ActionDetail`]
        """
        self._action_details = action_details

    @property
    def create_time(self):
        r"""Gets the create_time of this V2AgencyPolicy.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :return: The create_time of this V2AgencyPolicy.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this V2AgencyPolicy.

        **参数解释**：资源创建时间。 **取值范围**：ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSZ，UTC时间。 

        :param create_time: The create_time of this V2AgencyPolicy.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def changed_action_details(self):
        r"""Gets the changed_action_details of this V2AgencyPolicy.

        **参数解释**：策略内容与预期不一致时的 action 变更详情列表。只展示需要新增的 action（代码有但 IAM 没有的）。策略内容完全一致或策略完全缺失时返回空数组。

        :return: The changed_action_details of this V2AgencyPolicy.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.ChangedActionDetail`]
        """
        return self._changed_action_details

    @changed_action_details.setter
    def changed_action_details(self, changed_action_details):
        r"""Sets the changed_action_details of this V2AgencyPolicy.

        **参数解释**：策略内容与预期不一致时的 action 变更详情列表。只展示需要新增的 action（代码有但 IAM 没有的）。策略内容完全一致或策略完全缺失时返回空数组。

        :param changed_action_details: The changed_action_details of this V2AgencyPolicy.
        :type changed_action_details: list[:class:`huaweicloudsdkaidatalake.v2.ChangedActionDetail`]
        """
        self._changed_action_details = changed_action_details

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
        if not isinstance(other, V2AgencyPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
