# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PutObjectTaggingRequestBodyTagSet:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "PutObjectTaggingRequestBodyTagSet"

    sensitive_list = []

    openapi_types = {
        'tag': 'list[Tag]'
    }

    attribute_map = {
        'tag': 'Tag'
    }

    def __init__(self, tag=None):
        r"""PutObjectTaggingRequestBodyTagSet

        The model defined in huaweicloud sdk

        :param tag: Information element of Tag 
        :type tag: list[:class:`huaweicloudsdkobs.v1.Tag`]
        """
        
        

        self._tag = None
        self.discriminator = None

        self.tag = tag

    @property
    def tag(self):
        r"""Gets the tag of this PutObjectTaggingRequestBodyTagSet.

        Information element of Tag 

        :return: The tag of this PutObjectTaggingRequestBodyTagSet.
        :rtype: list[:class:`huaweicloudsdkobs.v1.Tag`]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this PutObjectTaggingRequestBodyTagSet.

        Information element of Tag 

        :param tag: The tag of this PutObjectTaggingRequestBodyTagSet.
        :type tag: list[:class:`huaweicloudsdkobs.v1.Tag`]
        """
        self._tag = tag

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
        if not isinstance(other, PutObjectTaggingRequestBodyTagSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
