# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerOption:

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
        'hostname': 'str',
        'user_data': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'hostname': 'hostname',
        'user_data': 'user_data'
    }

    def __init__(self, name=None, description=None, hostname=None, user_data=None):
        """UpdateServerOption

        The model defined in huaweicloud sdk

        :param name: 修改后的云服务器名称。  只能由中文字符、英文字母、数字及“_”、“-”、“.”组成，且长度为[1-64]个字符。
        :type name: str
        :param description: 对弹性云服务器的任意描述。  不能包含“&lt;”,“&gt;”，且长度范围为[0-85]个字符。
        :type description: str
        :param hostname: 修改云服务hostname。  命令规范：长度为 [1-64] 个字符，允许使用点号(.)分隔字符成多段，每段允许使用大小写字母、数字或连字符(-)，但不能连续使用点号(.)或连字符(-),不能以点号(.)或连字符(-)开头或结尾，不能出现（.-）和（-.）。
        :type hostname: str
        :param user_data: 修改云服务器云主机过程中待注入实例自定义数据。支持注入文本、文本文件。  示例：  base64编码前：   Linux服务器：     #!/bin/bash     echo user_test &gt; /home/user.txt   Windows服务器：     rem cmd     echo 111 &gt; c:\\aaa.txt  base64编码后：   Linux服务器：IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA&#x3D;&#x3D;   Windows服务器：cmVtIGNtZA0KZWNobyAxMTEgJmd0OyBjOlxhYWEudHh0
        :type user_data: str
        """
        
        

        self._name = None
        self._description = None
        self._hostname = None
        self._user_data = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if hostname is not None:
            self.hostname = hostname
        if user_data is not None:
            self.user_data = user_data

    @property
    def name(self):
        """Gets the name of this UpdateServerOption.

        修改后的云服务器名称。  只能由中文字符、英文字母、数字及“_”、“-”、“.”组成，且长度为[1-64]个字符。

        :return: The name of this UpdateServerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateServerOption.

        修改后的云服务器名称。  只能由中文字符、英文字母、数字及“_”、“-”、“.”组成，且长度为[1-64]个字符。

        :param name: The name of this UpdateServerOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateServerOption.

        对弹性云服务器的任意描述。  不能包含“<”,“>”，且长度范围为[0-85]个字符。

        :return: The description of this UpdateServerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateServerOption.

        对弹性云服务器的任意描述。  不能包含“<”,“>”，且长度范围为[0-85]个字符。

        :param description: The description of this UpdateServerOption.
        :type description: str
        """
        self._description = description

    @property
    def hostname(self):
        """Gets the hostname of this UpdateServerOption.

        修改云服务hostname。  命令规范：长度为 [1-64] 个字符，允许使用点号(.)分隔字符成多段，每段允许使用大小写字母、数字或连字符(-)，但不能连续使用点号(.)或连字符(-),不能以点号(.)或连字符(-)开头或结尾，不能出现（.-）和（-.）。

        :return: The hostname of this UpdateServerOption.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this UpdateServerOption.

        修改云服务hostname。  命令规范：长度为 [1-64] 个字符，允许使用点号(.)分隔字符成多段，每段允许使用大小写字母、数字或连字符(-)，但不能连续使用点号(.)或连字符(-),不能以点号(.)或连字符(-)开头或结尾，不能出现（.-）和（-.）。

        :param hostname: The hostname of this UpdateServerOption.
        :type hostname: str
        """
        self._hostname = hostname

    @property
    def user_data(self):
        """Gets the user_data of this UpdateServerOption.

        修改云服务器云主机过程中待注入实例自定义数据。支持注入文本、文本文件。  示例：  base64编码前：   Linux服务器：     #!/bin/bash     echo user_test > /home/user.txt   Windows服务器：     rem cmd     echo 111 > c:\\aaa.txt  base64编码后：   Linux服务器：IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA==   Windows服务器：cmVtIGNtZA0KZWNobyAxMTEgJmd0OyBjOlxhYWEudHh0

        :return: The user_data of this UpdateServerOption.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this UpdateServerOption.

        修改云服务器云主机过程中待注入实例自定义数据。支持注入文本、文本文件。  示例：  base64编码前：   Linux服务器：     #!/bin/bash     echo user_test > /home/user.txt   Windows服务器：     rem cmd     echo 111 > c:\\aaa.txt  base64编码后：   Linux服务器：IyEvYmluL2Jhc2gKZWNobyB1c2VyX3Rlc3QgPiAvaG9tZS91c2VyLnR4dA==   Windows服务器：cmVtIGNtZA0KZWNobyAxMTEgJmd0OyBjOlxhYWEudHh0

        :param user_data: The user_data of this UpdateServerOption.
        :type user_data: str
        """
        self._user_data = user_data

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
        if not isinstance(other, UpdateServerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
