# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionFileSnake:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'asset_type': 'str',
        'source': 'str'
    }

    attribute_map = {
        'asset_type': 'asset_type',
        'source': 'source'
    }

    def __init__(self, asset_type=None, source=None):
        r"""ExtensionFileSnake

        The model defined in huaweicloud sdk

        :param asset_type: 资源类型
        :type asset_type: str
        :param source: 资源地址
        :type source: str
        """
        
        

        self._asset_type = None
        self._source = None
        self.discriminator = None

        if asset_type is not None:
            self.asset_type = asset_type
        if source is not None:
            self.source = source

    @property
    def asset_type(self):
        r"""Gets the asset_type of this ExtensionFileSnake.

        资源类型

        :return: The asset_type of this ExtensionFileSnake.
        :rtype: str
        """
        return self._asset_type

    @asset_type.setter
    def asset_type(self, asset_type):
        r"""Sets the asset_type of this ExtensionFileSnake.

        资源类型

        :param asset_type: The asset_type of this ExtensionFileSnake.
        :type asset_type: str
        """
        self._asset_type = asset_type

    @property
    def source(self):
        r"""Gets the source of this ExtensionFileSnake.

        资源地址

        :return: The source of this ExtensionFileSnake.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ExtensionFileSnake.

        资源地址

        :param source: The source of this ExtensionFileSnake.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, ExtensionFileSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
