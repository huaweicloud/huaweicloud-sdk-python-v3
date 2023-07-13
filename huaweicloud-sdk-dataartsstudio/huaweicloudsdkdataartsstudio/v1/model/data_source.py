# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datasource_name': 'str',
        'datasource_type': 'str',
        'datasource_guid': 'str',
        'datasource_qualified_name': 'str',
        'obs_folder_count': 'int',
        'obs_file_count': 'int',
        'css_index_count': 'int',
        'css_index_field_count': 'int',
        'namespace_count': 'int',
        'ges_vertex_count': 'int',
        'ges_edge_count': 'int',
        'database_count': 'int',
        'stream_count': 'int',
        'table_count': 'int',
        'data_size': 'int',
        'databases': 'list[Database]',
        'folders': 'list[ObsFolder]',
        'css_indices': 'list[CssIndex]',
        'namespaces': 'list[Namespace]',
        'dis_streams': 'list[DisStream]'
    }

    attribute_map = {
        'datasource_name': 'datasource_name',
        'datasource_type': 'datasource_type',
        'datasource_guid': 'datasource_guid',
        'datasource_qualified_name': 'datasource_qualified_name',
        'obs_folder_count': 'obs_folder_count',
        'obs_file_count': 'obs_file_count',
        'css_index_count': 'css_index_count',
        'css_index_field_count': 'css_index_field_count',
        'namespace_count': 'namespace_count',
        'ges_vertex_count': 'ges_vertex_count',
        'ges_edge_count': 'ges_edge_count',
        'database_count': 'database_count',
        'stream_count': 'stream_count',
        'table_count': 'table_count',
        'data_size': 'data_size',
        'databases': 'databases',
        'folders': 'folders',
        'css_indices': 'css_indices',
        'namespaces': 'namespaces',
        'dis_streams': 'dis_streams'
    }

    def __init__(self, datasource_name=None, datasource_type=None, datasource_guid=None, datasource_qualified_name=None, obs_folder_count=None, obs_file_count=None, css_index_count=None, css_index_field_count=None, namespace_count=None, ges_vertex_count=None, ges_edge_count=None, database_count=None, stream_count=None, table_count=None, data_size=None, databases=None, folders=None, css_indices=None, namespaces=None, dis_streams=None):
        """DataSource

        The model defined in huaweicloud sdk

        :param datasource_name: 数据连接名称
        :type datasource_name: str
        :param datasource_type: 数据连接类型
        :type datasource_type: str
        :param datasource_guid: 数据连接guid
        :type datasource_guid: str
        :param datasource_qualified_name: 数据连接唯一标识名称
        :type datasource_qualified_name: str
        :param obs_folder_count: obs目录数
        :type obs_folder_count: int
        :param obs_file_count: obs文件数
        :type obs_file_count: int
        :param css_index_count: css索引数
        :type css_index_count: int
        :param css_index_field_count: css 索引字段数目
        :type css_index_field_count: int
        :param namespace_count: 命名空间数
        :type namespace_count: int
        :param ges_vertex_count: ges点的总数
        :type ges_vertex_count: int
        :param ges_edge_count: ges边的总数
        :type ges_edge_count: int
        :param database_count: 数据库总数
        :type database_count: int
        :param stream_count: 通道总数
        :type stream_count: int
        :param table_count: 表总数
        :type table_count: int
        :param data_size: 数据大小
        :type data_size: int
        :param databases: 数据库统计信息
        :type databases: list[:class:`huaweicloudsdkdataartsstudio.v1.Database`]
        :param folders: 顶层目录统计信息
        :type folders: list[:class:`huaweicloudsdkdataartsstudio.v1.ObsFolder`]
        :param css_indices: css索引统计信息
        :type css_indices: list[:class:`huaweicloudsdkdataartsstudio.v1.CssIndex`]
        :param namespaces: 命名空间统计信息
        :type namespaces: list[:class:`huaweicloudsdkdataartsstudio.v1.Namespace`]
        :param dis_streams: 通道统计信息
        :type dis_streams: list[:class:`huaweicloudsdkdataartsstudio.v1.DisStream`]
        """
        
        

        self._datasource_name = None
        self._datasource_type = None
        self._datasource_guid = None
        self._datasource_qualified_name = None
        self._obs_folder_count = None
        self._obs_file_count = None
        self._css_index_count = None
        self._css_index_field_count = None
        self._namespace_count = None
        self._ges_vertex_count = None
        self._ges_edge_count = None
        self._database_count = None
        self._stream_count = None
        self._table_count = None
        self._data_size = None
        self._databases = None
        self._folders = None
        self._css_indices = None
        self._namespaces = None
        self._dis_streams = None
        self.discriminator = None

        if datasource_name is not None:
            self.datasource_name = datasource_name
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if datasource_guid is not None:
            self.datasource_guid = datasource_guid
        if datasource_qualified_name is not None:
            self.datasource_qualified_name = datasource_qualified_name
        if obs_folder_count is not None:
            self.obs_folder_count = obs_folder_count
        if obs_file_count is not None:
            self.obs_file_count = obs_file_count
        if css_index_count is not None:
            self.css_index_count = css_index_count
        if css_index_field_count is not None:
            self.css_index_field_count = css_index_field_count
        if namespace_count is not None:
            self.namespace_count = namespace_count
        if ges_vertex_count is not None:
            self.ges_vertex_count = ges_vertex_count
        if ges_edge_count is not None:
            self.ges_edge_count = ges_edge_count
        if database_count is not None:
            self.database_count = database_count
        if stream_count is not None:
            self.stream_count = stream_count
        if table_count is not None:
            self.table_count = table_count
        if data_size is not None:
            self.data_size = data_size
        if databases is not None:
            self.databases = databases
        if folders is not None:
            self.folders = folders
        if css_indices is not None:
            self.css_indices = css_indices
        if namespaces is not None:
            self.namespaces = namespaces
        if dis_streams is not None:
            self.dis_streams = dis_streams

    @property
    def datasource_name(self):
        """Gets the datasource_name of this DataSource.

        数据连接名称

        :return: The datasource_name of this DataSource.
        :rtype: str
        """
        return self._datasource_name

    @datasource_name.setter
    def datasource_name(self, datasource_name):
        """Sets the datasource_name of this DataSource.

        数据连接名称

        :param datasource_name: The datasource_name of this DataSource.
        :type datasource_name: str
        """
        self._datasource_name = datasource_name

    @property
    def datasource_type(self):
        """Gets the datasource_type of this DataSource.

        数据连接类型

        :return: The datasource_type of this DataSource.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this DataSource.

        数据连接类型

        :param datasource_type: The datasource_type of this DataSource.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def datasource_guid(self):
        """Gets the datasource_guid of this DataSource.

        数据连接guid

        :return: The datasource_guid of this DataSource.
        :rtype: str
        """
        return self._datasource_guid

    @datasource_guid.setter
    def datasource_guid(self, datasource_guid):
        """Sets the datasource_guid of this DataSource.

        数据连接guid

        :param datasource_guid: The datasource_guid of this DataSource.
        :type datasource_guid: str
        """
        self._datasource_guid = datasource_guid

    @property
    def datasource_qualified_name(self):
        """Gets the datasource_qualified_name of this DataSource.

        数据连接唯一标识名称

        :return: The datasource_qualified_name of this DataSource.
        :rtype: str
        """
        return self._datasource_qualified_name

    @datasource_qualified_name.setter
    def datasource_qualified_name(self, datasource_qualified_name):
        """Sets the datasource_qualified_name of this DataSource.

        数据连接唯一标识名称

        :param datasource_qualified_name: The datasource_qualified_name of this DataSource.
        :type datasource_qualified_name: str
        """
        self._datasource_qualified_name = datasource_qualified_name

    @property
    def obs_folder_count(self):
        """Gets the obs_folder_count of this DataSource.

        obs目录数

        :return: The obs_folder_count of this DataSource.
        :rtype: int
        """
        return self._obs_folder_count

    @obs_folder_count.setter
    def obs_folder_count(self, obs_folder_count):
        """Sets the obs_folder_count of this DataSource.

        obs目录数

        :param obs_folder_count: The obs_folder_count of this DataSource.
        :type obs_folder_count: int
        """
        self._obs_folder_count = obs_folder_count

    @property
    def obs_file_count(self):
        """Gets the obs_file_count of this DataSource.

        obs文件数

        :return: The obs_file_count of this DataSource.
        :rtype: int
        """
        return self._obs_file_count

    @obs_file_count.setter
    def obs_file_count(self, obs_file_count):
        """Sets the obs_file_count of this DataSource.

        obs文件数

        :param obs_file_count: The obs_file_count of this DataSource.
        :type obs_file_count: int
        """
        self._obs_file_count = obs_file_count

    @property
    def css_index_count(self):
        """Gets the css_index_count of this DataSource.

        css索引数

        :return: The css_index_count of this DataSource.
        :rtype: int
        """
        return self._css_index_count

    @css_index_count.setter
    def css_index_count(self, css_index_count):
        """Sets the css_index_count of this DataSource.

        css索引数

        :param css_index_count: The css_index_count of this DataSource.
        :type css_index_count: int
        """
        self._css_index_count = css_index_count

    @property
    def css_index_field_count(self):
        """Gets the css_index_field_count of this DataSource.

        css 索引字段数目

        :return: The css_index_field_count of this DataSource.
        :rtype: int
        """
        return self._css_index_field_count

    @css_index_field_count.setter
    def css_index_field_count(self, css_index_field_count):
        """Sets the css_index_field_count of this DataSource.

        css 索引字段数目

        :param css_index_field_count: The css_index_field_count of this DataSource.
        :type css_index_field_count: int
        """
        self._css_index_field_count = css_index_field_count

    @property
    def namespace_count(self):
        """Gets the namespace_count of this DataSource.

        命名空间数

        :return: The namespace_count of this DataSource.
        :rtype: int
        """
        return self._namespace_count

    @namespace_count.setter
    def namespace_count(self, namespace_count):
        """Sets the namespace_count of this DataSource.

        命名空间数

        :param namespace_count: The namespace_count of this DataSource.
        :type namespace_count: int
        """
        self._namespace_count = namespace_count

    @property
    def ges_vertex_count(self):
        """Gets the ges_vertex_count of this DataSource.

        ges点的总数

        :return: The ges_vertex_count of this DataSource.
        :rtype: int
        """
        return self._ges_vertex_count

    @ges_vertex_count.setter
    def ges_vertex_count(self, ges_vertex_count):
        """Sets the ges_vertex_count of this DataSource.

        ges点的总数

        :param ges_vertex_count: The ges_vertex_count of this DataSource.
        :type ges_vertex_count: int
        """
        self._ges_vertex_count = ges_vertex_count

    @property
    def ges_edge_count(self):
        """Gets the ges_edge_count of this DataSource.

        ges边的总数

        :return: The ges_edge_count of this DataSource.
        :rtype: int
        """
        return self._ges_edge_count

    @ges_edge_count.setter
    def ges_edge_count(self, ges_edge_count):
        """Sets the ges_edge_count of this DataSource.

        ges边的总数

        :param ges_edge_count: The ges_edge_count of this DataSource.
        :type ges_edge_count: int
        """
        self._ges_edge_count = ges_edge_count

    @property
    def database_count(self):
        """Gets the database_count of this DataSource.

        数据库总数

        :return: The database_count of this DataSource.
        :rtype: int
        """
        return self._database_count

    @database_count.setter
    def database_count(self, database_count):
        """Sets the database_count of this DataSource.

        数据库总数

        :param database_count: The database_count of this DataSource.
        :type database_count: int
        """
        self._database_count = database_count

    @property
    def stream_count(self):
        """Gets the stream_count of this DataSource.

        通道总数

        :return: The stream_count of this DataSource.
        :rtype: int
        """
        return self._stream_count

    @stream_count.setter
    def stream_count(self, stream_count):
        """Sets the stream_count of this DataSource.

        通道总数

        :param stream_count: The stream_count of this DataSource.
        :type stream_count: int
        """
        self._stream_count = stream_count

    @property
    def table_count(self):
        """Gets the table_count of this DataSource.

        表总数

        :return: The table_count of this DataSource.
        :rtype: int
        """
        return self._table_count

    @table_count.setter
    def table_count(self, table_count):
        """Sets the table_count of this DataSource.

        表总数

        :param table_count: The table_count of this DataSource.
        :type table_count: int
        """
        self._table_count = table_count

    @property
    def data_size(self):
        """Gets the data_size of this DataSource.

        数据大小

        :return: The data_size of this DataSource.
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this DataSource.

        数据大小

        :param data_size: The data_size of this DataSource.
        :type data_size: int
        """
        self._data_size = data_size

    @property
    def databases(self):
        """Gets the databases of this DataSource.

        数据库统计信息

        :return: The databases of this DataSource.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Database`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        """Sets the databases of this DataSource.

        数据库统计信息

        :param databases: The databases of this DataSource.
        :type databases: list[:class:`huaweicloudsdkdataartsstudio.v1.Database`]
        """
        self._databases = databases

    @property
    def folders(self):
        """Gets the folders of this DataSource.

        顶层目录统计信息

        :return: The folders of this DataSource.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ObsFolder`]
        """
        return self._folders

    @folders.setter
    def folders(self, folders):
        """Sets the folders of this DataSource.

        顶层目录统计信息

        :param folders: The folders of this DataSource.
        :type folders: list[:class:`huaweicloudsdkdataartsstudio.v1.ObsFolder`]
        """
        self._folders = folders

    @property
    def css_indices(self):
        """Gets the css_indices of this DataSource.

        css索引统计信息

        :return: The css_indices of this DataSource.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.CssIndex`]
        """
        return self._css_indices

    @css_indices.setter
    def css_indices(self, css_indices):
        """Sets the css_indices of this DataSource.

        css索引统计信息

        :param css_indices: The css_indices of this DataSource.
        :type css_indices: list[:class:`huaweicloudsdkdataartsstudio.v1.CssIndex`]
        """
        self._css_indices = css_indices

    @property
    def namespaces(self):
        """Gets the namespaces of this DataSource.

        命名空间统计信息

        :return: The namespaces of this DataSource.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Namespace`]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this DataSource.

        命名空间统计信息

        :param namespaces: The namespaces of this DataSource.
        :type namespaces: list[:class:`huaweicloudsdkdataartsstudio.v1.Namespace`]
        """
        self._namespaces = namespaces

    @property
    def dis_streams(self):
        """Gets the dis_streams of this DataSource.

        通道统计信息

        :return: The dis_streams of this DataSource.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DisStream`]
        """
        return self._dis_streams

    @dis_streams.setter
    def dis_streams(self, dis_streams):
        """Sets the dis_streams of this DataSource.

        通道统计信息

        :param dis_streams: The dis_streams of this DataSource.
        :type dis_streams: list[:class:`huaweicloudsdkdataartsstudio.v1.DisStream`]
        """
        self._dis_streams = dis_streams

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
        if not isinstance(other, DataSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
