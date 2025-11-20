# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateLogicDbOpenReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_nodes': 'list[DataNode]',
        'switch_route_begin_time': 'str',
        'switch_route_end_time': 'str',
        'new_shard_number': 'str',
        'is_exclusive': 'bool'
    }

    attribute_map = {
        'data_nodes': 'data_nodes',
        'switch_route_begin_time': 'switch_route_begin_time',
        'switch_route_end_time': 'switch_route_end_time',
        'new_shard_number': 'new_shard_number',
        'is_exclusive': 'is_exclusive'
    }

    def __init__(self, data_nodes=None, switch_route_begin_time=None, switch_route_end_time=None, new_shard_number=None, is_exclusive=None):
        r"""MigrateLogicDbOpenReq

        The model defined in huaweicloud sdk

        :param data_nodes: 关联的后端DN信息。
        :type data_nodes: list[:class:`huaweicloudsdkddm.v1.DataNode`]
        :param switch_route_begin_time: 路由切换开始时间。
        :type switch_route_begin_time: str
        :param switch_route_end_time: 路由切换结束时间。
        :type switch_route_end_time: str
        :param new_shard_number: 新分片数。
        :type new_shard_number: str
        :param is_exclusive: 是否独占。
        :type is_exclusive: bool
        """
        
        

        self._data_nodes = None
        self._switch_route_begin_time = None
        self._switch_route_end_time = None
        self._new_shard_number = None
        self._is_exclusive = None
        self.discriminator = None

        if data_nodes is not None:
            self.data_nodes = data_nodes
        if switch_route_begin_time is not None:
            self.switch_route_begin_time = switch_route_begin_time
        if switch_route_end_time is not None:
            self.switch_route_end_time = switch_route_end_time
        if new_shard_number is not None:
            self.new_shard_number = new_shard_number
        if is_exclusive is not None:
            self.is_exclusive = is_exclusive

    @property
    def data_nodes(self):
        r"""Gets the data_nodes of this MigrateLogicDbOpenReq.

        关联的后端DN信息。

        :return: The data_nodes of this MigrateLogicDbOpenReq.
        :rtype: list[:class:`huaweicloudsdkddm.v1.DataNode`]
        """
        return self._data_nodes

    @data_nodes.setter
    def data_nodes(self, data_nodes):
        r"""Sets the data_nodes of this MigrateLogicDbOpenReq.

        关联的后端DN信息。

        :param data_nodes: The data_nodes of this MigrateLogicDbOpenReq.
        :type data_nodes: list[:class:`huaweicloudsdkddm.v1.DataNode`]
        """
        self._data_nodes = data_nodes

    @property
    def switch_route_begin_time(self):
        r"""Gets the switch_route_begin_time of this MigrateLogicDbOpenReq.

        路由切换开始时间。

        :return: The switch_route_begin_time of this MigrateLogicDbOpenReq.
        :rtype: str
        """
        return self._switch_route_begin_time

    @switch_route_begin_time.setter
    def switch_route_begin_time(self, switch_route_begin_time):
        r"""Sets the switch_route_begin_time of this MigrateLogicDbOpenReq.

        路由切换开始时间。

        :param switch_route_begin_time: The switch_route_begin_time of this MigrateLogicDbOpenReq.
        :type switch_route_begin_time: str
        """
        self._switch_route_begin_time = switch_route_begin_time

    @property
    def switch_route_end_time(self):
        r"""Gets the switch_route_end_time of this MigrateLogicDbOpenReq.

        路由切换结束时间。

        :return: The switch_route_end_time of this MigrateLogicDbOpenReq.
        :rtype: str
        """
        return self._switch_route_end_time

    @switch_route_end_time.setter
    def switch_route_end_time(self, switch_route_end_time):
        r"""Sets the switch_route_end_time of this MigrateLogicDbOpenReq.

        路由切换结束时间。

        :param switch_route_end_time: The switch_route_end_time of this MigrateLogicDbOpenReq.
        :type switch_route_end_time: str
        """
        self._switch_route_end_time = switch_route_end_time

    @property
    def new_shard_number(self):
        r"""Gets the new_shard_number of this MigrateLogicDbOpenReq.

        新分片数。

        :return: The new_shard_number of this MigrateLogicDbOpenReq.
        :rtype: str
        """
        return self._new_shard_number

    @new_shard_number.setter
    def new_shard_number(self, new_shard_number):
        r"""Sets the new_shard_number of this MigrateLogicDbOpenReq.

        新分片数。

        :param new_shard_number: The new_shard_number of this MigrateLogicDbOpenReq.
        :type new_shard_number: str
        """
        self._new_shard_number = new_shard_number

    @property
    def is_exclusive(self):
        r"""Gets the is_exclusive of this MigrateLogicDbOpenReq.

        是否独占。

        :return: The is_exclusive of this MigrateLogicDbOpenReq.
        :rtype: bool
        """
        return self._is_exclusive

    @is_exclusive.setter
    def is_exclusive(self, is_exclusive):
        r"""Sets the is_exclusive of this MigrateLogicDbOpenReq.

        是否独占。

        :param is_exclusive: The is_exclusive of this MigrateLogicDbOpenReq.
        :type is_exclusive: bool
        """
        self._is_exclusive = is_exclusive

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
        if not isinstance(other, MigrateLogicDbOpenReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
