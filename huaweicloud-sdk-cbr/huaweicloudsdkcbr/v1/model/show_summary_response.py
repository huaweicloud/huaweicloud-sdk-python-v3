# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'used_size': 'int'
    }

    attribute_map = {
        'size': 'size',
        'used_size': 'used_size'
    }

    def __init__(self, size=None, used_size=None):
        r"""ShowSummaryResponse

        The model defined in huaweicloud sdk

        :param size: 总容量大小
        :type size: int
        :param used_size: 总使用量
        :type used_size: int
        """
        
        super(ShowSummaryResponse, self).__init__()

        self._size = None
        self._used_size = None
        self.discriminator = None

        if size is not None:
            self.size = size
        if used_size is not None:
            self.used_size = used_size

    @property
    def size(self):
        r"""Gets the size of this ShowSummaryResponse.

        总容量大小

        :return: The size of this ShowSummaryResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ShowSummaryResponse.

        总容量大小

        :param size: The size of this ShowSummaryResponse.
        :type size: int
        """
        self._size = size

    @property
    def used_size(self):
        r"""Gets the used_size of this ShowSummaryResponse.

        总使用量

        :return: The used_size of this ShowSummaryResponse.
        :rtype: int
        """
        return self._used_size

    @used_size.setter
    def used_size(self, used_size):
        r"""Sets the used_size of this ShowSummaryResponse.

        总使用量

        :param used_size: The used_size of this ShowSummaryResponse.
        :type used_size: int
        """
        self._used_size = used_size

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
        if not isinstance(other, ShowSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
