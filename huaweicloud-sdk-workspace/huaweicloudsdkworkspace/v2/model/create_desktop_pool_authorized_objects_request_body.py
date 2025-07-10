# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDesktopPoolAuthorizedObjectsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'objects': 'list[AuthorizedObjects]',
        'action': 'str'
    }

    attribute_map = {
        'objects': 'objects',
        'action': 'action'
    }

    def __init__(self, objects=None, action=None):
        r"""CreateDesktopPoolAuthorizedObjectsRequestBody

        The model defined in huaweicloud sdk

        :param objects: 要授权的用户/用户组。
        :type objects: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        :param action: 执行动作，ADD：增加授权用户/用户组，REMOVE：移除已授权用户/用户组。
        :type action: str
        """
        
        

        self._objects = None
        self._action = None
        self.discriminator = None

        if objects is not None:
            self.objects = objects
        self.action = action

    @property
    def objects(self):
        r"""Gets the objects of this CreateDesktopPoolAuthorizedObjectsRequestBody.

        要授权的用户/用户组。

        :return: The objects of this CreateDesktopPoolAuthorizedObjectsRequestBody.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        r"""Sets the objects of this CreateDesktopPoolAuthorizedObjectsRequestBody.

        要授权的用户/用户组。

        :param objects: The objects of this CreateDesktopPoolAuthorizedObjectsRequestBody.
        :type objects: list[:class:`huaweicloudsdkworkspace.v2.AuthorizedObjects`]
        """
        self._objects = objects

    @property
    def action(self):
        r"""Gets the action of this CreateDesktopPoolAuthorizedObjectsRequestBody.

        执行动作，ADD：增加授权用户/用户组，REMOVE：移除已授权用户/用户组。

        :return: The action of this CreateDesktopPoolAuthorizedObjectsRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CreateDesktopPoolAuthorizedObjectsRequestBody.

        执行动作，ADD：增加授权用户/用户组，REMOVE：移除已授权用户/用户组。

        :param action: The action of this CreateDesktopPoolAuthorizedObjectsRequestBody.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, CreateDesktopPoolAuthorizedObjectsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
