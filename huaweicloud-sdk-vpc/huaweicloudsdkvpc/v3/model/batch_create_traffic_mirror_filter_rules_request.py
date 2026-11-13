# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateTrafficMirrorFilterRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'traffic_mirror_filter_id': 'str',
        'body': 'BatchCreateTrafficMirrorFilterRulesRequestBody'
    }

    attribute_map = {
        'traffic_mirror_filter_id': 'traffic_mirror_filter_id',
        'body': 'body'
    }

    def __init__(self, traffic_mirror_filter_id=None, body=None):
        r"""BatchCreateTrafficMirrorFilterRulesRequest

        The model defined in huaweicloud sdk

        :param traffic_mirror_filter_id: 流量镜像筛选条件ID
        :type traffic_mirror_filter_id: str
        :param body: Body of the BatchCreateTrafficMirrorFilterRulesRequest
        :type body: :class:`huaweicloudsdkvpc.v3.BatchCreateTrafficMirrorFilterRulesRequestBody`
        """
        
        

        self._traffic_mirror_filter_id = None
        self._body = None
        self.discriminator = None

        self.traffic_mirror_filter_id = traffic_mirror_filter_id
        if body is not None:
            self.body = body

    @property
    def traffic_mirror_filter_id(self):
        r"""Gets the traffic_mirror_filter_id of this BatchCreateTrafficMirrorFilterRulesRequest.

        流量镜像筛选条件ID

        :return: The traffic_mirror_filter_id of this BatchCreateTrafficMirrorFilterRulesRequest.
        :rtype: str
        """
        return self._traffic_mirror_filter_id

    @traffic_mirror_filter_id.setter
    def traffic_mirror_filter_id(self, traffic_mirror_filter_id):
        r"""Sets the traffic_mirror_filter_id of this BatchCreateTrafficMirrorFilterRulesRequest.

        流量镜像筛选条件ID

        :param traffic_mirror_filter_id: The traffic_mirror_filter_id of this BatchCreateTrafficMirrorFilterRulesRequest.
        :type traffic_mirror_filter_id: str
        """
        self._traffic_mirror_filter_id = traffic_mirror_filter_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateTrafficMirrorFilterRulesRequest.

        :return: The body of this BatchCreateTrafficMirrorFilterRulesRequest.
        :rtype: :class:`huaweicloudsdkvpc.v3.BatchCreateTrafficMirrorFilterRulesRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateTrafficMirrorFilterRulesRequest.

        :param body: The body of this BatchCreateTrafficMirrorFilterRulesRequest.
        :type body: :class:`huaweicloudsdkvpc.v3.BatchCreateTrafficMirrorFilterRulesRequestBody`
        """
        self._body = body

    def to_dict(self):
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
        if not isinstance(other, BatchCreateTrafficMirrorFilterRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
