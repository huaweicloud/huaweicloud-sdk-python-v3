# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceHealthReportTasksRequest:

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
        'start_at': 'str',
        'end_at': 'str',
        'page_num': 'str',
        'page_size': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_at': 'start_at',
        'end_at': 'end_at',
        'page_num': 'page_num',
        'page_size': 'page_size'
    }

    def __init__(self, instance_id=None, start_at=None, end_at=None, page_num=None, page_size=None):
        r"""ListInstanceHealthReportTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param start_at: 开始时间（Unix时间戳，毫秒）
        :type start_at: str
        :param end_at: 结束时间（Unix时间戳，毫秒）
        :type end_at: str
        :param page_num: 页码
        :type page_num: str
        :param page_size: 每页记录数
        :type page_size: str
        """
        
        

        self._instance_id = None
        self._start_at = None
        self._end_at = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None

        self.instance_id = instance_id
        if start_at is not None:
            self.start_at = start_at
        if end_at is not None:
            self.end_at = end_at
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceHealthReportTasksRequest.

        实例ID

        :return: The instance_id of this ListInstanceHealthReportTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceHealthReportTasksRequest.

        实例ID

        :param instance_id: The instance_id of this ListInstanceHealthReportTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ListInstanceHealthReportTasksRequest.

        开始时间（Unix时间戳，毫秒）

        :return: The start_at of this ListInstanceHealthReportTasksRequest.
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ListInstanceHealthReportTasksRequest.

        开始时间（Unix时间戳，毫秒）

        :param start_at: The start_at of this ListInstanceHealthReportTasksRequest.
        :type start_at: str
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ListInstanceHealthReportTasksRequest.

        结束时间（Unix时间戳，毫秒）

        :return: The end_at of this ListInstanceHealthReportTasksRequest.
        :rtype: str
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ListInstanceHealthReportTasksRequest.

        结束时间（Unix时间戳，毫秒）

        :param end_at: The end_at of this ListInstanceHealthReportTasksRequest.
        :type end_at: str
        """
        self._end_at = end_at

    @property
    def page_num(self):
        r"""Gets the page_num of this ListInstanceHealthReportTasksRequest.

        页码

        :return: The page_num of this ListInstanceHealthReportTasksRequest.
        :rtype: str
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ListInstanceHealthReportTasksRequest.

        页码

        :param page_num: The page_num of this ListInstanceHealthReportTasksRequest.
        :type page_num: str
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ListInstanceHealthReportTasksRequest.

        每页记录数

        :return: The page_size of this ListInstanceHealthReportTasksRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ListInstanceHealthReportTasksRequest.

        每页记录数

        :param page_size: The page_size of this ListInstanceHealthReportTasksRequest.
        :type page_size: str
        """
        self._page_size = page_size

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
        if not isinstance(other, ListInstanceHealthReportTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
