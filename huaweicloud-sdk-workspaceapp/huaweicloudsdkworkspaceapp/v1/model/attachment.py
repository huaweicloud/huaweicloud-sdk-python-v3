# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Attachment:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attach': 'str',
        'attach_type': 'str'
    }

    attribute_map = {
        'attach': 'attach',
        'attach_type': 'attach_type'
    }

    def __init__(self, attach=None, attach_type=None):
        r"""Attachment

        The model defined in huaweicloud sdk

        :param attach: 目标。
        :type attach: str
        :param attach_type: 关联对象类型： * &#x60;USER&#x60; -  用户 * &#x60;USER_GROUP&#x60; - 用户组
        :type attach_type: str
        """
        
        

        self._attach = None
        self._attach_type = None
        self.discriminator = None

        self.attach = attach
        self.attach_type = attach_type

    @property
    def attach(self):
        r"""Gets the attach of this Attachment.

        目标。

        :return: The attach of this Attachment.
        :rtype: str
        """
        return self._attach

    @attach.setter
    def attach(self, attach):
        r"""Sets the attach of this Attachment.

        目标。

        :param attach: The attach of this Attachment.
        :type attach: str
        """
        self._attach = attach

    @property
    def attach_type(self):
        r"""Gets the attach_type of this Attachment.

        关联对象类型： * `USER` -  用户 * `USER_GROUP` - 用户组

        :return: The attach_type of this Attachment.
        :rtype: str
        """
        return self._attach_type

    @attach_type.setter
    def attach_type(self, attach_type):
        r"""Sets the attach_type of this Attachment.

        关联对象类型： * `USER` -  用户 * `USER_GROUP` - 用户组

        :param attach_type: The attach_type of this Attachment.
        :type attach_type: str
        """
        self._attach_type = attach_type

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
        if not isinstance(other, Attachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
