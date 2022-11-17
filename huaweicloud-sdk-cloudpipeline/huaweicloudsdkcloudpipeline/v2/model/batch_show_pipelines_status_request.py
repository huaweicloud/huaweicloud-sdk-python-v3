# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchShowPipelinesStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'pipeline_ids': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'pipeline_ids': 'pipeline_ids'
    }

    def __init__(self, x_language=None, pipeline_ids=None):
        """BatchShowPipelinesStatusRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us，默认en-us
        :type x_language: str
        :param pipeline_ids: 要获取状态的流水线ID，用逗号隔开
        :type pipeline_ids: str
        """
        
        

        self._x_language = None
        self._pipeline_ids = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.pipeline_ids = pipeline_ids

    @property
    def x_language(self):
        """Gets the x_language of this BatchShowPipelinesStatusRequest.

        语言类型 中文:zh-cn 英文:en-us，默认en-us

        :return: The x_language of this BatchShowPipelinesStatusRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this BatchShowPipelinesStatusRequest.

        语言类型 中文:zh-cn 英文:en-us，默认en-us

        :param x_language: The x_language of this BatchShowPipelinesStatusRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def pipeline_ids(self):
        """Gets the pipeline_ids of this BatchShowPipelinesStatusRequest.

        要获取状态的流水线ID，用逗号隔开

        :return: The pipeline_ids of this BatchShowPipelinesStatusRequest.
        :rtype: str
        """
        return self._pipeline_ids

    @pipeline_ids.setter
    def pipeline_ids(self, pipeline_ids):
        """Sets the pipeline_ids of this BatchShowPipelinesStatusRequest.

        要获取状态的流水线ID，用逗号隔开

        :param pipeline_ids: The pipeline_ids of this BatchShowPipelinesStatusRequest.
        :type pipeline_ids: str
        """
        self._pipeline_ids = pipeline_ids

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
        if not isinstance(other, BatchShowPipelinesStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
