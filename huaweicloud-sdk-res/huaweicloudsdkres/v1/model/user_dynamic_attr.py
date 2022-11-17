# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserDynamicAttr:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_interested_attrs': 'Attribute',
        'user_interested_action_type': 'Attribute'
    }

    attribute_map = {
        'user_interested_attrs': 'user_interested_attrs',
        'user_interested_action_type': 'user_interested_action_type'
    }

    def __init__(self, user_interested_attrs=None, user_interested_action_type=None):
        """UserDynamicAttr

        The model defined in huaweicloud sdk

        :param user_interested_attrs: 
        :type user_interested_attrs: :class:`huaweicloudsdkres.v1.Attribute`
        :param user_interested_action_type: 
        :type user_interested_action_type: :class:`huaweicloudsdkres.v1.Attribute`
        """
        
        

        self._user_interested_attrs = None
        self._user_interested_action_type = None
        self.discriminator = None

        if user_interested_attrs is not None:
            self.user_interested_attrs = user_interested_attrs
        if user_interested_action_type is not None:
            self.user_interested_action_type = user_interested_action_type

    @property
    def user_interested_attrs(self):
        """Gets the user_interested_attrs of this UserDynamicAttr.

        :return: The user_interested_attrs of this UserDynamicAttr.
        :rtype: :class:`huaweicloudsdkres.v1.Attribute`
        """
        return self._user_interested_attrs

    @user_interested_attrs.setter
    def user_interested_attrs(self, user_interested_attrs):
        """Sets the user_interested_attrs of this UserDynamicAttr.

        :param user_interested_attrs: The user_interested_attrs of this UserDynamicAttr.
        :type user_interested_attrs: :class:`huaweicloudsdkres.v1.Attribute`
        """
        self._user_interested_attrs = user_interested_attrs

    @property
    def user_interested_action_type(self):
        """Gets the user_interested_action_type of this UserDynamicAttr.

        :return: The user_interested_action_type of this UserDynamicAttr.
        :rtype: :class:`huaweicloudsdkres.v1.Attribute`
        """
        return self._user_interested_action_type

    @user_interested_action_type.setter
    def user_interested_action_type(self, user_interested_action_type):
        """Sets the user_interested_action_type of this UserDynamicAttr.

        :param user_interested_action_type: The user_interested_action_type of this UserDynamicAttr.
        :type user_interested_action_type: :class:`huaweicloudsdkres.v1.Attribute`
        """
        self._user_interested_action_type = user_interested_action_type

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
        if not isinstance(other, UserDynamicAttr):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
