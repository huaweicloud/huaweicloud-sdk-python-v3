# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyDepends:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'catalog': 'catalog',
        'display_name': 'display_name'
    }

    def __init__(self, catalog=None, display_name=None):
        r"""PolicyDepends

        The model defined in huaweicloud sdk

        :param catalog: 权限所在目录。
        :type catalog: str
        :param display_name: 权限展示名。
        :type display_name: str
        """
        
        

        self._catalog = None
        self._display_name = None
        self.discriminator = None

        self.catalog = catalog
        self.display_name = display_name

    @property
    def catalog(self):
        r"""Gets the catalog of this PolicyDepends.

        权限所在目录。

        :return: The catalog of this PolicyDepends.
        :rtype: str
        """
        return self._catalog

    @catalog.setter
    def catalog(self, catalog):
        r"""Sets the catalog of this PolicyDepends.

        权限所在目录。

        :param catalog: The catalog of this PolicyDepends.
        :type catalog: str
        """
        self._catalog = catalog

    @property
    def display_name(self):
        r"""Gets the display_name of this PolicyDepends.

        权限展示名。

        :return: The display_name of this PolicyDepends.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this PolicyDepends.

        权限展示名。

        :param display_name: The display_name of this PolicyDepends.
        :type display_name: str
        """
        self._display_name = display_name

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
        if not isinstance(other, PolicyDepends):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
