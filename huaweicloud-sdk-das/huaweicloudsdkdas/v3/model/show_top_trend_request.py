# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopTrendRequest:

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
        'engine_type': 'str',
        'object_type': 'str',
        'object_name': 'str',
        'database_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'node_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'engine_type': 'engine_type',
        'object_type': 'object_type',
        'object_name': 'object_name',
        'database_name': 'database_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'node_id': 'node_id'
    }

    def __init__(self, instance_id=None, engine_type=None, object_type=None, object_name=None, database_name=None, start_time=None, end_time=None, node_id=None):
        r"""ShowTopTrendRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param object_type: 库表对象类型
        :type object_type: str
        :param object_name: 库表对象名称
        :type object_name: str
        :param database_name: 库名
        :type database_name: str
        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param node_id: 节点ID
        :type node_id: str
        """
        
        

        self._instance_id = None
        self._engine_type = None
        self._object_type = None
        self._object_name = None
        self._database_name = None
        self._start_time = None
        self._end_time = None
        self._node_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.engine_type = engine_type
        self.object_type = object_type
        self.object_name = object_name
        if database_name is not None:
            self.database_name = database_name
        self.start_time = start_time
        self.end_time = end_time
        if node_id is not None:
            self.node_id = node_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowTopTrendRequest.

        实例ID

        :return: The instance_id of this ShowTopTrendRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowTopTrendRequest.

        实例ID

        :param instance_id: The instance_id of this ShowTopTrendRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowTopTrendRequest.

        数据库引擎类型

        :return: The engine_type of this ShowTopTrendRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowTopTrendRequest.

        数据库引擎类型

        :param engine_type: The engine_type of this ShowTopTrendRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def object_type(self):
        r"""Gets the object_type of this ShowTopTrendRequest.

        库表对象类型

        :return: The object_type of this ShowTopTrendRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ShowTopTrendRequest.

        库表对象类型

        :param object_type: The object_type of this ShowTopTrendRequest.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def object_name(self):
        r"""Gets the object_name of this ShowTopTrendRequest.

        库表对象名称

        :return: The object_name of this ShowTopTrendRequest.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ShowTopTrendRequest.

        库表对象名称

        :param object_name: The object_name of this ShowTopTrendRequest.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowTopTrendRequest.

        库名

        :return: The database_name of this ShowTopTrendRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowTopTrendRequest.

        库名

        :param database_name: The database_name of this ShowTopTrendRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowTopTrendRequest.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this ShowTopTrendRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowTopTrendRequest.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this ShowTopTrendRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTopTrendRequest.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this ShowTopTrendRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTopTrendRequest.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this ShowTopTrendRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowTopTrendRequest.

        节点ID

        :return: The node_id of this ShowTopTrendRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowTopTrendRequest.

        节点ID

        :param node_id: The node_id of this ShowTopTrendRequest.
        :type node_id: str
        """
        self._node_id = node_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowTopTrendRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
