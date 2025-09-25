# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAspResult:

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
        'file_size': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'download_url': 'str',
        'status': 'str'
    }

    attribute_map = {
        'job_id': 'job_id',
        'file_size': 'file_size',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'download_url': 'download_url',
        'status': 'status'
    }

    def __init__(self, job_id=None, file_size=None, start_time=None, end_time=None, download_url=None, status=None):
        r"""ListAspResult

        The model defined in huaweicloud sdk

        :param job_id: **参数解释**: 任务ID。 **取值范围**: 不涉及。
        :type job_id: str
        :param file_size: **参数解释**: 文件大小单位KB。 **取值范围**: 当status为SUCCESS时，该值不为空。
        :type file_size: int
        :param start_time: **参数解释**: 开始采集时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type start_time: str
        :param end_time: **参数解释**: 结束采集时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。
        :type end_time: str
        :param download_url: **参数解释**: 报告下载链接，有效时间为30分钟。 **取值范围**: 当status为SUCCESS时，该值不为空。
        :type download_url: str
        :param status: **参数解释**: 采集状态。 **取值范围**: - SUCCESS：成功。 - FAILED：失败。 - EXPORTING：采集中。
        :type status: str
        """
        
        

        self._job_id = None
        self._file_size = None
        self._start_time = None
        self._end_time = None
        self._download_url = None
        self._status = None
        self.discriminator = None

        self.job_id = job_id
        if file_size is not None:
            self.file_size = file_size
        self.start_time = start_time
        self.end_time = end_time
        if download_url is not None:
            self.download_url = download_url
        self.status = status

    @property
    def job_id(self):
        r"""Gets the job_id of this ListAspResult.

        **参数解释**: 任务ID。 **取值范围**: 不涉及。

        :return: The job_id of this ListAspResult.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListAspResult.

        **参数解释**: 任务ID。 **取值范围**: 不涉及。

        :param job_id: The job_id of this ListAspResult.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def file_size(self):
        r"""Gets the file_size of this ListAspResult.

        **参数解释**: 文件大小单位KB。 **取值范围**: 当status为SUCCESS时，该值不为空。

        :return: The file_size of this ListAspResult.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this ListAspResult.

        **参数解释**: 文件大小单位KB。 **取值范围**: 当status为SUCCESS时，该值不为空。

        :param file_size: The file_size of this ListAspResult.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def start_time(self):
        r"""Gets the start_time of this ListAspResult.

        **参数解释**: 开始采集时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The start_time of this ListAspResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListAspResult.

        **参数解释**: 开始采集时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param start_time: The start_time of this ListAspResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListAspResult.

        **参数解释**: 结束采集时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :return: The end_time of this ListAspResult.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListAspResult.

        **参数解释**: 结束采集时间。 格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**: 不涉及。

        :param end_time: The end_time of this ListAspResult.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def download_url(self):
        r"""Gets the download_url of this ListAspResult.

        **参数解释**: 报告下载链接，有效时间为30分钟。 **取值范围**: 当status为SUCCESS时，该值不为空。

        :return: The download_url of this ListAspResult.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this ListAspResult.

        **参数解释**: 报告下载链接，有效时间为30分钟。 **取值范围**: 当status为SUCCESS时，该值不为空。

        :param download_url: The download_url of this ListAspResult.
        :type download_url: str
        """
        self._download_url = download_url

    @property
    def status(self):
        r"""Gets the status of this ListAspResult.

        **参数解释**: 采集状态。 **取值范围**: - SUCCESS：成功。 - FAILED：失败。 - EXPORTING：采集中。

        :return: The status of this ListAspResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAspResult.

        **参数解释**: 采集状态。 **取值范围**: - SUCCESS：成功。 - FAILED：失败。 - EXPORTING：采集中。

        :param status: The status of this ListAspResult.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListAspResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
