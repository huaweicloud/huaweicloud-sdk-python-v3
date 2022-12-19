# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowTrafficEventsRequest:

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
        'area_code': 'int',
        'status': 'str',
        'event_type': 'int',
        'event_source_type': 'list[str]',
        'event_class': 'str',
        'event_id': 'str',
        'from_time': 'str',
        'to_time': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'offset': 'offset',
        'limit': 'limit',
        'area_code': 'area_code',
        'status': 'status',
        'event_type': 'event_type',
        'event_source_type': 'event_source_type',
        'event_class': 'event_class',
        'event_id': 'event_id',
        'from_time': 'from_time',
        'to_time': 'to_time',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, area_code=None, status=None, event_type=None, event_source_type=None, event_class=None, event_id=None, from_time=None, to_time=None, sort_key=None, sort_dir=None):
        """BatchShowTrafficEventsRequest

        The model defined in huaweicloud sdk

        :param instance_id: \&quot;**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\&quot;
        :type instance_id: str
        :param offset: **参数说明**：查询事件列表的页码。
        :type offset: int
        :param limit: **参数说明**：查询时每页显示的记录数。
        :type limit: int
        :param area_code: **参数说明**：区域码，参考[区域码查询](http://xzqh.mca.gov.cn/map)。
        :type area_code: int
        :param status:  **参数说明**：事件状态。  **取值范围**：  - Invalid：为过期事件，事件结束时间（end_time）在当前时间之前。  - Active：为活动事件，事件开始时间（start_time）在当前时间之前，并且事件结束时间（end_time）在当前时间之后。  - Future：为未来事件，事件开始时间（start_time）在当前时间之前。 
        :type status: str
        :param event_type: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。
        :type event_type: int
        :param event_source_type:  **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 
        :type event_source_type: list[str]
        :param event_class: **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。
        :type event_class: str
        :param event_id: **参数说明**：事件ID，创建事件后获得。方法参见 [新增交通事件](https://support.huaweicloud.com/api-v2x/v2x_04_0048.html)。
        :type event_id: str
        :param from_time: **参数说明**：查询事件开始时间段的起始时间。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。  例如 2020-09-01T01:37:01Z。 
        :type from_time: str
        :param to_time: **参数说明**：查询事件开始时间段的结束时间。  格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss&#39;Z&#39;。  例如 2020-09-01T01:37:01Z。 
        :type to_time: str
        :param sort_key: **参数说明**：按照哪一个字段排序,默认按事件开始时间。
        :type sort_key: str
        :param sort_dir: **参数说明**：升序或降序，升序为ASC, 降序为DESC，默认降序。
        :type sort_dir: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._area_code = None
        self._status = None
        self._event_type = None
        self._event_source_type = None
        self._event_class = None
        self._event_id = None
        self._from_time = None
        self._to_time = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if area_code is not None:
            self.area_code = area_code
        if status is not None:
            self.status = status
        if event_type is not None:
            self.event_type = event_type
        if event_source_type is not None:
            self.event_source_type = event_source_type
        if event_class is not None:
            self.event_class = event_class
        if event_id is not None:
            self.event_id = event_id
        if from_time is not None:
            self.from_time = from_time
        if to_time is not None:
            self.to_time = to_time
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchShowTrafficEventsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :return: The instance_id of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchShowTrafficEventsRequest.

        \"**参数说明**：实例ID。dris物理实例的唯一标识。获取方法参见[获取Instance-Id](https://support.huaweicloud.com/api-v2x/v2x_04_0030.html)。  **取值范围**：仅支持数字，小写字母和横杠（-）的组合，长度36。\"

        :param instance_id: The instance_id of this BatchShowTrafficEventsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this BatchShowTrafficEventsRequest.

        **参数说明**：查询事件列表的页码。

        :return: The offset of this BatchShowTrafficEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this BatchShowTrafficEventsRequest.

        **参数说明**：查询事件列表的页码。

        :param offset: The offset of this BatchShowTrafficEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this BatchShowTrafficEventsRequest.

        **参数说明**：查询时每页显示的记录数。

        :return: The limit of this BatchShowTrafficEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BatchShowTrafficEventsRequest.

        **参数说明**：查询时每页显示的记录数。

        :param limit: The limit of this BatchShowTrafficEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def area_code(self):
        """Gets the area_code of this BatchShowTrafficEventsRequest.

        **参数说明**：区域码，参考[区域码查询](http://xzqh.mca.gov.cn/map)。

        :return: The area_code of this BatchShowTrafficEventsRequest.
        :rtype: int
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """Sets the area_code of this BatchShowTrafficEventsRequest.

        **参数说明**：区域码，参考[区域码查询](http://xzqh.mca.gov.cn/map)。

        :param area_code: The area_code of this BatchShowTrafficEventsRequest.
        :type area_code: int
        """
        self._area_code = area_code

    @property
    def status(self):
        """Gets the status of this BatchShowTrafficEventsRequest.

         **参数说明**：事件状态。  **取值范围**：  - Invalid：为过期事件，事件结束时间（end_time）在当前时间之前。  - Active：为活动事件，事件开始时间（start_time）在当前时间之前，并且事件结束时间（end_time）在当前时间之后。  - Future：为未来事件，事件开始时间（start_time）在当前时间之前。 

        :return: The status of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchShowTrafficEventsRequest.

         **参数说明**：事件状态。  **取值范围**：  - Invalid：为过期事件，事件结束时间（end_time）在当前时间之前。  - Active：为活动事件，事件开始时间（start_time）在当前时间之前，并且事件结束时间（end_time）在当前时间之后。  - Future：为未来事件，事件开始时间（start_time）在当前时间之前。 

        :param status: The status of this BatchShowTrafficEventsRequest.
        :type status: str
        """
        self._status = status

    @property
    def event_type(self):
        """Gets the event_type of this BatchShowTrafficEventsRequest.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :return: The event_type of this BatchShowTrafficEventsRequest.
        :rtype: int
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this BatchShowTrafficEventsRequest.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :param event_type: The event_type of this BatchShowTrafficEventsRequest.
        :type event_type: int
        """
        self._event_type = event_type

    @property
    def event_source_type(self):
        """Gets the event_source_type of this BatchShowTrafficEventsRequest.

         **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 

        :return: The event_source_type of this BatchShowTrafficEventsRequest.
        :rtype: list[str]
        """
        return self._event_source_type

    @event_source_type.setter
    def event_source_type(self, event_source_type):
        """Sets the event_source_type of this BatchShowTrafficEventsRequest.

         **参数说明**：事件来源类型列表,支持事件来源。  **取值范围**：  - unknown：未知数据  - police：警方数据  - government：政府数据  - meteorological：气象数据  - internet：互联网数据  - detection：检测器检测到的数据  - v2xServer：平台上报数据  - rsu：RSU上报数据  - obu：车载终端上报数据 

        :param event_source_type: The event_source_type of this BatchShowTrafficEventsRequest.
        :type event_source_type: list[str]
        """
        self._event_source_type = event_source_type

    @property
    def event_class(self):
        """Gets the event_class of this BatchShowTrafficEventsRequest.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :return: The event_class of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._event_class

    @event_class.setter
    def event_class(self, event_class):
        """Sets the event_class of this BatchShowTrafficEventsRequest.

        **参数说明**：事件类型，参照附录[《国标交通事件及标志列表》](https://support.huaweicloud.com/api-v2x/v2x_04_0101.html)文件。当填写event_type时，event_class为必选。

        :param event_class: The event_class of this BatchShowTrafficEventsRequest.
        :type event_class: str
        """
        self._event_class = event_class

    @property
    def event_id(self):
        """Gets the event_id of this BatchShowTrafficEventsRequest.

        **参数说明**：事件ID，创建事件后获得。方法参见 [新增交通事件](https://support.huaweicloud.com/api-v2x/v2x_04_0048.html)。

        :return: The event_id of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this BatchShowTrafficEventsRequest.

        **参数说明**：事件ID，创建事件后获得。方法参见 [新增交通事件](https://support.huaweicloud.com/api-v2x/v2x_04_0048.html)。

        :param event_id: The event_id of this BatchShowTrafficEventsRequest.
        :type event_id: str
        """
        self._event_id = event_id

    @property
    def from_time(self):
        """Gets the from_time of this BatchShowTrafficEventsRequest.

        **参数说明**：查询事件开始时间段的起始时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'。  例如 2020-09-01T01:37:01Z。 

        :return: The from_time of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._from_time

    @from_time.setter
    def from_time(self, from_time):
        """Sets the from_time of this BatchShowTrafficEventsRequest.

        **参数说明**：查询事件开始时间段的起始时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'。  例如 2020-09-01T01:37:01Z。 

        :param from_time: The from_time of this BatchShowTrafficEventsRequest.
        :type from_time: str
        """
        self._from_time = from_time

    @property
    def to_time(self):
        """Gets the to_time of this BatchShowTrafficEventsRequest.

        **参数说明**：查询事件开始时间段的结束时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'。  例如 2020-09-01T01:37:01Z。 

        :return: The to_time of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._to_time

    @to_time.setter
    def to_time(self, to_time):
        """Sets the to_time of this BatchShowTrafficEventsRequest.

        **参数说明**：查询事件开始时间段的结束时间。  格式：yyyy-MM-dd'T'HH:mm:ss'Z'。  例如 2020-09-01T01:37:01Z。 

        :param to_time: The to_time of this BatchShowTrafficEventsRequest.
        :type to_time: str
        """
        self._to_time = to_time

    @property
    def sort_key(self):
        """Gets the sort_key of this BatchShowTrafficEventsRequest.

        **参数说明**：按照哪一个字段排序,默认按事件开始时间。

        :return: The sort_key of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        """Sets the sort_key of this BatchShowTrafficEventsRequest.

        **参数说明**：按照哪一个字段排序,默认按事件开始时间。

        :param sort_key: The sort_key of this BatchShowTrafficEventsRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        """Gets the sort_dir of this BatchShowTrafficEventsRequest.

        **参数说明**：升序或降序，升序为ASC, 降序为DESC，默认降序。

        :return: The sort_dir of this BatchShowTrafficEventsRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        """Sets the sort_dir of this BatchShowTrafficEventsRequest.

        **参数说明**：升序或降序，升序为ASC, 降序为DESC，默认降序。

        :param sort_dir: The sort_dir of this BatchShowTrafficEventsRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, BatchShowTrafficEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
