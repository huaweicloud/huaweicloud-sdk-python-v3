# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStarRocksDatabaseUserRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'user_name': 'str',
        'limit': 'int',
        'x_language': 'str',
        'offset': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'user_name': 'user_name',
        'limit': 'limit',
        'x_language': 'X-Language',
        'offset': 'offset'
    }

    def __init__(self, instance_id=None, user_name=None, limit=None, x_language=None, offset=None):
        """ShowStarRocksDatabaseUserRequest

        The model defined in huaweicloud sdk

        :param instance_id: StarRocks实例ID，严格匹配UUID规则。
        :type instance_id: str
        :param user_name: 数据库账户。
        :type user_name: str
        :param limit: 查询记录数，不能为负数，最小值为1，最大值为100。
        :type limit: int
        :param x_language: 请求语言类型。默认en-us。 取值范围： - en-us - zh-cn
        :type x_language: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        """
        
        

        self._instance_id = None
        self._user_name = None
        self._limit = None
        self._x_language = None
        self._offset = None
        self.discriminator = None

        self.instance_id = instance_id
        if user_name is not None:
            self.user_name = user_name
        self.limit = limit
        if x_language is not None:
            self.x_language = x_language
        self.offset = offset

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowStarRocksDatabaseUserRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :return: The instance_id of this ShowStarRocksDatabaseUserRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowStarRocksDatabaseUserRequest.

        StarRocks实例ID，严格匹配UUID规则。

        :param instance_id: The instance_id of this ShowStarRocksDatabaseUserRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        """Gets the user_name of this ShowStarRocksDatabaseUserRequest.

        数据库账户。

        :return: The user_name of this ShowStarRocksDatabaseUserRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ShowStarRocksDatabaseUserRequest.

        数据库账户。

        :param user_name: The user_name of this ShowStarRocksDatabaseUserRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def limit(self):
        """Gets the limit of this ShowStarRocksDatabaseUserRequest.

        查询记录数，不能为负数，最小值为1，最大值为100。

        :return: The limit of this ShowStarRocksDatabaseUserRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowStarRocksDatabaseUserRequest.

        查询记录数，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this ShowStarRocksDatabaseUserRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ShowStarRocksDatabaseUserRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :return: The x_language of this ShowStarRocksDatabaseUserRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ShowStarRocksDatabaseUserRequest.

        请求语言类型。默认en-us。 取值范围： - en-us - zh-cn

        :param x_language: The x_language of this ShowStarRocksDatabaseUserRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        """Gets the offset of this ShowStarRocksDatabaseUserRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowStarRocksDatabaseUserRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowStarRocksDatabaseUserRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowStarRocksDatabaseUserRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ShowStarRocksDatabaseUserRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
