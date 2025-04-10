# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtitleFileInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subtitle_file_download_url': 'str',
        'subtitle_file_upload_url': 'str',
        'subtitle_file_state': 'str',
        'job_id': 'str'
    }

    attribute_map = {
        'subtitle_file_download_url': 'subtitle_file_download_url',
        'subtitle_file_upload_url': 'subtitle_file_upload_url',
        'subtitle_file_state': 'subtitle_file_state',
        'job_id': 'job_id'
    }

    def __init__(self, subtitle_file_download_url=None, subtitle_file_upload_url=None, subtitle_file_state=None, job_id=None):
        r"""SubtitleFileInfo

        The model defined in huaweicloud sdk

        :param subtitle_file_download_url: 字幕文件下载链接。
        :type subtitle_file_download_url: str
        :param subtitle_file_upload_url: 字幕文件上传链接。
        :type subtitle_file_upload_url: str
        :param subtitle_file_state: 字幕文件生成状态。 * GENERATING：字幕文件生成中。 * GENERATE_SUCCEED：字幕文件生成成功。 * GENERATE_FAILED：字幕文件生成失败。
        :type subtitle_file_state: str
        :param job_id: 字幕文件生成任务ID。
        :type job_id: str
        """
        
        

        self._subtitle_file_download_url = None
        self._subtitle_file_upload_url = None
        self._subtitle_file_state = None
        self._job_id = None
        self.discriminator = None

        if subtitle_file_download_url is not None:
            self.subtitle_file_download_url = subtitle_file_download_url
        if subtitle_file_upload_url is not None:
            self.subtitle_file_upload_url = subtitle_file_upload_url
        if subtitle_file_state is not None:
            self.subtitle_file_state = subtitle_file_state
        if job_id is not None:
            self.job_id = job_id

    @property
    def subtitle_file_download_url(self):
        r"""Gets the subtitle_file_download_url of this SubtitleFileInfo.

        字幕文件下载链接。

        :return: The subtitle_file_download_url of this SubtitleFileInfo.
        :rtype: str
        """
        return self._subtitle_file_download_url

    @subtitle_file_download_url.setter
    def subtitle_file_download_url(self, subtitle_file_download_url):
        r"""Sets the subtitle_file_download_url of this SubtitleFileInfo.

        字幕文件下载链接。

        :param subtitle_file_download_url: The subtitle_file_download_url of this SubtitleFileInfo.
        :type subtitle_file_download_url: str
        """
        self._subtitle_file_download_url = subtitle_file_download_url

    @property
    def subtitle_file_upload_url(self):
        r"""Gets the subtitle_file_upload_url of this SubtitleFileInfo.

        字幕文件上传链接。

        :return: The subtitle_file_upload_url of this SubtitleFileInfo.
        :rtype: str
        """
        return self._subtitle_file_upload_url

    @subtitle_file_upload_url.setter
    def subtitle_file_upload_url(self, subtitle_file_upload_url):
        r"""Sets the subtitle_file_upload_url of this SubtitleFileInfo.

        字幕文件上传链接。

        :param subtitle_file_upload_url: The subtitle_file_upload_url of this SubtitleFileInfo.
        :type subtitle_file_upload_url: str
        """
        self._subtitle_file_upload_url = subtitle_file_upload_url

    @property
    def subtitle_file_state(self):
        r"""Gets the subtitle_file_state of this SubtitleFileInfo.

        字幕文件生成状态。 * GENERATING：字幕文件生成中。 * GENERATE_SUCCEED：字幕文件生成成功。 * GENERATE_FAILED：字幕文件生成失败。

        :return: The subtitle_file_state of this SubtitleFileInfo.
        :rtype: str
        """
        return self._subtitle_file_state

    @subtitle_file_state.setter
    def subtitle_file_state(self, subtitle_file_state):
        r"""Sets the subtitle_file_state of this SubtitleFileInfo.

        字幕文件生成状态。 * GENERATING：字幕文件生成中。 * GENERATE_SUCCEED：字幕文件生成成功。 * GENERATE_FAILED：字幕文件生成失败。

        :param subtitle_file_state: The subtitle_file_state of this SubtitleFileInfo.
        :type subtitle_file_state: str
        """
        self._subtitle_file_state = subtitle_file_state

    @property
    def job_id(self):
        r"""Gets the job_id of this SubtitleFileInfo.

        字幕文件生成任务ID。

        :return: The job_id of this SubtitleFileInfo.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this SubtitleFileInfo.

        字幕文件生成任务ID。

        :param job_id: The job_id of this SubtitleFileInfo.
        :type job_id: str
        """
        self._job_id = job_id

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
        if not isinstance(other, SubtitleFileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
