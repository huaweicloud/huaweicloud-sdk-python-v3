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
        'billing_mode': 'str',
        'reuse_resource': 'bool',
        'concurrency': 'int',
        'client_nums': 'int',
        'voice_config_list': 'list[VoiceConfigRsp]',
        'default_language': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'exit_mute_threshold': 'int'
    }

    attribute_map = {
        'room_id': 'room_id',
        'room_name': 'room_name',
        'room_description': 'room_description',
        'robot_id': 'robot_id',
        'cover_url': 'cover_url',
        'model_infos': 'model_infos',
        'voice_config': 'voice_config',
        'billing_mode': 'billing_mode',
        'reuse_resource': 'reuse_resource',
        'concurrency': 'concurrency',
        'client_nums': 'client_nums',
        'voice_config_list': 'voice_config_list',
        'default_language': 'default_language',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'exit_mute_threshold': 'exit_mute_threshold'
    }

    def __init__(self, room_id=None, room_name=None, room_description=None, robot_id=None, cover_url=None, model_infos=None, voice_config=None, billing_mode=None, reuse_resource=None, concurrency=None, client_nums=None, voice_config_list=None, default_language=None, create_time=None, update_time=None, exit_mute_threshold=None):
        r"""SmartChatRoomBaseInfo

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
        :param billing_mode: 计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）
        :type billing_mode: str
        :param reuse_resource: 是否允许使用未分配的并发数（端模式下不能复用），默认不使用。
        :type reuse_resource: bool
        :param concurrency: **参数解释**： 并发路数。
        :type concurrency: int
        :param client_nums: **参数解释**： 允许接入终端端数量。
        :type client_nums: int
        :param voice_config_list: 语音配置参数列表。
        :type voice_config_list: list[:class:`huaweicloudsdkmetastudio.v1.VoiceConfigRsp`]
        :param default_language: 默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）
        :type default_language: str
        :param create_time: 创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。
        :type update_time: str
        :param exit_mute_threshold: **参数解释**： 静默退出时长。
        :type exit_mute_threshold: int
        """
        
        

        self._room_id = None
        self._room_name = None
        self._room_description = None
        self._robot_id = None
        self._cover_url = None
        self._model_infos = None
        self._voice_config = None
        self._billing_mode = None
        self._reuse_resource = None
        self._concurrency = None
        self._client_nums = None
        self._voice_config_list = None
        self._default_language = None
        self._create_time = None
        self._update_time = None
        self._exit_mute_threshold = None
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
        if billing_mode is not None:
            self.billing_mode = billing_mode
        if reuse_resource is not None:
            self.reuse_resource = reuse_resource
        if concurrency is not None:
            self.concurrency = concurrency
        if client_nums is not None:
            self.client_nums = client_nums
        if voice_config_list is not None:
            self.voice_config_list = voice_config_list
        if default_language is not None:
            self.default_language = default_language
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if exit_mute_threshold is not None:
            self.exit_mute_threshold = exit_mute_threshold

    @property
    def room_id(self):
        r"""Gets the room_id of this SmartChatRoomBaseInfo.

        智能交互对话ID

        :return: The room_id of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this SmartChatRoomBaseInfo.

        智能交互对话ID

        :param room_id: The room_id of this SmartChatRoomBaseInfo.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def room_name(self):
        r"""Gets the room_name of this SmartChatRoomBaseInfo.

        智能交互对话名称

        :return: The room_name of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, room_name):
        r"""Sets the room_name of this SmartChatRoomBaseInfo.

        智能交互对话名称

        :param room_name: The room_name of this SmartChatRoomBaseInfo.
        :type room_name: str
        """
        self._room_name = room_name

    @property
    def room_description(self):
        r"""Gets the room_description of this SmartChatRoomBaseInfo.

        智能交互对话描述。

        :return: The room_description of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._room_description

    @room_description.setter
    def room_description(self, room_description):
        r"""Sets the room_description of this SmartChatRoomBaseInfo.

        智能交互对话描述。

        :param room_description: The room_description of this SmartChatRoomBaseInfo.
        :type room_description: str
        """
        self._room_description = room_description

    @property
    def robot_id(self):
        r"""Gets the robot_id of this SmartChatRoomBaseInfo.

        机器人ID。

        :return: The robot_id of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this SmartChatRoomBaseInfo.

        机器人ID。

        :param robot_id: The robot_id of this SmartChatRoomBaseInfo.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def cover_url(self):
        r"""Gets the cover_url of this SmartChatRoomBaseInfo.

        对话封面图URL

        :return: The cover_url of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._cover_url

    @cover_url.setter
    def cover_url(self, cover_url):
        r"""Sets the cover_url of this SmartChatRoomBaseInfo.

        对话封面图URL

        :param cover_url: The cover_url of this SmartChatRoomBaseInfo.
        :type cover_url: str
        """
        self._cover_url = cover_url

    @property
    def model_infos(self):
        r"""Gets the model_infos of this SmartChatRoomBaseInfo.

        :return: The model_infos of this SmartChatRoomBaseInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.ModelInfo`
        """
        return self._model_infos

    @model_infos.setter
    def model_infos(self, model_infos):
        r"""Sets the model_infos of this SmartChatRoomBaseInfo.

        :param model_infos: The model_infos of this SmartChatRoomBaseInfo.
        :type model_infos: :class:`huaweicloudsdkmetastudio.v1.ModelInfo`
        """
        self._model_infos = model_infos

    @property
    def voice_config(self):
        r"""Gets the voice_config of this SmartChatRoomBaseInfo.

        :return: The voice_config of this SmartChatRoomBaseInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        return self._voice_config

    @voice_config.setter
    def voice_config(self, voice_config):
        r"""Sets the voice_config of this SmartChatRoomBaseInfo.

        :param voice_config: The voice_config of this SmartChatRoomBaseInfo.
        :type voice_config: :class:`huaweicloudsdkmetastudio.v1.VoiceConfig`
        """
        self._voice_config = voice_config

    @property
    def billing_mode(self):
        r"""Gets the billing_mode of this SmartChatRoomBaseInfo.

        计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）

        :return: The billing_mode of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._billing_mode

    @billing_mode.setter
    def billing_mode(self, billing_mode):
        r"""Sets the billing_mode of this SmartChatRoomBaseInfo.

        计费模式，默认值CONCURRENCY * CONCURRENCY：并发计费 * CLIENT：按接入端计费 * CLIENT_TOKENS: 按接入端计费（TOKENS）

        :param billing_mode: The billing_mode of this SmartChatRoomBaseInfo.
        :type billing_mode: str
        """
        self._billing_mode = billing_mode

    @property
    def reuse_resource(self):
        r"""Gets the reuse_resource of this SmartChatRoomBaseInfo.

        是否允许使用未分配的并发数（端模式下不能复用），默认不使用。

        :return: The reuse_resource of this SmartChatRoomBaseInfo.
        :rtype: bool
        """
        return self._reuse_resource

    @reuse_resource.setter
    def reuse_resource(self, reuse_resource):
        r"""Sets the reuse_resource of this SmartChatRoomBaseInfo.

        是否允许使用未分配的并发数（端模式下不能复用），默认不使用。

        :param reuse_resource: The reuse_resource of this SmartChatRoomBaseInfo.
        :type reuse_resource: bool
        """
        self._reuse_resource = reuse_resource

    @property
    def concurrency(self):
        r"""Gets the concurrency of this SmartChatRoomBaseInfo.

        **参数解释**： 并发路数。

        :return: The concurrency of this SmartChatRoomBaseInfo.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        r"""Sets the concurrency of this SmartChatRoomBaseInfo.

        **参数解释**： 并发路数。

        :param concurrency: The concurrency of this SmartChatRoomBaseInfo.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def client_nums(self):
        r"""Gets the client_nums of this SmartChatRoomBaseInfo.

        **参数解释**： 允许接入终端端数量。

        :return: The client_nums of this SmartChatRoomBaseInfo.
        :rtype: int
        """
        return self._client_nums

    @client_nums.setter
    def client_nums(self, client_nums):
        r"""Sets the client_nums of this SmartChatRoomBaseInfo.

        **参数解释**： 允许接入终端端数量。

        :param client_nums: The client_nums of this SmartChatRoomBaseInfo.
        :type client_nums: int
        """
        self._client_nums = client_nums

    @property
    def voice_config_list(self):
        r"""Gets the voice_config_list of this SmartChatRoomBaseInfo.

        语音配置参数列表。

        :return: The voice_config_list of this SmartChatRoomBaseInfo.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.VoiceConfigRsp`]
        """
        return self._voice_config_list

    @voice_config_list.setter
    def voice_config_list(self, voice_config_list):
        r"""Sets the voice_config_list of this SmartChatRoomBaseInfo.

        语音配置参数列表。

        :param voice_config_list: The voice_config_list of this SmartChatRoomBaseInfo.
        :type voice_config_list: list[:class:`huaweicloudsdkmetastudio.v1.VoiceConfigRsp`]
        """
        self._voice_config_list = voice_config_list

    @property
    def default_language(self):
        r"""Gets the default_language of this SmartChatRoomBaseInfo.

        默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :return: The default_language of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        r"""Sets the default_language of this SmartChatRoomBaseInfo.

        默认语言，智能交互接口使用。默认值CN。 * CN：简体中文。 * EN：英语。 * ESP：西班牙语（仅海外站点支持） * por：葡萄牙语（仅海外站点支持） * Arabic：阿拉伯语（仅海外站点支持） * Thai：泰语（仅海外站点支持）

        :param default_language: The default_language of this SmartChatRoomBaseInfo.
        :type default_language: str
        """
        self._default_language = default_language

    @property
    def create_time(self):
        r"""Gets the create_time of this SmartChatRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The create_time of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this SmartChatRoomBaseInfo.

        创建时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param create_time: The create_time of this SmartChatRoomBaseInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this SmartChatRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :return: The update_time of this SmartChatRoomBaseInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this SmartChatRoomBaseInfo.

        更新时间，格式遵循：RFC 3339 如“2021-01-10T08:43:17Z”。

        :param update_time: The update_time of this SmartChatRoomBaseInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def exit_mute_threshold(self):
        r"""Gets the exit_mute_threshold of this SmartChatRoomBaseInfo.

        **参数解释**： 静默退出时长。

        :return: The exit_mute_threshold of this SmartChatRoomBaseInfo.
        :rtype: int
        """
        return self._exit_mute_threshold

    @exit_mute_threshold.setter
    def exit_mute_threshold(self, exit_mute_threshold):
        r"""Sets the exit_mute_threshold of this SmartChatRoomBaseInfo.

        **参数解释**： 静默退出时长。

        :param exit_mute_threshold: The exit_mute_threshold of this SmartChatRoomBaseInfo.
        :type exit_mute_threshold: int
        """
        self._exit_mute_threshold = exit_mute_threshold

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
