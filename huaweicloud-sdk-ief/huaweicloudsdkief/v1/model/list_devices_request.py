# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevicesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'name': 'str',
        'node_id': 'str',
        'limit': 'str',
        'offset': 'str',
        'is_binding': 'str',
        'tags': 'str'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'name': 'name',
        'node_id': 'node_id',
        'limit': 'limit',
        'offset': 'offset',
        'is_binding': 'is_binding',
        'tags': 'tags'
    }

    def __init__(self, ief_instance_id=None, name=None, node_id=None, limit=None, offset=None, is_binding=None, tags=None):
        r"""ListDevicesRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param name: 终端设备名称，模糊匹配
        :type name: str
        :param node_id: 节点ID, 精确匹配
        :type node_id: str
        :param limit: 每页显示的条目数量，取值范围1~1000，默认为1000
        :type limit: str
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: str
        :param is_binding: 是否绑定到边缘节点，为“true”时返回所有已绑定到节点的设备列表；为“false”则返回未绑定节点的设备列表。
        :type is_binding: str
        :param tags: 标签的key和value通过点连接， 多个标签通过逗号连接，如：tags&#x3D;key1.value1,key2.value2
        :type tags: str
        """
        
        

        self._ief_instance_id = None
        self._name = None
        self._node_id = None
        self._limit = None
        self._offset = None
        self._is_binding = None
        self._tags = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if name is not None:
            self.name = name
        if node_id is not None:
            self.node_id = node_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if is_binding is not None:
            self.is_binding = is_binding
        if tags is not None:
            self.tags = tags

    @property
    def ief_instance_id(self):
        r"""Gets the ief_instance_id of this ListDevicesRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        r"""Sets the ief_instance_id of this ListDevicesRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListDevicesRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def name(self):
        r"""Gets the name of this ListDevicesRequest.

        终端设备名称，模糊匹配

        :return: The name of this ListDevicesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDevicesRequest.

        终端设备名称，模糊匹配

        :param name: The name of this ListDevicesRequest.
        :type name: str
        """
        self._name = name

    @property
    def node_id(self):
        r"""Gets the node_id of this ListDevicesRequest.

        节点ID, 精确匹配

        :return: The node_id of this ListDevicesRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ListDevicesRequest.

        节点ID, 精确匹配

        :param node_id: The node_id of this ListDevicesRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def limit(self):
        r"""Gets the limit of this ListDevicesRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :return: The limit of this ListDevicesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDevicesRequest.

        每页显示的条目数量，取值范围1~1000，默认为1000

        :param limit: The limit of this ListDevicesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListDevicesRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDevicesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListDevicesRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def is_binding(self):
        r"""Gets the is_binding of this ListDevicesRequest.

        是否绑定到边缘节点，为“true”时返回所有已绑定到节点的设备列表；为“false”则返回未绑定节点的设备列表。

        :return: The is_binding of this ListDevicesRequest.
        :rtype: str
        """
        return self._is_binding

    @is_binding.setter
    def is_binding(self, is_binding):
        r"""Sets the is_binding of this ListDevicesRequest.

        是否绑定到边缘节点，为“true”时返回所有已绑定到节点的设备列表；为“false”则返回未绑定节点的设备列表。

        :param is_binding: The is_binding of this ListDevicesRequest.
        :type is_binding: str
        """
        self._is_binding = is_binding

    @property
    def tags(self):
        r"""Gets the tags of this ListDevicesRequest.

        标签的key和value通过点连接， 多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :return: The tags of this ListDevicesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListDevicesRequest.

        标签的key和value通过点连接， 多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :param tags: The tags of this ListDevicesRequest.
        :type tags: str
        """
        self._tags = tags

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
        if not isinstance(other, ListDevicesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
