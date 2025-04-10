# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryDRInfoRequest:

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
        'status': 'str',
        'master_instance_id': 'str',
        'master_region': 'str',
        'slave_instance_id': 'str',
        'slave_region': 'str',
        'create_at_start': 'int',
        'create_at_end': 'int',
        'order': 'str',
        'sort_field': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'master_instance_id': 'master_instance_id',
        'master_region': 'master_region',
        'slave_instance_id': 'slave_instance_id',
        'slave_region': 'slave_region',
        'create_at_start': 'create_at_start',
        'create_at_end': 'create_at_end',
        'order': 'order',
        'sort_field': 'sort_field',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, id=None, status=None, master_instance_id=None, master_region=None, slave_instance_id=None, slave_region=None, create_at_start=None, create_at_end=None, order=None, sort_field=None, offset=None, limit=None):
        r"""QueryDRInfoRequest

        The model defined in huaweicloud sdk

        :param id: 容灾关系id
        :type id: str
        :param status: 容灾搭建状态
        :type status: str
        :param master_instance_id: 灾备实例id
        :type master_instance_id: str
        :param master_region: 主实例region
        :type master_region: str
        :param slave_instance_id: 灾备实例id
        :type slave_instance_id: str
        :param slave_region: 灾备实例region
        :type slave_region: str
        :param create_at_start: 创建起始时间
        :type create_at_start: int
        :param create_at_end: 创建结束时间
        :type create_at_end: int
        :param order: 排序方式。 DESC，降序。 ASC，升序。 默认降序。
        :type order: str
        :param sort_field: 排序字段。 status 容灾搭建状态。 time 容灾搭建时间。 master_region 主实例region。 slave_region 灾备实例region 默认容灾搭建时间。
        :type sort_field: str
        :param offset: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。
        :type offset: int
        :param limit: 查询记录数。默认为10，不能为负数，最小值为1，最大值为100。
        :type limit: int
        """
        
        

        self._id = None
        self._status = None
        self._master_instance_id = None
        self._master_region = None
        self._slave_instance_id = None
        self._slave_region = None
        self._create_at_start = None
        self._create_at_end = None
        self._order = None
        self._sort_field = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if master_instance_id is not None:
            self.master_instance_id = master_instance_id
        if master_region is not None:
            self.master_region = master_region
        if slave_instance_id is not None:
            self.slave_instance_id = slave_instance_id
        if slave_region is not None:
            self.slave_region = slave_region
        if create_at_start is not None:
            self.create_at_start = create_at_start
        if create_at_end is not None:
            self.create_at_end = create_at_end
        if order is not None:
            self.order = order
        if sort_field is not None:
            self.sort_field = sort_field
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        r"""Gets the id of this QueryDRInfoRequest.

        容灾关系id

        :return: The id of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryDRInfoRequest.

        容灾关系id

        :param id: The id of this QueryDRInfoRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this QueryDRInfoRequest.

        容灾搭建状态

        :return: The status of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this QueryDRInfoRequest.

        容灾搭建状态

        :param status: The status of this QueryDRInfoRequest.
        :type status: str
        """
        self._status = status

    @property
    def master_instance_id(self):
        r"""Gets the master_instance_id of this QueryDRInfoRequest.

        灾备实例id

        :return: The master_instance_id of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._master_instance_id

    @master_instance_id.setter
    def master_instance_id(self, master_instance_id):
        r"""Sets the master_instance_id of this QueryDRInfoRequest.

        灾备实例id

        :param master_instance_id: The master_instance_id of this QueryDRInfoRequest.
        :type master_instance_id: str
        """
        self._master_instance_id = master_instance_id

    @property
    def master_region(self):
        r"""Gets the master_region of this QueryDRInfoRequest.

        主实例region

        :return: The master_region of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._master_region

    @master_region.setter
    def master_region(self, master_region):
        r"""Sets the master_region of this QueryDRInfoRequest.

        主实例region

        :param master_region: The master_region of this QueryDRInfoRequest.
        :type master_region: str
        """
        self._master_region = master_region

    @property
    def slave_instance_id(self):
        r"""Gets the slave_instance_id of this QueryDRInfoRequest.

        灾备实例id

        :return: The slave_instance_id of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._slave_instance_id

    @slave_instance_id.setter
    def slave_instance_id(self, slave_instance_id):
        r"""Sets the slave_instance_id of this QueryDRInfoRequest.

        灾备实例id

        :param slave_instance_id: The slave_instance_id of this QueryDRInfoRequest.
        :type slave_instance_id: str
        """
        self._slave_instance_id = slave_instance_id

    @property
    def slave_region(self):
        r"""Gets the slave_region of this QueryDRInfoRequest.

        灾备实例region

        :return: The slave_region of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._slave_region

    @slave_region.setter
    def slave_region(self, slave_region):
        r"""Sets the slave_region of this QueryDRInfoRequest.

        灾备实例region

        :param slave_region: The slave_region of this QueryDRInfoRequest.
        :type slave_region: str
        """
        self._slave_region = slave_region

    @property
    def create_at_start(self):
        r"""Gets the create_at_start of this QueryDRInfoRequest.

        创建起始时间

        :return: The create_at_start of this QueryDRInfoRequest.
        :rtype: int
        """
        return self._create_at_start

    @create_at_start.setter
    def create_at_start(self, create_at_start):
        r"""Sets the create_at_start of this QueryDRInfoRequest.

        创建起始时间

        :param create_at_start: The create_at_start of this QueryDRInfoRequest.
        :type create_at_start: int
        """
        self._create_at_start = create_at_start

    @property
    def create_at_end(self):
        r"""Gets the create_at_end of this QueryDRInfoRequest.

        创建结束时间

        :return: The create_at_end of this QueryDRInfoRequest.
        :rtype: int
        """
        return self._create_at_end

    @create_at_end.setter
    def create_at_end(self, create_at_end):
        r"""Sets the create_at_end of this QueryDRInfoRequest.

        创建结束时间

        :param create_at_end: The create_at_end of this QueryDRInfoRequest.
        :type create_at_end: int
        """
        self._create_at_end = create_at_end

    @property
    def order(self):
        r"""Gets the order of this QueryDRInfoRequest.

        排序方式。 DESC，降序。 ASC，升序。 默认降序。

        :return: The order of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this QueryDRInfoRequest.

        排序方式。 DESC，降序。 ASC，升序。 默认降序。

        :param order: The order of this QueryDRInfoRequest.
        :type order: str
        """
        self._order = order

    @property
    def sort_field(self):
        r"""Gets the sort_field of this QueryDRInfoRequest.

        排序字段。 status 容灾搭建状态。 time 容灾搭建时间。 master_region 主实例region。 slave_region 灾备实例region 默认容灾搭建时间。

        :return: The sort_field of this QueryDRInfoRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this QueryDRInfoRequest.

        排序字段。 status 容灾搭建状态。 time 容灾搭建时间。 master_region 主实例region。 slave_region 灾备实例region 默认容灾搭建时间。

        :param sort_field: The sort_field of this QueryDRInfoRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def offset(self):
        r"""Gets the offset of this QueryDRInfoRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :return: The offset of this QueryDRInfoRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this QueryDRInfoRequest.

        索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。

        :param offset: The offset of this QueryDRInfoRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this QueryDRInfoRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :return: The limit of this QueryDRInfoRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QueryDRInfoRequest.

        查询记录数。默认为10，不能为负数，最小值为1，最大值为100。

        :param limit: The limit of this QueryDRInfoRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, QueryDRInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
