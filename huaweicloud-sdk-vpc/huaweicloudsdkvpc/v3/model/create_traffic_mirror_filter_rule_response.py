# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTrafficMirrorFilterRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_mirror_filter_rule': 'TrafficMirrorFilterRule',
        'request_id': 'str'
    }

    attribute_map = {
        'traffic_mirror_filter_rule': 'traffic_mirror_filter_rule',
        'request_id': 'request_id'
    }

    def __init__(self, traffic_mirror_filter_rule=None, request_id=None):
        r"""CreateTrafficMirrorFilterRuleResponse

        The model defined in huaweicloud sdk

        :param traffic_mirror_filter_rule: 
        :type traffic_mirror_filter_rule: :class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(CreateTrafficMirrorFilterRuleResponse, self).__init__()

        self._traffic_mirror_filter_rule = None
        self._request_id = None
        self.discriminator = None

        if traffic_mirror_filter_rule is not None:
            self.traffic_mirror_filter_rule = traffic_mirror_filter_rule
        if request_id is not None:
            self.request_id = request_id

    @property
    def traffic_mirror_filter_rule(self):
        r"""Gets the traffic_mirror_filter_rule of this CreateTrafficMirrorFilterRuleResponse.

        :return: The traffic_mirror_filter_rule of this CreateTrafficMirrorFilterRuleResponse.
        :rtype: :class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`
        """
        return self._traffic_mirror_filter_rule

    @traffic_mirror_filter_rule.setter
    def traffic_mirror_filter_rule(self, traffic_mirror_filter_rule):
        r"""Sets the traffic_mirror_filter_rule of this CreateTrafficMirrorFilterRuleResponse.

        :param traffic_mirror_filter_rule: The traffic_mirror_filter_rule of this CreateTrafficMirrorFilterRuleResponse.
        :type traffic_mirror_filter_rule: :class:`huaweicloudsdkvpc.v3.TrafficMirrorFilterRule`
        """
        self._traffic_mirror_filter_rule = traffic_mirror_filter_rule

    @property
    def request_id(self):
        r"""Gets the request_id of this CreateTrafficMirrorFilterRuleResponse.

        请求ID

        :return: The request_id of this CreateTrafficMirrorFilterRuleResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this CreateTrafficMirrorFilterRuleResponse.

        请求ID

        :param request_id: The request_id of this CreateTrafficMirrorFilterRuleResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, CreateTrafficMirrorFilterRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
