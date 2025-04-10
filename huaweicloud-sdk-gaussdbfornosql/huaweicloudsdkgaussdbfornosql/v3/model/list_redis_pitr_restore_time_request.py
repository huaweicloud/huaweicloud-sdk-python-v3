# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRedisPitrRestoreTimeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, start_time=None, end_time=None, offset=None, limit=None):
        r"""ListRedisPitrRestoreTimeRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param start_time: 查询可恢复时间点的开始时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。
        :type start_time: str
        :param end_time: 查询可恢复时间点的结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。
        :type end_time: str
        :param offset: 偏移量，表示查询该偏移量后面的记录，默认值为0。
        :type offset: int
        :param limit: 查询返回记录的数量上限值，取值范围为1~100，默认值为100。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListRedisPitrRestoreTimeRequest.

        实例ID。

        :return: The instance_id of this ListRedisPitrRestoreTimeRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListRedisPitrRestoreTimeRequest.

        实例ID。

        :param instance_id: The instance_id of this ListRedisPitrRestoreTimeRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListRedisPitrRestoreTimeRequest.

        查询可恢复时间点的开始时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :return: The start_time of this ListRedisPitrRestoreTimeRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListRedisPitrRestoreTimeRequest.

        查询可恢复时间点的开始时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :param start_time: The start_time of this ListRedisPitrRestoreTimeRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListRedisPitrRestoreTimeRequest.

        查询可恢复时间点的结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :return: The end_time of this ListRedisPitrRestoreTimeRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListRedisPitrRestoreTimeRequest.

        查询可恢复时间点的结束时间，为yyyy-mm-ddThh:mm:ssZ字符串格式，T指某个时间的开始，Z指时区偏移量。

        :param end_time: The end_time of this ListRedisPitrRestoreTimeRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListRedisPitrRestoreTimeRequest.

        偏移量，表示查询该偏移量后面的记录，默认值为0。

        :return: The offset of this ListRedisPitrRestoreTimeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRedisPitrRestoreTimeRequest.

        偏移量，表示查询该偏移量后面的记录，默认值为0。

        :param offset: The offset of this ListRedisPitrRestoreTimeRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRedisPitrRestoreTimeRequest.

        查询返回记录的数量上限值，取值范围为1~100，默认值为100。

        :return: The limit of this ListRedisPitrRestoreTimeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRedisPitrRestoreTimeRequest.

        查询返回记录的数量上限值，取值范围为1~100，默认值为100。

        :param limit: The limit of this ListRedisPitrRestoreTimeRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRedisPitrRestoreTimeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
