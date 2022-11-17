# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskHostingResultHostingResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'overdue_date': 'datetime',
        'status': 'str',
        'data': 'str',
        'file_size': 'str'
    }

    attribute_map = {
        'overdue_date': 'overdue_date',
        'status': 'status',
        'data': 'data',
        'file_size': 'file_size'
    }

    def __init__(self, overdue_date=None, status=None, data=None, file_size=None):
        """TaskHostingResultHostingResult

        The model defined in huaweicloud sdk

        :param overdue_date: 结果文件result.json的过期时间
        :type overdue_date: datetime
        :param status: 结果文件result.json的状态
        :type status: str
        :param data: 结果文件result.json的具体内容
        :type data: str
        :param file_size: 结果文件result.json的大小
        :type file_size: str
        """
        
        

        self._overdue_date = None
        self._status = None
        self._data = None
        self._file_size = None
        self.discriminator = None

        if overdue_date is not None:
            self.overdue_date = overdue_date
        if status is not None:
            self.status = status
        if data is not None:
            self.data = data
        if file_size is not None:
            self.file_size = file_size

    @property
    def overdue_date(self):
        """Gets the overdue_date of this TaskHostingResultHostingResult.

        结果文件result.json的过期时间

        :return: The overdue_date of this TaskHostingResultHostingResult.
        :rtype: datetime
        """
        return self._overdue_date

    @overdue_date.setter
    def overdue_date(self, overdue_date):
        """Sets the overdue_date of this TaskHostingResultHostingResult.

        结果文件result.json的过期时间

        :param overdue_date: The overdue_date of this TaskHostingResultHostingResult.
        :type overdue_date: datetime
        """
        self._overdue_date = overdue_date

    @property
    def status(self):
        """Gets the status of this TaskHostingResultHostingResult.

        结果文件result.json的状态

        :return: The status of this TaskHostingResultHostingResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskHostingResultHostingResult.

        结果文件result.json的状态

        :param status: The status of this TaskHostingResultHostingResult.
        :type status: str
        """
        self._status = status

    @property
    def data(self):
        """Gets the data of this TaskHostingResultHostingResult.

        结果文件result.json的具体内容

        :return: The data of this TaskHostingResultHostingResult.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this TaskHostingResultHostingResult.

        结果文件result.json的具体内容

        :param data: The data of this TaskHostingResultHostingResult.
        :type data: str
        """
        self._data = data

    @property
    def file_size(self):
        """Gets the file_size of this TaskHostingResultHostingResult.

        结果文件result.json的大小

        :return: The file_size of this TaskHostingResultHostingResult.
        :rtype: str
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this TaskHostingResultHostingResult.

        结果文件result.json的大小

        :param file_size: The file_size of this TaskHostingResultHostingResult.
        :type file_size: str
        """
        self._file_size = file_size

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
        if not isinstance(other, TaskHostingResultHostingResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
