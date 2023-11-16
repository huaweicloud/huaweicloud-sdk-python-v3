# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleOpenSourceRuleSetVO:

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
        'level': 'str',
        'is_valid': 'bool',
        'version': 'str',
        'operator': 'str',
        'is_public': 'bool',
        'is_legacy': 'bool',
        'operate_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'level': 'level',
        'is_valid': 'is_valid',
        'version': 'version',
        'operator': 'operator',
        'is_public': 'is_public',
        'is_legacy': 'is_legacy',
        'operate_time': 'operate_time'
    }

    def __init__(self, id=None, name=None, level=None, is_valid=None, version=None, operator=None, is_public=None, is_legacy=None, operate_time=None):
        """SimpleOpenSourceRuleSetVO

        The model defined in huaweicloud sdk

        :param id: 开源治理策略ID
        :type id: str
        :param name: 开源治理策略名称
        :type name: str
        :param level: 开源治理策略级别（tenant-租户级，project-项目级）
        :type level: str
        :param is_valid: 是否可用
        :type is_valid: bool
        :param version: 版本
        :type version: str
        :param operator: 操作人
        :type operator: str
        :param is_public: 是否系统策略
        :type is_public: bool
        :param is_legacy: 是否老版
        :type is_legacy: bool
        :param operate_time: 操作时间
        :type operate_time: int
        """
        
        

        self._id = None
        self._name = None
        self._level = None
        self._is_valid = None
        self._version = None
        self._operator = None
        self._is_public = None
        self._is_legacy = None
        self._operate_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if level is not None:
            self.level = level
        if is_valid is not None:
            self.is_valid = is_valid
        if version is not None:
            self.version = version
        if operator is not None:
            self.operator = operator
        if is_public is not None:
            self.is_public = is_public
        if is_legacy is not None:
            self.is_legacy = is_legacy
        if operate_time is not None:
            self.operate_time = operate_time

    @property
    def id(self):
        """Gets the id of this SimpleOpenSourceRuleSetVO.

        开源治理策略ID

        :return: The id of this SimpleOpenSourceRuleSetVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimpleOpenSourceRuleSetVO.

        开源治理策略ID

        :param id: The id of this SimpleOpenSourceRuleSetVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this SimpleOpenSourceRuleSetVO.

        开源治理策略名称

        :return: The name of this SimpleOpenSourceRuleSetVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimpleOpenSourceRuleSetVO.

        开源治理策略名称

        :param name: The name of this SimpleOpenSourceRuleSetVO.
        :type name: str
        """
        self._name = name

    @property
    def level(self):
        """Gets the level of this SimpleOpenSourceRuleSetVO.

        开源治理策略级别（tenant-租户级，project-项目级）

        :return: The level of this SimpleOpenSourceRuleSetVO.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this SimpleOpenSourceRuleSetVO.

        开源治理策略级别（tenant-租户级，project-项目级）

        :param level: The level of this SimpleOpenSourceRuleSetVO.
        :type level: str
        """
        self._level = level

    @property
    def is_valid(self):
        """Gets the is_valid of this SimpleOpenSourceRuleSetVO.

        是否可用

        :return: The is_valid of this SimpleOpenSourceRuleSetVO.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this SimpleOpenSourceRuleSetVO.

        是否可用

        :param is_valid: The is_valid of this SimpleOpenSourceRuleSetVO.
        :type is_valid: bool
        """
        self._is_valid = is_valid

    @property
    def version(self):
        """Gets the version of this SimpleOpenSourceRuleSetVO.

        版本

        :return: The version of this SimpleOpenSourceRuleSetVO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SimpleOpenSourceRuleSetVO.

        版本

        :param version: The version of this SimpleOpenSourceRuleSetVO.
        :type version: str
        """
        self._version = version

    @property
    def operator(self):
        """Gets the operator of this SimpleOpenSourceRuleSetVO.

        操作人

        :return: The operator of this SimpleOpenSourceRuleSetVO.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this SimpleOpenSourceRuleSetVO.

        操作人

        :param operator: The operator of this SimpleOpenSourceRuleSetVO.
        :type operator: str
        """
        self._operator = operator

    @property
    def is_public(self):
        """Gets the is_public of this SimpleOpenSourceRuleSetVO.

        是否系统策略

        :return: The is_public of this SimpleOpenSourceRuleSetVO.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this SimpleOpenSourceRuleSetVO.

        是否系统策略

        :param is_public: The is_public of this SimpleOpenSourceRuleSetVO.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def is_legacy(self):
        """Gets the is_legacy of this SimpleOpenSourceRuleSetVO.

        是否老版

        :return: The is_legacy of this SimpleOpenSourceRuleSetVO.
        :rtype: bool
        """
        return self._is_legacy

    @is_legacy.setter
    def is_legacy(self, is_legacy):
        """Sets the is_legacy of this SimpleOpenSourceRuleSetVO.

        是否老版

        :param is_legacy: The is_legacy of this SimpleOpenSourceRuleSetVO.
        :type is_legacy: bool
        """
        self._is_legacy = is_legacy

    @property
    def operate_time(self):
        """Gets the operate_time of this SimpleOpenSourceRuleSetVO.

        操作时间

        :return: The operate_time of this SimpleOpenSourceRuleSetVO.
        :rtype: int
        """
        return self._operate_time

    @operate_time.setter
    def operate_time(self, operate_time):
        """Sets the operate_time of this SimpleOpenSourceRuleSetVO.

        操作时间

        :param operate_time: The operate_time of this SimpleOpenSourceRuleSetVO.
        :type operate_time: int
        """
        self._operate_time = operate_time

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
        if not isinstance(other, SimpleOpenSourceRuleSetVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
