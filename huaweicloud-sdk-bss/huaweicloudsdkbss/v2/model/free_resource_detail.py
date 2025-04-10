# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FreeResourceDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'free_resource_id': 'str',
        'free_resource_type_name': 'str',
        'quota_reuse_cycle': 'int',
        'quota_reuse_cycle_type': 'int',
        'usage_type_name': 'str',
        'start_time': 'str',
        'end_time': 'str',
        'amount': 'decimal.Decimal',
        'original_amount': 'decimal.Decimal',
        'measure_id': 'int'
    }

    attribute_map = {
        'free_resource_id': 'free_resource_id',
        'free_resource_type_name': 'free_resource_type_name',
        'quota_reuse_cycle': 'quota_reuse_cycle',
        'quota_reuse_cycle_type': 'quota_reuse_cycle_type',
        'usage_type_name': 'usage_type_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'amount': 'amount',
        'original_amount': 'original_amount',
        'measure_id': 'measure_id'
    }

    def __init__(self, free_resource_id=None, free_resource_type_name=None, quota_reuse_cycle=None, quota_reuse_cycle_type=None, usage_type_name=None, start_time=None, end_time=None, amount=None, original_amount=None, measure_id=None):
        r"""FreeResourceDetail

        The model defined in huaweicloud sdk

        :param free_resource_id: 资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。
        :type free_resource_id: str
        :param free_resource_type_name: 资源项类型名称。
        :type free_resource_type_name: str
        :param quota_reuse_cycle: 重置周期，只有quota_reuse_mode为可重置，该字段才有意义。 1：小时2：天3：周4：月5：年
        :type quota_reuse_cycle: int
        :param quota_reuse_cycle_type: 重置周期类别，只有quota_reuse_mode为可重置，该字段才有意义。 1：按自然周期重置是指重置周期是按照自然月/年来重置，例如如果周期是月，按自然周期重置，表示每个月的1号重置。 2：按订购周期重置。是指重置周期是按照订购时间来重置，例如如果周期是月，按订购周期重置，15号订购了该套餐，表示每个月的15号重置。
        :type quota_reuse_cycle_type: int
        :param usage_type_name: 使用量类型名称。
        :type usage_type_name: str
        :param start_time: 开始时间，格式UTC。 如果quota_reuse_mode为可重置，则此时间为当前时间所在的重置周期的开始时间。如果quota_reuse_mode为不可重置，则此时间为订购实例的生效时间。
        :type start_time: str
        :param end_time: 结束时间，格式UTC。 如果quota_reuse_mode为可重置，则此时间为当前时间所在的重置周期的结束时间。如果quota_reuse_mode为不可重置，则此时间为订购实例的失效时间。
        :type end_time: str
        :param amount: 资源剩余额度，针对可重置资源包，是指当前重置周期内的剩余量。
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param original_amount: 资源原始额度，针对可重置资源包，是指每个重置周期内的总量。
        :type original_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        :param measure_id: 度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。
        :type measure_id: int
        """
        
        

        self._free_resource_id = None
        self._free_resource_type_name = None
        self._quota_reuse_cycle = None
        self._quota_reuse_cycle_type = None
        self._usage_type_name = None
        self._start_time = None
        self._end_time = None
        self._amount = None
        self._original_amount = None
        self._measure_id = None
        self.discriminator = None

        if free_resource_id is not None:
            self.free_resource_id = free_resource_id
        if free_resource_type_name is not None:
            self.free_resource_type_name = free_resource_type_name
        if quota_reuse_cycle is not None:
            self.quota_reuse_cycle = quota_reuse_cycle
        if quota_reuse_cycle_type is not None:
            self.quota_reuse_cycle_type = quota_reuse_cycle_type
        if usage_type_name is not None:
            self.usage_type_name = usage_type_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if amount is not None:
            self.amount = amount
        if original_amount is not None:
            self.original_amount = original_amount
        if measure_id is not None:
            self.measure_id = measure_id

    @property
    def free_resource_id(self):
        r"""Gets the free_resource_id of this FreeResourceDetail.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。

        :return: The free_resource_id of this FreeResourceDetail.
        :rtype: str
        """
        return self._free_resource_id

    @free_resource_id.setter
    def free_resource_id(self, free_resource_id):
        r"""Sets the free_resource_id of this FreeResourceDetail.

        资源项ID，一个资源包中会含有多个资源项，一个使用量类型对应一个资源项。

        :param free_resource_id: The free_resource_id of this FreeResourceDetail.
        :type free_resource_id: str
        """
        self._free_resource_id = free_resource_id

    @property
    def free_resource_type_name(self):
        r"""Gets the free_resource_type_name of this FreeResourceDetail.

        资源项类型名称。

        :return: The free_resource_type_name of this FreeResourceDetail.
        :rtype: str
        """
        return self._free_resource_type_name

    @free_resource_type_name.setter
    def free_resource_type_name(self, free_resource_type_name):
        r"""Sets the free_resource_type_name of this FreeResourceDetail.

        资源项类型名称。

        :param free_resource_type_name: The free_resource_type_name of this FreeResourceDetail.
        :type free_resource_type_name: str
        """
        self._free_resource_type_name = free_resource_type_name

    @property
    def quota_reuse_cycle(self):
        r"""Gets the quota_reuse_cycle of this FreeResourceDetail.

        重置周期，只有quota_reuse_mode为可重置，该字段才有意义。 1：小时2：天3：周4：月5：年

        :return: The quota_reuse_cycle of this FreeResourceDetail.
        :rtype: int
        """
        return self._quota_reuse_cycle

    @quota_reuse_cycle.setter
    def quota_reuse_cycle(self, quota_reuse_cycle):
        r"""Sets the quota_reuse_cycle of this FreeResourceDetail.

        重置周期，只有quota_reuse_mode为可重置，该字段才有意义。 1：小时2：天3：周4：月5：年

        :param quota_reuse_cycle: The quota_reuse_cycle of this FreeResourceDetail.
        :type quota_reuse_cycle: int
        """
        self._quota_reuse_cycle = quota_reuse_cycle

    @property
    def quota_reuse_cycle_type(self):
        r"""Gets the quota_reuse_cycle_type of this FreeResourceDetail.

        重置周期类别，只有quota_reuse_mode为可重置，该字段才有意义。 1：按自然周期重置是指重置周期是按照自然月/年来重置，例如如果周期是月，按自然周期重置，表示每个月的1号重置。 2：按订购周期重置。是指重置周期是按照订购时间来重置，例如如果周期是月，按订购周期重置，15号订购了该套餐，表示每个月的15号重置。

        :return: The quota_reuse_cycle_type of this FreeResourceDetail.
        :rtype: int
        """
        return self._quota_reuse_cycle_type

    @quota_reuse_cycle_type.setter
    def quota_reuse_cycle_type(self, quota_reuse_cycle_type):
        r"""Sets the quota_reuse_cycle_type of this FreeResourceDetail.

        重置周期类别，只有quota_reuse_mode为可重置，该字段才有意义。 1：按自然周期重置是指重置周期是按照自然月/年来重置，例如如果周期是月，按自然周期重置，表示每个月的1号重置。 2：按订购周期重置。是指重置周期是按照订购时间来重置，例如如果周期是月，按订购周期重置，15号订购了该套餐，表示每个月的15号重置。

        :param quota_reuse_cycle_type: The quota_reuse_cycle_type of this FreeResourceDetail.
        :type quota_reuse_cycle_type: int
        """
        self._quota_reuse_cycle_type = quota_reuse_cycle_type

    @property
    def usage_type_name(self):
        r"""Gets the usage_type_name of this FreeResourceDetail.

        使用量类型名称。

        :return: The usage_type_name of this FreeResourceDetail.
        :rtype: str
        """
        return self._usage_type_name

    @usage_type_name.setter
    def usage_type_name(self, usage_type_name):
        r"""Sets the usage_type_name of this FreeResourceDetail.

        使用量类型名称。

        :param usage_type_name: The usage_type_name of this FreeResourceDetail.
        :type usage_type_name: str
        """
        self._usage_type_name = usage_type_name

    @property
    def start_time(self):
        r"""Gets the start_time of this FreeResourceDetail.

        开始时间，格式UTC。 如果quota_reuse_mode为可重置，则此时间为当前时间所在的重置周期的开始时间。如果quota_reuse_mode为不可重置，则此时间为订购实例的生效时间。

        :return: The start_time of this FreeResourceDetail.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this FreeResourceDetail.

        开始时间，格式UTC。 如果quota_reuse_mode为可重置，则此时间为当前时间所在的重置周期的开始时间。如果quota_reuse_mode为不可重置，则此时间为订购实例的生效时间。

        :param start_time: The start_time of this FreeResourceDetail.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this FreeResourceDetail.

        结束时间，格式UTC。 如果quota_reuse_mode为可重置，则此时间为当前时间所在的重置周期的结束时间。如果quota_reuse_mode为不可重置，则此时间为订购实例的失效时间。

        :return: The end_time of this FreeResourceDetail.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this FreeResourceDetail.

        结束时间，格式UTC。 如果quota_reuse_mode为可重置，则此时间为当前时间所在的重置周期的结束时间。如果quota_reuse_mode为不可重置，则此时间为订购实例的失效时间。

        :param end_time: The end_time of this FreeResourceDetail.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def amount(self):
        r"""Gets the amount of this FreeResourceDetail.

        资源剩余额度，针对可重置资源包，是指当前重置周期内的剩余量。

        :return: The amount of this FreeResourceDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        r"""Sets the amount of this FreeResourceDetail.

        资源剩余额度，针对可重置资源包，是指当前重置周期内的剩余量。

        :param amount: The amount of this FreeResourceDetail.
        :type amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._amount = amount

    @property
    def original_amount(self):
        r"""Gets the original_amount of this FreeResourceDetail.

        资源原始额度，针对可重置资源包，是指每个重置周期内的总量。

        :return: The original_amount of this FreeResourceDetail.
        :rtype: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        return self._original_amount

    @original_amount.setter
    def original_amount(self, original_amount):
        r"""Sets the original_amount of this FreeResourceDetail.

        资源原始额度，针对可重置资源包，是指每个重置周期内的总量。

        :param original_amount: The original_amount of this FreeResourceDetail.
        :type original_amount: :class:`huaweicloudsdkbss.v2.decimal.Decimal`
        """
        self._original_amount = original_amount

    @property
    def measure_id(self):
        r"""Gets the measure_id of this FreeResourceDetail.

        度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。

        :return: The measure_id of this FreeResourceDetail.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        r"""Sets the measure_id of this FreeResourceDetail.

        度量单位，免费资源套餐额度度量单位。您可以调用查询度量单位列表接口获取。

        :param measure_id: The measure_id of this FreeResourceDetail.
        :type measure_id: int
        """
        self._measure_id = measure_id

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
        if not isinstance(other, FreeResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
