# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EditMediaTask:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'inputs': 'list[EditMediaTaskInput]',
        'output': 'TaskOutPut'
    }

    attribute_map = {
        'inputs': 'inputs',
        'output': 'output'
    }

    def __init__(self, inputs=None, output=None):
        r"""EditMediaTask

        The model defined in huaweicloud sdk

        :param inputs: 剪辑任务的输入文件信息
        :type inputs: list[:class:`huaweicloudsdkvod.v1.EditMediaTaskInput`]
        :param output: 
        :type output: :class:`huaweicloudsdkvod.v1.TaskOutPut`
        """
        
        

        self._inputs = None
        self._output = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if output is not None:
            self.output = output

    @property
    def inputs(self):
        r"""Gets the inputs of this EditMediaTask.

        剪辑任务的输入文件信息

        :return: The inputs of this EditMediaTask.
        :rtype: list[:class:`huaweicloudsdkvod.v1.EditMediaTaskInput`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this EditMediaTask.

        剪辑任务的输入文件信息

        :param inputs: The inputs of this EditMediaTask.
        :type inputs: list[:class:`huaweicloudsdkvod.v1.EditMediaTaskInput`]
        """
        self._inputs = inputs

    @property
    def output(self):
        r"""Gets the output of this EditMediaTask.

        :return: The output of this EditMediaTask.
        :rtype: :class:`huaweicloudsdkvod.v1.TaskOutPut`
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this EditMediaTask.

        :param output: The output of this EditMediaTask.
        :type output: :class:`huaweicloudsdkvod.v1.TaskOutPut`
        """
        self._output = output

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
        if not isinstance(other, EditMediaTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
