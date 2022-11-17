# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussExpandCluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'coordinators': 'list[OpenGaussCoordinators]',
        'shard': 'OpenGaussShard'
    }

    attribute_map = {
        'coordinators': 'coordinators',
        'shard': 'shard'
    }

    def __init__(self, coordinators=None, shard=None):
        """OpenGaussExpandCluster

        The model defined in huaweicloud sdk

        :param coordinators: CN横向扩容时必填
        :type coordinators: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussCoordinators`]
        :param shard: 
        :type shard: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussShard`
        """
        
        

        self._coordinators = None
        self._shard = None
        self.discriminator = None

        if coordinators is not None:
            self.coordinators = coordinators
        if shard is not None:
            self.shard = shard

    @property
    def coordinators(self):
        """Gets the coordinators of this OpenGaussExpandCluster.

        CN横向扩容时必填

        :return: The coordinators of this OpenGaussExpandCluster.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussCoordinators`]
        """
        return self._coordinators

    @coordinators.setter
    def coordinators(self, coordinators):
        """Sets the coordinators of this OpenGaussExpandCluster.

        CN横向扩容时必填

        :param coordinators: The coordinators of this OpenGaussExpandCluster.
        :type coordinators: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussCoordinators`]
        """
        self._coordinators = coordinators

    @property
    def shard(self):
        """Gets the shard of this OpenGaussExpandCluster.

        :return: The shard of this OpenGaussExpandCluster.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussShard`
        """
        return self._shard

    @shard.setter
    def shard(self, shard):
        """Sets the shard of this OpenGaussExpandCluster.

        :param shard: The shard of this OpenGaussExpandCluster.
        :type shard: :class:`huaweicloudsdkgaussdbforopengauss.v3.OpenGaussShard`
        """
        self._shard = shard

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
        if not isinstance(other, OpenGaussExpandCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
