# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorSellPoliciesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_id': 'str',
        'sell_status': 'str',
        'sell_mode': 'str',
        'availability_zone_id': 'str',
        'longest_spot_duration_hours_gt': 'int',
        'largest_spot_duration_count_gt': 'int',
        'longest_spot_duration_hours': 'int',
        'largest_spot_duration_count': 'int',
        'interruption_policy': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'flavor_id': 'flavor_id',
        'sell_status': 'sell_status',
        'sell_mode': 'sell_mode',
        'availability_zone_id': 'availability_zone_id',
        'longest_spot_duration_hours_gt': 'longest_spot_duration_hours_gt',
        'largest_spot_duration_count_gt': 'largest_spot_duration_count_gt',
        'longest_spot_duration_hours': 'longest_spot_duration_hours',
        'largest_spot_duration_count': 'largest_spot_duration_count',
        'interruption_policy': 'interruption_policy',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, flavor_id=None, sell_status=None, sell_mode=None, availability_zone_id=None, longest_spot_duration_hours_gt=None, largest_spot_duration_count_gt=None, longest_spot_duration_hours=None, largest_spot_duration_count=None, interruption_policy=None, limit=None, marker=None):
        r"""ListFlavorSellPoliciesRequest

        The model defined in huaweicloud sdk

        :param flavor_id: 云服务器的系统规格的ID
        :type flavor_id: str
        :param sell_status: 云服务器的系统规格销售状态。  取值范围：  - available：正常售卖 - sellout：售罄
        :type sell_status: str
        :param sell_mode: 计费模式。  key的取值范围：  - postPaid：按需计费实例。 - prePaid：包年/包月计费实例。 - spot：竞价实例。 - ri：预留实例。
        :type sell_mode: str
        :param availability_zone_id: 可用区，需要指定可用区（AZ）
        :type availability_zone_id: str
        :param longest_spot_duration_hours_gt: 查询竞价实例时长大于设置值的策略
        :type longest_spot_duration_hours_gt: int
        :param largest_spot_duration_count_gt: 查询“竞价实例时长”的个数大于设置值的策略
        :type largest_spot_duration_count_gt: int
        :param longest_spot_duration_hours: 查询竞价实例时长等于设置值的策略
        :type longest_spot_duration_hours: int
        :param largest_spot_duration_count: 查询“竞价实例时长”的个数等于设置值的策略
        :type largest_spot_duration_count: int
        :param interruption_policy: 中断策略。  取值范围：  - immediate：立即释放 - delay：延迟释放
        :type interruption_policy: str
        :param limit: 单页面可显示的flavor条数最大值，默认是1000。
        :type limit: int
        :param marker: 以单页最后一条flavor的ID作为分页标记。
        :type marker: str
        """
        
        

        self._flavor_id = None
        self._sell_status = None
        self._sell_mode = None
        self._availability_zone_id = None
        self._longest_spot_duration_hours_gt = None
        self._largest_spot_duration_count_gt = None
        self._longest_spot_duration_hours = None
        self._largest_spot_duration_count = None
        self._interruption_policy = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if flavor_id is not None:
            self.flavor_id = flavor_id
        if sell_status is not None:
            self.sell_status = sell_status
        if sell_mode is not None:
            self.sell_mode = sell_mode
        if availability_zone_id is not None:
            self.availability_zone_id = availability_zone_id
        if longest_spot_duration_hours_gt is not None:
            self.longest_spot_duration_hours_gt = longest_spot_duration_hours_gt
        if largest_spot_duration_count_gt is not None:
            self.largest_spot_duration_count_gt = largest_spot_duration_count_gt
        if longest_spot_duration_hours is not None:
            self.longest_spot_duration_hours = longest_spot_duration_hours
        if largest_spot_duration_count is not None:
            self.largest_spot_duration_count = largest_spot_duration_count
        if interruption_policy is not None:
            self.interruption_policy = interruption_policy
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def flavor_id(self):
        r"""Gets the flavor_id of this ListFlavorSellPoliciesRequest.

        云服务器的系统规格的ID

        :return: The flavor_id of this ListFlavorSellPoliciesRequest.
        :rtype: str
        """
        return self._flavor_id

    @flavor_id.setter
    def flavor_id(self, flavor_id):
        r"""Sets the flavor_id of this ListFlavorSellPoliciesRequest.

        云服务器的系统规格的ID

        :param flavor_id: The flavor_id of this ListFlavorSellPoliciesRequest.
        :type flavor_id: str
        """
        self._flavor_id = flavor_id

    @property
    def sell_status(self):
        r"""Gets the sell_status of this ListFlavorSellPoliciesRequest.

        云服务器的系统规格销售状态。  取值范围：  - available：正常售卖 - sellout：售罄

        :return: The sell_status of this ListFlavorSellPoliciesRequest.
        :rtype: str
        """
        return self._sell_status

    @sell_status.setter
    def sell_status(self, sell_status):
        r"""Sets the sell_status of this ListFlavorSellPoliciesRequest.

        云服务器的系统规格销售状态。  取值范围：  - available：正常售卖 - sellout：售罄

        :param sell_status: The sell_status of this ListFlavorSellPoliciesRequest.
        :type sell_status: str
        """
        self._sell_status = sell_status

    @property
    def sell_mode(self):
        r"""Gets the sell_mode of this ListFlavorSellPoliciesRequest.

        计费模式。  key的取值范围：  - postPaid：按需计费实例。 - prePaid：包年/包月计费实例。 - spot：竞价实例。 - ri：预留实例。

        :return: The sell_mode of this ListFlavorSellPoliciesRequest.
        :rtype: str
        """
        return self._sell_mode

    @sell_mode.setter
    def sell_mode(self, sell_mode):
        r"""Sets the sell_mode of this ListFlavorSellPoliciesRequest.

        计费模式。  key的取值范围：  - postPaid：按需计费实例。 - prePaid：包年/包月计费实例。 - spot：竞价实例。 - ri：预留实例。

        :param sell_mode: The sell_mode of this ListFlavorSellPoliciesRequest.
        :type sell_mode: str
        """
        self._sell_mode = sell_mode

    @property
    def availability_zone_id(self):
        r"""Gets the availability_zone_id of this ListFlavorSellPoliciesRequest.

        可用区，需要指定可用区（AZ）

        :return: The availability_zone_id of this ListFlavorSellPoliciesRequest.
        :rtype: str
        """
        return self._availability_zone_id

    @availability_zone_id.setter
    def availability_zone_id(self, availability_zone_id):
        r"""Sets the availability_zone_id of this ListFlavorSellPoliciesRequest.

        可用区，需要指定可用区（AZ）

        :param availability_zone_id: The availability_zone_id of this ListFlavorSellPoliciesRequest.
        :type availability_zone_id: str
        """
        self._availability_zone_id = availability_zone_id

    @property
    def longest_spot_duration_hours_gt(self):
        r"""Gets the longest_spot_duration_hours_gt of this ListFlavorSellPoliciesRequest.

        查询竞价实例时长大于设置值的策略

        :return: The longest_spot_duration_hours_gt of this ListFlavorSellPoliciesRequest.
        :rtype: int
        """
        return self._longest_spot_duration_hours_gt

    @longest_spot_duration_hours_gt.setter
    def longest_spot_duration_hours_gt(self, longest_spot_duration_hours_gt):
        r"""Sets the longest_spot_duration_hours_gt of this ListFlavorSellPoliciesRequest.

        查询竞价实例时长大于设置值的策略

        :param longest_spot_duration_hours_gt: The longest_spot_duration_hours_gt of this ListFlavorSellPoliciesRequest.
        :type longest_spot_duration_hours_gt: int
        """
        self._longest_spot_duration_hours_gt = longest_spot_duration_hours_gt

    @property
    def largest_spot_duration_count_gt(self):
        r"""Gets the largest_spot_duration_count_gt of this ListFlavorSellPoliciesRequest.

        查询“竞价实例时长”的个数大于设置值的策略

        :return: The largest_spot_duration_count_gt of this ListFlavorSellPoliciesRequest.
        :rtype: int
        """
        return self._largest_spot_duration_count_gt

    @largest_spot_duration_count_gt.setter
    def largest_spot_duration_count_gt(self, largest_spot_duration_count_gt):
        r"""Sets the largest_spot_duration_count_gt of this ListFlavorSellPoliciesRequest.

        查询“竞价实例时长”的个数大于设置值的策略

        :param largest_spot_duration_count_gt: The largest_spot_duration_count_gt of this ListFlavorSellPoliciesRequest.
        :type largest_spot_duration_count_gt: int
        """
        self._largest_spot_duration_count_gt = largest_spot_duration_count_gt

    @property
    def longest_spot_duration_hours(self):
        r"""Gets the longest_spot_duration_hours of this ListFlavorSellPoliciesRequest.

        查询竞价实例时长等于设置值的策略

        :return: The longest_spot_duration_hours of this ListFlavorSellPoliciesRequest.
        :rtype: int
        """
        return self._longest_spot_duration_hours

    @longest_spot_duration_hours.setter
    def longest_spot_duration_hours(self, longest_spot_duration_hours):
        r"""Sets the longest_spot_duration_hours of this ListFlavorSellPoliciesRequest.

        查询竞价实例时长等于设置值的策略

        :param longest_spot_duration_hours: The longest_spot_duration_hours of this ListFlavorSellPoliciesRequest.
        :type longest_spot_duration_hours: int
        """
        self._longest_spot_duration_hours = longest_spot_duration_hours

    @property
    def largest_spot_duration_count(self):
        r"""Gets the largest_spot_duration_count of this ListFlavorSellPoliciesRequest.

        查询“竞价实例时长”的个数等于设置值的策略

        :return: The largest_spot_duration_count of this ListFlavorSellPoliciesRequest.
        :rtype: int
        """
        return self._largest_spot_duration_count

    @largest_spot_duration_count.setter
    def largest_spot_duration_count(self, largest_spot_duration_count):
        r"""Sets the largest_spot_duration_count of this ListFlavorSellPoliciesRequest.

        查询“竞价实例时长”的个数等于设置值的策略

        :param largest_spot_duration_count: The largest_spot_duration_count of this ListFlavorSellPoliciesRequest.
        :type largest_spot_duration_count: int
        """
        self._largest_spot_duration_count = largest_spot_duration_count

    @property
    def interruption_policy(self):
        r"""Gets the interruption_policy of this ListFlavorSellPoliciesRequest.

        中断策略。  取值范围：  - immediate：立即释放 - delay：延迟释放

        :return: The interruption_policy of this ListFlavorSellPoliciesRequest.
        :rtype: str
        """
        return self._interruption_policy

    @interruption_policy.setter
    def interruption_policy(self, interruption_policy):
        r"""Sets the interruption_policy of this ListFlavorSellPoliciesRequest.

        中断策略。  取值范围：  - immediate：立即释放 - delay：延迟释放

        :param interruption_policy: The interruption_policy of this ListFlavorSellPoliciesRequest.
        :type interruption_policy: str
        """
        self._interruption_policy = interruption_policy

    @property
    def limit(self):
        r"""Gets the limit of this ListFlavorSellPoliciesRequest.

        单页面可显示的flavor条数最大值，默认是1000。

        :return: The limit of this ListFlavorSellPoliciesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlavorSellPoliciesRequest.

        单页面可显示的flavor条数最大值，默认是1000。

        :param limit: The limit of this ListFlavorSellPoliciesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListFlavorSellPoliciesRequest.

        以单页最后一条flavor的ID作为分页标记。

        :return: The marker of this ListFlavorSellPoliciesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFlavorSellPoliciesRequest.

        以单页最后一条flavor的ID作为分页标记。

        :param marker: The marker of this ListFlavorSellPoliciesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListFlavorSellPoliciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
