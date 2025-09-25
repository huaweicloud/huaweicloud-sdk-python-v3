# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseVolumeSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_disk_capacity': 'str',
        'data_disk_usage': 'str',
        'space_usage_growth_per_day': 'str',
        'estimated_remaining_days': 'str',
        'cn_components': 'list[CnComponentInfoResult]',
        'dn_components': 'list[DnComponentInfoResult]'
    }

    attribute_map = {
        'data_disk_capacity': 'data_disk_capacity',
        'data_disk_usage': 'data_disk_usage',
        'space_usage_growth_per_day': 'space_usage_growth_per_day',
        'estimated_remaining_days': 'estimated_remaining_days',
        'cn_components': 'cn_components',
        'dn_components': 'dn_components'
    }

    def __init__(self, data_disk_capacity=None, data_disk_usage=None, space_usage_growth_per_day=None, estimated_remaining_days=None, cn_components=None, dn_components=None):
        r"""ListDatabaseVolumeSummaryResponse

        The model defined in huaweicloud sdk

        :param data_disk_capacity: **参数解释**: 数据盘总量。 **取值范围**: 不涉及。
        :type data_disk_capacity: str
        :param data_disk_usage: **参数解释**: 数据盘使用量。 **取值范围**: 不涉及。
        :type data_disk_usage: str
        :param space_usage_growth_per_day: **参数解释**: 空间使用日均增长量。 **取值范围**: 不涉及。
        :type space_usage_growth_per_day: str
        :param estimated_remaining_days: **参数解释**: 预计可用天数。 **取值范围**: 不涉及。
        :type estimated_remaining_days: str
        :param cn_components: **参数解释**: CN节点信息。
        :type cn_components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CnComponentInfoResult`]
        :param dn_components: **参数解释**: DN节点信息。
        :type dn_components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DnComponentInfoResult`]
        """
        
        super(ListDatabaseVolumeSummaryResponse, self).__init__()

        self._data_disk_capacity = None
        self._data_disk_usage = None
        self._space_usage_growth_per_day = None
        self._estimated_remaining_days = None
        self._cn_components = None
        self._dn_components = None
        self.discriminator = None

        if data_disk_capacity is not None:
            self.data_disk_capacity = data_disk_capacity
        if data_disk_usage is not None:
            self.data_disk_usage = data_disk_usage
        if space_usage_growth_per_day is not None:
            self.space_usage_growth_per_day = space_usage_growth_per_day
        if estimated_remaining_days is not None:
            self.estimated_remaining_days = estimated_remaining_days
        if cn_components is not None:
            self.cn_components = cn_components
        if dn_components is not None:
            self.dn_components = dn_components

    @property
    def data_disk_capacity(self):
        r"""Gets the data_disk_capacity of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 数据盘总量。 **取值范围**: 不涉及。

        :return: The data_disk_capacity of this ListDatabaseVolumeSummaryResponse.
        :rtype: str
        """
        return self._data_disk_capacity

    @data_disk_capacity.setter
    def data_disk_capacity(self, data_disk_capacity):
        r"""Sets the data_disk_capacity of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 数据盘总量。 **取值范围**: 不涉及。

        :param data_disk_capacity: The data_disk_capacity of this ListDatabaseVolumeSummaryResponse.
        :type data_disk_capacity: str
        """
        self._data_disk_capacity = data_disk_capacity

    @property
    def data_disk_usage(self):
        r"""Gets the data_disk_usage of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 数据盘使用量。 **取值范围**: 不涉及。

        :return: The data_disk_usage of this ListDatabaseVolumeSummaryResponse.
        :rtype: str
        """
        return self._data_disk_usage

    @data_disk_usage.setter
    def data_disk_usage(self, data_disk_usage):
        r"""Sets the data_disk_usage of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 数据盘使用量。 **取值范围**: 不涉及。

        :param data_disk_usage: The data_disk_usage of this ListDatabaseVolumeSummaryResponse.
        :type data_disk_usage: str
        """
        self._data_disk_usage = data_disk_usage

    @property
    def space_usage_growth_per_day(self):
        r"""Gets the space_usage_growth_per_day of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 空间使用日均增长量。 **取值范围**: 不涉及。

        :return: The space_usage_growth_per_day of this ListDatabaseVolumeSummaryResponse.
        :rtype: str
        """
        return self._space_usage_growth_per_day

    @space_usage_growth_per_day.setter
    def space_usage_growth_per_day(self, space_usage_growth_per_day):
        r"""Sets the space_usage_growth_per_day of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 空间使用日均增长量。 **取值范围**: 不涉及。

        :param space_usage_growth_per_day: The space_usage_growth_per_day of this ListDatabaseVolumeSummaryResponse.
        :type space_usage_growth_per_day: str
        """
        self._space_usage_growth_per_day = space_usage_growth_per_day

    @property
    def estimated_remaining_days(self):
        r"""Gets the estimated_remaining_days of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 预计可用天数。 **取值范围**: 不涉及。

        :return: The estimated_remaining_days of this ListDatabaseVolumeSummaryResponse.
        :rtype: str
        """
        return self._estimated_remaining_days

    @estimated_remaining_days.setter
    def estimated_remaining_days(self, estimated_remaining_days):
        r"""Sets the estimated_remaining_days of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: 预计可用天数。 **取值范围**: 不涉及。

        :param estimated_remaining_days: The estimated_remaining_days of this ListDatabaseVolumeSummaryResponse.
        :type estimated_remaining_days: str
        """
        self._estimated_remaining_days = estimated_remaining_days

    @property
    def cn_components(self):
        r"""Gets the cn_components of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: CN节点信息。

        :return: The cn_components of this ListDatabaseVolumeSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CnComponentInfoResult`]
        """
        return self._cn_components

    @cn_components.setter
    def cn_components(self, cn_components):
        r"""Sets the cn_components of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: CN节点信息。

        :param cn_components: The cn_components of this ListDatabaseVolumeSummaryResponse.
        :type cn_components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CnComponentInfoResult`]
        """
        self._cn_components = cn_components

    @property
    def dn_components(self):
        r"""Gets the dn_components of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: DN节点信息。

        :return: The dn_components of this ListDatabaseVolumeSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DnComponentInfoResult`]
        """
        return self._dn_components

    @dn_components.setter
    def dn_components(self, dn_components):
        r"""Sets the dn_components of this ListDatabaseVolumeSummaryResponse.

        **参数解释**: DN节点信息。

        :param dn_components: The dn_components of this ListDatabaseVolumeSummaryResponse.
        :type dn_components: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.DnComponentInfoResult`]
        """
        self._dn_components = dn_components

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
        if not isinstance(other, ListDatabaseVolumeSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
