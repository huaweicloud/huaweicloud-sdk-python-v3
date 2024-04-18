# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceLogFile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'file_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'file_size': 'str',
        'file_link': 'str'
    }

    attribute_map = {
        'status': 'status',
        'file_name': 'file_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'file_size': 'file_size',
        'file_link': 'file_link'
    }

    def __init__(self, status=None, file_name=None, start_time=None, end_time=None, file_size=None, file_link=None):
        """InstanceLogFile

        The model defined in huaweicloud sdk

        :param status: 日志采集状态。
        :type status: str
        :param file_name: 日志文件名称。
        :type file_name: str
        :param start_time: 日志开始时间。
        :type start_time: str
        :param end_time: 日志结束时间。
        :type end_time: str
        :param file_size: 日志文件大小，单位kb。
        :type file_size: str
        :param file_link: 日志文件下载链接。
        :type file_link: str
        """
        
        

        self._status = None
        self._file_name = None
        self._start_time = None
        self._end_time = None
        self._file_size = None
        self._file_link = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if file_name is not None:
            self.file_name = file_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if file_size is not None:
            self.file_size = file_size
        if file_link is not None:
            self.file_link = file_link

    @property
    def status(self):
        """Gets the status of this InstanceLogFile.

        日志采集状态。

        :return: The status of this InstanceLogFile.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InstanceLogFile.

        日志采集状态。

        :param status: The status of this InstanceLogFile.
        :type status: str
        """
        self._status = status

    @property
    def file_name(self):
        """Gets the file_name of this InstanceLogFile.

        日志文件名称。

        :return: The file_name of this InstanceLogFile.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this InstanceLogFile.

        日志文件名称。

        :param file_name: The file_name of this InstanceLogFile.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def start_time(self):
        """Gets the start_time of this InstanceLogFile.

        日志开始时间。

        :return: The start_time of this InstanceLogFile.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InstanceLogFile.

        日志开始时间。

        :param start_time: The start_time of this InstanceLogFile.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InstanceLogFile.

        日志结束时间。

        :return: The end_time of this InstanceLogFile.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InstanceLogFile.

        日志结束时间。

        :param end_time: The end_time of this InstanceLogFile.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def file_size(self):
        """Gets the file_size of this InstanceLogFile.

        日志文件大小，单位kb。

        :return: The file_size of this InstanceLogFile.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this InstanceLogFile.

        日志文件大小，单位kb。

        :param file_size: The file_size of this InstanceLogFile.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        """Gets the file_link of this InstanceLogFile.

        日志文件下载链接。

        :return: The file_link of this InstanceLogFile.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        """Sets the file_link of this InstanceLogFile.

        日志文件下载链接。

        :param file_link: The file_link of this InstanceLogFile.
        :type file_link: str
        """
        self._file_link = file_link

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
        if not isinstance(other, InstanceLogFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
