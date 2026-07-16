# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CoreRunVersionWeightResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_name': 'str',
        'weight': 'float'
    }

    attribute_map = {
        'version_name': 'version_name',
        'weight': 'weight'
    }

    def __init__(self, version_name=None, weight=None):
        r"""CoreRunVersionWeightResp

        The model defined in huaweicloud sdk

        :param version_name: **参数解释**: 版本名称。 
        :type version_name: str
        :param weight: **参数解释**: 流量权重比例 (0.0 - 1.0)。 
        :type weight: float
        """
        
        

        self._version_name = None
        self._weight = None
        self.discriminator = None

        if version_name is not None:
            self.version_name = version_name
        if weight is not None:
            self.weight = weight

    @property
    def version_name(self):
        r"""Gets the version_name of this CoreRunVersionWeightResp.

        **参数解释**: 版本名称。 

        :return: The version_name of this CoreRunVersionWeightResp.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this CoreRunVersionWeightResp.

        **参数解释**: 版本名称。 

        :param version_name: The version_name of this CoreRunVersionWeightResp.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def weight(self):
        r"""Gets the weight of this CoreRunVersionWeightResp.

        **参数解释**: 流量权重比例 (0.0 - 1.0)。 

        :return: The weight of this CoreRunVersionWeightResp.
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this CoreRunVersionWeightResp.

        **参数解释**: 流量权重比例 (0.0 - 1.0)。 

        :param weight: The weight of this CoreRunVersionWeightResp.
        :type weight: float
        """
        self._weight = weight

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
        if not isinstance(other, CoreRunVersionWeightResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
