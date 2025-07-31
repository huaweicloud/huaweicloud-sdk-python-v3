# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDaemonsetRespInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_reson': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'failed_reson': 'failed_reson',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, failed_reson=None, cluster_id=None):
        r"""UpdateDaemonsetRespInfo

        The model defined in huaweicloud sdk

        :param failed_reson: 失败原因
        :type failed_reson: str
        :param cluster_id: 集群Id
        :type cluster_id: str
        """
        
        

        self._failed_reson = None
        self._cluster_id = None
        self.discriminator = None

        if failed_reson is not None:
            self.failed_reson = failed_reson
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def failed_reson(self):
        r"""Gets the failed_reson of this UpdateDaemonsetRespInfo.

        失败原因

        :return: The failed_reson of this UpdateDaemonsetRespInfo.
        :rtype: str
        """
        return self._failed_reson

    @failed_reson.setter
    def failed_reson(self, failed_reson):
        r"""Sets the failed_reson of this UpdateDaemonsetRespInfo.

        失败原因

        :param failed_reson: The failed_reson of this UpdateDaemonsetRespInfo.
        :type failed_reson: str
        """
        self._failed_reson = failed_reson

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateDaemonsetRespInfo.

        集群Id

        :return: The cluster_id of this UpdateDaemonsetRespInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateDaemonsetRespInfo.

        集群Id

        :param cluster_id: The cluster_id of this UpdateDaemonsetRespInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, UpdateDaemonsetRespInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
