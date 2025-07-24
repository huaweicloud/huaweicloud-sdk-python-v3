# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHpcCacheTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'share_id': 'str',
        'type': 'str',
        'status': 'str',
        'offset': 'int',
        'limit': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'share_id': 'share_id',
        'type': 'type',
        'status': 'status',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, share_id=None, type=None, status=None, offset=None, limit=None, start_time=None, end_time=None):
        r"""ListHpcCacheTasksRequest

        The model defined in huaweicloud sdk

        :param share_id: 文件系统ID
        :type share_id: str
        :param type: 任务类型
        :type type: str
        :param status: 任务状态
        :type status: str
        :param offset: offset，默认值为 0
        :type offset: int
        :param limit: limit，默认值为 1000
        :type limit: int
        :param start_time: start_time
        :type start_time: str
        :param end_time: end_time
        :type end_time: str
        """
        
        

        self._share_id = None
        self._type = None
        self._status = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.share_id = share_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def share_id(self):
        r"""Gets the share_id of this ListHpcCacheTasksRequest.

        文件系统ID

        :return: The share_id of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._share_id

    @share_id.setter
    def share_id(self, share_id):
        r"""Sets the share_id of this ListHpcCacheTasksRequest.

        文件系统ID

        :param share_id: The share_id of this ListHpcCacheTasksRequest.
        :type share_id: str
        """
        self._share_id = share_id

    @property
    def type(self):
        r"""Gets the type of this ListHpcCacheTasksRequest.

        任务类型

        :return: The type of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListHpcCacheTasksRequest.

        任务类型

        :param type: The type of this ListHpcCacheTasksRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ListHpcCacheTasksRequest.

        任务状态

        :return: The status of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListHpcCacheTasksRequest.

        任务状态

        :param status: The status of this ListHpcCacheTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def offset(self):
        r"""Gets the offset of this ListHpcCacheTasksRequest.

        offset，默认值为 0

        :return: The offset of this ListHpcCacheTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHpcCacheTasksRequest.

        offset，默认值为 0

        :param offset: The offset of this ListHpcCacheTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHpcCacheTasksRequest.

        limit，默认值为 1000

        :return: The limit of this ListHpcCacheTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHpcCacheTasksRequest.

        limit，默认值为 1000

        :param limit: The limit of this ListHpcCacheTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ListHpcCacheTasksRequest.

        start_time

        :return: The start_time of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListHpcCacheTasksRequest.

        start_time

        :param start_time: The start_time of this ListHpcCacheTasksRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHpcCacheTasksRequest.

        end_time

        :return: The end_time of this ListHpcCacheTasksRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHpcCacheTasksRequest.

        end_time

        :param end_time: The end_time of this ListHpcCacheTasksRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListHpcCacheTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
