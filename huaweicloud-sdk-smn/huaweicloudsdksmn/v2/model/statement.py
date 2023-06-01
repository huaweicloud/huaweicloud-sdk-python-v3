# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Statement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sid': 'str',
        'effect': 'str',
        'principal': 'str',
        'not_principal': 'str',
        'action': 'str',
        'not_action': 'str',
        'resource': 'str',
        'not_resource': 'str'
    }

    attribute_map = {
        'sid': 'Sid',
        'effect': 'Effect',
        'principal': 'Principal',
        'not_principal': 'NotPrincipal',
        'action': 'Action',
        'not_action': 'NotAction',
        'resource': 'Resource',
        'not_resource': 'NotResource'
    }

    def __init__(self, sid=None, effect=None, principal=None, not_principal=None, action=None, not_action=None, resource=None, not_resource=None):
        """Statement

        The model defined in huaweicloud sdk

        :param sid: Statement语句的ID。 Statement语句ID必须是唯一的，例如statement01、statement02。
        :type sid: str
        :param effect: Statement语句的效果。“Allow”或者“Deny”。
        :type effect: str
        :param principal: Statement语句作用的对象。 目前支持“CSP”和“Service”两类对象。  “CSP”对象指的是其他用户，可以作用于多个用户。  “Service”对象指的是云服务，可以作用于多个云服务。  Principal元素和NotPrincipal元素两者任选其一。选定后， “CSP”对象填写内容的格式为urn:csp:iam::domainId:root或“\\*”，其中domainId为其他用户的“账号ID”，“\\*”指作用于所有人。  “Service”对象填写内容的格式为小写的云服务名称缩写。
        :type principal: str
        :param not_principal: NotPrincipal：Statement语句排除作用的对象。  目前支持“CSP”和“Service”两类对象。  “CSP”对象指的是其他用户，可以作用于多个用户。  “Service”对象指的是云服务，可以作用于多个云服务。  Principal元素和NotPrincipal元素两者任选其一。选定后， “CSP”对象填写内容的格式为urn:csp:iam::domainId:root或“\\*”，其中domainId为其他用户的“账号ID”，“\\*”指作用于所有人。  “Service”对象填写内容的格式为小写的云服务名称缩写。
        :type not_principal: str
        :param action: Statement语句作用的操作。  允许使用通配符来表示一类操作，例如：SMN:Update*、SMN:Delete*。如果只填写“*”，表示Statement语句作用的操作为该资源支持的所有操作。  Action元素和NotAction元素两者任选其一。  目前支持的操作有：  SMN:UpdateTopic SMN:DeleteTopic SMN:QueryTopicDetail SMN:ListTopicAttributes SMN:UpdateTopicAttribute SMN:DeleteTopicAttributes SMN:DeleteTopicAttributeByName SMN:ListSubscriptionsByTopic SMN:Subscribe SMN:Unsubscribe SMN:Publish
        :type action: str
        :param not_action: Statement语句排除作用的操作。  允许使用通配符来表示一类操作，例如：SMN:Update*、SMN:Delete*。如果只填写“*”，表示Statement语句作用的操作为该资源支持的所有操作。  Action元素和NotAction元素两者任选其一。  目前支持的操作有：  SMN:UpdateTopic  SMN:DeleteTopic  SMN:QueryTopicDetail  SMN:ListTopicAttributes  SMN:UpdateTopicAttribute  SMN:DeleteTopicAttributes  SMN:DeleteTopicAttributeByName  SMN:ListSubscriptionsByTopic  SMN:Subscribe  SMN:Unsubscribe  SMN:Publish
        :type not_action: str
        :param resource: Statement语句作用的主题。  Resource和NotResource两者任选其一。选定后，填写内容为主题URN。
        :type resource: str
        :param not_resource: Statement语句排除作用的主题。  Resource和NotResource两者任选其一。选定后，填写内容为主题URN。
        :type not_resource: str
        """
        
        

        self._sid = None
        self._effect = None
        self._principal = None
        self._not_principal = None
        self._action = None
        self._not_action = None
        self._resource = None
        self._not_resource = None
        self.discriminator = None

        self.sid = sid
        self.effect = effect
        if principal is not None:
            self.principal = principal
        if not_principal is not None:
            self.not_principal = not_principal
        if action is not None:
            self.action = action
        if not_action is not None:
            self.not_action = not_action
        if resource is not None:
            self.resource = resource
        if not_resource is not None:
            self.not_resource = not_resource

    @property
    def sid(self):
        """Gets the sid of this Statement.

        Statement语句的ID。 Statement语句ID必须是唯一的，例如statement01、statement02。

        :return: The sid of this Statement.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this Statement.

        Statement语句的ID。 Statement语句ID必须是唯一的，例如statement01、statement02。

        :param sid: The sid of this Statement.
        :type sid: str
        """
        self._sid = sid

    @property
    def effect(self):
        """Gets the effect of this Statement.

        Statement语句的效果。“Allow”或者“Deny”。

        :return: The effect of this Statement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this Statement.

        Statement语句的效果。“Allow”或者“Deny”。

        :param effect: The effect of this Statement.
        :type effect: str
        """
        self._effect = effect

    @property
    def principal(self):
        """Gets the principal of this Statement.

        Statement语句作用的对象。 目前支持“CSP”和“Service”两类对象。  “CSP”对象指的是其他用户，可以作用于多个用户。  “Service”对象指的是云服务，可以作用于多个云服务。  Principal元素和NotPrincipal元素两者任选其一。选定后， “CSP”对象填写内容的格式为urn:csp:iam::domainId:root或“\\*”，其中domainId为其他用户的“账号ID”，“\\*”指作用于所有人。  “Service”对象填写内容的格式为小写的云服务名称缩写。

        :return: The principal of this Statement.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this Statement.

        Statement语句作用的对象。 目前支持“CSP”和“Service”两类对象。  “CSP”对象指的是其他用户，可以作用于多个用户。  “Service”对象指的是云服务，可以作用于多个云服务。  Principal元素和NotPrincipal元素两者任选其一。选定后， “CSP”对象填写内容的格式为urn:csp:iam::domainId:root或“\\*”，其中domainId为其他用户的“账号ID”，“\\*”指作用于所有人。  “Service”对象填写内容的格式为小写的云服务名称缩写。

        :param principal: The principal of this Statement.
        :type principal: str
        """
        self._principal = principal

    @property
    def not_principal(self):
        """Gets the not_principal of this Statement.

        NotPrincipal：Statement语句排除作用的对象。  目前支持“CSP”和“Service”两类对象。  “CSP”对象指的是其他用户，可以作用于多个用户。  “Service”对象指的是云服务，可以作用于多个云服务。  Principal元素和NotPrincipal元素两者任选其一。选定后， “CSP”对象填写内容的格式为urn:csp:iam::domainId:root或“\\*”，其中domainId为其他用户的“账号ID”，“\\*”指作用于所有人。  “Service”对象填写内容的格式为小写的云服务名称缩写。

        :return: The not_principal of this Statement.
        :rtype: str
        """
        return self._not_principal

    @not_principal.setter
    def not_principal(self, not_principal):
        """Sets the not_principal of this Statement.

        NotPrincipal：Statement语句排除作用的对象。  目前支持“CSP”和“Service”两类对象。  “CSP”对象指的是其他用户，可以作用于多个用户。  “Service”对象指的是云服务，可以作用于多个云服务。  Principal元素和NotPrincipal元素两者任选其一。选定后， “CSP”对象填写内容的格式为urn:csp:iam::domainId:root或“\\*”，其中domainId为其他用户的“账号ID”，“\\*”指作用于所有人。  “Service”对象填写内容的格式为小写的云服务名称缩写。

        :param not_principal: The not_principal of this Statement.
        :type not_principal: str
        """
        self._not_principal = not_principal

    @property
    def action(self):
        """Gets the action of this Statement.

        Statement语句作用的操作。  允许使用通配符来表示一类操作，例如：SMN:Update*、SMN:Delete*。如果只填写“*”，表示Statement语句作用的操作为该资源支持的所有操作。  Action元素和NotAction元素两者任选其一。  目前支持的操作有：  SMN:UpdateTopic SMN:DeleteTopic SMN:QueryTopicDetail SMN:ListTopicAttributes SMN:UpdateTopicAttribute SMN:DeleteTopicAttributes SMN:DeleteTopicAttributeByName SMN:ListSubscriptionsByTopic SMN:Subscribe SMN:Unsubscribe SMN:Publish

        :return: The action of this Statement.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this Statement.

        Statement语句作用的操作。  允许使用通配符来表示一类操作，例如：SMN:Update*、SMN:Delete*。如果只填写“*”，表示Statement语句作用的操作为该资源支持的所有操作。  Action元素和NotAction元素两者任选其一。  目前支持的操作有：  SMN:UpdateTopic SMN:DeleteTopic SMN:QueryTopicDetail SMN:ListTopicAttributes SMN:UpdateTopicAttribute SMN:DeleteTopicAttributes SMN:DeleteTopicAttributeByName SMN:ListSubscriptionsByTopic SMN:Subscribe SMN:Unsubscribe SMN:Publish

        :param action: The action of this Statement.
        :type action: str
        """
        self._action = action

    @property
    def not_action(self):
        """Gets the not_action of this Statement.

        Statement语句排除作用的操作。  允许使用通配符来表示一类操作，例如：SMN:Update*、SMN:Delete*。如果只填写“*”，表示Statement语句作用的操作为该资源支持的所有操作。  Action元素和NotAction元素两者任选其一。  目前支持的操作有：  SMN:UpdateTopic  SMN:DeleteTopic  SMN:QueryTopicDetail  SMN:ListTopicAttributes  SMN:UpdateTopicAttribute  SMN:DeleteTopicAttributes  SMN:DeleteTopicAttributeByName  SMN:ListSubscriptionsByTopic  SMN:Subscribe  SMN:Unsubscribe  SMN:Publish

        :return: The not_action of this Statement.
        :rtype: str
        """
        return self._not_action

    @not_action.setter
    def not_action(self, not_action):
        """Sets the not_action of this Statement.

        Statement语句排除作用的操作。  允许使用通配符来表示一类操作，例如：SMN:Update*、SMN:Delete*。如果只填写“*”，表示Statement语句作用的操作为该资源支持的所有操作。  Action元素和NotAction元素两者任选其一。  目前支持的操作有：  SMN:UpdateTopic  SMN:DeleteTopic  SMN:QueryTopicDetail  SMN:ListTopicAttributes  SMN:UpdateTopicAttribute  SMN:DeleteTopicAttributes  SMN:DeleteTopicAttributeByName  SMN:ListSubscriptionsByTopic  SMN:Subscribe  SMN:Unsubscribe  SMN:Publish

        :param not_action: The not_action of this Statement.
        :type not_action: str
        """
        self._not_action = not_action

    @property
    def resource(self):
        """Gets the resource of this Statement.

        Statement语句作用的主题。  Resource和NotResource两者任选其一。选定后，填写内容为主题URN。

        :return: The resource of this Statement.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this Statement.

        Statement语句作用的主题。  Resource和NotResource两者任选其一。选定后，填写内容为主题URN。

        :param resource: The resource of this Statement.
        :type resource: str
        """
        self._resource = resource

    @property
    def not_resource(self):
        """Gets the not_resource of this Statement.

        Statement语句排除作用的主题。  Resource和NotResource两者任选其一。选定后，填写内容为主题URN。

        :return: The not_resource of this Statement.
        :rtype: str
        """
        return self._not_resource

    @not_resource.setter
    def not_resource(self, not_resource):
        """Sets the not_resource of this Statement.

        Statement语句排除作用的主题。  Resource和NotResource两者任选其一。选定后，填写内容为主题URN。

        :param not_resource: The not_resource of this Statement.
        :type not_resource: str
        """
        self._not_resource = not_resource

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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
