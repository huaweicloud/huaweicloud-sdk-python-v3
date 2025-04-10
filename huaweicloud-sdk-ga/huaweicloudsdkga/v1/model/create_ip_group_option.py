# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateIpGroupOption:

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
        'ip_list': 'list[CreateIpGroupIpOption]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'ip_list': 'ip_list'
    }

    def __init__(self, name=None, description=None, ip_list=None):
        r"""CreateIpGroupOption

        The model defined in huaweicloud sdk

        :param name: IP地址组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: IP地址组的描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param ip_list: IP地址组中的IP网段列表，一次最多支持添加20个条目。
        :type ip_list: list[:class:`huaweicloudsdkga.v1.CreateIpGroupIpOption`]
        """
        
        

        self._name = None
        self._description = None
        self._ip_list = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if ip_list is not None:
            self.ip_list = ip_list

    @property
    def name(self):
        r"""Gets the name of this CreateIpGroupOption.

        IP地址组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this CreateIpGroupOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateIpGroupOption.

        IP地址组名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this CreateIpGroupOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateIpGroupOption.

        IP地址组的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this CreateIpGroupOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateIpGroupOption.

        IP地址组的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this CreateIpGroupOption.
        :type description: str
        """
        self._description = description

    @property
    def ip_list(self):
        r"""Gets the ip_list of this CreateIpGroupOption.

        IP地址组中的IP网段列表，一次最多支持添加20个条目。

        :return: The ip_list of this CreateIpGroupOption.
        :rtype: list[:class:`huaweicloudsdkga.v1.CreateIpGroupIpOption`]
        """
        return self._ip_list

    @ip_list.setter
    def ip_list(self, ip_list):
        r"""Sets the ip_list of this CreateIpGroupOption.

        IP地址组中的IP网段列表，一次最多支持添加20个条目。

        :param ip_list: The ip_list of this CreateIpGroupOption.
        :type ip_list: list[:class:`huaweicloudsdkga.v1.CreateIpGroupIpOption`]
        """
        self._ip_list = ip_list

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
        if not isinstance(other, CreateIpGroupOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
