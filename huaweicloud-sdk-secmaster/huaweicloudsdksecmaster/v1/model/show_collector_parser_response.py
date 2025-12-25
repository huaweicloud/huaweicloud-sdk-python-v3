# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCollectorParserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_refer_count': 'int',
        'description': 'str',
        'modules': 'list[ShowModuleVo]',
        'parser_id': 'str',
        'title': 'str'
    }

    attribute_map = {
        'channel_refer_count': 'channel_refer_count',
        'description': 'description',
        'modules': 'modules',
        'parser_id': 'parser_id',
        'title': 'title'
    }

    def __init__(self, channel_refer_count=None, description=None, modules=None, parser_id=None, title=None):
        r"""ShowCollectorParserResponse

        The model defined in huaweicloud sdk

        :param channel_refer_count: 数值
        :type channel_refer_count: int
        :param description: 描述信息
        :type description: str
        :param modules: 相关描述信息
        :type modules: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        :param parser_id: UUID
        :type parser_id: str
        :param title: 相关标题
        :type title: str
        """
        
        super().__init__()

        self._channel_refer_count = None
        self._description = None
        self._modules = None
        self._parser_id = None
        self._title = None
        self.discriminator = None

        if channel_refer_count is not None:
            self.channel_refer_count = channel_refer_count
        if description is not None:
            self.description = description
        if modules is not None:
            self.modules = modules
        if parser_id is not None:
            self.parser_id = parser_id
        if title is not None:
            self.title = title

    @property
    def channel_refer_count(self):
        r"""Gets the channel_refer_count of this ShowCollectorParserResponse.

        数值

        :return: The channel_refer_count of this ShowCollectorParserResponse.
        :rtype: int
        """
        return self._channel_refer_count

    @channel_refer_count.setter
    def channel_refer_count(self, channel_refer_count):
        r"""Sets the channel_refer_count of this ShowCollectorParserResponse.

        数值

        :param channel_refer_count: The channel_refer_count of this ShowCollectorParserResponse.
        :type channel_refer_count: int
        """
        self._channel_refer_count = channel_refer_count

    @property
    def description(self):
        r"""Gets the description of this ShowCollectorParserResponse.

        描述信息

        :return: The description of this ShowCollectorParserResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCollectorParserResponse.

        描述信息

        :param description: The description of this ShowCollectorParserResponse.
        :type description: str
        """
        self._description = description

    @property
    def modules(self):
        r"""Gets the modules of this ShowCollectorParserResponse.

        相关描述信息

        :return: The modules of this ShowCollectorParserResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        r"""Sets the modules of this ShowCollectorParserResponse.

        相关描述信息

        :param modules: The modules of this ShowCollectorParserResponse.
        :type modules: list[:class:`huaweicloudsdksecmaster.v1.ShowModuleVo`]
        """
        self._modules = modules

    @property
    def parser_id(self):
        r"""Gets the parser_id of this ShowCollectorParserResponse.

        UUID

        :return: The parser_id of this ShowCollectorParserResponse.
        :rtype: str
        """
        return self._parser_id

    @parser_id.setter
    def parser_id(self, parser_id):
        r"""Sets the parser_id of this ShowCollectorParserResponse.

        UUID

        :param parser_id: The parser_id of this ShowCollectorParserResponse.
        :type parser_id: str
        """
        self._parser_id = parser_id

    @property
    def title(self):
        r"""Gets the title of this ShowCollectorParserResponse.

        相关标题

        :return: The title of this ShowCollectorParserResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowCollectorParserResponse.

        相关标题

        :param title: The title of this ShowCollectorParserResponse.
        :type title: str
        """
        self._title = title

    def to_dict(self):
        import warnings
        warnings.warn("ShowCollectorParserResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowCollectorParserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
