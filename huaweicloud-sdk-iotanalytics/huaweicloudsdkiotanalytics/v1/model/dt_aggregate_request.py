# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DTAggregateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'inputs': 'list[InputRequest]',
        'outputs': 'list[OutputRequest]'
    }

    attribute_map = {
        'inputs': 'inputs',
        'outputs': 'outputs'
    }

    def __init__(self, inputs=None, outputs=None):
        """DTAggregateRequest

        The model defined in huaweicloud sdk

        :param inputs: 输入参数，最多支持10个
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputRequest`]
        :param outputs: 
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.OutputRequest`]
        """
        
        

        self._inputs = None
        self._outputs = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if outputs is not None:
            self.outputs = outputs

    @property
    def inputs(self):
        """Gets the inputs of this DTAggregateRequest.

        输入参数，最多支持10个

        :return: The inputs of this DTAggregateRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.InputRequest`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this DTAggregateRequest.

        输入参数，最多支持10个

        :param inputs: The inputs of this DTAggregateRequest.
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputRequest`]
        """
        self._inputs = inputs

    @property
    def outputs(self):
        """Gets the outputs of this DTAggregateRequest.


        :return: The outputs of this DTAggregateRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.OutputRequest`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this DTAggregateRequest.


        :param outputs: The outputs of this DTAggregateRequest.
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.OutputRequest`]
        """
        self._outputs = outputs

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
        if not isinstance(other, DTAggregateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
