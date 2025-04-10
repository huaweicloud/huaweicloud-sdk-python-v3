# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionScaleGroupSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor': 'str',
        'az': 'str',
        'capacity_reservation_specification': 'CapacityReservationSpecification',
        'autoscaling': 'ScaleGroupAutoscaling'
    }

    attribute_map = {
        'flavor': 'flavor',
        'az': 'az',
        'capacity_reservation_specification': 'capacityReservationSpecification',
        'autoscaling': 'autoscaling'
    }

    def __init__(self, flavor=None, az=None, capacity_reservation_specification=None, autoscaling=None):
        r"""ExtensionScaleGroupSpec

        The model defined in huaweicloud sdk

        :param flavor: 节点规格
        :type flavor: str
        :param az: 节点可用区，未指定或者为空则以默认伸缩组中配置为准
        :type az: str
        :param capacity_reservation_specification: 
        :type capacity_reservation_specification: :class:`huaweicloudsdkcce.v3.CapacityReservationSpecification`
        :param autoscaling: 
        :type autoscaling: :class:`huaweicloudsdkcce.v3.ScaleGroupAutoscaling`
        """
        
        

        self._flavor = None
        self._az = None
        self._capacity_reservation_specification = None
        self._autoscaling = None
        self.discriminator = None

        if flavor is not None:
            self.flavor = flavor
        if az is not None:
            self.az = az
        if capacity_reservation_specification is not None:
            self.capacity_reservation_specification = capacity_reservation_specification
        if autoscaling is not None:
            self.autoscaling = autoscaling

    @property
    def flavor(self):
        r"""Gets the flavor of this ExtensionScaleGroupSpec.

        节点规格

        :return: The flavor of this ExtensionScaleGroupSpec.
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this ExtensionScaleGroupSpec.

        节点规格

        :param flavor: The flavor of this ExtensionScaleGroupSpec.
        :type flavor: str
        """
        self._flavor = flavor

    @property
    def az(self):
        r"""Gets the az of this ExtensionScaleGroupSpec.

        节点可用区，未指定或者为空则以默认伸缩组中配置为准

        :return: The az of this ExtensionScaleGroupSpec.
        :rtype: str
        """
        return self._az

    @az.setter
    def az(self, az):
        r"""Sets the az of this ExtensionScaleGroupSpec.

        节点可用区，未指定或者为空则以默认伸缩组中配置为准

        :param az: The az of this ExtensionScaleGroupSpec.
        :type az: str
        """
        self._az = az

    @property
    def capacity_reservation_specification(self):
        r"""Gets the capacity_reservation_specification of this ExtensionScaleGroupSpec.

        :return: The capacity_reservation_specification of this ExtensionScaleGroupSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.CapacityReservationSpecification`
        """
        return self._capacity_reservation_specification

    @capacity_reservation_specification.setter
    def capacity_reservation_specification(self, capacity_reservation_specification):
        r"""Sets the capacity_reservation_specification of this ExtensionScaleGroupSpec.

        :param capacity_reservation_specification: The capacity_reservation_specification of this ExtensionScaleGroupSpec.
        :type capacity_reservation_specification: :class:`huaweicloudsdkcce.v3.CapacityReservationSpecification`
        """
        self._capacity_reservation_specification = capacity_reservation_specification

    @property
    def autoscaling(self):
        r"""Gets the autoscaling of this ExtensionScaleGroupSpec.

        :return: The autoscaling of this ExtensionScaleGroupSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.ScaleGroupAutoscaling`
        """
        return self._autoscaling

    @autoscaling.setter
    def autoscaling(self, autoscaling):
        r"""Sets the autoscaling of this ExtensionScaleGroupSpec.

        :param autoscaling: The autoscaling of this ExtensionScaleGroupSpec.
        :type autoscaling: :class:`huaweicloudsdkcce.v3.ScaleGroupAutoscaling`
        """
        self._autoscaling = autoscaling

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
        if not isinstance(other, ExtensionScaleGroupSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
