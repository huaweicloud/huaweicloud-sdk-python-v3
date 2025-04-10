# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGroupNodeBindingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add_node_ids': 'list[str]',
        'remove_node_ids': 'list[str]'
    }

    attribute_map = {
        'add_node_ids': 'add_node_ids',
        'remove_node_ids': 'remove_node_ids'
    }

    def __init__(self, add_node_ids=None, remove_node_ids=None):
        r"""UpdateGroupNodeBindingRequest

        The model defined in huaweicloud sdk

        :param add_node_ids: 新增绑定的节点ID列表
        :type add_node_ids: list[str]
        :param remove_node_ids: 新增解绑的节点ID列表
        :type remove_node_ids: list[str]
        """
        
        

        self._add_node_ids = None
        self._remove_node_ids = None
        self.discriminator = None

        if add_node_ids is not None:
            self.add_node_ids = add_node_ids
        if remove_node_ids is not None:
            self.remove_node_ids = remove_node_ids

    @property
    def add_node_ids(self):
        r"""Gets the add_node_ids of this UpdateGroupNodeBindingRequest.

        新增绑定的节点ID列表

        :return: The add_node_ids of this UpdateGroupNodeBindingRequest.
        :rtype: list[str]
        """
        return self._add_node_ids

    @add_node_ids.setter
    def add_node_ids(self, add_node_ids):
        r"""Sets the add_node_ids of this UpdateGroupNodeBindingRequest.

        新增绑定的节点ID列表

        :param add_node_ids: The add_node_ids of this UpdateGroupNodeBindingRequest.
        :type add_node_ids: list[str]
        """
        self._add_node_ids = add_node_ids

    @property
    def remove_node_ids(self):
        r"""Gets the remove_node_ids of this UpdateGroupNodeBindingRequest.

        新增解绑的节点ID列表

        :return: The remove_node_ids of this UpdateGroupNodeBindingRequest.
        :rtype: list[str]
        """
        return self._remove_node_ids

    @remove_node_ids.setter
    def remove_node_ids(self, remove_node_ids):
        r"""Sets the remove_node_ids of this UpdateGroupNodeBindingRequest.

        新增解绑的节点ID列表

        :param remove_node_ids: The remove_node_ids of this UpdateGroupNodeBindingRequest.
        :type remove_node_ids: list[str]
        """
        self._remove_node_ids = remove_node_ids

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
        if not isinstance(other, UpdateGroupNodeBindingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
