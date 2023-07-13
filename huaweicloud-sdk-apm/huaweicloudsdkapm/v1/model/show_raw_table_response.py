# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRawTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'row_list': 'list[FrontRow]',
        'latest_data_time': 'str',
        'table_direction': 'str',
        'result_id': 'str',
        'real_start_time': 'int',
        'real_end_time': 'int'
    }

    attribute_map = {
        'row_list': 'row_list',
        'latest_data_time': 'latest_data_Time',
        'table_direction': 'table_direction',
        'result_id': 'result_id',
        'real_start_time': 'real_start_time',
        'real_end_time': 'real_end_time'
    }

    def __init__(self, row_list=None, latest_data_time=None, table_direction=None, result_id=None, real_start_time=None, real_end_time=None):
        """ShowRawTableResponse

        The model defined in huaweicloud sdk

        :param row_list: 
        :type row_list: list[:class:`huaweicloudsdkapm.v1.FrontRow`]
        :param latest_data_time: 最近一笔数据的时间。
        :type latest_data_time: str
        :param table_direction: 表格的方向，H：默认，表头横向，V：表头纵向。
        :type table_direction: str
        :param result_id: 上次请求id。
        :type result_id: str
        :param real_start_time: 实际开始的时间，主要用于下一次调用，特别是分页调用的时候传的参数。
        :type real_start_time: int
        :param real_end_time: 实际结束的时间。
        :type real_end_time: int
        """
        
        super(ShowRawTableResponse, self).__init__()

        self._row_list = None
        self._latest_data_time = None
        self._table_direction = None
        self._result_id = None
        self._real_start_time = None
        self._real_end_time = None
        self.discriminator = None

        if row_list is not None:
            self.row_list = row_list
        if latest_data_time is not None:
            self.latest_data_time = latest_data_time
        if table_direction is not None:
            self.table_direction = table_direction
        if result_id is not None:
            self.result_id = result_id
        if real_start_time is not None:
            self.real_start_time = real_start_time
        if real_end_time is not None:
            self.real_end_time = real_end_time

    @property
    def row_list(self):
        """Gets the row_list of this ShowRawTableResponse.

        :return: The row_list of this ShowRawTableResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.FrontRow`]
        """
        return self._row_list

    @row_list.setter
    def row_list(self, row_list):
        """Sets the row_list of this ShowRawTableResponse.

        :param row_list: The row_list of this ShowRawTableResponse.
        :type row_list: list[:class:`huaweicloudsdkapm.v1.FrontRow`]
        """
        self._row_list = row_list

    @property
    def latest_data_time(self):
        """Gets the latest_data_time of this ShowRawTableResponse.

        最近一笔数据的时间。

        :return: The latest_data_time of this ShowRawTableResponse.
        :rtype: str
        """
        return self._latest_data_time

    @latest_data_time.setter
    def latest_data_time(self, latest_data_time):
        """Sets the latest_data_time of this ShowRawTableResponse.

        最近一笔数据的时间。

        :param latest_data_time: The latest_data_time of this ShowRawTableResponse.
        :type latest_data_time: str
        """
        self._latest_data_time = latest_data_time

    @property
    def table_direction(self):
        """Gets the table_direction of this ShowRawTableResponse.

        表格的方向，H：默认，表头横向，V：表头纵向。

        :return: The table_direction of this ShowRawTableResponse.
        :rtype: str
        """
        return self._table_direction

    @table_direction.setter
    def table_direction(self, table_direction):
        """Sets the table_direction of this ShowRawTableResponse.

        表格的方向，H：默认，表头横向，V：表头纵向。

        :param table_direction: The table_direction of this ShowRawTableResponse.
        :type table_direction: str
        """
        self._table_direction = table_direction

    @property
    def result_id(self):
        """Gets the result_id of this ShowRawTableResponse.

        上次请求id。

        :return: The result_id of this ShowRawTableResponse.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this ShowRawTableResponse.

        上次请求id。

        :param result_id: The result_id of this ShowRawTableResponse.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def real_start_time(self):
        """Gets the real_start_time of this ShowRawTableResponse.

        实际开始的时间，主要用于下一次调用，特别是分页调用的时候传的参数。

        :return: The real_start_time of this ShowRawTableResponse.
        :rtype: int
        """
        return self._real_start_time

    @real_start_time.setter
    def real_start_time(self, real_start_time):
        """Sets the real_start_time of this ShowRawTableResponse.

        实际开始的时间，主要用于下一次调用，特别是分页调用的时候传的参数。

        :param real_start_time: The real_start_time of this ShowRawTableResponse.
        :type real_start_time: int
        """
        self._real_start_time = real_start_time

    @property
    def real_end_time(self):
        """Gets the real_end_time of this ShowRawTableResponse.

        实际结束的时间。

        :return: The real_end_time of this ShowRawTableResponse.
        :rtype: int
        """
        return self._real_end_time

    @real_end_time.setter
    def real_end_time(self, real_end_time):
        """Sets the real_end_time of this ShowRawTableResponse.

        实际结束的时间。

        :param real_end_time: The real_end_time of this ShowRawTableResponse.
        :type real_end_time: int
        """
        self._real_end_time = real_end_time

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
        if not isinstance(other, ShowRawTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
