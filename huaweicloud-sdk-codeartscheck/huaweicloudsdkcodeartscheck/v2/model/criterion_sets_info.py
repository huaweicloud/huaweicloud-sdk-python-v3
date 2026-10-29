# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CriterionSetsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'criterion_set_list': 'list[CriterionSetListV2Body]',
        'total': 'int'
    }

    attribute_map = {
        'criterion_set_list': 'criterionSetList',
        'total': 'total'
    }

    def __init__(self, criterion_set_list=None, total=None):
        r"""CriterionSetsInfo

        The model defined in huaweicloud sdk

        :param criterion_set_list: **参数解释：** 规则列表。 **取值范围：** 不涉及。
        :type criterion_set_list: list[:class:`huaweicloudsdkcodeartscheck.v2.CriterionSetListV2Body`]
        :param total: **参数解释：** 规则总数。 **取值范围：** ≥0
        :type total: int
        """
        
        

        self._criterion_set_list = None
        self._total = None
        self.discriminator = None

        if criterion_set_list is not None:
            self.criterion_set_list = criterion_set_list
        if total is not None:
            self.total = total

    @property
    def criterion_set_list(self):
        r"""Gets the criterion_set_list of this CriterionSetsInfo.

        **参数解释：** 规则列表。 **取值范围：** 不涉及。

        :return: The criterion_set_list of this CriterionSetsInfo.
        :rtype: list[:class:`huaweicloudsdkcodeartscheck.v2.CriterionSetListV2Body`]
        """
        return self._criterion_set_list

    @criterion_set_list.setter
    def criterion_set_list(self, criterion_set_list):
        r"""Sets the criterion_set_list of this CriterionSetsInfo.

        **参数解释：** 规则列表。 **取值范围：** 不涉及。

        :param criterion_set_list: The criterion_set_list of this CriterionSetsInfo.
        :type criterion_set_list: list[:class:`huaweicloudsdkcodeartscheck.v2.CriterionSetListV2Body`]
        """
        self._criterion_set_list = criterion_set_list

    @property
    def total(self):
        r"""Gets the total of this CriterionSetsInfo.

        **参数解释：** 规则总数。 **取值范围：** ≥0

        :return: The total of this CriterionSetsInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this CriterionSetsInfo.

        **参数解释：** 规则总数。 **取值范围：** ≥0

        :param total: The total of this CriterionSetsInfo.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, CriterionSetsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
