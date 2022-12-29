# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeploymentAddNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_ids': 'list[str]',
        'deployment_id': 'str',
        'node_tags': 'list[DeploymentTag]',
        'node_num': 'int'
    }

    attribute_map = {
        'node_ids': 'node_ids',
        'deployment_id': 'deployment_id',
        'node_tags': 'node_tags',
        'node_num': 'node_num'
    }

    def __init__(self, node_ids=None, deployment_id=None, node_tags=None, node_num=None):
        """DeploymentAddNodesRequest

        The model defined in huaweicloud sdk

        :param node_ids: 应用部署到指定节点
        :type node_ids: list[str]
        :param deployment_id: 应用部署ID
        :type deployment_id: str
        :param node_tags: 添加节点的标签
        :type node_tags: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        :param node_num: 添加的节点数量
        :type node_num: int
        """
        
        

        self._node_ids = None
        self._deployment_id = None
        self._node_tags = None
        self._node_num = None
        self.discriminator = None

        if node_ids is not None:
            self.node_ids = node_ids
        self.deployment_id = deployment_id
        if node_tags is not None:
            self.node_tags = node_tags
        self.node_num = node_num

    @property
    def node_ids(self):
        """Gets the node_ids of this DeploymentAddNodesRequest.

        应用部署到指定节点

        :return: The node_ids of this DeploymentAddNodesRequest.
        :rtype: list[str]
        """
        return self._node_ids

    @node_ids.setter
    def node_ids(self, node_ids):
        """Sets the node_ids of this DeploymentAddNodesRequest.

        应用部署到指定节点

        :param node_ids: The node_ids of this DeploymentAddNodesRequest.
        :type node_ids: list[str]
        """
        self._node_ids = node_ids

    @property
    def deployment_id(self):
        """Gets the deployment_id of this DeploymentAddNodesRequest.

        应用部署ID

        :return: The deployment_id of this DeploymentAddNodesRequest.
        :rtype: str
        """
        return self._deployment_id

    @deployment_id.setter
    def deployment_id(self, deployment_id):
        """Sets the deployment_id of this DeploymentAddNodesRequest.

        应用部署ID

        :param deployment_id: The deployment_id of this DeploymentAddNodesRequest.
        :type deployment_id: str
        """
        self._deployment_id = deployment_id

    @property
    def node_tags(self):
        """Gets the node_tags of this DeploymentAddNodesRequest.

        添加节点的标签

        :return: The node_tags of this DeploymentAddNodesRequest.
        :rtype: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        """
        return self._node_tags

    @node_tags.setter
    def node_tags(self, node_tags):
        """Sets the node_tags of this DeploymentAddNodesRequest.

        添加节点的标签

        :param node_tags: The node_tags of this DeploymentAddNodesRequest.
        :type node_tags: list[:class:`huaweicloudsdkhilens.v3.DeploymentTag`]
        """
        self._node_tags = node_tags

    @property
    def node_num(self):
        """Gets the node_num of this DeploymentAddNodesRequest.

        添加的节点数量

        :return: The node_num of this DeploymentAddNodesRequest.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this DeploymentAddNodesRequest.

        添加的节点数量

        :param node_num: The node_num of this DeploymentAddNodesRequest.
        :type node_num: int
        """
        self._node_num = node_num

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
        if not isinstance(other, DeploymentAddNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
