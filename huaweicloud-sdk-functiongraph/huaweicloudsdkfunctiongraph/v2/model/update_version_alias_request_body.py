# coding: utf-8

import pprint
import re

import six





class UpdateVersionAliasRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'version': 'str',
        'description': 'str',
        'last_modified': 'datetime',
        'alias_urn': 'str',
        'additional_version_weights': 'dict(str, int)'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'description': 'description',
        'last_modified': 'last_modified',
        'alias_urn': 'alias_urn',
        'additional_version_weights': 'additional_version_weights'
    }

    def __init__(self, name=None, version=None, description=None, last_modified=None, alias_urn=None, additional_version_weights=None):
        """UpdateVersionAliasRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._version = None
        self._description = None
        self._last_modified = None
        self._alias_urn = None
        self._additional_version_weights = None
        self.discriminator = None

        self.name = name
        self.version = version
        if description is not None:
            self.description = description
        self.last_modified = last_modified
        self.alias_urn = alias_urn
        if additional_version_weights is not None:
            self.additional_version_weights = additional_version_weights

    @property
    def name(self):
        """Gets the name of this UpdateVersionAliasRequestBody.

        要获取的别名名称。

        :return: The name of this UpdateVersionAliasRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateVersionAliasRequestBody.

        要获取的别名名称。

        :param name: The name of this UpdateVersionAliasRequestBody.
        :type: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this UpdateVersionAliasRequestBody.

        别名对应的版本名称。

        :return: The version of this UpdateVersionAliasRequestBody.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateVersionAliasRequestBody.

        别名对应的版本名称。

        :param version: The version of this UpdateVersionAliasRequestBody.
        :type: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this UpdateVersionAliasRequestBody.

        别名描述信息。

        :return: The description of this UpdateVersionAliasRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateVersionAliasRequestBody.

        别名描述信息。

        :param description: The description of this UpdateVersionAliasRequestBody.
        :type: str
        """
        self._description = description

    @property
    def last_modified(self):
        """Gets the last_modified of this UpdateVersionAliasRequestBody.

        别名最后修改时间。

        :return: The last_modified of this UpdateVersionAliasRequestBody.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this UpdateVersionAliasRequestBody.

        别名最后修改时间。

        :param last_modified: The last_modified of this UpdateVersionAliasRequestBody.
        :type: datetime
        """
        self._last_modified = last_modified

    @property
    def alias_urn(self):
        """Gets the alias_urn of this UpdateVersionAliasRequestBody.

        版本别名唯一标识。

        :return: The alias_urn of this UpdateVersionAliasRequestBody.
        :rtype: str
        """
        return self._alias_urn

    @alias_urn.setter
    def alias_urn(self, alias_urn):
        """Sets the alias_urn of this UpdateVersionAliasRequestBody.

        版本别名唯一标识。

        :param alias_urn: The alias_urn of this UpdateVersionAliasRequestBody.
        :type: str
        """
        self._alias_urn = alias_urn

    @property
    def additional_version_weights(self):
        """Gets the additional_version_weights of this UpdateVersionAliasRequestBody.

        灰度版本信息

        :return: The additional_version_weights of this UpdateVersionAliasRequestBody.
        :rtype: dict(str, int)
        """
        return self._additional_version_weights

    @additional_version_weights.setter
    def additional_version_weights(self, additional_version_weights):
        """Sets the additional_version_weights of this UpdateVersionAliasRequestBody.

        灰度版本信息

        :param additional_version_weights: The additional_version_weights of this UpdateVersionAliasRequestBody.
        :type: dict(str, int)
        """
        self._additional_version_weights = additional_version_weights

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
        if not isinstance(other, UpdateVersionAliasRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
