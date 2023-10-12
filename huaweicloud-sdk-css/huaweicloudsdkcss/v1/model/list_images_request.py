# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImagesRequest:

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
        'upgrade_type': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'upgrade_type': 'upgrade_type'
    }

    def __init__(self, cluster_id=None, upgrade_type=None):
        """ListImagesRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 待升级的集群的ID。
        :type cluster_id: str
        :param upgrade_type: 升级目标版本类型： - same：相同版本。 - cross： 跨版本。
        :type upgrade_type: str
        """
        
        

        self._cluster_id = None
        self._upgrade_type = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.upgrade_type = upgrade_type

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListImagesRequest.

        待升级的集群的ID。

        :return: The cluster_id of this ListImagesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListImagesRequest.

        待升级的集群的ID。

        :param cluster_id: The cluster_id of this ListImagesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this ListImagesRequest.

        升级目标版本类型： - same：相同版本。 - cross： 跨版本。

        :return: The upgrade_type of this ListImagesRequest.
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this ListImagesRequest.

        升级目标版本类型： - same：相同版本。 - cross： 跨版本。

        :param upgrade_type: The upgrade_type of this ListImagesRequest.
        :type upgrade_type: str
        """
        self._upgrade_type = upgrade_type

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
        if not isinstance(other, ListImagesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
