# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtitleFileDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence_no': 'int',
        'subtitle_file_state': 'str',
        'subtitle_file_download_url': 'str',
        'subtitle_file_upload_url': 'str',
        'generate_time': 'str'
    }

    attribute_map = {
        'sequence_no': 'sequence_no',
        'subtitle_file_state': 'subtitle_file_state',
        'subtitle_file_download_url': 'subtitle_file_download_url',
        'subtitle_file_upload_url': 'subtitle_file_upload_url',
        'generate_time': 'generate_time'
    }

    def __init__(self, sequence_no=None, subtitle_file_state=None, subtitle_file_download_url=None, subtitle_file_upload_url=None, generate_time=None):
        r"""SubtitleFileDetail

        The model defined in huaweicloud sdk

        :param sequence_no: 剧本序号。
        :type sequence_no: int
        :param subtitle_file_state: 字幕文件生成状态。 * GENERATING：字幕文件生成中。 * GENERATE_SUCCEED：字幕文件生成成功。 * GENERATE_FAILED：字幕文件生成失败。
        :type subtitle_file_state: str
        :param subtitle_file_download_url: 字幕文件下载链接。
        :type subtitle_file_download_url: str
        :param subtitle_file_upload_url: 字幕文件上传链接。
        :type subtitle_file_upload_url: str
        :param generate_time: 字幕文件生成时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type generate_time: str
        """
        
        

        self._sequence_no = None
        self._subtitle_file_state = None
        self._subtitle_file_download_url = None
        self._subtitle_file_upload_url = None
        self._generate_time = None
        self.discriminator = None

        if sequence_no is not None:
            self.sequence_no = sequence_no
        if subtitle_file_state is not None:
            self.subtitle_file_state = subtitle_file_state
        if subtitle_file_download_url is not None:
            self.subtitle_file_download_url = subtitle_file_download_url
        if subtitle_file_upload_url is not None:
            self.subtitle_file_upload_url = subtitle_file_upload_url
        if generate_time is not None:
            self.generate_time = generate_time

    @property
    def sequence_no(self):
        r"""Gets the sequence_no of this SubtitleFileDetail.

        剧本序号。

        :return: The sequence_no of this SubtitleFileDetail.
        :rtype: int
        """
        return self._sequence_no

    @sequence_no.setter
    def sequence_no(self, sequence_no):
        r"""Sets the sequence_no of this SubtitleFileDetail.

        剧本序号。

        :param sequence_no: The sequence_no of this SubtitleFileDetail.
        :type sequence_no: int
        """
        self._sequence_no = sequence_no

    @property
    def subtitle_file_state(self):
        r"""Gets the subtitle_file_state of this SubtitleFileDetail.

        字幕文件生成状态。 * GENERATING：字幕文件生成中。 * GENERATE_SUCCEED：字幕文件生成成功。 * GENERATE_FAILED：字幕文件生成失败。

        :return: The subtitle_file_state of this SubtitleFileDetail.
        :rtype: str
        """
        return self._subtitle_file_state

    @subtitle_file_state.setter
    def subtitle_file_state(self, subtitle_file_state):
        r"""Sets the subtitle_file_state of this SubtitleFileDetail.

        字幕文件生成状态。 * GENERATING：字幕文件生成中。 * GENERATE_SUCCEED：字幕文件生成成功。 * GENERATE_FAILED：字幕文件生成失败。

        :param subtitle_file_state: The subtitle_file_state of this SubtitleFileDetail.
        :type subtitle_file_state: str
        """
        self._subtitle_file_state = subtitle_file_state

    @property
    def subtitle_file_download_url(self):
        r"""Gets the subtitle_file_download_url of this SubtitleFileDetail.

        字幕文件下载链接。

        :return: The subtitle_file_download_url of this SubtitleFileDetail.
        :rtype: str
        """
        return self._subtitle_file_download_url

    @subtitle_file_download_url.setter
    def subtitle_file_download_url(self, subtitle_file_download_url):
        r"""Sets the subtitle_file_download_url of this SubtitleFileDetail.

        字幕文件下载链接。

        :param subtitle_file_download_url: The subtitle_file_download_url of this SubtitleFileDetail.
        :type subtitle_file_download_url: str
        """
        self._subtitle_file_download_url = subtitle_file_download_url

    @property
    def subtitle_file_upload_url(self):
        r"""Gets the subtitle_file_upload_url of this SubtitleFileDetail.

        字幕文件上传链接。

        :return: The subtitle_file_upload_url of this SubtitleFileDetail.
        :rtype: str
        """
        return self._subtitle_file_upload_url

    @subtitle_file_upload_url.setter
    def subtitle_file_upload_url(self, subtitle_file_upload_url):
        r"""Sets the subtitle_file_upload_url of this SubtitleFileDetail.

        字幕文件上传链接。

        :param subtitle_file_upload_url: The subtitle_file_upload_url of this SubtitleFileDetail.
        :type subtitle_file_upload_url: str
        """
        self._subtitle_file_upload_url = subtitle_file_upload_url

    @property
    def generate_time(self):
        r"""Gets the generate_time of this SubtitleFileDetail.

        字幕文件生成时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The generate_time of this SubtitleFileDetail.
        :rtype: str
        """
        return self._generate_time

    @generate_time.setter
    def generate_time(self, generate_time):
        r"""Sets the generate_time of this SubtitleFileDetail.

        字幕文件生成时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param generate_time: The generate_time of this SubtitleFileDetail.
        :type generate_time: str
        """
        self._generate_time = generate_time

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
        if not isinstance(other, SubtitleFileDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
