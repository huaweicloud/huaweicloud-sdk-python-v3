# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessTopStatisticsVO:

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
        'deny_access_top_counts': 'int',
        'permit_access_top_counts': 'int',
        'total_access_top_counts': 'int'
    }

    attribute_map = {
        'agg_time': 'agg_time',
        'deny_access_top_counts': 'deny_access_top_counts',
        'permit_access_top_counts': 'permit_access_top_counts',
        'total_access_top_counts': 'total_access_top_counts'
    }

    def __init__(self, agg_time=None, deny_access_top_counts=None, permit_access_top_counts=None, total_access_top_counts=None):
        r"""AccessTopStatisticsVO

        The model defined in huaweicloud sdk

        :param agg_time: **参数解释**： 聚合时间 **取值范围**： 不涉及
        :type agg_time: int
        :param deny_access_top_counts: **参数解释**： 阻断数量 **取值范围**： 不涉及
        :type deny_access_top_counts: int
        :param permit_access_top_counts: **参数解释**： 放行数量 **取值范围**： 不涉及
        :type permit_access_top_counts: int
        :param total_access_top_counts: **参数解释**： 命中次数 **取值范围**： 不涉及
        :type total_access_top_counts: int
        """
        
        

        self._agg_time = None
        self._deny_access_top_counts = None
        self._permit_access_top_counts = None
        self._total_access_top_counts = None
        self.discriminator = None

        if agg_time is not None:
            self.agg_time = agg_time
        if deny_access_top_counts is not None:
            self.deny_access_top_counts = deny_access_top_counts
        if permit_access_top_counts is not None:
            self.permit_access_top_counts = permit_access_top_counts
        if total_access_top_counts is not None:
            self.total_access_top_counts = total_access_top_counts

    @property
    def agg_time(self):
        r"""Gets the agg_time of this AccessTopStatisticsVO.

        **参数解释**： 聚合时间 **取值范围**： 不涉及

        :return: The agg_time of this AccessTopStatisticsVO.
        :rtype: int
        """
        return self._agg_time

    @agg_time.setter
    def agg_time(self, agg_time):
        r"""Sets the agg_time of this AccessTopStatisticsVO.

        **参数解释**： 聚合时间 **取值范围**： 不涉及

        :param agg_time: The agg_time of this AccessTopStatisticsVO.
        :type agg_time: int
        """
        self._agg_time = agg_time

    @property
    def deny_access_top_counts(self):
        r"""Gets the deny_access_top_counts of this AccessTopStatisticsVO.

        **参数解释**： 阻断数量 **取值范围**： 不涉及

        :return: The deny_access_top_counts of this AccessTopStatisticsVO.
        :rtype: int
        """
        return self._deny_access_top_counts

    @deny_access_top_counts.setter
    def deny_access_top_counts(self, deny_access_top_counts):
        r"""Sets the deny_access_top_counts of this AccessTopStatisticsVO.

        **参数解释**： 阻断数量 **取值范围**： 不涉及

        :param deny_access_top_counts: The deny_access_top_counts of this AccessTopStatisticsVO.
        :type deny_access_top_counts: int
        """
        self._deny_access_top_counts = deny_access_top_counts

    @property
    def permit_access_top_counts(self):
        r"""Gets the permit_access_top_counts of this AccessTopStatisticsVO.

        **参数解释**： 放行数量 **取值范围**： 不涉及

        :return: The permit_access_top_counts of this AccessTopStatisticsVO.
        :rtype: int
        """
        return self._permit_access_top_counts

    @permit_access_top_counts.setter
    def permit_access_top_counts(self, permit_access_top_counts):
        r"""Sets the permit_access_top_counts of this AccessTopStatisticsVO.

        **参数解释**： 放行数量 **取值范围**： 不涉及

        :param permit_access_top_counts: The permit_access_top_counts of this AccessTopStatisticsVO.
        :type permit_access_top_counts: int
        """
        self._permit_access_top_counts = permit_access_top_counts

    @property
    def total_access_top_counts(self):
        r"""Gets the total_access_top_counts of this AccessTopStatisticsVO.

        **参数解释**： 命中次数 **取值范围**： 不涉及

        :return: The total_access_top_counts of this AccessTopStatisticsVO.
        :rtype: int
        """
        return self._total_access_top_counts

    @total_access_top_counts.setter
    def total_access_top_counts(self, total_access_top_counts):
        r"""Sets the total_access_top_counts of this AccessTopStatisticsVO.

        **参数解释**： 命中次数 **取值范围**： 不涉及

        :param total_access_top_counts: The total_access_top_counts of this AccessTopStatisticsVO.
        :type total_access_top_counts: int
        """
        self._total_access_top_counts = total_access_top_counts

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
        if not isinstance(other, AccessTopStatisticsVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
