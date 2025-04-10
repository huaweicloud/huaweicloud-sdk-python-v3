# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'tags': 'tags'
    }

    def __init__(self, tags=None):
        r"""TagsReq

        The model defined in huaweicloud sdk

        :param tags: 标签列表。租户权限时该字段必选，op_service权限时和sys_tags二选一。
        :type tags: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        
        

        self._tags = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags

    @property
    def tags(self):
        r"""Gets the tags of this TagsReq.

        标签列表。租户权限时该字段必选，op_service权限时和sys_tags二选一。

        :return: The tags of this TagsReq.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this TagsReq.

        标签列表。租户权限时该字段必选，op_service权限时和sys_tags二选一。

        :param tags: The tags of this TagsReq.
        :type tags: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, TagsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
