# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeFlavorGroupsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_type': 'str',
        'compute_flavors': 'list[ComputeFlavors]',
        'offset': 'int',
        'limit': 'int',
        'total': 'int'
    }

    attribute_map = {
        'group_type': 'groupType',
        'compute_flavors': 'computeFlavors',
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, group_type=None, compute_flavors=None, offset=None, limit=None, total=None):
        """ComputeFlavorGroupsInfo

        The model defined in huaweicloud sdk

        :param group_type: 计算资源架构类型，目前分X86和ARM两种。
        :type group_type: str
        :param compute_flavors: 计算类型规格详情。
        :type compute_flavors: list[:class:`huaweicloudsdkddm.v1.ComputeFlavors`]
        :param offset: 分页参数: 起始值。
        :type offset: int
        :param limit: 分页参数：每页多少条。
        :type limit: int
        :param total: 计算类型规格总数。
        :type total: int
        """
        
        

        self._group_type = None
        self._compute_flavors = None
        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if group_type is not None:
            self.group_type = group_type
        if compute_flavors is not None:
            self.compute_flavors = compute_flavors
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def group_type(self):
        """Gets the group_type of this ComputeFlavorGroupsInfo.

        计算资源架构类型，目前分X86和ARM两种。

        :return: The group_type of this ComputeFlavorGroupsInfo.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        """Sets the group_type of this ComputeFlavorGroupsInfo.

        计算资源架构类型，目前分X86和ARM两种。

        :param group_type: The group_type of this ComputeFlavorGroupsInfo.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def compute_flavors(self):
        """Gets the compute_flavors of this ComputeFlavorGroupsInfo.

        计算类型规格详情。

        :return: The compute_flavors of this ComputeFlavorGroupsInfo.
        :rtype: list[:class:`huaweicloudsdkddm.v1.ComputeFlavors`]
        """
        return self._compute_flavors

    @compute_flavors.setter
    def compute_flavors(self, compute_flavors):
        """Sets the compute_flavors of this ComputeFlavorGroupsInfo.

        计算类型规格详情。

        :param compute_flavors: The compute_flavors of this ComputeFlavorGroupsInfo.
        :type compute_flavors: list[:class:`huaweicloudsdkddm.v1.ComputeFlavors`]
        """
        self._compute_flavors = compute_flavors

    @property
    def offset(self):
        """Gets the offset of this ComputeFlavorGroupsInfo.

        分页参数: 起始值。

        :return: The offset of this ComputeFlavorGroupsInfo.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ComputeFlavorGroupsInfo.

        分页参数: 起始值。

        :param offset: The offset of this ComputeFlavorGroupsInfo.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ComputeFlavorGroupsInfo.

        分页参数：每页多少条。

        :return: The limit of this ComputeFlavorGroupsInfo.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ComputeFlavorGroupsInfo.

        分页参数：每页多少条。

        :param limit: The limit of this ComputeFlavorGroupsInfo.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this ComputeFlavorGroupsInfo.

        计算类型规格总数。

        :return: The total of this ComputeFlavorGroupsInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ComputeFlavorGroupsInfo.

        计算类型规格总数。

        :param total: The total of this ComputeFlavorGroupsInfo.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ComputeFlavorGroupsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
