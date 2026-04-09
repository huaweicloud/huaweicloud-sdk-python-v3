# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Statement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "Statement"

    sensitive_list = []

    openapi_types = {
        'sid': 'str',
        'principal': 'StatementPrincipal',
        'not_principal': 'StatementNotPrincipal',
        'action': 'list[str]',
        'not_action': 'list[str]',
        'effect': 'str',
        'resource': 'list[str]',
        'not_resource': 'list[str]',
        'condition': 'object'
    }

    attribute_map = {
        'sid': 'Sid',
        'principal': 'Principal',
        'not_principal': 'NotPrincipal',
        'action': 'Action',
        'not_action': 'NotAction',
        'effect': 'Effect',
        'resource': 'Resource',
        'not_resource': 'NotResource',
        'condition': 'Condition'
    }

    def __init__(self, sid=None, principal=None, not_principal=None, action=None, not_action=None, effect=None, resource=None, not_resource=None, condition=None):
        r"""Statement

        The model defined in huaweicloud sdk

        :param sid: (Optional) ID of a statement. The value is a string that describes the statement.
        :type sid: str
        :param principal: 
        :type principal: :class:`huaweicloudsdkobs.v1.StatementPrincipal`
        :param not_principal: 
        :type not_principal: :class:`huaweicloudsdkobs.v1.StatementNotPrincipal`
        :param action: (Optional) Actions to which a statement applies. This parameter specifies a set of all the operations supported by OBS. It is a string of case-insensitive characters. A wildcard character (*) can be used, indicating all operations, for example, **\&quot;Action\&quot;:[\&quot;List*\&quot;,\&quot;Get*\&quot;]**.Select either **Action** or **NotAction**.
        :type action: list[str]
        :param not_action: (Optional) An exception to a list of actions in the statement. All actions are performed except the ones specified in **NotAction**. This parameter has the same value format as **Action*. Select either **Action** or **NotAction**.
        :type not_action: list[str]
        :param effect: Whether the permission in a statement is allowed or denied. The value is **Allow** or **Deny**.
        :type effect: str
        :param resource: Resources on which the statement takes effect. The wildcard (*) is supported, indicating all resources. Select either **Resource** or **NotResource**.
        :type resource: list[str]
        :param not_resource: An exception to a list of resources in a statement. A policy is not applied to the resources specified in **NotResource**. This parameter has the same value format as **Resource**. Optional. Select either **Resource** or **NotResource**.
        :type not_resource: list[str]
        :param condition: In addition to the effect, principal, resources, and actions, you can also specify the conditions under which a bucket policy takes effect. The bucket policy takes effect only when its condition expressions match values contained in the request. Conditions are optional. You can choose whether to configure them.  A condition consists of three parts: condition operator, key, and value. If there are multiple identical keys in the same condition operator, only the last key is retained. Condition operators and keys are mutually restricted: If you select a conditional operator of the string type, for example, **StringEquals**, the key can only be of the string type, for example, **UserAgent**. Likewise, if a key of the date type is selected, for example, **CurrentTime**, the conditional operator can only be of the date type, for example, **DateEquals**.  For general condition types and keys, see the condition description in [Bucket Policy Parameters](https://support.huaweicloud.com/intl/en-us/perms-cfg-obs/obs_40_0041.html).
        :type condition: object
        """
        
        

        self._sid = None
        self._principal = None
        self._not_principal = None
        self._action = None
        self._not_action = None
        self._effect = None
        self._resource = None
        self._not_resource = None
        self._condition = None
        self.discriminator = None

        if sid is not None:
            self.sid = sid
        if principal is not None:
            self.principal = principal
        if not_principal is not None:
            self.not_principal = not_principal
        if action is not None:
            self.action = action
        if not_action is not None:
            self.not_action = not_action
        if effect is not None:
            self.effect = effect
        if resource is not None:
            self.resource = resource
        if not_resource is not None:
            self.not_resource = not_resource
        if condition is not None:
            self.condition = condition

    @property
    def sid(self):
        r"""Gets the sid of this Statement.

        (Optional) ID of a statement. The value is a string that describes the statement.

        :return: The sid of this Statement.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        r"""Sets the sid of this Statement.

        (Optional) ID of a statement. The value is a string that describes the statement.

        :param sid: The sid of this Statement.
        :type sid: str
        """
        self._sid = sid

    @property
    def principal(self):
        r"""Gets the principal of this Statement.

        :return: The principal of this Statement.
        :rtype: :class:`huaweicloudsdkobs.v1.StatementPrincipal`
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this Statement.

        :param principal: The principal of this Statement.
        :type principal: :class:`huaweicloudsdkobs.v1.StatementPrincipal`
        """
        self._principal = principal

    @property
    def not_principal(self):
        r"""Gets the not_principal of this Statement.

        :return: The not_principal of this Statement.
        :rtype: :class:`huaweicloudsdkobs.v1.StatementNotPrincipal`
        """
        return self._not_principal

    @not_principal.setter
    def not_principal(self, not_principal):
        r"""Sets the not_principal of this Statement.

        :param not_principal: The not_principal of this Statement.
        :type not_principal: :class:`huaweicloudsdkobs.v1.StatementNotPrincipal`
        """
        self._not_principal = not_principal

    @property
    def action(self):
        r"""Gets the action of this Statement.

        (Optional) Actions to which a statement applies. This parameter specifies a set of all the operations supported by OBS. It is a string of case-insensitive characters. A wildcard character (*) can be used, indicating all operations, for example, **\"Action\":[\"List*\",\"Get*\"]**.Select either **Action** or **NotAction**.

        :return: The action of this Statement.
        :rtype: list[str]
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this Statement.

        (Optional) Actions to which a statement applies. This parameter specifies a set of all the operations supported by OBS. It is a string of case-insensitive characters. A wildcard character (*) can be used, indicating all operations, for example, **\"Action\":[\"List*\",\"Get*\"]**.Select either **Action** or **NotAction**.

        :param action: The action of this Statement.
        :type action: list[str]
        """
        self._action = action

    @property
    def not_action(self):
        r"""Gets the not_action of this Statement.

        (Optional) An exception to a list of actions in the statement. All actions are performed except the ones specified in **NotAction**. This parameter has the same value format as **Action*. Select either **Action** or **NotAction**.

        :return: The not_action of this Statement.
        :rtype: list[str]
        """
        return self._not_action

    @not_action.setter
    def not_action(self, not_action):
        r"""Sets the not_action of this Statement.

        (Optional) An exception to a list of actions in the statement. All actions are performed except the ones specified in **NotAction**. This parameter has the same value format as **Action*. Select either **Action** or **NotAction**.

        :param not_action: The not_action of this Statement.
        :type not_action: list[str]
        """
        self._not_action = not_action

    @property
    def effect(self):
        r"""Gets the effect of this Statement.

        Whether the permission in a statement is allowed or denied. The value is **Allow** or **Deny**.

        :return: The effect of this Statement.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        r"""Sets the effect of this Statement.

        Whether the permission in a statement is allowed or denied. The value is **Allow** or **Deny**.

        :param effect: The effect of this Statement.
        :type effect: str
        """
        self._effect = effect

    @property
    def resource(self):
        r"""Gets the resource of this Statement.

        Resources on which the statement takes effect. The wildcard (*) is supported, indicating all resources. Select either **Resource** or **NotResource**.

        :return: The resource of this Statement.
        :rtype: list[str]
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this Statement.

        Resources on which the statement takes effect. The wildcard (*) is supported, indicating all resources. Select either **Resource** or **NotResource**.

        :param resource: The resource of this Statement.
        :type resource: list[str]
        """
        self._resource = resource

    @property
    def not_resource(self):
        r"""Gets the not_resource of this Statement.

        An exception to a list of resources in a statement. A policy is not applied to the resources specified in **NotResource**. This parameter has the same value format as **Resource**. Optional. Select either **Resource** or **NotResource**.

        :return: The not_resource of this Statement.
        :rtype: list[str]
        """
        return self._not_resource

    @not_resource.setter
    def not_resource(self, not_resource):
        r"""Sets the not_resource of this Statement.

        An exception to a list of resources in a statement. A policy is not applied to the resources specified in **NotResource**. This parameter has the same value format as **Resource**. Optional. Select either **Resource** or **NotResource**.

        :param not_resource: The not_resource of this Statement.
        :type not_resource: list[str]
        """
        self._not_resource = not_resource

    @property
    def condition(self):
        r"""Gets the condition of this Statement.

        In addition to the effect, principal, resources, and actions, you can also specify the conditions under which a bucket policy takes effect. The bucket policy takes effect only when its condition expressions match values contained in the request. Conditions are optional. You can choose whether to configure them.  A condition consists of three parts: condition operator, key, and value. If there are multiple identical keys in the same condition operator, only the last key is retained. Condition operators and keys are mutually restricted: If you select a conditional operator of the string type, for example, **StringEquals**, the key can only be of the string type, for example, **UserAgent**. Likewise, if a key of the date type is selected, for example, **CurrentTime**, the conditional operator can only be of the date type, for example, **DateEquals**.  For general condition types and keys, see the condition description in [Bucket Policy Parameters](https://support.huaweicloud.com/intl/en-us/perms-cfg-obs/obs_40_0041.html).

        :return: The condition of this Statement.
        :rtype: object
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this Statement.

        In addition to the effect, principal, resources, and actions, you can also specify the conditions under which a bucket policy takes effect. The bucket policy takes effect only when its condition expressions match values contained in the request. Conditions are optional. You can choose whether to configure them.  A condition consists of three parts: condition operator, key, and value. If there are multiple identical keys in the same condition operator, only the last key is retained. Condition operators and keys are mutually restricted: If you select a conditional operator of the string type, for example, **StringEquals**, the key can only be of the string type, for example, **UserAgent**. Likewise, if a key of the date type is selected, for example, **CurrentTime**, the conditional operator can only be of the date type, for example, **DateEquals**.  For general condition types and keys, see the condition description in [Bucket Policy Parameters](https://support.huaweicloud.com/intl/en-us/perms-cfg-obs/obs_40_0041.html).

        :param condition: The condition of this Statement.
        :type condition: object
        """
        self._condition = condition

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
        if not isinstance(other, Statement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
