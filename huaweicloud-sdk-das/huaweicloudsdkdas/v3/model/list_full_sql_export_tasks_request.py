# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFullSqlExportTasksRequest:

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
        'task_id': 'int',
        'page_size': 'int',
        'page_no': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'task_id': 'task_id',
        'page_size': 'page_size',
        'page_no': 'page_no'
    }

    def __init__(self, instance_id=None, task_id=None, page_size=None, page_no=None):
        r"""ListFullSqlExportTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param task_id: 任务ID
        :type task_id: int
        :param page_size: 每页记录数
        :type page_size: int
        :param page_no: 页码
        :type page_no: int
        """
        
        

        self._instance_id = None
        self._task_id = None
        self._page_size = None
        self._page_no = None
        self.discriminator = None

        self.instance_id = instance_id
        if task_id is not None:
            self.task_id = task_id
        self.page_size = page_size
        self.page_no = page_no

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListFullSqlExportTasksRequest.

        实例ID

        :return: The instance_id of this ListFullSqlExportTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListFullSqlExportTasksRequest.

        实例ID

        :param instance_id: The instance_id of this ListFullSqlExportTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def task_id(self):
        r"""Gets the task_id of this ListFullSqlExportTasksRequest.

        任务ID

        :return: The task_id of this ListFullSqlExportTasksRequest.
        :rtype: int
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        r"""Sets the task_id of this ListFullSqlExportTasksRequest.

        任务ID

        :param task_id: The task_id of this ListFullSqlExportTasksRequest.
        :type task_id: int
        """
        self._task_id = task_id

    @property
    def page_size(self):
        r"""Gets the page_size of this ListFullSqlExportTasksRequest.

        每页记录数

        :return: The page_size of this ListFullSqlExportTasksRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListFullSqlExportTasksRequest.

        每页记录数

        :param page_size: The page_size of this ListFullSqlExportTasksRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_no(self):
        r"""Gets the page_no of this ListFullSqlExportTasksRequest.

        页码

        :return: The page_no of this ListFullSqlExportTasksRequest.
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        r"""Sets the page_no of this ListFullSqlExportTasksRequest.

        页码

        :param page_no: The page_no of this ListFullSqlExportTasksRequest.
        :type page_no: int
        """
        self._page_no = page_no

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
        if not isinstance(other, ListFullSqlExportTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
