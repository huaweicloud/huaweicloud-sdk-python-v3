# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeOwnerReference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodepool_name': 'str',
        'nodepool_id': 'str'
    }

    attribute_map = {
        'nodepool_name': 'nodepoolName',
        'nodepool_id': 'nodepoolID'
    }

    def __init__(self, nodepool_name=None, nodepool_id=None):
        r"""NodeOwnerReference

        The model defined in huaweicloud sdk

        :param nodepool_name: 节点池名称
        :type nodepool_name: str
        :param nodepool_id: 节点池UID
        :type nodepool_id: str
        """
        
        

        self._nodepool_name = None
        self._nodepool_id = None
        self.discriminator = None

        if nodepool_name is not None:
            self.nodepool_name = nodepool_name
        if nodepool_id is not None:
            self.nodepool_id = nodepool_id

    @property
    def nodepool_name(self):
        r"""Gets the nodepool_name of this NodeOwnerReference.

        节点池名称

        :return: The nodepool_name of this NodeOwnerReference.
        :rtype: str
        """
        return self._nodepool_name

    @nodepool_name.setter
    def nodepool_name(self, nodepool_name):
        r"""Sets the nodepool_name of this NodeOwnerReference.

        节点池名称

        :param nodepool_name: The nodepool_name of this NodeOwnerReference.
        :type nodepool_name: str
        """
        self._nodepool_name = nodepool_name

    @property
    def nodepool_id(self):
        r"""Gets the nodepool_id of this NodeOwnerReference.

        节点池UID

        :return: The nodepool_id of this NodeOwnerReference.
        :rtype: str
        """
        return self._nodepool_id

    @nodepool_id.setter
    def nodepool_id(self, nodepool_id):
        r"""Sets the nodepool_id of this NodeOwnerReference.

        节点池UID

        :param nodepool_id: The nodepool_id of this NodeOwnerReference.
        :type nodepool_id: str
        """
        self._nodepool_id = nodepool_id

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
        if not isinstance(other, NodeOwnerReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
