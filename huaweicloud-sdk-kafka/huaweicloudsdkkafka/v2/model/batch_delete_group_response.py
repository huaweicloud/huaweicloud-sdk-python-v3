# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed_groups': 'list[BatchDeleteGroupRespFailedGroups]',
        'total': 'int'
    }

    attribute_map = {
        'failed_groups': 'failed_groups',
        'total': 'total'
    }

    def __init__(self, failed_groups=None, total=None):
        """BatchDeleteGroupResponse

        The model defined in huaweicloud sdk

        :param failed_groups: 删除失败的消费组列表。
        :type failed_groups: list[:class:`huaweicloudsdkkafka.v2.BatchDeleteGroupRespFailedGroups`]
        :param total: 删除失败的个数
        :type total: int
        """
        
        super(BatchDeleteGroupResponse, self).__init__()

        self._failed_groups = None
        self._total = None
        self.discriminator = None

        if failed_groups is not None:
            self.failed_groups = failed_groups
        if total is not None:
            self.total = total

    @property
    def failed_groups(self):
        """Gets the failed_groups of this BatchDeleteGroupResponse.

        删除失败的消费组列表。

        :return: The failed_groups of this BatchDeleteGroupResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.BatchDeleteGroupRespFailedGroups`]
        """
        return self._failed_groups

    @failed_groups.setter
    def failed_groups(self, failed_groups):
        """Sets the failed_groups of this BatchDeleteGroupResponse.

        删除失败的消费组列表。

        :param failed_groups: The failed_groups of this BatchDeleteGroupResponse.
        :type failed_groups: list[:class:`huaweicloudsdkkafka.v2.BatchDeleteGroupRespFailedGroups`]
        """
        self._failed_groups = failed_groups

    @property
    def total(self):
        """Gets the total of this BatchDeleteGroupResponse.

        删除失败的个数

        :return: The total of this BatchDeleteGroupResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this BatchDeleteGroupResponse.

        删除失败的个数

        :param total: The total of this BatchDeleteGroupResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, BatchDeleteGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
