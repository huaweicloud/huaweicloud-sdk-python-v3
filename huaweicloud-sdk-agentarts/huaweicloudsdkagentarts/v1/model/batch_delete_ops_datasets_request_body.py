# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteOpsDatasetsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_ids': 'list[str]'
    }

    attribute_map = {
        'dataset_ids': 'dataset_ids'
    }

    def __init__(self, dataset_ids=None):
        r"""BatchDeleteOpsDatasetsRequestBody

        The model defined in huaweicloud sdk

        :param dataset_ids: **参数解释：** 待删除的评测集ID集合。 **约束限制：** 数组元素数量为1-1000个；单个ID长度不超过100字符。 **取值范围：** 由有效的评测集唯一标识符组成的列表。 **默认取值：** 不涉及。 
        :type dataset_ids: list[str]
        """
        
        

        self._dataset_ids = None
        self.discriminator = None

        self.dataset_ids = dataset_ids

    @property
    def dataset_ids(self):
        r"""Gets the dataset_ids of this BatchDeleteOpsDatasetsRequestBody.

        **参数解释：** 待删除的评测集ID集合。 **约束限制：** 数组元素数量为1-1000个；单个ID长度不超过100字符。 **取值范围：** 由有效的评测集唯一标识符组成的列表。 **默认取值：** 不涉及。 

        :return: The dataset_ids of this BatchDeleteOpsDatasetsRequestBody.
        :rtype: list[str]
        """
        return self._dataset_ids

    @dataset_ids.setter
    def dataset_ids(self, dataset_ids):
        r"""Sets the dataset_ids of this BatchDeleteOpsDatasetsRequestBody.

        **参数解释：** 待删除的评测集ID集合。 **约束限制：** 数组元素数量为1-1000个；单个ID长度不超过100字符。 **取值范围：** 由有效的评测集唯一标识符组成的列表。 **默认取值：** 不涉及。 

        :param dataset_ids: The dataset_ids of this BatchDeleteOpsDatasetsRequestBody.
        :type dataset_ids: list[str]
        """
        self._dataset_ids = dataset_ids

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
        if not isinstance(other, BatchDeleteOpsDatasetsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
