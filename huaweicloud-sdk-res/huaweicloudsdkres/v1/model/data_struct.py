# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataStruct:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'behaviors': 'BehaviorsConfig',
        'item_attrs': 'list[ItemAttrs]',
        'user_attrs': 'list[UserAttrs]',
        'user_dynamic_attr': 'UserDynamicAttr'
    }

    attribute_map = {
        'behaviors': 'behaviors',
        'item_attrs': 'item_attrs',
        'user_attrs': 'user_attrs',
        'user_dynamic_attr': 'user_dynamic_attr'
    }

    def __init__(self, behaviors=None, item_attrs=None, user_attrs=None, user_dynamic_attr=None):
        """DataStruct - a model defined in huaweicloud sdk"""
        
        

        self._behaviors = None
        self._item_attrs = None
        self._user_attrs = None
        self._user_dynamic_attr = None
        self.discriminator = None

        if behaviors is not None:
            self.behaviors = behaviors
        if item_attrs is not None:
            self.item_attrs = item_attrs
        if user_attrs is not None:
            self.user_attrs = user_attrs
        if user_dynamic_attr is not None:
            self.user_dynamic_attr = user_dynamic_attr

    @property
    def behaviors(self):
        """Gets the behaviors of this DataStruct.


        :return: The behaviors of this DataStruct.
        :rtype: BehaviorsConfig
        """
        return self._behaviors

    @behaviors.setter
    def behaviors(self, behaviors):
        """Sets the behaviors of this DataStruct.


        :param behaviors: The behaviors of this DataStruct.
        :type: BehaviorsConfig
        """
        self._behaviors = behaviors

    @property
    def item_attrs(self):
        """Gets the item_attrs of this DataStruct.

        物品参数。

        :return: The item_attrs of this DataStruct.
        :rtype: list[ItemAttrs]
        """
        return self._item_attrs

    @item_attrs.setter
    def item_attrs(self, item_attrs):
        """Sets the item_attrs of this DataStruct.

        物品参数。

        :param item_attrs: The item_attrs of this DataStruct.
        :type: list[ItemAttrs]
        """
        self._item_attrs = item_attrs

    @property
    def user_attrs(self):
        """Gets the user_attrs of this DataStruct.

        用户参数。

        :return: The user_attrs of this DataStruct.
        :rtype: list[UserAttrs]
        """
        return self._user_attrs

    @user_attrs.setter
    def user_attrs(self, user_attrs):
        """Sets the user_attrs of this DataStruct.

        用户参数。

        :param user_attrs: The user_attrs of this DataStruct.
        :type: list[UserAttrs]
        """
        self._user_attrs = user_attrs

    @property
    def user_dynamic_attr(self):
        """Gets the user_dynamic_attr of this DataStruct.


        :return: The user_dynamic_attr of this DataStruct.
        :rtype: UserDynamicAttr
        """
        return self._user_dynamic_attr

    @user_dynamic_attr.setter
    def user_dynamic_attr(self, user_dynamic_attr):
        """Sets the user_dynamic_attr of this DataStruct.


        :param user_dynamic_attr: The user_dynamic_attr of this DataStruct.
        :type: UserDynamicAttr
        """
        self._user_dynamic_attr = user_dynamic_attr

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
        if not isinstance(other, DataStruct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
