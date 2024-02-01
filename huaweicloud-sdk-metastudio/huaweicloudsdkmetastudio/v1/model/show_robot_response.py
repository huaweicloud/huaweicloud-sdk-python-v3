# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRobotResponse(SdkResponse):

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
        'app_id': 'str',
        'app_type': 'int',
        'concurrency': 'int',
        'language': 'LanguageEnum',
        'create_time': 'str',
        'update_time': 'str',
        'region': 'int',
        'cbs_project_id': 'str',
        'llm_url': 'str',
        'is_stream': 'bool',
        'chat_rounds': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'robot_id': 'robot_id',
        'name': 'name',
        'app_id': 'app_id',
        'app_type': 'app_type',
        'concurrency': 'concurrency',
        'language': 'language',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'region': 'region',
        'cbs_project_id': 'cbs_project_id',
        'llm_url': 'llm_url',
        'is_stream': 'is_stream',
        'chat_rounds': 'chat_rounds',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, robot_id=None, name=None, app_id=None, app_type=None, concurrency=None, language=None, create_time=None, update_time=None, region=None, cbs_project_id=None, llm_url=None, is_stream=None, chat_rounds=None, x_request_id=None):
        """ShowRobotResponse

        The model defined in huaweicloud sdk

        :param robot_id: 应用ID。
        :type robot_id: str
        :param name: 应用名称。
        :type name: str
        :param app_id: 第三方应用ID。
        :type app_id: str
        :param app_type: 对接第三方应用厂商类型。 &gt; 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型
        :type app_type: int
        :param concurrency: 对话的并发数
        :type concurrency: int
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
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowRobotResponse, self).__init__()

        self._robot_id = None
        self._name = None
        self._app_id = None
        self._app_type = None
        self._concurrency = None
        self._language = None
        self._create_time = None
        self._update_time = None
        self._region = None
        self._cbs_project_id = None
        self._llm_url = None
        self._is_stream = None
        self._chat_rounds = None
        self._x_request_id = None
        self.discriminator = None

        if robot_id is not None:
            self.robot_id = robot_id
        if name is not None:
            self.name = name
        if app_id is not None:
            self.app_id = app_id
        if app_type is not None:
            self.app_type = app_type
        if concurrency is not None:
            self.concurrency = concurrency
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
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def robot_id(self):
        """Gets the robot_id of this ShowRobotResponse.

        应用ID。

        :return: The robot_id of this ShowRobotResponse.
        :rtype: str
        """
        return self._robot_id

    @robot_id.setter
    def robot_id(self, robot_id):
        """Sets the robot_id of this ShowRobotResponse.

        应用ID。

        :param robot_id: The robot_id of this ShowRobotResponse.
        :type robot_id: str
        """
        self._robot_id = robot_id

    @property
    def name(self):
        """Gets the name of this ShowRobotResponse.

        应用名称。

        :return: The name of this ShowRobotResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowRobotResponse.

        应用名称。

        :param name: The name of this ShowRobotResponse.
        :type name: str
        """
        self._name = name

    @property
    def app_id(self):
        """Gets the app_id of this ShowRobotResponse.

        第三方应用ID。

        :return: The app_id of this ShowRobotResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowRobotResponse.

        第三方应用ID。

        :param app_id: The app_id of this ShowRobotResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_type(self):
        """Gets the app_type of this ShowRobotResponse.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型

        :return: The app_type of this ShowRobotResponse.
        :rtype: int
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this ShowRobotResponse.

        对接第三方应用厂商类型。 > 0：科大讯飞AIUI；1：华为云CBS；2：科大讯飞星火交互认知大模型；5：第三方驱动；6：第三方语言模型

        :param app_type: The app_type of this ShowRobotResponse.
        :type app_type: int
        """
        self._app_type = app_type

    @property
    def concurrency(self):
        """Gets the concurrency of this ShowRobotResponse.

        对话的并发数

        :return: The concurrency of this ShowRobotResponse.
        :rtype: int
        """
        return self._concurrency

    @concurrency.setter
    def concurrency(self, concurrency):
        """Sets the concurrency of this ShowRobotResponse.

        对话的并发数

        :param concurrency: The concurrency of this ShowRobotResponse.
        :type concurrency: int
        """
        self._concurrency = concurrency

    @property
    def language(self):
        """Gets the language of this ShowRobotResponse.

        :return: The language of this ShowRobotResponse.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShowRobotResponse.

        :param language: The language of this ShowRobotResponse.
        :type language: :class:`huaweicloudsdkmetastudio.v1.LanguageEnum`
        """
        self._language = language

    @property
    def create_time(self):
        """Gets the create_time of this ShowRobotResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The create_time of this ShowRobotResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowRobotResponse.

        创建时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param create_time: The create_time of this ShowRobotResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowRobotResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :return: The update_time of this ShowRobotResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowRobotResponse.

        更新时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"。

        :param update_time: The update_time of this ShowRobotResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def region(self):
        """Gets the region of this ShowRobotResponse.

        CBS所在区域

        :return: The region of this ShowRobotResponse.
        :rtype: int
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ShowRobotResponse.

        CBS所在区域

        :param region: The region of this ShowRobotResponse.
        :type region: int
        """
        self._region = region

    @property
    def cbs_project_id(self):
        """Gets the cbs_project_id of this ShowRobotResponse.

        CBS所在区域的projectId

        :return: The cbs_project_id of this ShowRobotResponse.
        :rtype: str
        """
        return self._cbs_project_id

    @cbs_project_id.setter
    def cbs_project_id(self, cbs_project_id):
        """Sets the cbs_project_id of this ShowRobotResponse.

        CBS所在区域的projectId

        :param cbs_project_id: The cbs_project_id of this ShowRobotResponse.
        :type cbs_project_id: str
        """
        self._cbs_project_id = cbs_project_id

    @property
    def llm_url(self):
        """Gets the llm_url of this ShowRobotResponse.

        第三方语言模型地址。

        :return: The llm_url of this ShowRobotResponse.
        :rtype: str
        """
        return self._llm_url

    @llm_url.setter
    def llm_url(self, llm_url):
        """Sets the llm_url of this ShowRobotResponse.

        第三方语言模型地址。

        :param llm_url: The llm_url of this ShowRobotResponse.
        :type llm_url: str
        """
        self._llm_url = llm_url

    @property
    def is_stream(self):
        """Gets the is_stream of this ShowRobotResponse.

        是否采用流式响应。

        :return: The is_stream of this ShowRobotResponse.
        :rtype: bool
        """
        return self._is_stream

    @is_stream.setter
    def is_stream(self, is_stream):
        """Sets the is_stream of this ShowRobotResponse.

        是否采用流式响应。

        :param is_stream: The is_stream of this ShowRobotResponse.
        :type is_stream: bool
        """
        self._is_stream = is_stream

    @property
    def chat_rounds(self):
        """Gets the chat_rounds of this ShowRobotResponse.

        支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。

        :return: The chat_rounds of this ShowRobotResponse.
        :rtype: int
        """
        return self._chat_rounds

    @chat_rounds.setter
    def chat_rounds(self, chat_rounds):
        """Sets the chat_rounds of this ShowRobotResponse.

        支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。

        :param chat_rounds: The chat_rounds of this ShowRobotResponse.
        :type chat_rounds: int
        """
        self._chat_rounds = chat_rounds

    @property
    def x_request_id(self):
        """Gets the x_request_id of this ShowRobotResponse.

        :return: The x_request_id of this ShowRobotResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        """Sets the x_request_id of this ShowRobotResponse.

        :param x_request_id: The x_request_id of this ShowRobotResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowRobotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
