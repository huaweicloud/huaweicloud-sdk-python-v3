# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackPoolVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'pool_name': 'str',
        'price_plan_name': 'str',
        'price_plan_id': 'str',
        'effective_time': 'datetime',
        'expired_time': 'datetime',
        'billing_cycle': 'str',
        'pool_status': 'int',
        'flow_used': 'float',
        'status_time': 'datetime',
        'quantity': 'int',
        'modify_time': 'datetime',
        'order_id': 'int',
        'activated_sim_quantity': 'int',
        'inactive_sim_quantity': 'int',
        'disassembled_sim_quantity': 'int',
        'order_ids': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pool_name': 'pool_name',
        'price_plan_name': 'price_plan_name',
        'price_plan_id': 'price_plan_id',
        'effective_time': 'effective_time',
        'expired_time': 'expired_time',
        'billing_cycle': 'billing_cycle',
        'pool_status': 'pool_status',
        'flow_used': 'flow_used',
        'status_time': 'status_time',
        'quantity': 'quantity',
        'modify_time': 'modify_time',
        'order_id': 'order_id',
        'activated_sim_quantity': 'activated_sim_quantity',
        'inactive_sim_quantity': 'inactive_sim_quantity',
        'disassembled_sim_quantity': 'disassembled_sim_quantity',
        'order_ids': 'order_ids'
    }

    def __init__(self, id=None, pool_name=None, price_plan_name=None, price_plan_id=None, effective_time=None, expired_time=None, billing_cycle=None, pool_status=None, flow_used=None, status_time=None, quantity=None, modify_time=None, order_id=None, activated_sim_quantity=None, inactive_sim_quantity=None, disassembled_sim_quantity=None, order_ids=None):
        r"""BackPoolVO

        The model defined in huaweicloud sdk

        :param id: 流量池标识
        :type id: int
        :param pool_name: 流量池名称
        :type pool_name: str
        :param price_plan_name: 套餐名称
        :type price_plan_name: str
        :param price_plan_id: 套餐标识
        :type price_plan_id: str
        :param effective_time: 生效时间
        :type effective_time: datetime
        :param expired_time: 失效时间
        :type expired_time: datetime
        :param billing_cycle: 账期
        :type billing_cycle: str
        :param pool_status: 流量池状态: 2-在用,-1-已停用,-2已废弃
        :type pool_status: int
        :param flow_used: 已用流量(查询账期所在月份), 单位MB
        :type flow_used: float
        :param status_time: 状态变更时间
        :type status_time: datetime
        :param quantity: 流量池成员数量
        :type quantity: int
        :param modify_time: 更新时间
        :type modify_time: datetime
        :param order_id: 批次号
        :type order_id: int
        :param activated_sim_quantity: 已激活成员数量
        :type activated_sim_quantity: int
        :param inactive_sim_quantity: 未激活成员数量
        :type inactive_sim_quantity: int
        :param disassembled_sim_quantity: 已拆机成员数量
        :type disassembled_sim_quantity: int
        :param order_ids: 组成流量池的批次号列表
        :type order_ids: str
        """
        
        

        self._id = None
        self._pool_name = None
        self._price_plan_name = None
        self._price_plan_id = None
        self._effective_time = None
        self._expired_time = None
        self._billing_cycle = None
        self._pool_status = None
        self._flow_used = None
        self._status_time = None
        self._quantity = None
        self._modify_time = None
        self._order_id = None
        self._activated_sim_quantity = None
        self._inactive_sim_quantity = None
        self._disassembled_sim_quantity = None
        self._order_ids = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if pool_name is not None:
            self.pool_name = pool_name
        if price_plan_name is not None:
            self.price_plan_name = price_plan_name
        if price_plan_id is not None:
            self.price_plan_id = price_plan_id
        if effective_time is not None:
            self.effective_time = effective_time
        if expired_time is not None:
            self.expired_time = expired_time
        if billing_cycle is not None:
            self.billing_cycle = billing_cycle
        if pool_status is not None:
            self.pool_status = pool_status
        if flow_used is not None:
            self.flow_used = flow_used
        if status_time is not None:
            self.status_time = status_time
        if quantity is not None:
            self.quantity = quantity
        if modify_time is not None:
            self.modify_time = modify_time
        if order_id is not None:
            self.order_id = order_id
        if activated_sim_quantity is not None:
            self.activated_sim_quantity = activated_sim_quantity
        if inactive_sim_quantity is not None:
            self.inactive_sim_quantity = inactive_sim_quantity
        if disassembled_sim_quantity is not None:
            self.disassembled_sim_quantity = disassembled_sim_quantity
        if order_ids is not None:
            self.order_ids = order_ids

    @property
    def id(self):
        r"""Gets the id of this BackPoolVO.

        流量池标识

        :return: The id of this BackPoolVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BackPoolVO.

        流量池标识

        :param id: The id of this BackPoolVO.
        :type id: int
        """
        self._id = id

    @property
    def pool_name(self):
        r"""Gets the pool_name of this BackPoolVO.

        流量池名称

        :return: The pool_name of this BackPoolVO.
        :rtype: str
        """
        return self._pool_name

    @pool_name.setter
    def pool_name(self, pool_name):
        r"""Sets the pool_name of this BackPoolVO.

        流量池名称

        :param pool_name: The pool_name of this BackPoolVO.
        :type pool_name: str
        """
        self._pool_name = pool_name

    @property
    def price_plan_name(self):
        r"""Gets the price_plan_name of this BackPoolVO.

        套餐名称

        :return: The price_plan_name of this BackPoolVO.
        :rtype: str
        """
        return self._price_plan_name

    @price_plan_name.setter
    def price_plan_name(self, price_plan_name):
        r"""Sets the price_plan_name of this BackPoolVO.

        套餐名称

        :param price_plan_name: The price_plan_name of this BackPoolVO.
        :type price_plan_name: str
        """
        self._price_plan_name = price_plan_name

    @property
    def price_plan_id(self):
        r"""Gets the price_plan_id of this BackPoolVO.

        套餐标识

        :return: The price_plan_id of this BackPoolVO.
        :rtype: str
        """
        return self._price_plan_id

    @price_plan_id.setter
    def price_plan_id(self, price_plan_id):
        r"""Sets the price_plan_id of this BackPoolVO.

        套餐标识

        :param price_plan_id: The price_plan_id of this BackPoolVO.
        :type price_plan_id: str
        """
        self._price_plan_id = price_plan_id

    @property
    def effective_time(self):
        r"""Gets the effective_time of this BackPoolVO.

        生效时间

        :return: The effective_time of this BackPoolVO.
        :rtype: datetime
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this BackPoolVO.

        生效时间

        :param effective_time: The effective_time of this BackPoolVO.
        :type effective_time: datetime
        """
        self._effective_time = effective_time

    @property
    def expired_time(self):
        r"""Gets the expired_time of this BackPoolVO.

        失效时间

        :return: The expired_time of this BackPoolVO.
        :rtype: datetime
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this BackPoolVO.

        失效时间

        :param expired_time: The expired_time of this BackPoolVO.
        :type expired_time: datetime
        """
        self._expired_time = expired_time

    @property
    def billing_cycle(self):
        r"""Gets the billing_cycle of this BackPoolVO.

        账期

        :return: The billing_cycle of this BackPoolVO.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        r"""Sets the billing_cycle of this BackPoolVO.

        账期

        :param billing_cycle: The billing_cycle of this BackPoolVO.
        :type billing_cycle: str
        """
        self._billing_cycle = billing_cycle

    @property
    def pool_status(self):
        r"""Gets the pool_status of this BackPoolVO.

        流量池状态: 2-在用,-1-已停用,-2已废弃

        :return: The pool_status of this BackPoolVO.
        :rtype: int
        """
        return self._pool_status

    @pool_status.setter
    def pool_status(self, pool_status):
        r"""Sets the pool_status of this BackPoolVO.

        流量池状态: 2-在用,-1-已停用,-2已废弃

        :param pool_status: The pool_status of this BackPoolVO.
        :type pool_status: int
        """
        self._pool_status = pool_status

    @property
    def flow_used(self):
        r"""Gets the flow_used of this BackPoolVO.

        已用流量(查询账期所在月份), 单位MB

        :return: The flow_used of this BackPoolVO.
        :rtype: float
        """
        return self._flow_used

    @flow_used.setter
    def flow_used(self, flow_used):
        r"""Sets the flow_used of this BackPoolVO.

        已用流量(查询账期所在月份), 单位MB

        :param flow_used: The flow_used of this BackPoolVO.
        :type flow_used: float
        """
        self._flow_used = flow_used

    @property
    def status_time(self):
        r"""Gets the status_time of this BackPoolVO.

        状态变更时间

        :return: The status_time of this BackPoolVO.
        :rtype: datetime
        """
        return self._status_time

    @status_time.setter
    def status_time(self, status_time):
        r"""Sets the status_time of this BackPoolVO.

        状态变更时间

        :param status_time: The status_time of this BackPoolVO.
        :type status_time: datetime
        """
        self._status_time = status_time

    @property
    def quantity(self):
        r"""Gets the quantity of this BackPoolVO.

        流量池成员数量

        :return: The quantity of this BackPoolVO.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        r"""Sets the quantity of this BackPoolVO.

        流量池成员数量

        :param quantity: The quantity of this BackPoolVO.
        :type quantity: int
        """
        self._quantity = quantity

    @property
    def modify_time(self):
        r"""Gets the modify_time of this BackPoolVO.

        更新时间

        :return: The modify_time of this BackPoolVO.
        :rtype: datetime
        """
        return self._modify_time

    @modify_time.setter
    def modify_time(self, modify_time):
        r"""Sets the modify_time of this BackPoolVO.

        更新时间

        :param modify_time: The modify_time of this BackPoolVO.
        :type modify_time: datetime
        """
        self._modify_time = modify_time

    @property
    def order_id(self):
        r"""Gets the order_id of this BackPoolVO.

        批次号

        :return: The order_id of this BackPoolVO.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this BackPoolVO.

        批次号

        :param order_id: The order_id of this BackPoolVO.
        :type order_id: int
        """
        self._order_id = order_id

    @property
    def activated_sim_quantity(self):
        r"""Gets the activated_sim_quantity of this BackPoolVO.

        已激活成员数量

        :return: The activated_sim_quantity of this BackPoolVO.
        :rtype: int
        """
        return self._activated_sim_quantity

    @activated_sim_quantity.setter
    def activated_sim_quantity(self, activated_sim_quantity):
        r"""Sets the activated_sim_quantity of this BackPoolVO.

        已激活成员数量

        :param activated_sim_quantity: The activated_sim_quantity of this BackPoolVO.
        :type activated_sim_quantity: int
        """
        self._activated_sim_quantity = activated_sim_quantity

    @property
    def inactive_sim_quantity(self):
        r"""Gets the inactive_sim_quantity of this BackPoolVO.

        未激活成员数量

        :return: The inactive_sim_quantity of this BackPoolVO.
        :rtype: int
        """
        return self._inactive_sim_quantity

    @inactive_sim_quantity.setter
    def inactive_sim_quantity(self, inactive_sim_quantity):
        r"""Sets the inactive_sim_quantity of this BackPoolVO.

        未激活成员数量

        :param inactive_sim_quantity: The inactive_sim_quantity of this BackPoolVO.
        :type inactive_sim_quantity: int
        """
        self._inactive_sim_quantity = inactive_sim_quantity

    @property
    def disassembled_sim_quantity(self):
        r"""Gets the disassembled_sim_quantity of this BackPoolVO.

        已拆机成员数量

        :return: The disassembled_sim_quantity of this BackPoolVO.
        :rtype: int
        """
        return self._disassembled_sim_quantity

    @disassembled_sim_quantity.setter
    def disassembled_sim_quantity(self, disassembled_sim_quantity):
        r"""Sets the disassembled_sim_quantity of this BackPoolVO.

        已拆机成员数量

        :param disassembled_sim_quantity: The disassembled_sim_quantity of this BackPoolVO.
        :type disassembled_sim_quantity: int
        """
        self._disassembled_sim_quantity = disassembled_sim_quantity

    @property
    def order_ids(self):
        r"""Gets the order_ids of this BackPoolVO.

        组成流量池的批次号列表

        :return: The order_ids of this BackPoolVO.
        :rtype: str
        """
        return self._order_ids

    @order_ids.setter
    def order_ids(self, order_ids):
        r"""Sets the order_ids of this BackPoolVO.

        组成流量池的批次号列表

        :param order_ids: The order_ids of this BackPoolVO.
        :type order_ids: str
        """
        self._order_ids = order_ids

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
        if not isinstance(other, BackPoolVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
