# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateTrafficMirrorFilterRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_mirror_filter_rules': 'list[TrafficMirrorFilterRule]',
        'request_id': 'str'
    }

    attribute_map = {
        'traffic_mirror_filter_rules': 'traffic_mirror_filter_rules',
        'request_id': 'request_id'
    }

    def __init__(self, traffic_mirror_filter_rules=None, request_id=None):
        r"""BatchCreateTrafficMirrorFilterRulesResponse

        The model defined in huaweicloud sdk

        :param traffic_mirror_filter_rules: **参数解释**： 流量镜像筛选规则列表的响应体。 **取值范围**： 不涉及。
        :type traffic_mirror_filter_rules: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        :param request_id: **参数解释**： 请求ID。 **取值范围**： 不涉及。
        :type request_id: str
        """
        
        super().__init__()

        self._traffic_mirror_filter_rules = None
        self._request_id = None
        self.discriminator = None

        if traffic_mirror_filter_rules is not None:
            self.traffic_mirror_filter_rules = traffic_mirror_filter_rules
        if request_id is not None:
            self.request_id = request_id

    @property
    def traffic_mirror_filter_rules(self):
        r"""Gets the traffic_mirror_filter_rules of this BatchCreateTrafficMirrorFilterRulesResponse.

        **参数解释**： 流量镜像筛选规则列表的响应体。 **取值范围**： 不涉及。

        :return: The traffic_mirror_filter_rules of this BatchCreateTrafficMirrorFilterRulesResponse.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        """
        return self._traffic_mirror_filter_rules

    @traffic_mirror_filter_rules.setter
    def traffic_mirror_filter_rules(self, traffic_mirror_filter_rules):
        r"""Sets the traffic_mirror_filter_rules of this BatchCreateTrafficMirrorFilterRulesResponse.

        **参数解释**： 流量镜像筛选规则列表的响应体。 **取值范围**： 不涉及。

        :param traffic_mirror_filter_rules: The traffic_mirror_filter_rules of this BatchCreateTrafficMirrorFilterRulesResponse.
        :type traffic_mirror_filter_rules: list[:class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`]
        """
        self._traffic_mirror_filter_rules = traffic_mirror_filter_rules

    @property
    def request_id(self):
        r"""Gets the request_id of this BatchCreateTrafficMirrorFilterRulesResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :return: The request_id of this BatchCreateTrafficMirrorFilterRulesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this BatchCreateTrafficMirrorFilterRulesResponse.

        **参数解释**： 请求ID。 **取值范围**： 不涉及。

        :param request_id: The request_id of this BatchCreateTrafficMirrorFilterRulesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    def to_dict(self):
        import warnings
        warnings.warn("BatchCreateTrafficMirrorFilterRulesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, BatchCreateTrafficMirrorFilterRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
