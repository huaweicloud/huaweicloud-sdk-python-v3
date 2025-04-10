# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailViewItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function': 'str',
        '_as': 'str'
    }

    attribute_map = {
        'function': 'function',
        '_as': 'as'
    }

    def __init__(self, function=None, _as=None):
        r"""DetailViewItem

        The model defined in huaweicloud sdk

        :param function: 表达式。
        :type function: str
        :param _as: 作为。
        :type _as: str
        """
        
        

        self._function = None
        self.__as = None
        self.discriminator = None

        if function is not None:
            self.function = function
        if _as is not None:
            self._as = _as

    @property
    def function(self):
        r"""Gets the function of this DetailViewItem.

        表达式。

        :return: The function of this DetailViewItem.
        :rtype: str
        """
        return self._function

    @function.setter
    def function(self, function):
        r"""Sets the function of this DetailViewItem.

        表达式。

        :param function: The function of this DetailViewItem.
        :type function: str
        """
        self._function = function

    @property
    def _as(self):
        r"""Gets the _as of this DetailViewItem.

        作为。

        :return: The _as of this DetailViewItem.
        :rtype: str
        """
        return self.__as

    @_as.setter
    def _as(self, _as):
        r"""Sets the _as of this DetailViewItem.

        作为。

        :param _as: The _as of this DetailViewItem.
        :type _as: str
        """
        self.__as = _as

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
        if not isinstance(other, DetailViewItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
