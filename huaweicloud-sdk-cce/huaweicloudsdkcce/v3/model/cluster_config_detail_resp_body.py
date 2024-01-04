# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterConfigDetailRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kube_apiserver': 'list[PackageOptions]'
    }

    attribute_map = {
        'kube_apiserver': 'kube-apiserver'
    }

    def __init__(self, kube_apiserver=None):
        """ClusterConfigDetailRespBody

        The model defined in huaweicloud sdk

        :param kube_apiserver: 配置参数，由key/value组成。
        :type kube_apiserver: list[:class:`huaweicloudsdkcce.v3.PackageOptions`]
        """
        
        

        self._kube_apiserver = None
        self.discriminator = None

        if kube_apiserver is not None:
            self.kube_apiserver = kube_apiserver

    @property
    def kube_apiserver(self):
        """Gets the kube_apiserver of this ClusterConfigDetailRespBody.

        配置参数，由key/value组成。

        :return: The kube_apiserver of this ClusterConfigDetailRespBody.
        :rtype: list[:class:`huaweicloudsdkcce.v3.PackageOptions`]
        """
        return self._kube_apiserver

    @kube_apiserver.setter
    def kube_apiserver(self, kube_apiserver):
        """Sets the kube_apiserver of this ClusterConfigDetailRespBody.

        配置参数，由key/value组成。

        :param kube_apiserver: The kube_apiserver of this ClusterConfigDetailRespBody.
        :type kube_apiserver: list[:class:`huaweicloudsdkcce.v3.PackageOptions`]
        """
        self._kube_apiserver = kube_apiserver

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
        if not isinstance(other, ClusterConfigDetailRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
