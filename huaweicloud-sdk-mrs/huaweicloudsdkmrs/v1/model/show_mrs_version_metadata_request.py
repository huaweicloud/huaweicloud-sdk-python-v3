# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMrsVersionMetadataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_name': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'version_name': 'version_name',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, version_name=None, cluster_id=None):
        r"""ShowMrsVersionMetadataRequest

        The model defined in huaweicloud sdk

        :param version_name: 集群版本。例如“MRS 3.1.0”。如果请求客户端不支持自动转义，则需要将空格转义为%20，例如“MRS%203.1.0”。
        :type version_name: str
        :param cluster_id: 集群ID。如果指定集群ID，则获取该集群做过补丁更新的最新版本元数据。
        :type cluster_id: str
        """
        
        

        self._version_name = None
        self._cluster_id = None
        self.discriminator = None

        self.version_name = version_name
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def version_name(self):
        r"""Gets the version_name of this ShowMrsVersionMetadataRequest.

        集群版本。例如“MRS 3.1.0”。如果请求客户端不支持自动转义，则需要将空格转义为%20，例如“MRS%203.1.0”。

        :return: The version_name of this ShowMrsVersionMetadataRequest.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this ShowMrsVersionMetadataRequest.

        集群版本。例如“MRS 3.1.0”。如果请求客户端不支持自动转义，则需要将空格转义为%20，例如“MRS%203.1.0”。

        :param version_name: The version_name of this ShowMrsVersionMetadataRequest.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowMrsVersionMetadataRequest.

        集群ID。如果指定集群ID，则获取该集群做过补丁更新的最新版本元数据。

        :return: The cluster_id of this ShowMrsVersionMetadataRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowMrsVersionMetadataRequest.

        集群ID。如果指定集群ID，则获取该集群做过补丁更新的最新版本元数据。

        :param cluster_id: The cluster_id of this ShowMrsVersionMetadataRequest.
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
        if not isinstance(other, ShowMrsVersionMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
