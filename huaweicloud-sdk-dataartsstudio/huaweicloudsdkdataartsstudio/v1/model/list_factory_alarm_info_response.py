# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryAlarmInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alarm_info': 'list[AlarmInfoResponseAlarmInfo]',
        'total': 'int'
    }

    attribute_map = {
        'alarm_info': 'alarm_info',
        'total': 'total'
    }

    def __init__(self, alarm_info=None, total=None):
        r"""ListFactoryAlarmInfoResponse

        The model defined in huaweicloud sdk

        :param alarm_info: 通知记录信息
        :type alarm_info: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmInfoResponseAlarmInfo`]
        :param total: 通知记录数量
        :type total: int
        """
        
        super(ListFactoryAlarmInfoResponse, self).__init__()

        self._alarm_info = None
        self._total = None
        self.discriminator = None

        if alarm_info is not None:
            self.alarm_info = alarm_info
        if total is not None:
            self.total = total

    @property
    def alarm_info(self):
        r"""Gets the alarm_info of this ListFactoryAlarmInfoResponse.

        通知记录信息

        :return: The alarm_info of this ListFactoryAlarmInfoResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmInfoResponseAlarmInfo`]
        """
        return self._alarm_info

    @alarm_info.setter
    def alarm_info(self, alarm_info):
        r"""Sets the alarm_info of this ListFactoryAlarmInfoResponse.

        通知记录信息

        :param alarm_info: The alarm_info of this ListFactoryAlarmInfoResponse.
        :type alarm_info: list[:class:`huaweicloudsdkdataartsstudio.v1.AlarmInfoResponseAlarmInfo`]
        """
        self._alarm_info = alarm_info

    @property
    def total(self):
        r"""Gets the total of this ListFactoryAlarmInfoResponse.

        通知记录数量

        :return: The total of this ListFactoryAlarmInfoResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListFactoryAlarmInfoResponse.

        通知记录数量

        :param total: The total of this ListFactoryAlarmInfoResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListFactoryAlarmInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
