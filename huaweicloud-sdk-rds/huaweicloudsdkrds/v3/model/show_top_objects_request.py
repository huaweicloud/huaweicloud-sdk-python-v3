# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopObjectsRequest:

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
        'top': 'int',
        'database_name': 'str',
        'order': 'str',
        'x_language': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'top': 'top',
        'database_name': 'database_name',
        'order': 'order',
        'x_language': 'X-Language',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, top=None, database_name=None, order=None, x_language=None, offset=None, limit=None):
        r"""ShowTopObjectsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param top: top行数
        :type top: int
        :param database_name: 数据库名
        :type database_name: str
        :param order: 排序规则
        :type order: str
        :param x_language: 语言
        :type x_language: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为1000，不能为负数，最小值为1，最大值为1000。
        :type limit: int
        """
        
        

        self._instance_id = None
        self._top = None
        self._database_name = None
        self._order = None
        self._x_language = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if top is not None:
            self.top = top
        if database_name is not None:
            self.database_name = database_name
        if order is not None:
            self.order = order
        if x_language is not None:
            self.x_language = x_language
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowTopObjectsRequest.

        实例ID。

        :return: The instance_id of this ShowTopObjectsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowTopObjectsRequest.

        实例ID。

        :param instance_id: The instance_id of this ShowTopObjectsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def top(self):
        r"""Gets the top of this ShowTopObjectsRequest.

        top行数

        :return: The top of this ShowTopObjectsRequest.
        :rtype: int
        """
        return self._top

    @top.setter
    def top(self, top):
        r"""Sets the top of this ShowTopObjectsRequest.

        top行数

        :param top: The top of this ShowTopObjectsRequest.
        :type top: int
        """
        self._top = top

    @property
    def database_name(self):
        r"""Gets the database_name of this ShowTopObjectsRequest.

        数据库名

        :return: The database_name of this ShowTopObjectsRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ShowTopObjectsRequest.

        数据库名

        :param database_name: The database_name of this ShowTopObjectsRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def order(self):
        r"""Gets the order of this ShowTopObjectsRequest.

        排序规则

        :return: The order of this ShowTopObjectsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ShowTopObjectsRequest.

        排序规则

        :param order: The order of this ShowTopObjectsRequest.
        :type order: str
        """
        self._order = order

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowTopObjectsRequest.

        语言

        :return: The x_language of this ShowTopObjectsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowTopObjectsRequest.

        语言

        :param x_language: The x_language of this ShowTopObjectsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def offset(self):
        r"""Gets the offset of this ShowTopObjectsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this ShowTopObjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowTopObjectsRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this ShowTopObjectsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowTopObjectsRequest.

        查询记录数。默认为1000，不能为负数，最小值为1，最大值为1000。

        :return: The limit of this ShowTopObjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowTopObjectsRequest.

        查询记录数。默认为1000，不能为负数，最小值为1，最大值为1000。

        :param limit: The limit of this ShowTopObjectsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowTopObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
