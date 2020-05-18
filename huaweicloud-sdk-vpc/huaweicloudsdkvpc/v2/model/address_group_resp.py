# coding: utf-8

import pprint
import re

import six


class AddressGroupResp(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'created_at': 'str',
        'description': 'str',
        'id': 'str',
        'ip_set': 'list[str]',
        'ip_version': 'int',
        'name': 'str',
        'tenant_id': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'created_at': 'created_at',
        'description': 'description',
        'id': 'id',
        'ip_set': 'ip_set',
        'ip_version': 'ip_version',
        'name': 'name',
        'tenant_id': 'tenant_id',
        'updated_at': 'updated_at'
    }

    def __init__(self, created_at=None, description=None, id=None, ip_set=None, ip_version=None, name=None, tenant_id=None, updated_at=None):  # noqa: E501
        """AddressGroupResp - a model defined in huaweicloud sdk"""

        self._created_at = None
        self._description = None
        self._id = None
        self._ip_set = None
        self._ip_version = None
        self._name = None
        self._tenant_id = None
        self._updated_at = None
        self.discriminator = None

        self.created_at = created_at
        self.description = description
        self.id = id
        self.ip_set = ip_set
        self.ip_version = ip_version
        self.name = name
        self.tenant_id = tenant_id
        self.updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this AddressGroupResp.

        1、功能说明：地址组创建时间 2、取值范围：系统自动生成 3、约束：N/A 4、默认值：系统自动生成 5、权限：N/A

        :return: The created_at of this AddressGroupResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AddressGroupResp.

        1、功能说明：地址组创建时间 2、取值范围：系统自动生成 3、约束：N/A 4、默认值：系统自动生成 5、权限：N/A

        :param created_at: The created_at of this AddressGroupResp.
        :type: str
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this AddressGroupResp.

        1、功能说明：地址组描述信息 2、取值范围：0-255个字符 3、约束：不能包含“<”和“>”。 4、默认值：N/A 5、权限：N/A

        :return: The description of this AddressGroupResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddressGroupResp.

        1、功能说明：地址组描述信息 2、取值范围：0-255个字符 3、约束：不能包含“<”和“>”。 4、默认值：N/A 5、权限：N/A

        :param description: The description of this AddressGroupResp.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """Gets the id of this AddressGroupResp.

        1、功能说明：地址组唯一标识 2、取值范围：合法UUID的字符串 3、约束：合法UUID 4、默认值：N/A 5、权限：N/A

        :return: The id of this AddressGroupResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddressGroupResp.

        1、功能说明：地址组唯一标识 2、取值范围：合法UUID的字符串 3、约束：合法UUID 4、默认值：N/A 5、权限：N/A

        :param id: The id of this AddressGroupResp.
        :type: str
        """
        self._id = id

    @property
    def ip_set(self):
        """Gets the ip_set of this AddressGroupResp.

        1、功能说明：IP地址组可包含地址集 2、取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 3、约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20 4、默认值：N/A 5、权限：N/A

        :return: The ip_set of this AddressGroupResp.
        :rtype: list[str]
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this AddressGroupResp.

        1、功能说明：IP地址组可包含地址集 2、取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 3、约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20 4、默认值：N/A 5、权限：N/A

        :param ip_set: The ip_set of this AddressGroupResp.
        :type: list[str]
        """
        self._ip_set = ip_set

    @property
    def ip_version(self):
        """Gets the ip_version of this AddressGroupResp.

        1、功能说明：IP地址组ip版本，当前只支持ipv4 2、取值范围：4, 表示ipv4地址组 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The ip_version of this AddressGroupResp.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this AddressGroupResp.

        1、功能说明：IP地址组ip版本，当前只支持ipv4 2、取值范围：4, 表示ipv4地址组 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param ip_version: The ip_version of this AddressGroupResp.
        :type: int
        """
        self._ip_version = ip_version

    @property
    def name(self):
        """Gets the name of this AddressGroupResp.

        1、功能说明：地址组名称 2、取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The name of this AddressGroupResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddressGroupResp.

        1、功能说明：地址组名称 2、取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param name: The name of this AddressGroupResp.
        :type: str
        """
        self._name = name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this AddressGroupResp.

        1、功能说明：租户ID 2、取值范围：租户的tenant_id 3、约束：租户信息合法 4、默认值：N/A 5、权限：N/A

        :return: The tenant_id of this AddressGroupResp.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this AddressGroupResp.

        1、功能说明：租户ID 2、取值范围：租户的tenant_id 3、约束：租户信息合法 4、默认值：N/A 5、权限：N/A

        :param tenant_id: The tenant_id of this AddressGroupResp.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def updated_at(self):
        """Gets the updated_at of this AddressGroupResp.

        1、功能描述：地址组最近一次更新资源的时间 2、取值范围：系统自动生成 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :return: The updated_at of this AddressGroupResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this AddressGroupResp.

        1、功能描述：地址组最近一次更新资源的时间 2、取值范围：系统自动生成 3、约束：N/A 4、默认值：N/A 5、权限：N/A

        :param updated_at: The updated_at of this AddressGroupResp.
        :type: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, AddressGroupResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
