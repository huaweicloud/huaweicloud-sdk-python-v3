# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateScriptReq:

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
        'content': 'str',
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'content': 'content',
        'version': 'version'
    }

    def __init__(self, name=None, description=None, content=None, version=None):
        r"""UpdateScriptReq

        The model defined in huaweicloud sdk

        :param name: 脚本名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param content: 脚本内容。
        :type content: str
        :param version: 脚本版本。
        :type version: str
        """
        
        

        self._name = None
        self._description = None
        self._content = None
        self._version = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.content = content
        if version is not None:
            self.version = version

    @property
    def name(self):
        r"""Gets the name of this UpdateScriptReq.

        脚本名称。

        :return: The name of this UpdateScriptReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateScriptReq.

        脚本名称。

        :param name: The name of this UpdateScriptReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateScriptReq.

        描述。

        :return: The description of this UpdateScriptReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateScriptReq.

        描述。

        :param description: The description of this UpdateScriptReq.
        :type description: str
        """
        self._description = description

    @property
    def content(self):
        r"""Gets the content of this UpdateScriptReq.

        脚本内容。

        :return: The content of this UpdateScriptReq.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this UpdateScriptReq.

        脚本内容。

        :param content: The content of this UpdateScriptReq.
        :type content: str
        """
        self._content = content

    @property
    def version(self):
        r"""Gets the version of this UpdateScriptReq.

        脚本版本。

        :return: The version of this UpdateScriptReq.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateScriptReq.

        脚本版本。

        :param version: The version of this UpdateScriptReq.
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
        if not isinstance(other, UpdateScriptReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
