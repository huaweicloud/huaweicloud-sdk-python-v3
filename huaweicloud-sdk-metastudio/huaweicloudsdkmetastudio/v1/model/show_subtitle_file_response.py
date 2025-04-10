# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSubtitleFileResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_state': 'str',
        'subtitle_file_info': 'list[SubtitleFileDetail]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'job_state': 'job_state',
        'subtitle_file_info': 'subtitle_file_info',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, job_state=None, subtitle_file_info=None, x_request_id=None):
        r"""ShowSubtitleFileResponse

        The model defined in huaweicloud sdk

        :param job_state: 字幕文件所有任务状态。 * GENERATING：字幕文件任务生成中。 * GENERATED：字幕文件生成结束。
        :type job_state: str
        :param subtitle_file_info: 字幕文件列表。
        :type subtitle_file_info: list[:class:`huaweicloudsdkmetastudio.v1.SubtitleFileDetail`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowSubtitleFileResponse, self).__init__()

        self._job_state = None
        self._subtitle_file_info = None
        self._x_request_id = None
        self.discriminator = None

        if job_state is not None:
            self.job_state = job_state
        if subtitle_file_info is not None:
            self.subtitle_file_info = subtitle_file_info
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def job_state(self):
        r"""Gets the job_state of this ShowSubtitleFileResponse.

        字幕文件所有任务状态。 * GENERATING：字幕文件任务生成中。 * GENERATED：字幕文件生成结束。

        :return: The job_state of this ShowSubtitleFileResponse.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        r"""Sets the job_state of this ShowSubtitleFileResponse.

        字幕文件所有任务状态。 * GENERATING：字幕文件任务生成中。 * GENERATED：字幕文件生成结束。

        :param job_state: The job_state of this ShowSubtitleFileResponse.
        :type job_state: str
        """
        self._job_state = job_state

    @property
    def subtitle_file_info(self):
        r"""Gets the subtitle_file_info of this ShowSubtitleFileResponse.

        字幕文件列表。

        :return: The subtitle_file_info of this ShowSubtitleFileResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.SubtitleFileDetail`]
        """
        return self._subtitle_file_info

    @subtitle_file_info.setter
    def subtitle_file_info(self, subtitle_file_info):
        r"""Sets the subtitle_file_info of this ShowSubtitleFileResponse.

        字幕文件列表。

        :param subtitle_file_info: The subtitle_file_info of this ShowSubtitleFileResponse.
        :type subtitle_file_info: list[:class:`huaweicloudsdkmetastudio.v1.SubtitleFileDetail`]
        """
        self._subtitle_file_info = subtitle_file_info

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowSubtitleFileResponse.

        :return: The x_request_id of this ShowSubtitleFileResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowSubtitleFileResponse.

        :param x_request_id: The x_request_id of this ShowSubtitleFileResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowSubtitleFileResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
