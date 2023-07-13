# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopologyTreeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topology_tree': 'TopologyTree'
    }

    attribute_map = {
        'topology_tree': 'topology_tree'
    }

    def __init__(self, topology_tree=None):
        """ShowTopologyTreeResponse

        The model defined in huaweicloud sdk

        :param topology_tree: 
        :type topology_tree: :class:`huaweicloudsdkapm.v1.TopologyTree`
        """
        
        super(ShowTopologyTreeResponse, self).__init__()

        self._topology_tree = None
        self.discriminator = None

        if topology_tree is not None:
            self.topology_tree = topology_tree

    @property
    def topology_tree(self):
        """Gets the topology_tree of this ShowTopologyTreeResponse.

        :return: The topology_tree of this ShowTopologyTreeResponse.
        :rtype: :class:`huaweicloudsdkapm.v1.TopologyTree`
        """
        return self._topology_tree

    @topology_tree.setter
    def topology_tree(self, topology_tree):
        """Sets the topology_tree of this ShowTopologyTreeResponse.

        :param topology_tree: The topology_tree of this ShowTopologyTreeResponse.
        :type topology_tree: :class:`huaweicloudsdkapm.v1.TopologyTree`
        """
        self._topology_tree = topology_tree

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
        if not isinstance(other, ShowTopologyTreeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
