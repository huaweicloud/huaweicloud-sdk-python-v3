# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAddressGroupOption:

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
        'description': 'str',
        'ip_version': 'int',
        'ip_set': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ip_version': 'ip_version',
        'ip_set': 'ip_set'
    }

    def __init__(self, name=None, description=None, ip_version=None, ip_set=None):
        """CreateAddressGroupOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：地址组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：地址组描述信息 取值范围：0-255个字符，不能包含“&lt;”和“&gt;”。 
        :type description: str
        :param ip_version: 功能说明：地址组ip版本 取值范围：4, 表示ipv4地址组；6，表示ipv6地址组
        :type ip_version: int
        :param ip_set: 功能说明：地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20
        :type ip_set: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._ip_version = None
        self._ip_set = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.ip_version = ip_version
        if ip_set is not None:
            self.ip_set = ip_set

    @property
    def name(self):
        """Gets the name of this CreateAddressGroupOption.

        功能说明：地址组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this CreateAddressGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateAddressGroupOption.

        功能说明：地址组名称 取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this CreateAddressGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateAddressGroupOption.

        功能说明：地址组描述信息 取值范围：0-255个字符，不能包含“<”和“>”。 

        :return: The description of this CreateAddressGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateAddressGroupOption.

        功能说明：地址组描述信息 取值范围：0-255个字符，不能包含“<”和“>”。 

        :param description: The description of this CreateAddressGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def ip_version(self):
        """Gets the ip_version of this CreateAddressGroupOption.

        功能说明：地址组ip版本 取值范围：4, 表示ipv4地址组；6，表示ipv6地址组

        :return: The ip_version of this CreateAddressGroupOption.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this CreateAddressGroupOption.

        功能说明：地址组ip版本 取值范围：4, 表示ipv4地址组；6，表示ipv6地址组

        :param ip_version: The ip_version of this CreateAddressGroupOption.
        :type ip_version: int
        """
        self._ip_version = ip_version

    @property
    def ip_set(self):
        """Gets the ip_set of this CreateAddressGroupOption.

        功能说明：地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20

        :return: The ip_set of this CreateAddressGroupOption.
        :rtype: list[str]
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this CreateAddressGroupOption.

        功能说明：地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20

        :param ip_set: The ip_set of this CreateAddressGroupOption.
        :type ip_set: list[str]
        """
        self._ip_set = ip_set

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateAddressGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
