# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PluginExtensions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'extension_name': 'extension_name',
        'status': 'status'
    }

    def __init__(self, extension_name=None, status=None):
        r"""PluginExtensions

        The model defined in huaweicloud sdk

        :param extension_name: 拓展名称
        :type extension_name: str
        :param status: 拓展状态。on表示开启，off表示关闭。
        :type status: str
        """
        
        

        self._extension_name = None
        self._status = None
        self.discriminator = None

        if extension_name is not None:
            self.extension_name = extension_name
        if status is not None:
            self.status = status

    @property
    def extension_name(self):
        r"""Gets the extension_name of this PluginExtensions.

        拓展名称

        :return: The extension_name of this PluginExtensions.
        :rtype: str
        """
        return self._extension_name

    @extension_name.setter
    def extension_name(self, extension_name):
        r"""Sets the extension_name of this PluginExtensions.

        拓展名称

        :param extension_name: The extension_name of this PluginExtensions.
        :type extension_name: str
        """
        self._extension_name = extension_name

    @property
    def status(self):
        r"""Gets the status of this PluginExtensions.

        拓展状态。on表示开启，off表示关闭。

        :return: The status of this PluginExtensions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PluginExtensions.

        拓展状态。on表示开启，off表示关闭。

        :param status: The status of this PluginExtensions.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, PluginExtensions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
