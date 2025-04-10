# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadSlowLogFileItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'file_name': 'str',
        'status': 'str',
        'file_size': 'str',
        'file_link': 'str',
        'create_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'file_name': 'file_name',
        'status': 'status',
        'file_size': 'file_size',
        'file_link': 'file_link',
        'create_at': 'create_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, job_id=None, file_name=None, status=None, file_size=None, file_link=None, create_at=None, updated_at=None):
        r"""DownloadSlowLogFileItem

        The model defined in huaweicloud sdk

        :param job_id: 任务ID。
        :type job_id: str
        :param file_name: 文件名。
        :type file_name: str
        :param status: 状态。  取值范围:   - SUCCESS：表示下载链接已经生成完成。   - EXPORTING：表示下载链接正在生成中。   - FAILED： 表示下载链接生成失败。
        :type status: str
        :param file_size: 文件大小，单位：KB。
        :type file_size: str
        :param file_link: 下载链接。链接有效时间为5分钟。
        :type file_link: str
        :param create_at: 创建时间。
        :type create_at: int
        :param updated_at: 更新时间。
        :type updated_at: int
        """
        
        

        self._job_id = None
        self._file_name = None
        self._status = None
        self._file_size = None
        self._file_link = None
        self._create_at = None
        self._updated_at = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if file_name is not None:
            self.file_name = file_name
        if status is not None:
            self.status = status
        if file_size is not None:
            self.file_size = file_size
        if file_link is not None:
            self.file_link = file_link
        if create_at is not None:
            self.create_at = create_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def job_id(self):
        r"""Gets the job_id of this DownloadSlowLogFileItem.

        任务ID。

        :return: The job_id of this DownloadSlowLogFileItem.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DownloadSlowLogFileItem.

        任务ID。

        :param job_id: The job_id of this DownloadSlowLogFileItem.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def file_name(self):
        r"""Gets the file_name of this DownloadSlowLogFileItem.

        文件名。

        :return: The file_name of this DownloadSlowLogFileItem.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this DownloadSlowLogFileItem.

        文件名。

        :param file_name: The file_name of this DownloadSlowLogFileItem.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def status(self):
        r"""Gets the status of this DownloadSlowLogFileItem.

        状态。  取值范围:   - SUCCESS：表示下载链接已经生成完成。   - EXPORTING：表示下载链接正在生成中。   - FAILED： 表示下载链接生成失败。

        :return: The status of this DownloadSlowLogFileItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DownloadSlowLogFileItem.

        状态。  取值范围:   - SUCCESS：表示下载链接已经生成完成。   - EXPORTING：表示下载链接正在生成中。   - FAILED： 表示下载链接生成失败。

        :param status: The status of this DownloadSlowLogFileItem.
        :type status: str
        """
        self._status = status

    @property
    def file_size(self):
        r"""Gets the file_size of this DownloadSlowLogFileItem.

        文件大小，单位：KB。

        :return: The file_size of this DownloadSlowLogFileItem.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this DownloadSlowLogFileItem.

        文件大小，单位：KB。

        :param file_size: The file_size of this DownloadSlowLogFileItem.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        r"""Gets the file_link of this DownloadSlowLogFileItem.

        下载链接。链接有效时间为5分钟。

        :return: The file_link of this DownloadSlowLogFileItem.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        r"""Sets the file_link of this DownloadSlowLogFileItem.

        下载链接。链接有效时间为5分钟。

        :param file_link: The file_link of this DownloadSlowLogFileItem.
        :type file_link: str
        """
        self._file_link = file_link

    @property
    def create_at(self):
        r"""Gets the create_at of this DownloadSlowLogFileItem.

        创建时间。

        :return: The create_at of this DownloadSlowLogFileItem.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this DownloadSlowLogFileItem.

        创建时间。

        :param create_at: The create_at of this DownloadSlowLogFileItem.
        :type create_at: int
        """
        self._create_at = create_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this DownloadSlowLogFileItem.

        更新时间。

        :return: The updated_at of this DownloadSlowLogFileItem.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this DownloadSlowLogFileItem.

        更新时间。

        :param updated_at: The updated_at of this DownloadSlowLogFileItem.
        :type updated_at: int
        """
        self._updated_at = updated_at

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
        if not isinstance(other, DownloadSlowLogFileItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
