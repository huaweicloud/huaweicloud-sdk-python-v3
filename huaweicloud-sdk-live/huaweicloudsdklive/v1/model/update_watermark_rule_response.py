# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWatermarkRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_name': 'str',
        'template_id': 'str',
        'domain': 'str',
        'app': 'str',
        'stream': 'str',
        'location': 'WatermarkLocation',
        'channel_id': 'str',
        'transcode_template_name': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'template_id': 'template_id',
        'domain': 'domain',
        'app': 'app',
        'stream': 'stream',
        'location': 'location',
        'channel_id': 'channel_id',
        'transcode_template_name': 'transcode_template_name',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, rule_name=None, template_id=None, domain=None, app=None, stream=None, location=None, channel_id=None, transcode_template_name=None, x_request_id=None):
        r"""UpdateWatermarkRuleResponse

        The model defined in huaweicloud sdk

        :param rule_name: 水印规则名称，如果不填会使用默认名称。默认名称的构造规则为“域名:应用名:流名”，示例“example.com:live:stream”。
        :type rule_name: str
        :param template_id: 水印模板ID，只包含数字字母中划线，创建模板时生成
        :type template_id: str
        :param domain: 域名
        :type domain: str
        :param app: APP名。须知：云直播场景是可选配置，媒体直播场景为必选配置。
        :type app: str
        :param stream: 流名OTT场景下，可以不填
        :type stream: str
        :param location: 
        :type location: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        :param channel_id: OTT场景使用，填对应频道的频ID
        :type channel_id: str
        :param transcode_template_name: OTT场景时，填频道对应的转码模板名称
        :type transcode_template_name: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._rule_name = None
        self._template_id = None
        self._domain = None
        self._app = None
        self._stream = None
        self._location = None
        self._channel_id = None
        self._transcode_template_name = None
        self._x_request_id = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if template_id is not None:
            self.template_id = template_id
        if domain is not None:
            self.domain = domain
        if app is not None:
            self.app = app
        if stream is not None:
            self.stream = stream
        if location is not None:
            self.location = location
        if channel_id is not None:
            self.channel_id = channel_id
        if transcode_template_name is not None:
            self.transcode_template_name = transcode_template_name
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def rule_name(self):
        r"""Gets the rule_name of this UpdateWatermarkRuleResponse.

        水印规则名称，如果不填会使用默认名称。默认名称的构造规则为“域名:应用名:流名”，示例“example.com:live:stream”。

        :return: The rule_name of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this UpdateWatermarkRuleResponse.

        水印规则名称，如果不填会使用默认名称。默认名称的构造规则为“域名:应用名:流名”，示例“example.com:live:stream”。

        :param rule_name: The rule_name of this UpdateWatermarkRuleResponse.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def template_id(self):
        r"""Gets the template_id of this UpdateWatermarkRuleResponse.

        水印模板ID，只包含数字字母中划线，创建模板时生成

        :return: The template_id of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this UpdateWatermarkRuleResponse.

        水印模板ID，只包含数字字母中划线，创建模板时生成

        :param template_id: The template_id of this UpdateWatermarkRuleResponse.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def domain(self):
        r"""Gets the domain of this UpdateWatermarkRuleResponse.

        域名

        :return: The domain of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this UpdateWatermarkRuleResponse.

        域名

        :param domain: The domain of this UpdateWatermarkRuleResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def app(self):
        r"""Gets the app of this UpdateWatermarkRuleResponse.

        APP名。须知：云直播场景是可选配置，媒体直播场景为必选配置。

        :return: The app of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this UpdateWatermarkRuleResponse.

        APP名。须知：云直播场景是可选配置，媒体直播场景为必选配置。

        :param app: The app of this UpdateWatermarkRuleResponse.
        :type app: str
        """
        self._app = app

    @property
    def stream(self):
        r"""Gets the stream of this UpdateWatermarkRuleResponse.

        流名OTT场景下，可以不填

        :return: The stream of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this UpdateWatermarkRuleResponse.

        流名OTT场景下，可以不填

        :param stream: The stream of this UpdateWatermarkRuleResponse.
        :type stream: str
        """
        self._stream = stream

    @property
    def location(self):
        r"""Gets the location of this UpdateWatermarkRuleResponse.

        :return: The location of this UpdateWatermarkRuleResponse.
        :rtype: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this UpdateWatermarkRuleResponse.

        :param location: The location of this UpdateWatermarkRuleResponse.
        :type location: :class:`huaweicloudsdklive.v1.WatermarkLocation`
        """
        self._location = location

    @property
    def channel_id(self):
        r"""Gets the channel_id of this UpdateWatermarkRuleResponse.

        OTT场景使用，填对应频道的频ID

        :return: The channel_id of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this UpdateWatermarkRuleResponse.

        OTT场景使用，填对应频道的频ID

        :param channel_id: The channel_id of this UpdateWatermarkRuleResponse.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def transcode_template_name(self):
        r"""Gets the transcode_template_name of this UpdateWatermarkRuleResponse.

        OTT场景时，填频道对应的转码模板名称

        :return: The transcode_template_name of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._transcode_template_name

    @transcode_template_name.setter
    def transcode_template_name(self, transcode_template_name):
        r"""Sets the transcode_template_name of this UpdateWatermarkRuleResponse.

        OTT场景时，填频道对应的转码模板名称

        :param transcode_template_name: The transcode_template_name of this UpdateWatermarkRuleResponse.
        :type transcode_template_name: str
        """
        self._transcode_template_name = transcode_template_name

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this UpdateWatermarkRuleResponse.

        :return: The x_request_id of this UpdateWatermarkRuleResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this UpdateWatermarkRuleResponse.

        :param x_request_id: The x_request_id of this UpdateWatermarkRuleResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("UpdateWatermarkRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateWatermarkRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
