# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RulesetItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'language': 'str',
        'template_name': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'template_create_time': 'str',
        'is_used': 'str',
        'rule_ids': 'str',
        'is_default': 'str',
        'is_devcloud_project_default': 'str',
        'is_default_template': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'language': 'language',
        'template_name': 'template_name',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'template_create_time': 'template_create_time',
        'is_used': 'is_used',
        'rule_ids': 'rule_ids',
        'is_default': 'is_default',
        'is_devcloud_project_default': 'is_devcloud_project_default',
        'is_default_template': 'is_default_template'
    }

    def __init__(self, template_id=None, language=None, template_name=None, creator_id=None, creator_name=None, template_create_time=None, is_used=None, rule_ids=None, is_default=None, is_devcloud_project_default=None, is_default_template=None):
        """RulesetItem

        The model defined in huaweicloud sdk

        :param template_id: 规则集id
        :type template_id: str
        :param language: 规则集语言
        :type language: str
        :param template_name: 规则集名称
        :type template_name: str
        :param creator_id: 创建人ID
        :type creator_id: str
        :param creator_name: 创建人名称
        :type creator_name: str
        :param template_create_time: 创建人时间
        :type template_create_time: str
        :param is_used: 使用状态1使用中，0空闲中
        :type is_used: str
        :param rule_ids: 规则集包含的规则id
        :type rule_ids: str
        :param is_default: 是否该语言默认规则集，0不是，1是
        :type is_default: str
        :param is_devcloud_project_default: 是否是项目下语言默认规则集，0不是，1是
        :type is_devcloud_project_default: str
        :param is_default_template: 是否是系统规则集，0不是，1是
        :type is_default_template: str
        """
        
        

        self._template_id = None
        self._language = None
        self._template_name = None
        self._creator_id = None
        self._creator_name = None
        self._template_create_time = None
        self._is_used = None
        self._rule_ids = None
        self._is_default = None
        self._is_devcloud_project_default = None
        self._is_default_template = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if language is not None:
            self.language = language
        if template_name is not None:
            self.template_name = template_name
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if template_create_time is not None:
            self.template_create_time = template_create_time
        if is_used is not None:
            self.is_used = is_used
        if rule_ids is not None:
            self.rule_ids = rule_ids
        if is_default is not None:
            self.is_default = is_default
        if is_devcloud_project_default is not None:
            self.is_devcloud_project_default = is_devcloud_project_default
        if is_default_template is not None:
            self.is_default_template = is_default_template

    @property
    def template_id(self):
        """Gets the template_id of this RulesetItem.

        规则集id

        :return: The template_id of this RulesetItem.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this RulesetItem.

        规则集id

        :param template_id: The template_id of this RulesetItem.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def language(self):
        """Gets the language of this RulesetItem.

        规则集语言

        :return: The language of this RulesetItem.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RulesetItem.

        规则集语言

        :param language: The language of this RulesetItem.
        :type language: str
        """
        self._language = language

    @property
    def template_name(self):
        """Gets the template_name of this RulesetItem.

        规则集名称

        :return: The template_name of this RulesetItem.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this RulesetItem.

        规则集名称

        :param template_name: The template_name of this RulesetItem.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def creator_id(self):
        """Gets the creator_id of this RulesetItem.

        创建人ID

        :return: The creator_id of this RulesetItem.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this RulesetItem.

        创建人ID

        :param creator_id: The creator_id of this RulesetItem.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        """Gets the creator_name of this RulesetItem.

        创建人名称

        :return: The creator_name of this RulesetItem.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        """Sets the creator_name of this RulesetItem.

        创建人名称

        :param creator_name: The creator_name of this RulesetItem.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def template_create_time(self):
        """Gets the template_create_time of this RulesetItem.

        创建人时间

        :return: The template_create_time of this RulesetItem.
        :rtype: str
        """
        return self._template_create_time

    @template_create_time.setter
    def template_create_time(self, template_create_time):
        """Sets the template_create_time of this RulesetItem.

        创建人时间

        :param template_create_time: The template_create_time of this RulesetItem.
        :type template_create_time: str
        """
        self._template_create_time = template_create_time

    @property
    def is_used(self):
        """Gets the is_used of this RulesetItem.

        使用状态1使用中，0空闲中

        :return: The is_used of this RulesetItem.
        :rtype: str
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        """Sets the is_used of this RulesetItem.

        使用状态1使用中，0空闲中

        :param is_used: The is_used of this RulesetItem.
        :type is_used: str
        """
        self._is_used = is_used

    @property
    def rule_ids(self):
        """Gets the rule_ids of this RulesetItem.

        规则集包含的规则id

        :return: The rule_ids of this RulesetItem.
        :rtype: str
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this RulesetItem.

        规则集包含的规则id

        :param rule_ids: The rule_ids of this RulesetItem.
        :type rule_ids: str
        """
        self._rule_ids = rule_ids

    @property
    def is_default(self):
        """Gets the is_default of this RulesetItem.

        是否该语言默认规则集，0不是，1是

        :return: The is_default of this RulesetItem.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this RulesetItem.

        是否该语言默认规则集，0不是，1是

        :param is_default: The is_default of this RulesetItem.
        :type is_default: str
        """
        self._is_default = is_default

    @property
    def is_devcloud_project_default(self):
        """Gets the is_devcloud_project_default of this RulesetItem.

        是否是项目下语言默认规则集，0不是，1是

        :return: The is_devcloud_project_default of this RulesetItem.
        :rtype: str
        """
        return self._is_devcloud_project_default

    @is_devcloud_project_default.setter
    def is_devcloud_project_default(self, is_devcloud_project_default):
        """Sets the is_devcloud_project_default of this RulesetItem.

        是否是项目下语言默认规则集，0不是，1是

        :param is_devcloud_project_default: The is_devcloud_project_default of this RulesetItem.
        :type is_devcloud_project_default: str
        """
        self._is_devcloud_project_default = is_devcloud_project_default

    @property
    def is_default_template(self):
        """Gets the is_default_template of this RulesetItem.

        是否是系统规则集，0不是，1是

        :return: The is_default_template of this RulesetItem.
        :rtype: str
        """
        return self._is_default_template

    @is_default_template.setter
    def is_default_template(self, is_default_template):
        """Sets the is_default_template of this RulesetItem.

        是否是系统规则集，0不是，1是

        :param is_default_template: The is_default_template of this RulesetItem.
        :type is_default_template: str
        """
        self._is_default_template = is_default_template

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
        if not isinstance(other, RulesetItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
