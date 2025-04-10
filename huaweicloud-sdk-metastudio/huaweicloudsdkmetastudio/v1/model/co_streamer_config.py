# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoStreamerConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'voice_config': 'VoiceConfig',
        'streamer_action': 'str'
    }

    attribute_map = {
        'voice_config': 'voice_config',
        'streamer_action': 'streamer_action'
    }

    def __init__(self, voice_config=None, streamer_action=None):
        r"""CoStreamerConfig

        The model defined in huaweicloud sdk

        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param streamer_action: **参数解释**： 助播出声时主播行为设置。 **约束限制**： 不涉及 **取值范围**： * SILENCE：静默 * VOLUME_DOWN：音量降低  **默认取值**： 不涉及。
        :type streamer_action: str
        """
        
        

        self._voice_config = None
        self._streamer_action = None
        self.discriminator = None

        if voice_config is not None:
            self.voice_config = voice_config
        if streamer_action is not None:
            self.streamer_action = streamer_action

    @property
    def voice_config(self):
        r"""Gets the voice_config of this CoStreamerConfig.

        :return: The voice_config of this CoStreamerConfig.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        r"""Sets the voice_config of this CoStreamerConfig.

        :param voice_config: The voice_config of this CoStreamerConfig.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def streamer_action(self):
        r"""Gets the streamer_action of this CoStreamerConfig.

        **参数解释**： 助播出声时主播行为设置。 **约束限制**： 不涉及 **取值范围**： * SILENCE：静默 * VOLUME_DOWN：音量降低  **默认取值**： 不涉及。

        :return: The streamer_action of this CoStreamerConfig.
        :rtype: str
        """
        return self._streamer_action

    @streamer_action.setter
    def streamer_action(self, streamer_action):
        r"""Sets the streamer_action of this CoStreamerConfig.

        **参数解释**： 助播出声时主播行为设置。 **约束限制**： 不涉及 **取值范围**： * SILENCE：静默 * VOLUME_DOWN：音量降低  **默认取值**： 不涉及。

        :param streamer_action: The streamer_action of this CoStreamerConfig.
        :type streamer_action: str
        """
        self._streamer_action = streamer_action

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
        if not isinstance(other, CoStreamerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
