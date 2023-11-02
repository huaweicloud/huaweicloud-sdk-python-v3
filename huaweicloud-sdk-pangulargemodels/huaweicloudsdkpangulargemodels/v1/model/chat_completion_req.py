# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChatCompletionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'messages': 'list[Message]',
        'user': 'str',
        'stream': 'bool',
        'temperature': 'float',
        'top_p': 'float',
        'max_tokens': 'int',
        'n': 'int',
        'presence_penalty': 'float'
    }

    attribute_map = {
        'messages': 'messages',
        'user': 'user',
        'stream': 'stream',
        'temperature': 'temperature',
        'top_p': 'top_p',
        'max_tokens': 'max_tokens',
        'n': 'n',
        'presence_penalty': 'presence_penalty'
    }

    def __init__(self, messages=None, user=None, stream=None, temperature=None, top_p=None, max_tokens=None, n=None, presence_penalty=None):
        """ChatCompletionReq

        The model defined in huaweicloud sdk

        :param messages: 多轮对话问答对
        :type messages: list[:class:`huaweicloudsdkpangulargemodels.v1.Message`]
        :param user: 用于代表客户的唯一标识符，最小长度：1，最大长度64
        :type user: str
        :param stream: 流式调用的开启开关，true为开启流式调用，如果要开启流式调用，请使用流式SDK；false为关闭流式调用。默认为关闭状态（当前API Explorer不支持流式，在API Explorer调试时请使用非流式）。
        :type stream: bool
        :param temperature: 用于控制生成文本的多样性和创造力。参数的取值范围是0到1，其中0表示最低的随机性。一般来说，temperature越低，适合完成确定性的任务。temperature越高，例如0.9，适合完成创造性的任务。temperature参数可以影响语言模型输出的质量和多样性，但也不是唯一的因素。还有其他一些参数，如top_p参数也可以用来调整语言模型的行为和偏好，但不建议同时更改这两个参数。
        :type temperature: float
        :param top_p: 一种替代温度采样的方法，称为nucleus sampling，其中模型考虑具有top_p 概率质量的标记的结果。因此 0.1 意味着只考虑构成前 10% 概率质量的标记。我们通常建议更改此值或温度，但不要同时更改两者。通常建议更改top_p或temperature来调整生成文本的倾向性，但不要同时更改这两个参数。
        :type top_p: float
        :param max_tokens: 用于控制聊天回复的长度和质量。一般来说，较大的max_tokens值可以生成较长和较完整的回复，但也可能增加生成无关或重复内容的风险。较小的max_tokens值可以生成较短和较简洁的回复，但也可能导致生成不完整或不连贯的内容。因此，需要根据不同的场景和需求来选择合适的max_tokens值。最小值：1，最大值：根据模型不同最大值不同。
        :type max_tokens: int
        :param n: 表示对每个问题生成多少条答案。n参数的默认值是1，表示只生成一个答案。如果想要生成多条答案，可以设置n参数为一个大于1的整数，例如n&#x3D;2。这样，API会返回一个包含2个答案的数组。流式调用时，n只能取1。最小值：1，最大值：2，默认值：1
        :type n: int
        :param presence_penalty: 用于控制生成文本中的重复程度。正值会根据它们到目前为止在文本中的现有频率来惩罚新tokens，从而降低模型逐字重复同一行的可能性。  presence_penalty 参数可以用来提高生成文本的多样性和创造性，避免生成单调或重复的内容。最小值：-2，最大值：2
        :type presence_penalty: float
        """
        
        

        self._messages = None
        self._user = None
        self._stream = None
        self._temperature = None
        self._top_p = None
        self._max_tokens = None
        self._n = None
        self._presence_penalty = None
        self.discriminator = None

        self.messages = messages
        if user is not None:
            self.user = user
        if stream is not None:
            self.stream = stream
        if temperature is not None:
            self.temperature = temperature
        if top_p is not None:
            self.top_p = top_p
        if max_tokens is not None:
            self.max_tokens = max_tokens
        if n is not None:
            self.n = n
        if presence_penalty is not None:
            self.presence_penalty = presence_penalty

    @property
    def messages(self):
        """Gets the messages of this ChatCompletionReq.

        多轮对话问答对

        :return: The messages of this ChatCompletionReq.
        :rtype: list[:class:`huaweicloudsdkpangulargemodels.v1.Message`]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this ChatCompletionReq.

        多轮对话问答对

        :param messages: The messages of this ChatCompletionReq.
        :type messages: list[:class:`huaweicloudsdkpangulargemodels.v1.Message`]
        """
        self._messages = messages

    @property
    def user(self):
        """Gets the user of this ChatCompletionReq.

        用于代表客户的唯一标识符，最小长度：1，最大长度64

        :return: The user of this ChatCompletionReq.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ChatCompletionReq.

        用于代表客户的唯一标识符，最小长度：1，最大长度64

        :param user: The user of this ChatCompletionReq.
        :type user: str
        """
        self._user = user

    @property
    def stream(self):
        """Gets the stream of this ChatCompletionReq.

        流式调用的开启开关，true为开启流式调用，如果要开启流式调用，请使用流式SDK；false为关闭流式调用。默认为关闭状态（当前API Explorer不支持流式，在API Explorer调试时请使用非流式）。

        :return: The stream of this ChatCompletionReq.
        :rtype: bool
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        """Sets the stream of this ChatCompletionReq.

        流式调用的开启开关，true为开启流式调用，如果要开启流式调用，请使用流式SDK；false为关闭流式调用。默认为关闭状态（当前API Explorer不支持流式，在API Explorer调试时请使用非流式）。

        :param stream: The stream of this ChatCompletionReq.
        :type stream: bool
        """
        self._stream = stream

    @property
    def temperature(self):
        """Gets the temperature of this ChatCompletionReq.

        用于控制生成文本的多样性和创造力。参数的取值范围是0到1，其中0表示最低的随机性。一般来说，temperature越低，适合完成确定性的任务。temperature越高，例如0.9，适合完成创造性的任务。temperature参数可以影响语言模型输出的质量和多样性，但也不是唯一的因素。还有其他一些参数，如top_p参数也可以用来调整语言模型的行为和偏好，但不建议同时更改这两个参数。

        :return: The temperature of this ChatCompletionReq.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this ChatCompletionReq.

        用于控制生成文本的多样性和创造力。参数的取值范围是0到1，其中0表示最低的随机性。一般来说，temperature越低，适合完成确定性的任务。temperature越高，例如0.9，适合完成创造性的任务。temperature参数可以影响语言模型输出的质量和多样性，但也不是唯一的因素。还有其他一些参数，如top_p参数也可以用来调整语言模型的行为和偏好，但不建议同时更改这两个参数。

        :param temperature: The temperature of this ChatCompletionReq.
        :type temperature: float
        """
        self._temperature = temperature

    @property
    def top_p(self):
        """Gets the top_p of this ChatCompletionReq.

        一种替代温度采样的方法，称为nucleus sampling，其中模型考虑具有top_p 概率质量的标记的结果。因此 0.1 意味着只考虑构成前 10% 概率质量的标记。我们通常建议更改此值或温度，但不要同时更改两者。通常建议更改top_p或temperature来调整生成文本的倾向性，但不要同时更改这两个参数。

        :return: The top_p of this ChatCompletionReq.
        :rtype: float
        """
        return self._top_p

    @top_p.setter
    def top_p(self, top_p):
        """Sets the top_p of this ChatCompletionReq.

        一种替代温度采样的方法，称为nucleus sampling，其中模型考虑具有top_p 概率质量的标记的结果。因此 0.1 意味着只考虑构成前 10% 概率质量的标记。我们通常建议更改此值或温度，但不要同时更改两者。通常建议更改top_p或temperature来调整生成文本的倾向性，但不要同时更改这两个参数。

        :param top_p: The top_p of this ChatCompletionReq.
        :type top_p: float
        """
        self._top_p = top_p

    @property
    def max_tokens(self):
        """Gets the max_tokens of this ChatCompletionReq.

        用于控制聊天回复的长度和质量。一般来说，较大的max_tokens值可以生成较长和较完整的回复，但也可能增加生成无关或重复内容的风险。较小的max_tokens值可以生成较短和较简洁的回复，但也可能导致生成不完整或不连贯的内容。因此，需要根据不同的场景和需求来选择合适的max_tokens值。最小值：1，最大值：根据模型不同最大值不同。

        :return: The max_tokens of this ChatCompletionReq.
        :rtype: int
        """
        return self._max_tokens

    @max_tokens.setter
    def max_tokens(self, max_tokens):
        """Sets the max_tokens of this ChatCompletionReq.

        用于控制聊天回复的长度和质量。一般来说，较大的max_tokens值可以生成较长和较完整的回复，但也可能增加生成无关或重复内容的风险。较小的max_tokens值可以生成较短和较简洁的回复，但也可能导致生成不完整或不连贯的内容。因此，需要根据不同的场景和需求来选择合适的max_tokens值。最小值：1，最大值：根据模型不同最大值不同。

        :param max_tokens: The max_tokens of this ChatCompletionReq.
        :type max_tokens: int
        """
        self._max_tokens = max_tokens

    @property
    def n(self):
        """Gets the n of this ChatCompletionReq.

        表示对每个问题生成多少条答案。n参数的默认值是1，表示只生成一个答案。如果想要生成多条答案，可以设置n参数为一个大于1的整数，例如n=2。这样，API会返回一个包含2个答案的数组。流式调用时，n只能取1。最小值：1，最大值：2，默认值：1

        :return: The n of this ChatCompletionReq.
        :rtype: int
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this ChatCompletionReq.

        表示对每个问题生成多少条答案。n参数的默认值是1，表示只生成一个答案。如果想要生成多条答案，可以设置n参数为一个大于1的整数，例如n=2。这样，API会返回一个包含2个答案的数组。流式调用时，n只能取1。最小值：1，最大值：2，默认值：1

        :param n: The n of this ChatCompletionReq.
        :type n: int
        """
        self._n = n

    @property
    def presence_penalty(self):
        """Gets the presence_penalty of this ChatCompletionReq.

        用于控制生成文本中的重复程度。正值会根据它们到目前为止在文本中的现有频率来惩罚新tokens，从而降低模型逐字重复同一行的可能性。  presence_penalty 参数可以用来提高生成文本的多样性和创造性，避免生成单调或重复的内容。最小值：-2，最大值：2

        :return: The presence_penalty of this ChatCompletionReq.
        :rtype: float
        """
        return self._presence_penalty

    @presence_penalty.setter
    def presence_penalty(self, presence_penalty):
        """Sets the presence_penalty of this ChatCompletionReq.

        用于控制生成文本中的重复程度。正值会根据它们到目前为止在文本中的现有频率来惩罚新tokens，从而降低模型逐字重复同一行的可能性。  presence_penalty 参数可以用来提高生成文本的多样性和创造性，避免生成单调或重复的内容。最小值：-2，最大值：2

        :param presence_penalty: The presence_penalty of this ChatCompletionReq.
        :type presence_penalty: float
        """
        self._presence_penalty = presence_penalty

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
        if not isinstance(other, ChatCompletionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
