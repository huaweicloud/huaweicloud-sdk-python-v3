# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreSplitKeyOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'range_split_points': 'list[dict]'
    }

    attribute_map = {
        'range_split_points': 'range_split_points'
    }

    def __init__(self, range_split_points=None):
        r"""PreSplitKeyOptions

        The model defined in huaweicloud sdk

        :param range_split_points: 在range分区模式有效，最大10个。
        :type range_split_points: list[dict]
        """
        
        

        self._range_split_points = None
        self.discriminator = None

        if range_split_points is not None:
            self.range_split_points = range_split_points

    @property
    def range_split_points(self):
        r"""Gets the range_split_points of this PreSplitKeyOptions.

        在range分区模式有效，最大10个。

        :return: The range_split_points of this PreSplitKeyOptions.
        :rtype: list[dict]
        """
        return self._range_split_points

    @range_split_points.setter
    def range_split_points(self, range_split_points):
        r"""Sets the range_split_points of this PreSplitKeyOptions.

        在range分区模式有效，最大10个。

        :param range_split_points: The range_split_points of this PreSplitKeyOptions.
        :type range_split_points: list[dict]
        """
        self._range_split_points = range_split_points

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
        if not isinstance(other, PreSplitKeyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
