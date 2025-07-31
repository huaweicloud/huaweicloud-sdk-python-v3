# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchClusterProtectionModeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_ids': 'list[str]',
        'opr': 'int'
    }

    attribute_map = {
        'cluster_ids': 'cluster_ids',
        'opr': 'opr'
    }

    def __init__(self, cluster_ids=None, opr=None):
        r"""SwitchClusterProtectionModeRequestBody

        The model defined in huaweicloud sdk

        :param cluster_ids: 集群ID列表
        :type cluster_ids: list[str]
        :param opr: - 1：开 - 0：关 - 2：关闭并卸载插件
        :type opr: int
        """
        
        

        self._cluster_ids = None
        self._opr = None
        self.discriminator = None

        self.cluster_ids = cluster_ids
        self.opr = opr

    @property
    def cluster_ids(self):
        r"""Gets the cluster_ids of this SwitchClusterProtectionModeRequestBody.

        集群ID列表

        :return: The cluster_ids of this SwitchClusterProtectionModeRequestBody.
        :rtype: list[str]
        """
        return self._cluster_ids

    @cluster_ids.setter
    def cluster_ids(self, cluster_ids):
        r"""Sets the cluster_ids of this SwitchClusterProtectionModeRequestBody.

        集群ID列表

        :param cluster_ids: The cluster_ids of this SwitchClusterProtectionModeRequestBody.
        :type cluster_ids: list[str]
        """
        self._cluster_ids = cluster_ids

    @property
    def opr(self):
        r"""Gets the opr of this SwitchClusterProtectionModeRequestBody.

        - 1：开 - 0：关 - 2：关闭并卸载插件

        :return: The opr of this SwitchClusterProtectionModeRequestBody.
        :rtype: int
        """
        return self._opr

    @opr.setter
    def opr(self, opr):
        r"""Sets the opr of this SwitchClusterProtectionModeRequestBody.

        - 1：开 - 0：关 - 2：关闭并卸载插件

        :param opr: The opr of this SwitchClusterProtectionModeRequestBody.
        :type opr: int
        """
        self._opr = opr

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
        if not isinstance(other, SwitchClusterProtectionModeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
