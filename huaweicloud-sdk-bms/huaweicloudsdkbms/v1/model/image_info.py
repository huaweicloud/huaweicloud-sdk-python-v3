# coding: utf-8

import pprint
import re

import six





class ImageInfo:


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
        'os_type': 'str',
        'links': 'list[Links]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'os_type': '__os_type',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, os_type=None, links=None):
        """ImageInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._os_type = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if os_type is not None:
            self.os_type = os_type
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this ImageInfo.

        镜像ID，格式为UUID。

        :return: The id of this ImageInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageInfo.

        镜像ID，格式为UUID。

        :param id: The id of this ImageInfo.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ImageInfo.

        镜像的名称

        :return: The name of this ImageInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageInfo.

        镜像的名称

        :param name: The name of this ImageInfo.
        :type: str
        """
        self._name = name

    @property
    def os_type(self):
        """Gets the os_type of this ImageInfo.

        镜像的类型。取值为：Linux（包括SUSE/RedHat/CentOS/Oracle Linux/EulerOS/Ubuntu操作系统）Windows（Windows操作系统）Other（ESXi操作系统）

        :return: The os_type of this ImageInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        """Sets the os_type of this ImageInfo.

        镜像的类型。取值为：Linux（包括SUSE/RedHat/CentOS/Oracle Linux/EulerOS/Ubuntu操作系统）Windows（Windows操作系统）Other（ESXi操作系统）

        :param os_type: The os_type of this ImageInfo.
        :type: str
        """
        self._os_type = os_type

    @property
    def links(self):
        """Gets the links of this ImageInfo.

        镜像相关快捷链接地址。

        :return: The links of this ImageInfo.
        :rtype: list[Links]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ImageInfo.

        镜像相关快捷链接地址。

        :param links: The links of this ImageInfo.
        :type: list[Links]
        """
        self._links = links

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
        if not isinstance(other, ImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
