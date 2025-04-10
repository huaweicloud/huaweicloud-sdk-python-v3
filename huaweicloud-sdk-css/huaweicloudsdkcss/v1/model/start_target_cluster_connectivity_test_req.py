# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartTargetClusterConnectivityTestReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_cluster_id': 'str'
    }

    attribute_map = {
        'target_cluster_id': 'target_cluster_id'
    }

    def __init__(self, target_cluster_id=None):
        r"""StartTargetClusterConnectivityTestReq

        The model defined in huaweicloud sdk

        :param target_cluster_id: 目标集群ID
        :type target_cluster_id: str
        """
        
        

        self._target_cluster_id = None
        self.discriminator = None

        self.target_cluster_id = target_cluster_id

    @property
    def target_cluster_id(self):
        r"""Gets the target_cluster_id of this StartTargetClusterConnectivityTestReq.

        目标集群ID

        :return: The target_cluster_id of this StartTargetClusterConnectivityTestReq.
        :rtype: str
        """
        return self._target_cluster_id

    @target_cluster_id.setter
    def target_cluster_id(self, target_cluster_id):
        r"""Sets the target_cluster_id of this StartTargetClusterConnectivityTestReq.

        目标集群ID

        :param target_cluster_id: The target_cluster_id of this StartTargetClusterConnectivityTestReq.
        :type target_cluster_id: str
        """
        self._target_cluster_id = target_cluster_id

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
        if not isinstance(other, StartTargetClusterConnectivityTestReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
