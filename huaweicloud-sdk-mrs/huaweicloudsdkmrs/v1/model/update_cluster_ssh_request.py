# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClusterSshRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'enable': 'bool',
        'expire_time': 'float'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'enable': 'enable',
        'expire_time': 'expire_time'
    }

    def __init__(self, cluster_id=None, enable=None, expire_time=None):
        r"""UpdateClusterSshRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param enable: 开启/关闭集群节点授权
        :type enable: bool
        :param expire_time: 开启集群节点授权截止时间，仅enable为true时需要传递，如不传该值默认为1天授权时间
        :type expire_time: float
        """
        
        

        self._cluster_id = None
        self._enable = None
        self._expire_time = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.enable = enable
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateClusterSshRequest.

        集群ID

        :return: The cluster_id of this UpdateClusterSshRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateClusterSshRequest.

        集群ID

        :param cluster_id: The cluster_id of this UpdateClusterSshRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def enable(self):
        r"""Gets the enable of this UpdateClusterSshRequest.

        开启/关闭集群节点授权

        :return: The enable of this UpdateClusterSshRequest.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this UpdateClusterSshRequest.

        开启/关闭集群节点授权

        :param enable: The enable of this UpdateClusterSshRequest.
        :type enable: bool
        """
        self._enable = enable

    @property
    def expire_time(self):
        r"""Gets the expire_time of this UpdateClusterSshRequest.

        开启集群节点授权截止时间，仅enable为true时需要传递，如不传该值默认为1天授权时间

        :return: The expire_time of this UpdateClusterSshRequest.
        :rtype: float
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this UpdateClusterSshRequest.

        开启集群节点授权截止时间，仅enable为true时需要传递，如不传该值默认为1天授权时间

        :param expire_time: The expire_time of this UpdateClusterSshRequest.
        :type expire_time: float
        """
        self._expire_time = expire_time

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateClusterSshRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
