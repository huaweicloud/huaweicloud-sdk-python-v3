# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqConfigHpcCacheBackend:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'update_hpc_cache': 'ReqUpdateHpcCacheInfo'
    }

    attribute_map = {
        'update_hpc_cache': 'update_hpc_cache'
    }

    def __init__(self, update_hpc_cache=None):
        r"""ReqConfigHpcCacheBackend

        The model defined in huaweicloud sdk

        :param update_hpc_cache: 
        :type update_hpc_cache: :class:`huaweicloudsdksfsturbo.v1.ReqUpdateHpcCacheInfo`
        """
        
        

        self._update_hpc_cache = None
        self.discriminator = None

        self.update_hpc_cache = update_hpc_cache

    @property
    def update_hpc_cache(self):
        r"""Gets the update_hpc_cache of this ReqConfigHpcCacheBackend.

        :return: The update_hpc_cache of this ReqConfigHpcCacheBackend.
        :rtype: :class:`huaweicloudsdksfsturbo.v1.ReqUpdateHpcCacheInfo`
        """
        return self._update_hpc_cache

    @update_hpc_cache.setter
    def update_hpc_cache(self, update_hpc_cache):
        r"""Sets the update_hpc_cache of this ReqConfigHpcCacheBackend.

        :param update_hpc_cache: The update_hpc_cache of this ReqConfigHpcCacheBackend.
        :type update_hpc_cache: :class:`huaweicloudsdksfsturbo.v1.ReqUpdateHpcCacheInfo`
        """
        self._update_hpc_cache = update_hpc_cache

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
        if not isinstance(other, ReqConfigHpcCacheBackend):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
