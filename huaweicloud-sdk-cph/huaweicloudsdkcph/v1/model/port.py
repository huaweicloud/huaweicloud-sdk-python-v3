# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Port:

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
        'listen_port': 'int',
        'internet_accessible': 'str'
    }

    attribute_map = {
        'name': 'name',
        'listen_port': 'listen_port',
        'internet_accessible': 'internet_accessible'
    }

    def __init__(self, name=None, listen_port=None, internet_accessible=None):
        """Port

        The model defined in huaweicloud sdk

        :param name: 应用端口名称，不超过16个字节，系统关键服务名称不能使用\&quot;adb\&quot;和\&quot;vnc\&quot;。
        :type name: str
        :param listen_port: 端口号，大于等于10000，小于等于50000。
        :type listen_port: int
        :param internet_accessible: 为\&quot;true\&quot;则映射出公网访问（忽略大小写）。 为其他则不映射。
        :type internet_accessible: str
        """
        
        

        self._name = None
        self._listen_port = None
        self._internet_accessible = None
        self.discriminator = None

        self.name = name
        self.listen_port = listen_port
        self.internet_accessible = internet_accessible

    @property
    def name(self):
        """Gets the name of this Port.

        应用端口名称，不超过16个字节，系统关键服务名称不能使用\"adb\"和\"vnc\"。

        :return: The name of this Port.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Port.

        应用端口名称，不超过16个字节，系统关键服务名称不能使用\"adb\"和\"vnc\"。

        :param name: The name of this Port.
        :type name: str
        """
        self._name = name

    @property
    def listen_port(self):
        """Gets the listen_port of this Port.

        端口号，大于等于10000，小于等于50000。

        :return: The listen_port of this Port.
        :rtype: int
        """
        return self._listen_port

    @listen_port.setter
    def listen_port(self, listen_port):
        """Sets the listen_port of this Port.

        端口号，大于等于10000，小于等于50000。

        :param listen_port: The listen_port of this Port.
        :type listen_port: int
        """
        self._listen_port = listen_port

    @property
    def internet_accessible(self):
        """Gets the internet_accessible of this Port.

        为\"true\"则映射出公网访问（忽略大小写）。 为其他则不映射。

        :return: The internet_accessible of this Port.
        :rtype: str
        """
        return self._internet_accessible

    @internet_accessible.setter
    def internet_accessible(self, internet_accessible):
        """Sets the internet_accessible of this Port.

        为\"true\"则映射出公网访问（忽略大小写）。 为其他则不映射。

        :param internet_accessible: The internet_accessible of this Port.
        :type internet_accessible: str
        """
        self._internet_accessible = internet_accessible

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
        if not isinstance(other, Port):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
