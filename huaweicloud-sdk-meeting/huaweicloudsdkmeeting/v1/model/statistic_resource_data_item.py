# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticResourceDataItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'vmr_parties': 'str',
        'max_concurrency_vmr_count': 'str',
        'live_port_used_count': 'str',
        'record_used_size': 'str',
        'pstn_used_duration': 'str'
    }

    attribute_map = {
        'time': 'time',
        'vmr_parties': 'vmrParties',
        'max_concurrency_vmr_count': 'maxConcurrencyVmrCount',
        'live_port_used_count': 'livePortUsedCount',
        'record_used_size': 'recordUsedSize',
        'pstn_used_duration': 'pstnUsedDuration'
    }

    def __init__(self, time=None, vmr_parties=None, max_concurrency_vmr_count=None, live_port_used_count=None, record_used_size=None, pstn_used_duration=None):
        """StatisticResourceDataItem

        The model defined in huaweicloud sdk

        :param time: 日期/月份。
        :type time: str
        :param vmr_parties: VMR方数。 category &#x3D; used_vmr_info时有效。
        :type vmr_parties: str
        :param max_concurrency_vmr_count: VMR并发使用数。 category &#x3D; used_vmr_info时有效。
        :type max_concurrency_vmr_count: str
        :param live_port_used_count: 直播端口并发使用数。 category &#x3D; used_live_info时有效。
        :type live_port_used_count: str
        :param record_used_size: 录播使用空间(G)。 category &#x3D; used_record_info时有效。
        :type record_used_size: str
        :param pstn_used_duration: PSTN外呼时长(分钟)。 category &#x3D; used_pstn_info时有效。
        :type pstn_used_duration: str
        """
        
        

        self._time = None
        self._vmr_parties = None
        self._max_concurrency_vmr_count = None
        self._live_port_used_count = None
        self._record_used_size = None
        self._pstn_used_duration = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if vmr_parties is not None:
            self.vmr_parties = vmr_parties
        if max_concurrency_vmr_count is not None:
            self.max_concurrency_vmr_count = max_concurrency_vmr_count
        if live_port_used_count is not None:
            self.live_port_used_count = live_port_used_count
        if record_used_size is not None:
            self.record_used_size = record_used_size
        if pstn_used_duration is not None:
            self.pstn_used_duration = pstn_used_duration

    @property
    def time(self):
        """Gets the time of this StatisticResourceDataItem.

        日期/月份。

        :return: The time of this StatisticResourceDataItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StatisticResourceDataItem.

        日期/月份。

        :param time: The time of this StatisticResourceDataItem.
        :type time: str
        """
        self._time = time

    @property
    def vmr_parties(self):
        """Gets the vmr_parties of this StatisticResourceDataItem.

        VMR方数。 category = used_vmr_info时有效。

        :return: The vmr_parties of this StatisticResourceDataItem.
        :rtype: str
        """
        return self._vmr_parties

    @vmr_parties.setter
    def vmr_parties(self, vmr_parties):
        """Sets the vmr_parties of this StatisticResourceDataItem.

        VMR方数。 category = used_vmr_info时有效。

        :param vmr_parties: The vmr_parties of this StatisticResourceDataItem.
        :type vmr_parties: str
        """
        self._vmr_parties = vmr_parties

    @property
    def max_concurrency_vmr_count(self):
        """Gets the max_concurrency_vmr_count of this StatisticResourceDataItem.

        VMR并发使用数。 category = used_vmr_info时有效。

        :return: The max_concurrency_vmr_count of this StatisticResourceDataItem.
        :rtype: str
        """
        return self._max_concurrency_vmr_count

    @max_concurrency_vmr_count.setter
    def max_concurrency_vmr_count(self, max_concurrency_vmr_count):
        """Sets the max_concurrency_vmr_count of this StatisticResourceDataItem.

        VMR并发使用数。 category = used_vmr_info时有效。

        :param max_concurrency_vmr_count: The max_concurrency_vmr_count of this StatisticResourceDataItem.
        :type max_concurrency_vmr_count: str
        """
        self._max_concurrency_vmr_count = max_concurrency_vmr_count

    @property
    def live_port_used_count(self):
        """Gets the live_port_used_count of this StatisticResourceDataItem.

        直播端口并发使用数。 category = used_live_info时有效。

        :return: The live_port_used_count of this StatisticResourceDataItem.
        :rtype: str
        """
        return self._live_port_used_count

    @live_port_used_count.setter
    def live_port_used_count(self, live_port_used_count):
        """Sets the live_port_used_count of this StatisticResourceDataItem.

        直播端口并发使用数。 category = used_live_info时有效。

        :param live_port_used_count: The live_port_used_count of this StatisticResourceDataItem.
        :type live_port_used_count: str
        """
        self._live_port_used_count = live_port_used_count

    @property
    def record_used_size(self):
        """Gets the record_used_size of this StatisticResourceDataItem.

        录播使用空间(G)。 category = used_record_info时有效。

        :return: The record_used_size of this StatisticResourceDataItem.
        :rtype: str
        """
        return self._record_used_size

    @record_used_size.setter
    def record_used_size(self, record_used_size):
        """Sets the record_used_size of this StatisticResourceDataItem.

        录播使用空间(G)。 category = used_record_info时有效。

        :param record_used_size: The record_used_size of this StatisticResourceDataItem.
        :type record_used_size: str
        """
        self._record_used_size = record_used_size

    @property
    def pstn_used_duration(self):
        """Gets the pstn_used_duration of this StatisticResourceDataItem.

        PSTN外呼时长(分钟)。 category = used_pstn_info时有效。

        :return: The pstn_used_duration of this StatisticResourceDataItem.
        :rtype: str
        """
        return self._pstn_used_duration

    @pstn_used_duration.setter
    def pstn_used_duration(self, pstn_used_duration):
        """Sets the pstn_used_duration of this StatisticResourceDataItem.

        PSTN外呼时长(分钟)。 category = used_pstn_info时有效。

        :param pstn_used_duration: The pstn_used_duration of this StatisticResourceDataItem.
        :type pstn_used_duration: str
        """
        self._pstn_used_duration = pstn_used_duration

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
        if not isinstance(other, StatisticResourceDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
