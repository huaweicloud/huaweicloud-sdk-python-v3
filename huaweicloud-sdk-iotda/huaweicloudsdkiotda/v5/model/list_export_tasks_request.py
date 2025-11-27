# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListExportTasksRequest:

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
        'limit': 'int',
        'marker': 'str',
        'offset': 'int',
        'resource_type': 'str',
        'resource_condition': 'str',
        'app_type': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'limit': 'limit',
        'marker': 'marker',
        'offset': 'offset',
        'resource_type': 'resource_type',
        'resource_condition': 'resource_condition',
        'app_type': 'app_type',
        'app_id': 'app_id'
    }

    def __init__(self, instance_id=None, limit=None, marker=None, offset=None, resource_type=None, resource_condition=None, app_type=None, app_id=None):
        r"""ListExportTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。
        :type instance_id: str
        :param limit: 分页查询时每页显示的记录数，默认值为10，取值范围为1-50的整数。
        :type limit: int
        :param marker: 上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。
        :type marker: str
        :param offset: 表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。
        :type offset: int
        :param resource_type: 导出源资源类型，支持批量任务导出类型BatchTask。
        :type resource_type: str
        :param resource_condition: 资源过滤条件，Json格式，里面是(K,V)键值对，当resource_type为BatchTasks时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。当app_type为APP时，导出的结果也会在该app范围内，否则为租户级别筛选。
        :type resource_condition: str
        :param app_type: 租户规则的生效范围，默认GLOBAL，rule_id不携带的时候，该参数生效，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 
        :type app_type: str
        :param app_id: 应用ID。此参数为非必选参数，rule_id不携带切app_type为APP时，该参数生效，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定查询哪个应用下的消息订阅，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。
        :type app_id: str
        """
        
        

        self._instance_id = None
        self._limit = None
        self._marker = None
        self._offset = None
        self._resource_type = None
        self._resource_condition = None
        self._app_type = None
        self._app_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if offset is not None:
            self.offset = offset
        self.resource_type = resource_type
        if resource_condition is not None:
            self.resource_condition = resource_condition
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListExportTasksRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :return: The instance_id of this ListExportTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListExportTasksRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :param instance_id: The instance_id of this ListExportTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListExportTasksRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为1-50的整数。

        :return: The limit of this ListExportTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListExportTasksRequest.

        分页查询时每页显示的记录数，默认值为10，取值范围为1-50的整数。

        :param limit: The limit of this ListExportTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListExportTasksRequest.

        上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。

        :return: The marker of this ListExportTasksRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListExportTasksRequest.

        上一次分页查询结果中最后一条记录的ID，在上一次分页查询时由物联网平台返回获得。分页查询时物联网平台是按marker也就是记录ID降序查询的，越新的数据记录ID也会越大。若填写marker，则本次只查询记录ID小于marker的数据记录。若不填写，则从记录ID最大也就是最新的一条数据开始查询。如果需要依次查询所有数据，则每次查询时必须填写上一次查询响应中的marker值。

        :param marker: The marker of this ListExportTasksRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def offset(self):
        r"""Gets the offset of this ListExportTasksRequest.

        表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。

        :return: The offset of this ListExportTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListExportTasksRequest.

        表示从marker后偏移offset条记录开始查询。默认为0，取值范围为0-500的整数。当offset为0时，表示从marker后第一条记录开始输出。限制offset最大值是出于API性能考虑，您可以搭配marker使用该参数实现翻页，例如每页50条记录，1-11页内都可以直接使用offset跳转到指定页，但到11页后，由于offset限制为500，您需要使用第11页返回的marker作为下次查询的marker，以实现翻页到12-22页。

        :param offset: The offset of this ListExportTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListExportTasksRequest.

        导出源资源类型，支持批量任务导出类型BatchTask。

        :return: The resource_type of this ListExportTasksRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListExportTasksRequest.

        导出源资源类型，支持批量任务导出类型BatchTask。

        :param resource_type: The resource_type of this ListExportTasksRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_condition(self):
        r"""Gets the resource_condition of this ListExportTasksRequest.

        资源过滤条件，Json格式，里面是(K,V)键值对，当resource_type为BatchTasks时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。当app_type为APP时，导出的结果也会在该app范围内，否则为租户级别筛选。

        :return: The resource_condition of this ListExportTasksRequest.
        :rtype: str
        """
        return self._resource_condition

    @resource_condition.setter
    def resource_condition(self, resource_condition):
        r"""Sets the resource_condition of this ListExportTasksRequest.

        资源过滤条件，Json格式，里面是(K,V)键值对，当resource_type为BatchTasks时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。当app_type为APP时，导出的结果也会在该app范围内，否则为租户级别筛选。

        :param resource_condition: The resource_condition of this ListExportTasksRequest.
        :type resource_condition: str
        """
        self._resource_condition = resource_condition

    @property
    def app_type(self):
        r"""Gets the app_type of this ListExportTasksRequest.

        租户规则的生效范围，默认GLOBAL，rule_id不携带的时候，该参数生效，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 

        :return: The app_type of this ListExportTasksRequest.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ListExportTasksRequest.

        租户规则的生效范围，默认GLOBAL，rule_id不携带的时候，该参数生效，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 

        :param app_type: The app_type of this ListExportTasksRequest.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        r"""Gets the app_id of this ListExportTasksRequest.

        应用ID。此参数为非必选参数，rule_id不携带切app_type为APP时，该参数生效，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定查询哪个应用下的消息订阅，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :return: The app_id of this ListExportTasksRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ListExportTasksRequest.

        应用ID。此参数为非必选参数，rule_id不携带切app_type为APP时，该参数生效，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定查询哪个应用下的消息订阅，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :param app_id: The app_id of this ListExportTasksRequest.
        :type app_id: str
        """
        self._app_id = app_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListExportTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
