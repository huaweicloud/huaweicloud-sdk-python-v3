# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AnalysisInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'diarization': 'bool',
        'channel': 'str',
        'emotion': 'bool',
        'speed': 'bool'
    }

    attribute_map = {
        'diarization': 'diarization',
        'channel': 'channel',
        'emotion': 'emotion',
        'speed': 'speed'
    }

    def __init__(self, diarization=None, channel=None, emotion=None, speed=None):
        """AnalysisInfo

        The model defined in huaweicloud sdk

        :param diarization: 是否需要做话者分离。缺省为true，表示会进行话者分离，识别结果中会包含role项（角色）。如果diarization为false, 那么结果中不会出现role项。
        :type diarization: bool
        :param channel: 语音文件声道信息，可以为MONO（缺省), LEFT_AGENT, RIGHT_AGENT。  如果channel 为MONO，那么原始文件需要为单声道文件。  如果为双声道文件，系统会将其转换成单声道文件，可能会影响识别效果。  如果 channel 为 LEFT_AGENT或RIGHT_AGENT, 则原始文件需要为双声道文件，如果为单声道文件，系统会将其转换成双声道文件，可能会影响识别效果。  当channel 为 LEFT_AGENT或RIGHT_AGENT，且diarization为true时，系统会按照配置给出对应角色。其中：  LEFT_AGENT 指定左声道语音为agent（坐席）,  RIGHT_AGENT 指定右声道为agent（坐席）。
        :type channel: str
        :param emotion: 是否需要做情绪检测, 缺省为true。
        :type emotion: bool
        :param speed: 是否需要输出语速信息, 缺省为true。
        :type speed: bool
        """
        
        

        self._diarization = None
        self._channel = None
        self._emotion = None
        self._speed = None
        self.discriminator = None

        if diarization is not None:
            self.diarization = diarization
        if channel is not None:
            self.channel = channel
        if emotion is not None:
            self.emotion = emotion
        if speed is not None:
            self.speed = speed

    @property
    def diarization(self):
        """Gets the diarization of this AnalysisInfo.

        是否需要做话者分离。缺省为true，表示会进行话者分离，识别结果中会包含role项（角色）。如果diarization为false, 那么结果中不会出现role项。

        :return: The diarization of this AnalysisInfo.
        :rtype: bool
        """
        return self._diarization

    @diarization.setter
    def diarization(self, diarization):
        """Sets the diarization of this AnalysisInfo.

        是否需要做话者分离。缺省为true，表示会进行话者分离，识别结果中会包含role项（角色）。如果diarization为false, 那么结果中不会出现role项。

        :param diarization: The diarization of this AnalysisInfo.
        :type diarization: bool
        """
        self._diarization = diarization

    @property
    def channel(self):
        """Gets the channel of this AnalysisInfo.

        语音文件声道信息，可以为MONO（缺省), LEFT_AGENT, RIGHT_AGENT。  如果channel 为MONO，那么原始文件需要为单声道文件。  如果为双声道文件，系统会将其转换成单声道文件，可能会影响识别效果。  如果 channel 为 LEFT_AGENT或RIGHT_AGENT, 则原始文件需要为双声道文件，如果为单声道文件，系统会将其转换成双声道文件，可能会影响识别效果。  当channel 为 LEFT_AGENT或RIGHT_AGENT，且diarization为true时，系统会按照配置给出对应角色。其中：  LEFT_AGENT 指定左声道语音为agent（坐席）,  RIGHT_AGENT 指定右声道为agent（坐席）。

        :return: The channel of this AnalysisInfo.
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this AnalysisInfo.

        语音文件声道信息，可以为MONO（缺省), LEFT_AGENT, RIGHT_AGENT。  如果channel 为MONO，那么原始文件需要为单声道文件。  如果为双声道文件，系统会将其转换成单声道文件，可能会影响识别效果。  如果 channel 为 LEFT_AGENT或RIGHT_AGENT, 则原始文件需要为双声道文件，如果为单声道文件，系统会将其转换成双声道文件，可能会影响识别效果。  当channel 为 LEFT_AGENT或RIGHT_AGENT，且diarization为true时，系统会按照配置给出对应角色。其中：  LEFT_AGENT 指定左声道语音为agent（坐席）,  RIGHT_AGENT 指定右声道为agent（坐席）。

        :param channel: The channel of this AnalysisInfo.
        :type channel: str
        """
        self._channel = channel

    @property
    def emotion(self):
        """Gets the emotion of this AnalysisInfo.

        是否需要做情绪检测, 缺省为true。

        :return: The emotion of this AnalysisInfo.
        :rtype: bool
        """
        return self._emotion

    @emotion.setter
    def emotion(self, emotion):
        """Sets the emotion of this AnalysisInfo.

        是否需要做情绪检测, 缺省为true。

        :param emotion: The emotion of this AnalysisInfo.
        :type emotion: bool
        """
        self._emotion = emotion

    @property
    def speed(self):
        """Gets the speed of this AnalysisInfo.

        是否需要输出语速信息, 缺省为true。

        :return: The speed of this AnalysisInfo.
        :rtype: bool
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this AnalysisInfo.

        是否需要输出语速信息, 缺省为true。

        :param speed: The speed of this AnalysisInfo.
        :type speed: bool
        """
        self._speed = speed

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
        if not isinstance(other, AnalysisInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
