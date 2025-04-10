# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BizDatasourceRelationVO:

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
        'biz_id': 'str',
        'biz_type': 'BizTypeEnum',
        'dw_type': 'str',
        'dw_id': 'str',
        'dw_name': 'str',
        'db_name': 'str',
        'queue_name': 'str',
        'schema': 'str'
    }

    attribute_map = {
        'id': 'id',
        'biz_id': 'biz_id',
        'biz_type': 'biz_type',
        'dw_type': 'dw_type',
        'dw_id': 'dw_id',
        'dw_name': 'dw_name',
        'db_name': 'db_name',
        'queue_name': 'queue_name',
        'schema': 'schema'
    }

    def __init__(self, id=None, biz_id=None, biz_type=None, dw_type=None, dw_id=None, dw_name=None, db_name=None, queue_name=None, schema=None):
        r"""BizDatasourceRelationVO

        The model defined in huaweicloud sdk

        :param id: 编码，ID字符串。
        :type id: str
        :param biz_id: 业务对象信息，ID字符串。
        :type biz_id: str
        :param biz_type: 
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        :param dw_type: 数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。
        :type dw_type: str
        :param dw_id: 数据连接ID。
        :type dw_id: str
        :param dw_name: 数据连接名，只读。
        :type dw_name: str
        :param db_name: 数据库名。
        :type db_name: str
        :param queue_name: dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。
        :type queue_name: str
        :param schema: DWS类型需要。
        :type schema: str
        """
        
        

        self._id = None
        self._biz_id = None
        self._biz_type = None
        self._dw_type = None
        self._dw_id = None
        self._dw_name = None
        self._db_name = None
        self._queue_name = None
        self._schema = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if biz_id is not None:
            self.biz_id = biz_id
        if biz_type is not None:
            self.biz_type = biz_type
        self.dw_type = dw_type
        self.dw_id = dw_id
        if dw_name is not None:
            self.dw_name = dw_name
        if db_name is not None:
            self.db_name = db_name
        if queue_name is not None:
            self.queue_name = queue_name
        if schema is not None:
            self.schema = schema

    @property
    def id(self):
        r"""Gets the id of this BizDatasourceRelationVO.

        编码，ID字符串。

        :return: The id of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BizDatasourceRelationVO.

        编码，ID字符串。

        :param id: The id of this BizDatasourceRelationVO.
        :type id: str
        """
        self._id = id

    @property
    def biz_id(self):
        r"""Gets the biz_id of this BizDatasourceRelationVO.

        业务对象信息，ID字符串。

        :return: The biz_id of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        r"""Sets the biz_id of this BizDatasourceRelationVO.

        业务对象信息，ID字符串。

        :param biz_id: The biz_id of this BizDatasourceRelationVO.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def biz_type(self):
        r"""Gets the biz_type of this BizDatasourceRelationVO.

        :return: The biz_type of this BizDatasourceRelationVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        r"""Sets the biz_type of this BizDatasourceRelationVO.

        :param biz_type: The biz_type of this BizDatasourceRelationVO.
        :type biz_type: :class:`huaweicloudsdkdataartsstudio.v1.BizTypeEnum`
        """
        self._biz_type = biz_type

    @property
    def dw_type(self):
        r"""Gets the dw_type of this BizDatasourceRelationVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :return: The dw_type of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._dw_type

    @dw_type.setter
    def dw_type(self, dw_type):
        r"""Sets the dw_type of this BizDatasourceRelationVO.

        数据连接类型，对应表所在的数仓类型，取值可以为DLI、DWS、MRS_HIVE、POSTGRESQL、MRS_SPARK、CLICKHOUSE、MYSQL、ORACLE和DORIS等。

        :param dw_type: The dw_type of this BizDatasourceRelationVO.
        :type dw_type: str
        """
        self._dw_type = dw_type

    @property
    def dw_id(self):
        r"""Gets the dw_id of this BizDatasourceRelationVO.

        数据连接ID。

        :return: The dw_id of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        r"""Sets the dw_id of this BizDatasourceRelationVO.

        数据连接ID。

        :param dw_id: The dw_id of this BizDatasourceRelationVO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def dw_name(self):
        r"""Gets the dw_name of this BizDatasourceRelationVO.

        数据连接名，只读。

        :return: The dw_name of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._dw_name

    @dw_name.setter
    def dw_name(self, dw_name):
        r"""Sets the dw_name of this BizDatasourceRelationVO.

        数据连接名，只读。

        :param dw_name: The dw_name of this BizDatasourceRelationVO.
        :type dw_name: str
        """
        self._dw_name = dw_name

    @property
    def db_name(self):
        r"""Gets the db_name of this BizDatasourceRelationVO.

        数据库名。

        :return: The db_name of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        r"""Sets the db_name of this BizDatasourceRelationVO.

        数据库名。

        :param db_name: The db_name of this BizDatasourceRelationVO.
        :type db_name: str
        """
        self._db_name = db_name

    @property
    def queue_name(self):
        r"""Gets the queue_name of this BizDatasourceRelationVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :return: The queue_name of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        r"""Sets the queue_name of this BizDatasourceRelationVO.

        dli数据连接执行sql所需的队列，数据连接类型为DLI时必须。

        :param queue_name: The queue_name of this BizDatasourceRelationVO.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def schema(self):
        r"""Gets the schema of this BizDatasourceRelationVO.

        DWS类型需要。

        :return: The schema of this BizDatasourceRelationVO.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        r"""Sets the schema of this BizDatasourceRelationVO.

        DWS类型需要。

        :param schema: The schema of this BizDatasourceRelationVO.
        :type schema: str
        """
        self._schema = schema

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
        if not isinstance(other, BizDatasourceRelationVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
