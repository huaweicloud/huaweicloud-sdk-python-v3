# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTempApiKeyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expire_time': 'int',
        'workspace_id': 'str'
    }

    attribute_map = {
        'expire_time': 'expire_time',
        'workspace_id': 'workspace_id'
    }

    def __init__(self, expire_time=None, workspace_id=None):
        r"""CreateTempApiKeyReq

        The model defined in huaweicloud sdk

        :param expire_time: **参数解释：** 过期时间。 **约束限制：** 不能是小数。 **取值范围：** 最少1小时，最多24小时。 **默认取值：** 不涉及。
        :type expire_time: int
        :param workspace_id: **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及
        :type workspace_id: str
        """
        
        

        self._expire_time = None
        self._workspace_id = None
        self.discriminator = None

        if expire_time is not None:
            self.expire_time = expire_time
        if workspace_id is not None:
            self.workspace_id = workspace_id

    @property
    def expire_time(self):
        r"""Gets the expire_time of this CreateTempApiKeyReq.

        **参数解释：** 过期时间。 **约束限制：** 不能是小数。 **取值范围：** 最少1小时，最多24小时。 **默认取值：** 不涉及。

        :return: The expire_time of this CreateTempApiKeyReq.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this CreateTempApiKeyReq.

        **参数解释：** 过期时间。 **约束限制：** 不能是小数。 **取值范围：** 最少1小时，最多24小时。 **默认取值：** 不涉及。

        :param expire_time: The expire_time of this CreateTempApiKeyReq.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreateTempApiKeyReq.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及

        :return: The workspace_id of this CreateTempApiKeyReq.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreateTempApiKeyReq.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc)未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及

        :param workspace_id: The workspace_id of this CreateTempApiKeyReq.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

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
        if not isinstance(other, CreateTempApiKeyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
