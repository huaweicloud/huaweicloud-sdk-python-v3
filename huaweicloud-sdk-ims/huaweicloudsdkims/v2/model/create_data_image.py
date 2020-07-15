# coding: utf-8

import pprint
import re

import six





class CreateDataImage:


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
        'volume_id': 'str',
        'description': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'volume_id': 'volume_id',
        'description': 'description',
        'tags': 'tags'
    }

    def __init__(self, name=None, volume_id=None, description=None, tags=None):
        """CreateDataImage - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._volume_id = None
        self._description = None
        self._tags = None
        self.discriminator = None

        self.name = name
        self.volume_id = volume_id
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        """Gets the name of this CreateDataImage.

        数据盘镜像名称。

        :return: The name of this CreateDataImage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDataImage.

        数据盘镜像名称。

        :param name: The name of this CreateDataImage.
        :type: str
        """
        self._name = name

    @property
    def volume_id(self):
        """Gets the volume_id of this CreateDataImage.

        数据盘ID。

        :return: The volume_id of this CreateDataImage.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this CreateDataImage.

        数据盘ID。

        :param volume_id: The volume_id of this CreateDataImage.
        :type: str
        """
        self._volume_id = volume_id

    @property
    def description(self):
        """Gets the description of this CreateDataImage.

        数据盘描述。

        :return: The description of this CreateDataImage.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDataImage.

        数据盘描述。

        :param description: The description of this CreateDataImage.
        :type: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this CreateDataImage.

        数据盘镜像标签。

        :return: The tags of this CreateDataImage.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CreateDataImage.

        数据盘镜像标签。

        :param tags: The tags of this CreateDataImage.
        :type: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CreateDataImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
