# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterNameReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str'
    }

    attribute_map = {
        'cluster_name': 'cluster_name'
    }

    def __init__(self, cluster_name=None):
        r"""ClusterNameReq

        The model defined in huaweicloud sdk

        :param cluster_name: **参数解释**： 修改集群名称请求。 **约束限制**： guestAgent插件版本8.3.1及以上才支持。 **取值范围**： 中文或英文字母开头，3~64位长度。 **默认取值**： 不涉及。
        :type cluster_name: str
        """
        
        

        self._cluster_name = None
        self.discriminator = None

        if cluster_name is not None:
            self.cluster_name = cluster_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterNameReq.

        **参数解释**： 修改集群名称请求。 **约束限制**： guestAgent插件版本8.3.1及以上才支持。 **取值范围**： 中文或英文字母开头，3~64位长度。 **默认取值**： 不涉及。

        :return: The cluster_name of this ClusterNameReq.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterNameReq.

        **参数解释**： 修改集群名称请求。 **约束限制**： guestAgent插件版本8.3.1及以上才支持。 **取值范围**： 中文或英文字母开头，3~64位长度。 **默认取值**： 不涉及。

        :param cluster_name: The cluster_name of this ClusterNameReq.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

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
        if not isinstance(other, ClusterNameReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
