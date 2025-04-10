# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SegmentFileDO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'record_type': 'str',
        'begin_time': 'int',
        'end_time': 'int',
        'duration': 'int',
        'file_size': 'int',
        'sha256': 'str',
        'play_url': 'str',
        'download_url': 'str'
    }

    attribute_map = {
        'record_type': 'recordType',
        'begin_time': 'beginTime',
        'end_time': 'endTime',
        'duration': 'duration',
        'file_size': 'fileSize',
        'sha256': 'sha256',
        'play_url': 'playUrl',
        'download_url': 'downloadUrl'
    }

    def __init__(self, record_type=None, begin_time=None, end_time=None, duration=None, file_size=None, sha256=None, play_url=None, download_url=None):
        r"""SegmentFileDO

        The model defined in huaweicloud sdk

        :param record_type: 会议录制类型，取值范围见数据结构RecordType：AUDIO 纯音频录制，SPEAKER_VIDEO 演讲者视图，SHARE_VIDEO共享屏幕，SPEAKER_SHARE_VIDEO 含演讲者视图的共享屏幕
        :type record_type: str
        :param begin_time: 录制文件开始时间 
        :type begin_time: int
        :param end_time: 录制文件结束时间 
        :type end_time: int
        :param duration: 录制文件时长(秒)
        :type duration: int
        :param file_size: 文件大小(字节数)
        :type file_size: int
        :param sha256: 文件hash校验码(SHA256)，64个字符
        :type sha256: str
        :param play_url: 录制文件播放地址，有效期1小时
        :type play_url: str
        :param download_url: 录制文件下载地址，有效期1小时
        :type download_url: str
        """
        
        

        self._record_type = None
        self._begin_time = None
        self._end_time = None
        self._duration = None
        self._file_size = None
        self._sha256 = None
        self._play_url = None
        self._download_url = None
        self.discriminator = None

        if record_type is not None:
            self.record_type = record_type
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if duration is not None:
            self.duration = duration
        if file_size is not None:
            self.file_size = file_size
        if sha256 is not None:
            self.sha256 = sha256
        if play_url is not None:
            self.play_url = play_url
        if download_url is not None:
            self.download_url = download_url

    @property
    def record_type(self):
        r"""Gets the record_type of this SegmentFileDO.

        会议录制类型，取值范围见数据结构RecordType：AUDIO 纯音频录制，SPEAKER_VIDEO 演讲者视图，SHARE_VIDEO共享屏幕，SPEAKER_SHARE_VIDEO 含演讲者视图的共享屏幕

        :return: The record_type of this SegmentFileDO.
        :rtype: str
        """
        return self._record_type

    @record_type.setter
    def record_type(self, record_type):
        r"""Sets the record_type of this SegmentFileDO.

        会议录制类型，取值范围见数据结构RecordType：AUDIO 纯音频录制，SPEAKER_VIDEO 演讲者视图，SHARE_VIDEO共享屏幕，SPEAKER_SHARE_VIDEO 含演讲者视图的共享屏幕

        :param record_type: The record_type of this SegmentFileDO.
        :type record_type: str
        """
        self._record_type = record_type

    @property
    def begin_time(self):
        r"""Gets the begin_time of this SegmentFileDO.

        录制文件开始时间 

        :return: The begin_time of this SegmentFileDO.
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this SegmentFileDO.

        录制文件开始时间 

        :param begin_time: The begin_time of this SegmentFileDO.
        :type begin_time: int
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this SegmentFileDO.

        录制文件结束时间 

        :return: The end_time of this SegmentFileDO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this SegmentFileDO.

        录制文件结束时间 

        :param end_time: The end_time of this SegmentFileDO.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def duration(self):
        r"""Gets the duration of this SegmentFileDO.

        录制文件时长(秒)

        :return: The duration of this SegmentFileDO.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SegmentFileDO.

        录制文件时长(秒)

        :param duration: The duration of this SegmentFileDO.
        :type duration: int
        """
        self._duration = duration

    @property
    def file_size(self):
        r"""Gets the file_size of this SegmentFileDO.

        文件大小(字节数)

        :return: The file_size of this SegmentFileDO.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        r"""Sets the file_size of this SegmentFileDO.

        文件大小(字节数)

        :param file_size: The file_size of this SegmentFileDO.
        :type file_size: int
        """
        self._file_size = file_size

    @property
    def sha256(self):
        r"""Gets the sha256 of this SegmentFileDO.

        文件hash校验码(SHA256)，64个字符

        :return: The sha256 of this SegmentFileDO.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this SegmentFileDO.

        文件hash校验码(SHA256)，64个字符

        :param sha256: The sha256 of this SegmentFileDO.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def play_url(self):
        r"""Gets the play_url of this SegmentFileDO.

        录制文件播放地址，有效期1小时

        :return: The play_url of this SegmentFileDO.
        :rtype: str
        """
        return self._play_url

    @play_url.setter
    def play_url(self, play_url):
        r"""Sets the play_url of this SegmentFileDO.

        录制文件播放地址，有效期1小时

        :param play_url: The play_url of this SegmentFileDO.
        :type play_url: str
        """
        self._play_url = play_url

    @property
    def download_url(self):
        r"""Gets the download_url of this SegmentFileDO.

        录制文件下载地址，有效期1小时

        :return: The download_url of this SegmentFileDO.
        :rtype: str
        """
        return self._download_url

    @download_url.setter
    def download_url(self, download_url):
        r"""Sets the download_url of this SegmentFileDO.

        录制文件下载地址，有效期1小时

        :param download_url: The download_url of this SegmentFileDO.
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
        if not isinstance(other, SegmentFileDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
