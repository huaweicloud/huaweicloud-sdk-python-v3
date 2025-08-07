# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendedAvailabilityZone:

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
        'public_border_group': 'str',
        'available_specs': 'list[AvailableSpec]'
    }

    attribute_map = {
        'name': 'name',
        'public_border_group': 'public_border_group',
        'available_specs': 'available_specs'
    }

    def __init__(self, name=None, public_border_group=None, available_specs=None):
        r"""ExtendedAvailabilityZone

        The model defined in huaweicloud sdk

        :param name: 可用区名称
        :type name: str
        :param public_border_group: 公共边界组
        :type public_border_group: str
        :param available_specs: 该可用区下可选的VPN网关规格组合
        :type available_specs: list[:class:`huaweicloudsdkvpn.v5.AvailableSpec`]
        """
        
        

        self._name = None
        self._public_border_group = None
        self._available_specs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if public_border_group is not None:
            self.public_border_group = public_border_group
        if available_specs is not None:
            self.available_specs = available_specs

    @property
    def name(self):
        r"""Gets the name of this ExtendedAvailabilityZone.

        可用区名称

        :return: The name of this ExtendedAvailabilityZone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExtendedAvailabilityZone.

        可用区名称

        :param name: The name of this ExtendedAvailabilityZone.
        :type name: str
        """
        self._name = name

    @property
    def public_border_group(self):
        r"""Gets the public_border_group of this ExtendedAvailabilityZone.

        公共边界组

        :return: The public_border_group of this ExtendedAvailabilityZone.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        r"""Sets the public_border_group of this ExtendedAvailabilityZone.

        公共边界组

        :param public_border_group: The public_border_group of this ExtendedAvailabilityZone.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

    @property
    def available_specs(self):
        r"""Gets the available_specs of this ExtendedAvailabilityZone.

        该可用区下可选的VPN网关规格组合

        :return: The available_specs of this ExtendedAvailabilityZone.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.AvailableSpec`]
        """
        return self._available_specs

    @available_specs.setter
    def available_specs(self, available_specs):
        r"""Sets the available_specs of this ExtendedAvailabilityZone.

        该可用区下可选的VPN网关规格组合

        :param available_specs: The available_specs of this ExtendedAvailabilityZone.
        :type available_specs: list[:class:`huaweicloudsdkvpn.v5.AvailableSpec`]
        """
        self._available_specs = available_specs

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
        if not isinstance(other, ExtendedAvailabilityZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
