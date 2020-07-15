# coding: utf-8

import pprint
import re

import six





class CreateVpcOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cidr': 'str',
        'name': 'str',
        'description': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'cidr': 'cidr',
        'name': 'name',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, cidr=None, name=None, description=None, enterprise_project_id='0'):
        """CreateVpcOption - a model defined in huaweicloud sdk"""
        
        

        self._cidr = None
        self._name = None
        self._description = None
        self._enterprise_project_id = None
        self.discriminator = None

        if cidr is not None:
            self.cidr = cidr
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def cidr(self):
        """Gets the cidr of this CreateVpcOption.

        功能说明：虚拟私有云下可用子网的范围 取值范围： - 10.0.0.0/8 ~ 10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :return: The cidr of this CreateVpcOption.
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this CreateVpcOption.

        功能说明：虚拟私有云下可用子网的范围 取值范围： - 10.0.0.0/8 ~ 10.255.255.240/28 - 172.16.0.0/12 ~ 172.31.255.240/28 - 192.168.0.0/16 ~ 192.168.255.240/28 约束：必须是ipv4 cidr格式，例如:192.168.0.0/16

        :param cidr: The cidr of this CreateVpcOption.
        :type: str
        """
        self._cidr = cidr

    @property
    def name(self):
        """Gets the name of this CreateVpcOption.

        功能说明：虚拟私有云名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 约束：如果名称不为空，则同一个租户下的名称不能重复

        :return: The name of this CreateVpcOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateVpcOption.

        功能说明：虚拟私有云名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点） 约束：如果名称不为空，则同一个租户下的名称不能重复

        :param name: The name of this CreateVpcOption.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateVpcOption.

        功能说明：虚拟私有云的描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :return: The description of this CreateVpcOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateVpcOption.

        功能说明：虚拟私有云的描述 取值范围：0-255个字符，不能包含“<”和“>”。

        :param description: The description of this CreateVpcOption.
        :type: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this CreateVpcOption.

        功能说明：企业项目ID。创建虚拟私有云时，给虚拟私有云绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 默认值：\"0\"

        :return: The enterprise_project_id of this CreateVpcOption.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this CreateVpcOption.

        功能说明：企业项目ID。创建虚拟私有云时，给虚拟私有云绑定企业项目ID。 取值范围：最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 默认值：\"0\"

        :param enterprise_project_id: The enterprise_project_id of this CreateVpcOption.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateVpcOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
