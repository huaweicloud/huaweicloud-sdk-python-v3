# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsDatasetItemResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'turns': 'list[OpsTurn]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'turns': 'turns',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, turns=None, created_at=None, updated_at=None):
        r"""ShowOpsDatasetItemResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 数据条目的唯一标识符。 **取值范围：** 通常为符合 MongoDB ObjectID 规范的 24 位十六进制字符串。
        :type id: str
        :param turns: **参数解释：** 包含该条目具体业务内容的轮次数据列表，支持多轮对话格式。 **取值范围：** 符合OpsTurn定义的对象数组。
        :type turns: list[:class:`huaweicloudsdkagentarts.v1.OpsTurn`]
        :param created_at: **参数解释：** 该条目被首次创建的时间。 **取值范围：** UTC 时间字符串。
        :type created_at: datetime
        :param updated_at: **参数解释：** 该条目最后一次被修改的时间。 **取值范围：** UTC 时间字符串。
        :type updated_at: datetime
        """
        
        super().__init__()

        self._id = None
        self._turns = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if turns is not None:
            self.turns = turns
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ShowOpsDatasetItemResponse.

        **参数解释：** 数据条目的唯一标识符。 **取值范围：** 通常为符合 MongoDB ObjectID 规范的 24 位十六进制字符串。

        :return: The id of this ShowOpsDatasetItemResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowOpsDatasetItemResponse.

        **参数解释：** 数据条目的唯一标识符。 **取值范围：** 通常为符合 MongoDB ObjectID 规范的 24 位十六进制字符串。

        :param id: The id of this ShowOpsDatasetItemResponse.
        :type id: str
        """
        self._id = id

    @property
    def turns(self):
        r"""Gets the turns of this ShowOpsDatasetItemResponse.

        **参数解释：** 包含该条目具体业务内容的轮次数据列表，支持多轮对话格式。 **取值范围：** 符合OpsTurn定义的对象数组。

        :return: The turns of this ShowOpsDatasetItemResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTurn`]
        """
        return self._turns

    @turns.setter
    def turns(self, turns):
        r"""Sets the turns of this ShowOpsDatasetItemResponse.

        **参数解释：** 包含该条目具体业务内容的轮次数据列表，支持多轮对话格式。 **取值范围：** 符合OpsTurn定义的对象数组。

        :param turns: The turns of this ShowOpsDatasetItemResponse.
        :type turns: list[:class:`huaweicloudsdkagentarts.v1.OpsTurn`]
        """
        self._turns = turns

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowOpsDatasetItemResponse.

        **参数解释：** 该条目被首次创建的时间。 **取值范围：** UTC 时间字符串。

        :return: The created_at of this ShowOpsDatasetItemResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowOpsDatasetItemResponse.

        **参数解释：** 该条目被首次创建的时间。 **取值范围：** UTC 时间字符串。

        :param created_at: The created_at of this ShowOpsDatasetItemResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowOpsDatasetItemResponse.

        **参数解释：** 该条目最后一次被修改的时间。 **取值范围：** UTC 时间字符串。

        :return: The updated_at of this ShowOpsDatasetItemResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowOpsDatasetItemResponse.

        **参数解释：** 该条目最后一次被修改的时间。 **取值范围：** UTC 时间字符串。

        :param updated_at: The updated_at of this ShowOpsDatasetItemResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsDatasetItemResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowOpsDatasetItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
