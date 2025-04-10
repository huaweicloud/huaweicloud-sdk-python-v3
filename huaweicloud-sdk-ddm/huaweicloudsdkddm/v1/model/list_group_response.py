# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'group_list': 'list[GroupInfo]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'group_list': 'group_list'
    }

    def __init__(self, total_count=None, group_list=None):
        r"""ListGroupResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数。
        :type total_count: int
        :param group_list: 组信息列表。
        :type group_list: list[:class:`huaweicloudsdkddm.v1.GroupInfo`]
        """
        
        super(ListGroupResponse, self).__init__()

        self._total_count = None
        self._group_list = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if group_list is not None:
            self.group_list = group_list

    @property
    def total_count(self):
        r"""Gets the total_count of this ListGroupResponse.

        总数。

        :return: The total_count of this ListGroupResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListGroupResponse.

        总数。

        :param total_count: The total_count of this ListGroupResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def group_list(self):
        r"""Gets the group_list of this ListGroupResponse.

        组信息列表。

        :return: The group_list of this ListGroupResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GroupInfo`]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        r"""Sets the group_list of this ListGroupResponse.

        组信息列表。

        :param group_list: The group_list of this ListGroupResponse.
        :type group_list: list[:class:`huaweicloudsdkddm.v1.GroupInfo`]
        """
        self._group_list = group_list

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
        if not isinstance(other, ListGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
