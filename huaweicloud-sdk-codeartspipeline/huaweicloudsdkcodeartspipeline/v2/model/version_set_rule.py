# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionSetRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'ecosystem': 'str',
        'package_name': 'str',
        'package_version': 'str',
        'description': 'str',
        'predicate': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'ecosystem': 'ecosystem',
        'package_name': 'package_name',
        'package_version': 'package_version',
        'description': 'description',
        'predicate': 'predicate'
    }

    def __init__(self, enable=None, ecosystem=None, package_name=None, package_version=None, description=None, predicate=None):
        """VersionSetRule

        The model defined in huaweicloud sdk

        :param enable: 是否开启
        :type enable: bool
        :param ecosystem: 依赖类型
        :type ecosystem: str
        :param package_name: 包名称
        :type package_name: str
        :param package_version: 包版本
        :type package_version: str
        :param description: 规则说明
        :type description: str
        :param predicate: 比较规则
        :type predicate: str
        """
        
        

        self._enable = None
        self._ecosystem = None
        self._package_name = None
        self._package_version = None
        self._description = None
        self._predicate = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if ecosystem is not None:
            self.ecosystem = ecosystem
        if package_name is not None:
            self.package_name = package_name
        if package_version is not None:
            self.package_version = package_version
        if description is not None:
            self.description = description
        if predicate is not None:
            self.predicate = predicate

    @property
    def enable(self):
        """Gets the enable of this VersionSetRule.

        是否开启

        :return: The enable of this VersionSetRule.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this VersionSetRule.

        是否开启

        :param enable: The enable of this VersionSetRule.
        :type enable: bool
        """
        self._enable = enable

    @property
    def ecosystem(self):
        """Gets the ecosystem of this VersionSetRule.

        依赖类型

        :return: The ecosystem of this VersionSetRule.
        :rtype: str
        """
        return self._ecosystem

    @ecosystem.setter
    def ecosystem(self, ecosystem):
        """Sets the ecosystem of this VersionSetRule.

        依赖类型

        :param ecosystem: The ecosystem of this VersionSetRule.
        :type ecosystem: str
        """
        self._ecosystem = ecosystem

    @property
    def package_name(self):
        """Gets the package_name of this VersionSetRule.

        包名称

        :return: The package_name of this VersionSetRule.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this VersionSetRule.

        包名称

        :param package_name: The package_name of this VersionSetRule.
        :type package_name: str
        """
        self._package_name = package_name

    @property
    def package_version(self):
        """Gets the package_version of this VersionSetRule.

        包版本

        :return: The package_version of this VersionSetRule.
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this VersionSetRule.

        包版本

        :param package_version: The package_version of this VersionSetRule.
        :type package_version: str
        """
        self._package_version = package_version

    @property
    def description(self):
        """Gets the description of this VersionSetRule.

        规则说明

        :return: The description of this VersionSetRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VersionSetRule.

        规则说明

        :param description: The description of this VersionSetRule.
        :type description: str
        """
        self._description = description

    @property
    def predicate(self):
        """Gets the predicate of this VersionSetRule.

        比较规则

        :return: The predicate of this VersionSetRule.
        :rtype: str
        """
        return self._predicate

    @predicate.setter
    def predicate(self, predicate):
        """Sets the predicate of this VersionSetRule.

        比较规则

        :param predicate: The predicate of this VersionSetRule.
        :type predicate: str
        """
        self._predicate = predicate

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
        if not isinstance(other, VersionSetRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
