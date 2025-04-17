# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RobotInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'robot_id': 'str',
        'name': 'str',
        'room_id': 'str',
        'app_id': 'str',
        'app_type': 'int',
        'app_key': 'str',
        'robot_type': 'RobotTypeEnum',
        'language': 'LanguageEnum',
        'create_time': 'str',
        'update_time': 'str',
        'region': 'int',
        'cbs_project_id': 'str',
        'llm_url': 'str',
        'is_stream': 'bool',
        'chat_rounds': 'int',
        'is_ifly_production': 'bool',
        'tail_silence_time': 'int',
        'role_id': 'str',
        'sis_region': 'int',
        'sis_project_id': 'str',
        'enable_hot_words': 'bool',
        'enable_question_audit': 'bool',
        'asr_type': 'AsrTypeEnum',
        'asr_account': 'str'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'name': 'name',
        'room_id': 'room_id',
        'app_id': 'app_id',
        'app_type': 'app_type',
        'app_key': 'app_key',
        'robot_type': 'robot_type',
        'language': 'language',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'region': 'region',
        'cbs_project_id': 'cbs_project_id',
        'llm_url': 'llm_url',
        'is_stream': 'is_stream',
        'chat_rounds': 'chat_rounds',
        'is_ifly_production': 'is_ifly_production',
        'tail_silence_time': 'tail_silence_time',
        'role_id': 'role_id',
        'sis_region': 'sis_region',
        'sis_project_id': 'sis_project_id',
        'enable_hot_words': 'enable_hot_words',
        'enable_question_audit': 'enable_question_audit',
        'asr_type': 'asr_type',
        'asr_account': 'asr_account'
    }

    def __init__(self, robot_id=None, name=None, room_id=None, app_id=None, app_type=None, app_key=None, robot_type=None, language=None, create_time=None, update_time=None, region=None, cbs_project_id=None, llm_url=None, is_stream=None, chat_rounds=None, is_ifly_production=None, tail_silence_time=None, role_id=None, sis_region=None, sis_project_id=None, enable_hot_words=None, enable_question_audit=None, asr_type=None, asr_account=None):
        r"""RobotInfo

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param name: 应用名称。
        :type name: str
        :param room_id: 智能交互对话房间ID。
        :type room_id: str
        :param app_id: 第三方应用ID。
        :type app_id: str
        :param app_type: 对接第三方应用厂商类型。 &gt; 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型；7：交互助手；8：奇妙问
        :type app_type: int
        :param app_key: 应用的AccessKey或帐号。
        :type app_key: str
        :param robot_type: 
        :type robot_type: :class:`huaweicloudsdkmetastudio.v1.RobotTypeEnum`
        :param language: 
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        :param create_time: 创建时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type create_time: str
        :param update_time: 更新时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;。
        :type update_time: str
        :param region: CBS所在区域
        :type region: int
        :param cbs_project_id: CBS所在区域的projectId
        :type cbs_project_id: str
        :param llm_url: 第三方语言模型地址。
        :type llm_url: str
        :param is_stream: 是否采用流式响应。
        :type is_stream: bool
        :param chat_rounds: 支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。
        :type chat_rounds: int
        :param is_ifly_production: 是否为正式环境
        :type is_ifly_production: bool
        :param tail_silence_time: 语音识别后端点静音时长默认500ms
        :type tail_silence_time: int
        :param role_id: 奇妙问角色ID。
        :type role_id: str
        :param sis_region: SIS所在区域
        :type sis_region: int
        :param sis_project_id: SIS所在区域的projectId
        :type sis_project_id: str
        :param enable_hot_words: 是否开启热词
        :type enable_hot_words: bool
        :param enable_question_audit: 是否开启提问文本审核开关
        :type enable_question_audit: bool
        :param asr_type: 
        :type asr_type: :class:`huaweicloudsdkmetastudio.v1.AsrTypeEnum`
        :param asr_account: ASR帐号。
        :type asr_account: str
        """
        
        

        self._robot_id = None
        self._name = None
        self._room_id = None
        self._app_id = None
        self._app_type = None
        self._app_key = None
        self._robot_type = None
        self._language = None
        self._create_time = None
        self._update_time = None
        self._region = None
        self._cbs_project_id = None
        self._llm_url = None
        self._is_stream = None
        self._chat_rounds = None
        self._is_ifly_production = None
        self._tail_silence_time = None
        self._role_id = None
        self._sis_region = None
        self._sis_project_id = None
        self._enable_hot_words = None
        self._enable_question_audit = None
        self._asr_type = None
        self._asr_account = None
        self.discriminator = None

        if robot_id is not None:
            self.robot_id = robot_id
        if name is not None:
            self.name = name
        if room_id is not None:
            self.room_id = room_id
        if app_id is not None:
            self.app_id = app_id
        if app_type is not None:
            self.app_type = app_type
        if app_key is not None:
            self.app_key = app_key
        if robot_type is not None:
            self.robot_type = robot_type
        if language is not None:
            self.language = language
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if region is not None:
            self.region = region
        if cbs_project_id is not None:
            self.cbs_project_id = cbs_project_id
        if llm_url is not None:
            self.llm_url = llm_url
        if is_stream is not None:
            self.is_stream = is_stream
        if chat_rounds is not None:
            self.chat_rounds = chat_rounds
        if is_ifly_production is not None:
            self.is_ifly_production = is_ifly_production
        if tail_silence_time is not None:
            self.tail_silence_time = tail_silence_time
        if role_id is not None:
            self.role_id = role_id
        if sis_region is not None:
            self.sis_region = sis_region
        if sis_project_id is not None:
            self.sis_project_id = sis_project_id
        if enable_hot_words is not None:
            self.enable_hot_words = enable_hot_words
        if enable_question_audit is not None:
            self.enable_question_audit = enable_question_audit
        if asr_type is not None:
            self.asr_type = asr_type
        if asr_account is not None:
            self.asr_account = asr_account

    @property
    def robot_id(self):
        r"""Gets the robot_id of this RobotInfo.

        应用ID。

        :return: The robot_id of this RobotInfo.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        r"""Sets the robot_id of this RobotInfo.

        应用ID。

        :param robot_id: The robot_id of this RobotInfo.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def name(self):
        r"""Gets the name of this RobotInfo.

        应用名称。

        :return: The name of this RobotInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RobotInfo.

        应用名称。

        :param name: The name of this RobotInfo.
        :type name: str
        """
        self._name = name

    @property
    def room_id(self):
        r"""Gets the room_id of this RobotInfo.

        智能交互对话房间ID。

        :return: The room_id of this RobotInfo.
        :rtype: str
        """
        return self._room_id

    @room_id.setter
    def room_id(self, room_id):
        r"""Sets the room_id of this RobotInfo.

        智能交互对话房间ID。

        :param room_id: The room_id of this RobotInfo.
        :type room_id: str
        """
        self._room_id = room_id

    @property
    def app_id(self):
        r"""Gets the app_id of this RobotInfo.

        第三方应用ID。

        :return: The app_id of this RobotInfo.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this RobotInfo.

        第三方应用ID。

        :param app_id: The app_id of this RobotInfo.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_type(self):
        r"""Gets the app_type of this RobotInfo.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型；7：交互助手；8：奇妙问

        :return: The app_type of this RobotInfo.
        :rtype: int
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this RobotInfo.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型；7：交互助手；8：奇妙问

        :param app_type: The app_type of this RobotInfo.
        :type app_type: int
        """
        self._app_type = app_type

    @property
    def app_key(self):
        r"""Gets the app_key of this RobotInfo.

        应用的AccessKey或帐号。

        :return: The app_key of this RobotInfo.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        r"""Sets the app_key of this RobotInfo.

        应用的AccessKey或帐号。

        :param app_key: The app_key of this RobotInfo.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def robot_type(self):
        r"""Gets the robot_type of this RobotInfo.

        :return: The robot_type of this RobotInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.RobotTypeEnum`
        """
        return self._robot_type

    @robot_type.setter
    def robot_type(self, robot_type):
        r"""Sets the robot_type of this RobotInfo.

        :param robot_type: The robot_type of this RobotInfo.
        :type robot_type: :class:`huaweicloudsdkmetastudio.v1.RobotTypeEnum`
        """
        self._robot_type = robot_type

    @property
    def language(self):
        r"""Gets the language of this RobotInfo.

        :return: The language of this RobotInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this RobotInfo.

        :param language: The language of this RobotInfo.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def create_time(self):
        r"""Gets the create_time of this RobotInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this RobotInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this RobotInfo.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this RobotInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this RobotInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this RobotInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this RobotInfo.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this RobotInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def region(self):
        r"""Gets the region of this RobotInfo.

        CBS所在区域

        :return: The region of this RobotInfo.
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this RobotInfo.

        CBS所在区域

        :param region: The region of this RobotInfo.
        :type region: int
        """
        self._region = region

    @property
    def cbs_project_id(self):
        r"""Gets the cbs_project_id of this RobotInfo.

        CBS所在区域的projectId

        :return: The cbs_project_id of this RobotInfo.
        :rtype: str
        """
        return self._cbs_project_id

    @cbs_project_id.setter
    def cbs_project_id(self, cbs_project_id):
        r"""Sets the cbs_project_id of this RobotInfo.

        CBS所在区域的projectId

        :param cbs_project_id: The cbs_project_id of this RobotInfo.
        :type cbs_project_id: str
        """
        self._cbs_project_id = cbs_project_id

    @property
    def llm_url(self):
        r"""Gets the llm_url of this RobotInfo.

        第三方语言模型地址。

        :return: The llm_url of this RobotInfo.
        :rtype: str
        """
        return self._llm_url

    @llm_url.setter
    def llm_url(self, llm_url):
        r"""Sets the llm_url of this RobotInfo.

        第三方语言模型地址。

        :param llm_url: The llm_url of this RobotInfo.
        :type llm_url: str
        """
        self._llm_url = llm_url

    @property
    def is_stream(self):
        r"""Gets the is_stream of this RobotInfo.

        是否采用流式响应。

        :return: The is_stream of this RobotInfo.
        :rtype: bool
        """
        return self._is_stream

    @is_stream.setter
    def is_stream(self, is_stream):
        r"""Sets the is_stream of this RobotInfo.

        是否采用流式响应。

        :param is_stream: The is_stream of this RobotInfo.
        :type is_stream: bool
        """
        self._is_stream = is_stream

    @property
    def chat_rounds(self):
        r"""Gets the chat_rounds of this RobotInfo.

        支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。

        :return: The chat_rounds of this RobotInfo.
        :rtype: int
        """
        return self._chat_rounds

    @chat_rounds.setter
    def chat_rounds(self, chat_rounds):
        r"""Sets the chat_rounds of this RobotInfo.

        支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。

        :param chat_rounds: The chat_rounds of this RobotInfo.
        :type chat_rounds: int
        """
        self._chat_rounds = chat_rounds

    @property
    def is_ifly_production(self):
        r"""Gets the is_ifly_production of this RobotInfo.

        是否为正式环境

        :return: The is_ifly_production of this RobotInfo.
        :rtype: bool
        """
        return self._is_ifly_production

    @is_ifly_production.setter
    def is_ifly_production(self, is_ifly_production):
        r"""Sets the is_ifly_production of this RobotInfo.

        是否为正式环境

        :param is_ifly_production: The is_ifly_production of this RobotInfo.
        :type is_ifly_production: bool
        """
        self._is_ifly_production = is_ifly_production

    @property
    def tail_silence_time(self):
        r"""Gets the tail_silence_time of this RobotInfo.

        语音识别后端点静音时长默认500ms

        :return: The tail_silence_time of this RobotInfo.
        :rtype: int
        """
        return self._tail_silence_time

    @tail_silence_time.setter
    def tail_silence_time(self, tail_silence_time):
        r"""Sets the tail_silence_time of this RobotInfo.

        语音识别后端点静音时长默认500ms

        :param tail_silence_time: The tail_silence_time of this RobotInfo.
        :type tail_silence_time: int
        """
        self._tail_silence_time = tail_silence_time

    @property
    def role_id(self):
        r"""Gets the role_id of this RobotInfo.

        奇妙问角色ID。

        :return: The role_id of this RobotInfo.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this RobotInfo.

        奇妙问角色ID。

        :param role_id: The role_id of this RobotInfo.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def sis_region(self):
        r"""Gets the sis_region of this RobotInfo.

        SIS所在区域

        :return: The sis_region of this RobotInfo.
        :rtype: int
        """
        return self._sis_region

    @sis_region.setter
    def sis_region(self, sis_region):
        r"""Sets the sis_region of this RobotInfo.

        SIS所在区域

        :param sis_region: The sis_region of this RobotInfo.
        :type sis_region: int
        """
        self._sis_region = sis_region

    @property
    def sis_project_id(self):
        r"""Gets the sis_project_id of this RobotInfo.

        SIS所在区域的projectId

        :return: The sis_project_id of this RobotInfo.
        :rtype: str
        """
        return self._sis_project_id

    @sis_project_id.setter
    def sis_project_id(self, sis_project_id):
        r"""Sets the sis_project_id of this RobotInfo.

        SIS所在区域的projectId

        :param sis_project_id: The sis_project_id of this RobotInfo.
        :type sis_project_id: str
        """
        self._sis_project_id = sis_project_id

    @property
    def enable_hot_words(self):
        r"""Gets the enable_hot_words of this RobotInfo.

        是否开启热词

        :return: The enable_hot_words of this RobotInfo.
        :rtype: bool
        """
        return self._enable_hot_words

    @enable_hot_words.setter
    def enable_hot_words(self, enable_hot_words):
        r"""Sets the enable_hot_words of this RobotInfo.

        是否开启热词

        :param enable_hot_words: The enable_hot_words of this RobotInfo.
        :type enable_hot_words: bool
        """
        self._enable_hot_words = enable_hot_words

    @property
    def enable_question_audit(self):
        r"""Gets the enable_question_audit of this RobotInfo.

        是否开启提问文本审核开关

        :return: The enable_question_audit of this RobotInfo.
        :rtype: bool
        """
        return self._enable_question_audit

    @enable_question_audit.setter
    def enable_question_audit(self, enable_question_audit):
        r"""Sets the enable_question_audit of this RobotInfo.

        是否开启提问文本审核开关

        :param enable_question_audit: The enable_question_audit of this RobotInfo.
        :type enable_question_audit: bool
        """
        self._enable_question_audit = enable_question_audit

    @property
    def asr_type(self):
        r"""Gets the asr_type of this RobotInfo.

        :return: The asr_type of this RobotInfo.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.AsrTypeEnum`
        """
        return self._asr_type

    @asr_type.setter
    def asr_type(self, asr_type):
        r"""Sets the asr_type of this RobotInfo.

        :param asr_type: The asr_type of this RobotInfo.
        :type asr_type: :class:`huaweicloudsdkmetastudio.v1.AsrTypeEnum`
        """
        self._asr_type = asr_type

    @property
    def asr_account(self):
        r"""Gets the asr_account of this RobotInfo.

        ASR帐号。

        :return: The asr_account of this RobotInfo.
        :rtype: str
        """
        return self._asr_account

    @asr_account.setter
    def asr_account(self, asr_account):
        r"""Sets the asr_account of this RobotInfo.

        ASR帐号。

        :param asr_account: The asr_account of this RobotInfo.
        :type asr_account: str
        """
        self._asr_account = asr_account

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
        if not isinstance(other, RobotInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
