# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScriptInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'directory': 'str',
        'id': 'str',
        'create_user': 'str',
        'connection_name': 'str',
        'database': 'str',
        'queue_name': 'str',
        'configuration': 'object',
        'description': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'directory': 'directory',
        'id': 'id',
        'create_user': 'create_user',
        'connection_name': 'connection_name',
        'database': 'database',
        'queue_name': 'queue_name',
        'configuration': 'configuration',
        'description': 'description'
    }

    def __init__(self, name=None, type=None, directory=None, id=None, create_user=None, connection_name=None, database=None, queue_name=None, configuration=None, description=None):
        r"""ScriptInfo

        The model defined in huaweicloud sdk

        :param name: 脚本名称，只能包含五种字符：英文字母、数字、中文、中划线和点号，且长度小于等于128个字符。脚本名称不能重复。
        :type name: str
        :param type: 脚本类型 - FlinkSQL: Flink SQL - DLISQL：DLI SQL - SparkSQL: MRS Spark SQL - HiveSQL: MRS Hive SQL - DWSSQL: DWS SQL - RDSSQL: RDS SQL - Shell: Shell 脚本 - PYTHON：Python 脚本 - PRESTO: MRS Presto SQL - ClickHouseSQL: MRS ClickHouse SQL - HetuEngineSQL: MRS HetuEngine SQL - ImpalaSQL: MRS Impala SQL - SparkPython: MRS Spark Python脚本
        :type type: str
        :param directory: 脚本所在目录路径 通过DataArts Studio管理控制台 &gt; 数据开发，左侧列表选择“数据开发 &gt; 脚本开发”。在脚本的目录树上，可以查看到当前已经创建的目录，默认在根目录/。
        :type directory: str
        :param id: 脚本id。
        :type id: str
        :param create_user: 脚本创建人
        :type create_user: str
        :param connection_name: 脚本关联的连接名称。当type参数值为DLISQL、SparkSQL、HiveSQL、DWSSQL、Shell、PRESTO、ClickHouseSQL、ImpalaSQL、HetuEngineSQL、RDSSQL其中之一时，这个参数是必选的。用户可以通过查询连接列表（待下线）接口获取当前系统中已经存在的连接。默认值为空。
        :type connection_name: str
        :param database: 执行SQL语句所关联的数据库，当type参数值为DLISQL、SparkSQL、HiveSQL、DWSSQL、PRESTO、ClickHouseSQL、ImpalaSQL、HetuEngineSQL、RDSSQL其中之一时，才支持此参数。 - type为DLISQL时，可以通过查看所有数据库接口获取数据库信息。 - type为其他类型的时候，需要通过JDBC方式连上集群，查询数据库信息。默认值为空。
        :type database: str
        :param queue_name: DLI资源队列名称，当type参数值为DLISQL时，才支持此参数。可以通过查询队列列表接口获取队列信息。默认值为空。
        :type queue_name: str
        :param configuration: 用户定义适用于此作业的配置参数，当type参数值为DLISQL时存在。当前支持的配置项列表请参考DLI的conf参数说明。默认值为空。
        :type configuration: object
        :param description: 描述，长度不能超过255个字符。
        :type description: str
        """
        
        

        self._name = None
        self._type = None
        self._directory = None
        self._id = None
        self._create_user = None
        self._connection_name = None
        self._database = None
        self._queue_name = None
        self._configuration = None
        self._description = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if directory is not None:
            self.directory = directory
        if id is not None:
            self.id = id
        if create_user is not None:
            self.create_user = create_user
        if connection_name is not None:
            self.connection_name = connection_name
        if database is not None:
            self.database = database
        if queue_name is not None:
            self.queue_name = queue_name
        if configuration is not None:
            self.configuration = configuration
        if description is not None:
            self.description = description

    @property
    def name(self):
        r"""Gets the name of this ScriptInfo.

        脚本名称，只能包含五种字符：英文字母、数字、中文、中划线和点号，且长度小于等于128个字符。脚本名称不能重复。

        :return: The name of this ScriptInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ScriptInfo.

        脚本名称，只能包含五种字符：英文字母、数字、中文、中划线和点号，且长度小于等于128个字符。脚本名称不能重复。

        :param name: The name of this ScriptInfo.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ScriptInfo.

        脚本类型 - FlinkSQL: Flink SQL - DLISQL：DLI SQL - SparkSQL: MRS Spark SQL - HiveSQL: MRS Hive SQL - DWSSQL: DWS SQL - RDSSQL: RDS SQL - Shell: Shell 脚本 - PYTHON：Python 脚本 - PRESTO: MRS Presto SQL - ClickHouseSQL: MRS ClickHouse SQL - HetuEngineSQL: MRS HetuEngine SQL - ImpalaSQL: MRS Impala SQL - SparkPython: MRS Spark Python脚本

        :return: The type of this ScriptInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ScriptInfo.

        脚本类型 - FlinkSQL: Flink SQL - DLISQL：DLI SQL - SparkSQL: MRS Spark SQL - HiveSQL: MRS Hive SQL - DWSSQL: DWS SQL - RDSSQL: RDS SQL - Shell: Shell 脚本 - PYTHON：Python 脚本 - PRESTO: MRS Presto SQL - ClickHouseSQL: MRS ClickHouse SQL - HetuEngineSQL: MRS HetuEngine SQL - ImpalaSQL: MRS Impala SQL - SparkPython: MRS Spark Python脚本

        :param type: The type of this ScriptInfo.
        :type type: str
        """
        self._type = type

    @property
    def directory(self):
        r"""Gets the directory of this ScriptInfo.

        脚本所在目录路径 通过DataArts Studio管理控制台 > 数据开发，左侧列表选择“数据开发 > 脚本开发”。在脚本的目录树上，可以查看到当前已经创建的目录，默认在根目录/。

        :return: The directory of this ScriptInfo.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        r"""Sets the directory of this ScriptInfo.

        脚本所在目录路径 通过DataArts Studio管理控制台 > 数据开发，左侧列表选择“数据开发 > 脚本开发”。在脚本的目录树上，可以查看到当前已经创建的目录，默认在根目录/。

        :param directory: The directory of this ScriptInfo.
        :type directory: str
        """
        self._directory = directory

    @property
    def id(self):
        r"""Gets the id of this ScriptInfo.

        脚本id。

        :return: The id of this ScriptInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ScriptInfo.

        脚本id。

        :param id: The id of this ScriptInfo.
        :type id: str
        """
        self._id = id

    @property
    def create_user(self):
        r"""Gets the create_user of this ScriptInfo.

        脚本创建人

        :return: The create_user of this ScriptInfo.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ScriptInfo.

        脚本创建人

        :param create_user: The create_user of this ScriptInfo.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def connection_name(self):
        r"""Gets the connection_name of this ScriptInfo.

        脚本关联的连接名称。当type参数值为DLISQL、SparkSQL、HiveSQL、DWSSQL、Shell、PRESTO、ClickHouseSQL、ImpalaSQL、HetuEngineSQL、RDSSQL其中之一时，这个参数是必选的。用户可以通过查询连接列表（待下线）接口获取当前系统中已经存在的连接。默认值为空。

        :return: The connection_name of this ScriptInfo.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        r"""Sets the connection_name of this ScriptInfo.

        脚本关联的连接名称。当type参数值为DLISQL、SparkSQL、HiveSQL、DWSSQL、Shell、PRESTO、ClickHouseSQL、ImpalaSQL、HetuEngineSQL、RDSSQL其中之一时，这个参数是必选的。用户可以通过查询连接列表（待下线）接口获取当前系统中已经存在的连接。默认值为空。

        :param connection_name: The connection_name of this ScriptInfo.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def database(self):
        r"""Gets the database of this ScriptInfo.

        执行SQL语句所关联的数据库，当type参数值为DLISQL、SparkSQL、HiveSQL、DWSSQL、PRESTO、ClickHouseSQL、ImpalaSQL、HetuEngineSQL、RDSSQL其中之一时，才支持此参数。 - type为DLISQL时，可以通过查看所有数据库接口获取数据库信息。 - type为其他类型的时候，需要通过JDBC方式连上集群，查询数据库信息。默认值为空。

        :return: The database of this ScriptInfo.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ScriptInfo.

        执行SQL语句所关联的数据库，当type参数值为DLISQL、SparkSQL、HiveSQL、DWSSQL、PRESTO、ClickHouseSQL、ImpalaSQL、HetuEngineSQL、RDSSQL其中之一时，才支持此参数。 - type为DLISQL时，可以通过查看所有数据库接口获取数据库信息。 - type为其他类型的时候，需要通过JDBC方式连上集群，查询数据库信息。默认值为空。

        :param database: The database of this ScriptInfo.
        :type database: str
        """
        self._database = database

    @property
    def queue_name(self):
        r"""Gets the queue_name of this ScriptInfo.

        DLI资源队列名称，当type参数值为DLISQL时，才支持此参数。可以通过查询队列列表接口获取队列信息。默认值为空。

        :return: The queue_name of this ScriptInfo.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this ScriptInfo.

        DLI资源队列名称，当type参数值为DLISQL时，才支持此参数。可以通过查询队列列表接口获取队列信息。默认值为空。

        :param queue_name: The queue_name of this ScriptInfo.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def configuration(self):
        r"""Gets the configuration of this ScriptInfo.

        用户定义适用于此作业的配置参数，当type参数值为DLISQL时存在。当前支持的配置项列表请参考DLI的conf参数说明。默认值为空。

        :return: The configuration of this ScriptInfo.
        :rtype: object
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        r"""Sets the configuration of this ScriptInfo.

        用户定义适用于此作业的配置参数，当type参数值为DLISQL时存在。当前支持的配置项列表请参考DLI的conf参数说明。默认值为空。

        :param configuration: The configuration of this ScriptInfo.
        :type configuration: object
        """
        self._configuration = configuration

    @property
    def description(self):
        r"""Gets the description of this ScriptInfo.

        描述，长度不能超过255个字符。

        :return: The description of this ScriptInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ScriptInfo.

        描述，长度不能超过255个字符。

        :param description: The description of this ScriptInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ScriptInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
