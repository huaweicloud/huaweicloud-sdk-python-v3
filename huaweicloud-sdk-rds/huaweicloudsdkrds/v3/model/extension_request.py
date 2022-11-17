# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'extension_name': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'extension_name': 'extension_name'
    }

    def __init__(self, database_name=None, extension_name=None):
        """ExtensionRequest

        The model defined in huaweicloud sdk

        :param database_name: 数据库名称。
        :type database_name: str
        :param extension_name: 插件名称。
        :type extension_name: str
        """
        
        

        self._database_name = None
        self._extension_name = None
        self.discriminator = None

        self.database_name = database_name
        self.extension_name = extension_name

    @property
    def database_name(self):
        """Gets the database_name of this ExtensionRequest.

        数据库名称。

        :return: The database_name of this ExtensionRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this ExtensionRequest.

        数据库名称。

        :param database_name: The database_name of this ExtensionRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def extension_name(self):
        """Gets the extension_name of this ExtensionRequest.

        插件名称。

        :return: The extension_name of this ExtensionRequest.
        :rtype: str
        """
        return self._extension_name

    @extension_name.setter
    def extension_name(self, extension_name):
        """Sets the extension_name of this ExtensionRequest.

        插件名称。

        :param extension_name: The extension_name of this ExtensionRequest.
        :type extension_name: str
        """
        self._extension_name = extension_name

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
        if not isinstance(other, ExtensionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
