# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangePasswordReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'original_password': 'str',
        'new_password': 'str',
        'ticket': 'str'
    }

    attribute_map = {
        'original_password': 'original_password',
        'new_password': 'new_password',
        'ticket': 'ticket'
    }

    def __init__(self, original_password=None, new_password=None, ticket=None):
        r"""ChangePasswordReq

        The model defined in huaweicloud sdk

        :param original_password: 原始密码
        :type original_password: str
        :param new_password: 新密码
        :type new_password: str
        :param ticket: 预验证凭证
        :type ticket: str
        """
        
        

        self._original_password = None
        self._new_password = None
        self._ticket = None
        self.discriminator = None

        self.original_password = original_password
        self.new_password = new_password
        if ticket is not None:
            self.ticket = ticket

    @property
    def original_password(self):
        r"""Gets the original_password of this ChangePasswordReq.

        原始密码

        :return: The original_password of this ChangePasswordReq.
        :rtype: str
        """
        return self._original_password

    @original_password.setter
    def original_password(self, original_password):
        r"""Sets the original_password of this ChangePasswordReq.

        原始密码

        :param original_password: The original_password of this ChangePasswordReq.
        :type original_password: str
        """
        self._original_password = original_password

    @property
    def new_password(self):
        r"""Gets the new_password of this ChangePasswordReq.

        新密码

        :return: The new_password of this ChangePasswordReq.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        r"""Sets the new_password of this ChangePasswordReq.

        新密码

        :param new_password: The new_password of this ChangePasswordReq.
        :type new_password: str
        """
        self._new_password = new_password

    @property
    def ticket(self):
        r"""Gets the ticket of this ChangePasswordReq.

        预验证凭证

        :return: The ticket of this ChangePasswordReq.
        :rtype: str
        """
        return self._ticket

    @ticket.setter
    def ticket(self, ticket):
        r"""Sets the ticket of this ChangePasswordReq.

        预验证凭证

        :param ticket: The ticket of this ChangePasswordReq.
        :type ticket: str
        """
        self._ticket = ticket

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
        if not isinstance(other, ChangePasswordReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
