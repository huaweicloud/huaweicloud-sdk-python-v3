# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpsDatasetItemsRequest:

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
        'version_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'dataset_id': 'dataset_id',
        'version_id': 'version_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, dataset_id=None, version_id=None, offset=None, limit=None):
        r"""ListOpsDatasetItemsRequest

        The model defined in huaweicloud sdk

        :param dataset_id: **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 
        :type dataset_id: str
        :param version_id: **参数解释：** 评测集的版本标识符（ID），用于指定查询特定历史版本下的数据条目。 **约束限制：** 字符串长度限制为0到100个字符。 **取值范围：** 有效的版本ID字符串。 **默认取值：** 若为空，默认指向当前的草稿版本（Draft）。
        :type version_id: str
        :param offset: **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 
        :type offset: int
        :param limit: **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 
        :type limit: int
        """
        
        

        self._dataset_id = None
        self._version_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.dataset_id = dataset_id
        if version_id is not None:
            self.version_id = version_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def dataset_id(self):
        r"""Gets the dataset_id of this ListOpsDatasetItemsRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :return: The dataset_id of this ListOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        r"""Sets the dataset_id of this ListOpsDatasetItemsRequest.

        **参数解释：** 评测集的唯一标识符（ID） **约束限制：** 由英文、数字、“-”、“_”组成，长度为1到64个字符。 **取值范围：** 由英文、数字、连字符(-)、下划线(_)组成的1-64位字符串。 **默认取值：** 无。 

        :param dataset_id: The dataset_id of this ListOpsDatasetItemsRequest.
        :type dataset_id: str
        """
        self._dataset_id = dataset_id

    @property
    def version_id(self):
        r"""Gets the version_id of this ListOpsDatasetItemsRequest.

        **参数解释：** 评测集的版本标识符（ID），用于指定查询特定历史版本下的数据条目。 **约束限制：** 字符串长度限制为0到100个字符。 **取值范围：** 有效的版本ID字符串。 **默认取值：** 若为空，默认指向当前的草稿版本（Draft）。

        :return: The version_id of this ListOpsDatasetItemsRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this ListOpsDatasetItemsRequest.

        **参数解释：** 评测集的版本标识符（ID），用于指定查询特定历史版本下的数据条目。 **约束限制：** 字符串长度限制为0到100个字符。 **取值范围：** 有效的版本ID字符串。 **默认取值：** 若为空，默认指向当前的草稿版本（Draft）。

        :param version_id: The version_id of this ListOpsDatasetItemsRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def offset(self):
        r"""Gets the offset of this ListOpsDatasetItemsRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :return: The offset of this ListOpsDatasetItemsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOpsDatasetItemsRequest.

        **参数解释：** 分页查询的起始偏移量。用于指定从满足条件的第几条记录开始返回，常与 limit参数配合实现分页功能。 **约束限制：** 必须为整数，且大小在0到10,000之间。 **取值范围：** 0-10000。 **默认取值：** 0。 

        :param offset: The offset of this ListOpsDatasetItemsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListOpsDatasetItemsRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :return: The limit of this ListOpsDatasetItemsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOpsDatasetItemsRequest.

        **参数解释：** 单次查询返回的最大记录数量。用于控制分页查询时每页显示的数据条数。 **约束限制：** 必须为整数，且大小在1到100之间。 **取值范围：** 1-100。 **默认取值：** 10。 

        :param limit: The limit of this ListOpsDatasetItemsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListOpsDatasetItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
