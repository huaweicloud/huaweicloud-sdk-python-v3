# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTuningParamsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'full_sync': 'list[TuningParameter]',
        'incre_capture': 'list[TuningParameter]',
        'incre_apply': 'list[TuningParameter]',
        'incre_relay': 'list[TuningParameter]',
        'modify_result': 'str'
    }

    attribute_map = {
        'full_sync': 'full_sync',
        'incre_capture': 'incre_capture',
        'incre_apply': 'incre_apply',
        'incre_relay': 'incre_relay',
        'modify_result': 'modify_result'
    }

    def __init__(self, full_sync=None, incre_capture=None, incre_apply=None, incre_relay=None, modify_result=None):
        """UpdateTuningParamsResponse

        The model defined in huaweicloud sdk

        :param full_sync: 全量调优参数
        :type full_sync: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        :param incre_capture: 增量抓取调优参数
        :type incre_capture: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        :param incre_apply: 增量回放调优参数
        :type incre_apply: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        :param incre_relay: 增量日志拉取调优参数
        :type incre_relay: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        :param modify_result: 参数修改是否成功
        :type modify_result: str
        """
        
        super(UpdateTuningParamsResponse, self).__init__()

        self._full_sync = None
        self._incre_capture = None
        self._incre_apply = None
        self._incre_relay = None
        self._modify_result = None
        self.discriminator = None

        if full_sync is not None:
            self.full_sync = full_sync
        if incre_capture is not None:
            self.incre_capture = incre_capture
        if incre_apply is not None:
            self.incre_apply = incre_apply
        if incre_relay is not None:
            self.incre_relay = incre_relay
        if modify_result is not None:
            self.modify_result = modify_result

    @property
    def full_sync(self):
        """Gets the full_sync of this UpdateTuningParamsResponse.

        全量调优参数

        :return: The full_sync of this UpdateTuningParamsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        return self._full_sync

    @full_sync.setter
    def full_sync(self, full_sync):
        """Sets the full_sync of this UpdateTuningParamsResponse.

        全量调优参数

        :param full_sync: The full_sync of this UpdateTuningParamsResponse.
        :type full_sync: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        self._full_sync = full_sync

    @property
    def incre_capture(self):
        """Gets the incre_capture of this UpdateTuningParamsResponse.

        增量抓取调优参数

        :return: The incre_capture of this UpdateTuningParamsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        return self._incre_capture

    @incre_capture.setter
    def incre_capture(self, incre_capture):
        """Sets the incre_capture of this UpdateTuningParamsResponse.

        增量抓取调优参数

        :param incre_capture: The incre_capture of this UpdateTuningParamsResponse.
        :type incre_capture: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        self._incre_capture = incre_capture

    @property
    def incre_apply(self):
        """Gets the incre_apply of this UpdateTuningParamsResponse.

        增量回放调优参数

        :return: The incre_apply of this UpdateTuningParamsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        return self._incre_apply

    @incre_apply.setter
    def incre_apply(self, incre_apply):
        """Sets the incre_apply of this UpdateTuningParamsResponse.

        增量回放调优参数

        :param incre_apply: The incre_apply of this UpdateTuningParamsResponse.
        :type incre_apply: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        self._incre_apply = incre_apply

    @property
    def incre_relay(self):
        """Gets the incre_relay of this UpdateTuningParamsResponse.

        增量日志拉取调优参数

        :return: The incre_relay of this UpdateTuningParamsResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        return self._incre_relay

    @incre_relay.setter
    def incre_relay(self, incre_relay):
        """Sets the incre_relay of this UpdateTuningParamsResponse.

        增量日志拉取调优参数

        :param incre_relay: The incre_relay of this UpdateTuningParamsResponse.
        :type incre_relay: list[:class:`huaweicloudsdkdrs.v3.TuningParameter`]
        """
        self._incre_relay = incre_relay

    @property
    def modify_result(self):
        """Gets the modify_result of this UpdateTuningParamsResponse.

        参数修改是否成功

        :return: The modify_result of this UpdateTuningParamsResponse.
        :rtype: str
        """
        return self._modify_result

    @modify_result.setter
    def modify_result(self, modify_result):
        """Sets the modify_result of this UpdateTuningParamsResponse.

        参数修改是否成功

        :param modify_result: The modify_result of this UpdateTuningParamsResponse.
        :type modify_result: str
        """
        self._modify_result = modify_result

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
        if not isinstance(other, UpdateTuningParamsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
