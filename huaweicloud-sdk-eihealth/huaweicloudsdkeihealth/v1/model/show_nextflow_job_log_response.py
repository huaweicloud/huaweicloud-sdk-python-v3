# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNextflowJobLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'logs': 'list[str]',
        'download_url': 'str'
    }

    attribute_map = {
        'count': 'count',
        'logs': 'logs',
        'download_url': 'download_url'
    }

    def __init__(self, count=None, logs=None, download_url=None):
        r"""ShowNextflowJobLogResponse

        The model defined in huaweicloud sdk

        :param count: 作业日志条数
        :type count: int
        :param logs: 日志内容列表
        :type logs: list[str]
        :param download_url: 日志下载链接
        :type download_url: str
        """
        
        super(ShowNextflowJobLogResponse, self).__init__()

        self._count = None
        self._logs = None
        self._download_url = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if logs is not None:
            self.logs = logs
        if download_url is not None:
            self.download_url = download_url

    @property
    def count(self):
        r"""Gets the count of this ShowNextflowJobLogResponse.

        作业日志条数

        :return: The count of this ShowNextflowJobLogResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowNextflowJobLogResponse.

        作业日志条数

        :param count: The count of this ShowNextflowJobLogResponse.
        :type count: int
        """
        self._count = count

    @property
    def logs(self):
        r"""Gets the logs of this ShowNextflowJobLogResponse.

        日志内容列表

        :return: The logs of this ShowNextflowJobLogResponse.
        :rtype: list[str]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this ShowNextflowJobLogResponse.

        日志内容列表

        :param logs: The logs of this ShowNextflowJobLogResponse.
        :type logs: list[str]
        """
        self._logs = logs

    @property
    def download_url(self):
        r"""Gets the download_url of this ShowNextflowJobLogResponse.

        日志下载链接

        :return: The download_url of this ShowNextflowJobLogResponse.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this ShowNextflowJobLogResponse.

        日志下载链接

        :param download_url: The download_url of this ShowNextflowJobLogResponse.
        :type download_url: str
        """
        self._download_url = download_url

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
        if not isinstance(other, ShowNextflowJobLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
