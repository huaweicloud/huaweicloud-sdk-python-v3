# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFlowRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flow_id': 'str',
        'body': 'FlowMeta'
    }

    attribute_map = {
        'flow_id': 'flow_id',
        'body': 'body'
    }

    def __init__(self, flow_id=None, body=None):
        """UpdateFlowRequest

        The model defined in huaweicloud sdk

        :param flow_id: flow_id
        :type flow_id: str
        :param body: Body of the UpdateFlowRequest
        :type body: :class:`huaweicloudsdkmssi.v1.FlowMeta`
        """
        
        

        self._flow_id = None
        self._body = None
        self.discriminator = None

        self.flow_id = flow_id
        if body is not None:
            self.body = body

    @property
    def flow_id(self):
        """Gets the flow_id of this UpdateFlowRequest.

        flow_id

        :return: The flow_id of this UpdateFlowRequest.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        """Sets the flow_id of this UpdateFlowRequest.

        flow_id

        :param flow_id: The flow_id of this UpdateFlowRequest.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def body(self):
        """Gets the body of this UpdateFlowRequest.

        :return: The body of this UpdateFlowRequest.
        :rtype: :class:`huaweicloudsdkmssi.v1.FlowMeta`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateFlowRequest.

        :param body: The body of this UpdateFlowRequest.
        :type body: :class:`huaweicloudsdkmssi.v1.FlowMeta`
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
        if not isinstance(other, UpdateFlowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
