# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[BatchDeleteRequestBodyTags]',
        'sys_tags': 'list[BatchDeleteRequestBodySysTags]'
    }

    attribute_map = {
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, tags=None, sys_tags=None):
        r"""BatchDeleteRequestBody

        The model defined in huaweicloud sdk

        :param tags: 资源标签
        :type tags: list[:class:`huaweicloudsdkvpc.v3.BatchDeleteRequestBodyTags`]
        :param sys_tags: 系统标签
        :type sys_tags: list[:class:`huaweicloudsdkvpc.v3.BatchDeleteRequestBodySysTags`]
        """
        
        

        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def tags(self):
        r"""Gets the tags of this BatchDeleteRequestBody.

        资源标签

        :return: The tags of this BatchDeleteRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.BatchDeleteRequestBodyTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchDeleteRequestBody.

        资源标签

        :param tags: The tags of this BatchDeleteRequestBody.
        :type tags: list[:class:`huaweicloudsdkvpc.v3.BatchDeleteRequestBodyTags`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this BatchDeleteRequestBody.

        系统标签

        :return: The sys_tags of this BatchDeleteRequestBody.
        :rtype: list[:class:`huaweicloudsdkvpc.v3.BatchDeleteRequestBodySysTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this BatchDeleteRequestBody.

        系统标签

        :param sys_tags: The sys_tags of this BatchDeleteRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkvpc.v3.BatchDeleteRequestBodySysTags`]
        """
        self._sys_tags = sys_tags

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
        if not isinstance(other, BatchDeleteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
