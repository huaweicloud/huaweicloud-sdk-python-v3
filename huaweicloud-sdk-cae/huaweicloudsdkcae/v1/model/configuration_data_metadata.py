# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationDataMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'annotations': 'dict(str, str)'
    }

    attribute_map = {
        'annotations': 'annotations'
    }

    def __init__(self, annotations=None):
        """ConfigurationDataMetadata

        The model defined in huaweicloud sdk

        :param annotations: 如下配置表示：负载均衡分配策略使用加权轮询算法，不启用健康检查。 - \&quot;kubernetes.io/elb.health-check-flag\&quot;: \&quot;off\&quot; - \&quot;kubernetes.io/elb.lb-algorithm\&quot;: \&quot;ROUND_ROBIN\&quot;
        :type annotations: dict(str, str)
        """
        
        

        self._annotations = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations

    @property
    def annotations(self):
        """Gets the annotations of this ConfigurationDataMetadata.

        如下配置表示：负载均衡分配策略使用加权轮询算法，不启用健康检查。 - \"kubernetes.io/elb.health-check-flag\": \"off\" - \"kubernetes.io/elb.lb-algorithm\": \"ROUND_ROBIN\"

        :return: The annotations of this ConfigurationDataMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ConfigurationDataMetadata.

        如下配置表示：负载均衡分配策略使用加权轮询算法，不启用健康检查。 - \"kubernetes.io/elb.health-check-flag\": \"off\" - \"kubernetes.io/elb.lb-algorithm\": \"ROUND_ROBIN\"

        :param annotations: The annotations of this ConfigurationDataMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

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
        if not isinstance(other, ConfigurationDataMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
