# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiagnoseNoMaskingDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'task_id': 'str',
        'datasource_type': 'str',
        'cluster_name': 'str',
        'database': 'str',
        'schema': 'str',
        'table': 'str',
        'remark': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'task_id': 'task_id',
        'datasource_type': 'datasource_type',
        'cluster_name': 'cluster_name',
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'remark': 'remark'
    }

    def __init__(self, id=None, project_id=None, task_id=None, datasource_type=None, cluster_name=None, database=None, schema=None, table=None, remark=None):
        r"""DiagnoseNoMaskingDetail

        The model defined in huaweicloud sdk

        :param id: 详情uuid
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param task_id: 诊断任务id
        :type task_id: str
        :param datasource_type: 数据源类型
        :type datasource_type: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param database: 数据库名称
        :type database: str
        :param schema: schema名称
        :type schema: str
        :param table: 表名称
        :type table: str
        :param remark: 详情评价
        :type remark: str
        """
        
        

        self._id = None
        self._project_id = None
        self._task_id = None
        self._datasource_type = None
        self._cluster_name = None
        self._database = None
        self._schema = None
        self._table = None
        self._remark = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if task_id is not None:
            self.task_id = task_id
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if remark is not None:
            self.remark = remark

    @property
    def id(self):
        r"""Gets the id of this DiagnoseNoMaskingDetail.

        详情uuid

        :return: The id of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DiagnoseNoMaskingDetail.

        详情uuid

        :param id: The id of this DiagnoseNoMaskingDetail.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this DiagnoseNoMaskingDetail.

        项目ID

        :return: The project_id of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this DiagnoseNoMaskingDetail.

        项目ID

        :param project_id: The project_id of this DiagnoseNoMaskingDetail.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def task_id(self):
        r"""Gets the task_id of this DiagnoseNoMaskingDetail.

        诊断任务id

        :return: The task_id of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this DiagnoseNoMaskingDetail.

        诊断任务id

        :param task_id: The task_id of this DiagnoseNoMaskingDetail.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def datasource_type(self):
        r"""Gets the datasource_type of this DiagnoseNoMaskingDetail.

        数据源类型

        :return: The datasource_type of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        r"""Sets the datasource_type of this DiagnoseNoMaskingDetail.

        数据源类型

        :param datasource_type: The datasource_type of this DiagnoseNoMaskingDetail.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this DiagnoseNoMaskingDetail.

        集群名称

        :return: The cluster_name of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this DiagnoseNoMaskingDetail.

        集群名称

        :param cluster_name: The cluster_name of this DiagnoseNoMaskingDetail.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def database(self):
        r"""Gets the database of this DiagnoseNoMaskingDetail.

        数据库名称

        :return: The database of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this DiagnoseNoMaskingDetail.

        数据库名称

        :param database: The database of this DiagnoseNoMaskingDetail.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        r"""Gets the schema of this DiagnoseNoMaskingDetail.

        schema名称

        :return: The schema of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this DiagnoseNoMaskingDetail.

        schema名称

        :param schema: The schema of this DiagnoseNoMaskingDetail.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        r"""Gets the table of this DiagnoseNoMaskingDetail.

        表名称

        :return: The table of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this DiagnoseNoMaskingDetail.

        表名称

        :param table: The table of this DiagnoseNoMaskingDetail.
        :type table: str
        """
        self._table = table

    @property
    def remark(self):
        r"""Gets the remark of this DiagnoseNoMaskingDetail.

        详情评价

        :return: The remark of this DiagnoseNoMaskingDetail.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this DiagnoseNoMaskingDetail.

        详情评价

        :param remark: The remark of this DiagnoseNoMaskingDetail.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, DiagnoseNoMaskingDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
