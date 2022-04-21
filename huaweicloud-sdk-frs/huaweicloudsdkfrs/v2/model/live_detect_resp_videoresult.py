# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveDetectRespVideoresult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alive': 'bool',
        'actions': 'list[ActionsList]',
        'picture': 'str'
    }

    attribute_map = {
        'alive': 'alive',
        'actions': 'actions',
        'picture': 'picture'
    }

    def __init__(self, alive=None, actions=None, picture=None):
        """LiveDetectRespVideoresult

        The model defined in huaweicloud sdk

        :param alive: 是否是活体。
        :type alive: bool
        :param actions: 动作列表。
        :type actions: list[:class:`huaweicloudsdkfrs.v2.ActionsList`]
        :param picture: 检测出最大人脸的图片base64。
        :type picture: str
        """
        
        

        self._alive = None
        self._actions = None
        self._picture = None
        self.discriminator = None

        if alive is not None:
            self.alive = alive
        if actions is not None:
            self.actions = actions
        if picture is not None:
            self.picture = picture

    @property
    def alive(self):
        """Gets the alive of this LiveDetectRespVideoresult.

        是否是活体。

        :return: The alive of this LiveDetectRespVideoresult.
        :rtype: bool
        """
        return self._alive

    @alive.setter
    def alive(self, alive):
        """Sets the alive of this LiveDetectRespVideoresult.

        是否是活体。

        :param alive: The alive of this LiveDetectRespVideoresult.
        :type alive: bool
        """
        self._alive = alive

    @property
    def actions(self):
        """Gets the actions of this LiveDetectRespVideoresult.

        动作列表。

        :return: The actions of this LiveDetectRespVideoresult.
        :rtype: list[:class:`huaweicloudsdkfrs.v2.ActionsList`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this LiveDetectRespVideoresult.

        动作列表。

        :param actions: The actions of this LiveDetectRespVideoresult.
        :type actions: list[:class:`huaweicloudsdkfrs.v2.ActionsList`]
        """
        self._actions = actions

    @property
    def picture(self):
        """Gets the picture of this LiveDetectRespVideoresult.

        检测出最大人脸的图片base64。

        :return: The picture of this LiveDetectRespVideoresult.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this LiveDetectRespVideoresult.

        检测出最大人脸的图片base64。

        :param picture: The picture of this LiveDetectRespVideoresult.
        :type picture: str
        """
        self._picture = picture

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
        if not isinstance(other, LiveDetectRespVideoresult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
