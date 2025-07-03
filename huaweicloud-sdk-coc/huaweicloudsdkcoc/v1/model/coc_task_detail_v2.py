# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocTaskDetailV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'key': 'str',
        'name': 'str',
        'state': 'str',
        'operations': 'list[CocTaskOperationDetailV2]'
    }

    attribute_map = {
        'type': 'type',
        'key': 'key',
        'name': 'name',
        'state': 'state',
        'operations': 'operations'
    }

    def __init__(self, type=None, key=None, name=None, state=None, operations=None):
        r"""CocTaskDetailV2

        The model defined in huaweicloud sdk

        :param type: 节点类型
        :type type: str
        :param key: 节点KEY
        :type key: str
        :param name: 节点名称
        :type name: str
        :param state: 节点类型
        :type state: str
        :param operations: 操作列表
        :type operations: list[:class:`huaweicloudsdkcoc.v1.CocTaskOperationDetailV2`]
        """
        
        

        self._type = None
        self._key = None
        self._name = None
        self._state = None
        self._operations = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if operations is not None:
            self.operations = operations

    @property
    def type(self):
        r"""Gets the type of this CocTaskDetailV2.

        节点类型

        :return: The type of this CocTaskDetailV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CocTaskDetailV2.

        节点类型

        :param type: The type of this CocTaskDetailV2.
        :type type: str
        """
        self._type = type

    @property
    def key(self):
        r"""Gets the key of this CocTaskDetailV2.

        节点KEY

        :return: The key of this CocTaskDetailV2.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this CocTaskDetailV2.

        节点KEY

        :param key: The key of this CocTaskDetailV2.
        :type key: str
        """
        self._key = key

    @property
    def name(self):
        r"""Gets the name of this CocTaskDetailV2.

        节点名称

        :return: The name of this CocTaskDetailV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CocTaskDetailV2.

        节点名称

        :param name: The name of this CocTaskDetailV2.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        r"""Gets the state of this CocTaskDetailV2.

        节点类型

        :return: The state of this CocTaskDetailV2.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CocTaskDetailV2.

        节点类型

        :param state: The state of this CocTaskDetailV2.
        :type state: str
        """
        self._state = state

    @property
    def operations(self):
        r"""Gets the operations of this CocTaskDetailV2.

        操作列表

        :return: The operations of this CocTaskDetailV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CocTaskOperationDetailV2`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this CocTaskDetailV2.

        操作列表

        :param operations: The operations of this CocTaskDetailV2.
        :type operations: list[:class:`huaweicloudsdkcoc.v1.CocTaskOperationDetailV2`]
        """
        self._operations = operations

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
        if not isinstance(other, CocTaskDetailV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
