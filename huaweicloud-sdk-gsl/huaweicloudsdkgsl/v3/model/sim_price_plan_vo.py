# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimPricePlanVO:

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
        'account_id': 'str',
        'sim_card_id': 'int',
        'status': 'int',
        'price_plan_id': 'str',
        'cid': 'str',
        'order_id': 'str',
        'create_time': 'datetime',
        'active_time': 'datetime',
        'stop_time': 'datetime',
        'flow_total': 'float',
        'flow_used': 'float',
        'flow_left': 'float',
        'using': 'str',
        'price_plan_name': 'str',
        'description': 'str',
        'package_type': 'int',
        'effect_type': 'int',
        'silent_period_day': 'int',
        'silent_period_unit': 'int',
        'auto_renew': 'int',
        'location_desc': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'sim_card_id': 'sim_card_id',
        'status': 'status',
        'price_plan_id': 'price_plan_id',
        'cid': 'cid',
        'order_id': 'order_id',
        'create_time': 'create_time',
        'active_time': 'active_time',
        'stop_time': 'stop_time',
        'flow_total': 'flow_total',
        'flow_used': 'flow_used',
        'flow_left': 'flow_left',
        'using': 'using',
        'price_plan_name': 'price_plan_name',
        'description': 'description',
        'package_type': 'package_type',
        'effect_type': 'effect_type',
        'silent_period_day': 'silent_period_day',
        'silent_period_unit': 'silent_period_unit',
        'auto_renew': 'auto_renew',
        'location_desc': 'location_desc'
    }

    def __init__(self, id=None, account_id=None, sim_card_id=None, status=None, price_plan_id=None, cid=None, order_id=None, create_time=None, active_time=None, stop_time=None, flow_total=None, flow_used=None, flow_left=None, using=None, price_plan_name=None, description=None, package_type=None, effect_type=None, silent_period_day=None, silent_period_unit=None, auto_renew=None, location_desc=None):
        """SimPricePlanVO

        The model defined in huaweicloud sdk

        :param id: 套餐实例id
        :type id: int
        :param account_id: 账户id
        :type account_id: str
        :param sim_card_id: sim卡id
        :type sim_card_id: int
        :param status: 套餐状态:0 已删除 1 可激活 2 在用 3. 使用完 4. 可激活 5 已停用 6. 启用失败
        :type status: int
        :param price_plan_id: 套餐id
        :type price_plan_id: str
        :param cid: 容器ID:不同类型卡含义如下 iccid(实体卡)，eid（eSIM）cid（vSIM)
        :type cid: str
        :param order_id: 订单id
        :type order_id: str
        :param create_time: 创建时间 例如2020-08-24T07:57:56.000Z
        :type create_time: datetime
        :param active_time: 激活时间 例如2020-10-31T16:00:00.000Z
        :type active_time: datetime
        :param stop_time: 停用时间 2021-10-31T16:00:00.000Z
        :type stop_time: datetime
        :param flow_total: 总流量(MB)
        :type flow_total: float
        :param flow_used: 已使用流量(MB)
        :type flow_used: float
        :param flow_left: 剩余流量(MB)
        :type flow_left: float
        :param using: 是否使用中(0：否 1：是)
        :type using: str
        :param price_plan_name: 套餐名
        :type price_plan_name: str
        :param description: 描述
        :type description: str
        :param package_type: 套餐类型: 0.非自动续费 1.自动续费
        :type package_type: int
        :param effect_type: 生效类型: 1.订购后激活使用时生效 2.订购即时生效 3.订购下个月开始生效 
        :type effect_type: int
        :param silent_period_day: 沉默期
        :type silent_period_day: int
        :param silent_period_unit: 沉默期单位: 1.年 2.月 3.日 
        :type silent_period_unit: int
        :param auto_renew: 自动续订: 0.不自动续订 1.继续续订
        :type auto_renew: int
        :param location_desc: 位置信息:1.  中国 2.  欧洲 3.  大洋洲 4.  非洲5.  亚太
        :type location_desc: str
        """
        
        

        self._id = None
        self._account_id = None
        self._sim_card_id = None
        self._status = None
        self._price_plan_id = None
        self._cid = None
        self._order_id = None
        self._create_time = None
        self._active_time = None
        self._stop_time = None
        self._flow_total = None
        self._flow_used = None
        self._flow_left = None
        self._using = None
        self._price_plan_name = None
        self._description = None
        self._package_type = None
        self._effect_type = None
        self._silent_period_day = None
        self._silent_period_unit = None
        self._auto_renew = None
        self._location_desc = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if status is not None:
            self.status = status
        if price_plan_id is not None:
            self.price_plan_id = price_plan_id
        if cid is not None:
            self.cid = cid
        if order_id is not None:
            self.order_id = order_id
        if create_time is not None:
            self.create_time = create_time
        if active_time is not None:
            self.active_time = active_time
        if stop_time is not None:
            self.stop_time = stop_time
        if flow_total is not None:
            self.flow_total = flow_total
        if flow_used is not None:
            self.flow_used = flow_used
        if flow_left is not None:
            self.flow_left = flow_left
        if using is not None:
            self.using = using
        if price_plan_name is not None:
            self.price_plan_name = price_plan_name
        if description is not None:
            self.description = description
        if package_type is not None:
            self.package_type = package_type
        if effect_type is not None:
            self.effect_type = effect_type
        if silent_period_day is not None:
            self.silent_period_day = silent_period_day
        if silent_period_unit is not None:
            self.silent_period_unit = silent_period_unit
        if auto_renew is not None:
            self.auto_renew = auto_renew
        if location_desc is not None:
            self.location_desc = location_desc

    @property
    def id(self):
        """Gets the id of this SimPricePlanVO.

        套餐实例id

        :return: The id of this SimPricePlanVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimPricePlanVO.

        套餐实例id

        :param id: The id of this SimPricePlanVO.
        :type id: int
        """
        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this SimPricePlanVO.

        账户id

        :return: The account_id of this SimPricePlanVO.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SimPricePlanVO.

        账户id

        :param account_id: The account_id of this SimPricePlanVO.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this SimPricePlanVO.

        sim卡id

        :return: The sim_card_id of this SimPricePlanVO.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this SimPricePlanVO.

        sim卡id

        :param sim_card_id: The sim_card_id of this SimPricePlanVO.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def status(self):
        """Gets the status of this SimPricePlanVO.

        套餐状态:0 已删除 1 可激活 2 在用 3. 使用完 4. 可激活 5 已停用 6. 启用失败

        :return: The status of this SimPricePlanVO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SimPricePlanVO.

        套餐状态:0 已删除 1 可激活 2 在用 3. 使用完 4. 可激活 5 已停用 6. 启用失败

        :param status: The status of this SimPricePlanVO.
        :type status: int
        """
        self._status = status

    @property
    def price_plan_id(self):
        """Gets the price_plan_id of this SimPricePlanVO.

        套餐id

        :return: The price_plan_id of this SimPricePlanVO.
        :rtype: str
        """
        return self._price_plan_id

    @price_plan_id.setter
    def price_plan_id(self, price_plan_id):
        """Sets the price_plan_id of this SimPricePlanVO.

        套餐id

        :param price_plan_id: The price_plan_id of this SimPricePlanVO.
        :type price_plan_id: str
        """
        self._price_plan_id = price_plan_id

    @property
    def cid(self):
        """Gets the cid of this SimPricePlanVO.

        容器ID:不同类型卡含义如下 iccid(实体卡)，eid（eSIM）cid（vSIM)

        :return: The cid of this SimPricePlanVO.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        """Sets the cid of this SimPricePlanVO.

        容器ID:不同类型卡含义如下 iccid(实体卡)，eid（eSIM）cid（vSIM)

        :param cid: The cid of this SimPricePlanVO.
        :type cid: str
        """
        self._cid = cid

    @property
    def order_id(self):
        """Gets the order_id of this SimPricePlanVO.

        订单id

        :return: The order_id of this SimPricePlanVO.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this SimPricePlanVO.

        订单id

        :param order_id: The order_id of this SimPricePlanVO.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def create_time(self):
        """Gets the create_time of this SimPricePlanVO.

        创建时间 例如2020-08-24T07:57:56.000Z

        :return: The create_time of this SimPricePlanVO.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this SimPricePlanVO.

        创建时间 例如2020-08-24T07:57:56.000Z

        :param create_time: The create_time of this SimPricePlanVO.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def active_time(self):
        """Gets the active_time of this SimPricePlanVO.

        激活时间 例如2020-10-31T16:00:00.000Z

        :return: The active_time of this SimPricePlanVO.
        :rtype: datetime
        """
        return self._active_time

    @active_time.setter
    def active_time(self, active_time):
        """Sets the active_time of this SimPricePlanVO.

        激活时间 例如2020-10-31T16:00:00.000Z

        :param active_time: The active_time of this SimPricePlanVO.
        :type active_time: datetime
        """
        self._active_time = active_time

    @property
    def stop_time(self):
        """Gets the stop_time of this SimPricePlanVO.

        停用时间 2021-10-31T16:00:00.000Z

        :return: The stop_time of this SimPricePlanVO.
        :rtype: datetime
        """
        return self._stop_time

    @stop_time.setter
    def stop_time(self, stop_time):
        """Sets the stop_time of this SimPricePlanVO.

        停用时间 2021-10-31T16:00:00.000Z

        :param stop_time: The stop_time of this SimPricePlanVO.
        :type stop_time: datetime
        """
        self._stop_time = stop_time

    @property
    def flow_total(self):
        """Gets the flow_total of this SimPricePlanVO.

        总流量(MB)

        :return: The flow_total of this SimPricePlanVO.
        :rtype: float
        """
        return self._flow_total

    @flow_total.setter
    def flow_total(self, flow_total):
        """Sets the flow_total of this SimPricePlanVO.

        总流量(MB)

        :param flow_total: The flow_total of this SimPricePlanVO.
        :type flow_total: float
        """
        self._flow_total = flow_total

    @property
    def flow_used(self):
        """Gets the flow_used of this SimPricePlanVO.

        已使用流量(MB)

        :return: The flow_used of this SimPricePlanVO.
        :rtype: float
        """
        return self._flow_used

    @flow_used.setter
    def flow_used(self, flow_used):
        """Sets the flow_used of this SimPricePlanVO.

        已使用流量(MB)

        :param flow_used: The flow_used of this SimPricePlanVO.
        :type flow_used: float
        """
        self._flow_used = flow_used

    @property
    def flow_left(self):
        """Gets the flow_left of this SimPricePlanVO.

        剩余流量(MB)

        :return: The flow_left of this SimPricePlanVO.
        :rtype: float
        """
        return self._flow_left

    @flow_left.setter
    def flow_left(self, flow_left):
        """Sets the flow_left of this SimPricePlanVO.

        剩余流量(MB)

        :param flow_left: The flow_left of this SimPricePlanVO.
        :type flow_left: float
        """
        self._flow_left = flow_left

    @property
    def using(self):
        """Gets the using of this SimPricePlanVO.

        是否使用中(0：否 1：是)

        :return: The using of this SimPricePlanVO.
        :rtype: str
        """
        return self._using

    @using.setter
    def using(self, using):
        """Sets the using of this SimPricePlanVO.

        是否使用中(0：否 1：是)

        :param using: The using of this SimPricePlanVO.
        :type using: str
        """
        self._using = using

    @property
    def price_plan_name(self):
        """Gets the price_plan_name of this SimPricePlanVO.

        套餐名

        :return: The price_plan_name of this SimPricePlanVO.
        :rtype: str
        """
        return self._price_plan_name

    @price_plan_name.setter
    def price_plan_name(self, price_plan_name):
        """Sets the price_plan_name of this SimPricePlanVO.

        套餐名

        :param price_plan_name: The price_plan_name of this SimPricePlanVO.
        :type price_plan_name: str
        """
        self._price_plan_name = price_plan_name

    @property
    def description(self):
        """Gets the description of this SimPricePlanVO.

        描述

        :return: The description of this SimPricePlanVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SimPricePlanVO.

        描述

        :param description: The description of this SimPricePlanVO.
        :type description: str
        """
        self._description = description

    @property
    def package_type(self):
        """Gets the package_type of this SimPricePlanVO.

        套餐类型: 0.非自动续费 1.自动续费

        :return: The package_type of this SimPricePlanVO.
        :rtype: int
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """Sets the package_type of this SimPricePlanVO.

        套餐类型: 0.非自动续费 1.自动续费

        :param package_type: The package_type of this SimPricePlanVO.
        :type package_type: int
        """
        self._package_type = package_type

    @property
    def effect_type(self):
        """Gets the effect_type of this SimPricePlanVO.

        生效类型: 1.订购后激活使用时生效 2.订购即时生效 3.订购下个月开始生效 

        :return: The effect_type of this SimPricePlanVO.
        :rtype: int
        """
        return self._effect_type

    @effect_type.setter
    def effect_type(self, effect_type):
        """Sets the effect_type of this SimPricePlanVO.

        生效类型: 1.订购后激活使用时生效 2.订购即时生效 3.订购下个月开始生效 

        :param effect_type: The effect_type of this SimPricePlanVO.
        :type effect_type: int
        """
        self._effect_type = effect_type

    @property
    def silent_period_day(self):
        """Gets the silent_period_day of this SimPricePlanVO.

        沉默期

        :return: The silent_period_day of this SimPricePlanVO.
        :rtype: int
        """
        return self._silent_period_day

    @silent_period_day.setter
    def silent_period_day(self, silent_period_day):
        """Sets the silent_period_day of this SimPricePlanVO.

        沉默期

        :param silent_period_day: The silent_period_day of this SimPricePlanVO.
        :type silent_period_day: int
        """
        self._silent_period_day = silent_period_day

    @property
    def silent_period_unit(self):
        """Gets the silent_period_unit of this SimPricePlanVO.

        沉默期单位: 1.年 2.月 3.日 

        :return: The silent_period_unit of this SimPricePlanVO.
        :rtype: int
        """
        return self._silent_period_unit

    @silent_period_unit.setter
    def silent_period_unit(self, silent_period_unit):
        """Sets the silent_period_unit of this SimPricePlanVO.

        沉默期单位: 1.年 2.月 3.日 

        :param silent_period_unit: The silent_period_unit of this SimPricePlanVO.
        :type silent_period_unit: int
        """
        self._silent_period_unit = silent_period_unit

    @property
    def auto_renew(self):
        """Gets the auto_renew of this SimPricePlanVO.

        自动续订: 0.不自动续订 1.继续续订

        :return: The auto_renew of this SimPricePlanVO.
        :rtype: int
        """
        return self._auto_renew

    @auto_renew.setter
    def auto_renew(self, auto_renew):
        """Sets the auto_renew of this SimPricePlanVO.

        自动续订: 0.不自动续订 1.继续续订

        :param auto_renew: The auto_renew of this SimPricePlanVO.
        :type auto_renew: int
        """
        self._auto_renew = auto_renew

    @property
    def location_desc(self):
        """Gets the location_desc of this SimPricePlanVO.

        位置信息:1.  中国 2.  欧洲 3.  大洋洲 4.  非洲5.  亚太

        :return: The location_desc of this SimPricePlanVO.
        :rtype: str
        """
        return self._location_desc

    @location_desc.setter
    def location_desc(self, location_desc):
        """Sets the location_desc of this SimPricePlanVO.

        位置信息:1.  中国 2.  欧洲 3.  大洋洲 4.  非洲5.  亚太

        :param location_desc: The location_desc of this SimPricePlanVO.
        :type location_desc: str
        """
        self._location_desc = location_desc

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
        if not isinstance(other, SimPricePlanVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
