# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPatchBaselineResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'baseline_id': 'str',
        'name': 'str',
        'description': 'str',
        'region': 'str',
        'baseline_scene': 'str',
        'rule_type': 'str',
        'operating_system': 'str',
        'type': 'str',
        'approval_rules': 'list[PatchRule]',
        'custom_baseline_rules': 'list[CustomBaselineRule]',
        'default_patch_baseline': 'bool',
        'rejected_patches': 'str',
        'rejected_action': 'str',
        'approved_patches': 'str',
        'approved_compliance': 'str',
        'enable_security_approved': 'bool',
        'created_time': 'int',
        'modified_time': 'int'
    }

    attribute_map = {
        'baseline_id': 'baseline_id',
        'name': 'name',
        'description': 'description',
        'region': 'region',
        'baseline_scene': 'baseline_scene',
        'rule_type': 'rule_type',
        'operating_system': 'operating_system',
        'type': 'type',
        'approval_rules': 'approval_rules',
        'custom_baseline_rules': 'custom_baseline_rules',
        'default_patch_baseline': 'default_patch_baseline',
        'rejected_patches': 'rejected_patches',
        'rejected_action': 'rejected_action',
        'approved_patches': 'approved_patches',
        'approved_compliance': 'approved_compliance',
        'enable_security_approved': 'enable_security_approved',
        'created_time': 'created_time',
        'modified_time': 'modified_time'
    }

    def __init__(self, baseline_id=None, name=None, description=None, region=None, baseline_scene=None, rule_type=None, operating_system=None, type=None, approval_rules=None, custom_baseline_rules=None, default_patch_baseline=None, rejected_patches=None, rejected_action=None, approved_patches=None, approved_compliance=None, enable_security_approved=None, created_time=None, modified_time=None):
        r"""ShowPatchBaselineResponse

        The model defined in huaweicloud sdk

        :param baseline_id: 补丁基准ID
        :type baseline_id: str
        :param name: 补丁基准名称
        :type name: str
        :param description: 补丁基准描述
        :type description: str
        :param region: 区域
        :type region: str
        :param baseline_scene: 基线使用场景(CCE、ECS、BMS)
        :type baseline_scene: str
        :param rule_type: 基线规则类型(Standard,Custom)
        :type rule_type: str
        :param operating_system: 操作系统
        :type operating_system: str
        :param type: 补丁基准类型（公共/自定义）
        :type type: str
        :param approval_rules: 操作系统的批准规则
        :type approval_rules: list[:class:`huaweicloudsdkcoc.v1.PatchRule`]
        :param custom_baseline_rules: 自定义基线列表
        :type custom_baseline_rules: list[:class:`huaweicloudsdkcoc.v1.CustomBaselineRule`]
        :param default_patch_baseline: 是否默认基准
        :type default_patch_baseline: bool
        :param rejected_patches: 拒绝的补丁
        :type rejected_patches: str
        :param rejected_action: 拒绝策略
        :type rejected_action: str
        :param approved_patches: 批准的补丁
        :type approved_patches: str
        :param approved_compliance: 批准的补丁合规性级别
        :type approved_compliance: str
        :param enable_security_approved: 批准的补丁是否安全更新
        :type enable_security_approved: bool
        :param created_time: 创建时间
        :type created_time: int
        :param modified_time: modifiedTime
        :type modified_time: int
        """
        
        super(ShowPatchBaselineResponse, self).__init__()

        self._baseline_id = None
        self._name = None
        self._description = None
        self._region = None
        self._baseline_scene = None
        self._rule_type = None
        self._operating_system = None
        self._type = None
        self._approval_rules = None
        self._custom_baseline_rules = None
        self._default_patch_baseline = None
        self._rejected_patches = None
        self._rejected_action = None
        self._approved_patches = None
        self._approved_compliance = None
        self._enable_security_approved = None
        self._created_time = None
        self._modified_time = None
        self.discriminator = None

        if baseline_id is not None:
            self.baseline_id = baseline_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if region is not None:
            self.region = region
        if baseline_scene is not None:
            self.baseline_scene = baseline_scene
        if rule_type is not None:
            self.rule_type = rule_type
        if operating_system is not None:
            self.operating_system = operating_system
        if type is not None:
            self.type = type
        if approval_rules is not None:
            self.approval_rules = approval_rules
        if custom_baseline_rules is not None:
            self.custom_baseline_rules = custom_baseline_rules
        if default_patch_baseline is not None:
            self.default_patch_baseline = default_patch_baseline
        if rejected_patches is not None:
            self.rejected_patches = rejected_patches
        if rejected_action is not None:
            self.rejected_action = rejected_action
        if approved_patches is not None:
            self.approved_patches = approved_patches
        if approved_compliance is not None:
            self.approved_compliance = approved_compliance
        if enable_security_approved is not None:
            self.enable_security_approved = enable_security_approved
        if created_time is not None:
            self.created_time = created_time
        if modified_time is not None:
            self.modified_time = modified_time

    @property
    def baseline_id(self):
        r"""Gets the baseline_id of this ShowPatchBaselineResponse.

        补丁基准ID

        :return: The baseline_id of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._baseline_id

    @baseline_id.setter
    def baseline_id(self, baseline_id):
        r"""Sets the baseline_id of this ShowPatchBaselineResponse.

        补丁基准ID

        :param baseline_id: The baseline_id of this ShowPatchBaselineResponse.
        :type baseline_id: str
        """
        self._baseline_id = baseline_id

    @property
    def name(self):
        r"""Gets the name of this ShowPatchBaselineResponse.

        补丁基准名称

        :return: The name of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowPatchBaselineResponse.

        补丁基准名称

        :param name: The name of this ShowPatchBaselineResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowPatchBaselineResponse.

        补丁基准描述

        :return: The description of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowPatchBaselineResponse.

        补丁基准描述

        :param description: The description of this ShowPatchBaselineResponse.
        :type description: str
        """
        self._description = description

    @property
    def region(self):
        r"""Gets the region of this ShowPatchBaselineResponse.

        区域

        :return: The region of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ShowPatchBaselineResponse.

        区域

        :param region: The region of this ShowPatchBaselineResponse.
        :type region: str
        """
        self._region = region

    @property
    def baseline_scene(self):
        r"""Gets the baseline_scene of this ShowPatchBaselineResponse.

        基线使用场景(CCE、ECS、BMS)

        :return: The baseline_scene of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._baseline_scene

    @baseline_scene.setter
    def baseline_scene(self, baseline_scene):
        r"""Sets the baseline_scene of this ShowPatchBaselineResponse.

        基线使用场景(CCE、ECS、BMS)

        :param baseline_scene: The baseline_scene of this ShowPatchBaselineResponse.
        :type baseline_scene: str
        """
        self._baseline_scene = baseline_scene

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ShowPatchBaselineResponse.

        基线规则类型(Standard,Custom)

        :return: The rule_type of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ShowPatchBaselineResponse.

        基线规则类型(Standard,Custom)

        :param rule_type: The rule_type of this ShowPatchBaselineResponse.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def operating_system(self):
        r"""Gets the operating_system of this ShowPatchBaselineResponse.

        操作系统

        :return: The operating_system of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        r"""Sets the operating_system of this ShowPatchBaselineResponse.

        操作系统

        :param operating_system: The operating_system of this ShowPatchBaselineResponse.
        :type operating_system: str
        """
        self._operating_system = operating_system

    @property
    def type(self):
        r"""Gets the type of this ShowPatchBaselineResponse.

        补丁基准类型（公共/自定义）

        :return: The type of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ShowPatchBaselineResponse.

        补丁基准类型（公共/自定义）

        :param type: The type of this ShowPatchBaselineResponse.
        :type type: str
        """
        self._type = type

    @property
    def approval_rules(self):
        r"""Gets the approval_rules of this ShowPatchBaselineResponse.

        操作系统的批准规则

        :return: The approval_rules of this ShowPatchBaselineResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.PatchRule`]
        """
        return self._approval_rules

    @approval_rules.setter
    def approval_rules(self, approval_rules):
        r"""Sets the approval_rules of this ShowPatchBaselineResponse.

        操作系统的批准规则

        :param approval_rules: The approval_rules of this ShowPatchBaselineResponse.
        :type approval_rules: list[:class:`huaweicloudsdkcoc.v1.PatchRule`]
        """
        self._approval_rules = approval_rules

    @property
    def custom_baseline_rules(self):
        r"""Gets the custom_baseline_rules of this ShowPatchBaselineResponse.

        自定义基线列表

        :return: The custom_baseline_rules of this ShowPatchBaselineResponse.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CustomBaselineRule`]
        """
        return self._custom_baseline_rules

    @custom_baseline_rules.setter
    def custom_baseline_rules(self, custom_baseline_rules):
        r"""Sets the custom_baseline_rules of this ShowPatchBaselineResponse.

        自定义基线列表

        :param custom_baseline_rules: The custom_baseline_rules of this ShowPatchBaselineResponse.
        :type custom_baseline_rules: list[:class:`huaweicloudsdkcoc.v1.CustomBaselineRule`]
        """
        self._custom_baseline_rules = custom_baseline_rules

    @property
    def default_patch_baseline(self):
        r"""Gets the default_patch_baseline of this ShowPatchBaselineResponse.

        是否默认基准

        :return: The default_patch_baseline of this ShowPatchBaselineResponse.
        :rtype: bool
        """
        return self._default_patch_baseline

    @default_patch_baseline.setter
    def default_patch_baseline(self, default_patch_baseline):
        r"""Sets the default_patch_baseline of this ShowPatchBaselineResponse.

        是否默认基准

        :param default_patch_baseline: The default_patch_baseline of this ShowPatchBaselineResponse.
        :type default_patch_baseline: bool
        """
        self._default_patch_baseline = default_patch_baseline

    @property
    def rejected_patches(self):
        r"""Gets the rejected_patches of this ShowPatchBaselineResponse.

        拒绝的补丁

        :return: The rejected_patches of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._rejected_patches

    @rejected_patches.setter
    def rejected_patches(self, rejected_patches):
        r"""Sets the rejected_patches of this ShowPatchBaselineResponse.

        拒绝的补丁

        :param rejected_patches: The rejected_patches of this ShowPatchBaselineResponse.
        :type rejected_patches: str
        """
        self._rejected_patches = rejected_patches

    @property
    def rejected_action(self):
        r"""Gets the rejected_action of this ShowPatchBaselineResponse.

        拒绝策略

        :return: The rejected_action of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._rejected_action

    @rejected_action.setter
    def rejected_action(self, rejected_action):
        r"""Sets the rejected_action of this ShowPatchBaselineResponse.

        拒绝策略

        :param rejected_action: The rejected_action of this ShowPatchBaselineResponse.
        :type rejected_action: str
        """
        self._rejected_action = rejected_action

    @property
    def approved_patches(self):
        r"""Gets the approved_patches of this ShowPatchBaselineResponse.

        批准的补丁

        :return: The approved_patches of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._approved_patches

    @approved_patches.setter
    def approved_patches(self, approved_patches):
        r"""Sets the approved_patches of this ShowPatchBaselineResponse.

        批准的补丁

        :param approved_patches: The approved_patches of this ShowPatchBaselineResponse.
        :type approved_patches: str
        """
        self._approved_patches = approved_patches

    @property
    def approved_compliance(self):
        r"""Gets the approved_compliance of this ShowPatchBaselineResponse.

        批准的补丁合规性级别

        :return: The approved_compliance of this ShowPatchBaselineResponse.
        :rtype: str
        """
        return self._approved_compliance

    @approved_compliance.setter
    def approved_compliance(self, approved_compliance):
        r"""Sets the approved_compliance of this ShowPatchBaselineResponse.

        批准的补丁合规性级别

        :param approved_compliance: The approved_compliance of this ShowPatchBaselineResponse.
        :type approved_compliance: str
        """
        self._approved_compliance = approved_compliance

    @property
    def enable_security_approved(self):
        r"""Gets the enable_security_approved of this ShowPatchBaselineResponse.

        批准的补丁是否安全更新

        :return: The enable_security_approved of this ShowPatchBaselineResponse.
        :rtype: bool
        """
        return self._enable_security_approved

    @enable_security_approved.setter
    def enable_security_approved(self, enable_security_approved):
        r"""Sets the enable_security_approved of this ShowPatchBaselineResponse.

        批准的补丁是否安全更新

        :param enable_security_approved: The enable_security_approved of this ShowPatchBaselineResponse.
        :type enable_security_approved: bool
        """
        self._enable_security_approved = enable_security_approved

    @property
    def created_time(self):
        r"""Gets the created_time of this ShowPatchBaselineResponse.

        创建时间

        :return: The created_time of this ShowPatchBaselineResponse.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ShowPatchBaselineResponse.

        创建时间

        :param created_time: The created_time of this ShowPatchBaselineResponse.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def modified_time(self):
        r"""Gets the modified_time of this ShowPatchBaselineResponse.

        modifiedTime

        :return: The modified_time of this ShowPatchBaselineResponse.
        :rtype: int
        """
        return self._modified_time

    @modified_time.setter
    def modified_time(self, modified_time):
        r"""Sets the modified_time of this ShowPatchBaselineResponse.

        modifiedTime

        :param modified_time: The modified_time of this ShowPatchBaselineResponse.
        :type modified_time: int
        """
        self._modified_time = modified_time

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
        if not isinstance(other, ShowPatchBaselineResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
