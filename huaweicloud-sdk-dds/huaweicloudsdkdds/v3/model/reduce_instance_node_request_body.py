# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReduceInstanceNodeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'num': 'int',
        'node_list': 'list[str]'
    }

    attribute_map = {
        'num': 'num',
        'node_list': 'node_list'
    }

    def __init__(self, num=None, node_list=None):
        r"""ReduceInstanceNodeRequestBody

        The model defined in huaweicloud sdk

        :param num: 删除的节点数量。
        :type num: int
        :param node_list: 指定删除节点的ID列表。 - num与node_list必须有一个字段传值 - 如果num与node_list同时传值时，则以node_list的值为主 - 删除的节点角色不能是Primary - 如果是多AZ实例，请确保删除节点后，每个AZ至少保留一个节点
        :type node_list: list[str]
        """
        
        

        self._num = None
        self._node_list = None
        self.discriminator = None

        if num is not None:
            self.num = num
        if node_list is not None:
            self.node_list = node_list

    @property
    def num(self):
        r"""Gets the num of this ReduceInstanceNodeRequestBody.

        删除的节点数量。

        :return: The num of this ReduceInstanceNodeRequestBody.
        :rtype: int
        """
        return self._num

    @num.setter
    def num(self, num):
        r"""Sets the num of this ReduceInstanceNodeRequestBody.

        删除的节点数量。

        :param num: The num of this ReduceInstanceNodeRequestBody.
        :type num: int
        """
        self._num = num

    @property
    def node_list(self):
        r"""Gets the node_list of this ReduceInstanceNodeRequestBody.

        指定删除节点的ID列表。 - num与node_list必须有一个字段传值 - 如果num与node_list同时传值时，则以node_list的值为主 - 删除的节点角色不能是Primary - 如果是多AZ实例，请确保删除节点后，每个AZ至少保留一个节点

        :return: The node_list of this ReduceInstanceNodeRequestBody.
        :rtype: list[str]
        """
        return self._node_list

    @node_list.setter
    def node_list(self, node_list):
        r"""Sets the node_list of this ReduceInstanceNodeRequestBody.

        指定删除节点的ID列表。 - num与node_list必须有一个字段传值 - 如果num与node_list同时传值时，则以node_list的值为主 - 删除的节点角色不能是Primary - 如果是多AZ实例，请确保删除节点后，每个AZ至少保留一个节点

        :param node_list: The node_list of this ReduceInstanceNodeRequestBody.
        :type node_list: list[str]
        """
        self._node_list = node_list

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
        if not isinstance(other, ReduceInstanceNodeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
