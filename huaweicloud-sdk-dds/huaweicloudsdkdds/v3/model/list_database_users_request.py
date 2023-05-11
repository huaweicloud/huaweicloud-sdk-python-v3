# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseUsersRequest:

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
        'db_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'user_name': 'user_name',
        'db_name': 'db_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, user_name=None, db_name=None, offset=None, limit=None):
        """ListDatabaseUsersRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param user_name: 用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。
        :type user_name: str
        :param db_name: 数据库名称，默认为admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。
        :type db_name: str
        :param offset: 索引位置偏移量。 取值大于或等于0。不传该参数时，查询偏移量默认为0。
        :type offset: int
        :param limit: 查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._user_name = None
        self._db_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if user_name is not None:
            self.user_name = user_name
        if db_name is not None:
            self.db_name = db_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDatabaseUsersRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ListDatabaseUsersRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDatabaseUsersRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ListDatabaseUsersRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        """Gets the user_name of this ListDatabaseUsersRequest.

        用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :return: The user_name of this ListDatabaseUsersRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListDatabaseUsersRequest.

        用户名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :param user_name: The user_name of this ListDatabaseUsersRequest.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def db_name(self):
        """Gets the db_name of this ListDatabaseUsersRequest.

        数据库名称，默认为admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :return: The db_name of this ListDatabaseUsersRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """Sets the db_name of this ListDatabaseUsersRequest.

        数据库名称，默认为admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :param db_name: The db_name of this ListDatabaseUsersRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def offset(self):
        """Gets the offset of this ListDatabaseUsersRequest.

        索引位置偏移量。 取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :return: The offset of this ListDatabaseUsersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDatabaseUsersRequest.

        索引位置偏移量。 取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :param offset: The offset of this ListDatabaseUsersRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDatabaseUsersRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :return: The limit of this ListDatabaseUsersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatabaseUsersRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :param limit: The limit of this ListDatabaseUsersRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDatabaseUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
