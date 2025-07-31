# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyTemplateInfo:

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
        r"""PolicyTemplateInfo

        The model defined in huaweicloud sdk

        :param id: 模板ID
        :type id: str
        :param template_name: 模板名称
        :type template_name: str
        :param template_type: 模板类型
        :type template_type: str
        :param description: 描述
        :type description: str
        :param target_kind: 策略模板应用资源类型，多个资源类型通过分号份隔连接
        :type target_kind: str
        :param tag: 标签
        :type tag: str
        :param level: 推荐级别
        :type level: str
        :param constraint_template: 策略模板内容
        :type constraint_template: str
        """
        
        

        self._id = None
        self._template_name = None
        self._template_type = None
        self._description = None
        self._target_kind = None
        self._tag = None
        self._level = None
        self._constraint_template = None
        self.discriminator = None

        self.id = id
        self.template_name = template_name
        self.template_type = template_type
        if description is not None:
            self.description = description
        self.target_kind = target_kind
        if tag is not None:
            self.tag = tag
        if level is not None:
            self.level = level
        self.constraint_template = constraint_template

    @property
    def id(self):
        r"""Gets the id of this PolicyTemplateInfo.

        模板ID

        :return: The id of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PolicyTemplateInfo.

        模板ID

        :param id: The id of this PolicyTemplateInfo.
        :type id: str
        """
        self._id = id

    @property
    def template_name(self):
        r"""Gets the template_name of this PolicyTemplateInfo.

        模板名称

        :return: The template_name of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this PolicyTemplateInfo.

        模板名称

        :param template_name: The template_name of this PolicyTemplateInfo.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_type(self):
        r"""Gets the template_type of this PolicyTemplateInfo.

        模板类型

        :return: The template_type of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this PolicyTemplateInfo.

        模板类型

        :param template_type: The template_type of this PolicyTemplateInfo.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def description(self):
        r"""Gets the description of this PolicyTemplateInfo.

        描述

        :return: The description of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PolicyTemplateInfo.

        描述

        :param description: The description of this PolicyTemplateInfo.
        :type description: str
        """
        self._description = description

    @property
    def target_kind(self):
        r"""Gets the target_kind of this PolicyTemplateInfo.

        策略模板应用资源类型，多个资源类型通过分号份隔连接

        :return: The target_kind of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._target_kind

    @target_kind.setter
    def target_kind(self, target_kind):
        r"""Sets the target_kind of this PolicyTemplateInfo.

        策略模板应用资源类型，多个资源类型通过分号份隔连接

        :param target_kind: The target_kind of this PolicyTemplateInfo.
        :type target_kind: str
        """
        self._target_kind = target_kind

    @property
    def tag(self):
        r"""Gets the tag of this PolicyTemplateInfo.

        标签

        :return: The tag of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this PolicyTemplateInfo.

        标签

        :param tag: The tag of this PolicyTemplateInfo.
        :type tag: str
        """
        self._tag = tag

    @property
    def level(self):
        r"""Gets the level of this PolicyTemplateInfo.

        推荐级别

        :return: The level of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this PolicyTemplateInfo.

        推荐级别

        :param level: The level of this PolicyTemplateInfo.
        :type level: str
        """
        self._level = level

    @property
    def constraint_template(self):
        r"""Gets the constraint_template of this PolicyTemplateInfo.

        策略模板内容

        :return: The constraint_template of this PolicyTemplateInfo.
        :rtype: str
        """
        return self._constraint_template

    @constraint_template.setter
    def constraint_template(self, constraint_template):
        r"""Sets the constraint_template of this PolicyTemplateInfo.

        策略模板内容

        :param constraint_template: The constraint_template of this PolicyTemplateInfo.
        :type constraint_template: str
        """
        self._constraint_template = constraint_template

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
        if not isinstance(other, PolicyTemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
