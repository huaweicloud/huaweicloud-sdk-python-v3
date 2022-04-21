# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartPipelineJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'parallel': 'int',
        'rtu': 'int',
        'resume_savepoint': 'bool'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'parallel': 'parallel',
        'rtu': 'rtu',
        'resume_savepoint': 'resume_savepoint'
    }

    def __init__(self, pipeline_id=None, parallel=None, rtu=None, resume_savepoint=None):
        """StartPipelineJobRequest

        The model defined in huaweicloud sdk

        :param pipeline_id: 管道ID
        :type pipeline_id: str
        :param parallel: 运行管道的并发度
        :type parallel: int
        :param rtu: 运行管道的RTU个数
        :type rtu: int
        :param resume_savepoint: 运行管道作业使用历史缓存数据
        :type resume_savepoint: bool
        """
        
        

        self._pipeline_id = None
        self._parallel = None
        self._rtu = None
        self._resume_savepoint = None
        self.discriminator = None

        self.pipeline_id = pipeline_id
        if parallel is not None:
            self.parallel = parallel
        if rtu is not None:
            self.rtu = rtu
        if resume_savepoint is not None:
            self.resume_savepoint = resume_savepoint

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this StartPipelineJobRequest.

        管道ID

        :return: The pipeline_id of this StartPipelineJobRequest.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this StartPipelineJobRequest.

        管道ID

        :param pipeline_id: The pipeline_id of this StartPipelineJobRequest.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def parallel(self):
        """Gets the parallel of this StartPipelineJobRequest.

        运行管道的并发度

        :return: The parallel of this StartPipelineJobRequest.
        :rtype: int
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this StartPipelineJobRequest.

        运行管道的并发度

        :param parallel: The parallel of this StartPipelineJobRequest.
        :type parallel: int
        """
        self._parallel = parallel

    @property
    def rtu(self):
        """Gets the rtu of this StartPipelineJobRequest.

        运行管道的RTU个数

        :return: The rtu of this StartPipelineJobRequest.
        :rtype: int
        """
        return self._rtu

    @rtu.setter
    def rtu(self, rtu):
        """Sets the rtu of this StartPipelineJobRequest.

        运行管道的RTU个数

        :param rtu: The rtu of this StartPipelineJobRequest.
        :type rtu: int
        """
        self._rtu = rtu

    @property
    def resume_savepoint(self):
        """Gets the resume_savepoint of this StartPipelineJobRequest.

        运行管道作业使用历史缓存数据

        :return: The resume_savepoint of this StartPipelineJobRequest.
        :rtype: bool
        """
        return self._resume_savepoint

    @resume_savepoint.setter
    def resume_savepoint(self, resume_savepoint):
        """Sets the resume_savepoint of this StartPipelineJobRequest.

        运行管道作业使用历史缓存数据

        :param resume_savepoint: The resume_savepoint of this StartPipelineJobRequest.
        :type resume_savepoint: bool
        """
        self._resume_savepoint = resume_savepoint

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
        if not isinstance(other, StartPipelineJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
