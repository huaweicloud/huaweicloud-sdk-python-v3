# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateResDatastructRequestBodyBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'item_attrs': 'list[ItemAttrs]',
        'user_attrs': 'list[UserAttrs]',
        'behaviors': 'BehaviorsConfig'
    }

    attribute_map = {
        'item_attrs': 'item_attrs',
        'user_attrs': 'user_attrs',
        'behaviors': 'behaviors'
    }

    def __init__(self, item_attrs=None, user_attrs=None, behaviors=None):
        r"""UpdateResDatastructRequestBodyBody

        The model defined in huaweicloud sdk

        :param item_attrs: 物品特征信息。
        :type item_attrs: list[:class:`huaweicloudsdkres.v1.ItemAttrs`]
        :param user_attrs: 用户特征信息。
        :type user_attrs: list[:class:`huaweicloudsdkres.v1.UserAttrs`]
        :param behaviors: 
        :type behaviors: :class:`huaweicloudsdkres.v1.BehaviorsConfig`
        """
        
        

        self._item_attrs = None
        self._user_attrs = None
        self._behaviors = None
        self.discriminator = None

        self.item_attrs = item_attrs
        self.user_attrs = user_attrs
        self.behaviors = behaviors

    @property
    def item_attrs(self):
        r"""Gets the item_attrs of this UpdateResDatastructRequestBodyBody.

        物品特征信息。

        :return: The item_attrs of this UpdateResDatastructRequestBodyBody.
        :rtype: list[:class:`huaweicloudsdkres.v1.ItemAttrs`]
        """
        return self._item_attrs

    @item_attrs.setter
    def item_attrs(self, item_attrs):
        r"""Sets the item_attrs of this UpdateResDatastructRequestBodyBody.

        物品特征信息。

        :param item_attrs: The item_attrs of this UpdateResDatastructRequestBodyBody.
        :type item_attrs: list[:class:`huaweicloudsdkres.v1.ItemAttrs`]
        """
        self._item_attrs = item_attrs

    @property
    def user_attrs(self):
        r"""Gets the user_attrs of this UpdateResDatastructRequestBodyBody.

        用户特征信息。

        :return: The user_attrs of this UpdateResDatastructRequestBodyBody.
        :rtype: list[:class:`huaweicloudsdkres.v1.UserAttrs`]
        """
        return self._user_attrs

    @user_attrs.setter
    def user_attrs(self, user_attrs):
        r"""Sets the user_attrs of this UpdateResDatastructRequestBodyBody.

        用户特征信息。

        :param user_attrs: The user_attrs of this UpdateResDatastructRequestBodyBody.
        :type user_attrs: list[:class:`huaweicloudsdkres.v1.UserAttrs`]
        """
        self._user_attrs = user_attrs

    @property
    def behaviors(self):
        r"""Gets the behaviors of this UpdateResDatastructRequestBodyBody.

        :return: The behaviors of this UpdateResDatastructRequestBodyBody.
        :rtype: :class:`huaweicloudsdkres.v1.BehaviorsConfig`
        """
        return self._behaviors

    @behaviors.setter
    def behaviors(self, behaviors):
        r"""Sets the behaviors of this UpdateResDatastructRequestBodyBody.

        :param behaviors: The behaviors of this UpdateResDatastructRequestBodyBody.
        :type behaviors: :class:`huaweicloudsdkres.v1.BehaviorsConfig`
        """
        self._behaviors = behaviors

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
        if not isinstance(other, UpdateResDatastructRequestBodyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
