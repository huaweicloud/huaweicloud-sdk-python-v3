# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNotificationTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desc': 'str',
        'locale': 'str',
        'name': 'str',
        'templates': 'str'
    }

    attribute_map = {
        'desc': 'desc',
        'locale': 'locale',
        'name': 'name',
        'templates': 'templates'
    }

    def __init__(self, desc=None, locale=None, name=None, templates=None):
        r"""UpdateNotificationTemplate

        The model defined in huaweicloud sdk

        :param desc: 消息通知模板描述。
        :type desc: str
        :param locale: 消息通知模板语言。
        :type locale: str
        :param name: 消息通知模板名称。通知消息模板名称无法修改
        :type name: str
        :param templates: 消息通知模板内容。 消息通知模板内容为json字符串，具体内容是由下列参数拼接成json数组后转义而来。  | 名称 |是否必选  |参数类型  |说明  | |--|--|--|--| |content  |是  |string  |消息模板内容。|  |subType  |是  |string  |消息模板发送类型，支持：email，sms，webhook。| | topic | 否 | string |邮件主题。| | sendType |否  |string  |当消息模板发送类型为“webhook”时需要指定消息模板格式，支持：HTML、JSON。  | | version |是  |string  |默认为v2。 |
        :type templates: str
        """
        
        

        self._desc = None
        self._locale = None
        self._name = None
        self._templates = None
        self.discriminator = None

        if desc is not None:
            self.desc = desc
        self.locale = locale
        self.name = name
        self.templates = templates

    @property
    def desc(self):
        r"""Gets the desc of this UpdateNotificationTemplate.

        消息通知模板描述。

        :return: The desc of this UpdateNotificationTemplate.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this UpdateNotificationTemplate.

        消息通知模板描述。

        :param desc: The desc of this UpdateNotificationTemplate.
        :type desc: str
        """
        self._desc = desc

    @property
    def locale(self):
        r"""Gets the locale of this UpdateNotificationTemplate.

        消息通知模板语言。

        :return: The locale of this UpdateNotificationTemplate.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this UpdateNotificationTemplate.

        消息通知模板语言。

        :param locale: The locale of this UpdateNotificationTemplate.
        :type locale: str
        """
        self._locale = locale

    @property
    def name(self):
        r"""Gets the name of this UpdateNotificationTemplate.

        消息通知模板名称。通知消息模板名称无法修改

        :return: The name of this UpdateNotificationTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateNotificationTemplate.

        消息通知模板名称。通知消息模板名称无法修改

        :param name: The name of this UpdateNotificationTemplate.
        :type name: str
        """
        self._name = name

    @property
    def templates(self):
        r"""Gets the templates of this UpdateNotificationTemplate.

        消息通知模板内容。 消息通知模板内容为json字符串，具体内容是由下列参数拼接成json数组后转义而来。  | 名称 |是否必选  |参数类型  |说明  | |--|--|--|--| |content  |是  |string  |消息模板内容。|  |subType  |是  |string  |消息模板发送类型，支持：email，sms，webhook。| | topic | 否 | string |邮件主题。| | sendType |否  |string  |当消息模板发送类型为“webhook”时需要指定消息模板格式，支持：HTML、JSON。  | | version |是  |string  |默认为v2。 |

        :return: The templates of this UpdateNotificationTemplate.
        :rtype: str
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this UpdateNotificationTemplate.

        消息通知模板内容。 消息通知模板内容为json字符串，具体内容是由下列参数拼接成json数组后转义而来。  | 名称 |是否必选  |参数类型  |说明  | |--|--|--|--| |content  |是  |string  |消息模板内容。|  |subType  |是  |string  |消息模板发送类型，支持：email，sms，webhook。| | topic | 否 | string |邮件主题。| | sendType |否  |string  |当消息模板发送类型为“webhook”时需要指定消息模板格式，支持：HTML、JSON。  | | version |是  |string  |默认为v2。 |

        :param templates: The templates of this UpdateNotificationTemplate.
        :type templates: str
        """
        self._templates = templates

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
        if not isinstance(other, UpdateNotificationTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
