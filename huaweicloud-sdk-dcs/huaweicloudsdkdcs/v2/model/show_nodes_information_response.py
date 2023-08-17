# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodesInformationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'total': 'int',
        'nodes': 'list[NodesInfoResp]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'total': 'total',
        'nodes': 'nodes'
    }

    def __init__(self, instance_id=None, total=None, nodes=None):
        """ShowNodesInformationResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param total: 节点数量
        :type total: int
        :param nodes: 节点信息
        :type nodes: list[:class:`huaweicloudsdkdcs.v2.NodesInfoResp`]
        """
        
        super(ShowNodesInformationResponse, self).__init__()

        self._instance_id = None
        self._total = None
        self._nodes = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if total is not None:
            self.total = total
        if nodes is not None:
            self.nodes = nodes

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowNodesInformationResponse.

        实例ID

        :return: The instance_id of this ShowNodesInformationResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowNodesInformationResponse.

        实例ID

        :param instance_id: The instance_id of this ShowNodesInformationResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def total(self):
        """Gets the total of this ShowNodesInformationResponse.

        节点数量

        :return: The total of this ShowNodesInformationResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowNodesInformationResponse.

        节点数量

        :param total: The total of this ShowNodesInformationResponse.
        :type total: int
        """
        self._total = total

    @property
    def nodes(self):
        """Gets the nodes of this ShowNodesInformationResponse.

        节点信息

        :return: The nodes of this ShowNodesInformationResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.NodesInfoResp`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ShowNodesInformationResponse.

        节点信息

        :param nodes: The nodes of this ShowNodesInformationResponse.
        :type nodes: list[:class:`huaweicloudsdkdcs.v2.NodesInfoResp`]
        """
        self._nodes = nodes

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
        if not isinstance(other, ShowNodesInformationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
