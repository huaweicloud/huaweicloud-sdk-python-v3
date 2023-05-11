# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSkillListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'skill_name': 'str',
        'skill_form': 'str',
        'permission': 'str',
        'template_source': 'str',
        'status': 'int',
        'charge_model': 'int',
        'platform': 'str',
        'chip': 'str',
        'type': 'str',
        'charge_models': 'str',
        'device_types': 'str',
        'scenes': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'skill_name': 'skill_name',
        'skill_form': 'skill_form',
        'permission': 'permission',
        'template_source': 'template_source',
        'status': 'status',
        'charge_model': 'charge_model',
        'platform': 'platform',
        'chip': 'chip',
        'type': 'type',
        'charge_models': 'charge_models',
        'device_types': 'device_types',
        'scenes': 'scenes'
    }

    def __init__(self, limit=None, offset=None, skill_name=None, skill_form=None, permission=None, template_source=None, status=None, charge_model=None, platform=None, chip=None, type=None, charge_models=None, device_types=None, scenes=None):
        """ShowSkillListRequest

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量, 最大 100，默认值 10
        :type limit: int
        :param offset: 查询的起始位置, 默认值 0
        :type offset: int
        :param skill_name: 技能名称，支持模糊匹配。中英文、数字、下划线、中划线 长度[1-60]
        :type skill_name: str
        :param skill_form: 技能形式，no_termplate不支持Modelbox部署模板，support_template支持Modelbox模板。
        :type skill_form: str
        :param permission: 技能可见权限，支持公开可见public以及白名单whitelist
        :type permission: str
        :param template_source: 技能来源，分别hilens，ma_pro，studio
        :type template_source: str
        :param status: 技能审核状态状态，1表示审核通过，2表示审核不通过，0表示待审核
        :type status: int
        :param charge_model: 收费模式，0表示永久免费，1表示收费，2表示30天试用，3表示365天试用，4表示收费（永久使用）
        :type charge_model: int
        :param platform: 技能操作系统平台，其值为：Linux，Android， iOS， LiteOS，Windows
        :type platform: str
        :param chip: 技能芯片类型，其值为Ascend 310,Ascend 310(Atlas 200 DK)，Arm，x86，3516CV500,3519AV100,3519V101,3516DV300,3516EV200,3516EV300,3518EV300
        :type chip: str
        :param type: 技能类型，lite表示使用于海思芯片的轻量型技能。standard表示标准技能。
        :type type: str
        :param charge_models: 收费模式多选，0表示永久免费，1表示收费，2表示30天试用，3表示365天试用，4表示收费（永久使用），分隔符为|，例如输入为1|2|3
        :type charge_models: str
        :param device_types: 设备类型校验，允许输入多个设备类型，用|分隔，例如设备a|设备b。每种设备类型不允许#~^$%&amp;*&lt;&gt;{}[]&#39;|字符，长度1到100。最多50个设备类型
        :type device_types: str
        :param scenes: 技能适用场景，支持多选，分隔符|，例如场景a|场景b，每种场景不允许输入#~^$%&amp;*&lt;&gt;{}\\\\[\\\\]&#39;\\\\|等字符，长度100以内，最多20个设备类型。
        :type scenes: str
        """
        
        

        self._limit = None
        self._offset = None
        self._skill_name = None
        self._skill_form = None
        self._permission = None
        self._template_source = None
        self._status = None
        self._charge_model = None
        self._platform = None
        self._chip = None
        self._type = None
        self._charge_models = None
        self._device_types = None
        self._scenes = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if skill_name is not None:
            self.skill_name = skill_name
        if skill_form is not None:
            self.skill_form = skill_form
        if permission is not None:
            self.permission = permission
        if template_source is not None:
            self.template_source = template_source
        if status is not None:
            self.status = status
        if charge_model is not None:
            self.charge_model = charge_model
        if platform is not None:
            self.platform = platform
        if chip is not None:
            self.chip = chip
        if type is not None:
            self.type = type
        if charge_models is not None:
            self.charge_models = charge_models
        if device_types is not None:
            self.device_types = device_types
        if scenes is not None:
            self.scenes = scenes

    @property
    def limit(self):
        """Gets the limit of this ShowSkillListRequest.

        每页显示的条目数量, 最大 100，默认值 10

        :return: The limit of this ShowSkillListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowSkillListRequest.

        每页显示的条目数量, 最大 100，默认值 10

        :param limit: The limit of this ShowSkillListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowSkillListRequest.

        查询的起始位置, 默认值 0

        :return: The offset of this ShowSkillListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowSkillListRequest.

        查询的起始位置, 默认值 0

        :param offset: The offset of this ShowSkillListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def skill_name(self):
        """Gets the skill_name of this ShowSkillListRequest.

        技能名称，支持模糊匹配。中英文、数字、下划线、中划线 长度[1-60]

        :return: The skill_name of this ShowSkillListRequest.
        :rtype: str
        """
        return self._skill_name

    @skill_name.setter
    def skill_name(self, skill_name):
        """Sets the skill_name of this ShowSkillListRequest.

        技能名称，支持模糊匹配。中英文、数字、下划线、中划线 长度[1-60]

        :param skill_name: The skill_name of this ShowSkillListRequest.
        :type skill_name: str
        """
        self._skill_name = skill_name

    @property
    def skill_form(self):
        """Gets the skill_form of this ShowSkillListRequest.

        技能形式，no_termplate不支持Modelbox部署模板，support_template支持Modelbox模板。

        :return: The skill_form of this ShowSkillListRequest.
        :rtype: str
        """
        return self._skill_form

    @skill_form.setter
    def skill_form(self, skill_form):
        """Sets the skill_form of this ShowSkillListRequest.

        技能形式，no_termplate不支持Modelbox部署模板，support_template支持Modelbox模板。

        :param skill_form: The skill_form of this ShowSkillListRequest.
        :type skill_form: str
        """
        self._skill_form = skill_form

    @property
    def permission(self):
        """Gets the permission of this ShowSkillListRequest.

        技能可见权限，支持公开可见public以及白名单whitelist

        :return: The permission of this ShowSkillListRequest.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ShowSkillListRequest.

        技能可见权限，支持公开可见public以及白名单whitelist

        :param permission: The permission of this ShowSkillListRequest.
        :type permission: str
        """
        self._permission = permission

    @property
    def template_source(self):
        """Gets the template_source of this ShowSkillListRequest.

        技能来源，分别hilens，ma_pro，studio

        :return: The template_source of this ShowSkillListRequest.
        :rtype: str
        """
        return self._template_source

    @template_source.setter
    def template_source(self, template_source):
        """Sets the template_source of this ShowSkillListRequest.

        技能来源，分别hilens，ma_pro，studio

        :param template_source: The template_source of this ShowSkillListRequest.
        :type template_source: str
        """
        self._template_source = template_source

    @property
    def status(self):
        """Gets the status of this ShowSkillListRequest.

        技能审核状态状态，1表示审核通过，2表示审核不通过，0表示待审核

        :return: The status of this ShowSkillListRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowSkillListRequest.

        技能审核状态状态，1表示审核通过，2表示审核不通过，0表示待审核

        :param status: The status of this ShowSkillListRequest.
        :type status: int
        """
        self._status = status

    @property
    def charge_model(self):
        """Gets the charge_model of this ShowSkillListRequest.

        收费模式，0表示永久免费，1表示收费，2表示30天试用，3表示365天试用，4表示收费（永久使用）

        :return: The charge_model of this ShowSkillListRequest.
        :rtype: int
        """
        return self._charge_model

    @charge_model.setter
    def charge_model(self, charge_model):
        """Sets the charge_model of this ShowSkillListRequest.

        收费模式，0表示永久免费，1表示收费，2表示30天试用，3表示365天试用，4表示收费（永久使用）

        :param charge_model: The charge_model of this ShowSkillListRequest.
        :type charge_model: int
        """
        self._charge_model = charge_model

    @property
    def platform(self):
        """Gets the platform of this ShowSkillListRequest.

        技能操作系统平台，其值为：Linux，Android， iOS， LiteOS，Windows

        :return: The platform of this ShowSkillListRequest.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ShowSkillListRequest.

        技能操作系统平台，其值为：Linux，Android， iOS， LiteOS，Windows

        :param platform: The platform of this ShowSkillListRequest.
        :type platform: str
        """
        self._platform = platform

    @property
    def chip(self):
        """Gets the chip of this ShowSkillListRequest.

        技能芯片类型，其值为Ascend 310,Ascend 310(Atlas 200 DK)，Arm，x86，3516CV500,3519AV100,3519V101,3516DV300,3516EV200,3516EV300,3518EV300

        :return: The chip of this ShowSkillListRequest.
        :rtype: str
        """
        return self._chip

    @chip.setter
    def chip(self, chip):
        """Sets the chip of this ShowSkillListRequest.

        技能芯片类型，其值为Ascend 310,Ascend 310(Atlas 200 DK)，Arm，x86，3516CV500,3519AV100,3519V101,3516DV300,3516EV200,3516EV300,3518EV300

        :param chip: The chip of this ShowSkillListRequest.
        :type chip: str
        """
        self._chip = chip

    @property
    def type(self):
        """Gets the type of this ShowSkillListRequest.

        技能类型，lite表示使用于海思芯片的轻量型技能。standard表示标准技能。

        :return: The type of this ShowSkillListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowSkillListRequest.

        技能类型，lite表示使用于海思芯片的轻量型技能。standard表示标准技能。

        :param type: The type of this ShowSkillListRequest.
        :type type: str
        """
        self._type = type

    @property
    def charge_models(self):
        """Gets the charge_models of this ShowSkillListRequest.

        收费模式多选，0表示永久免费，1表示收费，2表示30天试用，3表示365天试用，4表示收费（永久使用），分隔符为|，例如输入为1|2|3

        :return: The charge_models of this ShowSkillListRequest.
        :rtype: str
        """
        return self._charge_models

    @charge_models.setter
    def charge_models(self, charge_models):
        """Sets the charge_models of this ShowSkillListRequest.

        收费模式多选，0表示永久免费，1表示收费，2表示30天试用，3表示365天试用，4表示收费（永久使用），分隔符为|，例如输入为1|2|3

        :param charge_models: The charge_models of this ShowSkillListRequest.
        :type charge_models: str
        """
        self._charge_models = charge_models

    @property
    def device_types(self):
        """Gets the device_types of this ShowSkillListRequest.

        设备类型校验，允许输入多个设备类型，用|分隔，例如设备a|设备b。每种设备类型不允许#~^$%&*<>{}[]'|字符，长度1到100。最多50个设备类型

        :return: The device_types of this ShowSkillListRequest.
        :rtype: str
        """
        return self._device_types

    @device_types.setter
    def device_types(self, device_types):
        """Sets the device_types of this ShowSkillListRequest.

        设备类型校验，允许输入多个设备类型，用|分隔，例如设备a|设备b。每种设备类型不允许#~^$%&*<>{}[]'|字符，长度1到100。最多50个设备类型

        :param device_types: The device_types of this ShowSkillListRequest.
        :type device_types: str
        """
        self._device_types = device_types

    @property
    def scenes(self):
        """Gets the scenes of this ShowSkillListRequest.

        技能适用场景，支持多选，分隔符|，例如场景a|场景b，每种场景不允许输入#~^$%&*<>{}\\\\[\\\\]'\\\\|等字符，长度100以内，最多20个设备类型。

        :return: The scenes of this ShowSkillListRequest.
        :rtype: str
        """
        return self._scenes

    @scenes.setter
    def scenes(self, scenes):
        """Sets the scenes of this ShowSkillListRequest.

        技能适用场景，支持多选，分隔符|，例如场景a|场景b，每种场景不允许输入#~^$%&*<>{}\\\\[\\\\]'\\\\|等字符，长度100以内，最多20个设备类型。

        :param scenes: The scenes of this ShowSkillListRequest.
        :type scenes: str
        """
        self._scenes = scenes

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
        if not isinstance(other, ShowSkillListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
