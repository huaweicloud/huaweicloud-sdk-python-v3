# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPipelineJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_config': 'dict(str, object)',
        'pipeline_info': 'PipelineJobInfoDto'
    }

    attribute_map = {
        'pipeline_config': 'pipeline_config',
        'pipeline_info': 'pipeline_info'
    }

    def __init__(self, pipeline_config=None, pipeline_info=None):
        """ShowPipelineJobResponse

        The model defined in huaweicloud sdk

        :param pipeline_config: 管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。
        :type pipeline_config: dict(str, object)
        :param pipeline_info: 
        :type pipeline_info: :class:`huaweicloudsdkiotanalytics.v1.PipelineJobInfoDto`
        """
        
        super(ShowPipelineJobResponse, self).__init__()

        self._pipeline_config = None
        self._pipeline_info = None
        self.discriminator = None

        if pipeline_config is not None:
            self.pipeline_config = pipeline_config
        if pipeline_info is not None:
            self.pipeline_info = pipeline_info

    @property
    def pipeline_config(self):
        """Gets the pipeline_config of this ShowPipelineJobResponse.

        管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。

        :return: The pipeline_config of this ShowPipelineJobResponse.
        :rtype: dict(str, object)
        """
        return self._pipeline_config

    @pipeline_config.setter
    def pipeline_config(self, pipeline_config):
        """Sets the pipeline_config of this ShowPipelineJobResponse.

        管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。

        :param pipeline_config: The pipeline_config of this ShowPipelineJobResponse.
        :type pipeline_config: dict(str, object)
        """
        self._pipeline_config = pipeline_config

    @property
    def pipeline_info(self):
        """Gets the pipeline_info of this ShowPipelineJobResponse.

        :return: The pipeline_info of this ShowPipelineJobResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.PipelineJobInfoDto`
        """
        return self._pipeline_info

    @pipeline_info.setter
    def pipeline_info(self, pipeline_info):
        """Sets the pipeline_info of this ShowPipelineJobResponse.

        :param pipeline_info: The pipeline_info of this ShowPipelineJobResponse.
        :type pipeline_info: :class:`huaweicloudsdkiotanalytics.v1.PipelineJobInfoDto`
        """
        self._pipeline_info = pipeline_info

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
        if not isinstance(other, ShowPipelineJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
