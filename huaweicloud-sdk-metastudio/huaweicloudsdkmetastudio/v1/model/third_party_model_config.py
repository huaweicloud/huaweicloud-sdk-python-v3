# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThirdPartyModelConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_key': 'str',
        'llm_url': 'str',
        'is_stream': 'bool',
        'chat_rounds': 'int',
        'sis_region': 'int',
        'sis_project_id': 'str',
        'enable_hot_words': 'bool'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_key': 'app_key',
        'llm_url': 'llm_url',
        'is_stream': 'is_stream',
        'chat_rounds': 'chat_rounds',
        'sis_region': 'sis_region',
        'sis_project_id': 'sis_project_id',
        'enable_hot_words': 'enable_hot_words'
    }

    def __init__(self, app_id=None, app_key=None, llm_url=None, is_stream=None, chat_rounds=None, sis_region=None, sis_project_id=None, enable_hot_words=None):
        """ThirdPartyModelConfig

        The model defined in huaweicloud sdk

        :param app_id: 第三方语言模型应用ID。
        :type app_id: str
        :param app_key: 第三方语言模型应用密钥。
        :type app_key: str
        :param llm_url: 第三方语言模型地址。
        :type llm_url: str
        :param is_stream: 是否采用流式响应。
        :type is_stream: bool
        :param chat_rounds: 支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。
        :type chat_rounds: int
        :param sis_region: SIS所在区域
        :type sis_region: int
        :param sis_project_id: SIS所在区域的projectId
        :type sis_project_id: str
        :param enable_hot_words: 是否开启热词
        :type enable_hot_words: bool
        """
        
        

        self._app_id = None
        self._app_key = None
        self._llm_url = None
        self._is_stream = None
        self._chat_rounds = None
        self._sis_region = None
        self._sis_project_id = None
        self._enable_hot_words = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_key is not None:
            self.app_key = app_key
        if llm_url is not None:
            self.llm_url = llm_url
        if is_stream is not None:
            self.is_stream = is_stream
        if chat_rounds is not None:
            self.chat_rounds = chat_rounds
        if sis_region is not None:
            self.sis_region = sis_region
        if sis_project_id is not None:
            self.sis_project_id = sis_project_id
        if enable_hot_words is not None:
            self.enable_hot_words = enable_hot_words

    @property
    def app_id(self):
        """Gets the app_id of this ThirdPartyModelConfig.

        第三方语言模型应用ID。

        :return: The app_id of this ThirdPartyModelConfig.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ThirdPartyModelConfig.

        第三方语言模型应用ID。

        :param app_id: The app_id of this ThirdPartyModelConfig.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_key(self):
        """Gets the app_key of this ThirdPartyModelConfig.

        第三方语言模型应用密钥。

        :return: The app_key of this ThirdPartyModelConfig.
        :rtype: str
        """
        return self._app_key

    @app_key.setter
    def app_key(self, app_key):
        """Sets the app_key of this ThirdPartyModelConfig.

        第三方语言模型应用密钥。

        :param app_key: The app_key of this ThirdPartyModelConfig.
        :type app_key: str
        """
        self._app_key = app_key

    @property
    def llm_url(self):
        """Gets the llm_url of this ThirdPartyModelConfig.

        第三方语言模型地址。

        :return: The llm_url of this ThirdPartyModelConfig.
        :rtype: str
        """
        return self._llm_url

    @llm_url.setter
    def llm_url(self, llm_url):
        """Sets the llm_url of this ThirdPartyModelConfig.

        第三方语言模型地址。

        :param llm_url: The llm_url of this ThirdPartyModelConfig.
        :type llm_url: str
        """
        self._llm_url = llm_url

    @property
    def is_stream(self):
        """Gets the is_stream of this ThirdPartyModelConfig.

        是否采用流式响应。

        :return: The is_stream of this ThirdPartyModelConfig.
        :rtype: bool
        """
        return self._is_stream

    @is_stream.setter
    def is_stream(self, is_stream):
        """Sets the is_stream of this ThirdPartyModelConfig.

        是否采用流式响应。

        :param is_stream: The is_stream of this ThirdPartyModelConfig.
        :type is_stream: bool
        """
        self._is_stream = is_stream

    @property
    def chat_rounds(self):
        """Gets the chat_rounds of this ThirdPartyModelConfig.

        支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。

        :return: The chat_rounds of this ThirdPartyModelConfig.
        :rtype: int
        """
        return self._chat_rounds

    @chat_rounds.setter
    def chat_rounds(self, chat_rounds):
        """Sets the chat_rounds of this ThirdPartyModelConfig.

        支持的多轮对话数量，取值大于1时，请求第三方语言模型时将携带历史对话信息。

        :param chat_rounds: The chat_rounds of this ThirdPartyModelConfig.
        :type chat_rounds: int
        """
        self._chat_rounds = chat_rounds

    @property
    def sis_region(self):
        """Gets the sis_region of this ThirdPartyModelConfig.

        SIS所在区域

        :return: The sis_region of this ThirdPartyModelConfig.
        :rtype: int
        """
        return self._sis_region

    @sis_region.setter
    def sis_region(self, sis_region):
        """Sets the sis_region of this ThirdPartyModelConfig.

        SIS所在区域

        :param sis_region: The sis_region of this ThirdPartyModelConfig.
        :type sis_region: int
        """
        self._sis_region = sis_region

    @property
    def sis_project_id(self):
        """Gets the sis_project_id of this ThirdPartyModelConfig.

        SIS所在区域的projectId

        :return: The sis_project_id of this ThirdPartyModelConfig.
        :rtype: str
        """
        return self._sis_project_id

    @sis_project_id.setter
    def sis_project_id(self, sis_project_id):
        """Sets the sis_project_id of this ThirdPartyModelConfig.

        SIS所在区域的projectId

        :param sis_project_id: The sis_project_id of this ThirdPartyModelConfig.
        :type sis_project_id: str
        """
        self._sis_project_id = sis_project_id

    @property
    def enable_hot_words(self):
        """Gets the enable_hot_words of this ThirdPartyModelConfig.

        是否开启热词

        :return: The enable_hot_words of this ThirdPartyModelConfig.
        :rtype: bool
        """
        return self._enable_hot_words

    @enable_hot_words.setter
    def enable_hot_words(self, enable_hot_words):
        """Sets the enable_hot_words of this ThirdPartyModelConfig.

        是否开启热词

        :param enable_hot_words: The enable_hot_words of this ThirdPartyModelConfig.
        :type enable_hot_words: bool
        """
        self._enable_hot_words = enable_hot_words

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
        if not isinstance(other, ThirdPartyModelConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
