# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RuleSet:

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
        'name': 'str',
        'type': 'str',
        'version': 'str',
        'operator': 'str',
        'operate_time': 'int',
        'is_valid': 'bool',
        'level': 'str',
        'is_public': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'version': 'version',
        'operator': 'operator',
        'operate_time': 'operate_time',
        'is_valid': 'is_valid',
        'level': 'level',
        'is_public': 'is_public'
    }

    def __init__(self, id=None, name=None, type=None, version=None, operator=None, operate_time=None, is_valid=None, level=None, is_public=None):
        """RuleSet

        The model defined in huaweicloud sdk

        :param id: 规则模版实例ID
        :type id: str
        :param name: 规则模版实例名称
        :type name: str
        :param type: 类型
        :type type: str
        :param version: 版本
        :type version: str
        :param operator: 最近操作人
        :type operator: str
        :param operate_time: 最近操作时间
        :type operate_time: int
        :param is_valid: 是否生效
        :type is_valid: bool
        :param level: 租户级、项目级
        :type level: str
        :param is_public: 是否系统级
        :type is_public: bool
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._version = None
        self._operator = None
        self._operate_time = None
        self._is_valid = None
        self._level = None
        self._is_public = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.type = type
        if version is not None:
            self.version = version
        self.operator = operator
        self.operate_time = operate_time
        self.is_valid = is_valid
        if level is not None:
            self.level = level
        if is_public is not None:
            self.is_public = is_public

    @property
    def id(self):
        """Gets the id of this RuleSet.

        规则模版实例ID

        :return: The id of this RuleSet.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleSet.

        规则模版实例ID

        :param id: The id of this RuleSet.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RuleSet.

        规则模版实例名称

        :return: The name of this RuleSet.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleSet.

        规则模版实例名称

        :param name: The name of this RuleSet.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this RuleSet.

        类型

        :return: The type of this RuleSet.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleSet.

        类型

        :param type: The type of this RuleSet.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this RuleSet.

        版本

        :return: The version of this RuleSet.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RuleSet.

        版本

        :param version: The version of this RuleSet.
        :type version: str
        """
        self._version = version

    @property
    def operator(self):
        """Gets the operator of this RuleSet.

        最近操作人

        :return: The operator of this RuleSet.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this RuleSet.

        最近操作人

        :param operator: The operator of this RuleSet.
        :type operator: str
        """
        self._operator = operator

    @property
    def operate_time(self):
        """Gets the operate_time of this RuleSet.

        最近操作时间

        :return: The operate_time of this RuleSet.
        :rtype: int
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this RuleSet.

        最近操作时间

        :param operate_time: The operate_time of this RuleSet.
        :type operate_time: int
        """
        self._operate_time = operate_time

    @property
    def is_valid(self):
        """Gets the is_valid of this RuleSet.

        是否生效

        :return: The is_valid of this RuleSet.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this RuleSet.

        是否生效

        :param is_valid: The is_valid of this RuleSet.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def level(self):
        """Gets the level of this RuleSet.

        租户级、项目级

        :return: The level of this RuleSet.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this RuleSet.

        租户级、项目级

        :param level: The level of this RuleSet.
        :type level: str
        """
        self._level = level

    @property
    def is_public(self):
        """Gets the is_public of this RuleSet.

        是否系统级

        :return: The is_public of this RuleSet.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this RuleSet.

        是否系统级

        :param is_public: The is_public of this RuleSet.
        :type is_public: bool
        """
        self._is_public = is_public

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
        if not isinstance(other, RuleSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
