# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartChatRoomBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'room_id': 'str',
        'room_name': 'str',
        'room_description': 'str',
        'robot_id': 'str',
        'cover_url': 'str',
        'model_infos': 'ModelInfo',
        'voice_config': 'VoiceConfig',
        'concurrency': 'int',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'room_id': 'room_id',
        'room_name': 'room_name',
        'room_description': 'room_description',
        'robot_id': 'robot_id',
        'cover_url': 'cover_url',
        'model_infos': 'model_infos',
        'voice_config': 'voice_config',
        'concurrency': 'concurrency',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, room_id=None, room_name=None, room_description=None, robot_id=None, cover_url=None, model_infos=None, voice_config=None, concurrency=None, create_time=None, update_time=None):
        """SmartChatRoomBaseInfo

        The model defined in huaweicloud sdk

        :param room_id: 智能交互对话ID
        :type room_id: str
        :param room_name: 智能交互对话名称
        :type room_name: str
        :param room_description: 智能交互对话描述。
        :type room_description: str
        :param robot_id: 机器人ID。
        :type robot_id: str
        :param cover_url: 对话封面图URL
        :type cover_url: str
        :param model_infos: 
        :type model_infos: :class:`huaweicloudsdkmetastudio.v1.ModelInfo`
        :param voice_config: 
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        :param concurrency: 并发路数。
        :type concurrency: int
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        """
        
        

        self._room_id = None
        self._room_name = None
        self._room_description = None
        self._robot_id = None
        self._cover_url = None
        self._model_infos = None
        self._voice_config = None
        self._concurrency = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if room_id is not None:
            self.room_id = room_id
        if room_name is not None:
            self.room_name = room_name
        if room_description is not None:
            self.room_description = room_description
        if robot_id is not None:
            self.robot_id = robot_id
        if cover_url is not None:
            self.cover_url = cover_url
        if model_infos is not None:
            self.model_infos = model_infos
        if voice_config is not None:
            self.voice_config = voice_config
        if concurrency is not None:
            self.concurrency = concurrency
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def room_id(self):
        """Gets the room_id of this SmartChatRoomBaseInfo.

        智能交互对话ID

        :return: The room_id of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        """Sets the room_id of this SmartChatRoomBaseInfo.

        智能交互对话ID

        :param room_id: The room_id of this SmartChatRoomBaseInfo.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def room_name(self):
        """Gets the room_name of this SmartChatRoomBaseInfo.

        智能交互对话名称

        :return: The room_name of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        """Sets the room_name of this SmartChatRoomBaseInfo.

        智能交互对话名称

        :param room_name: The room_name of this SmartChatRoomBaseInfo.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        """Gets the room_description of this SmartChatRoomBaseInfo.

        智能交互对话描述。

        :return: The room_description of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        """Sets the room_description of this SmartChatRoomBaseInfo.

        智能交互对话描述。

        :param room_description: The room_description of this SmartChatRoomBaseInfo.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def robot_id(self):
        """Gets the robot_id of this SmartChatRoomBaseInfo.

        机器人ID。

        :return: The robot_id of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this SmartChatRoomBaseInfo.

        机器人ID。

        :param robot_id: The robot_id of this SmartChatRoomBaseInfo.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def cover_url(self):
        """Gets the cover_url of this SmartChatRoomBaseInfo.

        对话封面图URL

        :return: The cover_url of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        """Sets the cover_url of this SmartChatRoomBaseInfo.

        对话封面图URL

        :param cover_url: The cover_url of this SmartChatRoomBaseInfo.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def model_infos(self):
        """Gets the model_infos of this SmartChatRoomBaseInfo.

        :return: The model_infos of this SmartChatRoomBaseInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ModelInfo`
        """
        return self._model_infos

    @model_infos.setter
    def model_infos(self, model_infos):
        """Sets the model_infos of this SmartChatRoomBaseInfo.

        :param model_infos: The model_infos of this SmartChatRoomBaseInfo.
        :type model_infos: :class:`huaweicloudsdkmetastudio.v1.ModelInfo`
        """
        self._model_infos = model_infos

    @property
    def voice_config(self):
        """Gets the voice_config of this SmartChatRoomBaseInfo.

        :return: The voice_config of this SmartChatRoomBaseInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        """Sets the voice_config of this SmartChatRoomBaseInfo.

        :param voice_config: The voice_config of this SmartChatRoomBaseInfo.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def concurrency(self):
        """Gets the concurrency of this SmartChatRoomBaseInfo.

        并发路数。

        :return: The concurrency of this SmartChatRoomBaseInfo.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this SmartChatRoomBaseInfo.

        并发路数。

        :param concurrency: The concurrency of this SmartChatRoomBaseInfo.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def create_time(self):
        """Gets the create_time of this SmartChatRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SmartChatRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this SmartChatRoomBaseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this SmartChatRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this SmartChatRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this SmartChatRoomBaseInfo.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, SmartChatRoomBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
