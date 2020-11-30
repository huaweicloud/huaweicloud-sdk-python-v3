# coding: utf-8

import pprint
import re

import six





class InstancesResponseInstancesVOResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'link': 'str',
        'arch': 'str',
        'id': 'str',
        'private': 'bool'
    }

    attribute_map = {
        'link': 'link',
        'arch': 'arch',
        'id': 'id',
        'private': 'private'
    }

    def __init__(self, link=None, arch=None, id=None, private=None):
        """InstancesResponseInstancesVOResult - a model defined in huaweicloud sdk"""
        
        

        self._link = None
        self._arch = None
        self._id = None
        self._private = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if arch is not None:
            self.arch = arch
        if id is not None:
            self.id = id
        if private is not None:
            self.private = private

    @property
    def link(self):
        """Gets the link of this InstancesResponseInstancesVOResult.

        链接

        :return: The link of this InstancesResponseInstancesVOResult.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InstancesResponseInstancesVOResult.

        链接

        :param link: The link of this InstancesResponseInstancesVOResult.
        :type: str
        """
        self._link = link

    @property
    def arch(self):
        """Gets the arch of this InstancesResponseInstancesVOResult.

        cpu架构 x86|arm

        :return: The arch of this InstancesResponseInstancesVOResult.
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this InstancesResponseInstancesVOResult.

        cpu架构 x86|arm

        :param arch: The arch of this InstancesResponseInstancesVOResult.
        :type: str
        """
        self._arch = arch

    @property
    def id(self):
        """Gets the id of this InstancesResponseInstancesVOResult.

        实例id

        :return: The id of this InstancesResponseInstancesVOResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstancesResponseInstancesVOResult.

        实例id

        :param id: The id of this InstancesResponseInstancesVOResult.
        :type: str
        """
        self._id = id

    @property
    def private(self):
        """Gets the private of this InstancesResponseInstancesVOResult.

        是否私有平台

        :return: The private of this InstancesResponseInstancesVOResult.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """Sets the private of this InstancesResponseInstancesVOResult.

        是否私有平台

        :param private: The private of this InstancesResponseInstancesVOResult.
        :type: bool
        """
        self._private = private

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
        if not isinstance(other, InstancesResponseInstancesVOResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
