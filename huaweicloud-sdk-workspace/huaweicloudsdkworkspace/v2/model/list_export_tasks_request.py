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
        'file_name': 'str',
        'task_id': 'str',
        'status': 'str',
        'is_download': 'bool',
        'sort_field': 'str',
        'sort_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'file_name': 'file_name',
        'task_id': 'task_id',
        'status': 'status',
        'is_download': 'is_download',
        'sort_field': 'sort_field',
        'sort_type': 'sort_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, file_name=None, task_id=None, status=None, is_download=None, sort_field=None, sort_type=None, offset=None, limit=None):
        r"""ListExportTasksRequest

        The model defined in huaweicloud sdk

        :param file_name: 文件名。
        :type file_name: str
        :param task_id: 任务id。
        :type task_id: str
        :param status: 导出任务的状态，取值为 CREATING, SUCCESS, FAIL, EXPIRED; CREATING为进行中，SUCCESS为成功，FAIL为失败，EXPIRED为过期。
        :type status: str
        :param is_download: 是否已下载，取值范围：true和false，默认值false。
        :type is_download: bool
        :param sort_field: 排序字段名称，需要结合sort_type字段一起使用。 - create_time 创建时间。
        :type sort_field: str
        :param sort_type: 排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。
        :type sort_type: str
        :param offset: 分页偏移量，默认值：0。
        :type offset: int
        :param limit: 分页大小，取值范围1-100，默认值:20。
        :type limit: int
        """
        
        

        self._file_name = None
        self._task_id = None
        self._status = None
        self._is_download = None
        self._sort_field = None
        self._sort_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if file_name is not None:
            self.file_name = file_name
        if task_id is not None:
            self.task_id = task_id
        if status is not None:
            self.status = status
        if is_download is not None:
            self.is_download = is_download
        if sort_field is not None:
            self.sort_field = sort_field
        if sort_type is not None:
            self.sort_type = sort_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def file_name(self):
        r"""Gets the file_name of this ListExportTasksRequest.

        文件名。

        :return: The file_name of this ListExportTasksRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        r"""Sets the file_name of this ListExportTasksRequest.

        文件名。

        :param file_name: The file_name of this ListExportTasksRequest.
        :type file_name: str
        """
        self._file_name = file_name

    @property
    def task_id(self):
        r"""Gets the task_id of this ListExportTasksRequest.

        任务id。

        :return: The task_id of this ListExportTasksRequest.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListExportTasksRequest.

        任务id。

        :param task_id: The task_id of this ListExportTasksRequest.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def status(self):
        r"""Gets the status of this ListExportTasksRequest.

        导出任务的状态，取值为 CREATING, SUCCESS, FAIL, EXPIRED; CREATING为进行中，SUCCESS为成功，FAIL为失败，EXPIRED为过期。

        :return: The status of this ListExportTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListExportTasksRequest.

        导出任务的状态，取值为 CREATING, SUCCESS, FAIL, EXPIRED; CREATING为进行中，SUCCESS为成功，FAIL为失败，EXPIRED为过期。

        :param status: The status of this ListExportTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def is_download(self):
        r"""Gets the is_download of this ListExportTasksRequest.

        是否已下载，取值范围：true和false，默认值false。

        :return: The is_download of this ListExportTasksRequest.
        :rtype: bool
        """
        return self._is_download

    @is_download.setter
    def is_download(self, is_download):
        r"""Sets the is_download of this ListExportTasksRequest.

        是否已下载，取值范围：true和false，默认值false。

        :param is_download: The is_download of this ListExportTasksRequest.
        :type is_download: bool
        """
        self._is_download = is_download

    @property
    def sort_field(self):
        r"""Gets the sort_field of this ListExportTasksRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - create_time 创建时间。

        :return: The sort_field of this ListExportTasksRequest.
        :rtype: str
        """
        return self._sort_field

    @sort_field.setter
    def sort_field(self, sort_field):
        r"""Sets the sort_field of this ListExportTasksRequest.

        排序字段名称，需要结合sort_type字段一起使用。 - create_time 创建时间。

        :param sort_field: The sort_field of this ListExportTasksRequest.
        :type sort_field: str
        """
        self._sort_field = sort_field

    @property
    def sort_type(self):
        r"""Gets the sort_type of this ListExportTasksRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :return: The sort_type of this ListExportTasksRequest.
        :rtype: str
        """
        return self._sort_type

    @sort_type.setter
    def sort_type(self, sort_type):
        r"""Sets the sort_type of this ListExportTasksRequest.

        排序类型，默认升序，需要结合sort_field字段一起使用。 - ASC 升序。 - DESC 降序。

        :param sort_type: The sort_type of this ListExportTasksRequest.
        :type sort_type: str
        """
        self._sort_type = sort_type

    @property
    def offset(self):
        r"""Gets the offset of this ListExportTasksRequest.

        分页偏移量，默认值：0。

        :return: The offset of this ListExportTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListExportTasksRequest.

        分页偏移量，默认值：0。

        :param offset: The offset of this ListExportTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListExportTasksRequest.

        分页大小，取值范围1-100，默认值:20。

        :return: The limit of this ListExportTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListExportTasksRequest.

        分页大小，取值范围1-100，默认值:20。

        :param limit: The limit of this ListExportTasksRequest.
        :type limit: int
        """
        self._limit = limit

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
