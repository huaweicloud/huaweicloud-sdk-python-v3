# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSumTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_id': 'str',
        'row_list': 'list[FrontRow]',
        'latest_data_time': 'int',
        'table_direction': 'str',
        'real_start_time': 'int',
        'real_end_time': 'int',
        'notice_msg': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'result_id': 'result_id',
        'row_list': 'row_list',
        'latest_data_time': 'latest_data_Time',
        'table_direction': 'table_direction',
        'real_start_time': 'real_start_time',
        'real_end_time': 'real_end_time',
        'notice_msg': 'notice_msg',
        'total_count': 'total_count'
    }

    def __init__(self, result_id=None, row_list=None, latest_data_time=None, table_direction=None, real_start_time=None, real_end_time=None, notice_msg=None, total_count=None):
        r"""ShowSumTableResponse

        The model defined in huaweicloud sdk

        :param result_id: 结果的ID信息，分页查询的时候带过来。
        :type result_id: str
        :param row_list: 数据行列表。
        :type row_list: list[:class:`huaweicloudsdkapm.v1.FrontRow`]
        :param latest_data_time: 最近一笔数据的时间。
        :type latest_data_time: int
        :param table_direction: 表格的方向，H：默认，表头横向，V：表头纵向。
        :type table_direction: str
        :param real_start_time: 实际开始的时间。
        :type real_start_time: int
        :param real_end_time: 实际结束的时间。
        :type real_end_time: int
        :param notice_msg: 提示信息。
        :type notice_msg: str
        :param total_count: 总数。
        :type total_count: int
        """
        
        super(ShowSumTableResponse, self).__init__()

        self._result_id = None
        self._row_list = None
        self._latest_data_time = None
        self._table_direction = None
        self._real_start_time = None
        self._real_end_time = None
        self._notice_msg = None
        self._total_count = None
        self.discriminator = None

        if result_id is not None:
            self.result_id = result_id
        if row_list is not None:
            self.row_list = row_list
        if latest_data_time is not None:
            self.latest_data_time = latest_data_time
        if table_direction is not None:
            self.table_direction = table_direction
        if real_start_time is not None:
            self.real_start_time = real_start_time
        if real_end_time is not None:
            self.real_end_time = real_end_time
        if notice_msg is not None:
            self.notice_msg = notice_msg
        if total_count is not None:
            self.total_count = total_count

    @property
    def result_id(self):
        r"""Gets the result_id of this ShowSumTableResponse.

        结果的ID信息，分页查询的时候带过来。

        :return: The result_id of this ShowSumTableResponse.
        :rtype: str
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        r"""Sets the result_id of this ShowSumTableResponse.

        结果的ID信息，分页查询的时候带过来。

        :param result_id: The result_id of this ShowSumTableResponse.
        :type result_id: str
        """
        self._result_id = result_id

    @property
    def row_list(self):
        r"""Gets the row_list of this ShowSumTableResponse.

        数据行列表。

        :return: The row_list of this ShowSumTableResponse.
        :rtype: list[:class:`huaweicloudsdkapm.v1.FrontRow`]
        """
        return self._row_list

    @row_list.setter
    def row_list(self, row_list):
        r"""Sets the row_list of this ShowSumTableResponse.

        数据行列表。

        :param row_list: The row_list of this ShowSumTableResponse.
        :type row_list: list[:class:`huaweicloudsdkapm.v1.FrontRow`]
        """
        self._row_list = row_list

    @property
    def latest_data_time(self):
        r"""Gets the latest_data_time of this ShowSumTableResponse.

        最近一笔数据的时间。

        :return: The latest_data_time of this ShowSumTableResponse.
        :rtype: int
        """
        return self._latest_data_time

    @latest_data_time.setter
    def latest_data_time(self, latest_data_time):
        r"""Sets the latest_data_time of this ShowSumTableResponse.

        最近一笔数据的时间。

        :param latest_data_time: The latest_data_time of this ShowSumTableResponse.
        :type latest_data_time: int
        """
        self._latest_data_time = latest_data_time

    @property
    def table_direction(self):
        r"""Gets the table_direction of this ShowSumTableResponse.

        表格的方向，H：默认，表头横向，V：表头纵向。

        :return: The table_direction of this ShowSumTableResponse.
        :rtype: str
        """
        return self._table_direction

    @table_direction.setter
    def table_direction(self, table_direction):
        r"""Sets the table_direction of this ShowSumTableResponse.

        表格的方向，H：默认，表头横向，V：表头纵向。

        :param table_direction: The table_direction of this ShowSumTableResponse.
        :type table_direction: str
        """
        self._table_direction = table_direction

    @property
    def real_start_time(self):
        r"""Gets the real_start_time of this ShowSumTableResponse.

        实际开始的时间。

        :return: The real_start_time of this ShowSumTableResponse.
        :rtype: int
        """
        return self._real_start_time

    @real_start_time.setter
    def real_start_time(self, real_start_time):
        r"""Sets the real_start_time of this ShowSumTableResponse.

        实际开始的时间。

        :param real_start_time: The real_start_time of this ShowSumTableResponse.
        :type real_start_time: int
        """
        self._real_start_time = real_start_time

    @property
    def real_end_time(self):
        r"""Gets the real_end_time of this ShowSumTableResponse.

        实际结束的时间。

        :return: The real_end_time of this ShowSumTableResponse.
        :rtype: int
        """
        return self._real_end_time

    @real_end_time.setter
    def real_end_time(self, real_end_time):
        r"""Sets the real_end_time of this ShowSumTableResponse.

        实际结束的时间。

        :param real_end_time: The real_end_time of this ShowSumTableResponse.
        :type real_end_time: int
        """
        self._real_end_time = real_end_time

    @property
    def notice_msg(self):
        r"""Gets the notice_msg of this ShowSumTableResponse.

        提示信息。

        :return: The notice_msg of this ShowSumTableResponse.
        :rtype: str
        """
        return self._notice_msg

    @notice_msg.setter
    def notice_msg(self, notice_msg):
        r"""Sets the notice_msg of this ShowSumTableResponse.

        提示信息。

        :param notice_msg: The notice_msg of this ShowSumTableResponse.
        :type notice_msg: str
        """
        self._notice_msg = notice_msg

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowSumTableResponse.

        总数。

        :return: The total_count of this ShowSumTableResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowSumTableResponse.

        总数。

        :param total_count: The total_count of this ShowSumTableResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowSumTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
