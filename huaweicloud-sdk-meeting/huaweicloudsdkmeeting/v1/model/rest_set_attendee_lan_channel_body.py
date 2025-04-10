# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestSetAttendeeLanChannelBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'participant_i_ds': 'list[str]',
        'listen_lan_channel': 'str',
        'speak_lan_channel': 'str',
        'include_original_voice': 'int'
    }

    attribute_map = {
        'participant_i_ds': 'participantIDs',
        'listen_lan_channel': 'listenLanChannel',
        'speak_lan_channel': 'speakLanChannel',
        'include_original_voice': 'includeOriginalVoice'
    }

    def __init__(self, participant_i_ds=None, listen_lan_channel=None, speak_lan_channel=None, include_original_voice=None):
        r"""RestSetAttendeeLanChannelBody

        The model defined in huaweicloud sdk

        :param participant_i_ds: 会场标识列表。
        :type participant_i_ds: list[str]
        :param listen_lan_channel: 与会者收听的语言频道，普通与会者听与说一致。
        :type listen_lan_channel: str
        :param speak_lan_channel: 与会者发言的语言频道，普通与会者听与说一致。
        :type speak_lan_channel: str
        :param include_original_voice: 是否包含原声，0：不包含，1：包含。
        :type include_original_voice: int
        """
        
        

        self._participant_i_ds = None
        self._listen_lan_channel = None
        self._speak_lan_channel = None
        self._include_original_voice = None
        self.discriminator = None

        if participant_i_ds is not None:
            self.participant_i_ds = participant_i_ds
        self.listen_lan_channel = listen_lan_channel
        self.speak_lan_channel = speak_lan_channel
        if include_original_voice is not None:
            self.include_original_voice = include_original_voice

    @property
    def participant_i_ds(self):
        r"""Gets the participant_i_ds of this RestSetAttendeeLanChannelBody.

        会场标识列表。

        :return: The participant_i_ds of this RestSetAttendeeLanChannelBody.
        :rtype: list[str]
        """
        return self._participant_i_ds

    @participant_i_ds.setter
    def participant_i_ds(self, participant_i_ds):
        r"""Sets the participant_i_ds of this RestSetAttendeeLanChannelBody.

        会场标识列表。

        :param participant_i_ds: The participant_i_ds of this RestSetAttendeeLanChannelBody.
        :type participant_i_ds: list[str]
        """
        self._participant_i_ds = participant_i_ds

    @property
    def listen_lan_channel(self):
        r"""Gets the listen_lan_channel of this RestSetAttendeeLanChannelBody.

        与会者收听的语言频道，普通与会者听与说一致。

        :return: The listen_lan_channel of this RestSetAttendeeLanChannelBody.
        :rtype: str
        """
        return self._listen_lan_channel

    @listen_lan_channel.setter
    def listen_lan_channel(self, listen_lan_channel):
        r"""Sets the listen_lan_channel of this RestSetAttendeeLanChannelBody.

        与会者收听的语言频道，普通与会者听与说一致。

        :param listen_lan_channel: The listen_lan_channel of this RestSetAttendeeLanChannelBody.
        :type listen_lan_channel: str
        """
        self._listen_lan_channel = listen_lan_channel

    @property
    def speak_lan_channel(self):
        r"""Gets the speak_lan_channel of this RestSetAttendeeLanChannelBody.

        与会者发言的语言频道，普通与会者听与说一致。

        :return: The speak_lan_channel of this RestSetAttendeeLanChannelBody.
        :rtype: str
        """
        return self._speak_lan_channel

    @speak_lan_channel.setter
    def speak_lan_channel(self, speak_lan_channel):
        r"""Sets the speak_lan_channel of this RestSetAttendeeLanChannelBody.

        与会者发言的语言频道，普通与会者听与说一致。

        :param speak_lan_channel: The speak_lan_channel of this RestSetAttendeeLanChannelBody.
        :type speak_lan_channel: str
        """
        self._speak_lan_channel = speak_lan_channel

    @property
    def include_original_voice(self):
        r"""Gets the include_original_voice of this RestSetAttendeeLanChannelBody.

        是否包含原声，0：不包含，1：包含。

        :return: The include_original_voice of this RestSetAttendeeLanChannelBody.
        :rtype: int
        """
        return self._include_original_voice

    @include_original_voice.setter
    def include_original_voice(self, include_original_voice):
        r"""Sets the include_original_voice of this RestSetAttendeeLanChannelBody.

        是否包含原声，0：不包含，1：包含。

        :param include_original_voice: The include_original_voice of this RestSetAttendeeLanChannelBody.
        :type include_original_voice: int
        """
        self._include_original_voice = include_original_voice

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
        if not isinstance(other, RestSetAttendeeLanChannelBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
