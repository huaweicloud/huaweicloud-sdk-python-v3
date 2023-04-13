# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSelfPrivilegesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_app_user_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'privilege_type': 'str'
    }

    attribute_map = {
        'x_app_user_id': 'X-App-UserId',
        'limit': 'limit',
        'offset': 'offset',
        'privilege_type': 'privilege_type'
    }

    def __init__(self, x_app_user_id=None, limit=None, offset=None, privilege_type=None):
        """ListSelfPrivilegesRequest

        The model defined in huaweicloud sdk

        :param x_app_user_id: 开发者应用作为资产权属的可选字段。
        :type x_app_user_id: str
        :param limit: 每页显示的条目数量
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询
        :type offset: int
        :param privilege_type: 权限类型
        :type privilege_type: str
        """
        
        

        self._x_app_user_id = None
        self._limit = None
        self._offset = None
        self._privilege_type = None
        self.discriminator = None

        if x_app_user_id is not None:
            self.x_app_user_id = x_app_user_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if privilege_type is not None:
            self.privilege_type = privilege_type

    @property
    def x_app_user_id(self):
        """Gets the x_app_user_id of this ListSelfPrivilegesRequest.

        开发者应用作为资产权属的可选字段。

        :return: The x_app_user_id of this ListSelfPrivilegesRequest.
        :rtype: str
        """
        return self._x_app_user_id

    @x_app_user_id.setter
    def x_app_user_id(self, x_app_user_id):
        """Sets the x_app_user_id of this ListSelfPrivilegesRequest.

        开发者应用作为资产权属的可选字段。

        :param x_app_user_id: The x_app_user_id of this ListSelfPrivilegesRequest.
        :type x_app_user_id: str
        """
        self._x_app_user_id = x_app_user_id

    @property
    def limit(self):
        """Gets the limit of this ListSelfPrivilegesRequest.

        每页显示的条目数量

        :return: The limit of this ListSelfPrivilegesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSelfPrivilegesRequest.

        每页显示的条目数量

        :param limit: The limit of this ListSelfPrivilegesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListSelfPrivilegesRequest.

        偏移量，表示从此偏移量开始查询

        :return: The offset of this ListSelfPrivilegesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSelfPrivilegesRequest.

        偏移量，表示从此偏移量开始查询

        :param offset: The offset of this ListSelfPrivilegesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def privilege_type(self):
        """Gets the privilege_type of this ListSelfPrivilegesRequest.

        权限类型

        :return: The privilege_type of this ListSelfPrivilegesRequest.
        :rtype: str
        """
        return self._privilege_type

    @privilege_type.setter
    def privilege_type(self, privilege_type):
        """Sets the privilege_type of this ListSelfPrivilegesRequest.

        权限类型

        :param privilege_type: The privilege_type of this ListSelfPrivilegesRequest.
        :type privilege_type: str
        """
        self._privilege_type = privilege_type

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
        if not isinstance(other, ListSelfPrivilegesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
