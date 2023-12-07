# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataClassificationRuleQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uuid': 'str',
        'rule_type': 'str',
        'secrecy_level': 'str',
        'secrecy_level_num': 'int',
        'name': 'str',
        'guid': 'str',
        'enable': 'bool',
        'method': 'str',
        'content_expression': 'str',
        'column_expression': 'str',
        'commit_expression': 'str',
        'project_id': 'str',
        'description': 'str',
        'created_by': 'str',
        'created_at': 'int',
        'updated_by': 'str',
        'updated_at': 'int',
        'builtin_rule_id': 'str',
        'category_id': 'str',
        'instance_id': 'str',
        'match_type': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'rule_type': 'rule_type',
        'secrecy_level': 'secrecy_level',
        'secrecy_level_num': 'secrecy_level_num',
        'name': 'name',
        'guid': 'guid',
        'enable': 'enable',
        'method': 'method',
        'content_expression': 'content_expression',
        'column_expression': 'column_expression',
        'commit_expression': 'commit_expression',
        'project_id': 'project_id',
        'description': 'description',
        'created_by': 'created_by',
        'created_at': 'created_at',
        'updated_by': 'updated_by',
        'updated_at': 'updated_at',
        'builtin_rule_id': 'builtin_rule_id',
        'category_id': 'category_id',
        'instance_id': 'instance_id',
        'match_type': 'match_type'
    }

    def __init__(self, uuid=None, rule_type=None, secrecy_level=None, secrecy_level_num=None, name=None, guid=None, enable=None, method=None, content_expression=None, column_expression=None, commit_expression=None, project_id=None, description=None, created_by=None, created_at=None, updated_by=None, updated_at=None, builtin_rule_id=None, category_id=None, instance_id=None, match_type=None):
        """DataClassificationRuleQueryDTO

        The model defined in huaweicloud sdk

        :param uuid: 规则ID
        :type uuid: str
        :param rule_type: 规则类型, CUSTOM, BUILTIN
        :type rule_type: str
        :param secrecy_level: 密级
        :type secrecy_level: str
        :param secrecy_level_num: 密级层级
        :type secrecy_level_num: int
        :param name: 规则名称
        :type name: str
        :param guid: guid
        :type guid: str
        :param enable: 规则是否开启
        :type enable: bool
        :param method: 规则方式, REGULAR, NONE, DEFAULT
        :type method: str
        :param content_expression: 内容表达式
        :type content_expression: str
        :param column_expression: 列表达式
        :type column_expression: str
        :param commit_expression: 备注表达式
        :type commit_expression: str
        :param project_id: 项目ID
        :type project_id: str
        :param description: 规则描述
        :type description: str
        :param created_by: 策略创建人
        :type created_by: str
        :param created_at: 策略创建时间
        :type created_at: int
        :param updated_by: 策略更新人
        :type updated_by: str
        :param updated_at: 策略更新时间
        :type updated_at: int
        :param builtin_rule_id: 内置规则ID
        :type builtin_rule_id: str
        :param category_id: 分类ID
        :type category_id: str
        :param instance_id: 实例ID
        :type instance_id: str
        :param match_type: 匹配类型
        :type match_type: str
        """
        
        

        self._uuid = None
        self._rule_type = None
        self._secrecy_level = None
        self._secrecy_level_num = None
        self._name = None
        self._guid = None
        self._enable = None
        self._method = None
        self._content_expression = None
        self._column_expression = None
        self._commit_expression = None
        self._project_id = None
        self._description = None
        self._created_by = None
        self._created_at = None
        self._updated_by = None
        self._updated_at = None
        self._builtin_rule_id = None
        self._category_id = None
        self._instance_id = None
        self._match_type = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if rule_type is not None:
            self.rule_type = rule_type
        if secrecy_level is not None:
            self.secrecy_level = secrecy_level
        if secrecy_level_num is not None:
            self.secrecy_level_num = secrecy_level_num
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid
        if enable is not None:
            self.enable = enable
        if method is not None:
            self.method = method
        if content_expression is not None:
            self.content_expression = content_expression
        if column_expression is not None:
            self.column_expression = column_expression
        if commit_expression is not None:
            self.commit_expression = commit_expression
        if project_id is not None:
            self.project_id = project_id
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_at is not None:
            self.updated_at = updated_at
        if builtin_rule_id is not None:
            self.builtin_rule_id = builtin_rule_id
        if category_id is not None:
            self.category_id = category_id
        if instance_id is not None:
            self.instance_id = instance_id
        if match_type is not None:
            self.match_type = match_type

    @property
    def uuid(self):
        """Gets the uuid of this DataClassificationRuleQueryDTO.

        规则ID

        :return: The uuid of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DataClassificationRuleQueryDTO.

        规则ID

        :param uuid: The uuid of this DataClassificationRuleQueryDTO.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def rule_type(self):
        """Gets the rule_type of this DataClassificationRuleQueryDTO.

        规则类型, CUSTOM, BUILTIN

        :return: The rule_type of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this DataClassificationRuleQueryDTO.

        规则类型, CUSTOM, BUILTIN

        :param rule_type: The rule_type of this DataClassificationRuleQueryDTO.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def secrecy_level(self):
        """Gets the secrecy_level of this DataClassificationRuleQueryDTO.

        密级

        :return: The secrecy_level of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._secrecy_level

    @secrecy_level.setter
    def secrecy_level(self, secrecy_level):
        """Sets the secrecy_level of this DataClassificationRuleQueryDTO.

        密级

        :param secrecy_level: The secrecy_level of this DataClassificationRuleQueryDTO.
        :type secrecy_level: str
        """
        self._secrecy_level = secrecy_level

    @property
    def secrecy_level_num(self):
        """Gets the secrecy_level_num of this DataClassificationRuleQueryDTO.

        密级层级

        :return: The secrecy_level_num of this DataClassificationRuleQueryDTO.
        :rtype: int
        """
        return self._secrecy_level_num

    @secrecy_level_num.setter
    def secrecy_level_num(self, secrecy_level_num):
        """Sets the secrecy_level_num of this DataClassificationRuleQueryDTO.

        密级层级

        :param secrecy_level_num: The secrecy_level_num of this DataClassificationRuleQueryDTO.
        :type secrecy_level_num: int
        """
        self._secrecy_level_num = secrecy_level_num

    @property
    def name(self):
        """Gets the name of this DataClassificationRuleQueryDTO.

        规则名称

        :return: The name of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataClassificationRuleQueryDTO.

        规则名称

        :param name: The name of this DataClassificationRuleQueryDTO.
        :type name: str
        """
        self._name = name

    @property
    def guid(self):
        """Gets the guid of this DataClassificationRuleQueryDTO.

        guid

        :return: The guid of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this DataClassificationRuleQueryDTO.

        guid

        :param guid: The guid of this DataClassificationRuleQueryDTO.
        :type guid: str
        """
        self._guid = guid

    @property
    def enable(self):
        """Gets the enable of this DataClassificationRuleQueryDTO.

        规则是否开启

        :return: The enable of this DataClassificationRuleQueryDTO.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this DataClassificationRuleQueryDTO.

        规则是否开启

        :param enable: The enable of this DataClassificationRuleQueryDTO.
        :type enable: bool
        """
        self._enable = enable

    @property
    def method(self):
        """Gets the method of this DataClassificationRuleQueryDTO.

        规则方式, REGULAR, NONE, DEFAULT

        :return: The method of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this DataClassificationRuleQueryDTO.

        规则方式, REGULAR, NONE, DEFAULT

        :param method: The method of this DataClassificationRuleQueryDTO.
        :type method: str
        """
        self._method = method

    @property
    def content_expression(self):
        """Gets the content_expression of this DataClassificationRuleQueryDTO.

        内容表达式

        :return: The content_expression of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._content_expression

    @content_expression.setter
    def content_expression(self, content_expression):
        """Sets the content_expression of this DataClassificationRuleQueryDTO.

        内容表达式

        :param content_expression: The content_expression of this DataClassificationRuleQueryDTO.
        :type content_expression: str
        """
        self._content_expression = content_expression

    @property
    def column_expression(self):
        """Gets the column_expression of this DataClassificationRuleQueryDTO.

        列表达式

        :return: The column_expression of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._column_expression

    @column_expression.setter
    def column_expression(self, column_expression):
        """Sets the column_expression of this DataClassificationRuleQueryDTO.

        列表达式

        :param column_expression: The column_expression of this DataClassificationRuleQueryDTO.
        :type column_expression: str
        """
        self._column_expression = column_expression

    @property
    def commit_expression(self):
        """Gets the commit_expression of this DataClassificationRuleQueryDTO.

        备注表达式

        :return: The commit_expression of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._commit_expression

    @commit_expression.setter
    def commit_expression(self, commit_expression):
        """Sets the commit_expression of this DataClassificationRuleQueryDTO.

        备注表达式

        :param commit_expression: The commit_expression of this DataClassificationRuleQueryDTO.
        :type commit_expression: str
        """
        self._commit_expression = commit_expression

    @property
    def project_id(self):
        """Gets the project_id of this DataClassificationRuleQueryDTO.

        项目ID

        :return: The project_id of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DataClassificationRuleQueryDTO.

        项目ID

        :param project_id: The project_id of this DataClassificationRuleQueryDTO.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def description(self):
        """Gets the description of this DataClassificationRuleQueryDTO.

        规则描述

        :return: The description of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataClassificationRuleQueryDTO.

        规则描述

        :param description: The description of this DataClassificationRuleQueryDTO.
        :type description: str
        """
        self._description = description

    @property
    def created_by(self):
        """Gets the created_by of this DataClassificationRuleQueryDTO.

        策略创建人

        :return: The created_by of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this DataClassificationRuleQueryDTO.

        策略创建人

        :param created_by: The created_by of this DataClassificationRuleQueryDTO.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this DataClassificationRuleQueryDTO.

        策略创建时间

        :return: The created_at of this DataClassificationRuleQueryDTO.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DataClassificationRuleQueryDTO.

        策略创建时间

        :param created_at: The created_at of this DataClassificationRuleQueryDTO.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_by(self):
        """Gets the updated_by of this DataClassificationRuleQueryDTO.

        策略更新人

        :return: The updated_by of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this DataClassificationRuleQueryDTO.

        策略更新人

        :param updated_by: The updated_by of this DataClassificationRuleQueryDTO.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def updated_at(self):
        """Gets the updated_at of this DataClassificationRuleQueryDTO.

        策略更新时间

        :return: The updated_at of this DataClassificationRuleQueryDTO.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DataClassificationRuleQueryDTO.

        策略更新时间

        :param updated_at: The updated_at of this DataClassificationRuleQueryDTO.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def builtin_rule_id(self):
        """Gets the builtin_rule_id of this DataClassificationRuleQueryDTO.

        内置规则ID

        :return: The builtin_rule_id of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._builtin_rule_id

    @builtin_rule_id.setter
    def builtin_rule_id(self, builtin_rule_id):
        """Sets the builtin_rule_id of this DataClassificationRuleQueryDTO.

        内置规则ID

        :param builtin_rule_id: The builtin_rule_id of this DataClassificationRuleQueryDTO.
        :type builtin_rule_id: str
        """
        self._builtin_rule_id = builtin_rule_id

    @property
    def category_id(self):
        """Gets the category_id of this DataClassificationRuleQueryDTO.

        分类ID

        :return: The category_id of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this DataClassificationRuleQueryDTO.

        分类ID

        :param category_id: The category_id of this DataClassificationRuleQueryDTO.
        :type category_id: str
        """
        self._category_id = category_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DataClassificationRuleQueryDTO.

        实例ID

        :return: The instance_id of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DataClassificationRuleQueryDTO.

        实例ID

        :param instance_id: The instance_id of this DataClassificationRuleQueryDTO.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def match_type(self):
        """Gets the match_type of this DataClassificationRuleQueryDTO.

        匹配类型

        :return: The match_type of this DataClassificationRuleQueryDTO.
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this DataClassificationRuleQueryDTO.

        匹配类型

        :param match_type: The match_type of this DataClassificationRuleQueryDTO.
        :type match_type: str
        """
        self._match_type = match_type

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
        if not isinstance(other, DataClassificationRuleQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
