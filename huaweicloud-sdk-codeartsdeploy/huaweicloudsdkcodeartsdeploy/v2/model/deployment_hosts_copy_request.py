# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentHostsCopyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_uuids': 'list[str]',
        'target_group_id': 'str'
    }

    attribute_map = {
        'host_uuids': 'host_uuids',
        'target_group_id': 'target_group_id'
    }

    def __init__(self, host_uuids=None, target_group_id=None):
        r"""DeploymentHostsCopyRequest

        The model defined in huaweicloud sdk

        :param host_uuids: 主机id列表
        :type host_uuids: list[str]
        :param target_group_id: 目标主机集群id
        :type target_group_id: str
        """
        
        

        self._host_uuids = None
        self._target_group_id = None
        self.discriminator = None

        self.host_uuids = host_uuids
        self.target_group_id = target_group_id

    @property
    def host_uuids(self):
        r"""Gets the host_uuids of this DeploymentHostsCopyRequest.

        主机id列表

        :return: The host_uuids of this DeploymentHostsCopyRequest.
        :rtype: list[str]
        """
        return self._host_uuids

    @host_uuids.setter
    def host_uuids(self, host_uuids):
        r"""Sets the host_uuids of this DeploymentHostsCopyRequest.

        主机id列表

        :param host_uuids: The host_uuids of this DeploymentHostsCopyRequest.
        :type host_uuids: list[str]
        """
        self._host_uuids = host_uuids

    @property
    def target_group_id(self):
        r"""Gets the target_group_id of this DeploymentHostsCopyRequest.

        目标主机集群id

        :return: The target_group_id of this DeploymentHostsCopyRequest.
        :rtype: str
        """
        return self._target_group_id

    @target_group_id.setter
    def target_group_id(self, target_group_id):
        r"""Sets the target_group_id of this DeploymentHostsCopyRequest.

        目标主机集群id

        :param target_group_id: The target_group_id of this DeploymentHostsCopyRequest.
        :type target_group_id: str
        """
        self._target_group_id = target_group_id

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
        if not isinstance(other, DeploymentHostsCopyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
