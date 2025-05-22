# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SCTE35InfoItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'event_id': 'int',
        'start_date': 'int',
        'duration': 'int',
        'segmentation_type': 'str',
        'base64_data': 'str',
        'raw_splice': 'str'
    }

    attribute_map = {
        'type': 'type',
        'event_id': 'event_id',
        'start_date': 'start_date',
        'duration': 'duration',
        'segmentation_type': 'segmentation_type',
        'base64_data': 'base64_data',
        'raw_splice': 'raw_splice'
    }

    def __init__(self, type=None, event_id=None, start_date=None, duration=None, segmentation_type=None, base64_data=None, raw_splice=None):
        r"""SCTE35InfoItem

        The model defined in huaweicloud sdk

        :param type: 信号类型，splice_insert/time_signal。
        :type type: str
        :param event_id: 广告信号的Event ID，Time Signal打印数组第一个。
        :type event_id: int
        :param start_date: 广告信号的执行时间，unix time，单位：秒。
        :type start_date: int
        :param duration: 广告信号时长，-1表示没有携带,单位：秒。
        :type duration: int
        :param segmentation_type: // Splice Insert填空\&quot;-\&quot;； // Time Signal，支持0x30，0x31，0x32，0x33，0x34，0x35，0x36，0x37 // 0x30: ProviderAdvertisementStart // 0x31: ProviderAdvertisementEnd // 0x32: DistributorAdvertisementStart // 0x33: DistributorAdvertisementEnd // 0x34: ProviderPlacementOpportunityStart // 0x35: ProviderPlacementOpportunityEnd // 0x36: DistributorPlacementOpportunityStart // 0x37: DistributorPlacementOpportunityEnd
        :type segmentation_type: str
        :param base64_data: 广告信号原始数据的base64值。
        :type base64_data: str
        :param raw_splice: 广告信号全量信息。
        :type raw_splice: str
        """
        
        

        self._type = None
        self._event_id = None
        self._start_date = None
        self._duration = None
        self._segmentation_type = None
        self._base64_data = None
        self._raw_splice = None
        self.discriminator = None

        self.type = type
        self.event_id = event_id
        self.start_date = start_date
        self.duration = duration
        self.segmentation_type = segmentation_type
        self.base64_data = base64_data
        self.raw_splice = raw_splice

    @property
    def type(self):
        r"""Gets the type of this SCTE35InfoItem.

        信号类型，splice_insert/time_signal。

        :return: The type of this SCTE35InfoItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SCTE35InfoItem.

        信号类型，splice_insert/time_signal。

        :param type: The type of this SCTE35InfoItem.
        :type type: str
        """
        self._type = type

    @property
    def event_id(self):
        r"""Gets the event_id of this SCTE35InfoItem.

        广告信号的Event ID，Time Signal打印数组第一个。

        :return: The event_id of this SCTE35InfoItem.
        :rtype: int
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this SCTE35InfoItem.

        广告信号的Event ID，Time Signal打印数组第一个。

        :param event_id: The event_id of this SCTE35InfoItem.
        :type event_id: int
        """
        self._event_id = event_id

    @property
    def start_date(self):
        r"""Gets the start_date of this SCTE35InfoItem.

        广告信号的执行时间，unix time，单位：秒。

        :return: The start_date of this SCTE35InfoItem.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        r"""Sets the start_date of this SCTE35InfoItem.

        广告信号的执行时间，unix time，单位：秒。

        :param start_date: The start_date of this SCTE35InfoItem.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def duration(self):
        r"""Gets the duration of this SCTE35InfoItem.

        广告信号时长，-1表示没有携带,单位：秒。

        :return: The duration of this SCTE35InfoItem.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this SCTE35InfoItem.

        广告信号时长，-1表示没有携带,单位：秒。

        :param duration: The duration of this SCTE35InfoItem.
        :type duration: int
        """
        self._duration = duration

    @property
    def segmentation_type(self):
        r"""Gets the segmentation_type of this SCTE35InfoItem.

        // Splice Insert填空\"-\"； // Time Signal，支持0x30，0x31，0x32，0x33，0x34，0x35，0x36，0x37 // 0x30: ProviderAdvertisementStart // 0x31: ProviderAdvertisementEnd // 0x32: DistributorAdvertisementStart // 0x33: DistributorAdvertisementEnd // 0x34: ProviderPlacementOpportunityStart // 0x35: ProviderPlacementOpportunityEnd // 0x36: DistributorPlacementOpportunityStart // 0x37: DistributorPlacementOpportunityEnd

        :return: The segmentation_type of this SCTE35InfoItem.
        :rtype: str
        """
        return self._segmentation_type

    @segmentation_type.setter
    def segmentation_type(self, segmentation_type):
        r"""Sets the segmentation_type of this SCTE35InfoItem.

        // Splice Insert填空\"-\"； // Time Signal，支持0x30，0x31，0x32，0x33，0x34，0x35，0x36，0x37 // 0x30: ProviderAdvertisementStart // 0x31: ProviderAdvertisementEnd // 0x32: DistributorAdvertisementStart // 0x33: DistributorAdvertisementEnd // 0x34: ProviderPlacementOpportunityStart // 0x35: ProviderPlacementOpportunityEnd // 0x36: DistributorPlacementOpportunityStart // 0x37: DistributorPlacementOpportunityEnd

        :param segmentation_type: The segmentation_type of this SCTE35InfoItem.
        :type segmentation_type: str
        """
        self._segmentation_type = segmentation_type

    @property
    def base64_data(self):
        r"""Gets the base64_data of this SCTE35InfoItem.

        广告信号原始数据的base64值。

        :return: The base64_data of this SCTE35InfoItem.
        :rtype: str
        """
        return self._base64_data

    @base64_data.setter
    def base64_data(self, base64_data):
        r"""Sets the base64_data of this SCTE35InfoItem.

        广告信号原始数据的base64值。

        :param base64_data: The base64_data of this SCTE35InfoItem.
        :type base64_data: str
        """
        self._base64_data = base64_data

    @property
    def raw_splice(self):
        r"""Gets the raw_splice of this SCTE35InfoItem.

        广告信号全量信息。

        :return: The raw_splice of this SCTE35InfoItem.
        :rtype: str
        """
        return self._raw_splice

    @raw_splice.setter
    def raw_splice(self, raw_splice):
        r"""Sets the raw_splice of this SCTE35InfoItem.

        广告信号全量信息。

        :param raw_splice: The raw_splice of this SCTE35InfoItem.
        :type raw_splice: str
        """
        self._raw_splice = raw_splice

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
        if not isinstance(other, SCTE35InfoItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
