# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSimPoolsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pool_name': 'str',
        'limit': 'int',
        'offset': 'int',
        'billing_cycle': 'str',
        'all_billing_cycle': 'bool',
        'status': 'list[int]'
    }

    attribute_map = {
        'pool_name': 'pool_name',
        'limit': 'limit',
        'offset': 'offset',
        'billing_cycle': 'billing_cycle',
        'all_billing_cycle': 'all_billing_cycle',
        'status': 'status'
    }

    def __init__(self, pool_name=None, limit=None, offset=None, billing_cycle=None, all_billing_cycle=None, status=None):
        r"""ListSimPoolsRequest

        The model defined in huaweicloud sdk

        :param pool_name: 流量池名称
        :type pool_name: str
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数
        :type limit: int
        :param offset: 分页查询时的页码数，默认值为1，取值范围为1-1000000的整数
        :type offset: int
        :param billing_cycle: 账期，例如：2021-04
        :type billing_cycle: str
        :param all_billing_cycle: 是否查询近六个月账期标识
        :type all_billing_cycle: bool
        :param status: 流量池状态
        :type status: list[int]
        """
        
        

        self._pool_name = None
        self._limit = None
        self._offset = None
        self._billing_cycle = None
        self._all_billing_cycle = None
        self._status = None
        self.discriminator = None

        if pool_name is not None:
            self.pool_name = pool_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if billing_cycle is not None:
            self.billing_cycle = billing_cycle
        if all_billing_cycle is not None:
            self.all_billing_cycle = all_billing_cycle
        if status is not None:
            self.status = status

    @property
    def pool_name(self):
        r"""Gets the pool_name of this ListSimPoolsRequest.

        流量池名称

        :return: The pool_name of this ListSimPoolsRequest.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this ListSimPoolsRequest.

        流量池名称

        :param pool_name: The pool_name of this ListSimPoolsRequest.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def limit(self):
        r"""Gets the limit of this ListSimPoolsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :return: The limit of this ListSimPoolsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSimPoolsRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为10-500的整数

        :param limit: The limit of this ListSimPoolsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSimPoolsRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :return: The offset of this ListSimPoolsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSimPoolsRequest.

        分页查询时的页码数，默认值为1，取值范围为1-1000000的整数

        :param offset: The offset of this ListSimPoolsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def billing_cycle(self):
        r"""Gets the billing_cycle of this ListSimPoolsRequest.

        账期，例如：2021-04

        :return: The billing_cycle of this ListSimPoolsRequest.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        r"""Sets the billing_cycle of this ListSimPoolsRequest.

        账期，例如：2021-04

        :param billing_cycle: The billing_cycle of this ListSimPoolsRequest.
        :type billing_cycle: str
        """
        self._billing_cycle = billing_cycle

    @property
    def all_billing_cycle(self):
        r"""Gets the all_billing_cycle of this ListSimPoolsRequest.

        是否查询近六个月账期标识

        :return: The all_billing_cycle of this ListSimPoolsRequest.
        :rtype: bool
        """
        return self._all_billing_cycle

    @all_billing_cycle.setter
    def all_billing_cycle(self, all_billing_cycle):
        r"""Sets the all_billing_cycle of this ListSimPoolsRequest.

        是否查询近六个月账期标识

        :param all_billing_cycle: The all_billing_cycle of this ListSimPoolsRequest.
        :type all_billing_cycle: bool
        """
        self._all_billing_cycle = all_billing_cycle

    @property
    def status(self):
        r"""Gets the status of this ListSimPoolsRequest.

        流量池状态

        :return: The status of this ListSimPoolsRequest.
        :rtype: list[int]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSimPoolsRequest.

        流量池状态

        :param status: The status of this ListSimPoolsRequest.
        :type status: list[int]
        """
        self._status = status

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
        if not isinstance(other, ListSimPoolsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
