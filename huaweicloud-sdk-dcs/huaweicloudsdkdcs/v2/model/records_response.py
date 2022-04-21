# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecordsResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'scan_type': 'str',
        'created_at': 'str',
        'started_at': 'str',
        'finished_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'scan_type': 'scan_type',
        'created_at': 'created_at',
        'started_at': 'started_at',
        'finished_at': 'finished_at'
    }

    def __init__(self, id=None, status=None, scan_type=None, created_at=None, started_at=None, finished_at=None):
        """RecordsResponse

        The model defined in huaweicloud sdk

        :param id: 大key分析记录ID
        :type id: str
        :param status: 分析任务状态
        :type status: str
        :param scan_type: 分析方式
        :type scan_type: str
        :param created_at: 分析任务创建时间,格式为：\&quot;2020-06-15T02:21:18.669Z\&quot;
        :type created_at: str
        :param started_at: 分析任务开始时间,格式为：\&quot;2020-06-15T02:21:18.669Z\&quot;
        :type started_at: str
        :param finished_at: 分析任务结束时间,格式为：\&quot;2020-06-15T02:21:18.669Z\&quot;
        :type finished_at: str
        """
        
        

        self._id = None
        self._status = None
        self._scan_type = None
        self._created_at = None
        self._started_at = None
        self._finished_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if scan_type is not None:
            self.scan_type = scan_type
        if created_at is not None:
            self.created_at = created_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at

    @property
    def id(self):
        """Gets the id of this RecordsResponse.

        大key分析记录ID

        :return: The id of this RecordsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RecordsResponse.

        大key分析记录ID

        :param id: The id of this RecordsResponse.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this RecordsResponse.

        分析任务状态

        :return: The status of this RecordsResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RecordsResponse.

        分析任务状态

        :param status: The status of this RecordsResponse.
        :type status: str
        """
        self._status = status

    @property
    def scan_type(self):
        """Gets the scan_type of this RecordsResponse.

        分析方式

        :return: The scan_type of this RecordsResponse.
        :rtype: str
        """
        return self._scan_type

    @scan_type.setter
    def scan_type(self, scan_type):
        """Sets the scan_type of this RecordsResponse.

        分析方式

        :param scan_type: The scan_type of this RecordsResponse.
        :type scan_type: str
        """
        self._scan_type = scan_type

    @property
    def created_at(self):
        """Gets the created_at of this RecordsResponse.

        分析任务创建时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :return: The created_at of this RecordsResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this RecordsResponse.

        分析任务创建时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :param created_at: The created_at of this RecordsResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def started_at(self):
        """Gets the started_at of this RecordsResponse.

        分析任务开始时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :return: The started_at of this RecordsResponse.
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this RecordsResponse.

        分析任务开始时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :param started_at: The started_at of this RecordsResponse.
        :type started_at: str
        """
        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this RecordsResponse.

        分析任务结束时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :return: The finished_at of this RecordsResponse.
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this RecordsResponse.

        分析任务结束时间,格式为：\"2020-06-15T02:21:18.669Z\"

        :param finished_at: The finished_at of this RecordsResponse.
        :type finished_at: str
        """
        self._finished_at = finished_at

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
        if not isinstance(other, RecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
