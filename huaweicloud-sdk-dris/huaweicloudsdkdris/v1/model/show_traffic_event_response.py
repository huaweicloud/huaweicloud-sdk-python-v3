# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTrafficEventResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'event_id': 'str',
        'event_source_type': 'str',
        'event_source_id': 'str',
        'event_class': 'str',
        'event_type': 'int',
        'area_code': 'int',
        'event_level': 'int',
        'event_params': 'dict(str, str)',
        'event_position': 'EventLocation',
        'event_description': 'str',
        'reference_paths': 'list[EventReferencePath]',
        'event_position_name': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'note': 'str',
        'event_confidence': 'int',
        'created_time': 'datetime',
        'last_modified_time': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'event_id': 'event_id',
        'event_source_type': 'event_source_type',
        'event_source_id': 'event_source_id',
        'event_class': 'event_class',
        'event_type': 'event_type',
        'area_code': 'area_code',
        'event_level': 'event_level',
        'event_params': 'event_params',
        'event_position': 'event_position',
        'event_description': 'event_description',
        'reference_paths': 'reference_paths',
        'event_position_name': 'event_position_name',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'note': 'note',
        'event_confidence': 'event_confidence',
        'created_time': 'created_time',
        'last_modified_time': 'last_modified_time'
    }

    def __init__(self, status=None, event_id=None, event_source_type=None, event_source_id=None, event_class=None, event_type=None, area_code=None, event_level=None, event_params=None, event_position=None, event_description=None, reference_paths=None, event_position_name=None, start_time=None, end_time=None, note=None, event_confidence=None, created_time=None, last_modified_time=None):
        r"""ShowTrafficEventResponse

        The model defined in huaweicloud sdk

        :param status:  **参数说明**：事件状态。  **取值范围**：  - Invalid：为过期事件，事件结束时间（end_time）在当前时间之前。  - Active：为活动事件，事件开始时间（start_time）在当前时间之前，并且事件结束时间（end_time）在当前时间之后。  - Future：为未来事件，事件开始时间（start_time）在当前时间之前。 
        :type status: str
        :param event_id: **参数说明**：事件ID，创建事件后获得。方法参见 [新增交通事件](https://support.huaweicloud.com/api-v2x/v2x_04_0048.html)。
        :type event_id: str
        :param event_source_type:  **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 
        :type event_source_type: str
        :param event_source_id: **参数说明**：事件来源的ID，由用户自定义。
        :type event_source_id: str
        :param event_class: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。
        :type event_class: str
        :param event_type: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。
        :type event_type: int
        :param area_code: **参数说明**：区域码，参考[区域码查询](http://xzqh.mca.gov.cn/map)。
        :type area_code: int
        :param event_level: **参数说明**：事件优先级，0-7越大优先级越高。
        :type event_level: int
        :param event_params:  **参数说明**：事件附加信息。  事件类型为如下数据时生效：  - 道路最高限：必选，设置最高限速（整数值）km/h  - 道路最低限速：必选，设置最低限速（整数值）km/h  - 建议速度：必选，建议速度（整数值）km/h  - 急弯路：可选，建议最高限速（整数值）km/h  - 雨：可选，请输入1~4：1-细雨，2-小雨，3-中雨，4-大雨  - 雪：可选，请输入1~4：1-小雪，2-中雪，3-大雪，4-暴雪  - 风：可选，设置风速值（整数值）km/h  - 雾：可选，请输入1或2：1-薄雾，2-浓雾  - 路面湿滑：可选，设置湿滑系数（0~1）  - 路面结冰：可选，请设置冰层厚度（整数值）mm  建议填写方式为：user_defined_param1: \&quot;xx\&quot; 
        :type event_params: dict(str, str)
        :param event_position: 
        :type event_position: :class:`huaweicloudsdkdris.v1.EventLocation`
        :param event_description: **参数说明**：事件描述。支持英文字母、数字、下划线、斜杠、中文及中文常用字符：。 ？ ！ ， 、 ； ： “ ”
        :type event_description: str
        :param reference_paths: **参数说明**：事件生效的关联路径，至少需写入起始和终止位置的两个坐标点。
        :type reference_paths: list[:class:`huaweicloudsdkdris.v1.EventReferencePath`]
        :param event_position_name: **参数说明**：事件所在位置。
        :type event_position_name: str
        :param start_time: **参数说明**：开始时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。 
        :type start_time: datetime
        :param end_time: **参数说明**：结束时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。 
        :type end_time: datetime
        :param note: **参数说明**：备注。
        :type note: str
        :param event_confidence: **参数说明**：事件可信度。
        :type event_confidence: int
        :param created_time: &#39;**参数说明**：创建时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。 
        :type created_time: datetime
        :param last_modified_time: **参数说明**：最后修改的时间。  格式：yyyy-MM-dd&#39;&#39;T&#39;&#39;HH:mm:ss&#39;&#39;Z&#39;&#39;。  例如 2020-09-01T01:37:01Z。 
        :type last_modified_time: datetime
        """
        
        super(ShowTrafficEventResponse, self).__init__()

        self._status = None
        self._event_id = None
        self._event_source_type = None
        self._event_source_id = None
        self._event_class = None
        self._event_type = None
        self._area_code = None
        self._event_level = None
        self._event_params = None
        self._event_position = None
        self._event_description = None
        self._reference_paths = None
        self._event_position_name = None
        self._start_time = None
        self._end_time = None
        self._note = None
        self._event_confidence = None
        self._created_time = None
        self._last_modified_time = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if event_id is not None:
            self.event_id = event_id
        if event_source_type is not None:
            self.event_source_type = event_source_type
        if event_source_id is not None:
            self.event_source_id = event_source_id
        if event_class is not None:
            self.event_class = event_class
        if event_type is not None:
            self.event_type = event_type
        if area_code is not None:
            self.area_code = area_code
        if event_level is not None:
            self.event_level = event_level
        if event_params is not None:
            self.event_params = event_params
        if event_position is not None:
            self.event_position = event_position
        if event_description is not None:
            self.event_description = event_description
        if reference_paths is not None:
            self.reference_paths = reference_paths
        if event_position_name is not None:
            self.event_position_name = event_position_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if note is not None:
            self.note = note
        if event_confidence is not None:
            self.event_confidence = event_confidence
        if created_time is not None:
            self.created_time = created_time
        if last_modified_time is not None:
            self.last_modified_time = last_modified_time

    @property
    def status(self):
        r"""Gets the status of this ShowTrafficEventResponse.

         **参数说明**：事件状态。  **取值范围**：  - Invalid：为过期事件，事件结束时间（end_time）在当前时间之前。  - Active：为活动事件，事件开始时间（start_time）在当前时间之前，并且事件结束时间（end_time）在当前时间之后。  - Future：为未来事件，事件开始时间（start_time）在当前时间之前。 

        :return: The status of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTrafficEventResponse.

         **参数说明**：事件状态。  **取值范围**：  - Invalid：为过期事件，事件结束时间（end_time）在当前时间之前。  - Active：为活动事件，事件开始时间（start_time）在当前时间之前，并且事件结束时间（end_time）在当前时间之后。  - Future：为未来事件，事件开始时间（start_time）在当前时间之前。 

        :param status: The status of this ShowTrafficEventResponse.
        :type status: str
        """
        self._status = status

    @property
    def event_id(self):
        r"""Gets the event_id of this ShowTrafficEventResponse.

        **参数说明**：事件ID，创建事件后获得。方法参见 [新增交通事件](https://support.huaweicloud.com/api-v2x/v2x_04_0048.html)。

        :return: The event_id of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        r"""Sets the event_id of this ShowTrafficEventResponse.

        **参数说明**：事件ID，创建事件后获得。方法参见 [新增交通事件](https://support.huaweicloud.com/api-v2x/v2x_04_0048.html)。

        :param event_id: The event_id of this ShowTrafficEventResponse.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def event_source_type(self):
        r"""Gets the event_source_type of this ShowTrafficEventResponse.

         **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 

        :return: The event_source_type of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._event_source_type

    @event_source_type.setter
    def event_source_type(self, event_source_type):
        r"""Sets the event_source_type of this ShowTrafficEventResponse.

         **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 

        :param event_source_type: The event_source_type of this ShowTrafficEventResponse.
        :type event_source_type: str
        """
        self._event_source_type = event_source_type

    @property
    def event_source_id(self):
        r"""Gets the event_source_id of this ShowTrafficEventResponse.

        **参数说明**：事件来源的ID，由用户自定义。

        :return: The event_source_id of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._event_source_id

    @event_source_id.setter
    def event_source_id(self, event_source_id):
        r"""Sets the event_source_id of this ShowTrafficEventResponse.

        **参数说明**：事件来源的ID，由用户自定义。

        :param event_source_id: The event_source_id of this ShowTrafficEventResponse.
        :type event_source_id: str
        """
        self._event_source_id = event_source_id

    @property
    def event_class(self):
        r"""Gets the event_class of this ShowTrafficEventResponse.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :return: The event_class of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._event_class

    @event_class.setter
    def event_class(self, event_class):
        r"""Sets the event_class of this ShowTrafficEventResponse.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :param event_class: The event_class of this ShowTrafficEventResponse.
        :type event_class: str
        """
        self._event_class = event_class

    @property
    def event_type(self):
        r"""Gets the event_type of this ShowTrafficEventResponse.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。

        :return: The event_type of this ShowTrafficEventResponse.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        r"""Sets the event_type of this ShowTrafficEventResponse.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。

        :param event_type: The event_type of this ShowTrafficEventResponse.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def area_code(self):
        r"""Gets the area_code of this ShowTrafficEventResponse.

        **参数说明**：区域码，参考[区域码查询](http://xzqh.mca.gov.cn/map)。

        :return: The area_code of this ShowTrafficEventResponse.
        :rtype: int
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        r"""Sets the area_code of this ShowTrafficEventResponse.

        **参数说明**：区域码，参考[区域码查询](http://xzqh.mca.gov.cn/map)。

        :param area_code: The area_code of this ShowTrafficEventResponse.
        :type area_code: int
        """
        self._area_code = area_code

    @property
    def event_level(self):
        r"""Gets the event_level of this ShowTrafficEventResponse.

        **参数说明**：事件优先级，0-7越大优先级越高。

        :return: The event_level of this ShowTrafficEventResponse.
        :rtype: int
        """
        return self._event_level

    @event_level.setter
    def event_level(self, event_level):
        r"""Sets the event_level of this ShowTrafficEventResponse.

        **参数说明**：事件优先级，0-7越大优先级越高。

        :param event_level: The event_level of this ShowTrafficEventResponse.
        :type event_level: int
        """
        self._event_level = event_level

    @property
    def event_params(self):
        r"""Gets the event_params of this ShowTrafficEventResponse.

         **参数说明**：事件附加信息。  事件类型为如下数据时生效：  - 道路最高限：必选，设置最高限速（整数值）km/h  - 道路最低限速：必选，设置最低限速（整数值）km/h  - 建议速度：必选，建议速度（整数值）km/h  - 急弯路：可选，建议最高限速（整数值）km/h  - 雨：可选，请输入1~4：1-细雨，2-小雨，3-中雨，4-大雨  - 雪：可选，请输入1~4：1-小雪，2-中雪，3-大雪，4-暴雪  - 风：可选，设置风速值（整数值）km/h  - 雾：可选，请输入1或2：1-薄雾，2-浓雾  - 路面湿滑：可选，设置湿滑系数（0~1）  - 路面结冰：可选，请设置冰层厚度（整数值）mm  建议填写方式为：user_defined_param1: \"xx\" 

        :return: The event_params of this ShowTrafficEventResponse.
        :rtype: dict(str, str)
        """
        return self._event_params

    @event_params.setter
    def event_params(self, event_params):
        r"""Sets the event_params of this ShowTrafficEventResponse.

         **参数说明**：事件附加信息。  事件类型为如下数据时生效：  - 道路最高限：必选，设置最高限速（整数值）km/h  - 道路最低限速：必选，设置最低限速（整数值）km/h  - 建议速度：必选，建议速度（整数值）km/h  - 急弯路：可选，建议最高限速（整数值）km/h  - 雨：可选，请输入1~4：1-细雨，2-小雨，3-中雨，4-大雨  - 雪：可选，请输入1~4：1-小雪，2-中雪，3-大雪，4-暴雪  - 风：可选，设置风速值（整数值）km/h  - 雾：可选，请输入1或2：1-薄雾，2-浓雾  - 路面湿滑：可选，设置湿滑系数（0~1）  - 路面结冰：可选，请设置冰层厚度（整数值）mm  建议填写方式为：user_defined_param1: \"xx\" 

        :param event_params: The event_params of this ShowTrafficEventResponse.
        :type event_params: dict(str, str)
        """
        self._event_params = event_params

    @property
    def event_position(self):
        r"""Gets the event_position of this ShowTrafficEventResponse.

        :return: The event_position of this ShowTrafficEventResponse.
        :rtype: :class:`huaweicloudsdkdris.v1.EventLocation`
        """
        return self._event_position

    @event_position.setter
    def event_position(self, event_position):
        r"""Sets the event_position of this ShowTrafficEventResponse.

        :param event_position: The event_position of this ShowTrafficEventResponse.
        :type event_position: :class:`huaweicloudsdkdris.v1.EventLocation`
        """
        self._event_position = event_position

    @property
    def event_description(self):
        r"""Gets the event_description of this ShowTrafficEventResponse.

        **参数说明**：事件描述。支持英文字母、数字、下划线、斜杠、中文及中文常用字符：。 ？ ！ ， 、 ； ： “ ”

        :return: The event_description of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._event_description

    @event_description.setter
    def event_description(self, event_description):
        r"""Sets the event_description of this ShowTrafficEventResponse.

        **参数说明**：事件描述。支持英文字母、数字、下划线、斜杠、中文及中文常用字符：。 ？ ！ ， 、 ； ： “ ”

        :param event_description: The event_description of this ShowTrafficEventResponse.
        :type event_description: str
        """
        self._event_description = event_description

    @property
    def reference_paths(self):
        r"""Gets the reference_paths of this ShowTrafficEventResponse.

        **参数说明**：事件生效的关联路径，至少需写入起始和终止位置的两个坐标点。

        :return: The reference_paths of this ShowTrafficEventResponse.
        :rtype: list[:class:`huaweicloudsdkdris.v1.EventReferencePath`]
        """
        return self._reference_paths

    @reference_paths.setter
    def reference_paths(self, reference_paths):
        r"""Sets the reference_paths of this ShowTrafficEventResponse.

        **参数说明**：事件生效的关联路径，至少需写入起始和终止位置的两个坐标点。

        :param reference_paths: The reference_paths of this ShowTrafficEventResponse.
        :type reference_paths: list[:class:`huaweicloudsdkdris.v1.EventReferencePath`]
        """
        self._reference_paths = reference_paths

    @property
    def event_position_name(self):
        r"""Gets the event_position_name of this ShowTrafficEventResponse.

        **参数说明**：事件所在位置。

        :return: The event_position_name of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._event_position_name

    @event_position_name.setter
    def event_position_name(self, event_position_name):
        r"""Sets the event_position_name of this ShowTrafficEventResponse.

        **参数说明**：事件所在位置。

        :param event_position_name: The event_position_name of this ShowTrafficEventResponse.
        :type event_position_name: str
        """
        self._event_position_name = event_position_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowTrafficEventResponse.

        **参数说明**：开始时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :return: The start_time of this ShowTrafficEventResponse.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowTrafficEventResponse.

        **参数说明**：开始时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :param start_time: The start_time of this ShowTrafficEventResponse.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTrafficEventResponse.

        **参数说明**：结束时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :return: The end_time of this ShowTrafficEventResponse.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTrafficEventResponse.

        **参数说明**：结束时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :param end_time: The end_time of this ShowTrafficEventResponse.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def note(self):
        r"""Gets the note of this ShowTrafficEventResponse.

        **参数说明**：备注。

        :return: The note of this ShowTrafficEventResponse.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this ShowTrafficEventResponse.

        **参数说明**：备注。

        :param note: The note of this ShowTrafficEventResponse.
        :type note: str
        """
        self._note = note

    @property
    def event_confidence(self):
        r"""Gets the event_confidence of this ShowTrafficEventResponse.

        **参数说明**：事件可信度。

        :return: The event_confidence of this ShowTrafficEventResponse.
        :rtype: int
        """
        return self._event_confidence

    @event_confidence.setter
    def event_confidence(self, event_confidence):
        r"""Sets the event_confidence of this ShowTrafficEventResponse.

        **参数说明**：事件可信度。

        :param event_confidence: The event_confidence of this ShowTrafficEventResponse.
        :type event_confidence: int
        """
        self._event_confidence = event_confidence

    @property
    def created_time(self):
        r"""Gets the created_time of this ShowTrafficEventResponse.

        '**参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :return: The created_time of this ShowTrafficEventResponse.
        :rtype: datetime
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ShowTrafficEventResponse.

        '**参数说明**：创建时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :param created_time: The created_time of this ShowTrafficEventResponse.
        :type created_time: datetime
        """
        self._created_time = created_time

    @property
    def last_modified_time(self):
        r"""Gets the last_modified_time of this ShowTrafficEventResponse.

        **参数说明**：最后修改的时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :return: The last_modified_time of this ShowTrafficEventResponse.
        :rtype: datetime
        """
        return self._last_modified_time

    @last_modified_time.setter
    def last_modified_time(self, last_modified_time):
        r"""Sets the last_modified_time of this ShowTrafficEventResponse.

        **参数说明**：最后修改的时间。  格式：yyyy-MM-dd''T''HH:mm:ss''Z''。  例如 2020-09-01T01:37:01Z。 

        :param last_modified_time: The last_modified_time of this ShowTrafficEventResponse.
        :type last_modified_time: datetime
        """
        self._last_modified_time = last_modified_time

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
        if not isinstance(other, ShowTrafficEventResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
