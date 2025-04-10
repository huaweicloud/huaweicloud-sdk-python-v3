# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyProxyWeightRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'master_weight': 'str',
        'readonly_instances': 'list[ProxyReadonlyInstances]'
    }

    attribute_map = {
        'master_weight': 'master_weight',
        'readonly_instances': 'readonly_instances'
    }

    def __init__(self, master_weight=None, readonly_instances=None):
        r"""ModifyProxyWeightRequest

        The model defined in huaweicloud sdk

        :param master_weight: 主实例权重，取值范围为0~1000。
        :type master_weight: str
        :param readonly_instances: 只读实例信息。
        :type readonly_instances: list[:class:`huaweicloudsdkrds.v3.ProxyReadonlyInstances`]
        """
        
        

        self._master_weight = None
        self._readonly_instances = None
        self.discriminator = None

        self.master_weight = master_weight
        self.readonly_instances = readonly_instances

    @property
    def master_weight(self):
        r"""Gets the master_weight of this ModifyProxyWeightRequest.

        主实例权重，取值范围为0~1000。

        :return: The master_weight of this ModifyProxyWeightRequest.
        :rtype: str
        """
        return self._master_weight

    @master_weight.setter
    def master_weight(self, master_weight):
        r"""Sets the master_weight of this ModifyProxyWeightRequest.

        主实例权重，取值范围为0~1000。

        :param master_weight: The master_weight of this ModifyProxyWeightRequest.
        :type master_weight: str
        """
        self._master_weight = master_weight

    @property
    def readonly_instances(self):
        r"""Gets the readonly_instances of this ModifyProxyWeightRequest.

        只读实例信息。

        :return: The readonly_instances of this ModifyProxyWeightRequest.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ProxyReadonlyInstances`]
        """
        return self._readonly_instances

    @readonly_instances.setter
    def readonly_instances(self, readonly_instances):
        r"""Sets the readonly_instances of this ModifyProxyWeightRequest.

        只读实例信息。

        :param readonly_instances: The readonly_instances of this ModifyProxyWeightRequest.
        :type readonly_instances: list[:class:`huaweicloudsdkrds.v3.ProxyReadonlyInstances`]
        """
        self._readonly_instances = readonly_instances

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
        if not isinstance(other, ModifyProxyWeightRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
