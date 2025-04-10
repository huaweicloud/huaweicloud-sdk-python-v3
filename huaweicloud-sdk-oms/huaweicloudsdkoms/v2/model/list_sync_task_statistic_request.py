# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSyncTaskStatisticRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_task_id': 'str',
        'data_type': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'sync_task_id': 'sync_task_id',
        'data_type': 'data_type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, sync_task_id=None, data_type=None, start_time=None, end_time=None):
        r"""ListSyncTaskStatisticRequest

        The model defined in huaweicloud sdk

        :param sync_task_id: 同步任务ID。
        :type sync_task_id: str
        :param data_type: 统计数据类型： 多类型查询用‘,’分割； REQUEST：接收同步请求对象数 SUCCESS：同步成功对象数 FAILURE：同步失败对象数 SKIP：同步跳过对象数 SIZE：同步成功对象容量(Byte)
        :type data_type: str
        :param start_time: 查询开始时间
        :type start_time: str
        :param end_time: 查询开始时间
        :type end_time: str
        """
        
        

        self._sync_task_id = None
        self._data_type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.sync_task_id = sync_task_id
        self.data_type = data_type
        self.start_time = start_time
        self.end_time = end_time

    @property
    def sync_task_id(self):
        r"""Gets the sync_task_id of this ListSyncTaskStatisticRequest.

        同步任务ID。

        :return: The sync_task_id of this ListSyncTaskStatisticRequest.
        :rtype: str
        """
        return self._sync_task_id

    @sync_task_id.setter
    def sync_task_id(self, sync_task_id):
        r"""Sets the sync_task_id of this ListSyncTaskStatisticRequest.

        同步任务ID。

        :param sync_task_id: The sync_task_id of this ListSyncTaskStatisticRequest.
        :type sync_task_id: str
        """
        self._sync_task_id = sync_task_id

    @property
    def data_type(self):
        r"""Gets the data_type of this ListSyncTaskStatisticRequest.

        统计数据类型： 多类型查询用‘,’分割； REQUEST：接收同步请求对象数 SUCCESS：同步成功对象数 FAILURE：同步失败对象数 SKIP：同步跳过对象数 SIZE：同步成功对象容量(Byte)

        :return: The data_type of this ListSyncTaskStatisticRequest.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this ListSyncTaskStatisticRequest.

        统计数据类型： 多类型查询用‘,’分割； REQUEST：接收同步请求对象数 SUCCESS：同步成功对象数 FAILURE：同步失败对象数 SKIP：同步跳过对象数 SIZE：同步成功对象容量(Byte)

        :param data_type: The data_type of this ListSyncTaskStatisticRequest.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListSyncTaskStatisticRequest.

        查询开始时间

        :return: The start_time of this ListSyncTaskStatisticRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListSyncTaskStatisticRequest.

        查询开始时间

        :param start_time: The start_time of this ListSyncTaskStatisticRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListSyncTaskStatisticRequest.

        查询开始时间

        :return: The end_time of this ListSyncTaskStatisticRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListSyncTaskStatisticRequest.

        查询开始时间

        :param end_time: The end_time of this ListSyncTaskStatisticRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListSyncTaskStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
