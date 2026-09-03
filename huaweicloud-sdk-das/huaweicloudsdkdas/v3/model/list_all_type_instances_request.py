# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllTypeInstancesRequest:

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
        'cur_page': 'int',
        'per_page': 'int',
        'network_type': 'str',
        'engine_type': 'str',
        'id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cur_page': 'cur_page',
        'per_page': 'per_page',
        'network_type': 'network_type',
        'engine_type': 'engine_type',
        'id': 'id'
    }

    def __init__(self, name=None, cur_page=None, per_page=None, network_type=None, engine_type=None, id=None):
        r"""ListAllTypeInstancesRequest

        The model defined in huaweicloud sdk

        :param name: 实例名称
        :type name: str
        :param cur_page: 页码
        :type cur_page: int
        :param per_page: 每页记录数
        :type per_page: int
        :param network_type: 数据库来源类型
        :type network_type: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param id: 实例ID
        :type id: str
        """
        
        

        self._name = None
        self._cur_page = None
        self._per_page = None
        self._network_type = None
        self._engine_type = None
        self._id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cur_page is not None:
            self.cur_page = cur_page
        if per_page is not None:
            self.per_page = per_page
        if network_type is not None:
            self.network_type = network_type
        if engine_type is not None:
            self.engine_type = engine_type
        if id is not None:
            self.id = id

    @property
    def name(self):
        r"""Gets the name of this ListAllTypeInstancesRequest.

        实例名称

        :return: The name of this ListAllTypeInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAllTypeInstancesRequest.

        实例名称

        :param name: The name of this ListAllTypeInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def cur_page(self):
        r"""Gets the cur_page of this ListAllTypeInstancesRequest.

        页码

        :return: The cur_page of this ListAllTypeInstancesRequest.
        :rtype: int
        """
        return self._cur_page

    @cur_page.setter
    def cur_page(self, cur_page):
        r"""Sets the cur_page of this ListAllTypeInstancesRequest.

        页码

        :param cur_page: The cur_page of this ListAllTypeInstancesRequest.
        :type cur_page: int
        """
        self._cur_page = cur_page

    @property
    def per_page(self):
        r"""Gets the per_page of this ListAllTypeInstancesRequest.

        每页记录数

        :return: The per_page of this ListAllTypeInstancesRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ListAllTypeInstancesRequest.

        每页记录数

        :param per_page: The per_page of this ListAllTypeInstancesRequest.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def network_type(self):
        r"""Gets the network_type of this ListAllTypeInstancesRequest.

        数据库来源类型

        :return: The network_type of this ListAllTypeInstancesRequest.
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        r"""Sets the network_type of this ListAllTypeInstancesRequest.

        数据库来源类型

        :param network_type: The network_type of this ListAllTypeInstancesRequest.
        :type network_type: str
        """
        self._network_type = network_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ListAllTypeInstancesRequest.

        数据库引擎类型

        :return: The engine_type of this ListAllTypeInstancesRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ListAllTypeInstancesRequest.

        数据库引擎类型

        :param engine_type: The engine_type of this ListAllTypeInstancesRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def id(self):
        r"""Gets the id of this ListAllTypeInstancesRequest.

        实例ID

        :return: The id of this ListAllTypeInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListAllTypeInstancesRequest.

        实例ID

        :param id: The id of this ListAllTypeInstancesRequest.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, ListAllTypeInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
