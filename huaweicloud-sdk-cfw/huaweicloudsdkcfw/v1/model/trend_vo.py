# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrendVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'agg_time': 'int',
        'bps': 'float',
        'deny': 'int',
        'in_bps': 'float',
        'out_bps': 'float',
        'permit': 'int'
    }

    attribute_map = {
        'agg_time': 'agg_time',
        'bps': 'bps',
        'deny': 'deny',
        'in_bps': 'in_bps',
        'out_bps': 'out_bps',
        'permit': 'permit'
    }

    def __init__(self, agg_time=None, bps=None, deny=None, in_bps=None, out_bps=None, permit=None):
        r"""TrendVO

        The model defined in huaweicloud sdk

        :param agg_time: **参数解释**： 聚合时间 **取值范围**： 不涉及
        :type agg_time: int
        :param bps: **参数解释**： 带宽 **取值范围**： 不涉及
        :type bps: float
        :param deny: **参数解释**： 阻断数量 **取值范围**： 不涉及
        :type deny: int
        :param in_bps: **参数解释**： 入方向bps **取值范围**： 不涉及
        :type in_bps: float
        :param out_bps: **参数解释**： 出方向bps **取值范围**： 不涉及
        :type out_bps: float
        :param permit: **参数解释**： 允许数量 **取值范围**： 不涉及
        :type permit: int
        """
        
        

        self._agg_time = None
        self._bps = None
        self._deny = None
        self._in_bps = None
        self._out_bps = None
        self._permit = None
        self.discriminator = None

        if agg_time is not None:
            self.agg_time = agg_time
        if bps is not None:
            self.bps = bps
        if deny is not None:
            self.deny = deny
        if in_bps is not None:
            self.in_bps = in_bps
        if out_bps is not None:
            self.out_bps = out_bps
        if permit is not None:
            self.permit = permit

    @property
    def agg_time(self):
        r"""Gets the agg_time of this TrendVO.

        **参数解释**： 聚合时间 **取值范围**： 不涉及

        :return: The agg_time of this TrendVO.
        :rtype: int
        """
        return self._agg_time

    @agg_time.setter
    def agg_time(self, agg_time):
        r"""Sets the agg_time of this TrendVO.

        **参数解释**： 聚合时间 **取值范围**： 不涉及

        :param agg_time: The agg_time of this TrendVO.
        :type agg_time: int
        """
        self._agg_time = agg_time

    @property
    def bps(self):
        r"""Gets the bps of this TrendVO.

        **参数解释**： 带宽 **取值范围**： 不涉及

        :return: The bps of this TrendVO.
        :rtype: float
        """
        return self._bps

    @bps.setter
    def bps(self, bps):
        r"""Sets the bps of this TrendVO.

        **参数解释**： 带宽 **取值范围**： 不涉及

        :param bps: The bps of this TrendVO.
        :type bps: float
        """
        self._bps = bps

    @property
    def deny(self):
        r"""Gets the deny of this TrendVO.

        **参数解释**： 阻断数量 **取值范围**： 不涉及

        :return: The deny of this TrendVO.
        :rtype: int
        """
        return self._deny

    @deny.setter
    def deny(self, deny):
        r"""Sets the deny of this TrendVO.

        **参数解释**： 阻断数量 **取值范围**： 不涉及

        :param deny: The deny of this TrendVO.
        :type deny: int
        """
        self._deny = deny

    @property
    def in_bps(self):
        r"""Gets the in_bps of this TrendVO.

        **参数解释**： 入方向bps **取值范围**： 不涉及

        :return: The in_bps of this TrendVO.
        :rtype: float
        """
        return self._in_bps

    @in_bps.setter
    def in_bps(self, in_bps):
        r"""Sets the in_bps of this TrendVO.

        **参数解释**： 入方向bps **取值范围**： 不涉及

        :param in_bps: The in_bps of this TrendVO.
        :type in_bps: float
        """
        self._in_bps = in_bps

    @property
    def out_bps(self):
        r"""Gets the out_bps of this TrendVO.

        **参数解释**： 出方向bps **取值范围**： 不涉及

        :return: The out_bps of this TrendVO.
        :rtype: float
        """
        return self._out_bps

    @out_bps.setter
    def out_bps(self, out_bps):
        r"""Sets the out_bps of this TrendVO.

        **参数解释**： 出方向bps **取值范围**： 不涉及

        :param out_bps: The out_bps of this TrendVO.
        :type out_bps: float
        """
        self._out_bps = out_bps

    @property
    def permit(self):
        r"""Gets the permit of this TrendVO.

        **参数解释**： 允许数量 **取值范围**： 不涉及

        :return: The permit of this TrendVO.
        :rtype: int
        """
        return self._permit

    @permit.setter
    def permit(self, permit):
        r"""Sets the permit of this TrendVO.

        **参数解释**： 允许数量 **取值范围**： 不涉及

        :param permit: The permit of this TrendVO.
        :type permit: int
        """
        self._permit = permit

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
        if not isinstance(other, TrendVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
