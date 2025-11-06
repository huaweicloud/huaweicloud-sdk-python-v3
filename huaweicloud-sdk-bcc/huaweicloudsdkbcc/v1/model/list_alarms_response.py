# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'next_marker': 'str',
        'alarms': 'list[AlarmEntity]'
    }

    attribute_map = {
        'count': 'count',
        'next_marker': 'next_marker',
        'alarms': 'alarms'
    }

    def __init__(self, count=None, next_marker=None, alarms=None):
        r"""ListAlarmsResponse

        The model defined in huaweicloud sdk

        :param count: 本次分页查询响应的告警数量
        :type count: int
        :param next_marker: 下一页的marker
        :type next_marker: str
        :param alarms: 告警数据
        :type alarms: list[:class:`huaweicloudsdkbcc.v1.AlarmEntity`]
        """
        
        super().__init__()

        self._count = None
        self._next_marker = None
        self._alarms = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if next_marker is not None:
            self.next_marker = next_marker
        if alarms is not None:
            self.alarms = alarms

    @property
    def count(self):
        r"""Gets the count of this ListAlarmsResponse.

        本次分页查询响应的告警数量

        :return: The count of this ListAlarmsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAlarmsResponse.

        本次分页查询响应的告警数量

        :param count: The count of this ListAlarmsResponse.
        :type count: int
        """
        self._count = count

    @property
    def next_marker(self):
        r"""Gets the next_marker of this ListAlarmsResponse.

        下一页的marker

        :return: The next_marker of this ListAlarmsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        r"""Sets the next_marker of this ListAlarmsResponse.

        下一页的marker

        :param next_marker: The next_marker of this ListAlarmsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def alarms(self):
        r"""Gets the alarms of this ListAlarmsResponse.

        告警数据

        :return: The alarms of this ListAlarmsResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.AlarmEntity`]
        """
        return self._alarms

    @alarms.setter
    def alarms(self, alarms):
        r"""Sets the alarms of this ListAlarmsResponse.

        告警数据

        :param alarms: The alarms of this ListAlarmsResponse.
        :type alarms: list[:class:`huaweicloudsdkbcc.v1.AlarmEntity`]
        """
        self._alarms = alarms

    def to_dict(self):
        import warnings
        warnings.warn("ListAlarmsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAlarmsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
