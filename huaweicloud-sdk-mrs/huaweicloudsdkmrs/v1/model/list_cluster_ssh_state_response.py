# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterSshStateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ssh_ops_stat': 'float'
    }

    attribute_map = {
        'ssh_ops_stat': 'sshOpsStat'
    }

    def __init__(self, ssh_ops_stat=None):
        r"""ListClusterSshStateResponse

        The model defined in huaweicloud sdk

        :param ssh_ops_stat: 查询指定集群节点授权状态 - -1：未开启集群节点授权 - 0：开启集群节点授权失败 - 1：正在开启集群节点授权 - 2：已开启集群节点授权 - 3：集群节点授权即将失效状态 - 4：集群节点授权已失效状态
        :type ssh_ops_stat: float
        """
        
        super().__init__()

        self._ssh_ops_stat = None
        self.discriminator = None

        if ssh_ops_stat is not None:
            self.ssh_ops_stat = ssh_ops_stat

    @property
    def ssh_ops_stat(self):
        r"""Gets the ssh_ops_stat of this ListClusterSshStateResponse.

        查询指定集群节点授权状态 - -1：未开启集群节点授权 - 0：开启集群节点授权失败 - 1：正在开启集群节点授权 - 2：已开启集群节点授权 - 3：集群节点授权即将失效状态 - 4：集群节点授权已失效状态

        :return: The ssh_ops_stat of this ListClusterSshStateResponse.
        :rtype: float
        """
        return self._ssh_ops_stat

    @ssh_ops_stat.setter
    def ssh_ops_stat(self, ssh_ops_stat):
        r"""Sets the ssh_ops_stat of this ListClusterSshStateResponse.

        查询指定集群节点授权状态 - -1：未开启集群节点授权 - 0：开启集群节点授权失败 - 1：正在开启集群节点授权 - 2：已开启集群节点授权 - 3：集群节点授权即将失效状态 - 4：集群节点授权已失效状态

        :param ssh_ops_stat: The ssh_ops_stat of this ListClusterSshStateResponse.
        :type ssh_ops_stat: float
        """
        self._ssh_ops_stat = ssh_ops_stat

    def to_dict(self):
        import warnings
        warnings.warn("ListClusterSshStateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListClusterSshStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
