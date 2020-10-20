# coding: utf-8

import pprint
import re

import six





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
        """AddRuleReq - a model defined in huaweicloud sdk"""
        
        

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

        用户自定义的规则名称。

        :return: The rule_name of this AddRuleReq.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this AddRuleReq.

        用户自定义的规则名称。

        :param rule_name: The rule_name of this AddRuleReq.
        :type: str
        """
        self._rule_name = rule_name

    @property
    def description(self):
        """Gets the description of this AddRuleReq.

        用户自定义的规则描述。

        :return: The description of this AddRuleReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddRuleReq.

        用户自定义的规则描述。

        :param description: The description of this AddRuleReq.
        :type: str
        """
        self._description = description

    @property
    def subject(self):
        """Gets the subject of this AddRuleReq.


        :return: The subject of this AddRuleReq.
        :rtype: RoutingRuleSubject
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this AddRuleReq.


        :param subject: The subject of this AddRuleReq.
        :type: RoutingRuleSubject
        """
        self._subject = subject

    @property
    def app_type(self):
        """Gets the app_type of this AddRuleReq.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为资源空间级。如果类型为APP，创建的规则生效范围为携带的app_id指定的资源空间，不携带app_id则创建规则生效范围为[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)。 

        :return: The app_type of this AddRuleReq.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        """Sets the app_type of this AddRuleReq.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为资源空间级。如果类型为APP，创建的规则生效范围为携带的app_id指定的资源空间，不携带app_id则创建规则生效范围为[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)。 

        :param app_type: The app_type of this AddRuleReq.
        :type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        """Gets the app_id of this AddRuleReq.

        资源空间ID。

        :return: The app_id of this AddRuleReq.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this AddRuleReq.

        资源空间ID。

        :param app_id: The app_id of this AddRuleReq.
        :type: str
        """
        self._app_id = app_id

    @property
    def select(self):
        """Gets the select of this AddRuleReq.

        用户自定义sql select语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :return: The select of this AddRuleReq.
        :rtype: str
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this AddRuleReq.

        用户自定义sql select语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :param select: The select of this AddRuleReq.
        :type: str
        """
        self._select = select

    @property
    def where(self):
        """Gets the where of this AddRuleReq.

        用户自定义sql where语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :return: The where of this AddRuleReq.
        :rtype: str
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this AddRuleReq.

        用户自定义sql where语句，最大长度500，该参数仅供标准版和企业版用户使用。

        :param where: The where of this AddRuleReq.
        :type: str
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddRuleReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
