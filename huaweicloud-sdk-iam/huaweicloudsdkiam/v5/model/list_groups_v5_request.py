# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupsV5Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'user_id': 'user_id'
    }

    def __init__(self, limit=None, marker=None, user_id=None):
        """ListGroupsV5Request

        The model defined in huaweicloud sdk

        :param limit: 每页显示的条目数量。
        :type limit: int
        :param marker: 分页标记，长度为4到400个字符，只包含字母、数字、\&quot;+\&quot;、\&quot;/\&quot;、\&quot;&#x3D;\&quot;、\&quot;-\&quot;和\&quot;_\&quot;的字符串。
        :type marker: str
        :param user_id: IAM用户ID，长度为1到64个字符，只包含字母、数字和\&quot;-\&quot;的字符串。
        :type user_id: str
        """
        
        

        self._limit = None
        self._marker = None
        self._user_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if user_id is not None:
            self.user_id = user_id

    @property
    def limit(self):
        """Gets the limit of this ListGroupsV5Request.

        每页显示的条目数量。

        :return: The limit of this ListGroupsV5Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGroupsV5Request.

        每页显示的条目数量。

        :param limit: The limit of this ListGroupsV5Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        """Gets the marker of this ListGroupsV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :return: The marker of this ListGroupsV5Request.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        """Sets the marker of this ListGroupsV5Request.

        分页标记，长度为4到400个字符，只包含字母、数字、\"+\"、\"/\"、\"=\"、\"-\"和\"_\"的字符串。

        :param marker: The marker of this ListGroupsV5Request.
        :type marker: str
        """
        self._marker = marker

    @property
    def user_id(self):
        """Gets the user_id of this ListGroupsV5Request.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :return: The user_id of this ListGroupsV5Request.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ListGroupsV5Request.

        IAM用户ID，长度为1到64个字符，只包含字母、数字和\"-\"的字符串。

        :param user_id: The user_id of this ListGroupsV5Request.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, ListGroupsV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
