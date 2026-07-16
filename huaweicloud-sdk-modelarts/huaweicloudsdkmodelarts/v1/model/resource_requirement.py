# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceRequirement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'values': 'list[str]',
        'operator': 'str'
    }

    attribute_map = {
        'key': 'key',
        'values': 'values',
        'operator': 'operator'
    }

    def __init__(self, key=None, values=None, operator=None):
        r"""ResourceRequirement

        The model defined in huaweicloud sdk

        :param key: 资源约束，可选键值如： - flavor_type（资源类型），对应值可选择CPU、GPU[或Ascend](tag:hc,hk,fcs_super)； - device_distributed_mode（是否支持多卡训练），对应值可选择multiple（支持）、singular（不支持）； - host_distributed_mode（是否支持分布式训练），对应值可选择multiple（支持）、singular（不支持）。
        :type key: str
        :param values: 资源约束键对应值。
        :type values: list[str]
        :param operator: 键与值关系，当前只支持in。例如flavor_type in [CPU,GPU]。
        :type operator: str
        """
        
        

        self._key = None
        self._values = None
        self._operator = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if values is not None:
            self.values = values
        if operator is not None:
            self.operator = operator

    @property
    def key(self):
        r"""Gets the key of this ResourceRequirement.

        资源约束，可选键值如： - flavor_type（资源类型），对应值可选择CPU、GPU[或Ascend](tag:hc,hk,fcs_super)； - device_distributed_mode（是否支持多卡训练），对应值可选择multiple（支持）、singular（不支持）； - host_distributed_mode（是否支持分布式训练），对应值可选择multiple（支持）、singular（不支持）。

        :return: The key of this ResourceRequirement.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this ResourceRequirement.

        资源约束，可选键值如： - flavor_type（资源类型），对应值可选择CPU、GPU[或Ascend](tag:hc,hk,fcs_super)； - device_distributed_mode（是否支持多卡训练），对应值可选择multiple（支持）、singular（不支持）； - host_distributed_mode（是否支持分布式训练），对应值可选择multiple（支持）、singular（不支持）。

        :param key: The key of this ResourceRequirement.
        :type key: str
        """
        self._key = key

    @property
    def values(self):
        r"""Gets the values of this ResourceRequirement.

        资源约束键对应值。

        :return: The values of this ResourceRequirement.
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ResourceRequirement.

        资源约束键对应值。

        :param values: The values of this ResourceRequirement.
        :type values: list[str]
        """
        self._values = values

    @property
    def operator(self):
        r"""Gets the operator of this ResourceRequirement.

        键与值关系，当前只支持in。例如flavor_type in [CPU,GPU]。

        :return: The operator of this ResourceRequirement.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this ResourceRequirement.

        键与值关系，当前只支持in。例如flavor_type in [CPU,GPU]。

        :param operator: The operator of this ResourceRequirement.
        :type operator: str
        """
        self._operator = operator

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
        if not isinstance(other, ResourceRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
