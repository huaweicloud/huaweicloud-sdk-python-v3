# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityPermissionSetsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'parent_id': 'str',
        'type_filter': 'str',
        'manager_id': 'str',
        'manager_name': 'str',
        'manager_type': 'str',
        'datasource_type': 'str',
        'sync_status': 'str',
        'order_by': 'str',
        'order_by_asc': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'parent_id': 'parent_id',
        'type_filter': 'type_filter',
        'manager_id': 'manager_id',
        'manager_name': 'manager_name',
        'manager_type': 'manager_type',
        'datasource_type': 'datasource_type',
        'sync_status': 'sync_status',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc'
    }

    def __init__(self, workspace=None, limit=None, offset=None, name=None, parent_id=None, type_filter=None, manager_id=None, manager_name=None, manager_type=None, datasource_type=None, sync_status=None, order_by=None, order_by_asc=None):
        r"""ListSecurityPermissionSetsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param name: 名称
        :type name: str
        :param parent_id: 父权限集id
        :type parent_id: str
        :param type_filter: 权限集类型过滤,TOP_PERMISSION_SET,SUB_PERMISSION_SET,ALL_PERMISSION_SET
        :type type_filter: str
        :param manager_id: 管理员id
        :type manager_id: str
        :param manager_name: 管理员名称
        :type manager_name: str
        :param manager_type: 管理员类型,USER,USER_GROUP
        :type manager_type: str
        :param datasource_type: 数据源类型,HIVE
        :type datasource_type: str
        :param sync_status: 同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL
        :type sync_status: str
        :param order_by: 排序参数, NAME,CREATE_TIME,UPDATE_TIME
        :type order_by: str
        :param order_by_asc: 是否升序（仅指定排序参数时有效）
        :type order_by_asc: bool
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._name = None
        self._parent_id = None
        self._type_filter = None
        self._manager_id = None
        self._manager_name = None
        self._manager_type = None
        self._datasource_type = None
        self._sync_status = None
        self._order_by = None
        self._order_by_asc = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if type_filter is not None:
            self.type_filter = type_filter
        if manager_id is not None:
            self.manager_id = manager_id
        if manager_name is not None:
            self.manager_name = manager_name
        if manager_type is not None:
            self.manager_type = manager_type
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if sync_status is not None:
            self.sync_status = sync_status
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityPermissionSetsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityPermissionSetsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityPermissionSetsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityPermissionSetsRequest.

        limit

        :return: The limit of this ListSecurityPermissionSetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityPermissionSetsRequest.

        limit

        :param limit: The limit of this ListSecurityPermissionSetsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityPermissionSetsRequest.

        offset

        :return: The offset of this ListSecurityPermissionSetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityPermissionSetsRequest.

        offset

        :param offset: The offset of this ListSecurityPermissionSetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListSecurityPermissionSetsRequest.

        名称

        :return: The name of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSecurityPermissionSetsRequest.

        名称

        :param name: The name of this ListSecurityPermissionSetsRequest.
        :type name: str
        """
        self._name = name

    @property
    def parent_id(self):
        r"""Gets the parent_id of this ListSecurityPermissionSetsRequest.

        父权限集id

        :return: The parent_id of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        r"""Sets the parent_id of this ListSecurityPermissionSetsRequest.

        父权限集id

        :param parent_id: The parent_id of this ListSecurityPermissionSetsRequest.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def type_filter(self):
        r"""Gets the type_filter of this ListSecurityPermissionSetsRequest.

        权限集类型过滤,TOP_PERMISSION_SET,SUB_PERMISSION_SET,ALL_PERMISSION_SET

        :return: The type_filter of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._type_filter

    @type_filter.setter
    def type_filter(self, type_filter):
        r"""Sets the type_filter of this ListSecurityPermissionSetsRequest.

        权限集类型过滤,TOP_PERMISSION_SET,SUB_PERMISSION_SET,ALL_PERMISSION_SET

        :param type_filter: The type_filter of this ListSecurityPermissionSetsRequest.
        :type type_filter: str
        """
        self._type_filter = type_filter

    @property
    def manager_id(self):
        r"""Gets the manager_id of this ListSecurityPermissionSetsRequest.

        管理员id

        :return: The manager_id of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._manager_id

    @manager_id.setter
    def manager_id(self, manager_id):
        r"""Sets the manager_id of this ListSecurityPermissionSetsRequest.

        管理员id

        :param manager_id: The manager_id of this ListSecurityPermissionSetsRequest.
        :type manager_id: str
        """
        self._manager_id = manager_id

    @property
    def manager_name(self):
        r"""Gets the manager_name of this ListSecurityPermissionSetsRequest.

        管理员名称

        :return: The manager_name of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._manager_name

    @manager_name.setter
    def manager_name(self, manager_name):
        r"""Sets the manager_name of this ListSecurityPermissionSetsRequest.

        管理员名称

        :param manager_name: The manager_name of this ListSecurityPermissionSetsRequest.
        :type manager_name: str
        """
        self._manager_name = manager_name

    @property
    def manager_type(self):
        r"""Gets the manager_type of this ListSecurityPermissionSetsRequest.

        管理员类型,USER,USER_GROUP

        :return: The manager_type of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._manager_type

    @manager_type.setter
    def manager_type(self, manager_type):
        r"""Sets the manager_type of this ListSecurityPermissionSetsRequest.

        管理员类型,USER,USER_GROUP

        :param manager_type: The manager_type of this ListSecurityPermissionSetsRequest.
        :type manager_type: str
        """
        self._manager_type = manager_type

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ListSecurityPermissionSetsRequest.

        数据源类型,HIVE

        :return: The datasource_type of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ListSecurityPermissionSetsRequest.

        数据源类型,HIVE

        :param datasource_type: The datasource_type of this ListSecurityPermissionSetsRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def sync_status(self):
        r"""Gets the sync_status of this ListSecurityPermissionSetsRequest.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :return: The sync_status of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        r"""Sets the sync_status of this ListSecurityPermissionSetsRequest.

        同步状态,UNKNOWN,NOT_SYNC,SYNCING,SYNC_SUCCESS,SYNC_FAIL

        :param sync_status: The sync_status of this ListSecurityPermissionSetsRequest.
        :type sync_status: str
        """
        self._sync_status = sync_status

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityPermissionSetsRequest.

        排序参数, NAME,CREATE_TIME,UPDATE_TIME

        :return: The order_by of this ListSecurityPermissionSetsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityPermissionSetsRequest.

        排序参数, NAME,CREATE_TIME,UPDATE_TIME

        :param order_by: The order_by of this ListSecurityPermissionSetsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecurityPermissionSetsRequest.

        是否升序（仅指定排序参数时有效）

        :return: The order_by_asc of this ListSecurityPermissionSetsRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecurityPermissionSetsRequest.

        是否升序（仅指定排序参数时有效）

        :param order_by_asc: The order_by_asc of this ListSecurityPermissionSetsRequest.
        :type order_by_asc: bool
        """
        self._order_by_asc = order_by_asc

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
        if not isinstance(other, ListSecurityPermissionSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
