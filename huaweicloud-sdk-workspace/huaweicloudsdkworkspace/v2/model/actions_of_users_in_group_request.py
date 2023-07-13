# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionsOfUsersInGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_ids': 'list[str]',
        'op_type': 'str'
    }

    attribute_map = {
        'user_ids': 'user_ids',
        'op_type': 'op_type'
    }

    def __init__(self, user_ids=None, op_type=None):
        """ActionsOfUsersInGroupRequest

        The model defined in huaweicloud sdk

        :param user_ids: 要添加或移除的用户Id列表。
        :type user_ids: list[str]
        :param op_type: 操作类型。 * ADD： 添加 * DELETE： 删除
        :type op_type: str
        """
        
        

        self._user_ids = None
        self._op_type = None
        self.discriminator = None

        self.user_ids = user_ids
        self.op_type = op_type

    @property
    def user_ids(self):
        """Gets the user_ids of this ActionsOfUsersInGroupRequest.

        要添加或移除的用户Id列表。

        :return: The user_ids of this ActionsOfUsersInGroupRequest.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this ActionsOfUsersInGroupRequest.

        要添加或移除的用户Id列表。

        :param user_ids: The user_ids of this ActionsOfUsersInGroupRequest.
        :type user_ids: list[str]
        """
        self._user_ids = user_ids

    @property
    def op_type(self):
        """Gets the op_type of this ActionsOfUsersInGroupRequest.

        操作类型。 * ADD： 添加 * DELETE： 删除

        :return: The op_type of this ActionsOfUsersInGroupRequest.
        :rtype: str
        """
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        """Sets the op_type of this ActionsOfUsersInGroupRequest.

        操作类型。 * ADD： 添加 * DELETE： 删除

        :param op_type: The op_type of this ActionsOfUsersInGroupRequest.
        :type op_type: str
        """
        self._op_type = op_type

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
        if not isinstance(other, ActionsOfUsersInGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
