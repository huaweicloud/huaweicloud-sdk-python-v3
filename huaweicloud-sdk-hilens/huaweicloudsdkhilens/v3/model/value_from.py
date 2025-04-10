# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValueFrom:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configmap': 'ConfigsMap',
        'secret': 'DeploymentSecrets'
    }

    attribute_map = {
        'configmap': 'configmap',
        'secret': 'secret'
    }

    def __init__(self, configmap=None, secret=None):
        r"""ValueFrom

        The model defined in huaweicloud sdk

        :param configmap: 
        :type configmap: :class:`huaweicloudsdkhilens.v3.ConfigsMap`
        :param secret: 
        :type secret: :class:`huaweicloudsdkhilens.v3.DeploymentSecrets`
        """
        
        

        self._configmap = None
        self._secret = None
        self.discriminator = None

        if configmap is not None:
            self.configmap = configmap
        if secret is not None:
            self.secret = secret

    @property
    def configmap(self):
        r"""Gets the configmap of this ValueFrom.

        :return: The configmap of this ValueFrom.
        :rtype: :class:`huaweicloudsdkhilens.v3.ConfigsMap`
        """
        return self._configmap

    @configmap.setter
    def configmap(self, configmap):
        r"""Sets the configmap of this ValueFrom.

        :param configmap: The configmap of this ValueFrom.
        :type configmap: :class:`huaweicloudsdkhilens.v3.ConfigsMap`
        """
        self._configmap = configmap

    @property
    def secret(self):
        r"""Gets the secret of this ValueFrom.

        :return: The secret of this ValueFrom.
        :rtype: :class:`huaweicloudsdkhilens.v3.DeploymentSecrets`
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        r"""Sets the secret of this ValueFrom.

        :param secret: The secret of this ValueFrom.
        :type secret: :class:`huaweicloudsdkhilens.v3.DeploymentSecrets`
        """
        self._secret = secret

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
        if not isinstance(other, ValueFrom):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
