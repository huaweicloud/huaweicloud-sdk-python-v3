# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQuotasDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'packet_cycle_num': 'int',
        'on_demand_num': 'int',
        'used_num': 'int',
        'idle_num': 'int',
        'normal_num': 'int',
        'expired_num': 'int',
        'create_time': 'int',
        'freeze_num': 'int',
        'quota_statistics_list': 'list[QuotaStatisticsResponseInfo]',
        'total_num': 'int',
        'data_list': 'list[QuotaResourcesResponseInfo]'
    }

    attribute_map = {
        'packet_cycle_num': 'packet_cycle_num',
        'on_demand_num': 'on_demand_num',
        'used_num': 'used_num',
        'idle_num': 'idle_num',
        'normal_num': 'normal_num',
        'expired_num': 'expired_num',
        'create_time': 'create_time',
        'freeze_num': 'freeze_num',
        'quota_statistics_list': 'quota_statistics_list',
        'total_num': 'total_num',
        'data_list': 'data_list'
    }

    def __init__(self, packet_cycle_num=None, on_demand_num=None, used_num=None, idle_num=None, normal_num=None, expired_num=None, create_time=None, freeze_num=None, quota_statistics_list=None, total_num=None, data_list=None):
        r"""ListQuotasDetailResponse

        The model defined in huaweicloud sdk

        :param packet_cycle_num: **参数解释**： 包周期配额数 **取值范围**： 0到10000000 
        :type packet_cycle_num: int
        :param on_demand_num: **参数解释**： 按需配额数 **取值范围**： 0到10000000 
        :type on_demand_num: int
        :param used_num: **参数解释**： 已使用配额数 **取值范围**： 0到10000000 
        :type used_num: int
        :param idle_num: **参数解释**： 空闲配额数 **取值范围**： 0到10000000 
        :type idle_num: int
        :param normal_num: **参数解释**： 正常配额数 **取值范围**： 0到10000000 
        :type normal_num: int
        :param expired_num: **参数解释**： 过期配额数 **取值范围**： 0到10000000 
        :type expired_num: int
        :param create_time: **参数解释**： 创建时间 **取值范围**： 0到9223372036854775807 
        :type create_time: int
        :param freeze_num: **参数解释**： 冻结配额数 **取值范围**： 0到10000000 
        :type freeze_num: int
        :param quota_statistics_list: **参数解释**： 配额统计列表 **取值范围**： 不涉及 
        :type quota_statistics_list: list[:class:`huaweicloudsdkhss.v5.QuotaStatisticsResponseInfo`]
        :param total_num: **参数解释**： 配额总数 **取值范围**： 0到10000000 
        :type total_num: int
        :param data_list: **参数解释**： 配额列表 **取值范围**： 不涉及 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.QuotaResourcesResponseInfo`]
        """
        
        super(ListQuotasDetailResponse, self).__init__()

        self._packet_cycle_num = None
        self._on_demand_num = None
        self._used_num = None
        self._idle_num = None
        self._normal_num = None
        self._expired_num = None
        self._create_time = None
        self._freeze_num = None
        self._quota_statistics_list = None
        self._total_num = None
        self._data_list = None
        self.discriminator = None

        if packet_cycle_num is not None:
            self.packet_cycle_num = packet_cycle_num
        if on_demand_num is not None:
            self.on_demand_num = on_demand_num
        if used_num is not None:
            self.used_num = used_num
        if idle_num is not None:
            self.idle_num = idle_num
        if normal_num is not None:
            self.normal_num = normal_num
        if expired_num is not None:
            self.expired_num = expired_num
        if create_time is not None:
            self.create_time = create_time
        if freeze_num is not None:
            self.freeze_num = freeze_num
        if quota_statistics_list is not None:
            self.quota_statistics_list = quota_statistics_list
        if total_num is not None:
            self.total_num = total_num
        if data_list is not None:
            self.data_list = data_list

    @property
    def packet_cycle_num(self):
        r"""Gets the packet_cycle_num of this ListQuotasDetailResponse.

        **参数解释**： 包周期配额数 **取值范围**： 0到10000000 

        :return: The packet_cycle_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._packet_cycle_num

    @packet_cycle_num.setter
    def packet_cycle_num(self, packet_cycle_num):
        r"""Sets the packet_cycle_num of this ListQuotasDetailResponse.

        **参数解释**： 包周期配额数 **取值范围**： 0到10000000 

        :param packet_cycle_num: The packet_cycle_num of this ListQuotasDetailResponse.
        :type packet_cycle_num: int
        """
        self._packet_cycle_num = packet_cycle_num

    @property
    def on_demand_num(self):
        r"""Gets the on_demand_num of this ListQuotasDetailResponse.

        **参数解释**： 按需配额数 **取值范围**： 0到10000000 

        :return: The on_demand_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._on_demand_num

    @on_demand_num.setter
    def on_demand_num(self, on_demand_num):
        r"""Sets the on_demand_num of this ListQuotasDetailResponse.

        **参数解释**： 按需配额数 **取值范围**： 0到10000000 

        :param on_demand_num: The on_demand_num of this ListQuotasDetailResponse.
        :type on_demand_num: int
        """
        self._on_demand_num = on_demand_num

    @property
    def used_num(self):
        r"""Gets the used_num of this ListQuotasDetailResponse.

        **参数解释**： 已使用配额数 **取值范围**： 0到10000000 

        :return: The used_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._used_num

    @used_num.setter
    def used_num(self, used_num):
        r"""Sets the used_num of this ListQuotasDetailResponse.

        **参数解释**： 已使用配额数 **取值范围**： 0到10000000 

        :param used_num: The used_num of this ListQuotasDetailResponse.
        :type used_num: int
        """
        self._used_num = used_num

    @property
    def idle_num(self):
        r"""Gets the idle_num of this ListQuotasDetailResponse.

        **参数解释**： 空闲配额数 **取值范围**： 0到10000000 

        :return: The idle_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._idle_num

    @idle_num.setter
    def idle_num(self, idle_num):
        r"""Sets the idle_num of this ListQuotasDetailResponse.

        **参数解释**： 空闲配额数 **取值范围**： 0到10000000 

        :param idle_num: The idle_num of this ListQuotasDetailResponse.
        :type idle_num: int
        """
        self._idle_num = idle_num

    @property
    def normal_num(self):
        r"""Gets the normal_num of this ListQuotasDetailResponse.

        **参数解释**： 正常配额数 **取值范围**： 0到10000000 

        :return: The normal_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._normal_num

    @normal_num.setter
    def normal_num(self, normal_num):
        r"""Sets the normal_num of this ListQuotasDetailResponse.

        **参数解释**： 正常配额数 **取值范围**： 0到10000000 

        :param normal_num: The normal_num of this ListQuotasDetailResponse.
        :type normal_num: int
        """
        self._normal_num = normal_num

    @property
    def expired_num(self):
        r"""Gets the expired_num of this ListQuotasDetailResponse.

        **参数解释**： 过期配额数 **取值范围**： 0到10000000 

        :return: The expired_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._expired_num

    @expired_num.setter
    def expired_num(self, expired_num):
        r"""Sets the expired_num of this ListQuotasDetailResponse.

        **参数解释**： 过期配额数 **取值范围**： 0到10000000 

        :param expired_num: The expired_num of this ListQuotasDetailResponse.
        :type expired_num: int
        """
        self._expired_num = expired_num

    @property
    def create_time(self):
        r"""Gets the create_time of this ListQuotasDetailResponse.

        **参数解释**： 创建时间 **取值范围**： 0到9223372036854775807 

        :return: The create_time of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ListQuotasDetailResponse.

        **参数解释**： 创建时间 **取值范围**： 0到9223372036854775807 

        :param create_time: The create_time of this ListQuotasDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def freeze_num(self):
        r"""Gets the freeze_num of this ListQuotasDetailResponse.

        **参数解释**： 冻结配额数 **取值范围**： 0到10000000 

        :return: The freeze_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._freeze_num

    @freeze_num.setter
    def freeze_num(self, freeze_num):
        r"""Sets the freeze_num of this ListQuotasDetailResponse.

        **参数解释**： 冻结配额数 **取值范围**： 0到10000000 

        :param freeze_num: The freeze_num of this ListQuotasDetailResponse.
        :type freeze_num: int
        """
        self._freeze_num = freeze_num

    @property
    def quota_statistics_list(self):
        r"""Gets the quota_statistics_list of this ListQuotasDetailResponse.

        **参数解释**： 配额统计列表 **取值范围**： 不涉及 

        :return: The quota_statistics_list of this ListQuotasDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.QuotaStatisticsResponseInfo`]
        """
        return self._quota_statistics_list

    @quota_statistics_list.setter
    def quota_statistics_list(self, quota_statistics_list):
        r"""Sets the quota_statistics_list of this ListQuotasDetailResponse.

        **参数解释**： 配额统计列表 **取值范围**： 不涉及 

        :param quota_statistics_list: The quota_statistics_list of this ListQuotasDetailResponse.
        :type quota_statistics_list: list[:class:`huaweicloudsdkhss.v5.QuotaStatisticsResponseInfo`]
        """
        self._quota_statistics_list = quota_statistics_list

    @property
    def total_num(self):
        r"""Gets the total_num of this ListQuotasDetailResponse.

        **参数解释**： 配额总数 **取值范围**： 0到10000000 

        :return: The total_num of this ListQuotasDetailResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        r"""Sets the total_num of this ListQuotasDetailResponse.

        **参数解释**： 配额总数 **取值范围**： 0到10000000 

        :param total_num: The total_num of this ListQuotasDetailResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def data_list(self):
        r"""Gets the data_list of this ListQuotasDetailResponse.

        **参数解释**： 配额列表 **取值范围**： 不涉及 

        :return: The data_list of this ListQuotasDetailResponse.
        :rtype: list[:class:`huaweicloudsdkhss.v5.QuotaResourcesResponseInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListQuotasDetailResponse.

        **参数解释**： 配额列表 **取值范围**： 不涉及 

        :param data_list: The data_list of this ListQuotasDetailResponse.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.QuotaResourcesResponseInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, ListQuotasDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
