# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowJobByIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_config': 'dict(str, object)',
        'job_info': 'StreamingJobInfoDto'
    }

    attribute_map = {
        'job_config': 'job_config',
        'job_info': 'job_info'
    }

    def __init__(self, job_config=None, job_info=None):
        """ShowJobByIdResponse

        The model defined in huaweicloud sdk

        :param job_config: 实时分析作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：实时分析算子配置指南。
        :type job_config: dict(str, object)
        :param job_info: 
        :type job_info: :class:`huaweicloudsdkiotanalytics.v1.StreamingJobInfoDto`
        """
        
        super(ShowJobByIdResponse, self).__init__()

        self._job_config = None
        self._job_info = None
        self.discriminator = None

        if job_config is not None:
            self.job_config = job_config
        if job_info is not None:
            self.job_info = job_info

    @property
    def job_config(self):
        """Gets the job_config of this ShowJobByIdResponse.

        实时分析作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：实时分析算子配置指南。

        :return: The job_config of this ShowJobByIdResponse.
        :rtype: dict(str, object)
        """
        return self._job_config

    @job_config.setter
    def job_config(self, job_config):
        """Sets the job_config of this ShowJobByIdResponse.

        实时分析作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：实时分析算子配置指南。

        :param job_config: The job_config of this ShowJobByIdResponse.
        :type job_config: dict(str, object)
        """
        self._job_config = job_config

    @property
    def job_info(self):
        """Gets the job_info of this ShowJobByIdResponse.

        :return: The job_info of this ShowJobByIdResponse.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.StreamingJobInfoDto`
        """
        return self._job_info

    @job_info.setter
    def job_info(self, job_info):
        """Sets the job_info of this ShowJobByIdResponse.

        :param job_info: The job_info of this ShowJobByIdResponse.
        :type job_info: :class:`huaweicloudsdkiotanalytics.v1.StreamingJobInfoDto`
        """
        self._job_info = job_info

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
        if not isinstance(other, ShowJobByIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
