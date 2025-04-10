# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReservedResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apu': 'ResourceDef',
        'dpu': 'ResourceDef',
        'mu': 'ResourceDemand'
    }

    attribute_map = {
        'apu': 'apu',
        'dpu': 'dpu',
        'mu': 'mu'
    }

    def __init__(self, apu=None, dpu=None, mu=None):
        r"""ReservedResource

        The model defined in huaweicloud sdk

        :param apu: 
        :type apu: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDef`
        :param dpu: 
        :type dpu: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDef`
        :param mu: 
        :type mu: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDemand`
        """
        
        

        self._apu = None
        self._dpu = None
        self._mu = None
        self.discriminator = None

        if apu is not None:
            self.apu = apu
        if dpu is not None:
            self.dpu = dpu
        if mu is not None:
            self.mu = mu

    @property
    def apu(self):
        r"""Gets the apu of this ReservedResource.

        :return: The apu of this ReservedResource.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDef`
        """
        return self._apu

    @apu.setter
    def apu(self, apu):
        r"""Sets the apu of this ReservedResource.

        :param apu: The apu of this ReservedResource.
        :type apu: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDef`
        """
        self._apu = apu

    @property
    def dpu(self):
        r"""Gets the dpu of this ReservedResource.

        :return: The dpu of this ReservedResource.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDef`
        """
        return self._dpu

    @dpu.setter
    def dpu(self, dpu):
        r"""Sets the dpu of this ReservedResource.

        :param dpu: The dpu of this ReservedResource.
        :type dpu: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDef`
        """
        self._dpu = dpu

    @property
    def mu(self):
        r"""Gets the mu of this ReservedResource.

        :return: The mu of this ReservedResource.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDemand`
        """
        return self._mu

    @mu.setter
    def mu(self, mu):
        r"""Sets the mu of this ReservedResource.

        :param mu: The mu of this ReservedResource.
        :type mu: :class:`huaweicloudsdkdataartsfabric.v1.ResourceDemand`
        """
        self._mu = mu

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
        if not isinstance(other, ReservedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
