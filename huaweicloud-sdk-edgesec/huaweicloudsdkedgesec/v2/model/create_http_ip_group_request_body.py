# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateHttpIpGroupRequestBody:

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
        'ips': 'str',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'ips': 'ips',
        'description': 'description'
    }

    def __init__(self, name=None, ips=None, description=None):
        r"""CreateHttpIpGroupRequestBody

        The model defined in huaweicloud sdk

        :param name: IP地址组名称
        :type name: str
        :param ips: IP地址/IP段，以英文逗号分隔，最多配置200个IP/IP段
        :type ips: str
        :param description: IP地址组备注，最长512字符
        :type description: str
        """
        
        

        self._name = None
        self._ips = None
        self._description = None
        self.discriminator = None

        self.name = name
        self.ips = ips
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this CreateHttpIpGroupRequestBody.

        IP地址组名称

        :return: The name of this CreateHttpIpGroupRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateHttpIpGroupRequestBody.

        IP地址组名称

        :param name: The name of this CreateHttpIpGroupRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def ips(self):
        r"""Gets the ips of this CreateHttpIpGroupRequestBody.

        IP地址/IP段，以英文逗号分隔，最多配置200个IP/IP段

        :return: The ips of this CreateHttpIpGroupRequestBody.
        :rtype: str
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        r"""Sets the ips of this CreateHttpIpGroupRequestBody.

        IP地址/IP段，以英文逗号分隔，最多配置200个IP/IP段

        :param ips: The ips of this CreateHttpIpGroupRequestBody.
        :type ips: str
        """
        self._ips = ips

    @property
    def description(self):
        r"""Gets the description of this CreateHttpIpGroupRequestBody.

        IP地址组备注，最长512字符

        :return: The description of this CreateHttpIpGroupRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateHttpIpGroupRequestBody.

        IP地址组备注，最长512字符

        :param description: The description of this CreateHttpIpGroupRequestBody.
        :type description: str
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
        if not isinstance(other, CreateHttpIpGroupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
