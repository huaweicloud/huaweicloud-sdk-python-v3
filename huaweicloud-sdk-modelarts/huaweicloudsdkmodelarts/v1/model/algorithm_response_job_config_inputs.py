# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmResponseJobConfigInputs:

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
        'description': 'str',
        'remote_constraints': 'list[AlgorithmResponseJobConfigRemoteConstraints]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'remote_constraints': 'remote_constraints'
    }

    def __init__(self, name=None, description=None, remote_constraints=None):
        r"""AlgorithmResponseJobConfigInputs

        The model defined in huaweicloud sdk

        :param name: 数据输入通道名称。
        :type name: str
        :param description: 数据输入通道描述信息。
        :type description: str
        :param remote_constraints: 数据输入约束。
        :type remote_constraints: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseJobConfigRemoteConstraints`]
        """
        
        

        self._name = None
        self._description = None
        self._remote_constraints = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if remote_constraints is not None:
            self.remote_constraints = remote_constraints

    @property
    def name(self):
        r"""Gets the name of this AlgorithmResponseJobConfigInputs.

        数据输入通道名称。

        :return: The name of this AlgorithmResponseJobConfigInputs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlgorithmResponseJobConfigInputs.

        数据输入通道名称。

        :param name: The name of this AlgorithmResponseJobConfigInputs.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AlgorithmResponseJobConfigInputs.

        数据输入通道描述信息。

        :return: The description of this AlgorithmResponseJobConfigInputs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlgorithmResponseJobConfigInputs.

        数据输入通道描述信息。

        :param description: The description of this AlgorithmResponseJobConfigInputs.
        :type description: str
        """
        self._description = description

    @property
    def remote_constraints(self):
        r"""Gets the remote_constraints of this AlgorithmResponseJobConfigInputs.

        数据输入约束。

        :return: The remote_constraints of this AlgorithmResponseJobConfigInputs.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseJobConfigRemoteConstraints`]
        """
        return self._remote_constraints

    @remote_constraints.setter
    def remote_constraints(self, remote_constraints):
        r"""Sets the remote_constraints of this AlgorithmResponseJobConfigInputs.

        数据输入约束。

        :param remote_constraints: The remote_constraints of this AlgorithmResponseJobConfigInputs.
        :type remote_constraints: list[:class:`huaweicloudsdkmodelarts.v1.AlgorithmResponseJobConfigRemoteConstraints`]
        """
        self._remote_constraints = remote_constraints

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
        if not isinstance(other, AlgorithmResponseJobConfigInputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
