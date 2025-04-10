# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReturnedSegmentItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'segment_min_key': 'dict',
        'segment_max_key': 'dict'
    }

    attribute_map = {
        'segment_min_key': 'segment_min_key',
        'segment_max_key': 'segment_max_key'
    }

    def __init__(self, segment_min_key=None, segment_max_key=None):
        r"""ReturnedSegmentItem

        The model defined in huaweicloud sdk

        :param segment_min_key: 采样段区间起始值。
        :type segment_min_key: dict
        :param segment_max_key: 采样段区间终止值。
        :type segment_max_key: dict
        """
        
        

        self._segment_min_key = None
        self._segment_max_key = None
        self.discriminator = None

        if segment_min_key is not None:
            self.segment_min_key = segment_min_key
        if segment_max_key is not None:
            self.segment_max_key = segment_max_key

    @property
    def segment_min_key(self):
        r"""Gets the segment_min_key of this ReturnedSegmentItem.

        采样段区间起始值。

        :return: The segment_min_key of this ReturnedSegmentItem.
        :rtype: dict
        """
        return self._segment_min_key

    @segment_min_key.setter
    def segment_min_key(self, segment_min_key):
        r"""Sets the segment_min_key of this ReturnedSegmentItem.

        采样段区间起始值。

        :param segment_min_key: The segment_min_key of this ReturnedSegmentItem.
        :type segment_min_key: dict
        """
        self._segment_min_key = segment_min_key

    @property
    def segment_max_key(self):
        r"""Gets the segment_max_key of this ReturnedSegmentItem.

        采样段区间终止值。

        :return: The segment_max_key of this ReturnedSegmentItem.
        :rtype: dict
        """
        return self._segment_max_key

    @segment_max_key.setter
    def segment_max_key(self, segment_max_key):
        r"""Sets the segment_max_key of this ReturnedSegmentItem.

        采样段区间终止值。

        :param segment_max_key: The segment_max_key of this ReturnedSegmentItem.
        :type segment_max_key: dict
        """
        self._segment_max_key = segment_max_key

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
        if not isinstance(other, ReturnedSegmentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
