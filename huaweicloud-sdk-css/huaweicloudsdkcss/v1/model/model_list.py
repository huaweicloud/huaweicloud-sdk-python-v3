# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_size': 'int',
        'models': 'list[Model]'
    }

    attribute_map = {
        'total_size': 'totalSize',
        'models': 'models'
    }

    def __init__(self, total_size=None, models=None):
        r"""ModelList

        The model defined in huaweicloud sdk

        :param total_size: **参数解释**： 模型数量 **取值范围**： 不涉及
        :type total_size: int
        :param models: **参数解释**： 模型列表 **取值范围**： 不涉及
        :type models: list[:class:`huaweicloudsdkcss.v1.Model`]
        """
        
        

        self._total_size = None
        self._models = None
        self.discriminator = None

        if total_size is not None:
            self.total_size = total_size
        if models is not None:
            self.models = models

    @property
    def total_size(self):
        r"""Gets the total_size of this ModelList.

        **参数解释**： 模型数量 **取值范围**： 不涉及

        :return: The total_size of this ModelList.
        :rtype: int
        """
        return self._total_size

    @total_size.setter
    def total_size(self, total_size):
        r"""Sets the total_size of this ModelList.

        **参数解释**： 模型数量 **取值范围**： 不涉及

        :param total_size: The total_size of this ModelList.
        :type total_size: int
        """
        self._total_size = total_size

    @property
    def models(self):
        r"""Gets the models of this ModelList.

        **参数解释**： 模型列表 **取值范围**： 不涉及

        :return: The models of this ModelList.
        :rtype: list[:class:`huaweicloudsdkcss.v1.Model`]
        """
        return self._models

    @models.setter
    def models(self, models):
        r"""Sets the models of this ModelList.

        **参数解释**： 模型列表 **取值范围**： 不涉及

        :param models: The models of this ModelList.
        :type models: list[:class:`huaweicloudsdkcss.v1.Model`]
        """
        self._models = models

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
        if not isinstance(other, ModelList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
