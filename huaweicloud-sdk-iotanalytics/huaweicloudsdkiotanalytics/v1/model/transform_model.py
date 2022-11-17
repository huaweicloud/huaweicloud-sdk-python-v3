# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransformModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[InputModel]',
        'expression': 'Formula',
        'output_property': 'str',
        'outputs': 'list[OutputWithModel]'
    }

    attribute_map = {
        'inputs': 'inputs',
        'expression': 'expression',
        'output_property': 'output_property',
        'outputs': 'outputs'
    }

    def __init__(self, inputs=None, expression=None, output_property=None, outputs=None):
        """TransformModel

        The model defined in huaweicloud sdk

        :param inputs: 输入参数，最多支持10个
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputModel`]
        :param expression: 
        :type expression: :class:`huaweicloudsdkiotanalytics.v1.Formula`
        :param output_property: 输出属性名(分析任务单输出场景，配合expression的formula使用)
        :type output_property: str
        :param outputs: 输出属性，最多支持10个
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.OutputWithModel`]
        """
        
        

        self._inputs = None
        self._expression = None
        self._output_property = None
        self._outputs = None
        self.discriminator = None

        self.inputs = inputs
        self.expression = expression
        if output_property is not None:
            self.output_property = output_property
        if outputs is not None:
            self.outputs = outputs

    @property
    def inputs(self):
        """Gets the inputs of this TransformModel.

        输入参数，最多支持10个

        :return: The inputs of this TransformModel.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.InputModel`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this TransformModel.

        输入参数，最多支持10个

        :param inputs: The inputs of this TransformModel.
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputModel`]
        """
        self._inputs = inputs

    @property
    def expression(self):
        """Gets the expression of this TransformModel.

        :return: The expression of this TransformModel.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.Formula`
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this TransformModel.

        :param expression: The expression of this TransformModel.
        :type expression: :class:`huaweicloudsdkiotanalytics.v1.Formula`
        """
        self._expression = expression

    @property
    def output_property(self):
        """Gets the output_property of this TransformModel.

        输出属性名(分析任务单输出场景，配合expression的formula使用)

        :return: The output_property of this TransformModel.
        :rtype: str
        """
        return self._output_property

    @output_property.setter
    def output_property(self, output_property):
        """Sets the output_property of this TransformModel.

        输出属性名(分析任务单输出场景，配合expression的formula使用)

        :param output_property: The output_property of this TransformModel.
        :type output_property: str
        """
        self._output_property = output_property

    @property
    def outputs(self):
        """Gets the outputs of this TransformModel.

        输出属性，最多支持10个

        :return: The outputs of this TransformModel.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.OutputWithModel`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this TransformModel.

        输出属性，最多支持10个

        :param outputs: The outputs of this TransformModel.
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.OutputWithModel`]
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
        if not isinstance(other, TransformModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
