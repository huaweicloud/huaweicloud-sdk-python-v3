# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAddressGroupOption:

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
        'ip_set': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ip_set': 'ip_set'
    }

    def __init__(self, name=None, description=None, ip_set=None):
        """UpdateAddressGroupOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：地址组名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param description: 功能说明：IP地址组描述信息 取值范围：0-255个字符 约束：不能包含“&lt;”和“&gt;”。 
        :type description: str
        :param ip_set: 功能说明：IP地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20
        :type ip_set: list[str]
        """
        
        

        self._name = None
        self._description = None
        self._ip_set = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if ip_set is not None:
            self.ip_set = ip_set

    @property
    def name(self):
        """Gets the name of this UpdateAddressGroupOption.

        功能说明：地址组名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this UpdateAddressGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAddressGroupOption.

        功能说明：地址组名称 取值范围：0-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this UpdateAddressGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateAddressGroupOption.

        功能说明：IP地址组描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。 

        :return: The description of this UpdateAddressGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAddressGroupOption.

        功能说明：IP地址组描述信息 取值范围：0-255个字符 约束：不能包含“<”和“>”。 

        :param description: The description of this UpdateAddressGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def ip_set(self):
        """Gets the ip_set of this UpdateAddressGroupOption.

        功能说明：IP地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20

        :return: The ip_set of this UpdateAddressGroupOption.
        :rtype: list[str]
        """
        return self._ip_set

    @ip_set.setter
    def ip_set(self, ip_set):
        """Sets the ip_set of this UpdateAddressGroupOption.

        功能说明：IP地址组可包含地址集 取值范围：可以是单个ip地址，ip地址范围，ip地址cidr 约束：当前一个地址组ip_set数量限制默认值为20，即配置的ip地址、ip地址范围或ip地址cidr的总数默认限制20

        :param ip_set: The ip_set of this UpdateAddressGroupOption.
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
        if not isinstance(other, UpdateAddressGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
