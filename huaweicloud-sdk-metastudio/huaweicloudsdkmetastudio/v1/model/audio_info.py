# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_id': 'int'
    }

    attribute_map = {
        'audio_id': 'audio_id'
    }

    def __init__(self, audio_id=None):
        r"""AudioInfo

        The model defined in huaweicloud sdk

        :param audio_id: **参数解释**： 音频id。 &gt; * 获取方式：剧本为音频驱动时，查询剧本详情或者更新剧本会返回audio_id  **约束限制**： 不涉及 **默认取值**： 不涉及
        :type audio_id: int
        """
        
        

        self._audio_id = None
        self.discriminator = None

        if audio_id is not None:
            self.audio_id = audio_id

    @property
    def audio_id(self):
        r"""Gets the audio_id of this AudioInfo.

        **参数解释**： 音频id。 > * 获取方式：剧本为音频驱动时，查询剧本详情或者更新剧本会返回audio_id  **约束限制**： 不涉及 **默认取值**： 不涉及

        :return: The audio_id of this AudioInfo.
        :rtype: int
        """
        return self._audio_id

    @audio_id.setter
    def audio_id(self, audio_id):
        r"""Sets the audio_id of this AudioInfo.

        **参数解释**： 音频id。 > * 获取方式：剧本为音频驱动时，查询剧本详情或者更新剧本会返回audio_id  **约束限制**： 不涉及 **默认取值**： 不涉及

        :param audio_id: The audio_id of this AudioInfo.
        :type audio_id: int
        """
        self._audio_id = audio_id

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
        if not isinstance(other, AudioInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
