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
        'flowlog_id': 'str',
        'body': 'UpdateFlowLogReqBody'
    }

    attribute_map = {
        'flowlog_id': 'flowlog_id',
        'body': 'body'
    }

    def __init__(self, flowlog_id=None, body=None):
        """UpdateFlowLogRequest

        The model defined in huaweicloud sdk

        :param flowlog_id: 流日志资源唯一标识
        :type flowlog_id: str
        :param body: Body of the UpdateFlowLogRequest
        :type body: :class:`huaweicloudsdkvpc.v2.UpdateFlowLogReqBody`
        """
        
        

        self._flowlog_id = None
        self._body = None
        self.discriminator = None

        self.flowlog_id = flowlog_id
        if body is not None:
            self.body = body

    @property
    def flowlog_id(self):
        """Gets the flowlog_id of this UpdateFlowLogRequest.

        流日志资源唯一标识

        :return: The flowlog_id of this UpdateFlowLogRequest.
        :rtype: str
        """
        return self._flowlog_id

    @flowlog_id.setter
    def flowlog_id(self, flowlog_id):
        """Sets the flowlog_id of this UpdateFlowLogRequest.

        流日志资源唯一标识

        :param flowlog_id: The flowlog_id of this UpdateFlowLogRequest.
        :type flowlog_id: str
        """
        self._flowlog_id = flowlog_id

    @property
    def body(self):
        """Gets the body of this UpdateFlowLogRequest.

        :return: The body of this UpdateFlowLogRequest.
        :rtype: :class:`huaweicloudsdkvpc.v2.UpdateFlowLogReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateFlowLogRequest.

        :param body: The body of this UpdateFlowLogRequest.
        :type body: :class:`huaweicloudsdkvpc.v2.UpdateFlowLogReqBody`
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
