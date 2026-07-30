# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiPolicyGroupInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'group_name': 'str',
        'group_type': 'int',
        'project_id': 'str',
        'protection_object': 'str',
        'object_type': 'int',
        'object_num': 'int',
        'is_default': 'bool',
        'is_exclusive': 'bool',
        'enabled': 'bool',
        'detail_is_used': 'bool',
        'description': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'policy_list': 'list[AiPolicyList]',
        'agent_id_list': 'list[str]'
    }

    attribute_map = {
        'group_id': 'group_id',
        'group_name': 'group_name',
        'group_type': 'group_type',
        'project_id': 'project_id',
        'protection_object': 'protection_object',
        'object_type': 'object_type',
        'object_num': 'object_num',
        'is_default': 'is_default',
        'is_exclusive': 'is_exclusive',
        'enabled': 'enabled',
        'detail_is_used': 'detail_is_used',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'policy_list': 'policy_list',
        'agent_id_list': 'agent_id_list'
    }

    def __init__(self, group_id=None, group_name=None, group_type=None, project_id=None, protection_object=None, object_type=None, object_num=None, is_default=None, is_exclusive=None, enabled=None, detail_is_used=None, description=None, create_time=None, update_time=None, policy_list=None, agent_id_list=None):
        r"""AiPolicyGroupInfo

        The model defined in huaweicloud sdk

        :param group_id: **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 
        :type group_id: str
        :param group_name: **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 
        :type group_name: str
        :param group_type: **参数解释**： 策略组ID **取值范围**： 最小值0，最大值2147483647 
        :type group_type: int
        :param project_id: 项目ID
        :type project_id: str
        :param protection_object: **参数解释**： 防护对象 **取值范围**： 字符长度1-128位 
        :type protection_object: str
        :param object_type: **参数解释**: 防护对象类型 **取值范围**: - 0：云服务 - 1：三方 
        :type object_type: int
        :param object_num: **参数解释**: 防护对象个数 **取值范围**: 取值0-100000 
        :type object_num: int
        :param is_default: **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 
        :type is_default: bool
        :param is_exclusive: **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 
        :type is_exclusive: bool
        :param enabled: **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 
        :type enabled: bool
        :param detail_is_used: **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 
        :type detail_is_used: bool
        :param description: **参数解释**: 描述 **取值范围**: 字符长度0-256位 
        :type description: str
        :param create_time: **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type create_time: int
        :param update_time: **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 
        :type update_time: int
        :param policy_list: **参数解释**: 策略列表 **取值范围**: 不涉及 
        :type policy_list: list[:class:`huaweicloudsdkhss.v5.AiPolicyList`]
        :param agent_id_list: **参数解释**: 智能体列表 **取值范围**: 不涉及 
        :type agent_id_list: list[str]
        """
        
        

        self._group_id = None
        self._group_name = None
        self._group_type = None
        self._project_id = None
        self._protection_object = None
        self._object_type = None
        self._object_num = None
        self._is_default = None
        self._is_exclusive = None
        self._enabled = None
        self._detail_is_used = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._policy_list = None
        self._agent_id_list = None
        self.discriminator = None

        if group_id is not None:
            self.group_id = group_id
        if group_name is not None:
            self.group_name = group_name
        if group_type is not None:
            self.group_type = group_type
        if project_id is not None:
            self.project_id = project_id
        if protection_object is not None:
            self.protection_object = protection_object
        if object_type is not None:
            self.object_type = object_type
        if object_num is not None:
            self.object_num = object_num
        if is_default is not None:
            self.is_default = is_default
        if is_exclusive is not None:
            self.is_exclusive = is_exclusive
        if enabled is not None:
            self.enabled = enabled
        if detail_is_used is not None:
            self.detail_is_used = detail_is_used
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if policy_list is not None:
            self.policy_list = policy_list
        if agent_id_list is not None:
            self.agent_id_list = agent_id_list

    @property
    def group_id(self):
        r"""Gets the group_id of this AiPolicyGroupInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 

        :return: The group_id of this AiPolicyGroupInfo.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this AiPolicyGroupInfo.

        **参数解释**： 策略组ID **取值范围**： 字符长度1-20位 

        :param group_id: The group_id of this AiPolicyGroupInfo.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def group_name(self):
        r"""Gets the group_name of this AiPolicyGroupInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 

        :return: The group_name of this AiPolicyGroupInfo.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        r"""Sets the group_name of this AiPolicyGroupInfo.

        **参数解释**: 策略组名称 **取值范围**: 字符长度1-128位 

        :param group_name: The group_name of this AiPolicyGroupInfo.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_type(self):
        r"""Gets the group_type of this AiPolicyGroupInfo.

        **参数解释**： 策略组ID **取值范围**： 最小值0，最大值2147483647 

        :return: The group_type of this AiPolicyGroupInfo.
        :rtype: int
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this AiPolicyGroupInfo.

        **参数解释**： 策略组ID **取值范围**： 最小值0，最大值2147483647 

        :param group_type: The group_type of this AiPolicyGroupInfo.
        :type group_type: int
        """
        self._group_type = group_type

    @property
    def project_id(self):
        r"""Gets the project_id of this AiPolicyGroupInfo.

        项目ID

        :return: The project_id of this AiPolicyGroupInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AiPolicyGroupInfo.

        项目ID

        :param project_id: The project_id of this AiPolicyGroupInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def protection_object(self):
        r"""Gets the protection_object of this AiPolicyGroupInfo.

        **参数解释**： 防护对象 **取值范围**： 字符长度1-128位 

        :return: The protection_object of this AiPolicyGroupInfo.
        :rtype: str
        """
        return self._protection_object

    @protection_object.setter
    def protection_object(self, protection_object):
        r"""Sets the protection_object of this AiPolicyGroupInfo.

        **参数解释**： 防护对象 **取值范围**： 字符长度1-128位 

        :param protection_object: The protection_object of this AiPolicyGroupInfo.
        :type protection_object: str
        """
        self._protection_object = protection_object

    @property
    def object_type(self):
        r"""Gets the object_type of this AiPolicyGroupInfo.

        **参数解释**: 防护对象类型 **取值范围**: - 0：云服务 - 1：三方 

        :return: The object_type of this AiPolicyGroupInfo.
        :rtype: int
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this AiPolicyGroupInfo.

        **参数解释**: 防护对象类型 **取值范围**: - 0：云服务 - 1：三方 

        :param object_type: The object_type of this AiPolicyGroupInfo.
        :type object_type: int
        """
        self._object_type = object_type

    @property
    def object_num(self):
        r"""Gets the object_num of this AiPolicyGroupInfo.

        **参数解释**: 防护对象个数 **取值范围**: 取值0-100000 

        :return: The object_num of this AiPolicyGroupInfo.
        :rtype: int
        """
        return self._object_num

    @object_num.setter
    def object_num(self, object_num):
        r"""Sets the object_num of this AiPolicyGroupInfo.

        **参数解释**: 防护对象个数 **取值范围**: 取值0-100000 

        :param object_num: The object_num of this AiPolicyGroupInfo.
        :type object_num: int
        """
        self._object_num = object_num

    @property
    def is_default(self):
        r"""Gets the is_default of this AiPolicyGroupInfo.

        **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 

        :return: The is_default of this AiPolicyGroupInfo.
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        r"""Sets the is_default of this AiPolicyGroupInfo.

        **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 

        :param is_default: The is_default of this AiPolicyGroupInfo.
        :type is_default: bool
        """
        self._is_default = is_default

    @property
    def is_exclusive(self):
        r"""Gets the is_exclusive of this AiPolicyGroupInfo.

        **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 

        :return: The is_exclusive of this AiPolicyGroupInfo.
        :rtype: bool
        """
        return self._is_exclusive

    @is_exclusive.setter
    def is_exclusive(self, is_exclusive):
        r"""Sets the is_exclusive of this AiPolicyGroupInfo.

        **参数解释**: 是否是默认策略 **取值范围**: - false：否 - true：是 

        :param is_exclusive: The is_exclusive of this AiPolicyGroupInfo.
        :type is_exclusive: bool
        """
        self._is_exclusive = is_exclusive

    @property
    def enabled(self):
        r"""Gets the enabled of this AiPolicyGroupInfo.

        **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 

        :return: The enabled of this AiPolicyGroupInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AiPolicyGroupInfo.

        **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 

        :param enabled: The enabled of this AiPolicyGroupInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def detail_is_used(self):
        r"""Gets the detail_is_used of this AiPolicyGroupInfo.

        **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 

        :return: The detail_is_used of this AiPolicyGroupInfo.
        :rtype: bool
        """
        return self._detail_is_used

    @detail_is_used.setter
    def detail_is_used(self, detail_is_used):
        r"""Sets the detail_is_used of this AiPolicyGroupInfo.

        **参数解释**: 是否启用 **取值范围**: - false：否 - true：是 

        :param detail_is_used: The detail_is_used of this AiPolicyGroupInfo.
        :type detail_is_used: bool
        """
        self._detail_is_used = detail_is_used

    @property
    def description(self):
        r"""Gets the description of this AiPolicyGroupInfo.

        **参数解释**: 描述 **取值范围**: 字符长度0-256位 

        :return: The description of this AiPolicyGroupInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AiPolicyGroupInfo.

        **参数解释**: 描述 **取值范围**: 字符长度0-256位 

        :param description: The description of this AiPolicyGroupInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this AiPolicyGroupInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The create_time of this AiPolicyGroupInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AiPolicyGroupInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this AiPolicyGroupInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AiPolicyGroupInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :return: The update_time of this AiPolicyGroupInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AiPolicyGroupInfo.

        **参数解释**： 创建时间 **取值范围**： 最小值0，最大值9223372036854775807 

        :param update_time: The update_time of this AiPolicyGroupInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def policy_list(self):
        r"""Gets the policy_list of this AiPolicyGroupInfo.

        **参数解释**: 策略列表 **取值范围**: 不涉及 

        :return: The policy_list of this AiPolicyGroupInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AiPolicyList`]
        """
        return self._policy_list

    @policy_list.setter
    def policy_list(self, policy_list):
        r"""Sets the policy_list of this AiPolicyGroupInfo.

        **参数解释**: 策略列表 **取值范围**: 不涉及 

        :param policy_list: The policy_list of this AiPolicyGroupInfo.
        :type policy_list: list[:class:`huaweicloudsdkhss.v5.AiPolicyList`]
        """
        self._policy_list = policy_list

    @property
    def agent_id_list(self):
        r"""Gets the agent_id_list of this AiPolicyGroupInfo.

        **参数解释**: 智能体列表 **取值范围**: 不涉及 

        :return: The agent_id_list of this AiPolicyGroupInfo.
        :rtype: list[str]
        """
        return self._agent_id_list

    @agent_id_list.setter
    def agent_id_list(self, agent_id_list):
        r"""Sets the agent_id_list of this AiPolicyGroupInfo.

        **参数解释**: 智能体列表 **取值范围**: 不涉及 

        :param agent_id_list: The agent_id_list of this AiPolicyGroupInfo.
        :type agent_id_list: list[str]
        """
        self._agent_id_list = agent_id_list

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
        if not isinstance(other, AiPolicyGroupInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
