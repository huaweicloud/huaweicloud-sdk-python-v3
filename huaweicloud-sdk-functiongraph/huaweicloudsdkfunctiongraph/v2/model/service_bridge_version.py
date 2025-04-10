# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceBridgeVersion:

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
        'version': 'str',
        'code_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'code_url': 'code_url'
    }

    def __init__(self, name=None, version=None, code_url=None):
        r"""ServiceBridgeVersion

        The model defined in huaweicloud sdk

        :param name: 代码包名
        :type name: str
        :param version: 代码版本
        :type version: str
        :param code_url: 代码所在obs路径
        :type code_url: str
        """
        
        

        self._name = None
        self._version = None
        self._code_url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if code_url is not None:
            self.code_url = code_url

    @property
    def name(self):
        r"""Gets the name of this ServiceBridgeVersion.

        代码包名

        :return: The name of this ServiceBridgeVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ServiceBridgeVersion.

        代码包名

        :param name: The name of this ServiceBridgeVersion.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ServiceBridgeVersion.

        代码版本

        :return: The version of this ServiceBridgeVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ServiceBridgeVersion.

        代码版本

        :param version: The version of this ServiceBridgeVersion.
        :type version: str
        """
        self._version = version

    @property
    def code_url(self):
        r"""Gets the code_url of this ServiceBridgeVersion.

        代码所在obs路径

        :return: The code_url of this ServiceBridgeVersion.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        r"""Sets the code_url of this ServiceBridgeVersion.

        代码所在obs路径

        :param code_url: The code_url of this ServiceBridgeVersion.
        :type code_url: str
        """
        self._code_url = code_url

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
        if not isinstance(other, ServiceBridgeVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
