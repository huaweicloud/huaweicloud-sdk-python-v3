# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchOperateInfo:

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
        'modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'modified_by': 'modified_by'
    }

    def __init__(self, id=None, modified_by=None):
        r"""BatchOperateInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 发布/迭代计划ID。 **取值范围**： 长度为18~19个字符的数字字符串。
        :type id: str
        :param modified_by: **参数解释**： 最近更新人ID。 **取值范围**： 不涉及。
        :type modified_by: str
        """
        
        

        self._id = None
        self._modified_by = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if modified_by is not None:
            self.modified_by = modified_by

    @property
    def id(self):
        r"""Gets the id of this BatchOperateInfo.

        **参数解释**： 发布/迭代计划ID。 **取值范围**： 长度为18~19个字符的数字字符串。

        :return: The id of this BatchOperateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchOperateInfo.

        **参数解释**： 发布/迭代计划ID。 **取值范围**： 长度为18~19个字符的数字字符串。

        :param id: The id of this BatchOperateInfo.
        :type id: str
        """
        self._id = id

    @property
    def modified_by(self):
        r"""Gets the modified_by of this BatchOperateInfo.

        **参数解释**： 最近更新人ID。 **取值范围**： 不涉及。

        :return: The modified_by of this BatchOperateInfo.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this BatchOperateInfo.

        **参数解释**： 最近更新人ID。 **取值范围**： 不涉及。

        :param modified_by: The modified_by of this BatchOperateInfo.
        :type modified_by: str
        """
        self._modified_by = modified_by

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
        if not isinstance(other, BatchOperateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
