# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'include_tags_quota': 'str'
    }

    attribute_map = {
        'include_tags_quota': 'includeTagsQuota'
    }

    def __init__(self, include_tags_quota=None):
        r"""ShowQuotasRequest

        The model defined in huaweicloud sdk

        :param include_tags_quota: 是否包含标签配额。
        :type include_tags_quota: str
        """
        
        

        self._include_tags_quota = None
        self.discriminator = None

        if include_tags_quota is not None:
            self.include_tags_quota = include_tags_quota

    @property
    def include_tags_quota(self):
        r"""Gets the include_tags_quota of this ShowQuotasRequest.

        是否包含标签配额。

        :return: The include_tags_quota of this ShowQuotasRequest.
        :rtype: str
        """
        return self._include_tags_quota

    @include_tags_quota.setter
    def include_tags_quota(self, include_tags_quota):
        r"""Sets the include_tags_quota of this ShowQuotasRequest.

        是否包含标签配额。

        :param include_tags_quota: The include_tags_quota of this ShowQuotasRequest.
        :type include_tags_quota: str
        """
        self._include_tags_quota = include_tags_quota

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
        if not isinstance(other, ShowQuotasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
