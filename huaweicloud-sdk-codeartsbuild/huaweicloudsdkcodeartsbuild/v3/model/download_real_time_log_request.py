# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadRealTimeLogRequest:

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
        'build_no': 'int',
        'offset': 'int',
        'length': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'build_no': 'build_no',
        'offset': 'offset',
        'length': 'length'
    }

    def __init__(self, job_id=None, build_no=None, offset=None, length=None):
        r"""DownloadRealTimeLogRequest

        The model defined in huaweicloud sdk

        :param job_id: 构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。
        :type job_id: str
        :param build_no: 构建任务的构建编号，从1开始，每次构建递增1
        :type build_no: int
        :param offset: 偏移量，传入前一次请求返回的offset
        :type offset: int
        :param length: 可控制返回内容长度，默认值为1000000
        :type length: int
        """
        
        

        self._job_id = None
        self._build_no = None
        self._offset = None
        self._length = None
        self.discriminator = None

        self.job_id = job_id
        self.build_no = build_no
        self.offset = offset
        if length is not None:
            self.length = length

    @property
    def job_id(self):
        r"""Gets the job_id of this DownloadRealTimeLogRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :return: The job_id of this DownloadRealTimeLogRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this DownloadRealTimeLogRequest.

        构建的任务ID； 编辑构建任务时，浏览器URL末尾的32位数字、字母组合的字符串。

        :param job_id: The job_id of this DownloadRealTimeLogRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def build_no(self):
        r"""Gets the build_no of this DownloadRealTimeLogRequest.

        构建任务的构建编号，从1开始，每次构建递增1

        :return: The build_no of this DownloadRealTimeLogRequest.
        :rtype: int
        """
        return self._build_no

    @build_no.setter
    def build_no(self, build_no):
        r"""Sets the build_no of this DownloadRealTimeLogRequest.

        构建任务的构建编号，从1开始，每次构建递增1

        :param build_no: The build_no of this DownloadRealTimeLogRequest.
        :type build_no: int
        """
        self._build_no = build_no

    @property
    def offset(self):
        r"""Gets the offset of this DownloadRealTimeLogRequest.

        偏移量，传入前一次请求返回的offset

        :return: The offset of this DownloadRealTimeLogRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this DownloadRealTimeLogRequest.

        偏移量，传入前一次请求返回的offset

        :param offset: The offset of this DownloadRealTimeLogRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def length(self):
        r"""Gets the length of this DownloadRealTimeLogRequest.

        可控制返回内容长度，默认值为1000000

        :return: The length of this DownloadRealTimeLogRequest.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        r"""Sets the length of this DownloadRealTimeLogRequest.

        可控制返回内容长度，默认值为1000000

        :param length: The length of this DownloadRealTimeLogRequest.
        :type length: int
        """
        self._length = length

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
        if not isinstance(other, DownloadRealTimeLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
