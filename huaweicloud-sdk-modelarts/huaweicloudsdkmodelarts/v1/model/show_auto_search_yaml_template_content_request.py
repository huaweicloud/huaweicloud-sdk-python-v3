# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoSearchYamlTemplateContentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_type': 'str',
        'algorithm_name': 'str'
    }

    attribute_map = {
        'algorithm_type': 'algorithm_type',
        'algorithm_name': 'algorithm_name'
    }

    def __init__(self, algorithm_type=None, algorithm_name=None):
        r"""ShowAutoSearchYamlTemplateContentRequest

        The model defined in huaweicloud sdk

        :param algorithm_type: 搜索算法类型。
        :type algorithm_type: str
        :param algorithm_name: 搜索算法名称。
        :type algorithm_name: str
        """
        
        

        self._algorithm_type = None
        self._algorithm_name = None
        self.discriminator = None

        self.algorithm_type = algorithm_type
        self.algorithm_name = algorithm_name

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this ShowAutoSearchYamlTemplateContentRequest.

        搜索算法类型。

        :return: The algorithm_type of this ShowAutoSearchYamlTemplateContentRequest.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this ShowAutoSearchYamlTemplateContentRequest.

        搜索算法类型。

        :param algorithm_type: The algorithm_type of this ShowAutoSearchYamlTemplateContentRequest.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def algorithm_name(self):
        r"""Gets the algorithm_name of this ShowAutoSearchYamlTemplateContentRequest.

        搜索算法名称。

        :return: The algorithm_name of this ShowAutoSearchYamlTemplateContentRequest.
        :rtype: str
        """
        return self._algorithm_name

    @algorithm_name.setter
    def algorithm_name(self, algorithm_name):
        r"""Sets the algorithm_name of this ShowAutoSearchYamlTemplateContentRequest.

        搜索算法名称。

        :param algorithm_name: The algorithm_name of this ShowAutoSearchYamlTemplateContentRequest.
        :type algorithm_name: str
        """
        self._algorithm_name = algorithm_name

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
        if not isinstance(other, ShowAutoSearchYamlTemplateContentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
