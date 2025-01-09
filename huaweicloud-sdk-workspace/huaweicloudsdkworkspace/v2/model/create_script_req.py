# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateScriptReq:

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
        'type': 'str',
        'description': 'str',
        'content': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'description': 'description',
        'content': 'content',
        'version': 'version'
    }

    def __init__(self, name=None, type=None, description=None, content=None, version=None):
        """CreateScriptReq

        The model defined in huaweicloud sdk

        :param name: 脚本名称。
        :type name: str
        :param type: 脚本类型：POWERSHELL/BAT/SHELL。
        :type type: str
        :param description: 描述。
        :type description: str
        :param content: 脚本内容。
        :type content: str
        :param version: 脚本版本。
        :type version: str
        """
        
        

        self._name = None
        self._type = None
        self._description = None
        self._content = None
        self._version = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if description is not None:
            self.description = description
        if content is not None:
            self.content = content
        if version is not None:
            self.version = version

    @property
    def name(self):
        """Gets the name of this CreateScriptReq.

        脚本名称。

        :return: The name of this CreateScriptReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateScriptReq.

        脚本名称。

        :param name: The name of this CreateScriptReq.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this CreateScriptReq.

        脚本类型：POWERSHELL/BAT/SHELL。

        :return: The type of this CreateScriptReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateScriptReq.

        脚本类型：POWERSHELL/BAT/SHELL。

        :param type: The type of this CreateScriptReq.
        :type type: str
        """
        self._type = type

    @property
    def description(self):
        """Gets the description of this CreateScriptReq.

        描述。

        :return: The description of this CreateScriptReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateScriptReq.

        描述。

        :param description: The description of this CreateScriptReq.
        :type description: str
        """
        self._description = description

    @property
    def content(self):
        """Gets the content of this CreateScriptReq.

        脚本内容。

        :return: The content of this CreateScriptReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateScriptReq.

        脚本内容。

        :param content: The content of this CreateScriptReq.
        :type content: str
        """
        self._content = content

    @property
    def version(self):
        """Gets the version of this CreateScriptReq.

        脚本版本。

        :return: The version of this CreateScriptReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateScriptReq.

        脚本版本。

        :param version: The version of this CreateScriptReq.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, CreateScriptReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
