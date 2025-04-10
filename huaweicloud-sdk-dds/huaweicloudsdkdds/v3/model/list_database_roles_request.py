# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseRolesRequest:

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
        'role_name': 'str',
        'db_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'role_name': 'role_name',
        'db_name': 'db_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, role_name=None, db_name=None, offset=None, limit=None):
        r"""ListDatabaseRolesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。
        :type instance_id: str
        :param role_name: 角色名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。
        :type role_name: str
        :param db_name: 数据库名称，默认为admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。
        :type db_name: str
        :param offset: 索引位置偏移量。 取值大于或等于0。不传该参数时，查询偏移量默认为0。
        :type offset: int
        :param limit: 查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._role_name = None
        self._db_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if role_name is not None:
            self.role_name = role_name
        if db_name is not None:
            self.db_name = db_name
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDatabaseRolesRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :return: The instance_id of this ListDatabaseRolesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDatabaseRolesRequest.

        实例ID，可以调用“查询实例列表和详情”接口获取。如果未申请实例，可以调用“创建实例”接口创建。

        :param instance_id: The instance_id of this ListDatabaseRolesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def role_name(self):
        r"""Gets the role_name of this ListDatabaseRolesRequest.

        角色名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :return: The role_name of this ListDatabaseRolesRequest.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        r"""Sets the role_name of this ListDatabaseRolesRequest.

        角色名称。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、中划线、下划线和点。

        :param role_name: The role_name of this ListDatabaseRolesRequest.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def db_name(self):
        r"""Gets the db_name of this ListDatabaseRolesRequest.

        数据库名称，默认为admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :return: The db_name of this ListDatabaseRolesRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListDatabaseRolesRequest.

        数据库名称，默认为admin。 - 长度为1~64位，可以包含大写字母（A~Z）、小写字母（a~z）、数字（0~9）、下划线。

        :param db_name: The db_name of this ListDatabaseRolesRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def offset(self):
        r"""Gets the offset of this ListDatabaseRolesRequest.

        索引位置偏移量。 取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :return: The offset of this ListDatabaseRolesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDatabaseRolesRequest.

        索引位置偏移量。 取值大于或等于0。不传该参数时，查询偏移量默认为0。

        :param offset: The offset of this ListDatabaseRolesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDatabaseRolesRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :return: The limit of this ListDatabaseRolesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDatabaseRolesRequest.

        查询实例个数上限值。 取值范围：1~100。不传该参数时，默认查询前100条实例信息。

        :param limit: The limit of this ListDatabaseRolesRequest.
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
        if not isinstance(other, ListDatabaseRolesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
