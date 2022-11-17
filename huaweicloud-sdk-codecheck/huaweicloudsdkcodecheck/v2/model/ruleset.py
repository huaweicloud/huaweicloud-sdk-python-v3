# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Ruleset:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'template_name': 'str',
        'language': 'str',
        'is_default': 'str',
        'rule_ids': 'str',
        'uncheck_ids': 'str',
        'template_id': 'str',
        'custom_attributes': 'list[CustomAttributes]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'template_name': 'template_name',
        'language': 'language',
        'is_default': 'is_default',
        'rule_ids': 'rule_ids',
        'uncheck_ids': 'uncheck_ids',
        'template_id': 'template_id',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, project_id=None, template_name=None, language=None, is_default=None, rule_ids=None, uncheck_ids=None, template_id=None, custom_attributes=None):
        """Ruleset

        The model defined in huaweicloud sdk

        :param project_id: 项目ID
        :type project_id: str
        :param template_name: 新规则集名称
        :type template_name: str
        :param language: 规则集语言
        :type language: str
        :param is_default: 如果有基于的规则集则是1，没有基于的规则集则是0
        :type is_default: str
        :param rule_ids: 新启用规则ids
        :type rule_ids: str
        :param uncheck_ids: 新关闭规则id
        :type uncheck_ids: str
        :param template_id: 规则集ID
        :type template_id: str
        :param custom_attributes: 自定义规则参数项，支持修改规则阈值
        :type custom_attributes: list[:class:`huaweicloudsdkcodecheck.v2.CustomAttributes`]
        """
        
        

        self._project_id = None
        self._template_name = None
        self._language = None
        self._is_default = None
        self._rule_ids = None
        self._uncheck_ids = None
        self._template_id = None
        self._custom_attributes = None
        self.discriminator = None

        self.project_id = project_id
        self.template_name = template_name
        self.language = language
        self.is_default = is_default
        self.rule_ids = rule_ids
        if uncheck_ids is not None:
            self.uncheck_ids = uncheck_ids
        if template_id is not None:
            self.template_id = template_id
        if custom_attributes is not None:
            self.custom_attributes = custom_attributes

    @property
    def project_id(self):
        """Gets the project_id of this Ruleset.

        项目ID

        :return: The project_id of this Ruleset.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Ruleset.

        项目ID

        :param project_id: The project_id of this Ruleset.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def template_name(self):
        """Gets the template_name of this Ruleset.

        新规则集名称

        :return: The template_name of this Ruleset.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this Ruleset.

        新规则集名称

        :param template_name: The template_name of this Ruleset.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def language(self):
        """Gets the language of this Ruleset.

        规则集语言

        :return: The language of this Ruleset.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Ruleset.

        规则集语言

        :param language: The language of this Ruleset.
        :type language: str
        """
        self._language = language

    @property
    def is_default(self):
        """Gets the is_default of this Ruleset.

        如果有基于的规则集则是1，没有基于的规则集则是0

        :return: The is_default of this Ruleset.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this Ruleset.

        如果有基于的规则集则是1，没有基于的规则集则是0

        :param is_default: The is_default of this Ruleset.
        :type is_default: str
        """
        self._is_default = is_default

    @property
    def rule_ids(self):
        """Gets the rule_ids of this Ruleset.

        新启用规则ids

        :return: The rule_ids of this Ruleset.
        :rtype: str
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this Ruleset.

        新启用规则ids

        :param rule_ids: The rule_ids of this Ruleset.
        :type rule_ids: str
        """
        self._rule_ids = rule_ids

    @property
    def uncheck_ids(self):
        """Gets the uncheck_ids of this Ruleset.

        新关闭规则id

        :return: The uncheck_ids of this Ruleset.
        :rtype: str
        """
        return self._uncheck_ids

    @uncheck_ids.setter
    def uncheck_ids(self, uncheck_ids):
        """Sets the uncheck_ids of this Ruleset.

        新关闭规则id

        :param uncheck_ids: The uncheck_ids of this Ruleset.
        :type uncheck_ids: str
        """
        self._uncheck_ids = uncheck_ids

    @property
    def template_id(self):
        """Gets the template_id of this Ruleset.

        规则集ID

        :return: The template_id of this Ruleset.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this Ruleset.

        规则集ID

        :param template_id: The template_id of this Ruleset.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def custom_attributes(self):
        """Gets the custom_attributes of this Ruleset.

        自定义规则参数项，支持修改规则阈值

        :return: The custom_attributes of this Ruleset.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.CustomAttributes`]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """Sets the custom_attributes of this Ruleset.

        自定义规则参数项，支持修改规则阈值

        :param custom_attributes: The custom_attributes of this Ruleset.
        :type custom_attributes: list[:class:`huaweicloudsdkcodecheck.v2.CustomAttributes`]
        """
        self._custom_attributes = custom_attributes

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
        if not isinstance(other, Ruleset):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
