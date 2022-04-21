# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupRecordsRequest:

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
        'begin_time': 'str',
        'end_time': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, begin_time=None, end_time=None, limit=None, offset=None):
        """ListBackupRecordsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param begin_time: 查询开始时间，时间为UTC时间。格式：yyyyMMddHHmmss，如：20170718235959。
        :type begin_time: str
        :param end_time: 查询结束时间，时间为UTC时间。格式：yyyyMMddHHmmss，如：20170718235959。
        :type end_time: str
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._begin_time = None
        self._end_time = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ListBackupRecordsRequest.

        实例ID。

        :return: The instance_id of this ListBackupRecordsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListBackupRecordsRequest.

        实例ID。

        :param instance_id: The instance_id of this ListBackupRecordsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def begin_time(self):
        """Gets the begin_time of this ListBackupRecordsRequest.

        查询开始时间，时间为UTC时间。格式：yyyyMMddHHmmss，如：20170718235959。

        :return: The begin_time of this ListBackupRecordsRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ListBackupRecordsRequest.

        查询开始时间，时间为UTC时间。格式：yyyyMMddHHmmss，如：20170718235959。

        :param begin_time: The begin_time of this ListBackupRecordsRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        """Gets the end_time of this ListBackupRecordsRequest.

        查询结束时间，时间为UTC时间。格式：yyyyMMddHHmmss，如：20170718235959。

        :return: The end_time of this ListBackupRecordsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this ListBackupRecordsRequest.

        查询结束时间，时间为UTC时间。格式：yyyyMMddHHmmss，如：20170718235959。

        :param end_time: The end_time of this ListBackupRecordsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def limit(self):
        """Gets the limit of this ListBackupRecordsRequest.

        每页显示的条目数量。

        :return: The limit of this ListBackupRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListBackupRecordsRequest.

        每页显示的条目数量。

        :param limit: The limit of this ListBackupRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListBackupRecordsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :return: The offset of this ListBackupRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListBackupRecordsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0。

        :param offset: The offset of this ListBackupRecordsRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListBackupRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
