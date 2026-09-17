# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopDataRequest:

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
        'end_time': 'int',
        'node_id': 'str',
        'order_by': 'str',
        'order': 'str',
        'keyword': 'str',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'engine_type': 'engine_type',
        'object_type': 'object_type',
        'end_time': 'end_time',
        'node_id': 'node_id',
        'order_by': 'order_by',
        'order': 'order',
        'keyword': 'keyword',
        'page_num': 'page_num',
        'page_size': 'page_size'
    }

    def __init__(self, instance_id=None, engine_type=None, object_type=None, end_time=None, node_id=None, order_by=None, order=None, keyword=None, page_num=None, page_size=None):
        r"""ShowTopDataRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param object_type: 库表对象类型
        :type object_type: str
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        :param node_id: 节点ID
        :type node_id: str
        :param order_by: 排序字段
        :type order_by: str
        :param order: 排序方式
        :type order: str
        :param keyword: 关键字
        :type keyword: str
        :param page_num: 页数
        :type page_num: int
        :param page_size: 页大小
        :type page_size: int
        """
        
        

        self._instance_id = None
        self._engine_type = None
        self._object_type = None
        self._end_time = None
        self._node_id = None
        self._order_by = None
        self._order = None
        self._keyword = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None

        self.instance_id = instance_id
        self.engine_type = engine_type
        self.object_type = object_type
        self.end_time = end_time
        if node_id is not None:
            self.node_id = node_id
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order
        if keyword is not None:
            self.keyword = keyword
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowTopDataRequest.

        实例ID

        :return: The instance_id of this ShowTopDataRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowTopDataRequest.

        实例ID

        :param instance_id: The instance_id of this ShowTopDataRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ShowTopDataRequest.

        数据库引擎类型

        :return: The engine_type of this ShowTopDataRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ShowTopDataRequest.

        数据库引擎类型

        :param engine_type: The engine_type of this ShowTopDataRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def object_type(self):
        r"""Gets the object_type of this ShowTopDataRequest.

        库表对象类型

        :return: The object_type of this ShowTopDataRequest.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ShowTopDataRequest.

        库表对象类型

        :param object_type: The object_type of this ShowTopDataRequest.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTopDataRequest.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this ShowTopDataRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTopDataRequest.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this ShowTopDataRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowTopDataRequest.

        节点ID

        :return: The node_id of this ShowTopDataRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowTopDataRequest.

        节点ID

        :param node_id: The node_id of this ShowTopDataRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def order_by(self):
        r"""Gets the order_by of this ShowTopDataRequest.

        排序字段

        :return: The order_by of this ShowTopDataRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ShowTopDataRequest.

        排序字段

        :param order_by: The order_by of this ShowTopDataRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ShowTopDataRequest.

        排序方式

        :return: The order of this ShowTopDataRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowTopDataRequest.

        排序方式

        :param order: The order of this ShowTopDataRequest.
        :type order: str
        """
        self._order = order

    @property
    def keyword(self):
        r"""Gets the keyword of this ShowTopDataRequest.

        关键字

        :return: The keyword of this ShowTopDataRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ShowTopDataRequest.

        关键字

        :param keyword: The keyword of this ShowTopDataRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowTopDataRequest.

        页数

        :return: The page_num of this ShowTopDataRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowTopDataRequest.

        页数

        :param page_num: The page_num of this ShowTopDataRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowTopDataRequest.

        页大小

        :return: The page_size of this ShowTopDataRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowTopDataRequest.

        页大小

        :param page_size: The page_size of this ShowTopDataRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ShowTopDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
