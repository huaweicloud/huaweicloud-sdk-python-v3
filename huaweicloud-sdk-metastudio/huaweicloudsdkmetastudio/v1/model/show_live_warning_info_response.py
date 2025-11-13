# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLiveWarningInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'live_warning_info': 'list[LiveWarningItem]',
        'limit_duration': 'int',
        'x_request_id': 'str'
    }

    attribute_map = {
        'live_warning_info': 'live_warning_info',
        'limit_duration': 'limit_duration',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, live_warning_info=None, limit_duration=None, x_request_id=None):
        r"""ShowLiveWarningInfoResponse

        The model defined in huaweicloud sdk

        :param live_warning_info: 开播风险告警列表。
        :type live_warning_info: list[:class:`huaweicloudsdkmetastudio.v1.LiveWarningItem`]
        :param limit_duration: **参数解释**： 配置的最大直播时长。单位小时。 0 为不限制。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。
        :type limit_duration: int
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._live_warning_info = None
        self._limit_duration = None
        self._x_request_id = None
        self.discriminator = None

        if live_warning_info is not None:
            self.live_warning_info = live_warning_info
        if limit_duration is not None:
            self.limit_duration = limit_duration
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def live_warning_info(self):
        r"""Gets the live_warning_info of this ShowLiveWarningInfoResponse.

        开播风险告警列表。

        :return: The live_warning_info of this ShowLiveWarningInfoResponse.
        :rtype: list[:class:`huaweicloudsdkmetastudio.v1.LiveWarningItem`]
        """
        return self._live_warning_info

    @live_warning_info.setter
    def live_warning_info(self, live_warning_info):
        r"""Sets the live_warning_info of this ShowLiveWarningInfoResponse.

        开播风险告警列表。

        :param live_warning_info: The live_warning_info of this ShowLiveWarningInfoResponse.
        :type live_warning_info: list[:class:`huaweicloudsdkmetastudio.v1.LiveWarningItem`]
        """
        self._live_warning_info = live_warning_info

    @property
    def limit_duration(self):
        r"""Gets the limit_duration of this ShowLiveWarningInfoResponse.

        **参数解释**： 配置的最大直播时长。单位小时。 0 为不限制。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。

        :return: The limit_duration of this ShowLiveWarningInfoResponse.
        :rtype: int
        """
        return self._limit_duration

    @limit_duration.setter
    def limit_duration(self, limit_duration):
        r"""Sets the limit_duration of this ShowLiveWarningInfoResponse.

        **参数解释**： 配置的最大直播时长。单位小时。 0 为不限制。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。

        :param limit_duration: The limit_duration of this ShowLiveWarningInfoResponse.
        :type limit_duration: int
        """
        self._limit_duration = limit_duration

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowLiveWarningInfoResponse.

        :return: The x_request_id of this ShowLiveWarningInfoResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowLiveWarningInfoResponse.

        :param x_request_id: The x_request_id of this ShowLiveWarningInfoResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ShowLiveWarningInfoResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLiveWarningInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
