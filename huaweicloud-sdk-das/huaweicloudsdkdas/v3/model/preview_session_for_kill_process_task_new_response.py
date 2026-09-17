# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreviewSessionForKillProcessTaskNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'processes': 'list[ProcessSessionInfo]',
        'data_sync_time': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'processes': 'processes',
        'data_sync_time': 'data_sync_time',
        'total_count': 'total_count'
    }

    def __init__(self, processes=None, data_sync_time=None, total_count=None):
        r"""PreviewSessionForKillProcessTaskNewResponse

        The model defined in huaweicloud sdk

        :param processes: SQL限流信息列表
        :type processes: list[:class:`huaweicloudsdkdas.v3.ProcessSessionInfo`]
        :param data_sync_time: 数据同步的时间
        :type data_sync_time: int
        :param total_count: 会话总数
        :type total_count: int
        """
        
        super().__init__()

        self._processes = None
        self._data_sync_time = None
        self._total_count = None
        self.discriminator = None

        if processes is not None:
            self.processes = processes
        if data_sync_time is not None:
            self.data_sync_time = data_sync_time
        if total_count is not None:
            self.total_count = total_count

    @property
    def processes(self):
        r"""Gets the processes of this PreviewSessionForKillProcessTaskNewResponse.

        SQL限流信息列表

        :return: The processes of this PreviewSessionForKillProcessTaskNewResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.ProcessSessionInfo`]
        """
        return self._processes

    @processes.setter
    def processes(self, processes):
        r"""Sets the processes of this PreviewSessionForKillProcessTaskNewResponse.

        SQL限流信息列表

        :param processes: The processes of this PreviewSessionForKillProcessTaskNewResponse.
        :type processes: list[:class:`huaweicloudsdkdas.v3.ProcessSessionInfo`]
        """
        self._processes = processes

    @property
    def data_sync_time(self):
        r"""Gets the data_sync_time of this PreviewSessionForKillProcessTaskNewResponse.

        数据同步的时间

        :return: The data_sync_time of this PreviewSessionForKillProcessTaskNewResponse.
        :rtype: int
        """
        return self._data_sync_time

    @data_sync_time.setter
    def data_sync_time(self, data_sync_time):
        r"""Sets the data_sync_time of this PreviewSessionForKillProcessTaskNewResponse.

        数据同步的时间

        :param data_sync_time: The data_sync_time of this PreviewSessionForKillProcessTaskNewResponse.
        :type data_sync_time: int
        """
        self._data_sync_time = data_sync_time

    @property
    def total_count(self):
        r"""Gets the total_count of this PreviewSessionForKillProcessTaskNewResponse.

        会话总数

        :return: The total_count of this PreviewSessionForKillProcessTaskNewResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this PreviewSessionForKillProcessTaskNewResponse.

        会话总数

        :param total_count: The total_count of this PreviewSessionForKillProcessTaskNewResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("PreviewSessionForKillProcessTaskNewResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, PreviewSessionForKillProcessTaskNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
