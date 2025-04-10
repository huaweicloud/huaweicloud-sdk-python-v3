# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImmediateEventResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time_stamp': 'datetime',
        'event_class': 'str',
        'event_type': 'int',
        'event_source': 'str',
        'event_source_id': 'str',
        'event_confidence': 'int',
        'event_position': 'ImmediateEventPosition3D',
        'event_radius': 'int',
        'event_description': 'str',
        'event_priority': 'int',
        'reference_paths': 'list[ImmediateEventReferencePath]'
    }

    attribute_map = {
        'time_stamp': 'time_stamp',
        'event_class': 'event_class',
        'event_type': 'event_type',
        'event_source': 'event_source',
        'event_source_id': 'event_source_id',
        'event_confidence': 'event_confidence',
        'event_position': 'event_position',
        'event_radius': 'event_radius',
        'event_description': 'event_description',
        'event_priority': 'event_priority',
        'reference_paths': 'reference_paths'
    }

    def __init__(self, time_stamp=None, event_class=None, event_type=None, event_source=None, event_source_id=None, event_confidence=None, event_position=None, event_radius=None, event_description=None, event_priority=None, reference_paths=None):
        r"""ImmediateEventResponseDTO

        The model defined in huaweicloud sdk

        :param time_stamp: **参数说明**：事件发生时间，毫秒级。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss.SSS&#39;&#39;Z&#39;&#39;  例如 2015-12-12T12:12:12.356Z。
        :type time_stamp: datetime
        :param event_class: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。
        :type event_class: str
        :param event_type: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件
        :type event_type: int
        :param event_source: **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据
        :type event_source: str
        :param event_source_id: **参数说明**：事件来源的ID，由用户自定义。
        :type event_source_id: str
        :param event_confidence: **参数说明**：道路交通事件的信息来源提供的事件置信度水平，帮助接收端判断是否相信该事件信息，可选。
        :type event_confidence: int
        :param event_position: 
        :type event_position: :class:`huaweicloudsdkdris.v1.ImmediateEventPosition3D`
        :param event_radius: **参数说明**：事件的发生区域半径，单位为分米。
        :type event_radius: int
        :param event_description: **参数说明**：事件的文本描述信息,可自行扩展需传递的信息。
        :type event_description: str
        :param event_priority: **参数说明**：事件优先级，0-7，数字越大，级别越高。
        :type event_priority: int
        :param reference_paths: **参数说明**：事件生效的关联路径。
        :type reference_paths: list[:class:`huaweicloudsdkdris.v1.ImmediateEventReferencePath`]
        """
        
        

        self._time_stamp = None
        self._event_class = None
        self._event_type = None
        self._event_source = None
        self._event_source_id = None
        self._event_confidence = None
        self._event_position = None
        self._event_radius = None
        self._event_description = None
        self._event_priority = None
        self._reference_paths = None
        self.discriminator = None

        if time_stamp is not None:
            self.time_stamp = time_stamp
        if event_class is not None:
            self.event_class = event_class
        if event_type is not None:
            self.event_type = event_type
        if event_source is not None:
            self.event_source = event_source
        if event_source_id is not None:
            self.event_source_id = event_source_id
        if event_confidence is not None:
            self.event_confidence = event_confidence
        if event_position is not None:
            self.event_position = event_position
        if event_radius is not None:
            self.event_radius = event_radius
        if event_description is not None:
            self.event_description = event_description
        if event_priority is not None:
            self.event_priority = event_priority
        if reference_paths is not None:
            self.reference_paths = reference_paths

    @property
    def time_stamp(self):
        r"""Gets the time_stamp of this ImmediateEventResponseDTO.

        **参数说明**：事件发生时间，毫秒级。  格式：yyyy-MM-dd''T''HH:mm:ss.SSS''Z''  例如 2015-12-12T12:12:12.356Z。

        :return: The time_stamp of this ImmediateEventResponseDTO.
        :rtype: datetime
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        r"""Sets the time_stamp of this ImmediateEventResponseDTO.

        **参数说明**：事件发生时间，毫秒级。  格式：yyyy-MM-dd''T''HH:mm:ss.SSS''Z''  例如 2015-12-12T12:12:12.356Z。

        :param time_stamp: The time_stamp of this ImmediateEventResponseDTO.
        :type time_stamp: datetime
        """
        self._time_stamp = time_stamp

    @property
    def event_class(self):
        r"""Gets the event_class of this ImmediateEventResponseDTO.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :return: The event_class of this ImmediateEventResponseDTO.
        :rtype: str
        """
        return self._event_class

    @event_class.setter
    def event_class(self, event_class):
        r"""Sets the event_class of this ImmediateEventResponseDTO.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :param event_class: The event_class of this ImmediateEventResponseDTO.
        :type event_class: str
        """
        self._event_class = event_class

    @property
    def event_type(self):
        r"""Gets the event_type of this ImmediateEventResponseDTO.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件

        :return: The event_type of this ImmediateEventResponseDTO.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ImmediateEventResponseDTO.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件

        :param event_type: The event_type of this ImmediateEventResponseDTO.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_source(self):
        r"""Gets the event_source of this ImmediateEventResponseDTO.

        **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据

        :return: The event_source of this ImmediateEventResponseDTO.
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        r"""Sets the event_source of this ImmediateEventResponseDTO.

        **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据

        :param event_source: The event_source of this ImmediateEventResponseDTO.
        :type event_source: str
        """
        self._event_source = event_source

    @property
    def event_source_id(self):
        r"""Gets the event_source_id of this ImmediateEventResponseDTO.

        **参数说明**：事件来源的ID，由用户自定义。

        :return: The event_source_id of this ImmediateEventResponseDTO.
        :rtype: str
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        r"""Sets the event_source_id of this ImmediateEventResponseDTO.

        **参数说明**：事件来源的ID，由用户自定义。

        :param event_source_id: The event_source_id of this ImmediateEventResponseDTO.
        :type event_source_id: str
        """
        self._event_source_id = event_source_id

    @property
    def event_confidence(self):
        r"""Gets the event_confidence of this ImmediateEventResponseDTO.

        **参数说明**：道路交通事件的信息来源提供的事件置信度水平，帮助接收端判断是否相信该事件信息，可选。

        :return: The event_confidence of this ImmediateEventResponseDTO.
        :rtype: int
        """
        return self._event_confidence

    @event_confidence.setter
    def event_confidence(self, event_confidence):
        r"""Sets the event_confidence of this ImmediateEventResponseDTO.

        **参数说明**：道路交通事件的信息来源提供的事件置信度水平，帮助接收端判断是否相信该事件信息，可选。

        :param event_confidence: The event_confidence of this ImmediateEventResponseDTO.
        :type event_confidence: int
        """
        self._event_confidence = event_confidence

    @property
    def event_position(self):
        r"""Gets the event_position of this ImmediateEventResponseDTO.

        :return: The event_position of this ImmediateEventResponseDTO.
        :rtype: :class:`huaweicloudsdkdris.v1.ImmediateEventPosition3D`
        """
        return self._event_position

    @event_position.setter
    def event_position(self, event_position):
        r"""Sets the event_position of this ImmediateEventResponseDTO.

        :param event_position: The event_position of this ImmediateEventResponseDTO.
        :type event_position: :class:`huaweicloudsdkdris.v1.ImmediateEventPosition3D`
        """
        self._event_position = event_position

    @property
    def event_radius(self):
        r"""Gets the event_radius of this ImmediateEventResponseDTO.

        **参数说明**：事件的发生区域半径，单位为分米。

        :return: The event_radius of this ImmediateEventResponseDTO.
        :rtype: int
        """
        return self._event_radius

    @event_radius.setter
    def event_radius(self, event_radius):
        r"""Sets the event_radius of this ImmediateEventResponseDTO.

        **参数说明**：事件的发生区域半径，单位为分米。

        :param event_radius: The event_radius of this ImmediateEventResponseDTO.
        :type event_radius: int
        """
        self._event_radius = event_radius

    @property
    def event_description(self):
        r"""Gets the event_description of this ImmediateEventResponseDTO.

        **参数说明**：事件的文本描述信息,可自行扩展需传递的信息。

        :return: The event_description of this ImmediateEventResponseDTO.
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        r"""Sets the event_description of this ImmediateEventResponseDTO.

        **参数说明**：事件的文本描述信息,可自行扩展需传递的信息。

        :param event_description: The event_description of this ImmediateEventResponseDTO.
        :type event_description: str
        """
        self._event_description = event_description

    @property
    def event_priority(self):
        r"""Gets the event_priority of this ImmediateEventResponseDTO.

        **参数说明**：事件优先级，0-7，数字越大，级别越高。

        :return: The event_priority of this ImmediateEventResponseDTO.
        :rtype: int
        """
        return self._event_priority

    @event_priority.setter
    def event_priority(self, event_priority):
        r"""Sets the event_priority of this ImmediateEventResponseDTO.

        **参数说明**：事件优先级，0-7，数字越大，级别越高。

        :param event_priority: The event_priority of this ImmediateEventResponseDTO.
        :type event_priority: int
        """
        self._event_priority = event_priority

    @property
    def reference_paths(self):
        r"""Gets the reference_paths of this ImmediateEventResponseDTO.

        **参数说明**：事件生效的关联路径。

        :return: The reference_paths of this ImmediateEventResponseDTO.
        :rtype: list[:class:`huaweicloudsdkdris.v1.ImmediateEventReferencePath`]
        """
        return self._reference_paths

    @reference_paths.setter
    def reference_paths(self, reference_paths):
        r"""Sets the reference_paths of this ImmediateEventResponseDTO.

        **参数说明**：事件生效的关联路径。

        :param reference_paths: The reference_paths of this ImmediateEventResponseDTO.
        :type reference_paths: list[:class:`huaweicloudsdkdris.v1.ImmediateEventReferencePath`]
        """
        self._reference_paths = reference_paths

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
        if not isinstance(other, ImmediateEventResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
