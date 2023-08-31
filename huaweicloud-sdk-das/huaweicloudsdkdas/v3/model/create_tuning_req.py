# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTuningReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'database_name': 'str',
        'schema_name': 'str',
        'sql_script': 'str',
        'node_type': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'database_name': 'database_name',
        'schema_name': 'schema_name',
        'sql_script': 'sql_script',
        'node_type': 'node_type',
        'node_id': 'node_id'
    }

    def __init__(self, database_name=None, schema_name=None, sql_script=None, node_type=None, node_id=None):
        """CreateTuningReq

        The model defined in huaweicloud sdk

        :param database_name: 数据库名称
        :type database_name: str
        :param schema_name: schema名称
        :type schema_name: str
        :param sql_script: sql脚本
        :type sql_script: str
        :param node_type: 节点类型
        :type node_type: str
        :param node_id: 节点Id
        :type node_id: str
        """
        
        

        self._database_name = None
        self._schema_name = None
        self._sql_script = None
        self._node_type = None
        self._node_id = None
        self.discriminator = None

        self.database_name = database_name
        if schema_name is not None:
            self.schema_name = schema_name
        self.sql_script = sql_script
        if node_type is not None:
            self.node_type = node_type
        if node_id is not None:
            self.node_id = node_id

    @property
    def database_name(self):
        """Gets the database_name of this CreateTuningReq.

        数据库名称

        :return: The database_name of this CreateTuningReq.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this CreateTuningReq.

        数据库名称

        :param database_name: The database_name of this CreateTuningReq.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def schema_name(self):
        """Gets the schema_name of this CreateTuningReq.

        schema名称

        :return: The schema_name of this CreateTuningReq.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """Sets the schema_name of this CreateTuningReq.

        schema名称

        :param schema_name: The schema_name of this CreateTuningReq.
        :type schema_name: str
        """
        self._schema_name = schema_name

    @property
    def sql_script(self):
        """Gets the sql_script of this CreateTuningReq.

        sql脚本

        :return: The sql_script of this CreateTuningReq.
        :rtype: str
        """
        return self._sql_script

    @sql_script.setter
    def sql_script(self, sql_script):
        """Sets the sql_script of this CreateTuningReq.

        sql脚本

        :param sql_script: The sql_script of this CreateTuningReq.
        :type sql_script: str
        """
        self._sql_script = sql_script

    @property
    def node_type(self):
        """Gets the node_type of this CreateTuningReq.

        节点类型

        :return: The node_type of this CreateTuningReq.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """Sets the node_type of this CreateTuningReq.

        节点类型

        :param node_type: The node_type of this CreateTuningReq.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def node_id(self):
        """Gets the node_id of this CreateTuningReq.

        节点Id

        :return: The node_id of this CreateTuningReq.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this CreateTuningReq.

        节点Id

        :param node_id: The node_id of this CreateTuningReq.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, CreateTuningReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
