# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteIpFromDomainNameRequest:

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
        'group_id': 'str',
        'node_id': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'node_id': 'node_id'
    }

    def __init__(self, instance_id=None, group_id=None, node_id=None):
        r"""DeleteIpFromDomainNameRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param group_id: 分片ID。
        :type group_id: str
        :param node_id: 节点ID。
        :type node_id: str
        """
        
        

        self._instance_id = None
        self._group_id = None
        self._node_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group_id = group_id
        self.node_id = node_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DeleteIpFromDomainNameRequest.

        实例ID。

        :return: The instance_id of this DeleteIpFromDomainNameRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DeleteIpFromDomainNameRequest.

        实例ID。

        :param instance_id: The instance_id of this DeleteIpFromDomainNameRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        r"""Gets the group_id of this DeleteIpFromDomainNameRequest.

        分片ID。

        :return: The group_id of this DeleteIpFromDomainNameRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this DeleteIpFromDomainNameRequest.

        分片ID。

        :param group_id: The group_id of this DeleteIpFromDomainNameRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def node_id(self):
        r"""Gets the node_id of this DeleteIpFromDomainNameRequest.

        节点ID。

        :return: The node_id of this DeleteIpFromDomainNameRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this DeleteIpFromDomainNameRequest.

        节点ID。

        :param node_id: The node_id of this DeleteIpFromDomainNameRequest.
        :type node_id: str
        """
        self._node_id = node_id

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
        if not isinstance(other, DeleteIpFromDomainNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
