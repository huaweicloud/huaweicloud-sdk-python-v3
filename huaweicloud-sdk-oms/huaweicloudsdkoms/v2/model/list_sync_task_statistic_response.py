# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSyncTaskStatisticResponse(SdkResponse):

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
        'statistic_time_type': 'str',
        'statistic_datas': 'list[StatisticTypeData]'
    }

    attribute_map = {
        'sync_task_id': 'sync_task_id',
        'statistic_time_type': 'statistic_time_type',
        'statistic_datas': 'statistic_datas'
    }

    def __init__(self, sync_task_id=None, statistic_time_type=None, statistic_datas=None):
        """ListSyncTaskStatisticResponse

        The model defined in huaweicloud sdk

        :param sync_task_id: 同步任务id
        :type sync_task_id: str
        :param statistic_time_type: 统计结果时间间隔说明描述 FIVE_MINUTES：5分钟 ONE_HOUR：1小时
        :type statistic_time_type: str
        :param statistic_datas: 查询的同步任务统计结果集
        :type statistic_datas: list[:class:`huaweicloudsdkoms.v2.StatisticTypeData`]
        """
        
        super(ListSyncTaskStatisticResponse, self).__init__()

        self._sync_task_id = None
        self._statistic_time_type = None
        self._statistic_datas = None
        self.discriminator = None

        if sync_task_id is not None:
            self.sync_task_id = sync_task_id
        if statistic_time_type is not None:
            self.statistic_time_type = statistic_time_type
        if statistic_datas is not None:
            self.statistic_datas = statistic_datas

    @property
    def sync_task_id(self):
        """Gets the sync_task_id of this ListSyncTaskStatisticResponse.

        同步任务id

        :return: The sync_task_id of this ListSyncTaskStatisticResponse.
        :rtype: str
        """
        return self._sync_task_id

    @sync_task_id.setter
    def sync_task_id(self, sync_task_id):
        """Sets the sync_task_id of this ListSyncTaskStatisticResponse.

        同步任务id

        :param sync_task_id: The sync_task_id of this ListSyncTaskStatisticResponse.
        :type sync_task_id: str
        """
        self._sync_task_id = sync_task_id

    @property
    def statistic_time_type(self):
        """Gets the statistic_time_type of this ListSyncTaskStatisticResponse.

        统计结果时间间隔说明描述 FIVE_MINUTES：5分钟 ONE_HOUR：1小时

        :return: The statistic_time_type of this ListSyncTaskStatisticResponse.
        :rtype: str
        """
        return self._statistic_time_type

    @statistic_time_type.setter
    def statistic_time_type(self, statistic_time_type):
        """Sets the statistic_time_type of this ListSyncTaskStatisticResponse.

        统计结果时间间隔说明描述 FIVE_MINUTES：5分钟 ONE_HOUR：1小时

        :param statistic_time_type: The statistic_time_type of this ListSyncTaskStatisticResponse.
        :type statistic_time_type: str
        """
        self._statistic_time_type = statistic_time_type

    @property
    def statistic_datas(self):
        """Gets the statistic_datas of this ListSyncTaskStatisticResponse.

        查询的同步任务统计结果集

        :return: The statistic_datas of this ListSyncTaskStatisticResponse.
        :rtype: list[:class:`huaweicloudsdkoms.v2.StatisticTypeData`]
        """
        return self._statistic_datas

    @statistic_datas.setter
    def statistic_datas(self, statistic_datas):
        """Sets the statistic_datas of this ListSyncTaskStatisticResponse.

        查询的同步任务统计结果集

        :param statistic_datas: The statistic_datas of this ListSyncTaskStatisticResponse.
        :type statistic_datas: list[:class:`huaweicloudsdkoms.v2.StatisticTypeData`]
        """
        self._statistic_datas = statistic_datas

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
        if not isinstance(other, ListSyncTaskStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
