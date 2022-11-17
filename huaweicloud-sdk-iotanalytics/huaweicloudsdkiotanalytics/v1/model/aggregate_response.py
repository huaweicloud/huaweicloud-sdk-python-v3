# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AggregateResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[InputResponse]',
        'expression': 'Expression',
        'output_property': 'str',
        'outputs': 'list[OutputResponse]',
        'schedule': 'DTSchedule'
    }

    attribute_map = {
        'inputs': 'inputs',
        'expression': 'expression',
        'output_property': 'output_property',
        'outputs': 'outputs',
        'schedule': 'schedule'
    }

    def __init__(self, inputs=None, expression=None, output_property=None, outputs=None, schedule=None):
        """AggregateResponse

        The model defined in huaweicloud sdk

        :param inputs: 输入参数
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputResponse`]
        :param expression: 
        :type expression: :class:`huaweicloudsdkiotanalytics.v1.Expression`
        :param output_property: 输出属性名(不推荐使用，待废弃，使用outputs替代)
        :type output_property: str
        :param outputs: 
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.OutputResponse`]
        :param schedule: 
        :type schedule: :class:`huaweicloudsdkiotanalytics.v1.DTSchedule`
        """
        
        

        self._inputs = None
        self._expression = None
        self._output_property = None
        self._outputs = None
        self._schedule = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if expression is not None:
            self.expression = expression
        if output_property is not None:
            self.output_property = output_property
        if outputs is not None:
            self.outputs = outputs
        if schedule is not None:
            self.schedule = schedule

    @property
    def inputs(self):
        """Gets the inputs of this AggregateResponse.

        输入参数

        :return: The inputs of this AggregateResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.InputResponse`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this AggregateResponse.

        输入参数

        :param inputs: The inputs of this AggregateResponse.
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputResponse`]
        """
        self._inputs = inputs

    @property
    def expression(self):
        """Gets the expression of this AggregateResponse.

        :return: The expression of this AggregateResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.Expression`
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this AggregateResponse.

        :param expression: The expression of this AggregateResponse.
        :type expression: :class:`huaweicloudsdkiotanalytics.v1.Expression`
        """
        self._expression = expression

    @property
    def output_property(self):
        """Gets the output_property of this AggregateResponse.

        输出属性名(不推荐使用，待废弃，使用outputs替代)

        :return: The output_property of this AggregateResponse.
        :rtype: str
        """
        return self._output_property

    @output_property.setter
    def output_property(self, output_property):
        """Sets the output_property of this AggregateResponse.

        输出属性名(不推荐使用，待废弃，使用outputs替代)

        :param output_property: The output_property of this AggregateResponse.
        :type output_property: str
        """
        self._output_property = output_property

    @property
    def outputs(self):
        """Gets the outputs of this AggregateResponse.

        :return: The outputs of this AggregateResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.OutputResponse`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this AggregateResponse.

        :param outputs: The outputs of this AggregateResponse.
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.OutputResponse`]
        """
        self._outputs = outputs

    @property
    def schedule(self):
        """Gets the schedule of this AggregateResponse.

        :return: The schedule of this AggregateResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.DTSchedule`
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this AggregateResponse.

        :param schedule: The schedule of this AggregateResponse.
        :type schedule: :class:`huaweicloudsdkiotanalytics.v1.DTSchedule`
        """
        self._schedule = schedule

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
        if not isinstance(other, AggregateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
