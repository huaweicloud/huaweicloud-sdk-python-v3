# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'install': 'int',
        'stars': 'float'
    }

    attribute_map = {
        'install': 'install',
        'stars': 'stars'
    }

    def __init__(self, install=None, stars=None):
        """ExtensionStatistics

        The model defined in huaweicloud sdk

        :param install: 下载量
        :type install: int
        :param stars: 评星
        :type stars: float
        """
        
        

        self._install = None
        self._stars = None
        self.discriminator = None

        if install is not None:
            self.install = install
        if stars is not None:
            self.stars = stars

    @property
    def install(self):
        """Gets the install of this ExtensionStatistics.

        下载量

        :return: The install of this ExtensionStatistics.
        :rtype: int
        """
        return self._install

    @install.setter
    def install(self, install):
        """Sets the install of this ExtensionStatistics.

        下载量

        :param install: The install of this ExtensionStatistics.
        :type install: int
        """
        self._install = install

    @property
    def stars(self):
        """Gets the stars of this ExtensionStatistics.

        评星

        :return: The stars of this ExtensionStatistics.
        :rtype: float
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this ExtensionStatistics.

        评星

        :param stars: The stars of this ExtensionStatistics.
        :type stars: float
        """
        self._stars = stars

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
        if not isinstance(other, ExtensionStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
