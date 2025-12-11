# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterProtectPolicyTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'template_name': 'str',
        'template_type': 'str',
        'description': 'str',
        'target_kind': 'str',
        'tag': 'str',
        'level': 'str',
        'constraint_template': 'str'
    }

    attribute_map = {
        'id': 'id',
        'template_name': 'template_name',
        'template_type': 'template_type',
        'description': 'description',
        'target_kind': 'target_kind',
        'tag': 'tag',
        'level': 'level',
        'constraint_template': 'constraint_template'
    }

    def __init__(self, id=None, template_name=None, template_type=None, description=None, target_kind=None, tag=None, level=None, constraint_template=None):
        r"""ShowClusterProtectPolicyTemplateResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**: 模板ID **取值范围**: 字符长度0-128 
        :type id: str
        :param template_name: **参数解释**: 模板名称 **取值范围**: 字符长度1-255 
        :type template_name: str
        :param template_type: **参数解释**: 模板类型 **取值范围**: 字符长度1-16 
        :type template_type: str
        :param description: **参数解释**: 描述 **取值范围**: 字符长度0-2048 
        :type description: str
        :param target_kind: **参数解释**: 策略模板应用资源类型，多个资源类型通过分号分隔连接 **取值范围**: 字符长度1-255 
        :type target_kind: str
        :param tag: **参数解释**: 标签 **取值范围**: 字符长度0-2048 
        :type tag: str
        :param level: **参数解释**: 推荐级别 **取值范围**: 字符长度1-5 
        :type level: str
        :param constraint_template: **参数解释**: 策略模板内容 **取值范围**: 字符长度1-65535 
        :type constraint_template: str
        """
        
        super().__init__()

        self._id = None
        self._template_name = None
        self._template_type = None
        self._description = None
        self._target_kind = None
        self._tag = None
        self._level = None
        self._constraint_template = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if template_name is not None:
            self.template_name = template_name
        if template_type is not None:
            self.template_type = template_type
        if description is not None:
            self.description = description
        if target_kind is not None:
            self.target_kind = target_kind
        if tag is not None:
            self.tag = tag
        if level is not None:
            self.level = level
        if constraint_template is not None:
            self.constraint_template = constraint_template

    @property
    def id(self):
        r"""Gets the id of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 模板ID **取值范围**: 字符长度0-128 

        :return: The id of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 模板ID **取值范围**: 字符长度0-128 

        :param id: The id of this ShowClusterProtectPolicyTemplateResponse.
        :type id: str
        """
        self._id = id

    @property
    def template_name(self):
        r"""Gets the template_name of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 模板名称 **取值范围**: 字符长度1-255 

        :return: The template_name of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 模板名称 **取值范围**: 字符长度1-255 

        :param template_name: The template_name of this ShowClusterProtectPolicyTemplateResponse.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 模板类型 **取值范围**: 字符长度1-16 

        :return: The template_type of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 模板类型 **取值范围**: 字符长度1-16 

        :param template_type: The template_type of this ShowClusterProtectPolicyTemplateResponse.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def description(self):
        r"""Gets the description of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 描述 **取值范围**: 字符长度0-2048 

        :return: The description of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 描述 **取值范围**: 字符长度0-2048 

        :param description: The description of this ShowClusterProtectPolicyTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def target_kind(self):
        r"""Gets the target_kind of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 策略模板应用资源类型，多个资源类型通过分号分隔连接 **取值范围**: 字符长度1-255 

        :return: The target_kind of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._target_kind

    @target_kind.setter
    def target_kind(self, target_kind):
        r"""Sets the target_kind of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 策略模板应用资源类型，多个资源类型通过分号分隔连接 **取值范围**: 字符长度1-255 

        :param target_kind: The target_kind of this ShowClusterProtectPolicyTemplateResponse.
        :type target_kind: str
        """
        self._target_kind = target_kind

    @property
    def tag(self):
        r"""Gets the tag of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 标签 **取值范围**: 字符长度0-2048 

        :return: The tag of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 标签 **取值范围**: 字符长度0-2048 

        :param tag: The tag of this ShowClusterProtectPolicyTemplateResponse.
        :type tag: str
        """
        self._tag = tag

    @property
    def level(self):
        r"""Gets the level of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 推荐级别 **取值范围**: 字符长度1-5 

        :return: The level of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 推荐级别 **取值范围**: 字符长度1-5 

        :param level: The level of this ShowClusterProtectPolicyTemplateResponse.
        :type level: str
        """
        self._level = level

    @property
    def constraint_template(self):
        r"""Gets the constraint_template of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 策略模板内容 **取值范围**: 字符长度1-65535 

        :return: The constraint_template of this ShowClusterProtectPolicyTemplateResponse.
        :rtype: str
        """
        return self._constraint_template

    @constraint_template.setter
    def constraint_template(self, constraint_template):
        r"""Sets the constraint_template of this ShowClusterProtectPolicyTemplateResponse.

        **参数解释**: 策略模板内容 **取值范围**: 字符长度1-65535 

        :param constraint_template: The constraint_template of this ShowClusterProtectPolicyTemplateResponse.
        :type constraint_template: str
        """
        self._constraint_template = constraint_template

    def to_dict(self):
        import warnings
        warnings.warn("ShowClusterProtectPolicyTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowClusterProtectPolicyTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
