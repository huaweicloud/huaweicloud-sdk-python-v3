# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRedisPitrRestoreTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restore_time': 'list[str]',
        'total_count': 'int'
    }

    attribute_map = {
        'restore_time': 'restore_time',
        'total_count': 'total_count'
    }

    def __init__(self, restore_time=None, total_count=None):
        r"""ListRedisPitrRestoreTimeResponse

        The model defined in huaweicloud sdk

        :param restore_time: Redis可恢复时间点列表。 yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。
        :type restore_time: list[str]
        :param total_count: Redis实例可恢复时间点总数。
        :type total_count: int
        """
        
        super(ListRedisPitrRestoreTimeResponse, self).__init__()

        self._restore_time = None
        self._total_count = None
        self.discriminator = None

        if restore_time is not None:
            self.restore_time = restore_time
        if total_count is not None:
            self.total_count = total_count

    @property
    def restore_time(self):
        r"""Gets the restore_time of this ListRedisPitrRestoreTimeResponse.

        Redis可恢复时间点列表。 yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :return: The restore_time of this ListRedisPitrRestoreTimeResponse.
        :rtype: list[str]
        """
        return self._restore_time

    @restore_time.setter
    def restore_time(self, restore_time):
        r"""Sets the restore_time of this ListRedisPitrRestoreTimeResponse.

        Redis可恢复时间点列表。 yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :param restore_time: The restore_time of this ListRedisPitrRestoreTimeResponse.
        :type restore_time: list[str]
        """
        self._restore_time = restore_time

    @property
    def total_count(self):
        r"""Gets the total_count of this ListRedisPitrRestoreTimeResponse.

        Redis实例可恢复时间点总数。

        :return: The total_count of this ListRedisPitrRestoreTimeResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListRedisPitrRestoreTimeResponse.

        Redis实例可恢复时间点总数。

        :param total_count: The total_count of this ListRedisPitrRestoreTimeResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListRedisPitrRestoreTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
