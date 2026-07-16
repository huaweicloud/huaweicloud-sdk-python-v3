# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'params': 'list[AutoSearchAlgoConfigParameter]'
    }

    attribute_map = {
        'name': 'name',
        'params': 'params'
    }

    def __init__(self, name=None, params=None):
        r"""JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs

        The model defined in huaweicloud sdk

        :param name: 搜索算法名称。
        :type name: str
        :param params: 搜索算法参数。
        :type params: list[:class:`huaweicloudsdkmodelarts.v1.AutoSearchAlgoConfigParameter`]
        """
        
        

        self._name = None
        self._params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if params is not None:
            self.params = params

    @property
    def name(self):
        r"""Gets the name of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.

        搜索算法名称。

        :return: The name of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.

        搜索算法名称。

        :param name: The name of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.
        :type name: str
        """
        self._name = name

    @property
    def params(self):
        r"""Gets the params of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.

        搜索算法参数。

        :return: The params of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AutoSearchAlgoConfigParameter`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.

        搜索算法参数。

        :param params: The params of this JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs.
        :type params: list[:class:`huaweicloudsdkmodelarts.v1.AutoSearchAlgoConfigParameter`]
        """
        self._params = params

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
        if not isinstance(other, JobAlgorithmResponsePoliciesAutoSearchAlgoConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
