# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workflow_id': 'str',
        'file_name': 'str',
        'status': 'str',
        'file_size': 'str',
        'file_link': 'str',
        'file_link_expiration_time': 'int',
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'file_name': 'file_name',
        'status': 'status',
        'file_size': 'file_size',
        'file_link': 'file_link',
        'file_link_expiration_time': 'file_link_expiration_time',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, workflow_id=None, file_name=None, status=None, file_size=None, file_link=None, file_link_expiration_time=None, start_time=None, end_time=None):
        r"""DownloadInfo

        The model defined in huaweicloud sdk

        :param workflow_id: 参数解释： 任务ID。 取值范围： 不涉及。
        :type workflow_id: str
        :param file_name: 参数解释： 生成的下载文件名。 取值范围： 不涉及。
        :type file_name: str
        :param status: 参数解释： 当前链接的生成状态。 取值范围： 不涉及。
        :type status: str
        :param file_size: 参数解释： 文件大小。单位Byte 取值范围： 不涉及。
        :type file_size: str
        :param file_link: 参数解释： 下载链接。 取值范围： 不涉及。
        :type file_link: str
        :param file_link_expiration_time: 下载链接过期时间
        :type file_link_expiration_time: int
        :param start_time: 参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。
        :type start_time: int
        :param end_time: 参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。
        :type end_time: int
        """
        
        

        self._workflow_id = None
        self._file_name = None
        self._status = None
        self._file_size = None
        self._file_link = None
        self._file_link_expiration_time = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if file_name is not None:
            self.file_name = file_name
        if status is not None:
            self.status = status
        if file_size is not None:
            self.file_size = file_size
        if file_link is not None:
            self.file_link = file_link
        if file_link_expiration_time is not None:
            self.file_link_expiration_time = file_link_expiration_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def workflow_id(self):
        r"""Gets the workflow_id of this DownloadInfo.

        参数解释： 任务ID。 取值范围： 不涉及。

        :return: The workflow_id of this DownloadInfo.
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        r"""Sets the workflow_id of this DownloadInfo.

        参数解释： 任务ID。 取值范围： 不涉及。

        :param workflow_id: The workflow_id of this DownloadInfo.
        :type workflow_id: str
        """
        self._workflow_id = workflow_id

    @property
    def file_name(self):
        r"""Gets the file_name of this DownloadInfo.

        参数解释： 生成的下载文件名。 取值范围： 不涉及。

        :return: The file_name of this DownloadInfo.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DownloadInfo.

        参数解释： 生成的下载文件名。 取值范围： 不涉及。

        :param file_name: The file_name of this DownloadInfo.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def status(self):
        r"""Gets the status of this DownloadInfo.

        参数解释： 当前链接的生成状态。 取值范围： 不涉及。

        :return: The status of this DownloadInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DownloadInfo.

        参数解释： 当前链接的生成状态。 取值范围： 不涉及。

        :param status: The status of this DownloadInfo.
        :type status: str
        """
        self._status = status

    @property
    def file_size(self):
        r"""Gets the file_size of this DownloadInfo.

        参数解释： 文件大小。单位Byte 取值范围： 不涉及。

        :return: The file_size of this DownloadInfo.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this DownloadInfo.

        参数解释： 文件大小。单位Byte 取值范围： 不涉及。

        :param file_size: The file_size of this DownloadInfo.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        r"""Gets the file_link of this DownloadInfo.

        参数解释： 下载链接。 取值范围： 不涉及。

        :return: The file_link of this DownloadInfo.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        r"""Sets the file_link of this DownloadInfo.

        参数解释： 下载链接。 取值范围： 不涉及。

        :param file_link: The file_link of this DownloadInfo.
        :type file_link: str
        """
        self._file_link = file_link

    @property
    def file_link_expiration_time(self):
        r"""Gets the file_link_expiration_time of this DownloadInfo.

        下载链接过期时间

        :return: The file_link_expiration_time of this DownloadInfo.
        :rtype: int
        """
        return self._file_link_expiration_time

    @file_link_expiration_time.setter
    def file_link_expiration_time(self, file_link_expiration_time):
        r"""Sets the file_link_expiration_time of this DownloadInfo.

        下载链接过期时间

        :param file_link_expiration_time: The file_link_expiration_time of this DownloadInfo.
        :type file_link_expiration_time: int
        """
        self._file_link_expiration_time = file_link_expiration_time

    @property
    def start_time(self):
        r"""Gets the start_time of this DownloadInfo.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。

        :return: The start_time of this DownloadInfo.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this DownloadInfo.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。

        :param start_time: The start_time of this DownloadInfo.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this DownloadInfo.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。

        :return: The end_time of this DownloadInfo.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this DownloadInfo.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。

        :param end_time: The end_time of this DownloadInfo.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, DownloadInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
