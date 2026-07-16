# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlgorithmByUuidRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_id': 'str'
    }

    attribute_map = {
        'algorithm_id': 'algorithm_id'
    }

    def __init__(self, algorithm_id=None):
        r"""ShowAlgorithmByUuidRequest

        The model defined in huaweicloud sdk

        :param algorithm_id: 算法ID。
        :type algorithm_id: str
        """
        
        

        self._algorithm_id = None
        self.discriminator = None

        self.algorithm_id = algorithm_id

    @property
    def algorithm_id(self):
        r"""Gets the algorithm_id of this ShowAlgorithmByUuidRequest.

        算法ID。

        :return: The algorithm_id of this ShowAlgorithmByUuidRequest.
        :rtype: str
        """
        return self._algorithm_id

    @algorithm_id.setter
    def algorithm_id(self, algorithm_id):
        r"""Sets the algorithm_id of this ShowAlgorithmByUuidRequest.

        算法ID。

        :param algorithm_id: The algorithm_id of this ShowAlgorithmByUuidRequest.
        :type algorithm_id: str
        """
        self._algorithm_id = algorithm_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAlgorithmByUuidRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
