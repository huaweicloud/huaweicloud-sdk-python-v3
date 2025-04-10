# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeFlavorGroup:

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
        'compute_flavors': 'list[ComputeFlavor]'
    }

    attribute_map = {
        'group_type': 'group_type',
        'compute_flavors': 'compute_flavors'
    }

    def __init__(self, group_type=None, compute_flavors=None):
        r"""ComputeFlavorGroup

        The model defined in huaweicloud sdk

        :param group_type: 性能规格，包含以下状态：  normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于PostgreSQL引擎：独享型
        :type group_type: str
        :param compute_flavors: 计算规格列表
        :type compute_flavors: list[:class:`huaweicloudsdkrds.v3.ComputeFlavor`]
        """
        
        

        self._group_type = None
        self._compute_flavors = None
        self.discriminator = None

        self.group_type = group_type
        self.compute_flavors = compute_flavors

    @property
    def group_type(self):
        r"""Gets the group_type of this ComputeFlavorGroup.

        性能规格，包含以下状态：  normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于PostgreSQL引擎：独享型

        :return: The group_type of this ComputeFlavorGroup.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this ComputeFlavorGroup.

        性能规格，包含以下状态：  normal：通用增强型。 normal2：通用增强Ⅱ型。 armFlavors：鲲鹏通用增强型。 dedicicateNormal（dedicatedNormalLocalssd）：x86独享型。 armLocalssd：鲲鹏通用型。 normalLocalssd：x86通用型。 general：通用型。 dedicated 对于PostgreSQL引擎：独享型

        :param group_type: The group_type of this ComputeFlavorGroup.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def compute_flavors(self):
        r"""Gets the compute_flavors of this ComputeFlavorGroup.

        计算规格列表

        :return: The compute_flavors of this ComputeFlavorGroup.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ComputeFlavor`]
        """
        return self._compute_flavors

    @compute_flavors.setter
    def compute_flavors(self, compute_flavors):
        r"""Sets the compute_flavors of this ComputeFlavorGroup.

        计算规格列表

        :param compute_flavors: The compute_flavors of this ComputeFlavorGroup.
        :type compute_flavors: list[:class:`huaweicloudsdkrds.v3.ComputeFlavor`]
        """
        self._compute_flavors = compute_flavors

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
        if not isinstance(other, ComputeFlavorGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
