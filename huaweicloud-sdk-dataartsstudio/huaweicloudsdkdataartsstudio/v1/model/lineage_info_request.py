# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LineageInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'data_source_type': 'str',
        'connection_id': 'str',
        'connection_name': 'str',
        'workspace_id': 'str',
        'job_id': 'str',
        'node_name': 'str',
        'table_lineage': 'TableLineageV2'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'data_source_type': 'data_source_type',
        'connection_id': 'connection_id',
        'connection_name': 'connection_name',
        'workspace_id': 'workspace_id',
        'job_id': 'job_id',
        'node_name': 'node_name',
        'table_lineage': 'table_lineage'
    }

    def __init__(self, cluster_id=None, data_source_type=None, connection_id=None, connection_name=None, workspace_id=None, job_id=None, node_name=None, table_lineage=None):
        r"""LineageInfoRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param data_source_type: 数据连接类型
        :type data_source_type: str
        :param connection_id: 数据连接id
        :type connection_id: str
        :param connection_name: 数据连接名称
        :type connection_name: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param job_id: 作业id
        :type job_id: str
        :param node_name: 算子名称
        :type node_name: str
        :param table_lineage: 
        :type table_lineage: :class:`huaweicloudsdkdataartsstudio.v1.TableLineageV2`
        """
        
        

        self._cluster_id = None
        self._data_source_type = None
        self._connection_id = None
        self._connection_name = None
        self._workspace_id = None
        self._job_id = None
        self._node_name = None
        self._table_lineage = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if data_source_type is not None:
            self.data_source_type = data_source_type
        if connection_id is not None:
            self.connection_id = connection_id
        if connection_name is not None:
            self.connection_name = connection_name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if job_id is not None:
            self.job_id = job_id
        if node_name is not None:
            self.node_name = node_name
        if table_lineage is not None:
            self.table_lineage = table_lineage

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this LineageInfoRequest.

        集群id

        :return: The cluster_id of this LineageInfoRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this LineageInfoRequest.

        集群id

        :param cluster_id: The cluster_id of this LineageInfoRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def data_source_type(self):
        r"""Gets the data_source_type of this LineageInfoRequest.

        数据连接类型

        :return: The data_source_type of this LineageInfoRequest.
        :rtype: str
        """
        return self._data_source_type

    @data_source_type.setter
    def data_source_type(self, data_source_type):
        r"""Sets the data_source_type of this LineageInfoRequest.

        数据连接类型

        :param data_source_type: The data_source_type of this LineageInfoRequest.
        :type data_source_type: str
        """
        self._data_source_type = data_source_type

    @property
    def connection_id(self):
        r"""Gets the connection_id of this LineageInfoRequest.

        数据连接id

        :return: The connection_id of this LineageInfoRequest.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        r"""Sets the connection_id of this LineageInfoRequest.

        数据连接id

        :param connection_id: The connection_id of this LineageInfoRequest.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def connection_name(self):
        r"""Gets the connection_name of this LineageInfoRequest.

        数据连接名称

        :return: The connection_name of this LineageInfoRequest.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        r"""Sets the connection_name of this LineageInfoRequest.

        数据连接名称

        :param connection_name: The connection_name of this LineageInfoRequest.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this LineageInfoRequest.

        工作空间id

        :return: The workspace_id of this LineageInfoRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this LineageInfoRequest.

        工作空间id

        :param workspace_id: The workspace_id of this LineageInfoRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_id(self):
        r"""Gets the job_id of this LineageInfoRequest.

        作业id

        :return: The job_id of this LineageInfoRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this LineageInfoRequest.

        作业id

        :param job_id: The job_id of this LineageInfoRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def node_name(self):
        r"""Gets the node_name of this LineageInfoRequest.

        算子名称

        :return: The node_name of this LineageInfoRequest.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this LineageInfoRequest.

        算子名称

        :param node_name: The node_name of this LineageInfoRequest.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def table_lineage(self):
        r"""Gets the table_lineage of this LineageInfoRequest.

        :return: The table_lineage of this LineageInfoRequest.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.TableLineageV2`
        """
        return self._table_lineage

    @table_lineage.setter
    def table_lineage(self, table_lineage):
        r"""Sets the table_lineage of this LineageInfoRequest.

        :param table_lineage: The table_lineage of this LineageInfoRequest.
        :type table_lineage: :class:`huaweicloudsdkdataartsstudio.v1.TableLineageV2`
        """
        self._table_lineage = table_lineage

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
        if not isinstance(other, LineageInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
