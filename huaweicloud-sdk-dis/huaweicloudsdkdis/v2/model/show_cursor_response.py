# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCursorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition_cursor': 'str'
    }

    attribute_map = {
        'partition_cursor': 'partition_cursor'
    }

    def __init__(self, partition_cursor=None):
        r"""ShowCursorResponse

        The model defined in huaweicloud sdk

        :param partition_cursor: 数据游标。  取值范围：1~512个字符。  说明：  数据游标有效期为5分钟。
        :type partition_cursor: str
        """
        
        super(ShowCursorResponse, self).__init__()

        self._partition_cursor = None
        self.discriminator = None

        if partition_cursor is not None:
            self.partition_cursor = partition_cursor

    @property
    def partition_cursor(self):
        r"""Gets the partition_cursor of this ShowCursorResponse.

        数据游标。  取值范围：1~512个字符。  说明：  数据游标有效期为5分钟。

        :return: The partition_cursor of this ShowCursorResponse.
        :rtype: str
        """
        return self._partition_cursor

    @partition_cursor.setter
    def partition_cursor(self, partition_cursor):
        r"""Sets the partition_cursor of this ShowCursorResponse.

        数据游标。  取值范围：1~512个字符。  说明：  数据游标有效期为5分钟。

        :param partition_cursor: The partition_cursor of this ShowCursorResponse.
        :type partition_cursor: str
        """
        self._partition_cursor = partition_cursor

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
        if not isinstance(other, ShowCursorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
