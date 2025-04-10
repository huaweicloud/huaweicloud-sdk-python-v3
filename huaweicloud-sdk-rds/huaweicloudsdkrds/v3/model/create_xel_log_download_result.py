# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateXelLogDownloadResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file_name': 'str',
        'status': 'str',
        'file_size': 'str',
        'file_link': 'str',
        'create_at': 'str',
        'update_at': 'str'
    }

    attribute_map = {
        'file_name': 'file_name',
        'status': 'status',
        'file_size': 'file_size',
        'file_link': 'file_link',
        'create_at': 'create_at',
        'update_at': 'update_at'
    }

    def __init__(self, file_name=None, status=None, file_size=None, file_link=None, create_at=None, update_at=None):
        r"""CreateXelLogDownloadResult

        The model defined in huaweicloud sdk

        :param file_name: 下载文件名
        :type file_name: str
        :param status: 生成链接的生成状态。FINISH，表示下载链接已经生成完成。EXPORTING，，表示正在生成文件。FAILED，表示存在日志文件准备失败。
        :type status: str
        :param file_size: 日志大小，单位：KB
        :type file_size: str
        :param file_link: 下载链接,链接的生成状态为EXPORTING，或者FAILED不予返回
        :type file_link: str
        :param create_at: 生成时间
        :type create_at: str
        :param update_at: 更新时间
        :type update_at: str
        """
        
        

        self._file_name = None
        self._status = None
        self._file_size = None
        self._file_link = None
        self._create_at = None
        self._update_at = None
        self.discriminator = None

        self.file_name = file_name
        self.status = status
        self.file_size = file_size
        self.file_link = file_link
        self.create_at = create_at
        self.update_at = update_at

    @property
    def file_name(self):
        r"""Gets the file_name of this CreateXelLogDownloadResult.

        下载文件名

        :return: The file_name of this CreateXelLogDownloadResult.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this CreateXelLogDownloadResult.

        下载文件名

        :param file_name: The file_name of this CreateXelLogDownloadResult.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def status(self):
        r"""Gets the status of this CreateXelLogDownloadResult.

        生成链接的生成状态。FINISH，表示下载链接已经生成完成。EXPORTING，，表示正在生成文件。FAILED，表示存在日志文件准备失败。

        :return: The status of this CreateXelLogDownloadResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateXelLogDownloadResult.

        生成链接的生成状态。FINISH，表示下载链接已经生成完成。EXPORTING，，表示正在生成文件。FAILED，表示存在日志文件准备失败。

        :param status: The status of this CreateXelLogDownloadResult.
        :type status: str
        """
        self._status = status

    @property
    def file_size(self):
        r"""Gets the file_size of this CreateXelLogDownloadResult.

        日志大小，单位：KB

        :return: The file_size of this CreateXelLogDownloadResult.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this CreateXelLogDownloadResult.

        日志大小，单位：KB

        :param file_size: The file_size of this CreateXelLogDownloadResult.
        :type file_size: str
        """
        self._file_size = file_size

    @property
    def file_link(self):
        r"""Gets the file_link of this CreateXelLogDownloadResult.

        下载链接,链接的生成状态为EXPORTING，或者FAILED不予返回

        :return: The file_link of this CreateXelLogDownloadResult.
        :rtype: str
        """
        return self._file_link

    @file_link.setter
    def file_link(self, file_link):
        r"""Sets the file_link of this CreateXelLogDownloadResult.

        下载链接,链接的生成状态为EXPORTING，或者FAILED不予返回

        :param file_link: The file_link of this CreateXelLogDownloadResult.
        :type file_link: str
        """
        self._file_link = file_link

    @property
    def create_at(self):
        r"""Gets the create_at of this CreateXelLogDownloadResult.

        生成时间

        :return: The create_at of this CreateXelLogDownloadResult.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this CreateXelLogDownloadResult.

        生成时间

        :param create_at: The create_at of this CreateXelLogDownloadResult.
        :type create_at: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        r"""Gets the update_at of this CreateXelLogDownloadResult.

        更新时间

        :return: The update_at of this CreateXelLogDownloadResult.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        r"""Sets the update_at of this CreateXelLogDownloadResult.

        更新时间

        :param update_at: The update_at of this CreateXelLogDownloadResult.
        :type update_at: str
        """
        self._update_at = update_at

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
        if not isinstance(other, CreateXelLogDownloadResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
