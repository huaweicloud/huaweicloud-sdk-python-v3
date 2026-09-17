# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommentUpdateVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'at': 'str'
    }

    attribute_map = {
        'description': 'description',
        'at': 'at'
    }

    def __init__(self, description=None, at=None):
        r"""CommentUpdateVO

        The model defined in huaweicloud sdk

        :param description: **参数解释**： 评论内容，使用html标记语言。 **默认取值**： 不涉及。
        :type description: str
        :param at: **参数解释**： 评论时@他人的用户ID，填写此参数后会通知被@的用户，通知形式在需求管理-设置-工作项设置-通知设置中配置。 **默认取值**： 不涉及。
        :type at: str
        """
        
        

        self._description = None
        self._at = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if at is not None:
            self.at = at

    @property
    def description(self):
        r"""Gets the description of this CommentUpdateVO.

        **参数解释**： 评论内容，使用html标记语言。 **默认取值**： 不涉及。

        :return: The description of this CommentUpdateVO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CommentUpdateVO.

        **参数解释**： 评论内容，使用html标记语言。 **默认取值**： 不涉及。

        :param description: The description of this CommentUpdateVO.
        :type description: str
        """
        self._description = description

    @property
    def at(self):
        r"""Gets the at of this CommentUpdateVO.

        **参数解释**： 评论时@他人的用户ID，填写此参数后会通知被@的用户，通知形式在需求管理-设置-工作项设置-通知设置中配置。 **默认取值**： 不涉及。

        :return: The at of this CommentUpdateVO.
        :rtype: str
        """
        return self._at

    @at.setter
    def at(self, at):
        r"""Sets the at of this CommentUpdateVO.

        **参数解释**： 评论时@他人的用户ID，填写此参数后会通知被@的用户，通知形式在需求管理-设置-工作项设置-通知设置中配置。 **默认取值**： 不涉及。

        :param at: The at of this CommentUpdateVO.
        :type at: str
        """
        self._at = at

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
        if not isinstance(other, CommentUpdateVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
