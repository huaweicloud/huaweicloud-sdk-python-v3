# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListChatResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'chats': 'list[ChatRsp]',
        'count': 'int'
    }

    attribute_map = {
        'chats': 'chats',
        'count': 'count'
    }

    def __init__(self, chats=None, count=None):
        r"""ListChatResponse

        The model defined in huaweicloud sdk

        :param chats: **参数解释**： 对话列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type chats: list[:class:`huaweicloudsdkeihealth.v1.ChatRsp`]
        :param count: **参数解释**： 对话个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type count: int
        """
        
        super(ListChatResponse, self).__init__()

        self._chats = None
        self._count = None
        self.discriminator = None

        if chats is not None:
            self.chats = chats
        if count is not None:
            self.count = count

    @property
    def chats(self):
        r"""Gets the chats of this ListChatResponse.

        **参数解释**： 对话列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The chats of this ListChatResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.ChatRsp`]
        """
        return self._chats

    @chats.setter
    def chats(self, chats):
        r"""Sets the chats of this ListChatResponse.

        **参数解释**： 对话列表。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param chats: The chats of this ListChatResponse.
        :type chats: list[:class:`huaweicloudsdkeihealth.v1.ChatRsp`]
        """
        self._chats = chats

    @property
    def count(self):
        r"""Gets the count of this ListChatResponse.

        **参数解释**： 对话个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The count of this ListChatResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListChatResponse.

        **参数解释**： 对话个数。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param count: The count of this ListChatResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListChatResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
