# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimCardsFlowVO:

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
        'price_plan_id': 'str',
        'price_plan_name': 'str',
        'iccid': 'str',
        'flow_total': 'float',
        'flow_used': 'float',
        'flow_left': 'float'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'account_id',
        'sim_card_id': 'sim_card_id',
        'price_plan_id': 'price_plan_id',
        'price_plan_name': 'price_plan_name',
        'iccid': 'iccid',
        'flow_total': 'flow_total',
        'flow_used': 'flow_used',
        'flow_left': 'flow_left'
    }

    def __init__(self, id=None, account_id=None, sim_card_id=None, price_plan_id=None, price_plan_name=None, iccid=None, flow_total=None, flow_used=None, flow_left=None):
        """SimCardsFlowVO

        The model defined in huaweicloud sdk

        :param id: 套餐实例ID
        :type id: int
        :param account_id: 账户ID
        :type account_id: str
        :param sim_card_id: sim卡ID
        :type sim_card_id: int
        :param price_plan_id: 套餐ID
        :type price_plan_id: str
        :param price_plan_name: 套餐名称
        :type price_plan_name: str
        :param iccid: ICCID
        :type iccid: str
        :param flow_total: 总流量(MB),两位小数
        :type flow_total: float
        :param flow_used: 已使用流量(MB),两位小数
        :type flow_used: float
        :param flow_left: 剩余流量(MB),两位小数
        :type flow_left: float
        """
        
        

        self._id = None
        self._account_id = None
        self._sim_card_id = None
        self._price_plan_id = None
        self._price_plan_name = None
        self._iccid = None
        self._flow_total = None
        self._flow_used = None
        self._flow_left = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if account_id is not None:
            self.account_id = account_id
        if sim_card_id is not None:
            self.sim_card_id = sim_card_id
        if price_plan_id is not None:
            self.price_plan_id = price_plan_id
        if price_plan_name is not None:
            self.price_plan_name = price_plan_name
        if iccid is not None:
            self.iccid = iccid
        if flow_total is not None:
            self.flow_total = flow_total
        if flow_used is not None:
            self.flow_used = flow_used
        if flow_left is not None:
            self.flow_left = flow_left

    @property
    def id(self):
        """Gets the id of this SimCardsFlowVO.

        套餐实例ID

        :return: The id of this SimCardsFlowVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimCardsFlowVO.

        套餐实例ID

        :param id: The id of this SimCardsFlowVO.
        :type id: int
        """
        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this SimCardsFlowVO.

        账户ID

        :return: The account_id of this SimCardsFlowVO.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this SimCardsFlowVO.

        账户ID

        :param account_id: The account_id of this SimCardsFlowVO.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def sim_card_id(self):
        """Gets the sim_card_id of this SimCardsFlowVO.

        sim卡ID

        :return: The sim_card_id of this SimCardsFlowVO.
        :rtype: int
        """
        return self._sim_card_id

    @sim_card_id.setter
    def sim_card_id(self, sim_card_id):
        """Sets the sim_card_id of this SimCardsFlowVO.

        sim卡ID

        :param sim_card_id: The sim_card_id of this SimCardsFlowVO.
        :type sim_card_id: int
        """
        self._sim_card_id = sim_card_id

    @property
    def price_plan_id(self):
        """Gets the price_plan_id of this SimCardsFlowVO.

        套餐ID

        :return: The price_plan_id of this SimCardsFlowVO.
        :rtype: str
        """
        return self._price_plan_id

    @price_plan_id.setter
    def price_plan_id(self, price_plan_id):
        """Sets the price_plan_id of this SimCardsFlowVO.

        套餐ID

        :param price_plan_id: The price_plan_id of this SimCardsFlowVO.
        :type price_plan_id: str
        """
        self._price_plan_id = price_plan_id

    @property
    def price_plan_name(self):
        """Gets the price_plan_name of this SimCardsFlowVO.

        套餐名称

        :return: The price_plan_name of this SimCardsFlowVO.
        :rtype: str
        """
        return self._price_plan_name

    @price_plan_name.setter
    def price_plan_name(self, price_plan_name):
        """Sets the price_plan_name of this SimCardsFlowVO.

        套餐名称

        :param price_plan_name: The price_plan_name of this SimCardsFlowVO.
        :type price_plan_name: str
        """
        self._price_plan_name = price_plan_name

    @property
    def iccid(self):
        """Gets the iccid of this SimCardsFlowVO.

        ICCID

        :return: The iccid of this SimCardsFlowVO.
        :rtype: str
        """
        return self._iccid

    @iccid.setter
    def iccid(self, iccid):
        """Sets the iccid of this SimCardsFlowVO.

        ICCID

        :param iccid: The iccid of this SimCardsFlowVO.
        :type iccid: str
        """
        self._iccid = iccid

    @property
    def flow_total(self):
        """Gets the flow_total of this SimCardsFlowVO.

        总流量(MB),两位小数

        :return: The flow_total of this SimCardsFlowVO.
        :rtype: float
        """
        return self._flow_total

    @flow_total.setter
    def flow_total(self, flow_total):
        """Sets the flow_total of this SimCardsFlowVO.

        总流量(MB),两位小数

        :param flow_total: The flow_total of this SimCardsFlowVO.
        :type flow_total: float
        """
        self._flow_total = flow_total

    @property
    def flow_used(self):
        """Gets the flow_used of this SimCardsFlowVO.

        已使用流量(MB),两位小数

        :return: The flow_used of this SimCardsFlowVO.
        :rtype: float
        """
        return self._flow_used

    @flow_used.setter
    def flow_used(self, flow_used):
        """Sets the flow_used of this SimCardsFlowVO.

        已使用流量(MB),两位小数

        :param flow_used: The flow_used of this SimCardsFlowVO.
        :type flow_used: float
        """
        self._flow_used = flow_used

    @property
    def flow_left(self):
        """Gets the flow_left of this SimCardsFlowVO.

        剩余流量(MB),两位小数

        :return: The flow_left of this SimCardsFlowVO.
        :rtype: float
        """
        return self._flow_left

    @flow_left.setter
    def flow_left(self, flow_left):
        """Sets the flow_left of this SimCardsFlowVO.

        剩余流量(MB),两位小数

        :param flow_left: The flow_left of this SimCardsFlowVO.
        :type flow_left: float
        """
        self._flow_left = flow_left

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
        if not isinstance(other, SimCardsFlowVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
