# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlowLogRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'flow_log_id': 'str',
        'body': 'UpdateFlowLogRequestBody'
    }

    attribute_map = {
        'er_id': 'er_id',
        'flow_log_id': 'flow_log_id',
        'body': 'body'
    }

    def __init__(self, er_id=None, flow_log_id=None, body=None):
        r"""UpdateFlowLogRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param flow_log_id: 流日志ID
        :type flow_log_id: str
        :param body: Body of the UpdateFlowLogRequest
        :type body: :class:`huaweicloudsdker.v3.UpdateFlowLogRequestBody`
        """
        
        

        self._er_id = None
        self._flow_log_id = None
        self._body = None
        self.discriminator = None

        self.er_id = er_id
        self.flow_log_id = flow_log_id
        if body is not None:
            self.body = body

    @property
    def er_id(self):
        r"""Gets the er_id of this UpdateFlowLogRequest.

        企业路由器实例ID

        :return: The er_id of this UpdateFlowLogRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        r"""Sets the er_id of this UpdateFlowLogRequest.

        企业路由器实例ID

        :param er_id: The er_id of this UpdateFlowLogRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def flow_log_id(self):
        r"""Gets the flow_log_id of this UpdateFlowLogRequest.

        流日志ID

        :return: The flow_log_id of this UpdateFlowLogRequest.
        :rtype: str
        """
        return self._flow_log_id

    @flow_log_id.setter
    def flow_log_id(self, flow_log_id):
        r"""Sets the flow_log_id of this UpdateFlowLogRequest.

        流日志ID

        :param flow_log_id: The flow_log_id of this UpdateFlowLogRequest.
        :type flow_log_id: str
        """
        self._flow_log_id = flow_log_id

    @property
    def body(self):
        r"""Gets the body of this UpdateFlowLogRequest.

        :return: The body of this UpdateFlowLogRequest.
        :rtype: :class:`huaweicloudsdker.v3.UpdateFlowLogRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateFlowLogRequest.

        :param body: The body of this UpdateFlowLogRequest.
        :type body: :class:`huaweicloudsdker.v3.UpdateFlowLogRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateFlowLogRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
