# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrincipalRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'principal': 'str',
        'principal_name': 'str',
        'action_type': 'str',
        'effect': 'str'
    }

    attribute_map = {
        'principal': 'principal',
        'principal_name': 'principal_name',
        'action_type': 'action_type',
        'effect': 'effect'
    }

    def __init__(self, principal=None, principal_name=None, action_type=None, effect=None):
        """PrincipalRule

        The model defined in huaweicloud sdk

        :param principal: 授权用户ID。
        :type principal: str
        :param principal_name: 授权用户名。  如果授权给租户下的所有子用户，格式为：domainName.*；如果授权给租户下的指定子用户，则格式为：domainName.userName
        :type principal_name: str
        :param action_type: 授权操作类型。  - putRecords：上传数据。 - getRecords：下载数据。
        :type action_type: str
        :param effect: 授权影响类型。  - accept：允许该授权操作。
        :type effect: str
        """
        
        

        self._principal = None
        self._principal_name = None
        self._action_type = None
        self._effect = None
        self.discriminator = None

        if principal is not None:
            self.principal = principal
        if principal_name is not None:
            self.principal_name = principal_name
        if action_type is not None:
            self.action_type = action_type
        if effect is not None:
            self.effect = effect

    @property
    def principal(self):
        """Gets the principal of this PrincipalRule.

        授权用户ID。

        :return: The principal of this PrincipalRule.
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this PrincipalRule.

        授权用户ID。

        :param principal: The principal of this PrincipalRule.
        :type principal: str
        """
        self._principal = principal

    @property
    def principal_name(self):
        """Gets the principal_name of this PrincipalRule.

        授权用户名。  如果授权给租户下的所有子用户，格式为：domainName.*；如果授权给租户下的指定子用户，则格式为：domainName.userName

        :return: The principal_name of this PrincipalRule.
        :rtype: str
        """
        return self._principal_name

    @principal_name.setter
    def principal_name(self, principal_name):
        """Sets the principal_name of this PrincipalRule.

        授权用户名。  如果授权给租户下的所有子用户，格式为：domainName.*；如果授权给租户下的指定子用户，则格式为：domainName.userName

        :param principal_name: The principal_name of this PrincipalRule.
        :type principal_name: str
        """
        self._principal_name = principal_name

    @property
    def action_type(self):
        """Gets the action_type of this PrincipalRule.

        授权操作类型。  - putRecords：上传数据。 - getRecords：下载数据。

        :return: The action_type of this PrincipalRule.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this PrincipalRule.

        授权操作类型。  - putRecords：上传数据。 - getRecords：下载数据。

        :param action_type: The action_type of this PrincipalRule.
        :type action_type: str
        """
        self._action_type = action_type

    @property
    def effect(self):
        """Gets the effect of this PrincipalRule.

        授权影响类型。  - accept：允许该授权操作。

        :return: The effect of this PrincipalRule.
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this PrincipalRule.

        授权影响类型。  - accept：允许该授权操作。

        :param effect: The effect of this PrincipalRule.
        :type effect: str
        """
        self._effect = effect

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
        if not isinstance(other, PrincipalRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
