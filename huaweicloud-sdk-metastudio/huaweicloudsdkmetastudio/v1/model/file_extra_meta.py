# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FileExtraMeta:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'video_transcoding_status': 'str'
    }

    attribute_map = {
        'video_transcoding_status': 'video_transcoding_status'
    }

    def __init__(self, video_transcoding_status=None):
        r"""FileExtraMeta

        The model defined in huaweicloud sdk

        :param video_transcoding_status: 视频转码状态。 * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功
        :type video_transcoding_status: str
        """
        
        

        self._video_transcoding_status = None
        self.discriminator = None

        if video_transcoding_status is not None:
            self.video_transcoding_status = video_transcoding_status

    @property
    def video_transcoding_status(self):
        r"""Gets the video_transcoding_status of this FileExtraMeta.

        视频转码状态。 * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功

        :return: The video_transcoding_status of this FileExtraMeta.
        :rtype: str
        """
        return self._video_transcoding_status

    @video_transcoding_status.setter
    def video_transcoding_status(self, video_transcoding_status):
        r"""Sets the video_transcoding_status of this FileExtraMeta.

        视频转码状态。 * WAITING：等待 * TRANSCODING：转码中 * FAILED：失败 * SUCCEEDED：成功

        :param video_transcoding_status: The video_transcoding_status of this FileExtraMeta.
        :type video_transcoding_status: str
        """
        self._video_transcoding_status = video_transcoding_status

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
        if not isinstance(other, FileExtraMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
