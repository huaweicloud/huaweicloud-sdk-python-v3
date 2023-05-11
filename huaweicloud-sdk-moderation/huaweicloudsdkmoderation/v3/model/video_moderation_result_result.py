# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoModerationResultResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'suggestion': 'str',
        'image_detail': 'list[VideoModerationImageDetail]',
        'audio_detail': 'list[VideoModerationVideoDetail]'
    }

    attribute_map = {
        'suggestion': 'suggestion',
        'image_detail': 'image_detail',
        'audio_detail': 'audio_detail'
    }

    def __init__(self, suggestion=None, image_detail=None, audio_detail=None):
        """VideoModerationResultResult

        The model defined in huaweicloud sdk

        :param suggestion: 视频审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检 pass：不包含敏感信息，通过
        :type suggestion: str
        :param image_detail: 图像审核详情
        :type image_detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationImageDetail`]
        :param audio_detail: 音频审核详情
        :type audio_detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationVideoDetail`]
        """
        
        

        self._suggestion = None
        self._image_detail = None
        self._audio_detail = None
        self.discriminator = None

        if suggestion is not None:
            self.suggestion = suggestion
        if image_detail is not None:
            self.image_detail = image_detail
        if audio_detail is not None:
            self.audio_detail = audio_detail

    @property
    def suggestion(self):
        """Gets the suggestion of this VideoModerationResultResult.

        视频审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检 pass：不包含敏感信息，通过

        :return: The suggestion of this VideoModerationResultResult.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        """Sets the suggestion of this VideoModerationResultResult.

        视频审核结果是否通过。 block：包含敏感信息，不通过  review：需要人工复检 pass：不包含敏感信息，通过

        :param suggestion: The suggestion of this VideoModerationResultResult.
        :type suggestion: str
        """
        self._suggestion = suggestion

    @property
    def image_detail(self):
        """Gets the image_detail of this VideoModerationResultResult.

        图像审核详情

        :return: The image_detail of this VideoModerationResultResult.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationImageDetail`]
        """
        return self._image_detail

    @image_detail.setter
    def image_detail(self, image_detail):
        """Sets the image_detail of this VideoModerationResultResult.

        图像审核详情

        :param image_detail: The image_detail of this VideoModerationResultResult.
        :type image_detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationImageDetail`]
        """
        self._image_detail = image_detail

    @property
    def audio_detail(self):
        """Gets the audio_detail of this VideoModerationResultResult.

        音频审核详情

        :return: The audio_detail of this VideoModerationResultResult.
        :rtype: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationVideoDetail`]
        """
        return self._audio_detail

    @audio_detail.setter
    def audio_detail(self, audio_detail):
        """Sets the audio_detail of this VideoModerationResultResult.

        音频审核详情

        :param audio_detail: The audio_detail of this VideoModerationResultResult.
        :type audio_detail: list[:class:`huaweicloudsdkmoderation.v3.VideoModerationVideoDetail`]
        """
        self._audio_detail = audio_detail

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
        if not isinstance(other, VideoModerationResultResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
