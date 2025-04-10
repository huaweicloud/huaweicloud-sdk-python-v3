# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetJobTagsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_names': 'list[str]'
    }

    attribute_map = {
        'tag_names': 'tag_names'
    }

    def __init__(self, tag_names=None):
        r"""SetJobTagsRequestBody

        The model defined in huaweicloud sdk

        :param tag_names: 标签列表, 若未空，则标识删除标签
        :type tag_names: list[str]
        """
        
        

        self._tag_names = None
        self.discriminator = None

        if tag_names is not None:
            self.tag_names = tag_names

    @property
    def tag_names(self):
        r"""Gets the tag_names of this SetJobTagsRequestBody.

        标签列表, 若未空，则标识删除标签

        :return: The tag_names of this SetJobTagsRequestBody.
        :rtype: list[str]
        """
        return self._tag_names

    @tag_names.setter
    def tag_names(self, tag_names):
        r"""Sets the tag_names of this SetJobTagsRequestBody.

        标签列表, 若未空，则标识删除标签

        :param tag_names: The tag_names of this SetJobTagsRequestBody.
        :type tag_names: list[str]
        """
        self._tag_names = tag_names

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
        if not isinstance(other, SetJobTagsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
