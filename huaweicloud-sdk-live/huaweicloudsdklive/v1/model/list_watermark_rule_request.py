# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWatermarkRuleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'domain': 'str',
        'app': 'str',
        'channel_id': 'str',
        'stream': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'domain': 'domain',
        'app': 'app',
        'channel_id': 'channel_id',
        'stream': 'stream',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, template_id=None, domain=None, app=None, channel_id=None, stream=None, offset=None, limit=None):
        r"""ListWatermarkRuleRequest

        The model defined in huaweicloud sdk

        :param template_id: 水印模板ID
        :type template_id: str
        :param domain: 推流域名
        :type domain: str
        :param app: 推流appname
        :type app: str
        :param channel_id: OTT场景，频道ID
        :type channel_id: str
        :param stream: OTT场景，填转码模板ID，云直播填流名
        :type stream: str
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        :param limit: 每页记录数，取值范围[1,100]，默认值10
        :type limit: int
        """
        
        

        self._template_id = None
        self._domain = None
        self._app = None
        self._channel_id = None
        self._stream = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if domain is not None:
            self.domain = domain
        if app is not None:
            self.app = app
        if channel_id is not None:
            self.channel_id = channel_id
        if stream is not None:
            self.stream = stream
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def template_id(self):
        r"""Gets the template_id of this ListWatermarkRuleRequest.

        水印模板ID

        :return: The template_id of this ListWatermarkRuleRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListWatermarkRuleRequest.

        水印模板ID

        :param template_id: The template_id of this ListWatermarkRuleRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def domain(self):
        r"""Gets the domain of this ListWatermarkRuleRequest.

        推流域名

        :return: The domain of this ListWatermarkRuleRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListWatermarkRuleRequest.

        推流域名

        :param domain: The domain of this ListWatermarkRuleRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app(self):
        r"""Gets the app of this ListWatermarkRuleRequest.

        推流appname

        :return: The app of this ListWatermarkRuleRequest.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this ListWatermarkRuleRequest.

        推流appname

        :param app: The app of this ListWatermarkRuleRequest.
        :type app: str
        """
        self._app = app

    @property
    def channel_id(self):
        r"""Gets the channel_id of this ListWatermarkRuleRequest.

        OTT场景，频道ID

        :return: The channel_id of this ListWatermarkRuleRequest.
        :rtype: str
        """
        return self._channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        r"""Sets the channel_id of this ListWatermarkRuleRequest.

        OTT场景，频道ID

        :param channel_id: The channel_id of this ListWatermarkRuleRequest.
        :type channel_id: str
        """
        self._channel_id = channel_id

    @property
    def stream(self):
        r"""Gets the stream of this ListWatermarkRuleRequest.

        OTT场景，填转码模板ID，云直播填流名

        :return: The stream of this ListWatermarkRuleRequest.
        :rtype: str
        """
        return self._stream

    @stream.setter
    def stream(self, stream):
        r"""Sets the stream of this ListWatermarkRuleRequest.

        OTT场景，填转码模板ID，云直播填流名

        :param stream: The stream of this ListWatermarkRuleRequest.
        :type stream: str
        """
        self._stream = stream

    @property
    def offset(self):
        r"""Gets the offset of this ListWatermarkRuleRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ListWatermarkRuleRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWatermarkRuleRequest.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ListWatermarkRuleRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWatermarkRuleRequest.

        每页记录数，取值范围[1,100]，默认值10

        :return: The limit of this ListWatermarkRuleRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWatermarkRuleRequest.

        每页记录数，取值范围[1,100]，默认值10

        :param limit: The limit of this ListWatermarkRuleRequest.
        :type limit: int
        """
        self._limit = limit

    def to_dict(self):
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
        if not isinstance(other, ListWatermarkRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
