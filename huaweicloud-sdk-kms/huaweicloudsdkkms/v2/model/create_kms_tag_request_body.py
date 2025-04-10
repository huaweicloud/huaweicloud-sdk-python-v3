# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKmsTagRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag': 'TagItem',
        'sequence': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'sequence': 'sequence'
    }

    def __init__(self, tag=None, sequence=None):
        r"""CreateKmsTagRequestBody

        The model defined in huaweicloud sdk

        :param tag: 
        :type tag: :class:`huaweicloudsdkkms.v2.TagItem`
        :param sequence: 请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff
        :type sequence: str
        """
        
        

        self._tag = None
        self._sequence = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if sequence is not None:
            self.sequence = sequence

    @property
    def tag(self):
        r"""Gets the tag of this CreateKmsTagRequestBody.

        :return: The tag of this CreateKmsTagRequestBody.
        :rtype: :class:`huaweicloudsdkkms.v2.TagItem`
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this CreateKmsTagRequestBody.

        :param tag: The tag of this CreateKmsTagRequestBody.
        :type tag: :class:`huaweicloudsdkkms.v2.TagItem`
        """
        self._tag = tag

    @property
    def sequence(self):
        r"""Gets the sequence of this CreateKmsTagRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :return: The sequence of this CreateKmsTagRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this CreateKmsTagRequestBody.

        请求消息序列号，36字节序列号。 例如：919c82d4-8046-4722-9094-35c3c6524cff

        :param sequence: The sequence of this CreateKmsTagRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, CreateKmsTagRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
