# coding: utf-8

import pprint
import re

import six





class Versions:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'creation_timestamp': 'date',
        'input': 'object',
        'stable': 'bool',
        'support_versions': 'list[SupportVersions]',
        'translate': 'object',
        'update_timestamp': 'date',
        'version': 'str'
    }

    attribute_map = {
        'creation_timestamp': 'creationTimestamp',
        'input': 'input',
        'stable': 'stable',
        'support_versions': 'supportVersions',
        'translate': 'translate',
        'update_timestamp': 'updateTimestamp',
        'version': 'version'
    }

    def __init__(self, creation_timestamp=None, input=None, stable=None, support_versions=None, translate=None, update_timestamp=None, version=None):
        """Versions - a model defined in huaweicloud sdk"""
        
        

        self._creation_timestamp = None
        self._input = None
        self._stable = None
        self._support_versions = None
        self._translate = None
        self._update_timestamp = None
        self._version = None
        self.discriminator = None

        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        self.input = input
        self.stable = stable
        self.support_versions = support_versions
        self.translate = translate
        self.update_timestamp = update_timestamp
        self.version = version

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Versions.

        创建时间

        :return: The creation_timestamp of this Versions.
        :rtype: date
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Versions.

        创建时间

        :param creation_timestamp: The creation_timestamp of this Versions.
        :type: date
        """
        self._creation_timestamp = creation_timestamp

    @property
    def input(self):
        """Gets the input of this Versions.

        插件安装参数

        :return: The input of this Versions.
        :rtype: object
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this Versions.

        插件安装参数

        :param input: The input of this Versions.
        :type: object
        """
        self._input = input

    @property
    def stable(self):
        """Gets the stable of this Versions.

        是否为稳定版本

        :return: The stable of this Versions.
        :rtype: bool
        """
        return self._stable

    @stable.setter
    def stable(self, stable):
        """Sets the stable of this Versions.

        是否为稳定版本

        :param stable: The stable of this Versions.
        :type: bool
        """
        self._stable = stable

    @property
    def support_versions(self):
        """Gets the support_versions of this Versions.

        支持集群版本号

        :return: The support_versions of this Versions.
        :rtype: list[SupportVersions]
        """
        return self._support_versions

    @support_versions.setter
    def support_versions(self, support_versions):
        """Sets the support_versions of this Versions.

        支持集群版本号

        :param support_versions: The support_versions of this Versions.
        :type: list[SupportVersions]
        """
        self._support_versions = support_versions

    @property
    def translate(self):
        """Gets the translate of this Versions.

        供界面使用的翻译信息

        :return: The translate of this Versions.
        :rtype: object
        """
        return self._translate

    @translate.setter
    def translate(self, translate):
        """Sets the translate of this Versions.

        供界面使用的翻译信息

        :param translate: The translate of this Versions.
        :type: object
        """
        self._translate = translate

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this Versions.

        更新时间

        :return: The update_timestamp of this Versions.
        :rtype: date
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this Versions.

        更新时间

        :param update_timestamp: The update_timestamp of this Versions.
        :type: date
        """
        self._update_timestamp = update_timestamp

    @property
    def version(self):
        """Gets the version of this Versions.

        插件版本号

        :return: The version of this Versions.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Versions.

        插件版本号

        :param version: The version of this Versions.
        :type: str
        """
        self._version = version

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Versions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
