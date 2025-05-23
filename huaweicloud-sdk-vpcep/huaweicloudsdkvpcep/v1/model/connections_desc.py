# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionsDesc:

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
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description'
    }

    def __init__(self, id=None, description=None):
        r"""ConnectionsDesc

        The model defined in huaweicloud sdk

        :param id: 终端节点ID，UUID格式字符
        :type id: str
        :param description: 描述字段，支持中英文字母、数字等字符，不支持“&lt;”或“&gt;”字符。
        :type description: str
        """
        
        

        self._id = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.description = description

    @property
    def id(self):
        r"""Gets the id of this ConnectionsDesc.

        终端节点ID，UUID格式字符

        :return: The id of this ConnectionsDesc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConnectionsDesc.

        终端节点ID，UUID格式字符

        :param id: The id of this ConnectionsDesc.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this ConnectionsDesc.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :return: The description of this ConnectionsDesc.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ConnectionsDesc.

        描述字段，支持中英文字母、数字等字符，不支持“<”或“>”字符。

        :param description: The description of this ConnectionsDesc.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ConnectionsDesc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
