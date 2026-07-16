# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateOpsDatasetItemsRequest:

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
        'source_version_id': 'str',
        'overwrite': 'bool',
        'body': 'BatchCreateOpsDatasetItemsRequestBody'
    }

    attribute_map = {
        'dataset_id': 'dataset_id',
        'source_version_id': 'source_version_id',
        'overwrite': 'overwrite',
        'body': 'body'
    }

    def __init__(self, dataset_id=None, source_version_id=None, overwrite=None, body=None):
        r"""BatchCreateOpsDatasetItemsRequest

        The model defined in huaweicloud sdk

        :param dataset_id: **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 
        :type dataset_id: str
        :param source_version_id: **参数解释：** 源版本ID。在执行版本还原或基于特定版本批量添加数据的场景下，指定作为数据来源的历史版本标识。 **约束限制：** 长度为0到100个字符。 **取值范围：** 有效的版本ID字符串。 **默认取值：** 不涉及。
        :type source_version_id: str
        :param overwrite: **参数解释：** 覆盖模式开关。用于控制在批量添加新条目之前，是否清空目标评测集（通常为草稿版）中的现有数据。 **约束限制：** 不涉及。 **取值范围：** - &#x60;true&#x60;: 覆盖模式，先清空后添加。 - &#x60;false&#x60;: 追加模式，在现有数据基础上新增。 **默认取值：** false。
        :type overwrite: bool
        :param body: Body of the BatchCreateOpsDatasetItemsRequest
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsDatasetItemsRequestBody`
        """
        
        

        self._dataset_id = None
        self._source_version_id = None
        self._overwrite = None
        self._body = None
        self.discriminator = None

        self.dataset_id = dataset_id
        if source_version_id is not None:
            self.source_version_id = source_version_id
        if overwrite is not None:
            self.overwrite = overwrite
        if body is not None:
            self.body = body

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this BatchCreateOpsDatasetItemsRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :return: The dataset_id of this BatchCreateOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this BatchCreateOpsDatasetItemsRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :param dataset_id: The dataset_id of this BatchCreateOpsDatasetItemsRequest.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def source_version_id(self):
        r"""Gets the source_version_id of this BatchCreateOpsDatasetItemsRequest.

        **参数解释：** 源版本ID。在执行版本还原或基于特定版本批量添加数据的场景下，指定作为数据来源的历史版本标识。 **约束限制：** 长度为0到100个字符。 **取值范围：** 有效的版本ID字符串。 **默认取值：** 不涉及。

        :return: The source_version_id of this BatchCreateOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._source_version_id

    @source_version_id.setter
    def source_version_id(self, source_version_id):
        r"""Sets the source_version_id of this BatchCreateOpsDatasetItemsRequest.

        **参数解释：** 源版本ID。在执行版本还原或基于特定版本批量添加数据的场景下，指定作为数据来源的历史版本标识。 **约束限制：** 长度为0到100个字符。 **取值范围：** 有效的版本ID字符串。 **默认取值：** 不涉及。

        :param source_version_id: The source_version_id of this BatchCreateOpsDatasetItemsRequest.
        :type source_version_id: str
        """
        self._source_version_id = source_version_id

    @property
    def overwrite(self):
        r"""Gets the overwrite of this BatchCreateOpsDatasetItemsRequest.

        **参数解释：** 覆盖模式开关。用于控制在批量添加新条目之前，是否清空目标评测集（通常为草稿版）中的现有数据。 **约束限制：** 不涉及。 **取值范围：** - `true`: 覆盖模式，先清空后添加。 - `false`: 追加模式，在现有数据基础上新增。 **默认取值：** false。

        :return: The overwrite of this BatchCreateOpsDatasetItemsRequest.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        r"""Sets the overwrite of this BatchCreateOpsDatasetItemsRequest.

        **参数解释：** 覆盖模式开关。用于控制在批量添加新条目之前，是否清空目标评测集（通常为草稿版）中的现有数据。 **约束限制：** 不涉及。 **取值范围：** - `true`: 覆盖模式，先清空后添加。 - `false`: 追加模式，在现有数据基础上新增。 **默认取值：** false。

        :param overwrite: The overwrite of this BatchCreateOpsDatasetItemsRequest.
        :type overwrite: bool
        """
        self._overwrite = overwrite

    @property
    def body(self):
        r"""Gets the body of this BatchCreateOpsDatasetItemsRequest.

        :return: The body of this BatchCreateOpsDatasetItemsRequest.
        :rtype: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsDatasetItemsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateOpsDatasetItemsRequest.

        :param body: The body of this BatchCreateOpsDatasetItemsRequest.
        :type body: :class:`huaweicloudsdkagentarts.v1.BatchCreateOpsDatasetItemsRequestBody`
        """
        self._body = body

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
        if not isinstance(other, BatchCreateOpsDatasetItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
