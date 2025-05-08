# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GroupMemberEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'member_id': 'str',
        'client_id': 'str'
    }

    attribute_map = {
        'member_id': 'member_id',
        'client_id': 'client_id'
    }

    def __init__(self, member_id=None, client_id=None):
        r"""GroupMemberEntity

        The model defined in huaweicloud sdk

        :param member_id: 成员Id
        :type member_id: str
        :param client_id: 客户端Id
        :type client_id: str
        """
        
        

        self._member_id = None
        self._client_id = None
        self.discriminator = None

        if member_id is not None:
            self.member_id = member_id
        if client_id is not None:
            self.client_id = client_id

    @property
    def member_id(self):
        r"""Gets the member_id of this GroupMemberEntity.

        成员Id

        :return: The member_id of this GroupMemberEntity.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this GroupMemberEntity.

        成员Id

        :param member_id: The member_id of this GroupMemberEntity.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def client_id(self):
        r"""Gets the client_id of this GroupMemberEntity.

        客户端Id

        :return: The client_id of this GroupMemberEntity.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this GroupMemberEntity.

        客户端Id

        :param client_id: The client_id of this GroupMemberEntity.
        :type client_id: str
        """
        self._client_id = client_id

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
        if not isinstance(other, GroupMemberEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
