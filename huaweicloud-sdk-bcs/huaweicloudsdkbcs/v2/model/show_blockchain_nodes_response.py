# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBlockchainNodesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_orgs': 'dict(str, Org)'
    }

    attribute_map = {
        'node_orgs': 'node_orgs'
    }

    def __init__(self, node_orgs=None):
        """ShowBlockchainNodesResponse

        The model defined in huaweicloud sdk

        :param node_orgs: key:组织名，value：组织详细信息
        :type node_orgs: dict(str, Org)
        """
        
        super(ShowBlockchainNodesResponse, self).__init__()

        self._node_orgs = None
        self.discriminator = None

        if node_orgs is not None:
            self.node_orgs = node_orgs

    @property
    def node_orgs(self):
        """Gets the node_orgs of this ShowBlockchainNodesResponse.

        key:组织名，value：组织详细信息

        :return: The node_orgs of this ShowBlockchainNodesResponse.
        :rtype: dict(str, Org)
        """
        return self._node_orgs

    @node_orgs.setter
    def node_orgs(self, node_orgs):
        """Sets the node_orgs of this ShowBlockchainNodesResponse.

        key:组织名，value：组织详细信息

        :param node_orgs: The node_orgs of this ShowBlockchainNodesResponse.
        :type node_orgs: dict(str, Org)
        """
        self._node_orgs = node_orgs

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
        if not isinstance(other, ShowBlockchainNodesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
