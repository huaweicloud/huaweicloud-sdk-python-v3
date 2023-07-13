# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddRuleReq:

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
        'description': 'str',
        'subject': 'RoutingRuleSubject',
        'app_type': 'str',
        'app_id': 'str',
        'select': 'str',
        'where': 'str'
    }

    attribute_map = {
        'rule_name': 'rule_name',
        'description': 'description',
        'subject': 'subject',
        'app_type': 'app_type',
        'app_id': 'app_id',
        'select': 'select',
        'where': 'where'
    }

    def __init__(self, rule_name=None, description=None, subject=None, app_type=None, app_id=None, select=None, where=None):
        """AddRuleReq

        The model defined in huaweicloud sdk

        :param rule_name: **参数说明**：规则名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合
        :type rule_name: str
        :param description: **参数说明**：用户自定义的规则描述。
        :type description: str
        :param subject: 
        :type subject: :class:`huaweicloudsdkiotda.v5.RoutingRuleSubject`
        :param app_type: **参数说明**：租户规则的生效范围，默认GLOBAL，。 **取值范围**： - GLOBAL：生效范围为租户级。 - APP：生效范围为资源空间级。如果类型为APP，创建的规则生效范围为携带的app_id指定的资源空间，不携带app_id则创建规则生效范围为[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)。
        :type app_type: str
        :param app_id: **参数说明**：资源空间ID。。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param select: **参数说明**：用户自定义sql select语句，最大长度2500，该参数仅供标准版和企业版用户使用。可填参数可参考帮助文档数据下各接口的请求参数，如notify_data.body。
        :type select: str
        :param where: **参数说明**：用户自定义sql where语句，最大长度2500，该参数仅供标准版和企业版用户使用可填参数可参考帮助文档数据下各接口的请求参数，如notify_data.body。
        :type where: str
        """
        
        

        self._rule_name = None
        self._description = None
        self._subject = None
        self._app_type = None
        self._app_id = None
        self._select = None
        self._where = None
        self.discriminator = None

        if rule_name is not None:
            self.rule_name = rule_name
        if description is not None:
            self.description = description
        self.subject = subject
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id
        if select is not None:
            self.select = select
        if where is not None:
            self.where = where

    @property
    def rule_name(self):
        """Gets the rule_name of this AddRuleReq.

        **参数说明**：规则名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :return: The rule_name of this AddRuleReq.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this AddRuleReq.

        **参数说明**：规则名称。 **取值范围**：长度不超过256，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合

        :param rule_name: The rule_name of this AddRuleReq.
        :type rule_name: str
        """
        self._rule_name = rule_name

    @property
    def description(self):
        """Gets the description of this AddRuleReq.

        **参数说明**：用户自定义的规则描述。

        :return: The description of this AddRuleReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddRuleReq.

        **参数说明**：用户自定义的规则描述。

        :param description: The description of this AddRuleReq.
        :type description: str
        """
        self._description = description

    @property
    def subject(self):
        """Gets the subject of this AddRuleReq.

        :return: The subject of this AddRuleReq.
        :rtype: :class:`huaweicloudsdkiotda.v5.RoutingRuleSubject`
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this AddRuleReq.

        :param subject: The subject of this AddRuleReq.
        :type subject: :class:`huaweicloudsdkiotda.v5.RoutingRuleSubject`
        """
        self._subject = subject

    @property
    def app_type(self):
        """Gets the app_type of this AddRuleReq.

        **参数说明**：租户规则的生效范围，默认GLOBAL，。 **取值范围**： - GLOBAL：生效范围为租户级。 - APP：生效范围为资源空间级。如果类型为APP，创建的规则生效范围为携带的app_id指定的资源空间，不携带app_id则创建规则生效范围为[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)。

        :return: The app_type of this AddRuleReq.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AddRuleReq.

        **参数说明**：租户规则的生效范围，默认GLOBAL，。 **取值范围**： - GLOBAL：生效范围为租户级。 - APP：生效范围为资源空间级。如果类型为APP，创建的规则生效范围为携带的app_id指定的资源空间，不携带app_id则创建规则生效范围为[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)。

        :param app_type: The app_type of this AddRuleReq.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this AddRuleReq.

        **参数说明**：资源空间ID。。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this AddRuleReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddRuleReq.

        **参数说明**：资源空间ID。。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this AddRuleReq.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def select(self):
        """Gets the select of this AddRuleReq.

        **参数说明**：用户自定义sql select语句，最大长度2500，该参数仅供标准版和企业版用户使用。可填参数可参考帮助文档数据下各接口的请求参数，如notify_data.body。

        :return: The select of this AddRuleReq.
        :rtype: str
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this AddRuleReq.

        **参数说明**：用户自定义sql select语句，最大长度2500，该参数仅供标准版和企业版用户使用。可填参数可参考帮助文档数据下各接口的请求参数，如notify_data.body。

        :param select: The select of this AddRuleReq.
        :type select: str
        """
        self._select = select

    @property
    def where(self):
        """Gets the where of this AddRuleReq.

        **参数说明**：用户自定义sql where语句，最大长度2500，该参数仅供标准版和企业版用户使用可填参数可参考帮助文档数据下各接口的请求参数，如notify_data.body。

        :return: The where of this AddRuleReq.
        :rtype: str
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this AddRuleReq.

        **参数说明**：用户自定义sql where语句，最大长度2500，该参数仅供标准版和企业版用户使用可填参数可参考帮助文档数据下各接口的请求参数，如notify_data.body。

        :param where: The where of this AddRuleReq.
        :type where: str
        """
        self._where = where

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
        if not isinstance(other, AddRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
