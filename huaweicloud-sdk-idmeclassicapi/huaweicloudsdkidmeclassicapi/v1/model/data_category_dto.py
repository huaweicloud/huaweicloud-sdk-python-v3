# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataCategoryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categoryable': 'ObjectReferenceParamDTO',
        'category': 'ObjectReferenceParamDTO',
        'modifier': 'str'
    }

    attribute_map = {
        'categoryable': 'categoryable',
        'category': 'category',
        'modifier': 'modifier'
    }

    def __init__(self, categoryable=None, category=None, modifier=None):
        r"""DataCategoryDTO

        The model defined in huaweicloud sdk

        :param categoryable: 
        :type categoryable: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param category: 
        :type category: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        :param modifier: **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。
        :type modifier: str
        """
        
        

        self._categoryable = None
        self._category = None
        self._modifier = None
        self.discriminator = None

        if categoryable is not None:
            self.categoryable = categoryable
        if category is not None:
            self.category = category
        if modifier is not None:
            self.modifier = modifier

    @property
    def categoryable(self):
        r"""Gets the categoryable of this DataCategoryDTO.

        :return: The categoryable of this DataCategoryDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._categoryable

    @categoryable.setter
    def categoryable(self, categoryable):
        r"""Sets the categoryable of this DataCategoryDTO.

        :param categoryable: The categoryable of this DataCategoryDTO.
        :type categoryable: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._categoryable = categoryable

    @property
    def category(self):
        r"""Gets the category of this DataCategoryDTO.

        :return: The category of this DataCategoryDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this DataCategoryDTO.

        :param category: The category of this DataCategoryDTO.
        :type category: :class:`huaweicloudsdkidmeclassicapi.v1.ObjectReferenceParamDTO`
        """
        self._category = category

    @property
    def modifier(self):
        r"""Gets the modifier of this DataCategoryDTO.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :return: The modifier of this DataCategoryDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        r"""Sets the modifier of this DataCategoryDTO.

        **参数解释：**  修改人。  **约束限制：**  不涉及。  **取值范围：**  不涉及。  **默认取值：**  不涉及。

        :param modifier: The modifier of this DataCategoryDTO.
        :type modifier: str
        """
        self._modifier = modifier

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
        if not isinstance(other, DataCategoryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
