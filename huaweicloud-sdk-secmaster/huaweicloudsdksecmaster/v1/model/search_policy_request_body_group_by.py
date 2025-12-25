# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchPolicyRequestBodyGroupBy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_by_fields': 'list[str]',
        'group_by_hit': 'SearchPolicyRequestBodyGroupByGroupByHit'
    }

    attribute_map = {
        'group_by_fields': 'group_by_fields',
        'group_by_hit': 'group_by_hit'
    }

    def __init__(self, group_by_fields=None, group_by_hit=None):
        r"""SearchPolicyRequestBodyGroupBy

        The model defined in huaweicloud sdk

        :param group_by_fields: 聚合字段
        :type group_by_fields: list[str]
        :param group_by_hit: 
        :type group_by_hit: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyGroupByGroupByHit`
        """
        
        

        self._group_by_fields = None
        self._group_by_hit = None
        self.discriminator = None

        if group_by_fields is not None:
            self.group_by_fields = group_by_fields
        if group_by_hit is not None:
            self.group_by_hit = group_by_hit

    @property
    def group_by_fields(self):
        r"""Gets the group_by_fields of this SearchPolicyRequestBodyGroupBy.

        聚合字段

        :return: The group_by_fields of this SearchPolicyRequestBodyGroupBy.
        :rtype: list[str]
        """
        return self._group_by_fields

    @group_by_fields.setter
    def group_by_fields(self, group_by_fields):
        r"""Sets the group_by_fields of this SearchPolicyRequestBodyGroupBy.

        聚合字段

        :param group_by_fields: The group_by_fields of this SearchPolicyRequestBodyGroupBy.
        :type group_by_fields: list[str]
        """
        self._group_by_fields = group_by_fields

    @property
    def group_by_hit(self):
        r"""Gets the group_by_hit of this SearchPolicyRequestBodyGroupBy.

        :return: The group_by_hit of this SearchPolicyRequestBodyGroupBy.
        :rtype: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyGroupByGroupByHit`
        """
        return self._group_by_hit

    @group_by_hit.setter
    def group_by_hit(self, group_by_hit):
        r"""Sets the group_by_hit of this SearchPolicyRequestBodyGroupBy.

        :param group_by_hit: The group_by_hit of this SearchPolicyRequestBodyGroupBy.
        :type group_by_hit: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyGroupByGroupByHit`
        """
        self._group_by_hit = group_by_hit

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
        if not isinstance(other, SearchPolicyRequestBodyGroupBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
