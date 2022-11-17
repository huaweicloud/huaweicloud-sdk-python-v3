# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputSetting:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'ObsObjInfo',
        'pane_id': 'str',
        'audio_policy': 'str'
    }

    attribute_map = {
        'input': 'input',
        'pane_id': 'pane_id',
        'audio_policy': 'audio_policy'
    }

    def __init__(self, input=None, pane_id=None, audio_policy=None):
        """InputSetting

        The model defined in huaweicloud sdk

        :param input: 
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        :param pane_id: 原视频的id,为整数类型数值字符串。用于匹配后面的布局配置。
        :type pane_id: str
        :param audio_policy: 该视频采取的音频策略。DISCARD表示丢弃音频，合成的视频中不会出现该视频的音频。 RESERVE表示保留音频，合成的视频中会出现该视频音频。如果多个原视频配置了RESERVE，合成的视频文件的音频，是多个原 视频音频的混合。默认会丢弃音频。
        :type audio_policy: str
        """
        
        

        self._input = None
        self._pane_id = None
        self._audio_policy = None
        self.discriminator = None

        self.input = input
        self.pane_id = pane_id
        if audio_policy is not None:
            self.audio_policy = audio_policy

    @property
    def input(self):
        """Gets the input of this InputSetting.

        :return: The input of this InputSetting.
        :rtype: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InputSetting.

        :param input: The input of this InputSetting.
        :type input: :class:`huaweicloudsdkmpc.v1.ObsObjInfo`
        """
        self._input = input

    @property
    def pane_id(self):
        """Gets the pane_id of this InputSetting.

        原视频的id,为整数类型数值字符串。用于匹配后面的布局配置。

        :return: The pane_id of this InputSetting.
        :rtype: str
        """
        return self._pane_id

    @pane_id.setter
    def pane_id(self, pane_id):
        """Sets the pane_id of this InputSetting.

        原视频的id,为整数类型数值字符串。用于匹配后面的布局配置。

        :param pane_id: The pane_id of this InputSetting.
        :type pane_id: str
        """
        self._pane_id = pane_id

    @property
    def audio_policy(self):
        """Gets the audio_policy of this InputSetting.

        该视频采取的音频策略。DISCARD表示丢弃音频，合成的视频中不会出现该视频的音频。 RESERVE表示保留音频，合成的视频中会出现该视频音频。如果多个原视频配置了RESERVE，合成的视频文件的音频，是多个原 视频音频的混合。默认会丢弃音频。

        :return: The audio_policy of this InputSetting.
        :rtype: str
        """
        return self._audio_policy

    @audio_policy.setter
    def audio_policy(self, audio_policy):
        """Sets the audio_policy of this InputSetting.

        该视频采取的音频策略。DISCARD表示丢弃音频，合成的视频中不会出现该视频的音频。 RESERVE表示保留音频，合成的视频中会出现该视频音频。如果多个原视频配置了RESERVE，合成的视频文件的音频，是多个原 视频音频的混合。默认会丢弃音频。

        :param audio_policy: The audio_policy of this InputSetting.
        :type audio_policy: str
        """
        self._audio_policy = audio_policy

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
        if not isinstance(other, InputSetting):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
