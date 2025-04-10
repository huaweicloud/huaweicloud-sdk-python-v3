# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineMoveToGroupResponseVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'pipeline_id': 'str',
        'pipeline_name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'pipeline_id': 'pipeline_id',
        'pipeline_name': 'pipeline_name'
    }

    def __init__(self, code=None, pipeline_id=None, pipeline_name=None):
        r"""PipelineMoveToGroupResponseVo

        The model defined in huaweicloud sdk

        :param code: 响应码 [\&quot;failed\&quot;, \&quot;success\&quot;]
        :type code: str
        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param pipeline_name: 流水线名
        :type pipeline_name: str
        """
        
        

        self._code = None
        self._pipeline_id = None
        self._pipeline_name = None
        self.discriminator = None

        self.code = code
        self.pipeline_id = pipeline_id
        self.pipeline_name = pipeline_name

    @property
    def code(self):
        r"""Gets the code of this PipelineMoveToGroupResponseVo.

        响应码 [\"failed\", \"success\"]

        :return: The code of this PipelineMoveToGroupResponseVo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this PipelineMoveToGroupResponseVo.

        响应码 [\"failed\", \"success\"]

        :param code: The code of this PipelineMoveToGroupResponseVo.
        :type code: str
        """
        self._code = code

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this PipelineMoveToGroupResponseVo.

        流水线ID

        :return: The pipeline_id of this PipelineMoveToGroupResponseVo.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this PipelineMoveToGroupResponseVo.

        流水线ID

        :param pipeline_id: The pipeline_id of this PipelineMoveToGroupResponseVo.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def pipeline_name(self):
        r"""Gets the pipeline_name of this PipelineMoveToGroupResponseVo.

        流水线名

        :return: The pipeline_name of this PipelineMoveToGroupResponseVo.
        :rtype: str
        """
        return self._pipeline_name

    @pipeline_name.setter
    def pipeline_name(self, pipeline_name):
        r"""Sets the pipeline_name of this PipelineMoveToGroupResponseVo.

        流水线名

        :param pipeline_name: The pipeline_name of this PipelineMoveToGroupResponseVo.
        :type pipeline_name: str
        """
        self._pipeline_name = pipeline_name

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
        if not isinstance(other, PipelineMoveToGroupResponseVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
