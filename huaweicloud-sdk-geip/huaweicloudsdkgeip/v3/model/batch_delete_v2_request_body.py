# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteV2RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[BatchDeleteV2RequestBodyTags]',
        'sys_tags': 'list[BatchDeleteV2RequestBodyTags]'
    }

    attribute_map = {
        'tags': 'tags',
        'sys_tags': 'sys_tags'
    }

    def __init__(self, tags=None, sys_tags=None):
        r"""BatchDeleteV2RequestBody

        The model defined in huaweicloud sdk

        :param tags: 全域弹性公网IP标签
        :type tags: list[:class:`huaweicloudsdkgeip.v3.BatchDeleteV2RequestBodyTags`]
        :param sys_tags: 系统标签
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.BatchDeleteV2RequestBodyTags`]
        """
        
        

        self._tags = None
        self._sys_tags = None
        self.discriminator = None

        self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags

    @property
    def tags(self):
        r"""Gets the tags of this BatchDeleteV2RequestBody.

        全域弹性公网IP标签

        :return: The tags of this BatchDeleteV2RequestBody.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.BatchDeleteV2RequestBodyTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchDeleteV2RequestBody.

        全域弹性公网IP标签

        :param tags: The tags of this BatchDeleteV2RequestBody.
        :type tags: list[:class:`huaweicloudsdkgeip.v3.BatchDeleteV2RequestBodyTags`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this BatchDeleteV2RequestBody.

        系统标签

        :return: The sys_tags of this BatchDeleteV2RequestBody.
        :rtype: list[:class:`huaweicloudsdkgeip.v3.BatchDeleteV2RequestBodyTags`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this BatchDeleteV2RequestBody.

        系统标签

        :param sys_tags: The sys_tags of this BatchDeleteV2RequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkgeip.v3.BatchDeleteV2RequestBodyTags`]
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
        if not isinstance(other, BatchDeleteV2RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
