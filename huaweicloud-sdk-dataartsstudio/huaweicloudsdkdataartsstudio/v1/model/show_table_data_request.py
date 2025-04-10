# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTableDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'guid': 'str',
        'data_connection_id': 'str',
        'source_type': 'str',
        'database': 'str',
        'schema': 'str',
        'table': 'str',
        'queue': 'str'
    }

    attribute_map = {
        'instance': 'instance',
        'guid': 'guid',
        'data_connection_id': 'data_connection_id',
        'source_type': 'source_type',
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'queue': 'queue'
    }

    def __init__(self, instance=None, guid=None, data_connection_id=None, source_type=None, database=None, schema=None, table=None, queue=None):
        r"""ShowTableDataRequest

        The model defined in huaweicloud sdk

        :param instance: 实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type instance: str
        :param guid: 资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。
        :type guid: str
        :param data_connection_id: 数据连接id。
        :type data_connection_id: str
        :param source_type: 数据源类型。
        :type source_type: str
        :param database: db名称。
        :type database: str
        :param schema: schema名称。
        :type schema: str
        :param table: table名称。
        :type table: str
        :param queue: 队列名称。
        :type queue: str
        """
        
        

        self._instance = None
        self._guid = None
        self._data_connection_id = None
        self._source_type = None
        self._database = None
        self._schema = None
        self._table = None
        self._queue = None
        self.discriminator = None

        self.instance = instance
        self.guid = guid
        if data_connection_id is not None:
            self.data_connection_id = data_connection_id
        if source_type is not None:
            self.source_type = source_type
        if database is not None:
            self.database = database
        if schema is not None:
            self.schema = schema
        if table is not None:
            self.table = table
        if queue is not None:
            self.queue = queue

    @property
    def instance(self):
        r"""Gets the instance of this ShowTableDataRequest.

        实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The instance of this ShowTableDataRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this ShowTableDataRequest.

        实例ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param instance: The instance of this ShowTableDataRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def guid(self):
        r"""Gets the guid of this ShowTableDataRequest.

        资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。

        :return: The guid of this ShowTableDataRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this ShowTableDataRequest.

        资产guid，获取方法请参见[数据资产guid](dataartsstudio_02_0351.xml)。

        :param guid: The guid of this ShowTableDataRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def data_connection_id(self):
        r"""Gets the data_connection_id of this ShowTableDataRequest.

        数据连接id。

        :return: The data_connection_id of this ShowTableDataRequest.
        :rtype: str
        """
        return self._data_connection_id

    @data_connection_id.setter
    def data_connection_id(self, data_connection_id):
        r"""Sets the data_connection_id of this ShowTableDataRequest.

        数据连接id。

        :param data_connection_id: The data_connection_id of this ShowTableDataRequest.
        :type data_connection_id: str
        """
        self._data_connection_id = data_connection_id

    @property
    def source_type(self):
        r"""Gets the source_type of this ShowTableDataRequest.

        数据源类型。

        :return: The source_type of this ShowTableDataRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ShowTableDataRequest.

        数据源类型。

        :param source_type: The source_type of this ShowTableDataRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def database(self):
        r"""Gets the database of this ShowTableDataRequest.

        db名称。

        :return: The database of this ShowTableDataRequest.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        r"""Sets the database of this ShowTableDataRequest.

        db名称。

        :param database: The database of this ShowTableDataRequest.
        :type database: str
        """
        self._database = database

    @property
    def schema(self):
        r"""Gets the schema of this ShowTableDataRequest.

        schema名称。

        :return: The schema of this ShowTableDataRequest.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this ShowTableDataRequest.

        schema名称。

        :param schema: The schema of this ShowTableDataRequest.
        :type schema: str
        """
        self._schema = schema

    @property
    def table(self):
        r"""Gets the table of this ShowTableDataRequest.

        table名称。

        :return: The table of this ShowTableDataRequest.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        r"""Sets the table of this ShowTableDataRequest.

        table名称。

        :param table: The table of this ShowTableDataRequest.
        :type table: str
        """
        self._table = table

    @property
    def queue(self):
        r"""Gets the queue of this ShowTableDataRequest.

        队列名称。

        :return: The queue of this ShowTableDataRequest.
        :rtype: str
        """
        return self._queue

    @queue.setter
    def queue(self, queue):
        r"""Sets the queue of this ShowTableDataRequest.

        队列名称。

        :param queue: The queue of this ShowTableDataRequest.
        :type queue: str
        """
        self._queue = queue

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
        if not isinstance(other, ShowTableDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
