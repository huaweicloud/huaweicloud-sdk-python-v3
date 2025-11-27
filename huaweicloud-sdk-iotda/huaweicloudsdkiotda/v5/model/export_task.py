# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'export_task_id': 'str',
        'resource_type': 'str',
        'resource_condition': 'object',
        'export_format': 'str',
        'status': 'str',
        'export_count': 'int',
        'progress': 'int',
        'create_time': 'str',
        'end_time': 'str',
        'app_type': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'export_task_id': 'export_task_id',
        'resource_type': 'resource_type',
        'resource_condition': 'resource_condition',
        'export_format': 'export_format',
        'status': 'status',
        'export_count': 'export_count',
        'progress': 'progress',
        'create_time': 'create_time',
        'end_time': 'end_time',
        'app_type': 'app_type',
        'app_id': 'app_id'
    }

    def __init__(self, export_task_id=None, resource_type=None, resource_condition=None, export_format=None, status=None, export_count=None, progress=None, create_time=None, end_time=None, app_type=None, app_id=None):
        r"""ExportTask

        The model defined in huaweicloud sdk

        :param export_task_id: 导出任务唯一id。
        :type export_task_id: str
        :param resource_type: 导出源资源类型，支持批量任务导出类型BatchTask。
        :type resource_type: str
        :param resource_condition: 资源过滤条件，Json格式，里面是(K,V)键值对，当resource_type为BatchTask时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。
        :type resource_condition: object
        :param export_format: 导出格式，目前xls格式。
        :type export_format: str
        :param status: 任务状态，状态分别有：Processing：执行中，Success：成功，Failed：失败。
        :type status: str
        :param export_count: 已导出的资源数量。
        :type export_count: int
        :param progress: 导出任务的执行进度，取值范围为1-100，当100表示进度为100%，任务完成。
        :type progress: int
        :param create_time: 在物联网平台创建产品的时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;，如2020-08-12T12:12:12.333Z。
        :type create_time: str
        :param end_time: 导出任务的执行结束时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSS&#39;Z&#39;，如2020-08-12T12:12:12.333Z。
        :type end_time: str
        :param app_type: 租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 
        :type app_type: str
        :param app_id: 应用ID。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定创建的规则归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。
        :type app_id: str
        """
        
        

        self._export_task_id = None
        self._resource_type = None
        self._resource_condition = None
        self._export_format = None
        self._status = None
        self._export_count = None
        self._progress = None
        self._create_time = None
        self._end_time = None
        self._app_type = None
        self._app_id = None
        self.discriminator = None

        if export_task_id is not None:
            self.export_task_id = export_task_id
        if resource_type is not None:
            self.resource_type = resource_type
        if resource_condition is not None:
            self.resource_condition = resource_condition
        if export_format is not None:
            self.export_format = export_format
        if status is not None:
            self.status = status
        if export_count is not None:
            self.export_count = export_count
        if progress is not None:
            self.progress = progress
        if create_time is not None:
            self.create_time = create_time
        if end_time is not None:
            self.end_time = end_time
        if app_type is not None:
            self.app_type = app_type
        if app_id is not None:
            self.app_id = app_id

    @property
    def export_task_id(self):
        r"""Gets the export_task_id of this ExportTask.

        导出任务唯一id。

        :return: The export_task_id of this ExportTask.
        :rtype: str
        """
        return self._export_task_id

    @export_task_id.setter
    def export_task_id(self, export_task_id):
        r"""Sets the export_task_id of this ExportTask.

        导出任务唯一id。

        :param export_task_id: The export_task_id of this ExportTask.
        :type export_task_id: str
        """
        self._export_task_id = export_task_id

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ExportTask.

        导出源资源类型，支持批量任务导出类型BatchTask。

        :return: The resource_type of this ExportTask.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ExportTask.

        导出源资源类型，支持批量任务导出类型BatchTask。

        :param resource_type: The resource_type of this ExportTask.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_condition(self):
        r"""Gets the resource_condition of this ExportTask.

        资源过滤条件，Json格式，里面是(K,V)键值对，当resource_type为BatchTask时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。

        :return: The resource_condition of this ExportTask.
        :rtype: object
        """
        return self._resource_condition

    @resource_condition.setter
    def resource_condition(self, resource_condition):
        r"""Sets the resource_condition of this ExportTask.

        资源过滤条件，Json格式，里面是(K,V)键值对，当resource_type为BatchTask时填写填写key为task_id，value为BatchTask的task_id(task_id从批量任务接口获得)。

        :param resource_condition: The resource_condition of this ExportTask.
        :type resource_condition: object
        """
        self._resource_condition = resource_condition

    @property
    def export_format(self):
        r"""Gets the export_format of this ExportTask.

        导出格式，目前xls格式。

        :return: The export_format of this ExportTask.
        :rtype: str
        """
        return self._export_format

    @export_format.setter
    def export_format(self, export_format):
        r"""Sets the export_format of this ExportTask.

        导出格式，目前xls格式。

        :param export_format: The export_format of this ExportTask.
        :type export_format: str
        """
        self._export_format = export_format

    @property
    def status(self):
        r"""Gets the status of this ExportTask.

        任务状态，状态分别有：Processing：执行中，Success：成功，Failed：失败。

        :return: The status of this ExportTask.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ExportTask.

        任务状态，状态分别有：Processing：执行中，Success：成功，Failed：失败。

        :param status: The status of this ExportTask.
        :type status: str
        """
        self._status = status

    @property
    def export_count(self):
        r"""Gets the export_count of this ExportTask.

        已导出的资源数量。

        :return: The export_count of this ExportTask.
        :rtype: int
        """
        return self._export_count

    @export_count.setter
    def export_count(self, export_count):
        r"""Sets the export_count of this ExportTask.

        已导出的资源数量。

        :param export_count: The export_count of this ExportTask.
        :type export_count: int
        """
        self._export_count = export_count

    @property
    def progress(self):
        r"""Gets the progress of this ExportTask.

        导出任务的执行进度，取值范围为1-100，当100表示进度为100%，任务完成。

        :return: The progress of this ExportTask.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this ExportTask.

        导出任务的执行进度，取值范围为1-100，当100表示进度为100%，任务完成。

        :param progress: The progress of this ExportTask.
        :type progress: int
        """
        self._progress = progress

    @property
    def create_time(self):
        r"""Gets the create_time of this ExportTask.

        在物联网平台创建产品的时间，格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'，如2020-08-12T12:12:12.333Z。

        :return: The create_time of this ExportTask.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ExportTask.

        在物联网平台创建产品的时间，格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'，如2020-08-12T12:12:12.333Z。

        :param create_time: The create_time of this ExportTask.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ExportTask.

        导出任务的执行结束时间，格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'，如2020-08-12T12:12:12.333Z。

        :return: The end_time of this ExportTask.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ExportTask.

        导出任务的执行结束时间，格式：yyyy-MM-dd'T'HH:mm:ss.SSS'Z'，如2020-08-12T12:12:12.333Z。

        :param end_time: The end_time of this ExportTask.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def app_type(self):
        r"""Gets the app_type of this ExportTask.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 

        :return: The app_type of this ExportTask.
        :rtype: str
        """
        return self._app_type

    @app_type.setter
    def app_type(self, app_type):
        r"""Sets the app_type of this ExportTask.

        租户规则的生效范围，默认GLOBAL，取值如下： - GLOBAL：生效范围为租户级 - APP：生效范围为应用级，如果类型为APP，需要携带app_id，如果不带，生效范围为defaultApp。 

        :param app_type: The app_type of this ExportTask.
        :type app_type: str
        """
        self._app_type = app_type

    @property
    def app_id(self):
        r"""Gets the app_id of this ExportTask.

        应用ID。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定创建的规则归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :return: The app_id of this ExportTask.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ExportTask.

        应用ID。此参数为非必选参数，用于兼容平台老用户存在多应用的场景。存在多应用的用户需要使用该接口时，必须携带该参数指定创建的规则归属到哪个应用下，否则接口会提示错误。如果用户存在多应用，同时又不想携带该参数，可以联系华为技术支持对用户数据做应用合并。

        :param app_id: The app_id of this ExportTask.
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
        if not isinstance(other, ExportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
