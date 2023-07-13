# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLinkRequest:

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
        'link_name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'link_name': 'link_name'
    }

    def __init__(self, cluster_id=None, link_name=None):
        """ShowLinkRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param link_name: 连接名称
        :type link_name: str
        """
        
        

        self._cluster_id = None
        self._link_name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.link_name = link_name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowLinkRequest.

        集群ID

        :return: The cluster_id of this ShowLinkRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowLinkRequest.

        集群ID

        :param cluster_id: The cluster_id of this ShowLinkRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def link_name(self):
        """Gets the link_name of this ShowLinkRequest.

        连接名称

        :return: The link_name of this ShowLinkRequest.
        :rtype: str
        """
        return self._link_name

    @link_name.setter
    def link_name(self, link_name):
        """Sets the link_name of this ShowLinkRequest.

        连接名称

        :param link_name: The link_name of this ShowLinkRequest.
        :type link_name: str
        """
        self._link_name = link_name

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
        if not isinstance(other, ShowLinkRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
