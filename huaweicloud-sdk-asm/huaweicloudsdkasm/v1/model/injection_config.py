# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InjectionConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'restart_pod': 'bool',
        'namespaces': 'Selector'
    }

    attribute_map = {
        'restart_pod': 'restartPod',
        'namespaces': 'namespaces'
    }

    def __init__(self, restart_pod=None, namespaces=None):
        """InjectionConfig

        The model defined in huaweicloud sdk

        :param restart_pod: 是否重启pod
        :type restart_pod: bool
        :param namespaces: 
        :type namespaces: :class:`huaweicloudsdkasm.v1.Selector`
        """
        
        

        self._restart_pod = None
        self._namespaces = None
        self.discriminator = None

        if restart_pod is not None:
            self.restart_pod = restart_pod
        if namespaces is not None:
            self.namespaces = namespaces

    @property
    def restart_pod(self):
        """Gets the restart_pod of this InjectionConfig.

        是否重启pod

        :return: The restart_pod of this InjectionConfig.
        :rtype: bool
        """
        return self._restart_pod

    @restart_pod.setter
    def restart_pod(self, restart_pod):
        """Sets the restart_pod of this InjectionConfig.

        是否重启pod

        :param restart_pod: The restart_pod of this InjectionConfig.
        :type restart_pod: bool
        """
        self._restart_pod = restart_pod

    @property
    def namespaces(self):
        """Gets the namespaces of this InjectionConfig.

        :return: The namespaces of this InjectionConfig.
        :rtype: :class:`huaweicloudsdkasm.v1.Selector`
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        """Sets the namespaces of this InjectionConfig.

        :param namespaces: The namespaces of this InjectionConfig.
        :type namespaces: :class:`huaweicloudsdkasm.v1.Selector`
        """
        self._namespaces = namespaces

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
        if not isinstance(other, InjectionConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
