# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StreamResponse:

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
        'job_id': 'str',
        'outputs': 'list[StreamOutput]'
    }

    attribute_map = {
        'inputs': 'inputs',
        'job_id': 'job_id',
        'outputs': 'outputs'
    }

    def __init__(self, inputs=None, job_id=None, outputs=None):
        """StreamResponse

        The model defined in huaweicloud sdk

        :param inputs: 输入参数
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputResponse`]
        :param job_id: 流计算任务ID
        :type job_id: str
        :param outputs: 输出属性，最多支持10个
        :type outputs: list[:class:`huaweicloudsdkiotanalytics.v1.StreamOutput`]
        """
        
        

        self._inputs = None
        self._job_id = None
        self._outputs = None
        self.discriminator = None

        if inputs is not None:
            self.inputs = inputs
        if job_id is not None:
            self.job_id = job_id
        if outputs is not None:
            self.outputs = outputs

    @property
    def inputs(self):
        """Gets the inputs of this StreamResponse.

        输入参数

        :return: The inputs of this StreamResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.InputResponse`]
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this StreamResponse.

        输入参数

        :param inputs: The inputs of this StreamResponse.
        :type inputs: list[:class:`huaweicloudsdkiotanalytics.v1.InputResponse`]
        """
        self._inputs = inputs

    @property
    def job_id(self):
        """Gets the job_id of this StreamResponse.

        流计算任务ID

        :return: The job_id of this StreamResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this StreamResponse.

        流计算任务ID

        :param job_id: The job_id of this StreamResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def outputs(self):
        """Gets the outputs of this StreamResponse.

        输出属性，最多支持10个

        :return: The outputs of this StreamResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.StreamOutput`]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this StreamResponse.

        输出属性，最多支持10个

        :param outputs: The outputs of this StreamResponse.
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
        if not isinstance(other, StreamResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
