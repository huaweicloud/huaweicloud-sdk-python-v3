# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComputeFlavorGroupDetail:

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
        'compute_flavors': 'list[ComputeFlavorItemDetail]'
    }

    attribute_map = {
        'group_type': 'group_type',
        'compute_flavors': 'compute_flavors'
    }

    def __init__(self, group_type=None, compute_flavors=None):
        r"""ComputeFlavorGroupDetail

        The model defined in huaweicloud sdk

        :param group_type: **参数解释**: 性能规格。 **取值范围**: - normal：独享型（1:8）。 - normal2：独享型（1:4）。 - armFlavors：鲲鹏独享型（1:8）。 - exclusive：独享型（1:4），仅基础版集中式实例支持。 - armExclusive：鲲鹏独享型（1:4），仅基础版集中式实例支持。 - economical：惠选型（1:4）。 - economical2：惠选型（1:8）。 - armFlavors2：鲲鹏独享型（1:4）。 - general：通用型（1:4）。
        :type group_type: str
        :param compute_flavors: **参数解释**: 计算规格列表。 **取值范围**: 不涉及。
        :type compute_flavors: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ComputeFlavorItemDetail`]
        """
        
        

        self._group_type = None
        self._compute_flavors = None
        self.discriminator = None

        if group_type is not None:
            self.group_type = group_type
        if compute_flavors is not None:
            self.compute_flavors = compute_flavors

    @property
    def group_type(self):
        r"""Gets the group_type of this ComputeFlavorGroupDetail.

        **参数解释**: 性能规格。 **取值范围**: - normal：独享型（1:8）。 - normal2：独享型（1:4）。 - armFlavors：鲲鹏独享型（1:8）。 - exclusive：独享型（1:4），仅基础版集中式实例支持。 - armExclusive：鲲鹏独享型（1:4），仅基础版集中式实例支持。 - economical：惠选型（1:4）。 - economical2：惠选型（1:8）。 - armFlavors2：鲲鹏独享型（1:4）。 - general：通用型（1:4）。

        :return: The group_type of this ComputeFlavorGroupDetail.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this ComputeFlavorGroupDetail.

        **参数解释**: 性能规格。 **取值范围**: - normal：独享型（1:8）。 - normal2：独享型（1:4）。 - armFlavors：鲲鹏独享型（1:8）。 - exclusive：独享型（1:4），仅基础版集中式实例支持。 - armExclusive：鲲鹏独享型（1:4），仅基础版集中式实例支持。 - economical：惠选型（1:4）。 - economical2：惠选型（1:8）。 - armFlavors2：鲲鹏独享型（1:4）。 - general：通用型（1:4）。

        :param group_type: The group_type of this ComputeFlavorGroupDetail.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def compute_flavors(self):
        r"""Gets the compute_flavors of this ComputeFlavorGroupDetail.

        **参数解释**: 计算规格列表。 **取值范围**: 不涉及。

        :return: The compute_flavors of this ComputeFlavorGroupDetail.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ComputeFlavorItemDetail`]
        """
        return self._compute_flavors

    @compute_flavors.setter
    def compute_flavors(self, compute_flavors):
        r"""Sets the compute_flavors of this ComputeFlavorGroupDetail.

        **参数解释**: 计算规格列表。 **取值范围**: 不涉及。

        :param compute_flavors: The compute_flavors of this ComputeFlavorGroupDetail.
        :type compute_flavors: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ComputeFlavorItemDetail`]
        """
        self._compute_flavors = compute_flavors

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
        if not isinstance(other, ComputeFlavorGroupDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
