# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchPolicyRequestBodyGroupByGroupByHit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'str',
        'dest': 'str'
    }

    attribute_map = {
        'source': 'source',
        'dest': 'dest'
    }

    def __init__(self, source=None, dest=None):
        r"""SearchPolicyRequestBodyGroupByGroupByHit

        The model defined in huaweicloud sdk

        :param source: 源字段
        :type source: str
        :param dest: 目标字段
        :type dest: str
        """
        
        

        self._source = None
        self._dest = None
        self.discriminator = None

        if source is not None:
            self.source = source
        if dest is not None:
            self.dest = dest

    @property
    def source(self):
        r"""Gets the source of this SearchPolicyRequestBodyGroupByGroupByHit.

        源字段

        :return: The source of this SearchPolicyRequestBodyGroupByGroupByHit.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this SearchPolicyRequestBodyGroupByGroupByHit.

        源字段

        :param source: The source of this SearchPolicyRequestBodyGroupByGroupByHit.
        :type source: str
        """
        self._source = source

    @property
    def dest(self):
        r"""Gets the dest of this SearchPolicyRequestBodyGroupByGroupByHit.

        目标字段

        :return: The dest of this SearchPolicyRequestBodyGroupByGroupByHit.
        :rtype: str
        """
        return self._dest

    @dest.setter
    def dest(self, dest):
        r"""Sets the dest of this SearchPolicyRequestBodyGroupByGroupByHit.

        目标字段

        :param dest: The dest of this SearchPolicyRequestBodyGroupByGroupByHit.
        :type dest: str
        """
        self._dest = dest

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
        if not isinstance(other, SearchPolicyRequestBodyGroupByGroupByHit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
