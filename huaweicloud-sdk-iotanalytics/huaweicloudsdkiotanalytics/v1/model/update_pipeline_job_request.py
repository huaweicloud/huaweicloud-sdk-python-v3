# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePipelineJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check': 'bool',
        'pipeline_id': 'str',
        'body': 'dict(str, object)'
    }

    attribute_map = {
        'check': 'check',
        'pipeline_id': 'pipeline_id',
        'body': 'body'
    }

    def __init__(self, check=None, pipeline_id=None, body=None):
        """UpdatePipelineJobRequest

        The model defined in huaweicloud sdk

        :param check: 是否需要校验配置是否正确
        :type check: bool
        :param pipeline_id: 管道ID
        :type pipeline_id: str
        :param body: 管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。
        :type body: dict(str, object)
        """
        
        

        self._check = None
        self._pipeline_id = None
        self._body = None
        self.discriminator = None

        if check is not None:
            self.check = check
        self.pipeline_id = pipeline_id
        if body is not None:
            self.body = body

    @property
    def check(self):
        """Gets the check of this UpdatePipelineJobRequest.

        是否需要校验配置是否正确

        :return: The check of this UpdatePipelineJobRequest.
        :rtype: bool
        """
        return self._check

    @check.setter
    def check(self, check):
        """Sets the check of this UpdatePipelineJobRequest.

        是否需要校验配置是否正确

        :param check: The check of this UpdatePipelineJobRequest.
        :type check: bool
        """
        self._check = check

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this UpdatePipelineJobRequest.

        管道ID

        :return: The pipeline_id of this UpdatePipelineJobRequest.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this UpdatePipelineJobRequest.

        管道ID

        :param pipeline_id: The pipeline_id of this UpdatePipelineJobRequest.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def body(self):
        """Gets the body of this UpdatePipelineJobRequest.

        管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。

        :return: The body of this UpdatePipelineJobRequest.
        :rtype: dict(str, object)
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePipelineJobRequest.

        管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。

        :param body: The body of this UpdatePipelineJobRequest.
        :type body: dict(str, object)
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
        if not isinstance(other, UpdatePipelineJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
