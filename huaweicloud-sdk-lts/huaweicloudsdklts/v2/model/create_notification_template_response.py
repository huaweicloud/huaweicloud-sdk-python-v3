# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotificationTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'list[str]',
        'desc': 'str',
        'source': 'str',
        'templates': 'list[SubTemplateResBody]',
        'locale': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'desc': 'desc',
        'source': 'source',
        'templates': 'templates',
        'locale': 'locale'
    }

    def __init__(self, name=None, type=None, desc=None, source=None, templates=None, locale=None):
        r"""CreateNotificationTemplateResponse

        The model defined in huaweicloud sdk

        :param name: **参数解释：**  消息模板名称。 **取值范围：**  不涉及。
        :type name: str
        :param type: **参数解释：**  消息通知方式。 **取值范围：**  - sms - dingding - wechat - webhook - email - voice - feishu - welink
        :type type: list[str]
        :param desc: **参数解释：**  消息模板描述。 **取值范围：**  不涉及。
        :type desc: str
        :param source: **参数解释：**  消息模板来源。 **取值范围：**  不涉及。
        :type source: str
        :param templates: **参数解释：**  不同通知渠道下消息模板的详细信息。
        :type templates: list[:class:`huaweicloudsdklts.v2.SubTemplateResBody`]
        :param locale: **参数解释：**  消息头语言，系统在发送消息时会默认添加消息头，中文如：“尊敬的用户...”；英文如：“Dear User...”。 **取值范围：**  - zh-cn - en-us
        :type locale: str
        """
        
        super().__init__()

        self._name = None
        self._type = None
        self._desc = None
        self._source = None
        self._templates = None
        self._locale = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if desc is not None:
            self.desc = desc
        if source is not None:
            self.source = source
        if templates is not None:
            self.templates = templates
        if locale is not None:
            self.locale = locale

    @property
    def name(self):
        r"""Gets the name of this CreateNotificationTemplateResponse.

        **参数解释：**  消息模板名称。 **取值范围：**  不涉及。

        :return: The name of this CreateNotificationTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateNotificationTemplateResponse.

        **参数解释：**  消息模板名称。 **取值范围：**  不涉及。

        :param name: The name of this CreateNotificationTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this CreateNotificationTemplateResponse.

        **参数解释：**  消息通知方式。 **取值范围：**  - sms - dingding - wechat - webhook - email - voice - feishu - welink

        :return: The type of this CreateNotificationTemplateResponse.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateNotificationTemplateResponse.

        **参数解释：**  消息通知方式。 **取值范围：**  - sms - dingding - wechat - webhook - email - voice - feishu - welink

        :param type: The type of this CreateNotificationTemplateResponse.
        :type type: list[str]
        """
        self._type = type

    @property
    def desc(self):
        r"""Gets the desc of this CreateNotificationTemplateResponse.

        **参数解释：**  消息模板描述。 **取值范围：**  不涉及。

        :return: The desc of this CreateNotificationTemplateResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this CreateNotificationTemplateResponse.

        **参数解释：**  消息模板描述。 **取值范围：**  不涉及。

        :param desc: The desc of this CreateNotificationTemplateResponse.
        :type desc: str
        """
        self._desc = desc

    @property
    def source(self):
        r"""Gets the source of this CreateNotificationTemplateResponse.

        **参数解释：**  消息模板来源。 **取值范围：**  不涉及。

        :return: The source of this CreateNotificationTemplateResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateNotificationTemplateResponse.

        **参数解释：**  消息模板来源。 **取值范围：**  不涉及。

        :param source: The source of this CreateNotificationTemplateResponse.
        :type source: str
        """
        self._source = source

    @property
    def templates(self):
        r"""Gets the templates of this CreateNotificationTemplateResponse.

        **参数解释：**  不同通知渠道下消息模板的详细信息。

        :return: The templates of this CreateNotificationTemplateResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.SubTemplateResBody`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this CreateNotificationTemplateResponse.

        **参数解释：**  不同通知渠道下消息模板的详细信息。

        :param templates: The templates of this CreateNotificationTemplateResponse.
        :type templates: list[:class:`huaweicloudsdklts.v2.SubTemplateResBody`]
        """
        self._templates = templates

    @property
    def locale(self):
        r"""Gets the locale of this CreateNotificationTemplateResponse.

        **参数解释：**  消息头语言，系统在发送消息时会默认添加消息头，中文如：“尊敬的用户...”；英文如：“Dear User...”。 **取值范围：**  - zh-cn - en-us

        :return: The locale of this CreateNotificationTemplateResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this CreateNotificationTemplateResponse.

        **参数解释：**  消息头语言，系统在发送消息时会默认添加消息头，中文如：“尊敬的用户...”；英文如：“Dear User...”。 **取值范围：**  - zh-cn - en-us

        :param locale: The locale of this CreateNotificationTemplateResponse.
        :type locale: str
        """
        self._locale = locale

    def to_dict(self):
        import warnings
        warnings.warn("CreateNotificationTemplateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, CreateNotificationTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
