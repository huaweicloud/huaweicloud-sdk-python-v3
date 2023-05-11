# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeGroupV10:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'node_num': 'int',
        'node_size': 'str',
        'node_spec_id': 'str',
        'vm_product_id': 'str',
        'vm_spec_code': 'str',
        'node_product_id': 'str',
        'root_volume_size': 'int',
        'root_volume_product_id': 'str',
        'root_volume_type': 'str',
        'root_volume_resource_spec_code': 'str',
        'root_volume_resource_type': 'str',
        'data_volume_type': 'str',
        'data_volume_count': 'int',
        'data_volume_size': 'int',
        'data_volume_product_id': 'str',
        'data_volume_resource_spec_code': 'str',
        'data_volume_resource_type': 'str'
    }

    attribute_map = {
        'group_name': 'GroupName',
        'node_num': 'NodeNum',
        'node_size': 'NodeSize',
        'node_spec_id': 'NodeSpecId',
        'vm_product_id': 'VmProductId',
        'vm_spec_code': 'VmSpecCode',
        'node_product_id': 'NodeProductId',
        'root_volume_size': 'RootVolumeSize',
        'root_volume_product_id': 'RootVolumeProductId',
        'root_volume_type': 'RootVolumeType',
        'root_volume_resource_spec_code': 'RootVolumeResourceSpecCode',
        'root_volume_resource_type': 'RootVolumeResourceType',
        'data_volume_type': 'DataVolumeType',
        'data_volume_count': 'DataVolumeCount',
        'data_volume_size': 'DataVolumeSize',
        'data_volume_product_id': 'DataVolumeProductId',
        'data_volume_resource_spec_code': 'DataVolumeResourceSpecCode',
        'data_volume_resource_type': 'DataVolumeResourceType'
    }

    def __init__(self, group_name=None, node_num=None, node_size=None, node_spec_id=None, vm_product_id=None, vm_spec_code=None, node_product_id=None, root_volume_size=None, root_volume_product_id=None, root_volume_type=None, root_volume_resource_spec_code=None, root_volume_resource_type=None, data_volume_type=None, data_volume_count=None, data_volume_size=None, data_volume_product_id=None, data_volume_resource_spec_code=None, data_volume_resource_type=None):
        """NodeGroupV10

        The model defined in huaweicloud sdk

        :param group_name: 节点组名。
        :type group_name: str
        :param node_num: 节点数量，取值范围0～500，Master节点和Core节点数量至少为1，Core与Task节点总数最大为500个。
        :type node_num: int
        :param node_size: 节点的实例规格。
        :type node_size: str
        :param node_spec_id: 节点实例规格ID。
        :type node_spec_id: str
        :param vm_product_id: 节点虚拟机产品ID。
        :type vm_product_id: str
        :param vm_spec_code: 节点虚拟机产品规格。
        :type vm_spec_code: str
        :param node_product_id: 节点实例产品ID。
        :type node_product_id: str
        :param root_volume_size: 节点系统盘大小，不可配置，默认为40GB。
        :type root_volume_size: int
        :param root_volume_product_id: 节点系统盘的产品ID。
        :type root_volume_product_id: str
        :param root_volume_type: 节点系统盘的类型。
        :type root_volume_type: str
        :param root_volume_resource_spec_code: 节点系统盘产品规格。
        :type root_volume_resource_spec_code: str
        :param root_volume_resource_type: 节点系统盘产品类型。
        :type root_volume_resource_type: str
        :param data_volume_type: 节点数据磁盘存储类别，目前支持SATA、SAS和SSD。  - SATA：普通IO - SAS：高IO - SSD：超高IO
        :type data_volume_type: str
        :param data_volume_count: 节点数据磁盘存储数目。
        :type data_volume_count: int
        :param data_volume_size: 节点数据磁盘存储大小。
        :type data_volume_size: int
        :param data_volume_product_id: 节点数据磁盘的产品ID。
        :type data_volume_product_id: str
        :param data_volume_resource_spec_code: 节点数据磁盘的产品规格。
        :type data_volume_resource_spec_code: str
        :param data_volume_resource_type: 节点数据磁盘的产品类型。
        :type data_volume_resource_type: str
        """
        
        

        self._group_name = None
        self._node_num = None
        self._node_size = None
        self._node_spec_id = None
        self._vm_product_id = None
        self._vm_spec_code = None
        self._node_product_id = None
        self._root_volume_size = None
        self._root_volume_product_id = None
        self._root_volume_type = None
        self._root_volume_resource_spec_code = None
        self._root_volume_resource_type = None
        self._data_volume_type = None
        self._data_volume_count = None
        self._data_volume_size = None
        self._data_volume_product_id = None
        self._data_volume_resource_spec_code = None
        self._data_volume_resource_type = None
        self.discriminator = None

        if group_name is not None:
            self.group_name = group_name
        if node_num is not None:
            self.node_num = node_num
        if node_size is not None:
            self.node_size = node_size
        if node_spec_id is not None:
            self.node_spec_id = node_spec_id
        if vm_product_id is not None:
            self.vm_product_id = vm_product_id
        if vm_spec_code is not None:
            self.vm_spec_code = vm_spec_code
        if node_product_id is not None:
            self.node_product_id = node_product_id
        if root_volume_size is not None:
            self.root_volume_size = root_volume_size
        if root_volume_product_id is not None:
            self.root_volume_product_id = root_volume_product_id
        if root_volume_type is not None:
            self.root_volume_type = root_volume_type
        if root_volume_resource_spec_code is not None:
            self.root_volume_resource_spec_code = root_volume_resource_spec_code
        if root_volume_resource_type is not None:
            self.root_volume_resource_type = root_volume_resource_type
        if data_volume_type is not None:
            self.data_volume_type = data_volume_type
        if data_volume_count is not None:
            self.data_volume_count = data_volume_count
        if data_volume_size is not None:
            self.data_volume_size = data_volume_size
        if data_volume_product_id is not None:
            self.data_volume_product_id = data_volume_product_id
        if data_volume_resource_spec_code is not None:
            self.data_volume_resource_spec_code = data_volume_resource_spec_code
        if data_volume_resource_type is not None:
            self.data_volume_resource_type = data_volume_resource_type

    @property
    def group_name(self):
        """Gets the group_name of this NodeGroupV10.

        节点组名。

        :return: The group_name of this NodeGroupV10.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this NodeGroupV10.

        节点组名。

        :param group_name: The group_name of this NodeGroupV10.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def node_num(self):
        """Gets the node_num of this NodeGroupV10.

        节点数量，取值范围0～500，Master节点和Core节点数量至少为1，Core与Task节点总数最大为500个。

        :return: The node_num of this NodeGroupV10.
        :rtype: int
        """
        return self._node_num

    @node_num.setter
    def node_num(self, node_num):
        """Sets the node_num of this NodeGroupV10.

        节点数量，取值范围0～500，Master节点和Core节点数量至少为1，Core与Task节点总数最大为500个。

        :param node_num: The node_num of this NodeGroupV10.
        :type node_num: int
        """
        self._node_num = node_num

    @property
    def node_size(self):
        """Gets the node_size of this NodeGroupV10.

        节点的实例规格。

        :return: The node_size of this NodeGroupV10.
        :rtype: str
        """
        return self._node_size

    @node_size.setter
    def node_size(self, node_size):
        """Sets the node_size of this NodeGroupV10.

        节点的实例规格。

        :param node_size: The node_size of this NodeGroupV10.
        :type node_size: str
        """
        self._node_size = node_size

    @property
    def node_spec_id(self):
        """Gets the node_spec_id of this NodeGroupV10.

        节点实例规格ID。

        :return: The node_spec_id of this NodeGroupV10.
        :rtype: str
        """
        return self._node_spec_id

    @node_spec_id.setter
    def node_spec_id(self, node_spec_id):
        """Sets the node_spec_id of this NodeGroupV10.

        节点实例规格ID。

        :param node_spec_id: The node_spec_id of this NodeGroupV10.
        :type node_spec_id: str
        """
        self._node_spec_id = node_spec_id

    @property
    def vm_product_id(self):
        """Gets the vm_product_id of this NodeGroupV10.

        节点虚拟机产品ID。

        :return: The vm_product_id of this NodeGroupV10.
        :rtype: str
        """
        return self._vm_product_id

    @vm_product_id.setter
    def vm_product_id(self, vm_product_id):
        """Sets the vm_product_id of this NodeGroupV10.

        节点虚拟机产品ID。

        :param vm_product_id: The vm_product_id of this NodeGroupV10.
        :type vm_product_id: str
        """
        self._vm_product_id = vm_product_id

    @property
    def vm_spec_code(self):
        """Gets the vm_spec_code of this NodeGroupV10.

        节点虚拟机产品规格。

        :return: The vm_spec_code of this NodeGroupV10.
        :rtype: str
        """
        return self._vm_spec_code

    @vm_spec_code.setter
    def vm_spec_code(self, vm_spec_code):
        """Sets the vm_spec_code of this NodeGroupV10.

        节点虚拟机产品规格。

        :param vm_spec_code: The vm_spec_code of this NodeGroupV10.
        :type vm_spec_code: str
        """
        self._vm_spec_code = vm_spec_code

    @property
    def node_product_id(self):
        """Gets the node_product_id of this NodeGroupV10.

        节点实例产品ID。

        :return: The node_product_id of this NodeGroupV10.
        :rtype: str
        """
        return self._node_product_id

    @node_product_id.setter
    def node_product_id(self, node_product_id):
        """Sets the node_product_id of this NodeGroupV10.

        节点实例产品ID。

        :param node_product_id: The node_product_id of this NodeGroupV10.
        :type node_product_id: str
        """
        self._node_product_id = node_product_id

    @property
    def root_volume_size(self):
        """Gets the root_volume_size of this NodeGroupV10.

        节点系统盘大小，不可配置，默认为40GB。

        :return: The root_volume_size of this NodeGroupV10.
        :rtype: int
        """
        return self._root_volume_size

    @root_volume_size.setter
    def root_volume_size(self, root_volume_size):
        """Sets the root_volume_size of this NodeGroupV10.

        节点系统盘大小，不可配置，默认为40GB。

        :param root_volume_size: The root_volume_size of this NodeGroupV10.
        :type root_volume_size: int
        """
        self._root_volume_size = root_volume_size

    @property
    def root_volume_product_id(self):
        """Gets the root_volume_product_id of this NodeGroupV10.

        节点系统盘的产品ID。

        :return: The root_volume_product_id of this NodeGroupV10.
        :rtype: str
        """
        return self._root_volume_product_id

    @root_volume_product_id.setter
    def root_volume_product_id(self, root_volume_product_id):
        """Sets the root_volume_product_id of this NodeGroupV10.

        节点系统盘的产品ID。

        :param root_volume_product_id: The root_volume_product_id of this NodeGroupV10.
        :type root_volume_product_id: str
        """
        self._root_volume_product_id = root_volume_product_id

    @property
    def root_volume_type(self):
        """Gets the root_volume_type of this NodeGroupV10.

        节点系统盘的类型。

        :return: The root_volume_type of this NodeGroupV10.
        :rtype: str
        """
        return self._root_volume_type

    @root_volume_type.setter
    def root_volume_type(self, root_volume_type):
        """Sets the root_volume_type of this NodeGroupV10.

        节点系统盘的类型。

        :param root_volume_type: The root_volume_type of this NodeGroupV10.
        :type root_volume_type: str
        """
        self._root_volume_type = root_volume_type

    @property
    def root_volume_resource_spec_code(self):
        """Gets the root_volume_resource_spec_code of this NodeGroupV10.

        节点系统盘产品规格。

        :return: The root_volume_resource_spec_code of this NodeGroupV10.
        :rtype: str
        """
        return self._root_volume_resource_spec_code

    @root_volume_resource_spec_code.setter
    def root_volume_resource_spec_code(self, root_volume_resource_spec_code):
        """Sets the root_volume_resource_spec_code of this NodeGroupV10.

        节点系统盘产品规格。

        :param root_volume_resource_spec_code: The root_volume_resource_spec_code of this NodeGroupV10.
        :type root_volume_resource_spec_code: str
        """
        self._root_volume_resource_spec_code = root_volume_resource_spec_code

    @property
    def root_volume_resource_type(self):
        """Gets the root_volume_resource_type of this NodeGroupV10.

        节点系统盘产品类型。

        :return: The root_volume_resource_type of this NodeGroupV10.
        :rtype: str
        """
        return self._root_volume_resource_type

    @root_volume_resource_type.setter
    def root_volume_resource_type(self, root_volume_resource_type):
        """Sets the root_volume_resource_type of this NodeGroupV10.

        节点系统盘产品类型。

        :param root_volume_resource_type: The root_volume_resource_type of this NodeGroupV10.
        :type root_volume_resource_type: str
        """
        self._root_volume_resource_type = root_volume_resource_type

    @property
    def data_volume_type(self):
        """Gets the data_volume_type of this NodeGroupV10.

        节点数据磁盘存储类别，目前支持SATA、SAS和SSD。  - SATA：普通IO - SAS：高IO - SSD：超高IO

        :return: The data_volume_type of this NodeGroupV10.
        :rtype: str
        """
        return self._data_volume_type

    @data_volume_type.setter
    def data_volume_type(self, data_volume_type):
        """Sets the data_volume_type of this NodeGroupV10.

        节点数据磁盘存储类别，目前支持SATA、SAS和SSD。  - SATA：普通IO - SAS：高IO - SSD：超高IO

        :param data_volume_type: The data_volume_type of this NodeGroupV10.
        :type data_volume_type: str
        """
        self._data_volume_type = data_volume_type

    @property
    def data_volume_count(self):
        """Gets the data_volume_count of this NodeGroupV10.

        节点数据磁盘存储数目。

        :return: The data_volume_count of this NodeGroupV10.
        :rtype: int
        """
        return self._data_volume_count

    @data_volume_count.setter
    def data_volume_count(self, data_volume_count):
        """Sets the data_volume_count of this NodeGroupV10.

        节点数据磁盘存储数目。

        :param data_volume_count: The data_volume_count of this NodeGroupV10.
        :type data_volume_count: int
        """
        self._data_volume_count = data_volume_count

    @property
    def data_volume_size(self):
        """Gets the data_volume_size of this NodeGroupV10.

        节点数据磁盘存储大小。

        :return: The data_volume_size of this NodeGroupV10.
        :rtype: int
        """
        return self._data_volume_size

    @data_volume_size.setter
    def data_volume_size(self, data_volume_size):
        """Sets the data_volume_size of this NodeGroupV10.

        节点数据磁盘存储大小。

        :param data_volume_size: The data_volume_size of this NodeGroupV10.
        :type data_volume_size: int
        """
        self._data_volume_size = data_volume_size

    @property
    def data_volume_product_id(self):
        """Gets the data_volume_product_id of this NodeGroupV10.

        节点数据磁盘的产品ID。

        :return: The data_volume_product_id of this NodeGroupV10.
        :rtype: str
        """
        return self._data_volume_product_id

    @data_volume_product_id.setter
    def data_volume_product_id(self, data_volume_product_id):
        """Sets the data_volume_product_id of this NodeGroupV10.

        节点数据磁盘的产品ID。

        :param data_volume_product_id: The data_volume_product_id of this NodeGroupV10.
        :type data_volume_product_id: str
        """
        self._data_volume_product_id = data_volume_product_id

    @property
    def data_volume_resource_spec_code(self):
        """Gets the data_volume_resource_spec_code of this NodeGroupV10.

        节点数据磁盘的产品规格。

        :return: The data_volume_resource_spec_code of this NodeGroupV10.
        :rtype: str
        """
        return self._data_volume_resource_spec_code

    @data_volume_resource_spec_code.setter
    def data_volume_resource_spec_code(self, data_volume_resource_spec_code):
        """Sets the data_volume_resource_spec_code of this NodeGroupV10.

        节点数据磁盘的产品规格。

        :param data_volume_resource_spec_code: The data_volume_resource_spec_code of this NodeGroupV10.
        :type data_volume_resource_spec_code: str
        """
        self._data_volume_resource_spec_code = data_volume_resource_spec_code

    @property
    def data_volume_resource_type(self):
        """Gets the data_volume_resource_type of this NodeGroupV10.

        节点数据磁盘的产品类型。

        :return: The data_volume_resource_type of this NodeGroupV10.
        :rtype: str
        """
        return self._data_volume_resource_type

    @data_volume_resource_type.setter
    def data_volume_resource_type(self, data_volume_resource_type):
        """Sets the data_volume_resource_type of this NodeGroupV10.

        节点数据磁盘的产品类型。

        :param data_volume_resource_type: The data_volume_resource_type of this NodeGroupV10.
        :type data_volume_resource_type: str
        """
        self._data_volume_resource_type = data_volume_resource_type

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
        if not isinstance(other, NodeGroupV10):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
