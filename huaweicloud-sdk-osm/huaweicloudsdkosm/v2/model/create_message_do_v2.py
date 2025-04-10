# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMessageDoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content': 'str',
        'accessory_ids': 'list[str]'
    }

    attribute_map = {
        'content': 'content',
        'accessory_ids': 'accessory_ids'
    }

    def __init__(self, content=None, accessory_ids=None):
        r"""CreateMessageDoV2

        The model defined in huaweicloud sdk

        :param content: 留言内容
        :type content: str
        :param accessory_ids: 附件id
        :type accessory_ids: list[str]
        """
        
        

        self._content = None
        self._accessory_ids = None
        self.discriminator = None

        self.content = content
        if accessory_ids is not None:
            self.accessory_ids = accessory_ids

    @property
    def content(self):
        r"""Gets the content of this CreateMessageDoV2.

        留言内容

        :return: The content of this CreateMessageDoV2.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this CreateMessageDoV2.

        留言内容

        :param content: The content of this CreateMessageDoV2.
        :type content: str
        """
        self._content = content

    @property
    def accessory_ids(self):
        r"""Gets the accessory_ids of this CreateMessageDoV2.

        附件id

        :return: The accessory_ids of this CreateMessageDoV2.
        :rtype: list[str]
        """
        return self._accessory_ids

    @accessory_ids.setter
    def accessory_ids(self, accessory_ids):
        r"""Sets the accessory_ids of this CreateMessageDoV2.

        附件id

        :param accessory_ids: The accessory_ids of this CreateMessageDoV2.
        :type accessory_ids: list[str]
        """
        self._accessory_ids = accessory_ids

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
        if not isinstance(other, CreateMessageDoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
