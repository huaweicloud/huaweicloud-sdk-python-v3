# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSchemaNamesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_id': 'str',
        'db_name': 'str',
        'obj_type': 'str',
        'is_with_all_user': 'str',
        'node_type': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'connection_id': 'connection_id',
        'db_name': 'db_name',
        'obj_type': 'obj_type',
        'is_with_all_user': 'is_with_all_user',
        'node_type': 'node_type',
        'node_id': 'node_id'
    }

    def __init__(self, connection_id=None, db_name=None, obj_type=None, is_with_all_user=None, node_type=None, node_id=None):
        r"""ListSchemaNamesRequest

        The model defined in huaweicloud sdk

        :param connection_id: 连接ID
        :type connection_id: str
        :param db_name: 数据库名
        :type db_name: str
        :param obj_type: 对象类型
        :type obj_type: str
        :param is_with_all_user: 是否包含所有用户
        :type is_with_all_user: str
        :param node_type: 节点类型
        :type node_type: str
        :param node_id: 节点ID
        :type node_id: str
        """
        
        

        self._connection_id = None
        self._db_name = None
        self._obj_type = None
        self._is_with_all_user = None
        self._node_type = None
        self._node_id = None
        self.discriminator = None

        self.connection_id = connection_id
        self.db_name = db_name
        if obj_type is not None:
            self.obj_type = obj_type
        if is_with_all_user is not None:
            self.is_with_all_user = is_with_all_user
        if node_type is not None:
            self.node_type = node_type
        if node_id is not None:
            self.node_id = node_id

    @property
    def connection_id(self):
        r"""Gets the connection_id of this ListSchemaNamesRequest.

        连接ID

        :return: The connection_id of this ListSchemaNamesRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this ListSchemaNamesRequest.

        连接ID

        :param connection_id: The connection_id of this ListSchemaNamesRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def db_name(self):
        r"""Gets the db_name of this ListSchemaNamesRequest.

        数据库名

        :return: The db_name of this ListSchemaNamesRequest.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this ListSchemaNamesRequest.

        数据库名

        :param db_name: The db_name of this ListSchemaNamesRequest.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def obj_type(self):
        r"""Gets the obj_type of this ListSchemaNamesRequest.

        对象类型

        :return: The obj_type of this ListSchemaNamesRequest.
        :rtype: str
        """
        return self._obj_type

    @obj_type.setter
    def obj_type(self, obj_type):
        r"""Sets the obj_type of this ListSchemaNamesRequest.

        对象类型

        :param obj_type: The obj_type of this ListSchemaNamesRequest.
        :type obj_type: str
        """
        self._obj_type = obj_type

    @property
    def is_with_all_user(self):
        r"""Gets the is_with_all_user of this ListSchemaNamesRequest.

        是否包含所有用户

        :return: The is_with_all_user of this ListSchemaNamesRequest.
        :rtype: str
        """
        return self._is_with_all_user

    @is_with_all_user.setter
    def is_with_all_user(self, is_with_all_user):
        r"""Sets the is_with_all_user of this ListSchemaNamesRequest.

        是否包含所有用户

        :param is_with_all_user: The is_with_all_user of this ListSchemaNamesRequest.
        :type is_with_all_user: str
        """
        self._is_with_all_user = is_with_all_user

    @property
    def node_type(self):
        r"""Gets the node_type of this ListSchemaNamesRequest.

        节点类型

        :return: The node_type of this ListSchemaNamesRequest.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this ListSchemaNamesRequest.

        节点类型

        :param node_type: The node_type of this ListSchemaNamesRequest.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_id(self):
        r"""Gets the node_id of this ListSchemaNamesRequest.

        节点ID

        :return: The node_id of this ListSchemaNamesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListSchemaNamesRequest.

        节点ID

        :param node_id: The node_id of this ListSchemaNamesRequest.
        :type node_id: str
        """
        self._node_id = node_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListSchemaNamesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
