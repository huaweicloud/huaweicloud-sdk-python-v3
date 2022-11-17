# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatasourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'datasource_type': 'str',
        'sort_field': 'str',
        'sort_type': 'str',
        'name': 'str',
        'app_id': 'str',
        'custom_plugin_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'datasource_type': 'datasource_type',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'name': 'name',
        'app_id': 'app_id',
        'custom_plugin_id': 'custom_plugin_id'
    }

    def __init__(self, instance_id=None, limit=None, offset=None, datasource_type=None, sort_field=None, sort_type=None, name=None, app_id=None, custom_plugin_id=None):
        """ListDatasourcesRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param limit: 每页显示条目数量，最大数量999，超过999后只返回999
        :type limit: int
        :param offset: 分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param datasource_type: 数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS
        :type datasource_type: str
        :param sort_field: 排序字段（CREATED_DATE）
        :type sort_field: str
        :param sort_type: 查询数据源排序的类型，增序还是降序，可为空
        :type sort_type: str
        :param name: 数据源名称,支持模糊匹配
        :type name: str
        :param app_id: 集成应用ID
        :type app_id: str
        :param custom_plugin_id: 连接器ID
        :type custom_plugin_id: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._offset = None
        self._datasource_type = None
        self._sort_field = None
        self._sort_type = None
        self._name = None
        self._app_id = None
        self._custom_plugin_id = None
        self.discriminator = None

        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if datasource_type is not None:
            self.datasource_type = datasource_type
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if name is not None:
            self.name = name
        if app_id is not None:
            self.app_id = app_id
        if custom_plugin_id is not None:
            self.custom_plugin_id = custom_plugin_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDatasourcesRequest.

        实例ID

        :return: The instance_id of this ListDatasourcesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDatasourcesRequest.

        实例ID

        :param instance_id: The instance_id of this ListDatasourcesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListDatasourcesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :return: The limit of this ListDatasourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDatasourcesRequest.

        每页显示条目数量，最大数量999，超过999后只返回999

        :param limit: The limit of this ListDatasourcesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListDatasourcesRequest.

        分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListDatasourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDatasourcesRequest.

        分页查询，分页的偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListDatasourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def datasource_type(self):
        """Gets the datasource_type of this ListDatasourcesRequest.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :return: The datasource_type of this ListDatasourcesRequest.
        :rtype: str
        """
        return self._datasource_type

    @datasource_type.setter
    def datasource_type(self, datasource_type):
        """Sets the datasource_type of this ListDatasourcesRequest.

        数据源类型 - DWS - MYSQL - KAFKA - API - OBS - SAP - MRSHBASE - MRSHDFS - MRSHIVE - WEBSOCKET - SQLSERVER - ORACLE - POSTGRESQL - REDIS - MONGODB - DIS - HL7 - RABBITMQ - SNMP - IBMMQ - CUSTOMIZED (自定义类型) - ACTIVEMQ - ARTEMISMQ - FTP - HIVE - HANA - FIKAFKA - MRSKAFKA - FIHDFS - FIHIVE - GAUSS200 - GAUSS100 - LDAP - DB2 - TAURUS

        :param datasource_type: The datasource_type of this ListDatasourcesRequest.
        :type datasource_type: str
        """
        self._datasource_type = datasource_type

    @property
    def sort_field(self):
        """Gets the sort_field of this ListDatasourcesRequest.

        排序字段（CREATED_DATE）

        :return: The sort_field of this ListDatasourcesRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        """Sets the sort_field of this ListDatasourcesRequest.

        排序字段（CREATED_DATE）

        :param sort_field: The sort_field of this ListDatasourcesRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        """Gets the sort_type of this ListDatasourcesRequest.

        查询数据源排序的类型，增序还是降序，可为空

        :return: The sort_type of this ListDatasourcesRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        """Sets the sort_type of this ListDatasourcesRequest.

        查询数据源排序的类型，增序还是降序，可为空

        :param sort_type: The sort_type of this ListDatasourcesRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def name(self):
        """Gets the name of this ListDatasourcesRequest.

        数据源名称,支持模糊匹配

        :return: The name of this ListDatasourcesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDatasourcesRequest.

        数据源名称,支持模糊匹配

        :param name: The name of this ListDatasourcesRequest.
        :type name: str
        """
        self._name = name

    @property
    def app_id(self):
        """Gets the app_id of this ListDatasourcesRequest.

        集成应用ID

        :return: The app_id of this ListDatasourcesRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListDatasourcesRequest.

        集成应用ID

        :param app_id: The app_id of this ListDatasourcesRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def custom_plugin_id(self):
        """Gets the custom_plugin_id of this ListDatasourcesRequest.

        连接器ID

        :return: The custom_plugin_id of this ListDatasourcesRequest.
        :rtype: str
        """
        return self._custom_plugin_id

    @custom_plugin_id.setter
    def custom_plugin_id(self, custom_plugin_id):
        """Sets the custom_plugin_id of this ListDatasourcesRequest.

        连接器ID

        :param custom_plugin_id: The custom_plugin_id of this ListDatasourcesRequest.
        :type custom_plugin_id: str
        """
        self._custom_plugin_id = custom_plugin_id

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
        if not isinstance(other, ListDatasourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
