# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class CreateRoutingRuleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'rule_name': 'str',
        'description': 'str',
        'subject': 'RoutingRuleSubject',
        'app_type': 'str',
        'app_id': 'str',
        'select': 'str',
        'where': 'str',
        'active': 'bool'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'rule_name': 'rule_name',
        'description': 'description',
        'subject': 'subject',
        'app_type': 'app_type',
        'app_id': 'app_id',
        'select': 'select',
        'where': 'where',
        'active': 'active'
    }

    def __init__(self, rule_id=None, rule_name=None, description=None, subject=None, app_type=None, app_id=None, select=None, where=None, active=None):
        """CreateRoutingRuleResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._rule_id = None
        self._rule_name = None
        self._description = None
        self._subject = None
        self._app_type = None
        self._app_id = None
        self._select = None
        self._where = None
        self._active = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if rule_name is not None:
            self.rule_name = rule_name
        if description is not None:
            self.description = description
        if subject is not None:
            self.subject = subject
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id
        if select is not None:
            self.select = select
        if where is not None:
            self.where = where
        if active is not None:
            self.active = active

    @property
    def rule_id(self):
        """Gets the rule_id of this CreateRoutingRuleResponse.

        规则触发条件ID，用于唯一标识一个规则触发条件，在创建规则条件时由物联网平台分配获得。

        :return: The rule_id of this CreateRoutingRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this CreateRoutingRuleResponse.

        规则触发条件ID，用于唯一标识一个规则触发条件，在创建规则条件时由物联网平台分配获得。

        :param rule_id: The rule_id of this CreateRoutingRuleResponse.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def rule_name(self):
        """Gets the rule_name of this CreateRoutingRuleResponse.

        用户自定义的规则名称。

        :return: The rule_name of this CreateRoutingRuleResponse.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this CreateRoutingRuleResponse.

        用户自定义的规则名称。

        :param rule_name: The rule_name of this CreateRoutingRuleResponse.
        :type: str
        """
        self._rule_name = rule_name

    @property
    def description(self):
        """Gets the description of this CreateRoutingRuleResponse.

        用户自定义的规则描述。

        :return: The description of this CreateRoutingRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateRoutingRuleResponse.

        用户自定义的规则描述。

        :param description: The description of this CreateRoutingRuleResponse.
        :type: str
        """
        self._description = description

    @property
    def subject(self):
        """Gets the subject of this CreateRoutingRuleResponse.


        :return: The subject of this CreateRoutingRuleResponse.
        :rtype: RoutingRuleSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CreateRoutingRuleResponse.


        :param subject: The subject of this CreateRoutingRuleResponse.
        :type: RoutingRuleSubject
        """
        self._subject = subject

    @property
    def app_type(self):
        """Gets the app_type of this CreateRoutingRuleResponse.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为资源空间级。 

        :return: The app_type of this CreateRoutingRuleResponse.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this CreateRoutingRuleResponse.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为资源空间级。 

        :param app_type: The app_type of this CreateRoutingRuleResponse.
        :type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this CreateRoutingRuleResponse.

        资源空间ID

        :return: The app_id of this CreateRoutingRuleResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateRoutingRuleResponse.

        资源空间ID

        :param app_id: The app_id of this CreateRoutingRuleResponse.
        :type: str
        """
        self._app_id = app_id

    @property
    def select(self):
        """Gets the select of this CreateRoutingRuleResponse.

        用户自定义sql select语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :return: The select of this CreateRoutingRuleResponse.
        :rtype: str
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this CreateRoutingRuleResponse.

        用户自定义sql select语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :param select: The select of this CreateRoutingRuleResponse.
        :type: str
        """
        self._select = select

    @property
    def where(self):
        """Gets the where of this CreateRoutingRuleResponse.

        用户自定义sql where语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :return: The where of this CreateRoutingRuleResponse.
        :rtype: str
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this CreateRoutingRuleResponse.

        用户自定义sql where语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :param where: The where of this CreateRoutingRuleResponse.
        :type: str
        """
        self._where = where

    @property
    def active(self):
        """Gets the active of this CreateRoutingRuleResponse.

        规则条件的状态是否为激活。

        :return: The active of this CreateRoutingRuleResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this CreateRoutingRuleResponse.

        规则条件的状态是否为激活。

        :param active: The active of this CreateRoutingRuleResponse.
        :type: bool
        """
        self._active = active

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateRoutingRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
