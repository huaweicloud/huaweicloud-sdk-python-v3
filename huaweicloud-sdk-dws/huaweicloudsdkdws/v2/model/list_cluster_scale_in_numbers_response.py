# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterScaleInNumbersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shrink_sequence': 'list[str]'
    }

    attribute_map = {
        'shrink_sequence': 'shrink_sequence'
    }

    def __init__(self, shrink_sequence=None):
        """ListClusterScaleInNumbersResponse

        The model defined in huaweicloud sdk

        :param shrink_sequence: 合适的缩容数
        :type shrink_sequence: list[str]
        """
        
        super(ListClusterScaleInNumbersResponse, self).__init__()

        self._shrink_sequence = None
        self.discriminator = None

        if shrink_sequence is not None:
            self.shrink_sequence = shrink_sequence

    @property
    def shrink_sequence(self):
        """Gets the shrink_sequence of this ListClusterScaleInNumbersResponse.

        合适的缩容数

        :return: The shrink_sequence of this ListClusterScaleInNumbersResponse.
        :rtype: list[str]
        """
        return self._shrink_sequence

    @shrink_sequence.setter
    def shrink_sequence(self, shrink_sequence):
        """Sets the shrink_sequence of this ListClusterScaleInNumbersResponse.

        合适的缩容数

        :param shrink_sequence: The shrink_sequence of this ListClusterScaleInNumbersResponse.
        :type shrink_sequence: list[str]
        """
        self._shrink_sequence = shrink_sequence

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
        if not isinstance(other, ListClusterScaleInNumbersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
