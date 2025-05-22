# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Nodes:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name'
    }

    def __init__(self, id=None, status=None, name=None):
        r"""Nodes

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 集群实例ID。 **取值范围**： 不涉及。
        :type id: str
        :param status: **参数解释**： 集群实例状态。 **取值范围**： 100：创建中 199：空闲 200：可用 300：不可用 303：创建失败 304：删除中 305：删除失败 400：已删除
        :type status: str
        :param name: **参数解释**： 实例名称。 **取值范围**： 不涉及。
        :type name: str
        """
        
        

        self._id = None
        self._status = None
        self._name = None
        self.discriminator = None

        self.id = id
        self.status = status
        if name is not None:
            self.name = name

    @property
    def id(self):
        r"""Gets the id of this Nodes.

        **参数解释**： 集群实例ID。 **取值范围**： 不涉及。

        :return: The id of this Nodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Nodes.

        **参数解释**： 集群实例ID。 **取值范围**： 不涉及。

        :param id: The id of this Nodes.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this Nodes.

        **参数解释**： 集群实例状态。 **取值范围**： 100：创建中 199：空闲 200：可用 300：不可用 303：创建失败 304：删除中 305：删除失败 400：已删除

        :return: The status of this Nodes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Nodes.

        **参数解释**： 集群实例状态。 **取值范围**： 100：创建中 199：空闲 200：可用 300：不可用 303：创建失败 304：删除中 305：删除失败 400：已删除

        :param status: The status of this Nodes.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this Nodes.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :return: The name of this Nodes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Nodes.

        **参数解释**： 实例名称。 **取值范围**： 不涉及。

        :param name: The name of this Nodes.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, Nodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
