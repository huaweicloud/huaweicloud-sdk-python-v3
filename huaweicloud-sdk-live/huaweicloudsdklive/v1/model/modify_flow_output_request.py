# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyFlowOutputRequest:

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
        'output_name': 'str',
        'body': 'UpdateFlowOutputRequestBody'
    }

    attribute_map = {
        'flow_id': 'flow_id',
        'output_name': 'output_name',
        'body': 'body'
    }

    def __init__(self, flow_id=None, output_name=None, body=None):
        r"""ModifyFlowOutputRequest

        The model defined in huaweicloud sdk

        :param flow_id: 流id
        :type flow_id: str
        :param output_name: 输出名称
        :type output_name: str
        :param body: Body of the ModifyFlowOutputRequest
        :type body: :class:`huaweicloudsdklive.v1.UpdateFlowOutputRequestBody`
        """
        
        

        self._flow_id = None
        self._output_name = None
        self._body = None
        self.discriminator = None

        self.flow_id = flow_id
        self.output_name = output_name
        if body is not None:
            self.body = body

    @property
    def flow_id(self):
        r"""Gets the flow_id of this ModifyFlowOutputRequest.

        流id

        :return: The flow_id of this ModifyFlowOutputRequest.
        :rtype: str
        """
        return self._flow_id

    @flow_id.setter
    def flow_id(self, flow_id):
        r"""Sets the flow_id of this ModifyFlowOutputRequest.

        流id

        :param flow_id: The flow_id of this ModifyFlowOutputRequest.
        :type flow_id: str
        """
        self._flow_id = flow_id

    @property
    def output_name(self):
        r"""Gets the output_name of this ModifyFlowOutputRequest.

        输出名称

        :return: The output_name of this ModifyFlowOutputRequest.
        :rtype: str
        """
        return self._output_name

    @output_name.setter
    def output_name(self, output_name):
        r"""Sets the output_name of this ModifyFlowOutputRequest.

        输出名称

        :param output_name: The output_name of this ModifyFlowOutputRequest.
        :type output_name: str
        """
        self._output_name = output_name

    @property
    def body(self):
        r"""Gets the body of this ModifyFlowOutputRequest.

        :return: The body of this ModifyFlowOutputRequest.
        :rtype: :class:`huaweicloudsdklive.v1.UpdateFlowOutputRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ModifyFlowOutputRequest.

        :param body: The body of this ModifyFlowOutputRequest.
        :type body: :class:`huaweicloudsdklive.v1.UpdateFlowOutputRequestBody`
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
        if not isinstance(other, ModifyFlowOutputRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
