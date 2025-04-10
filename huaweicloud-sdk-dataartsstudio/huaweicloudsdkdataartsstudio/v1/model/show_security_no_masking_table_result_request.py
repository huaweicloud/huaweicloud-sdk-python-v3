# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityNoMaskingTableResultRequest:

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
        'diagnose_id': 'str',
        'datasource_type': 'str',
        'database': 'str',
        'cluster_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'limit': 'limit',
        'offset': 'offset',
        'diagnose_id': 'diagnose_id',
        'datasource_type': 'datasource_type',
        'database': 'database',
        'cluster_name': 'cluster_name'
    }

    def __init__(self, workspace=None, limit=None, offset=None, diagnose_id=None, datasource_type=None, database=None, cluster_name=None):
        r"""ShowSecurityNoMaskingTableResultRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param limit: limit
        :type limit: int
        :param offset: offset
        :type offset: int
        :param diagnose_id: 诊断任务id，通过调用查询数据权限控制模块诊断结果接口获取。
        :type diagnose_id: str
        :param datasource_type: 数据源类型,HIVE
        :type datasource_type: str
        :param database: 数据库名称
        :type database: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        """
        
        

        self._workspace = None
        self._limit = None
        self._offset = None
        self._diagnose_id = None
        self._datasource_type = None
        self._database = None
        self._cluster_name = None
        self.discriminator = None

        self.workspace = workspace
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.diagnose_id = diagnose_id
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if database is not None:
            self.database = database
        if cluster_name is not None:
            self.cluster_name = cluster_name

    @property
    def workspace(self):
        r"""Gets the workspace of this ShowSecurityNoMaskingTableResultRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowSecurityNoMaskingTableResultRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ShowSecurityNoMaskingTableResultRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowSecurityNoMaskingTableResultRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def limit(self):
        r"""Gets the limit of this ShowSecurityNoMaskingTableResultRequest.

        limit

        :return: The limit of this ShowSecurityNoMaskingTableResultRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowSecurityNoMaskingTableResultRequest.

        limit

        :param limit: The limit of this ShowSecurityNoMaskingTableResultRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowSecurityNoMaskingTableResultRequest.

        offset

        :return: The offset of this ShowSecurityNoMaskingTableResultRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowSecurityNoMaskingTableResultRequest.

        offset

        :param offset: The offset of this ShowSecurityNoMaskingTableResultRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def diagnose_id(self):
        r"""Gets the diagnose_id of this ShowSecurityNoMaskingTableResultRequest.

        诊断任务id，通过调用查询数据权限控制模块诊断结果接口获取。

        :return: The diagnose_id of this ShowSecurityNoMaskingTableResultRequest.
        :rtype: str
        """
        return self._diagnose_id

    @diagnose_id.setter
    def diagnose_id(self, diagnose_id):
        r"""Sets the diagnose_id of this ShowSecurityNoMaskingTableResultRequest.

        诊断任务id，通过调用查询数据权限控制模块诊断结果接口获取。

        :param diagnose_id: The diagnose_id of this ShowSecurityNoMaskingTableResultRequest.
        :type diagnose_id: str
        """
        self._diagnose_id = diagnose_id

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this ShowSecurityNoMaskingTableResultRequest.

        数据源类型,HIVE

        :return: The datasource_type of this ShowSecurityNoMaskingTableResultRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this ShowSecurityNoMaskingTableResultRequest.

        数据源类型,HIVE

        :param datasource_type: The datasource_type of this ShowSecurityNoMaskingTableResultRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def database(self):
        r"""Gets the database of this ShowSecurityNoMaskingTableResultRequest.

        数据库名称

        :return: The database of this ShowSecurityNoMaskingTableResultRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ShowSecurityNoMaskingTableResultRequest.

        数据库名称

        :param database: The database of this ShowSecurityNoMaskingTableResultRequest.
        :type database: str
        """
        self._database = database

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowSecurityNoMaskingTableResultRequest.

        集群名称

        :return: The cluster_name of this ShowSecurityNoMaskingTableResultRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowSecurityNoMaskingTableResultRequest.

        集群名称

        :param cluster_name: The cluster_name of this ShowSecurityNoMaskingTableResultRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

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
        if not isinstance(other, ShowSecurityNoMaskingTableResultRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
