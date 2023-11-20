# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentVideoImageDetailSegments:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'segment': 'str'
    }

    attribute_map = {
        'segment': 'segment'
    }

    def __init__(self, segment=None):
        """DocumentVideoImageDetailSegments

        The model defined in huaweicloud sdk

        :param segment: 命中的风险片段
        :type segment: str
        """
        
        

        self._segment = None
        self.discriminator = None

        if segment is not None:
            self.segment = segment

    @property
    def segment(self):
        """Gets the segment of this DocumentVideoImageDetailSegments.

        命中的风险片段

        :return: The segment of this DocumentVideoImageDetailSegments.
        :rtype: str
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this DocumentVideoImageDetailSegments.

        命中的风险片段

        :param segment: The segment of this DocumentVideoImageDetailSegments.
        :type segment: str
        """
        self._segment = segment

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
        if not isinstance(other, DocumentVideoImageDetailSegments):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other