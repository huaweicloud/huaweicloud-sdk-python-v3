# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamModel:

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
        'job_id': 'str',
        'outputs': 'list[StreamOutput]'
    }

    attribute_map = {
        'inputs': 'inputs',
        'job_id': 'job_id',
        'outputs': 'outputs'
    }

    def __init__(self, inputs=None, job_id=None, outputs=None):
        r"""StreamModel

        The model defined in huaweicloud sdk

        :param inputs: 输入参数，最多支持10个；流计算的输入参数名需要在接收数据类型为资产数据的实时分析作业中定义，模型中必须与其保持一致
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputModel`]
        :param job_id: 实时分析作业ID
        :type job_id: str
        :param outputs: 输出属性，最多支持10个
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.StreamOutput`]
        """
        
        

        self._inputs = None
        self._job_id = None
        self._outputs = None
        self.discriminator = None

        self.inputs = inputs
        self.job_id = job_id
        self.outputs = outputs

    @property
    def inputs(self):
        r"""Gets the inputs of this StreamModel.

        输入参数，最多支持10个；流计算的输入参数名需要在接收数据类型为资产数据的实时分析作业中定义，模型中必须与其保持一致

        :return: The inputs of this StreamModel.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.InputModel`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this StreamModel.

        输入参数，最多支持10个；流计算的输入参数名需要在接收数据类型为资产数据的实时分析作业中定义，模型中必须与其保持一致

        :param inputs: The inputs of this StreamModel.
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputModel`]
        """
        self._inputs = inputs

    @property
    def job_id(self):
        r"""Gets the job_id of this StreamModel.

        实时分析作业ID

        :return: The job_id of this StreamModel.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this StreamModel.

        实时分析作业ID

        :param job_id: The job_id of this StreamModel.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def outputs(self):
        r"""Gets the outputs of this StreamModel.

        输出属性，最多支持10个

        :return: The outputs of this StreamModel.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.StreamOutput`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        r"""Sets the outputs of this StreamModel.

        输出属性，最多支持10个

        :param outputs: The outputs of this StreamModel.
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.StreamOutput`]
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
        if not isinstance(other, StreamModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
