# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetResourceGroupResources:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'dimensions': 'list[Dimension2]'
    }

    attribute_map = {
        'status': 'status',
        'dimensions': 'dimensions'
    }

    def __init__(self, status=None, dimensions=None):
        """GetResourceGroupResources

        The model defined in huaweicloud sdk

        :param status: 资源健康状态，取值为health（已设置告警规则且无告警触发的资源）、unhealthy（已设置告警规则且有告警触发的资源）、no_alarm_rule（未关联告警规则）
        :type status: str
        :param dimensions: 资源的维度信息
        :type dimensions: list[:class:`huaweicloudsdkces.v2.Dimension2`]
        """
        
        

        self._status = None
        self._dimensions = None
        self.discriminator = None

        self.status = status
        self.dimensions = dimensions

    @property
    def status(self):
        """Gets the status of this GetResourceGroupResources.

        资源健康状态，取值为health（已设置告警规则且无告警触发的资源）、unhealthy（已设置告警规则且有告警触发的资源）、no_alarm_rule（未关联告警规则）

        :return: The status of this GetResourceGroupResources.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetResourceGroupResources.

        资源健康状态，取值为health（已设置告警规则且无告警触发的资源）、unhealthy（已设置告警规则且有告警触发的资源）、no_alarm_rule（未关联告警规则）

        :param status: The status of this GetResourceGroupResources.
        :type status: str
        """
        self._status = status

    @property
    def dimensions(self):
        """Gets the dimensions of this GetResourceGroupResources.

        资源的维度信息

        :return: The dimensions of this GetResourceGroupResources.
        :rtype: list[:class:`huaweicloudsdkces.v2.Dimension2`]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this GetResourceGroupResources.

        资源的维度信息

        :param dimensions: The dimensions of this GetResourceGroupResources.
        :type dimensions: list[:class:`huaweicloudsdkces.v2.Dimension2`]
        """
        self._dimensions = dimensions

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
        if not isinstance(other, GetResourceGroupResources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
