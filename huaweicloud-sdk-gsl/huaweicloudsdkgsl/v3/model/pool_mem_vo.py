# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolMemVO:

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
        'cid': 'str',
        'sim_price_plan_id': 'int',
        'flow_used': 'float'
    }

    attribute_map = {
        'id': 'id',
        'cid': 'cid',
        'sim_price_plan_id': 'sim_price_plan_id',
        'flow_used': 'flow_used'
    }

    def __init__(self, id=None, cid=None, sim_price_plan_id=None, flow_used=None):
        r"""PoolMemVO

        The model defined in huaweicloud sdk

        :param id: 流量池标识
        :type id: int
        :param cid: 容器ID
        :type cid: str
        :param sim_price_plan_id: 套餐订购实例ID
        :type sim_price_plan_id: int
        :param flow_used: 已用流量(查询账期所在月份), 单位MB
        :type flow_used: float
        """
        
        

        self._id = None
        self._cid = None
        self._sim_price_plan_id = None
        self._flow_used = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cid is not None:
            self.cid = cid
        if sim_price_plan_id is not None:
            self.sim_price_plan_id = sim_price_plan_id
        if flow_used is not None:
            self.flow_used = flow_used

    @property
    def id(self):
        r"""Gets the id of this PoolMemVO.

        流量池标识

        :return: The id of this PoolMemVO.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PoolMemVO.

        流量池标识

        :param id: The id of this PoolMemVO.
        :type id: int
        """
        self._id = id

    @property
    def cid(self):
        r"""Gets the cid of this PoolMemVO.

        容器ID

        :return: The cid of this PoolMemVO.
        :rtype: str
        """
        return self._cid

    @cid.setter
    def cid(self, cid):
        r"""Sets the cid of this PoolMemVO.

        容器ID

        :param cid: The cid of this PoolMemVO.
        :type cid: str
        """
        self._cid = cid

    @property
    def sim_price_plan_id(self):
        r"""Gets the sim_price_plan_id of this PoolMemVO.

        套餐订购实例ID

        :return: The sim_price_plan_id of this PoolMemVO.
        :rtype: int
        """
        return self._sim_price_plan_id

    @sim_price_plan_id.setter
    def sim_price_plan_id(self, sim_price_plan_id):
        r"""Sets the sim_price_plan_id of this PoolMemVO.

        套餐订购实例ID

        :param sim_price_plan_id: The sim_price_plan_id of this PoolMemVO.
        :type sim_price_plan_id: int
        """
        self._sim_price_plan_id = sim_price_plan_id

    @property
    def flow_used(self):
        r"""Gets the flow_used of this PoolMemVO.

        已用流量(查询账期所在月份), 单位MB

        :return: The flow_used of this PoolMemVO.
        :rtype: float
        """
        return self._flow_used

    @flow_used.setter
    def flow_used(self, flow_used):
        r"""Sets the flow_used of this PoolMemVO.

        已用流量(查询账期所在月份), 单位MB

        :param flow_used: The flow_used of this PoolMemVO.
        :type flow_used: float
        """
        self._flow_used = flow_used

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
        if not isinstance(other, PoolMemVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
