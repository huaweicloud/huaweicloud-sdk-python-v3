# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppAuthorizationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'app_id': 'str',
        'name': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'app_id': 'app_id',
        'name': 'name',
        'target_type': 'target_type'
    }

    def __init__(self, offset=None, limit=None, app_id=None, name=None, target_type=None):
        """ListAppAuthorizationsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量。
        :type offset: int
        :param limit: 单次查询的大小[1-100]。
        :type limit: int
        :param app_id: 应用ID。
        :type app_id: str
        :param name: 用户名/用户组名。
        :type name: str
        :param target_type: 类型： * &#x60;SIMPLE&#x60; - 普通用户 * &#x60;USER_GROUP&#x60; - 用户组
        :type target_type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._app_id = None
        self._name = None
        self._target_type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.app_id = app_id
        if name is not None:
            self.name = name
        if target_type is not None:
            self.target_type = target_type

    @property
    def offset(self):
        """Gets the offset of this ListAppAuthorizationsRequest.

        查询的偏移量。

        :return: The offset of this ListAppAuthorizationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListAppAuthorizationsRequest.

        查询的偏移量。

        :param offset: The offset of this ListAppAuthorizationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListAppAuthorizationsRequest.

        单次查询的大小[1-100]。

        :return: The limit of this ListAppAuthorizationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAppAuthorizationsRequest.

        单次查询的大小[1-100]。

        :param limit: The limit of this ListAppAuthorizationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def app_id(self):
        """Gets the app_id of this ListAppAuthorizationsRequest.

        应用ID。

        :return: The app_id of this ListAppAuthorizationsRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListAppAuthorizationsRequest.

        应用ID。

        :param app_id: The app_id of this ListAppAuthorizationsRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def name(self):
        """Gets the name of this ListAppAuthorizationsRequest.

        用户名/用户组名。

        :return: The name of this ListAppAuthorizationsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAppAuthorizationsRequest.

        用户名/用户组名。

        :param name: The name of this ListAppAuthorizationsRequest.
        :type name: str
        """
        self._name = name

    @property
    def target_type(self):
        """Gets the target_type of this ListAppAuthorizationsRequest.

        类型： * `SIMPLE` - 普通用户 * `USER_GROUP` - 用户组

        :return: The target_type of this ListAppAuthorizationsRequest.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this ListAppAuthorizationsRequest.

        类型： * `SIMPLE` - 普通用户 * `USER_GROUP` - 用户组

        :param target_type: The target_type of this ListAppAuthorizationsRequest.
        :type target_type: str
        """
        self._target_type = target_type

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
        if not isinstance(other, ListAppAuthorizationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
