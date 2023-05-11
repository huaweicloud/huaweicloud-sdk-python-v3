# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteNodeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'force_delete': 'bool'
    }

    attribute_map = {
        'node_id': 'node_id',
        'force_delete': 'force_delete'
    }

    def __init__(self, node_id=None, force_delete=None):
        """DeleteNodeRequest

        The model defined in huaweicloud sdk

        :param node_id: 设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取
        :type node_id: str
        :param force_delete: 是否强制删除，true代表是，false代表否
        :type force_delete: bool
        """
        
        

        self._node_id = None
        self._force_delete = None
        self.discriminator = None

        self.node_id = node_id
        if force_delete is not None:
            self.force_delete = force_delete

    @property
    def node_id(self):
        """Gets the node_id of this DeleteNodeRequest.

        设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取

        :return: The node_id of this DeleteNodeRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DeleteNodeRequest.

        设备ID，从专业版HiLens控制台设备管理[查询设备列表](ListNodeUsingGeT.xml)获取

        :param node_id: The node_id of this DeleteNodeRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def force_delete(self):
        """Gets the force_delete of this DeleteNodeRequest.

        是否强制删除，true代表是，false代表否

        :return: The force_delete of this DeleteNodeRequest.
        :rtype: bool
        """
        return self._force_delete

    @force_delete.setter
    def force_delete(self, force_delete):
        """Sets the force_delete of this DeleteNodeRequest.

        是否强制删除，true代表是，false代表否

        :param force_delete: The force_delete of this DeleteNodeRequest.
        :type force_delete: bool
        """
        self._force_delete = force_delete

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
        if not isinstance(other, DeleteNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
