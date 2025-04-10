# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeConstraint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'other': 'dict(str, object)',
        'min_node_num': 'int',
        'max_node_num': 'int',
        'min_core_num': 'dict(str, int)',
        'min_mem_size': 'dict(str, int)',
        'min_disk_size': 'int',
        'max_node_group_num': 'int',
        'min_data_volume_total_size': 'dict(str, int)',
        'disk_type_constraint': 'dict(str, str)',
        'min_root_disk_size': 'int'
    }

    attribute_map = {
        'other': 'other',
        'min_node_num': 'min_node_num',
        'max_node_num': 'max_node_num',
        'min_core_num': 'min_core_num',
        'min_mem_size': 'min_mem_size',
        'min_disk_size': 'min_disk_size',
        'max_node_group_num': 'max_node_group_num',
        'min_data_volume_total_size': 'min_data_volume_total_size',
        'disk_type_constraint': 'disk_type_constraint',
        'min_root_disk_size': 'min_root_disk_size'
    }

    def __init__(self, other=None, min_node_num=None, max_node_num=None, min_core_num=None, min_mem_size=None, min_disk_size=None, max_node_group_num=None, min_data_volume_total_size=None, disk_type_constraint=None, min_root_disk_size=None):
        r"""NodeConstraint

        The model defined in huaweicloud sdk

        :param other: 其他限制
        :type other: dict(str, object)
        :param min_node_num: 最少节点数
        :type min_node_num: int
        :param max_node_num: 最多节点数
        :type max_node_num: int
        :param min_core_num: 最少核心数
        :type min_core_num: dict(str, int)
        :param min_mem_size: 最小内存容量
        :type min_mem_size: dict(str, int)
        :param min_disk_size: 最小磁盘容量
        :type min_disk_size: int
        :param max_node_group_num: 最大节点组数
        :type max_node_group_num: int
        :param min_data_volume_total_size: 最小数据卷容量
        :type min_data_volume_total_size: dict(str, int)
        :param disk_type_constraint: 磁盘类型限制，包含当前节点组所支持的磁盘类型
        :type disk_type_constraint: dict(str, str)
        :param min_root_disk_size: 最小系统磁盘大小
        :type min_root_disk_size: int
        """
        
        

        self._other = None
        self._min_node_num = None
        self._max_node_num = None
        self._min_core_num = None
        self._min_mem_size = None
        self._min_disk_size = None
        self._max_node_group_num = None
        self._min_data_volume_total_size = None
        self._disk_type_constraint = None
        self._min_root_disk_size = None
        self.discriminator = None

        if other is not None:
            self.other = other
        if min_node_num is not None:
            self.min_node_num = min_node_num
        if max_node_num is not None:
            self.max_node_num = max_node_num
        if min_core_num is not None:
            self.min_core_num = min_core_num
        if min_mem_size is not None:
            self.min_mem_size = min_mem_size
        if min_disk_size is not None:
            self.min_disk_size = min_disk_size
        if max_node_group_num is not None:
            self.max_node_group_num = max_node_group_num
        if min_data_volume_total_size is not None:
            self.min_data_volume_total_size = min_data_volume_total_size
        if disk_type_constraint is not None:
            self.disk_type_constraint = disk_type_constraint
        if min_root_disk_size is not None:
            self.min_root_disk_size = min_root_disk_size

    @property
    def other(self):
        r"""Gets the other of this NodeConstraint.

        其他限制

        :return: The other of this NodeConstraint.
        :rtype: dict(str, object)
        """
        return self._other

    @other.setter
    def other(self, other):
        r"""Sets the other of this NodeConstraint.

        其他限制

        :param other: The other of this NodeConstraint.
        :type other: dict(str, object)
        """
        self._other = other

    @property
    def min_node_num(self):
        r"""Gets the min_node_num of this NodeConstraint.

        最少节点数

        :return: The min_node_num of this NodeConstraint.
        :rtype: int
        """
        return self._min_node_num

    @min_node_num.setter
    def min_node_num(self, min_node_num):
        r"""Sets the min_node_num of this NodeConstraint.

        最少节点数

        :param min_node_num: The min_node_num of this NodeConstraint.
        :type min_node_num: int
        """
        self._min_node_num = min_node_num

    @property
    def max_node_num(self):
        r"""Gets the max_node_num of this NodeConstraint.

        最多节点数

        :return: The max_node_num of this NodeConstraint.
        :rtype: int
        """
        return self._max_node_num

    @max_node_num.setter
    def max_node_num(self, max_node_num):
        r"""Sets the max_node_num of this NodeConstraint.

        最多节点数

        :param max_node_num: The max_node_num of this NodeConstraint.
        :type max_node_num: int
        """
        self._max_node_num = max_node_num

    @property
    def min_core_num(self):
        r"""Gets the min_core_num of this NodeConstraint.

        最少核心数

        :return: The min_core_num of this NodeConstraint.
        :rtype: dict(str, int)
        """
        return self._min_core_num

    @min_core_num.setter
    def min_core_num(self, min_core_num):
        r"""Sets the min_core_num of this NodeConstraint.

        最少核心数

        :param min_core_num: The min_core_num of this NodeConstraint.
        :type min_core_num: dict(str, int)
        """
        self._min_core_num = min_core_num

    @property
    def min_mem_size(self):
        r"""Gets the min_mem_size of this NodeConstraint.

        最小内存容量

        :return: The min_mem_size of this NodeConstraint.
        :rtype: dict(str, int)
        """
        return self._min_mem_size

    @min_mem_size.setter
    def min_mem_size(self, min_mem_size):
        r"""Sets the min_mem_size of this NodeConstraint.

        最小内存容量

        :param min_mem_size: The min_mem_size of this NodeConstraint.
        :type min_mem_size: dict(str, int)
        """
        self._min_mem_size = min_mem_size

    @property
    def min_disk_size(self):
        r"""Gets the min_disk_size of this NodeConstraint.

        最小磁盘容量

        :return: The min_disk_size of this NodeConstraint.
        :rtype: int
        """
        return self._min_disk_size

    @min_disk_size.setter
    def min_disk_size(self, min_disk_size):
        r"""Sets the min_disk_size of this NodeConstraint.

        最小磁盘容量

        :param min_disk_size: The min_disk_size of this NodeConstraint.
        :type min_disk_size: int
        """
        self._min_disk_size = min_disk_size

    @property
    def max_node_group_num(self):
        r"""Gets the max_node_group_num of this NodeConstraint.

        最大节点组数

        :return: The max_node_group_num of this NodeConstraint.
        :rtype: int
        """
        return self._max_node_group_num

    @max_node_group_num.setter
    def max_node_group_num(self, max_node_group_num):
        r"""Sets the max_node_group_num of this NodeConstraint.

        最大节点组数

        :param max_node_group_num: The max_node_group_num of this NodeConstraint.
        :type max_node_group_num: int
        """
        self._max_node_group_num = max_node_group_num

    @property
    def min_data_volume_total_size(self):
        r"""Gets the min_data_volume_total_size of this NodeConstraint.

        最小数据卷容量

        :return: The min_data_volume_total_size of this NodeConstraint.
        :rtype: dict(str, int)
        """
        return self._min_data_volume_total_size

    @min_data_volume_total_size.setter
    def min_data_volume_total_size(self, min_data_volume_total_size):
        r"""Sets the min_data_volume_total_size of this NodeConstraint.

        最小数据卷容量

        :param min_data_volume_total_size: The min_data_volume_total_size of this NodeConstraint.
        :type min_data_volume_total_size: dict(str, int)
        """
        self._min_data_volume_total_size = min_data_volume_total_size

    @property
    def disk_type_constraint(self):
        r"""Gets the disk_type_constraint of this NodeConstraint.

        磁盘类型限制，包含当前节点组所支持的磁盘类型

        :return: The disk_type_constraint of this NodeConstraint.
        :rtype: dict(str, str)
        """
        return self._disk_type_constraint

    @disk_type_constraint.setter
    def disk_type_constraint(self, disk_type_constraint):
        r"""Sets the disk_type_constraint of this NodeConstraint.

        磁盘类型限制，包含当前节点组所支持的磁盘类型

        :param disk_type_constraint: The disk_type_constraint of this NodeConstraint.
        :type disk_type_constraint: dict(str, str)
        """
        self._disk_type_constraint = disk_type_constraint

    @property
    def min_root_disk_size(self):
        r"""Gets the min_root_disk_size of this NodeConstraint.

        最小系统磁盘大小

        :return: The min_root_disk_size of this NodeConstraint.
        :rtype: int
        """
        return self._min_root_disk_size

    @min_root_disk_size.setter
    def min_root_disk_size(self, min_root_disk_size):
        r"""Sets the min_root_disk_size of this NodeConstraint.

        最小系统磁盘大小

        :param min_root_disk_size: The min_root_disk_size of this NodeConstraint.
        :type min_root_disk_size: int
        """
        self._min_root_disk_size = min_root_disk_size

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
        if not isinstance(other, NodeConstraint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
