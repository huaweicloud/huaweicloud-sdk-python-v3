# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskLogsContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'prefix': 'str',
        'time': 'str',
        'files': 'list[TaskLogFile]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'prefix': 'prefix',
        'time': 'time',
        'files': 'files'
    }

    def __init__(self, is_success=None, message=None, prefix=None, time=None, files=None):
        r"""TaskLogsContent

        The model defined in huaweicloud sdk

        :param is_success: 请求是否成功。
        :type is_success: bool
        :param message: 返回消息。
        :type message: str
        :param prefix: 日志路径前缀。
        :type prefix: str
        :param time: 日志时间。
        :type time: str
        :param files: 文件列表。
        :type files: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskLogFile`]
        """
        
        

        self._is_success = None
        self._message = None
        self._prefix = None
        self._time = None
        self._files = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if prefix is not None:
            self.prefix = prefix
        if time is not None:
            self.time = time
        if files is not None:
            self.files = files

    @property
    def is_success(self):
        r"""Gets the is_success of this TaskLogsContent.

        请求是否成功。

        :return: The is_success of this TaskLogsContent.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this TaskLogsContent.

        请求是否成功。

        :param is_success: The is_success of this TaskLogsContent.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this TaskLogsContent.

        返回消息。

        :return: The message of this TaskLogsContent.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this TaskLogsContent.

        返回消息。

        :param message: The message of this TaskLogsContent.
        :type message: str
        """
        self._message = message

    @property
    def prefix(self):
        r"""Gets the prefix of this TaskLogsContent.

        日志路径前缀。

        :return: The prefix of this TaskLogsContent.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this TaskLogsContent.

        日志路径前缀。

        :param prefix: The prefix of this TaskLogsContent.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def time(self):
        r"""Gets the time of this TaskLogsContent.

        日志时间。

        :return: The time of this TaskLogsContent.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this TaskLogsContent.

        日志时间。

        :param time: The time of this TaskLogsContent.
        :type time: str
        """
        self._time = time

    @property
    def files(self):
        r"""Gets the files of this TaskLogsContent.

        文件列表。

        :return: The files of this TaskLogsContent.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskLogFile`]
        """
        return self._files

    @files.setter
    def files(self, files):
        r"""Sets the files of this TaskLogsContent.

        文件列表。

        :param files: The files of this TaskLogsContent.
        :type files: list[:class:`huaweicloudsdkdataartsstudio.v1.TaskLogFile`]
        """
        self._files = files

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TaskLogsContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
