# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VodRetrievalData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'retrieval_warm': 'float',
        'retrieval_cold': 'float',
        'retrieval_cold_speed': 'float'
    }

    attribute_map = {
        'retrieval_warm': 'retrieval_warm',
        'retrieval_cold': 'retrieval_cold',
        'retrieval_cold_speed': 'retrieval_cold_speed'
    }

    def __init__(self, retrieval_warm=None, retrieval_cold=None, retrieval_cold_speed=None):
        r"""VodRetrievalData

        The model defined in huaweicloud sdk

        :param retrieval_warm: 低频取回量 
        :type retrieval_warm: float
        :param retrieval_cold: 归档标准取回量 
        :type retrieval_cold: float
        :param retrieval_cold_speed: 归档快速取回量 
        :type retrieval_cold_speed: float
        """
        
        

        self._retrieval_warm = None
        self._retrieval_cold = None
        self._retrieval_cold_speed = None
        self.discriminator = None

        if retrieval_warm is not None:
            self.retrieval_warm = retrieval_warm
        if retrieval_cold is not None:
            self.retrieval_cold = retrieval_cold
        if retrieval_cold_speed is not None:
            self.retrieval_cold_speed = retrieval_cold_speed

    @property
    def retrieval_warm(self):
        r"""Gets the retrieval_warm of this VodRetrievalData.

        低频取回量 

        :return: The retrieval_warm of this VodRetrievalData.
        :rtype: float
        """
        return self._retrieval_warm

    @retrieval_warm.setter
    def retrieval_warm(self, retrieval_warm):
        r"""Sets the retrieval_warm of this VodRetrievalData.

        低频取回量 

        :param retrieval_warm: The retrieval_warm of this VodRetrievalData.
        :type retrieval_warm: float
        """
        self._retrieval_warm = retrieval_warm

    @property
    def retrieval_cold(self):
        r"""Gets the retrieval_cold of this VodRetrievalData.

        归档标准取回量 

        :return: The retrieval_cold of this VodRetrievalData.
        :rtype: float
        """
        return self._retrieval_cold

    @retrieval_cold.setter
    def retrieval_cold(self, retrieval_cold):
        r"""Sets the retrieval_cold of this VodRetrievalData.

        归档标准取回量 

        :param retrieval_cold: The retrieval_cold of this VodRetrievalData.
        :type retrieval_cold: float
        """
        self._retrieval_cold = retrieval_cold

    @property
    def retrieval_cold_speed(self):
        r"""Gets the retrieval_cold_speed of this VodRetrievalData.

        归档快速取回量 

        :return: The retrieval_cold_speed of this VodRetrievalData.
        :rtype: float
        """
        return self._retrieval_cold_speed

    @retrieval_cold_speed.setter
    def retrieval_cold_speed(self, retrieval_cold_speed):
        r"""Sets the retrieval_cold_speed of this VodRetrievalData.

        归档快速取回量 

        :param retrieval_cold_speed: The retrieval_cold_speed of this VodRetrievalData.
        :type retrieval_cold_speed: float
        """
        self._retrieval_cold_speed = retrieval_cold_speed

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
        if not isinstance(other, VodRetrievalData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
