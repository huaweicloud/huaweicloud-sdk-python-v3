# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AudioCreateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'AudioInputBody',
        'biz_type': 'str',
        'event_type': 'str',
        'categories': 'list[str]',
        'param_callback': 'str'
    }

    attribute_map = {
        'data': 'data',
        'biz_type': 'biz_type',
        'event_type': 'event_type',
        'categories': 'categories',
        'param_callback': 'callback'
    }

    def __init__(self, data=None, biz_type=None, event_type=None, categories=None, param_callback=None):
        """AudioCreateRequest

        The model defined in huaweicloud sdk

        :param data: 
        :type data: :class:`huaweicloudsdkmoderation.v3.AudioInputBody`
        :param biz_type: 用户在控制台界面创建的biz_type名称，如果请求参数中传了biz_type则优先使用biz_type；如果用户没传biz_type则event_type和categories必须传。
        :type biz_type: str
        :param event_type: 事件类型，可选值如下： default：默认事件 audiobook：有声书 education：教育音频 game：游戏语音房 live：秀场直播 ecommerce：电商直播 voiceroom：交友语音房 private：私密语音聊天
        :type event_type: str
        :param categories: 需要检测的风险类型，列表不能为空。 风险类型如下： - porn：涉黄检测 - ad：广告检测 - moan：娇喘检测 - abuse：辱骂检测
        :type categories: list[str]
        :param param_callback: 回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。
        :type param_callback: str
        """
        
        

        self._data = None
        self._biz_type = None
        self._event_type = None
        self._categories = None
        self._param_callback = None
        self.discriminator = None

        self.data = data
        if biz_type is not None:
            self.biz_type = biz_type
        if event_type is not None:
            self.event_type = event_type
        if categories is not None:
            self.categories = categories
        if param_callback is not None:
            self.param_callback = param_callback

    @property
    def data(self):
        """Gets the data of this AudioCreateRequest.

        :return: The data of this AudioCreateRequest.
        :rtype: :class:`huaweicloudsdkmoderation.v3.AudioInputBody`
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this AudioCreateRequest.

        :param data: The data of this AudioCreateRequest.
        :type data: :class:`huaweicloudsdkmoderation.v3.AudioInputBody`
        """
        self._data = data

    @property
    def biz_type(self):
        """Gets the biz_type of this AudioCreateRequest.

        用户在控制台界面创建的biz_type名称，如果请求参数中传了biz_type则优先使用biz_type；如果用户没传biz_type则event_type和categories必须传。

        :return: The biz_type of this AudioCreateRequest.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this AudioCreateRequest.

        用户在控制台界面创建的biz_type名称，如果请求参数中传了biz_type则优先使用biz_type；如果用户没传biz_type则event_type和categories必须传。

        :param biz_type: The biz_type of this AudioCreateRequest.
        :type biz_type: str
        """
        self._biz_type = biz_type

    @property
    def event_type(self):
        """Gets the event_type of this AudioCreateRequest.

        事件类型，可选值如下： default：默认事件 audiobook：有声书 education：教育音频 game：游戏语音房 live：秀场直播 ecommerce：电商直播 voiceroom：交友语音房 private：私密语音聊天

        :return: The event_type of this AudioCreateRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this AudioCreateRequest.

        事件类型，可选值如下： default：默认事件 audiobook：有声书 education：教育音频 game：游戏语音房 live：秀场直播 ecommerce：电商直播 voiceroom：交友语音房 private：私密语音聊天

        :param event_type: The event_type of this AudioCreateRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def categories(self):
        """Gets the categories of this AudioCreateRequest.

        需要检测的风险类型，列表不能为空。 风险类型如下： - porn：涉黄检测 - ad：广告检测 - moan：娇喘检测 - abuse：辱骂检测

        :return: The categories of this AudioCreateRequest.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this AudioCreateRequest.

        需要检测的风险类型，列表不能为空。 风险类型如下： - porn：涉黄检测 - ad：广告检测 - moan：娇喘检测 - abuse：辱骂检测

        :param categories: The categories of this AudioCreateRequest.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def param_callback(self):
        """Gets the param_callback of this AudioCreateRequest.

        回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。

        :return: The param_callback of this AudioCreateRequest.
        :rtype: str
        """
        return self._param_callback

    @param_callback.setter
    def param_callback(self, param_callback):
        """Sets the param_callback of this AudioCreateRequest.

        回调http接口：当该字段非空时，服务将根据该字段回调通知用户审核结果。

        :param param_callback: The param_callback of this AudioCreateRequest.
        :type param_callback: str
        """
        self._param_callback = param_callback

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
        if not isinstance(other, AudioCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
