# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReleaseStorageVOV5:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'used_capacity': 'str',
        'total_capacity': 'str',
        'used_capacity_size': 'int',
        'total_capacity_size': 'int',
        'package_type': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'used_capacity': 'used_capacity',
        'total_capacity': 'total_capacity',
        'used_capacity_size': 'used_capacity_size',
        'total_capacity_size': 'total_capacity_size',
        'package_type': 'package_type',
        'total_count': 'total_count'
    }

    def __init__(self, used_capacity=None, total_capacity=None, used_capacity_size=None, total_capacity_size=None, package_type=None, total_count=None):
        r"""ReleaseStorageVOV5

        The model defined in huaweicloud sdk

        :param used_capacity: **参数解释**: 已使用存储量 ---带单位。 **取值范围**: 不涉及。 
        :type used_capacity: str
        :param total_capacity: **参数解释**: 租户存储最大量 ---带单位。 **取值范围**: 不涉及。 
        :type total_capacity: str
        :param used_capacity_size: **参数解释**: 已使用存储量 ---字节。 **取值范围**: 不涉及。 
        :type used_capacity_size: int
        :param total_capacity_size: **参数解释**: 租户存储最大量 ---字节。 **取值范围**: 不涉及。 
        :type total_capacity_size: int
        :param package_type: **参数解释**: 包周期套餐类型(0.no_package 1.basic 2.professional 3.platinum)。 **取值范围**: 不涉及。 
        :type package_type: str
        :param total_count: **参数解释**: 项目仓库数量。 **取值范围**: 不涉及。 
        :type total_count: int
        """
        
        

        self._used_capacity = None
        self._total_capacity = None
        self._used_capacity_size = None
        self._total_capacity_size = None
        self._package_type = None
        self._total_count = None
        self.discriminator = None

        if used_capacity is not None:
            self.used_capacity = used_capacity
        if total_capacity is not None:
            self.total_capacity = total_capacity
        if used_capacity_size is not None:
            self.used_capacity_size = used_capacity_size
        if total_capacity_size is not None:
            self.total_capacity_size = total_capacity_size
        if package_type is not None:
            self.package_type = package_type
        if total_count is not None:
            self.total_count = total_count

    @property
    def used_capacity(self):
        r"""Gets the used_capacity of this ReleaseStorageVOV5.

        **参数解释**: 已使用存储量 ---带单位。 **取值范围**: 不涉及。 

        :return: The used_capacity of this ReleaseStorageVOV5.
        :rtype: str
        """
        return self._used_capacity

    @used_capacity.setter
    def used_capacity(self, used_capacity):
        r"""Sets the used_capacity of this ReleaseStorageVOV5.

        **参数解释**: 已使用存储量 ---带单位。 **取值范围**: 不涉及。 

        :param used_capacity: The used_capacity of this ReleaseStorageVOV5.
        :type used_capacity: str
        """
        self._used_capacity = used_capacity

    @property
    def total_capacity(self):
        r"""Gets the total_capacity of this ReleaseStorageVOV5.

        **参数解释**: 租户存储最大量 ---带单位。 **取值范围**: 不涉及。 

        :return: The total_capacity of this ReleaseStorageVOV5.
        :rtype: str
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        r"""Sets the total_capacity of this ReleaseStorageVOV5.

        **参数解释**: 租户存储最大量 ---带单位。 **取值范围**: 不涉及。 

        :param total_capacity: The total_capacity of this ReleaseStorageVOV5.
        :type total_capacity: str
        """
        self._total_capacity = total_capacity

    @property
    def used_capacity_size(self):
        r"""Gets the used_capacity_size of this ReleaseStorageVOV5.

        **参数解释**: 已使用存储量 ---字节。 **取值范围**: 不涉及。 

        :return: The used_capacity_size of this ReleaseStorageVOV5.
        :rtype: int
        """
        return self._used_capacity_size

    @used_capacity_size.setter
    def used_capacity_size(self, used_capacity_size):
        r"""Sets the used_capacity_size of this ReleaseStorageVOV5.

        **参数解释**: 已使用存储量 ---字节。 **取值范围**: 不涉及。 

        :param used_capacity_size: The used_capacity_size of this ReleaseStorageVOV5.
        :type used_capacity_size: int
        """
        self._used_capacity_size = used_capacity_size

    @property
    def total_capacity_size(self):
        r"""Gets the total_capacity_size of this ReleaseStorageVOV5.

        **参数解释**: 租户存储最大量 ---字节。 **取值范围**: 不涉及。 

        :return: The total_capacity_size of this ReleaseStorageVOV5.
        :rtype: int
        """
        return self._total_capacity_size

    @total_capacity_size.setter
    def total_capacity_size(self, total_capacity_size):
        r"""Sets the total_capacity_size of this ReleaseStorageVOV5.

        **参数解释**: 租户存储最大量 ---字节。 **取值范围**: 不涉及。 

        :param total_capacity_size: The total_capacity_size of this ReleaseStorageVOV5.
        :type total_capacity_size: int
        """
        self._total_capacity_size = total_capacity_size

    @property
    def package_type(self):
        r"""Gets the package_type of this ReleaseStorageVOV5.

        **参数解释**: 包周期套餐类型(0.no_package 1.basic 2.professional 3.platinum)。 **取值范围**: 不涉及。 

        :return: The package_type of this ReleaseStorageVOV5.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this ReleaseStorageVOV5.

        **参数解释**: 包周期套餐类型(0.no_package 1.basic 2.professional 3.platinum)。 **取值范围**: 不涉及。 

        :param package_type: The package_type of this ReleaseStorageVOV5.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def total_count(self):
        r"""Gets the total_count of this ReleaseStorageVOV5.

        **参数解释**: 项目仓库数量。 **取值范围**: 不涉及。 

        :return: The total_count of this ReleaseStorageVOV5.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ReleaseStorageVOV5.

        **参数解释**: 项目仓库数量。 **取值范围**: 不涉及。 

        :param total_count: The total_count of this ReleaseStorageVOV5.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReleaseStorageVOV5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
