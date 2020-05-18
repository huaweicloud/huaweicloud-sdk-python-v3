# coding: utf-8

import pprint
import re

import six


class RegisterFpgaImageOption(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'location': 'str',
        'name': 'str',
        'metadata': 'dict(str, str)',
        'description': 'str'
    }

    attribute_map = {
        'location': 'location',
        'name': 'name',
        'metadata': 'metadata',
        'description': 'description'
    }

    def __init__(self, location=None, name=None, metadata=None, description=None):  # noqa: E501
        """RegisterFpgaImageOption - a model defined in huaweicloud sdk"""

        self._location = None
        self._name = None
        self._metadata = None
        self._description = None
        self.discriminator = None

        self.location = location
        self.name = name
        self.metadata = metadata
        if description is not None:
            self.description = description

    @property
    def location(self):
        """Gets the location of this RegisterFpgaImageOption.

        FPGA逻辑文件在OBS桶中的路径，格式为“桶名:文件名”，例如“obs-fpga:fpga.bin”。  桶名的命名规则满足OBS的约束：  - 由英文小写字母、数字以及特殊字符“.”、“-”组成。  - 只能以数字或字母开头和结尾。  - 长度3～63个字符。  - 不能是ip地址。  - 不能包含“..”、“.-”&nbsp;、“-.”字符串。  文件名的命名规则如下：  - 由英文大、小写字母，数字，中划线，下划线，斜杠，英文句号组成。  - 必须以“.bin”或“xclbin”结尾。  - 长度4～64个字符。

        :return: The location of this RegisterFpgaImageOption.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this RegisterFpgaImageOption.

        FPGA逻辑文件在OBS桶中的路径，格式为“桶名:文件名”，例如“obs-fpga:fpga.bin”。  桶名的命名规则满足OBS的约束：  - 由英文小写字母、数字以及特殊字符“.”、“-”组成。  - 只能以数字或字母开头和结尾。  - 长度3～63个字符。  - 不能是ip地址。  - 不能包含“..”、“.-”&nbsp;、“-.”字符串。  文件名的命名规则如下：  - 由英文大、小写字母，数字，中划线，下划线，斜杠，英文句号组成。  - 必须以“.bin”或“xclbin”结尾。  - 长度4～64个字符。

        :param location: The location of this RegisterFpgaImageOption.
        :type: str
        """
        self._location = location

    @property
    def name(self):
        """Gets the name of this RegisterFpgaImageOption.

        FPGA镜像的名称。  取值范围：  - 只能由英文字母、数字、下划线、中划线组成。  - 长度1~64个字符。

        :return: The name of this RegisterFpgaImageOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RegisterFpgaImageOption.

        FPGA镜像的名称。  取值范围：  - 只能由英文字母、数字、下划线、中划线组成。  - 长度1~64个字符。

        :param name: The name of this RegisterFpgaImageOption.
        :type: str
        """
        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this RegisterFpgaImageOption.

        FPGA镜像的元数据信息，要求是合法的JSON（JavaScript Object Notation）对象类型。  metadata在进行JSON序列化后的字符个数不能超过1024。

        :return: The metadata of this RegisterFpgaImageOption.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RegisterFpgaImageOption.

        FPGA镜像的元数据信息，要求是合法的JSON（JavaScript Object Notation）对象类型。  metadata在进行JSON序列化后的字符个数不能超过1024。

        :param metadata: The metadata of this RegisterFpgaImageOption.
        :type: dict(str, str)
        """
        self._metadata = metadata

    @property
    def description(self):
        """Gets the description of this RegisterFpgaImageOption.

        FPGA镜像的描述信息，由中文汉字、中文句号、中文逗号、英文大小写字母、数字、中划线、下划线、英文句号、英文逗号、空格组成，长度0到255个字符。

        :return: The description of this RegisterFpgaImageOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RegisterFpgaImageOption.

        FPGA镜像的描述信息，由中文汉字、中文句号、中文逗号、英文大小写字母、数字、中划线、下划线、英文句号、英文逗号、空格组成，长度0到255个字符。

        :param description: The description of this RegisterFpgaImageOption.
        :type: str
        """
        self._description = description

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
        if not isinstance(other, RegisterFpgaImageOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
