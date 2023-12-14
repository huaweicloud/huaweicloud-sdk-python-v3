# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateLogicalClusterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_rings': 'list[ClusterRing]',
        'mode': 'str',
        'waiting_for_killing': 'int'
    }

    attribute_map = {
        'cluster_rings': 'cluster_rings',
        'mode': 'mode',
        'waiting_for_killing': 'waiting_for_killing'
    }

    def __init__(self, cluster_rings=None, mode=None, waiting_for_killing=None):
        """UpdateLogicalClusterRequestBody

        The model defined in huaweicloud sdk

        :param cluster_rings: 逻辑集群编辑环列表信息
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        :param mode: 模式
        :type mode: str
        :param waiting_for_killing: 是否等待销毁
        :type waiting_for_killing: int
        """
        
        

        self._cluster_rings = None
        self._mode = None
        self._waiting_for_killing = None
        self.discriminator = None

        self.cluster_rings = cluster_rings
        if mode is not None:
            self.mode = mode
        if waiting_for_killing is not None:
            self.waiting_for_killing = waiting_for_killing

    @property
    def cluster_rings(self):
        """Gets the cluster_rings of this UpdateLogicalClusterRequestBody.

        逻辑集群编辑环列表信息

        :return: The cluster_rings of this UpdateLogicalClusterRequestBody.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        return self._cluster_rings

    @cluster_rings.setter
    def cluster_rings(self, cluster_rings):
        """Sets the cluster_rings of this UpdateLogicalClusterRequestBody.

        逻辑集群编辑环列表信息

        :param cluster_rings: The cluster_rings of this UpdateLogicalClusterRequestBody.
        :type cluster_rings: list[:class:`huaweicloudsdkdws.v2.ClusterRing`]
        """
        self._cluster_rings = cluster_rings

    @property
    def mode(self):
        """Gets the mode of this UpdateLogicalClusterRequestBody.

        模式

        :return: The mode of this UpdateLogicalClusterRequestBody.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this UpdateLogicalClusterRequestBody.

        模式

        :param mode: The mode of this UpdateLogicalClusterRequestBody.
        :type mode: str
        """
        self._mode = mode

    @property
    def waiting_for_killing(self):
        """Gets the waiting_for_killing of this UpdateLogicalClusterRequestBody.

        是否等待销毁

        :return: The waiting_for_killing of this UpdateLogicalClusterRequestBody.
        :rtype: int
        """
        return self._waiting_for_killing

    @waiting_for_killing.setter
    def waiting_for_killing(self, waiting_for_killing):
        """Sets the waiting_for_killing of this UpdateLogicalClusterRequestBody.

        是否等待销毁

        :param waiting_for_killing: The waiting_for_killing of this UpdateLogicalClusterRequestBody.
        :type waiting_for_killing: int
        """
        self._waiting_for_killing = waiting_for_killing

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
        if not isinstance(other, UpdateLogicalClusterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
