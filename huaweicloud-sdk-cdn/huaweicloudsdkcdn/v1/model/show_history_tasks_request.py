# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowHistoryTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'page_size': 'int',
        'page_number': 'int',
        'status': 'str',
        'start_date': 'int',
        'end_date': 'int',
        'order_field': 'str',
        'order_type': 'str',
        'file_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'page_size': 'page_size',
        'page_number': 'page_number',
        'status': 'status',
        'start_date': 'start_date',
        'end_date': 'end_date',
        'order_field': 'order_field',
        'order_type': 'order_type',
        'file_type': 'file_type'
    }

    def __init__(self, enterprise_project_id=None, page_size=None, page_number=None, status=None, start_date=None, end_date=None, order_field=None, order_type=None, file_type=None):
        """ShowHistoryTasksRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\&quot;all\&quot;表示所有项目。注意：当使用子账号调用接口时，该参数必传。
        :type enterprise_project_id: str
        :param page_size: 单页最大数量，取值范围为1-10000。page_size和page_number必须同时传值。默认值30。
        :type page_size: int
        :param page_number: 当前查询第几页，取值范围为1-65535。默认值1。
        :type page_number: int
        :param status: 任务状态。 task_inprocess 表示任务处理中，task_done表示任务完成。
        :type status: str
        :param start_date: 查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type start_date: int
        :param end_date: 查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。
        :type end_date: int
        :param order_field: 用来排序的字段，支持的字段有“task_type”，“total”，“processing”， “succeed”，“failed”，“create_time”。order_field和order_type必须同时传值，否则使用默认值\&quot;create_time\&quot; 和 \&quot;desc\&quot;。
        :type order_field: str
        :param order_type: desc 或者asc。默认值desc。
        :type order_type: str
        :param file_type: 默认是文件file。file：文件,directory：目录。
        :type file_type: str
        """
        
        

        self._enterprise_project_id = None
        self._page_size = None
        self._page_number = None
        self._status = None
        self._start_date = None
        self._end_date = None
        self._order_field = None
        self._order_type = None
        self._file_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if page_size is not None:
            self.page_size = page_size
        if page_number is not None:
            self.page_number = page_number
        if status is not None:
            self.status = status
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if order_field is not None:
            self.order_field = order_field
        if order_type is not None:
            self.order_type = order_type
        if file_type is not None:
            self.file_type = file_type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowHistoryTasksRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowHistoryTasksRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，\"all\"表示所有项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this ShowHistoryTasksRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def page_size(self):
        """Gets the page_size of this ShowHistoryTasksRequest.

        单页最大数量，取值范围为1-10000。page_size和page_number必须同时传值。默认值30。

        :return: The page_size of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ShowHistoryTasksRequest.

        单页最大数量，取值范围为1-10000。page_size和page_number必须同时传值。默认值30。

        :param page_size: The page_size of this ShowHistoryTasksRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_number(self):
        """Gets the page_number of this ShowHistoryTasksRequest.

        当前查询第几页，取值范围为1-65535。默认值1。

        :return: The page_number of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ShowHistoryTasksRequest.

        当前查询第几页，取值范围为1-65535。默认值1。

        :param page_number: The page_number of this ShowHistoryTasksRequest.
        :type page_number: int
        """
        self._page_number = page_number

    @property
    def status(self):
        """Gets the status of this ShowHistoryTasksRequest.

        任务状态。 task_inprocess 表示任务处理中，task_done表示任务完成。

        :return: The status of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowHistoryTasksRequest.

        任务状态。 task_inprocess 表示任务处理中，task_done表示任务完成。

        :param status: The status of this ShowHistoryTasksRequest.
        :type status: str
        """
        self._status = status

    @property
    def start_date(self):
        """Gets the start_date of this ShowHistoryTasksRequest.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The start_date of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ShowHistoryTasksRequest.

        查询起始时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param start_date: The start_date of this ShowHistoryTasksRequest.
        :type start_date: int
        """
        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ShowHistoryTasksRequest.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :return: The end_date of this ShowHistoryTasksRequest.
        :rtype: int
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ShowHistoryTasksRequest.

        查询结束时间，相对于UTC 1970-01-01到当前时间相隔的毫秒数。

        :param end_date: The end_date of this ShowHistoryTasksRequest.
        :type end_date: int
        """
        self._end_date = end_date

    @property
    def order_field(self):
        """Gets the order_field of this ShowHistoryTasksRequest.

        用来排序的字段，支持的字段有“task_type”，“total”，“processing”， “succeed”，“failed”，“create_time”。order_field和order_type必须同时传值，否则使用默认值\"create_time\" 和 \"desc\"。

        :return: The order_field of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._order_field

    @order_field.setter
    def order_field(self, order_field):
        """Sets the order_field of this ShowHistoryTasksRequest.

        用来排序的字段，支持的字段有“task_type”，“total”，“processing”， “succeed”，“failed”，“create_time”。order_field和order_type必须同时传值，否则使用默认值\"create_time\" 和 \"desc\"。

        :param order_field: The order_field of this ShowHistoryTasksRequest.
        :type order_field: str
        """
        self._order_field = order_field

    @property
    def order_type(self):
        """Gets the order_type of this ShowHistoryTasksRequest.

        desc 或者asc。默认值desc。

        :return: The order_type of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this ShowHistoryTasksRequest.

        desc 或者asc。默认值desc。

        :param order_type: The order_type of this ShowHistoryTasksRequest.
        :type order_type: str
        """
        self._order_type = order_type

    @property
    def file_type(self):
        """Gets the file_type of this ShowHistoryTasksRequest.

        默认是文件file。file：文件,directory：目录。

        :return: The file_type of this ShowHistoryTasksRequest.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ShowHistoryTasksRequest.

        默认是文件file。file：文件,directory：目录。

        :param file_type: The file_type of this ShowHistoryTasksRequest.
        :type file_type: str
        """
        self._file_type = file_type

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
        if not isinstance(other, ShowHistoryTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
