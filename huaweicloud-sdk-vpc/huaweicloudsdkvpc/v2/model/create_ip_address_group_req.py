# coding: utf-8

import pprint
import re

import six


class CreateIpAddressGroupReq(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'name': 'str',
        'ip_version': 'int',
        'ip_set': 'list[str]',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ip_version': 'ip_version',
        'ip_set': 'ip_set',
        'description': 'description'
    }

    def __init__(self, name=None, ip_version=None, ip_set=None, description=None):  # noqa: E501
        """CreateIpAddressGroupReq - a model defined in huaweicloud sdk"""

        self._name = None
        self._ip_version = None
        self._ip_set = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.ip_version = ip_version
        if ip_set is not None:
            self.ip_set = ip_set
        if description is not None:
            self.description = description

    @property
    def name(self):
        """Gets the name of this CreateIpAddressGroupReq.

        1、功能说明：地址组名称 2、取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The name of this CreateIpAddressGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateIpAddressGroupReq.

        1、功能说明：地址组名称 2、取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param name: The name of this CreateIpAddressGroupReq.
        :type: str
        """
        self._name = name

    @property
    def ip_version(self):
        """Gets the ip_version of this CreateIpAddressGroupReq.

        1、功能说明：IP地址组ip版本，当前只支持ipv4 2、取值范围：4, 表示ipv4地址组 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The ip_version of this CreateIpAddressGroupReq.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CreateIpAddressGroupReq.

        1、功能说明：IP地址组ip版本，当前只支持ipv4 2、取值范围：4, 表示ipv4地址组 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param ip_version: The ip_version of this CreateIpAddressGroupReq.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def ip_set(self):
        """Gets the ip_set of this CreateIpAddressGroupReq.

        1、功能说明：IP地址组可包含地址集 2、取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 3、约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20 4、默认值：N/A 5、权限：N/A

        :return: The ip_set of this CreateIpAddressGroupReq.
        :rtype: list[str]
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this CreateIpAddressGroupReq.

        1、功能说明：IP地址组可包含地址集 2、取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 3、约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20 4、默认值：N/A 5、权限：N/A

        :param ip_set: The ip_set of this CreateIpAddressGroupReq.
        :type: list[str]
        """
        self._ip_set = ip_set

    @property
    def description(self):
        """Gets the description of this CreateIpAddressGroupReq.

        1、功能说明：IP地址组描述信息 2、取值范围：0-255个字符 3、约束：不能包含“<”和“>”。 4、默认值：N/A 5、权限：N/A

        :return: The description of this CreateIpAddressGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateIpAddressGroupReq.

        1、功能说明：IP地址组描述信息 2、取值范围：0-255个字符 3、约束：不能包含“<”和“>”。 4、默认值：N/A 5、权限：N/A

        :param description: The description of this CreateIpAddressGroupReq.
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
        if not isinstance(other, CreateIpAddressGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
