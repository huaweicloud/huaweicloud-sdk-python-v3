# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationTemplateByNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'create_time': 'int',
        'desc': 'str',
        'enterprise_project_id': 'str',
        'locale': 'str',
        'modify_time': 'int',
        'name': 'str',
        'project_id': 'str',
        'source': 'str',
        'templates': 'str',
        'type': 'list[str]'
    }

    attribute_map = {
        'create_time': 'create_time',
        'desc': 'desc',
        'enterprise_project_id': 'enterprise_project_id',
        'locale': 'locale',
        'modify_time': 'modify_time',
        'name': 'name',
        'project_id': 'project_id',
        'source': 'source',
        'templates': 'templates',
        'type': 'type'
    }

    def __init__(self, create_time=None, desc=None, enterprise_project_id=None, locale=None, modify_time=None, name=None, project_id=None, source=None, templates=None, type=None):
        r"""ListNotificationTemplateByNameResponse

        The model defined in huaweicloud sdk

        :param create_time: 消息通知模板创建时间。
        :type create_time: int
        :param desc: 消息通知模板描述。
        :type desc: str
        :param enterprise_project_id: 消息通知模板所属企业项目id。
        :type enterprise_project_id: str
        :param locale: 消息通知模板语言。
        :type locale: str
        :param modify_time: 消息通知模板修改时间。
        :type modify_time: int
        :param name: 消息通知模板名称。
        :type name: str
        :param project_id: 消息通知模板所属项目id。
        :type project_id: str
        :param source: 消息通知模板来源。
        :type source: str
        :param templates: 消息通知模板内容。 消息通知模板内容为json字符串，具体内容是由下列参数拼接成json数组后转义而来。  | 名称 |是否必选  |参数类型  |说明  | |--|--|--|--| |content  |是  |string  |消息模板内容。|  |subType  |是  |string  |消息模板发送类型，支持：email，sms，webhook。| | topic | 否 | string |邮件主题。| | sendType |否  |string  |当消息模板发送类型为“webhook”时需要指定消息模板格式，支持：HTML、JSON。  | | version |是  |string  |默认为v2。 |
        :type templates: str
        :param type: 消息通知方式。
        :type type: list[str]
        """
        
        super().__init__()

        self._create_time = None
        self._desc = None
        self._enterprise_project_id = None
        self._locale = None
        self._modify_time = None
        self._name = None
        self._project_id = None
        self._source = None
        self._templates = None
        self._type = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if desc is not None:
            self.desc = desc
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if locale is not None:
            self.locale = locale
        if modify_time is not None:
            self.modify_time = modify_time
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if source is not None:
            self.source = source
        if templates is not None:
            self.templates = templates
        if type is not None:
            self.type = type

    @property
    def create_time(self):
        r"""Gets the create_time of this ListNotificationTemplateByNameResponse.

        消息通知模板创建时间。

        :return: The create_time of this ListNotificationTemplateByNameResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListNotificationTemplateByNameResponse.

        消息通知模板创建时间。

        :param create_time: The create_time of this ListNotificationTemplateByNameResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def desc(self):
        r"""Gets the desc of this ListNotificationTemplateByNameResponse.

        消息通知模板描述。

        :return: The desc of this ListNotificationTemplateByNameResponse.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ListNotificationTemplateByNameResponse.

        消息通知模板描述。

        :param desc: The desc of this ListNotificationTemplateByNameResponse.
        :type desc: str
        """
        self._desc = desc

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListNotificationTemplateByNameResponse.

        消息通知模板所属企业项目id。

        :return: The enterprise_project_id of this ListNotificationTemplateByNameResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListNotificationTemplateByNameResponse.

        消息通知模板所属企业项目id。

        :param enterprise_project_id: The enterprise_project_id of this ListNotificationTemplateByNameResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def locale(self):
        r"""Gets the locale of this ListNotificationTemplateByNameResponse.

        消息通知模板语言。

        :return: The locale of this ListNotificationTemplateByNameResponse.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        r"""Sets the locale of this ListNotificationTemplateByNameResponse.

        消息通知模板语言。

        :param locale: The locale of this ListNotificationTemplateByNameResponse.
        :type locale: str
        """
        self._locale = locale

    @property
    def modify_time(self):
        r"""Gets the modify_time of this ListNotificationTemplateByNameResponse.

        消息通知模板修改时间。

        :return: The modify_time of this ListNotificationTemplateByNameResponse.
        :rtype: int
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this ListNotificationTemplateByNameResponse.

        消息通知模板修改时间。

        :param modify_time: The modify_time of this ListNotificationTemplateByNameResponse.
        :type modify_time: int
        """
        self._modify_time = modify_time

    @property
    def name(self):
        r"""Gets the name of this ListNotificationTemplateByNameResponse.

        消息通知模板名称。

        :return: The name of this ListNotificationTemplateByNameResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListNotificationTemplateByNameResponse.

        消息通知模板名称。

        :param name: The name of this ListNotificationTemplateByNameResponse.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ListNotificationTemplateByNameResponse.

        消息通知模板所属项目id。

        :return: The project_id of this ListNotificationTemplateByNameResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListNotificationTemplateByNameResponse.

        消息通知模板所属项目id。

        :param project_id: The project_id of this ListNotificationTemplateByNameResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def source(self):
        r"""Gets the source of this ListNotificationTemplateByNameResponse.

        消息通知模板来源。

        :return: The source of this ListNotificationTemplateByNameResponse.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ListNotificationTemplateByNameResponse.

        消息通知模板来源。

        :param source: The source of this ListNotificationTemplateByNameResponse.
        :type source: str
        """
        self._source = source

    @property
    def templates(self):
        r"""Gets the templates of this ListNotificationTemplateByNameResponse.

        消息通知模板内容。 消息通知模板内容为json字符串，具体内容是由下列参数拼接成json数组后转义而来。  | 名称 |是否必选  |参数类型  |说明  | |--|--|--|--| |content  |是  |string  |消息模板内容。|  |subType  |是  |string  |消息模板发送类型，支持：email，sms，webhook。| | topic | 否 | string |邮件主题。| | sendType |否  |string  |当消息模板发送类型为“webhook”时需要指定消息模板格式，支持：HTML、JSON。  | | version |是  |string  |默认为v2。 |

        :return: The templates of this ListNotificationTemplateByNameResponse.
        :rtype: str
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListNotificationTemplateByNameResponse.

        消息通知模板内容。 消息通知模板内容为json字符串，具体内容是由下列参数拼接成json数组后转义而来。  | 名称 |是否必选  |参数类型  |说明  | |--|--|--|--| |content  |是  |string  |消息模板内容。|  |subType  |是  |string  |消息模板发送类型，支持：email，sms，webhook。| | topic | 否 | string |邮件主题。| | sendType |否  |string  |当消息模板发送类型为“webhook”时需要指定消息模板格式，支持：HTML、JSON。  | | version |是  |string  |默认为v2。 |

        :param templates: The templates of this ListNotificationTemplateByNameResponse.
        :type templates: str
        """
        self._templates = templates

    @property
    def type(self):
        r"""Gets the type of this ListNotificationTemplateByNameResponse.

        消息通知方式。

        :return: The type of this ListNotificationTemplateByNameResponse.
        :rtype: list[str]
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListNotificationTemplateByNameResponse.

        消息通知方式。

        :param type: The type of this ListNotificationTemplateByNameResponse.
        :type type: list[str]
        """
        self._type = type

    def to_dict(self):
        import warnings
        warnings.warn("ListNotificationTemplateByNameResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListNotificationTemplateByNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
