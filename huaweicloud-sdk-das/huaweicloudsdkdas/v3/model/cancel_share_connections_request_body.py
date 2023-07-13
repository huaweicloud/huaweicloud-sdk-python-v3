# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CancelShareConnectionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shared_conn_id': 'str',
        'users': 'list[ShareConnUserInfo]'
    }

    attribute_map = {
        'shared_conn_id': 'shared_conn_id',
        'users': 'users'
    }

    def __init__(self, shared_conn_id=None, users=None):
        """CancelShareConnectionsRequestBody

        The model defined in huaweicloud sdk

        :param shared_conn_id: 共享链接ID
        :type shared_conn_id: str
        :param users: 用户
        :type users: list[:class:`huaweicloudsdkdas.v3.ShareConnUserInfo`]
        """
        
        

        self._shared_conn_id = None
        self._users = None
        self.discriminator = None

        self.shared_conn_id = shared_conn_id
        self.users = users

    @property
    def shared_conn_id(self):
        """Gets the shared_conn_id of this CancelShareConnectionsRequestBody.

        共享链接ID

        :return: The shared_conn_id of this CancelShareConnectionsRequestBody.
        :rtype: str
        """
        return self._shared_conn_id

    @shared_conn_id.setter
    def shared_conn_id(self, shared_conn_id):
        """Sets the shared_conn_id of this CancelShareConnectionsRequestBody.

        共享链接ID

        :param shared_conn_id: The shared_conn_id of this CancelShareConnectionsRequestBody.
        :type shared_conn_id: str
        """
        self._shared_conn_id = shared_conn_id

    @property
    def users(self):
        """Gets the users of this CancelShareConnectionsRequestBody.

        用户

        :return: The users of this CancelShareConnectionsRequestBody.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ShareConnUserInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this CancelShareConnectionsRequestBody.

        用户

        :param users: The users of this CancelShareConnectionsRequestBody.
        :type users: list[:class:`huaweicloudsdkdas.v3.ShareConnUserInfo`]
        """
        self._users = users

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
        if not isinstance(other, CancelShareConnectionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
