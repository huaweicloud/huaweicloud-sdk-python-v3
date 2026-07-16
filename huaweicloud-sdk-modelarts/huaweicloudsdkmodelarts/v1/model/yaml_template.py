# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class YamlTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'algorithm_type_en': 'str',
        'algorithm_type_zh': 'str',
        'algorithm_names': 'list[str]'
    }

    attribute_map = {
        'algorithm_type_en': 'algorithm_type_en',
        'algorithm_type_zh': 'algorithm_type_zh',
        'algorithm_names': 'algorithm_names'
    }

    def __init__(self, algorithm_type_en=None, algorithm_type_zh=None, algorithm_names=None):
        r"""YamlTemplate

        The model defined in huaweicloud sdk

        :param algorithm_type_en: AutoSearch算法类型，英文描述。
        :type algorithm_type_en: str
        :param algorithm_type_zh: AutoSearch算法类型[，中文描述](tag:hc,hk)。
        :type algorithm_type_zh: str
        :param algorithm_names: 该算法类型下所有算法的名称。
        :type algorithm_names: list[str]
        """
        
        

        self._algorithm_type_en = None
        self._algorithm_type_zh = None
        self._algorithm_names = None
        self.discriminator = None

        if algorithm_type_en is not None:
            self.algorithm_type_en = algorithm_type_en
        if algorithm_type_zh is not None:
            self.algorithm_type_zh = algorithm_type_zh
        if algorithm_names is not None:
            self.algorithm_names = algorithm_names

    @property
    def algorithm_type_en(self):
        r"""Gets the algorithm_type_en of this YamlTemplate.

        AutoSearch算法类型，英文描述。

        :return: The algorithm_type_en of this YamlTemplate.
        :rtype: str
        """
        return self._algorithm_type_en

    @algorithm_type_en.setter
    def algorithm_type_en(self, algorithm_type_en):
        r"""Sets the algorithm_type_en of this YamlTemplate.

        AutoSearch算法类型，英文描述。

        :param algorithm_type_en: The algorithm_type_en of this YamlTemplate.
        :type algorithm_type_en: str
        """
        self._algorithm_type_en = algorithm_type_en

    @property
    def algorithm_type_zh(self):
        r"""Gets the algorithm_type_zh of this YamlTemplate.

        AutoSearch算法类型[，中文描述](tag:hc,hk)。

        :return: The algorithm_type_zh of this YamlTemplate.
        :rtype: str
        """
        return self._algorithm_type_zh

    @algorithm_type_zh.setter
    def algorithm_type_zh(self, algorithm_type_zh):
        r"""Sets the algorithm_type_zh of this YamlTemplate.

        AutoSearch算法类型[，中文描述](tag:hc,hk)。

        :param algorithm_type_zh: The algorithm_type_zh of this YamlTemplate.
        :type algorithm_type_zh: str
        """
        self._algorithm_type_zh = algorithm_type_zh

    @property
    def algorithm_names(self):
        r"""Gets the algorithm_names of this YamlTemplate.

        该算法类型下所有算法的名称。

        :return: The algorithm_names of this YamlTemplate.
        :rtype: list[str]
        """
        return self._algorithm_names

    @algorithm_names.setter
    def algorithm_names(self, algorithm_names):
        r"""Sets the algorithm_names of this YamlTemplate.

        该算法类型下所有算法的名称。

        :param algorithm_names: The algorithm_names of this YamlTemplate.
        :type algorithm_names: list[str]
        """
        self._algorithm_names = algorithm_names

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
        if not isinstance(other, YamlTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
