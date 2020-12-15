# coding: utf-8

import pprint
import re

import six





class Templatespec:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'labels': 'list[str]',
        'logo_url': 'str',
        'readme_url': 'str',
        'require': 'bool',
        'type': 'str',
        'versions': 'list[Versions]'
    }

    attribute_map = {
        'description': 'description',
        'labels': 'labels',
        'logo_url': 'logoURL',
        'readme_url': 'readmeURL',
        'require': 'require',
        'type': 'type',
        'versions': 'versions'
    }

    def __init__(self, description=None, labels=None, logo_url=None, readme_url=None, require=None, type=None, versions=None):
        """Templatespec - a model defined in huaweicloud sdk"""
        
        

        self._description = None
        self._labels = None
        self._logo_url = None
        self._readme_url = None
        self._require = None
        self._type = None
        self._versions = None
        self.discriminator = None

        self.description = description
        self.labels = labels
        self.logo_url = logo_url
        self.readme_url = readme_url
        if require is not None:
            self.require = require
        self.type = type
        self.versions = versions

    @property
    def description(self):
        """Gets the description of this Templatespec.

        模板描述

        :return: The description of this Templatespec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Templatespec.

        模板描述

        :param description: The description of this Templatespec.
        :type: str
        """
        self._description = description

    @property
    def labels(self):
        """Gets the labels of this Templatespec.

        模板所属分组

        :return: The labels of this Templatespec.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Templatespec.

        模板所属分组

        :param labels: The labels of this Templatespec.
        :type: list[str]
        """
        self._labels = labels

    @property
    def logo_url(self):
        """Gets the logo_url of this Templatespec.

        Logo图片地址

        :return: The logo_url of this Templatespec.
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this Templatespec.

        Logo图片地址

        :param logo_url: The logo_url of this Templatespec.
        :type: str
        """
        self._logo_url = logo_url

    @property
    def readme_url(self):
        """Gets the readme_url of this Templatespec.

        插件详情描述及使用说明

        :return: The readme_url of this Templatespec.
        :rtype: str
        """
        return self._readme_url

    @readme_url.setter
    def readme_url(self, readme_url):
        """Sets the readme_url of this Templatespec.

        插件详情描述及使用说明

        :param readme_url: The readme_url of this Templatespec.
        :type: str
        """
        self._readme_url = readme_url

    @property
    def require(self):
        """Gets the require of this Templatespec.

        是否为必安装插件

        :return: The require of this Templatespec.
        :rtype: bool
        """
        return self._require

    @require.setter
    def require(self, require):
        """Sets the require of this Templatespec.

        是否为必安装插件

        :param require: The require of this Templatespec.
        :type: bool
        """
        self._require = require

    @property
    def type(self):
        """Gets the type of this Templatespec.

        模板类型（helm，static）

        :return: The type of this Templatespec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Templatespec.

        模板类型（helm，static）

        :param type: The type of this Templatespec.
        :type: str
        """
        self._type = type

    @property
    def versions(self):
        """Gets the versions of this Templatespec.

        模板具体版本详情

        :return: The versions of this Templatespec.
        :rtype: list[Versions]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Templatespec.

        模板具体版本详情

        :param versions: The versions of this Templatespec.
        :type: list[Versions]
        """
        self._versions = versions

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
        if not isinstance(other, Templatespec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
