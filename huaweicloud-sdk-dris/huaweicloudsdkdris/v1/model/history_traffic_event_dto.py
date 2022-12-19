# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HistoryTrafficEventDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'event_id': 'str',
        'event_source_type': 'str',
        'event_source_id': 'str',
        'area_code': 'int',
        'event_class': 'str',
        'event_type': 'int',
        'cross_id': 'str',
        'event_description': 'str',
        'event_level': 'int',
        'event_params': 'dict(str, str)',
        'event_position': 'Position3D',
        'event_position_name': 'str',
        'reference_paths': 'list[ReferencePath]',
        'note': 'str',
        'event_status': 'str',
        'event_confidence': 'int',
        'event_ex_info': 'EventExInfo',
        'rsu_id': 'list[str]',
        'start_time': 'str',
        'end_time': 'str',
        'created_time': 'str'
    }

    attribute_map = {
        'event_id': 'event_id',
        'event_source_type': 'event_source_type',
        'event_source_id': 'event_source_id',
        'area_code': 'area_code',
        'event_class': 'event_class',
        'event_type': 'event_type',
        'cross_id': 'cross_id',
        'event_description': 'event_description',
        'event_level': 'event_level',
        'event_params': 'event_params',
        'event_position': 'event_position',
        'event_position_name': 'event_position_name',
        'reference_paths': 'reference_paths',
        'note': 'note',
        'event_status': 'event_status',
        'event_confidence': 'event_confidence',
        'event_ex_info': 'event_ex_info',
        'rsu_id': 'rsu_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'created_time': 'created_time'
    }

    def __init__(self, event_id=None, event_source_type=None, event_source_id=None, area_code=None, event_class=None, event_type=None, cross_id=None, event_description=None, event_level=None, event_params=None, event_position=None, event_position_name=None, reference_paths=None, note=None, event_status=None, event_confidence=None, event_ex_info=None, rsu_id=None, start_time=None, end_time=None, created_time=None):
        """HistoryTrafficEventDTO

        The model defined in huaweicloud sdk

        :param event_id: **参数说明**：事件ID，由平台生成。
        :type event_id: str
        :param event_source_type:  **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 
        :type event_source_type: str
        :param event_source_id: **参数说明**：事件来源ID。
        :type event_source_id: str
        :param area_code: **参数说明**：区域码。
        :type area_code: int
        :param event_class: **参数说明**：事件的分类。  **取值范围**：  - AbnormalTraffic：异常路况  - AbnormalVehicle：异常车况  - AdverseWeather：恶劣天气  - TrafficSign：标志标牌 
        :type event_class: str
        :param event_type: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。
        :type event_type: int
        :param cross_id: **参数说明**：路口id，对应到一组雷视拟合设备，检测一个特定的路口或者路段。
        :type cross_id: str
        :param event_description: **参数说明**：交通事件描述。
        :type event_description: str
        :param event_level: **参数说明**：事件级别(1-5) 由低到高的事件严重程度。
        :type event_level: int
        :param event_params: **参数说明**：事件参数，用户自定义。
        :type event_params: dict(str, str)
        :param event_position: 
        :type event_position: :class:`huaweicloudsdkdris.v1.Position3D`
        :param event_position_name: **参数说明**：事件位置名称。
        :type event_position_name: str
        :param reference_paths: **参数说明**：事件的关联路径。
        :type reference_paths: list[:class:`huaweicloudsdkdris.v1.ReferencePath`]
        :param note: **参数说明**：用户备注信息。
        :type note: str
        :param event_status: **参数说明**：事件的状态。  **取值范围**：  - Invalid：过期事件，事件发生的时间段在当前时间之前。  - Active：活动事件，事件正在发生，当前时间处于事件发生时间段内。  - Future：未来事件，在当前时间之后才会发生的事件。 
        :type event_status: str
        :param event_confidence: **参数说明**：事件可信度。
        :type event_confidence: int
        :param event_ex_info: 
        :type event_ex_info: :class:`huaweicloudsdkdris.v1.EventExInfo`
        :param rsu_id: **参数说明**：事件关联的rsuID。
        :type rsu_id: list[str]
        :param start_time: **参数说明**：事件的开始时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。 
        :type start_time: str
        :param end_time: **参数说明**：事件的结束时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。 
        :type end_time: str
        :param created_time: **参数说明**：事件的创建时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。 
        :type created_time: str
        """
        
        

        self._event_id = None
        self._event_source_type = None
        self._event_source_id = None
        self._area_code = None
        self._event_class = None
        self._event_type = None
        self._cross_id = None
        self._event_description = None
        self._event_level = None
        self._event_params = None
        self._event_position = None
        self._event_position_name = None
        self._reference_paths = None
        self._note = None
        self._event_status = None
        self._event_confidence = None
        self._event_ex_info = None
        self._rsu_id = None
        self._start_time = None
        self._end_time = None
        self._created_time = None
        self.discriminator = None

        if event_id is not None:
            self.event_id = event_id
        if event_source_type is not None:
            self.event_source_type = event_source_type
        if event_source_id is not None:
            self.event_source_id = event_source_id
        if area_code is not None:
            self.area_code = area_code
        if event_class is not None:
            self.event_class = event_class
        if event_type is not None:
            self.event_type = event_type
        if cross_id is not None:
            self.cross_id = cross_id
        if event_description is not None:
            self.event_description = event_description
        if event_level is not None:
            self.event_level = event_level
        if event_params is not None:
            self.event_params = event_params
        if event_position is not None:
            self.event_position = event_position
        if event_position_name is not None:
            self.event_position_name = event_position_name
        if reference_paths is not None:
            self.reference_paths = reference_paths
        if note is not None:
            self.note = note
        if event_status is not None:
            self.event_status = event_status
        if event_confidence is not None:
            self.event_confidence = event_confidence
        if event_ex_info is not None:
            self.event_ex_info = event_ex_info
        if rsu_id is not None:
            self.rsu_id = rsu_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if created_time is not None:
            self.created_time = created_time

    @property
    def event_id(self):
        """Gets the event_id of this HistoryTrafficEventDTO.

        **参数说明**：事件ID，由平台生成。

        :return: The event_id of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this HistoryTrafficEventDTO.

        **参数说明**：事件ID，由平台生成。

        :param event_id: The event_id of this HistoryTrafficEventDTO.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_source_type(self):
        """Gets the event_source_type of this HistoryTrafficEventDTO.

         **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 

        :return: The event_source_type of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._event_source_type

    @event_source_type.setter
    def event_source_type(self, event_source_type):
        """Sets the event_source_type of this HistoryTrafficEventDTO.

         **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 

        :param event_source_type: The event_source_type of this HistoryTrafficEventDTO.
        :type event_source_type: str
        """
        self._event_source_type = event_source_type

    @property
    def event_source_id(self):
        """Gets the event_source_id of this HistoryTrafficEventDTO.

        **参数说明**：事件来源ID。

        :return: The event_source_id of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        """Sets the event_source_id of this HistoryTrafficEventDTO.

        **参数说明**：事件来源ID。

        :param event_source_id: The event_source_id of this HistoryTrafficEventDTO.
        :type event_source_id: str
        """
        self._event_source_id = event_source_id

    @property
    def area_code(self):
        """Gets the area_code of this HistoryTrafficEventDTO.

        **参数说明**：区域码。

        :return: The area_code of this HistoryTrafficEventDTO.
        :rtype: int
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this HistoryTrafficEventDTO.

        **参数说明**：区域码。

        :param area_code: The area_code of this HistoryTrafficEventDTO.
        :type area_code: int
        """
        self._area_code = area_code

    @property
    def event_class(self):
        """Gets the event_class of this HistoryTrafficEventDTO.

        **参数说明**：事件的分类。  **取值范围**：  - AbnormalTraffic：异常路况  - AbnormalVehicle：异常车况  - AdverseWeather：恶劣天气  - TrafficSign：标志标牌 

        :return: The event_class of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._event_class

    @event_class.setter
    def event_class(self, event_class):
        """Sets the event_class of this HistoryTrafficEventDTO.

        **参数说明**：事件的分类。  **取值范围**：  - AbnormalTraffic：异常路况  - AbnormalVehicle：异常车况  - AdverseWeather：恶劣天气  - TrafficSign：标志标牌 

        :param event_class: The event_class of this HistoryTrafficEventDTO.
        :type event_class: str
        """
        self._event_class = event_class

    @property
    def event_type(self):
        """Gets the event_type of this HistoryTrafficEventDTO.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。

        :return: The event_type of this HistoryTrafficEventDTO.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this HistoryTrafficEventDTO.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。

        :param event_type: The event_type of this HistoryTrafficEventDTO.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def cross_id(self):
        """Gets the cross_id of this HistoryTrafficEventDTO.

        **参数说明**：路口id，对应到一组雷视拟合设备，检测一个特定的路口或者路段。

        :return: The cross_id of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._cross_id

    @cross_id.setter
    def cross_id(self, cross_id):
        """Sets the cross_id of this HistoryTrafficEventDTO.

        **参数说明**：路口id，对应到一组雷视拟合设备，检测一个特定的路口或者路段。

        :param cross_id: The cross_id of this HistoryTrafficEventDTO.
        :type cross_id: str
        """
        self._cross_id = cross_id

    @property
    def event_description(self):
        """Gets the event_description of this HistoryTrafficEventDTO.

        **参数说明**：交通事件描述。

        :return: The event_description of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        """Sets the event_description of this HistoryTrafficEventDTO.

        **参数说明**：交通事件描述。

        :param event_description: The event_description of this HistoryTrafficEventDTO.
        :type event_description: str
        """
        self._event_description = event_description

    @property
    def event_level(self):
        """Gets the event_level of this HistoryTrafficEventDTO.

        **参数说明**：事件级别(1-5) 由低到高的事件严重程度。

        :return: The event_level of this HistoryTrafficEventDTO.
        :rtype: int
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        """Sets the event_level of this HistoryTrafficEventDTO.

        **参数说明**：事件级别(1-5) 由低到高的事件严重程度。

        :param event_level: The event_level of this HistoryTrafficEventDTO.
        :type event_level: int
        """
        self._event_level = event_level

    @property
    def event_params(self):
        """Gets the event_params of this HistoryTrafficEventDTO.

        **参数说明**：事件参数，用户自定义。

        :return: The event_params of this HistoryTrafficEventDTO.
        :rtype: dict(str, str)
        """
        return self._event_params

    @event_params.setter
    def event_params(self, event_params):
        """Sets the event_params of this HistoryTrafficEventDTO.

        **参数说明**：事件参数，用户自定义。

        :param event_params: The event_params of this HistoryTrafficEventDTO.
        :type event_params: dict(str, str)
        """
        self._event_params = event_params

    @property
    def event_position(self):
        """Gets the event_position of this HistoryTrafficEventDTO.

        :return: The event_position of this HistoryTrafficEventDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.Position3D`
        """
        return self._event_position

    @event_position.setter
    def event_position(self, event_position):
        """Sets the event_position of this HistoryTrafficEventDTO.

        :param event_position: The event_position of this HistoryTrafficEventDTO.
        :type event_position: :class:`huaweicloudsdkdris.v1.Position3D`
        """
        self._event_position = event_position

    @property
    def event_position_name(self):
        """Gets the event_position_name of this HistoryTrafficEventDTO.

        **参数说明**：事件位置名称。

        :return: The event_position_name of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._event_position_name

    @event_position_name.setter
    def event_position_name(self, event_position_name):
        """Sets the event_position_name of this HistoryTrafficEventDTO.

        **参数说明**：事件位置名称。

        :param event_position_name: The event_position_name of this HistoryTrafficEventDTO.
        :type event_position_name: str
        """
        self._event_position_name = event_position_name

    @property
    def reference_paths(self):
        """Gets the reference_paths of this HistoryTrafficEventDTO.

        **参数说明**：事件的关联路径。

        :return: The reference_paths of this HistoryTrafficEventDTO.
        :rtype: list[:class:`huaweicloudsdkdris.v1.ReferencePath`]
        """
        return self._reference_paths

    @reference_paths.setter
    def reference_paths(self, reference_paths):
        """Sets the reference_paths of this HistoryTrafficEventDTO.

        **参数说明**：事件的关联路径。

        :param reference_paths: The reference_paths of this HistoryTrafficEventDTO.
        :type reference_paths: list[:class:`huaweicloudsdkdris.v1.ReferencePath`]
        """
        self._reference_paths = reference_paths

    @property
    def note(self):
        """Gets the note of this HistoryTrafficEventDTO.

        **参数说明**：用户备注信息。

        :return: The note of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this HistoryTrafficEventDTO.

        **参数说明**：用户备注信息。

        :param note: The note of this HistoryTrafficEventDTO.
        :type note: str
        """
        self._note = note

    @property
    def event_status(self):
        """Gets the event_status of this HistoryTrafficEventDTO.

        **参数说明**：事件的状态。  **取值范围**：  - Invalid：过期事件，事件发生的时间段在当前时间之前。  - Active：活动事件，事件正在发生，当前时间处于事件发生时间段内。  - Future：未来事件，在当前时间之后才会发生的事件。 

        :return: The event_status of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._event_status

    @event_status.setter
    def event_status(self, event_status):
        """Sets the event_status of this HistoryTrafficEventDTO.

        **参数说明**：事件的状态。  **取值范围**：  - Invalid：过期事件，事件发生的时间段在当前时间之前。  - Active：活动事件，事件正在发生，当前时间处于事件发生时间段内。  - Future：未来事件，在当前时间之后才会发生的事件。 

        :param event_status: The event_status of this HistoryTrafficEventDTO.
        :type event_status: str
        """
        self._event_status = event_status

    @property
    def event_confidence(self):
        """Gets the event_confidence of this HistoryTrafficEventDTO.

        **参数说明**：事件可信度。

        :return: The event_confidence of this HistoryTrafficEventDTO.
        :rtype: int
        """
        return self._event_confidence

    @event_confidence.setter
    def event_confidence(self, event_confidence):
        """Sets the event_confidence of this HistoryTrafficEventDTO.

        **参数说明**：事件可信度。

        :param event_confidence: The event_confidence of this HistoryTrafficEventDTO.
        :type event_confidence: int
        """
        self._event_confidence = event_confidence

    @property
    def event_ex_info(self):
        """Gets the event_ex_info of this HistoryTrafficEventDTO.

        :return: The event_ex_info of this HistoryTrafficEventDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.EventExInfo`
        """
        return self._event_ex_info

    @event_ex_info.setter
    def event_ex_info(self, event_ex_info):
        """Sets the event_ex_info of this HistoryTrafficEventDTO.

        :param event_ex_info: The event_ex_info of this HistoryTrafficEventDTO.
        :type event_ex_info: :class:`huaweicloudsdkdris.v1.EventExInfo`
        """
        self._event_ex_info = event_ex_info

    @property
    def rsu_id(self):
        """Gets the rsu_id of this HistoryTrafficEventDTO.

        **参数说明**：事件关联的rsuID。

        :return: The rsu_id of this HistoryTrafficEventDTO.
        :rtype: list[str]
        """
        return self._rsu_id

    @rsu_id.setter
    def rsu_id(self, rsu_id):
        """Sets the rsu_id of this HistoryTrafficEventDTO.

        **参数说明**：事件关联的rsuID。

        :param rsu_id: The rsu_id of this HistoryTrafficEventDTO.
        :type rsu_id: list[str]
        """
        self._rsu_id = rsu_id

    @property
    def start_time(self):
        """Gets the start_time of this HistoryTrafficEventDTO.

        **参数说明**：事件的开始时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :return: The start_time of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this HistoryTrafficEventDTO.

        **参数说明**：事件的开始时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :param start_time: The start_time of this HistoryTrafficEventDTO.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this HistoryTrafficEventDTO.

        **参数说明**：事件的结束时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :return: The end_time of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this HistoryTrafficEventDTO.

        **参数说明**：事件的结束时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :param end_time: The end_time of this HistoryTrafficEventDTO.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def created_time(self):
        """Gets the created_time of this HistoryTrafficEventDTO.

        **参数说明**：事件的创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :return: The created_time of this HistoryTrafficEventDTO.
        :rtype: str
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this HistoryTrafficEventDTO.

        **参数说明**：事件的创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :param created_time: The created_time of this HistoryTrafficEventDTO.
        :type created_time: str
        """
        self._created_time = created_time

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
        if not isinstance(other, HistoryTrafficEventDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
