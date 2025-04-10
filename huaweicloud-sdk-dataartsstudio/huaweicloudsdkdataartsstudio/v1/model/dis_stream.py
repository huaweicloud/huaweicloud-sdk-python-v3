# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisStream:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'stream_guid': 'str',
        'stream_qualified_name': 'str',
        'partition_count': 'int',
        'app_count': 'int',
        'task_count': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'stream_guid': 'stream_guid',
        'stream_qualified_name': 'stream_qualified_name',
        'partition_count': 'partition_count',
        'app_count': 'app_count',
        'task_count': 'task_count'
    }

    def __init__(self, stream_name=None, stream_guid=None, stream_qualified_name=None, partition_count=None, app_count=None, task_count=None):
        r"""DisStream

        The model defined in huaweicloud sdk

        :param stream_name: 通道名称
        :type stream_name: str
        :param stream_guid: 通道GUID
        :type stream_guid: str
        :param stream_qualified_name: 通道的唯一标识名称
        :type stream_qualified_name: str
        :param partition_count: 分区数
        :type partition_count: int
        :param app_count: dis的app数目
        :type app_count: int
        :param task_count: 转储任务数
        :type task_count: int
        """
        
        

        self._stream_name = None
        self._stream_guid = None
        self._stream_qualified_name = None
        self._partition_count = None
        self._app_count = None
        self._task_count = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if stream_guid is not None:
            self.stream_guid = stream_guid
        if stream_qualified_name is not None:
            self.stream_qualified_name = stream_qualified_name
        if partition_count is not None:
            self.partition_count = partition_count
        if app_count is not None:
            self.app_count = app_count
        if task_count is not None:
            self.task_count = task_count

    @property
    def stream_name(self):
        r"""Gets the stream_name of this DisStream.

        通道名称

        :return: The stream_name of this DisStream.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this DisStream.

        通道名称

        :param stream_name: The stream_name of this DisStream.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def stream_guid(self):
        r"""Gets the stream_guid of this DisStream.

        通道GUID

        :return: The stream_guid of this DisStream.
        :rtype: str
        """
        return self._stream_guid

    @stream_guid.setter
    def stream_guid(self, stream_guid):
        r"""Sets the stream_guid of this DisStream.

        通道GUID

        :param stream_guid: The stream_guid of this DisStream.
        :type stream_guid: str
        """
        self._stream_guid = stream_guid

    @property
    def stream_qualified_name(self):
        r"""Gets the stream_qualified_name of this DisStream.

        通道的唯一标识名称

        :return: The stream_qualified_name of this DisStream.
        :rtype: str
        """
        return self._stream_qualified_name

    @stream_qualified_name.setter
    def stream_qualified_name(self, stream_qualified_name):
        r"""Sets the stream_qualified_name of this DisStream.

        通道的唯一标识名称

        :param stream_qualified_name: The stream_qualified_name of this DisStream.
        :type stream_qualified_name: str
        """
        self._stream_qualified_name = stream_qualified_name

    @property
    def partition_count(self):
        r"""Gets the partition_count of this DisStream.

        分区数

        :return: The partition_count of this DisStream.
        :rtype: int
        """
        return self._partition_count

    @partition_count.setter
    def partition_count(self, partition_count):
        r"""Sets the partition_count of this DisStream.

        分区数

        :param partition_count: The partition_count of this DisStream.
        :type partition_count: int
        """
        self._partition_count = partition_count

    @property
    def app_count(self):
        r"""Gets the app_count of this DisStream.

        dis的app数目

        :return: The app_count of this DisStream.
        :rtype: int
        """
        return self._app_count

    @app_count.setter
    def app_count(self, app_count):
        r"""Sets the app_count of this DisStream.

        dis的app数目

        :param app_count: The app_count of this DisStream.
        :type app_count: int
        """
        self._app_count = app_count

    @property
    def task_count(self):
        r"""Gets the task_count of this DisStream.

        转储任务数

        :return: The task_count of this DisStream.
        :rtype: int
        """
        return self._task_count

    @task_count.setter
    def task_count(self, task_count):
        r"""Sets the task_count of this DisStream.

        转储任务数

        :param task_count: The task_count of this DisStream.
        :type task_count: int
        """
        self._task_count = task_count

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
        if not isinstance(other, DisStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
