# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConnectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'condition': 'str',
        'perpage': 'str',
        'curpage': 'str',
        'network_type': 'str',
        'datastore_type': 'str',
        'connection_type': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'perpage': 'perpage',
        'curpage': 'curpage',
        'network_type': 'network_type',
        'datastore_type': 'datastore_type',
        'connection_type': 'connection_type',
        'instance_id': 'instance_id'
    }

    def __init__(self, condition=None, perpage=None, curpage=None, network_type=None, datastore_type=None, connection_type=None, instance_id=None):
        r"""ListConnectionRequest

        The model defined in huaweicloud sdk

        :param condition: 数据库实例地址/实例名称/备注等关键字
        :type condition: str
        :param perpage: 每页记录数
        :type perpage: str
        :param curpage: 页码
        :type curpage: str
        :param network_type: 数据库来源类型
        :type network_type: str
        :param datastore_type: 数据库引擎类型
        :type datastore_type: str
        :param connection_type: 连接类型
        :type connection_type: str
        :param instance_id: 实例ID
        :type instance_id: str
        """
        
        

        self._condition = None
        self._perpage = None
        self._curpage = None
        self._network_type = None
        self._datastore_type = None
        self._connection_type = None
        self._instance_id = None
        self.discriminator = None

        if condition is not None:
            self.condition = condition
        if perpage is not None:
            self.perpage = perpage
        if curpage is not None:
            self.curpage = curpage
        if network_type is not None:
            self.network_type = network_type
        if datastore_type is not None:
            self.datastore_type = datastore_type
        if connection_type is not None:
            self.connection_type = connection_type
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def condition(self):
        r"""Gets the condition of this ListConnectionRequest.

        数据库实例地址/实例名称/备注等关键字

        :return: The condition of this ListConnectionRequest.
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this ListConnectionRequest.

        数据库实例地址/实例名称/备注等关键字

        :param condition: The condition of this ListConnectionRequest.
        :type condition: str
        """
        self._condition = condition

    @property
    def perpage(self):
        r"""Gets the perpage of this ListConnectionRequest.

        每页记录数

        :return: The perpage of this ListConnectionRequest.
        :rtype: str
        """
        return self._perpage

    @perpage.setter
    def perpage(self, perpage):
        r"""Sets the perpage of this ListConnectionRequest.

        每页记录数

        :param perpage: The perpage of this ListConnectionRequest.
        :type perpage: str
        """
        self._perpage = perpage

    @property
    def curpage(self):
        r"""Gets the curpage of this ListConnectionRequest.

        页码

        :return: The curpage of this ListConnectionRequest.
        :rtype: str
        """
        return self._curpage

    @curpage.setter
    def curpage(self, curpage):
        r"""Sets the curpage of this ListConnectionRequest.

        页码

        :param curpage: The curpage of this ListConnectionRequest.
        :type curpage: str
        """
        self._curpage = curpage

    @property
    def network_type(self):
        r"""Gets the network_type of this ListConnectionRequest.

        数据库来源类型

        :return: The network_type of this ListConnectionRequest.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ListConnectionRequest.

        数据库来源类型

        :param network_type: The network_type of this ListConnectionRequest.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def datastore_type(self):
        r"""Gets the datastore_type of this ListConnectionRequest.

        数据库引擎类型

        :return: The datastore_type of this ListConnectionRequest.
        :rtype: str
        """
        return self._datastore_type

    @datastore_type.setter
    def datastore_type(self, datastore_type):
        r"""Sets the datastore_type of this ListConnectionRequest.

        数据库引擎类型

        :param datastore_type: The datastore_type of this ListConnectionRequest.
        :type datastore_type: str
        """
        self._datastore_type = datastore_type

    @property
    def connection_type(self):
        r"""Gets the connection_type of this ListConnectionRequest.

        连接类型

        :return: The connection_type of this ListConnectionRequest.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this ListConnectionRequest.

        连接类型

        :param connection_type: The connection_type of this ListConnectionRequest.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListConnectionRequest.

        实例ID

        :return: The instance_id of this ListConnectionRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListConnectionRequest.

        实例ID

        :param instance_id: The instance_id of this ListConnectionRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ListConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
