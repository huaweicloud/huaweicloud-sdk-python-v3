# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RulesLocal:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'RulesLocalUser',
        'group': 'RulesLocalGroup'
    }

    attribute_map = {
        'user': 'user',
        'group': 'group'
    }

    def __init__(self, user=None, group=None):
        """RulesLocal

        The model defined in huaweicloud sdk

        :param user: 
        :type user: :class:`huaweicloudsdkiam.v3.RulesLocalUser`
        :param group: 
        :type group: :class:`huaweicloudsdkiam.v3.RulesLocalGroup`
        """
        
        

        self._user = None
        self._group = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if group is not None:
            self.group = group

    @property
    def user(self):
        """Gets the user of this RulesLocal.

        :return: The user of this RulesLocal.
        :rtype: :class:`huaweicloudsdkiam.v3.RulesLocalUser`
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RulesLocal.

        :param user: The user of this RulesLocal.
        :type user: :class:`huaweicloudsdkiam.v3.RulesLocalUser`
        """
        self._user = user

    @property
    def group(self):
        """Gets the group of this RulesLocal.

        :return: The group of this RulesLocal.
        :rtype: :class:`huaweicloudsdkiam.v3.RulesLocalGroup`
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this RulesLocal.

        :param group: The group of this RulesLocal.
        :type group: :class:`huaweicloudsdkiam.v3.RulesLocalGroup`
        """
        self._group = group

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
        if not isinstance(other, RulesLocal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
