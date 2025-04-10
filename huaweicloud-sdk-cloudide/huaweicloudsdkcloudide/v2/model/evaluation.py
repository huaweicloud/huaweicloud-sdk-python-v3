# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Evaluation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_id': 'str',
        'text': 'str'
    }

    attribute_map = {
        'extension_id': 'extension_id',
        'text': 'text'
    }

    def __init__(self, extension_id=None, text=None):
        r"""Evaluation

        The model defined in huaweicloud sdk

        :param extension_id: 插件id
        :type extension_id: str
        :param text: 评论内容
        :type text: str
        """
        
        

        self._extension_id = None
        self._text = None
        self.discriminator = None

        self.extension_id = extension_id
        self.text = text

    @property
    def extension_id(self):
        r"""Gets the extension_id of this Evaluation.

        插件id

        :return: The extension_id of this Evaluation.
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        r"""Sets the extension_id of this Evaluation.

        插件id

        :param extension_id: The extension_id of this Evaluation.
        :type extension_id: str
        """
        self._extension_id = extension_id

    @property
    def text(self):
        r"""Gets the text of this Evaluation.

        评论内容

        :return: The text of this Evaluation.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this Evaluation.

        评论内容

        :param text: The text of this Evaluation.
        :type text: str
        """
        self._text = text

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
        if not isinstance(other, Evaluation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
