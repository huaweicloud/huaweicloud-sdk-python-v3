# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviousMarker:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'previous_marker': 'str'
    }

    attribute_map = {
        'previous_marker': 'previous_marker'
    }

    def __init__(self, previous_marker=None):
        """PreviousMarker

        The model defined in huaweicloud sdk

        :param previous_marker: 向前分页标识符。
        :type previous_marker: str
        """
        
        

        self._previous_marker = None
        self.discriminator = None

        if previous_marker is not None:
            self.previous_marker = previous_marker

    @property
    def previous_marker(self):
        """Gets the previous_marker of this PreviousMarker.

        向前分页标识符。

        :return: The previous_marker of this PreviousMarker.
        :rtype: str
        """
        return self._previous_marker

    @previous_marker.setter
    def previous_marker(self, previous_marker):
        """Sets the previous_marker of this PreviousMarker.

        向前分页标识符。

        :param previous_marker: The previous_marker of this PreviousMarker.
        :type previous_marker: str
        """
        self._previous_marker = previous_marker

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
        if not isinstance(other, PreviousMarker):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
