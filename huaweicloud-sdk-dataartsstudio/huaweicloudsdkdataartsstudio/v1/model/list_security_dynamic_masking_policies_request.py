# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecurityDynamicMaskingPoliciesRequest:

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
        'cluster_name': 'str',
        'database_name': 'str',
        'table_name': 'str',
        'order_by': 'str',
        'order_by_asc': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'cluster_name': 'cluster_name',
        'database_name': 'database_name',
        'table_name': 'table_name',
        'order_by': 'order_by',
        'order_by_asc': 'order_by_asc'
    }

    def __init__(self, workspace=None, limit=None, offset=None, name=None, cluster_name=None, database_name=None, table_name=None, order_by=None, order_by_asc=None):
        r"""ListSecurityDynamicMaskingPoliciesRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param name: 动态脱敏策略名称。
        :type name: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param database_name: 数据库名称
        :type database_name: str
        :param table_name: 表名称
        :type table_name: str
        :param order_by: 排序参数，UPDATE_TIME。
        :type order_by: str
        :param order_by_asc: 是否升序（仅指定排序参数时有效）。
        :type order_by_asc: bool
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._name = None
        self._cluster_name = None
        self._database_name = None
        self._table_name = None
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
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if database_name is not None:
            self.database_name = database_name
        if table_name is not None:
            self.table_name = table_name
        if order_by is not None:
            self.order_by = order_by
        if order_by_asc is not None:
            self.order_by_asc = order_by_asc

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecurityDynamicMaskingPoliciesRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecurityDynamicMaskingPoliciesRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecurityDynamicMaskingPoliciesRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ListSecurityDynamicMaskingPoliciesRequest.

        limit

        :return: The limit of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecurityDynamicMaskingPoliciesRequest.

        limit

        :param limit: The limit of this ListSecurityDynamicMaskingPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSecurityDynamicMaskingPoliciesRequest.

        offset

        :return: The offset of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecurityDynamicMaskingPoliciesRequest.

        offset

        :param offset: The offset of this ListSecurityDynamicMaskingPoliciesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListSecurityDynamicMaskingPoliciesRequest.

        动态脱敏策略名称。

        :return: The name of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSecurityDynamicMaskingPoliciesRequest.

        动态脱敏策略名称。

        :param name: The name of this ListSecurityDynamicMaskingPoliciesRequest.
        :type name: str
        """
        self._name = name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListSecurityDynamicMaskingPoliciesRequest.

        集群名称

        :return: The cluster_name of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListSecurityDynamicMaskingPoliciesRequest.

        集群名称

        :param cluster_name: The cluster_name of this ListSecurityDynamicMaskingPoliciesRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListSecurityDynamicMaskingPoliciesRequest.

        数据库名称

        :return: The database_name of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListSecurityDynamicMaskingPoliciesRequest.

        数据库名称

        :param database_name: The database_name of this ListSecurityDynamicMaskingPoliciesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def table_name(self):
        r"""Gets the table_name of this ListSecurityDynamicMaskingPoliciesRequest.

        表名称

        :return: The table_name of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        r"""Sets the table_name of this ListSecurityDynamicMaskingPoliciesRequest.

        表名称

        :param table_name: The table_name of this ListSecurityDynamicMaskingPoliciesRequest.
        :type table_name: str
        """
        self._table_name = table_name

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecurityDynamicMaskingPoliciesRequest.

        排序参数，UPDATE_TIME。

        :return: The order_by of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecurityDynamicMaskingPoliciesRequest.

        排序参数，UPDATE_TIME。

        :param order_by: The order_by of this ListSecurityDynamicMaskingPoliciesRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order_by_asc(self):
        r"""Gets the order_by_asc of this ListSecurityDynamicMaskingPoliciesRequest.

        是否升序（仅指定排序参数时有效）。

        :return: The order_by_asc of this ListSecurityDynamicMaskingPoliciesRequest.
        :rtype: bool
        """
        return self._order_by_asc

    @order_by_asc.setter
    def order_by_asc(self, order_by_asc):
        r"""Sets the order_by_asc of this ListSecurityDynamicMaskingPoliciesRequest.

        是否升序（仅指定排序参数时有效）。

        :param order_by_asc: The order_by_asc of this ListSecurityDynamicMaskingPoliciesRequest.
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
        if not isinstance(other, ListSecurityDynamicMaskingPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
