# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHistoryTrafficEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'from_date': 'int',
        'to_date': 'int',
        'event_id': 'str',
        'event_class': 'str',
        'event_type': 'str',
        'event_source': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'offset': 'offset',
        'limit': 'limit',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'event_id': 'event_id',
        'event_class': 'event_class',
        'event_type': 'event_type',
        'event_source': 'event_source'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, from_date=None, to_date=None, event_id=None, event_class=None, event_type=None, event_source=None):
        """ShowHistoryTrafficEventsRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param offset: **参数说明**：分页查询时的页码。
        :type offset: int
        :param limit: **参数说明**：分页查询时每页显示的记录数。
        :type limit: int
        :param from_date: **参数说明**：查询此时间后达到平台的消息，十位Unix时间戳，秒级，例如：1575446506。
        :type from_date: int
        :param to_date: **参数说明**：查询此时间前达到平台的消息，十位Unix时间戳，秒级，例如：1576396905。
        :type to_date: int
        :param event_id: **参数说明**：事件id
        :type event_id: str
        :param event_class: **参数说明**：事件的分类，event_type存在时，event_class必选。  **取值范围**：  - AbnormalTraffic：异常路况  - AbnormalVehicle：异常车况  - AdverseWeather：恶劣天气  - TrafficSign：标志标牌 
        :type event_class: str
        :param event_type: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。
        :type event_type: str
        :param event_source: **参数说明**：事件来源，默认值v2xServer。  **取值范围**：  - v2xServer：来源为通过Console下发的事件  - detection：来源为边缘edge上报的RSI  - rsu：来源为通过MQTT接入的RSU上报的RSI 
        :type event_source: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._from_date = None
        self._to_date = None
        self._event_id = None
        self._event_class = None
        self._event_type = None
        self._event_source = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if event_id is not None:
            self.event_id = event_id
        if event_class is not None:
            self.event_class = event_class
        if event_type is not None:
            self.event_type = event_type
        if event_source is not None:
            self.event_source = event_source

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowHistoryTrafficEventsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this ShowHistoryTrafficEventsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowHistoryTrafficEventsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this ShowHistoryTrafficEventsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ShowHistoryTrafficEventsRequest.

        **参数说明**：分页查询时的页码。

        :return: The offset of this ShowHistoryTrafficEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowHistoryTrafficEventsRequest.

        **参数说明**：分页查询时的页码。

        :param offset: The offset of this ShowHistoryTrafficEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowHistoryTrafficEventsRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :return: The limit of this ShowHistoryTrafficEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowHistoryTrafficEventsRequest.

        **参数说明**：分页查询时每页显示的记录数。

        :param limit: The limit of this ShowHistoryTrafficEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def from_date(self):
        """Gets the from_date of this ShowHistoryTrafficEventsRequest.

        **参数说明**：查询此时间后达到平台的消息，十位Unix时间戳，秒级，例如：1575446506。

        :return: The from_date of this ShowHistoryTrafficEventsRequest.
        :rtype: int
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this ShowHistoryTrafficEventsRequest.

        **参数说明**：查询此时间后达到平台的消息，十位Unix时间戳，秒级，例如：1575446506。

        :param from_date: The from_date of this ShowHistoryTrafficEventsRequest.
        :type from_date: int
        """
        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this ShowHistoryTrafficEventsRequest.

        **参数说明**：查询此时间前达到平台的消息，十位Unix时间戳，秒级，例如：1576396905。

        :return: The to_date of this ShowHistoryTrafficEventsRequest.
        :rtype: int
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this ShowHistoryTrafficEventsRequest.

        **参数说明**：查询此时间前达到平台的消息，十位Unix时间戳，秒级，例如：1576396905。

        :param to_date: The to_date of this ShowHistoryTrafficEventsRequest.
        :type to_date: int
        """
        self._to_date = to_date

    @property
    def event_id(self):
        """Gets the event_id of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件id

        :return: The event_id of this ShowHistoryTrafficEventsRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件id

        :param event_id: The event_id of this ShowHistoryTrafficEventsRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_class(self):
        """Gets the event_class of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件的分类，event_type存在时，event_class必选。  **取值范围**：  - AbnormalTraffic：异常路况  - AbnormalVehicle：异常车况  - AdverseWeather：恶劣天气  - TrafficSign：标志标牌 

        :return: The event_class of this ShowHistoryTrafficEventsRequest.
        :rtype: str
        """
        return self._event_class

    @event_class.setter
    def event_class(self, event_class):
        """Sets the event_class of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件的分类，event_type存在时，event_class必选。  **取值范围**：  - AbnormalTraffic：异常路况  - AbnormalVehicle：异常车况  - AdverseWeather：恶劣天气  - TrafficSign：标志标牌 

        :param event_class: The event_class of this ShowHistoryTrafficEventsRequest.
        :type event_class: str
        """
        self._event_class = event_class

    @property
    def event_type(self):
        """Gets the event_type of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。

        :return: The event_type of this ShowHistoryTrafficEventsRequest.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。

        :param event_type: The event_type of this ShowHistoryTrafficEventsRequest.
        :type event_type: str
        """
        self._event_type = event_type

    @property
    def event_source(self):
        """Gets the event_source of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件来源，默认值v2xServer。  **取值范围**：  - v2xServer：来源为通过Console下发的事件  - detection：来源为边缘edge上报的RSI  - rsu：来源为通过MQTT接入的RSU上报的RSI 

        :return: The event_source of this ShowHistoryTrafficEventsRequest.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this ShowHistoryTrafficEventsRequest.

        **参数说明**：事件来源，默认值v2xServer。  **取值范围**：  - v2xServer：来源为通过Console下发的事件  - detection：来源为边缘edge上报的RSI  - rsu：来源为通过MQTT接入的RSU上报的RSI 

        :param event_source: The event_source of this ShowHistoryTrafficEventsRequest.
        :type event_source: str
        """
        self._event_source = event_source

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
        if not isinstance(other, ShowHistoryTrafficEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
