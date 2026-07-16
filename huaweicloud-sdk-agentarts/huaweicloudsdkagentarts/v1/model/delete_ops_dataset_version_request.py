# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteOpsDatasetVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataset_id': 'str',
        'version_id': 'str'
    }

    attribute_map = {
        'dataset_id': 'dataset_id',
        'version_id': 'version_id'
    }

    def __init__(self, dataset_id=None, version_id=None):
        r"""DeleteOpsDatasetVersionRequest

        The model defined in huaweicloud sdk

        :param dataset_id: **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 
        :type dataset_id: str
        :param version_id: **参数解释：** 待删除的历史版本唯一标识符（ID）。该参数用于在路径中精确定位并移除评测集中特定的历史版本记录。 **约束限制：** 固定长度为36字符的 UUID格式。需确保该版本已存在且非当前草稿状态。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。
        :type version_id: str
        """
        
        

        self._dataset_id = None
        self._version_id = None
        self.discriminator = None

        self.dataset_id = dataset_id
        self.version_id = version_id

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this DeleteOpsDatasetVersionRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :return: The dataset_id of this DeleteOpsDatasetVersionRequest.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this DeleteOpsDatasetVersionRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :param dataset_id: The dataset_id of this DeleteOpsDatasetVersionRequest.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def version_id(self):
        r"""Gets the version_id of this DeleteOpsDatasetVersionRequest.

        **参数解释：** 待删除的历史版本唯一标识符（ID）。该参数用于在路径中精确定位并移除评测集中特定的历史版本记录。 **约束限制：** 固定长度为36字符的 UUID格式。需确保该版本已存在且非当前草稿状态。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :return: The version_id of this DeleteOpsDatasetVersionRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this DeleteOpsDatasetVersionRequest.

        **参数解释：** 待删除的历史版本唯一标识符（ID）。该参数用于在路径中精确定位并移除评测集中特定的历史版本记录。 **约束限制：** 固定长度为36字符的 UUID格式。需确保该版本已存在且非当前草稿状态。 **取值范围：** 符合通用唯一识别码(UUID)标准的字符串。 **默认取值：** 不涉及。

        :param version_id: The version_id of this DeleteOpsDatasetVersionRequest.
        :type version_id: str
        """
        self._version_id = version_id

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
        if not isinstance(other, DeleteOpsDatasetVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
