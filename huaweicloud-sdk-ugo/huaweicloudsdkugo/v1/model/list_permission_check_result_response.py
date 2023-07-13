# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPermissionCheckResultResponse(SdkResponse):

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
        'passed_permission_items': 'list[PermissionItem]',
        'alarm_permission_items': 'list[PermissionItem]',
        'failed_permission_items': 'list[PermissionItem]',
        'passed_count': 'int',
        'alarm_count': 'int',
        'failed_count': 'int'
    }

    attribute_map = {
        'total_count': 'total_count',
        'passed_permission_items': 'passed_permission_items',
        'alarm_permission_items': 'alarm_permission_items',
        'failed_permission_items': 'failed_permission_items',
        'passed_count': 'passed_count',
        'alarm_count': 'alarm_count',
        'failed_count': 'failed_count'
    }

    def __init__(self, total_count=None, passed_permission_items=None, alarm_permission_items=None, failed_permission_items=None, passed_count=None, alarm_count=None, failed_count=None):
        """ListPermissionCheckResultResponse

        The model defined in huaweicloud sdk

        :param total_count: 权限检查的总条目个数。
        :type total_count: int
        :param passed_permission_items: 权限检查的通过条目。
        :type passed_permission_items: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        :param alarm_permission_items: 权限检查的告警条目。
        :type alarm_permission_items: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        :param failed_permission_items: 权限检查的失败条目。
        :type failed_permission_items: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        :param passed_count: 权限检查的通过条目个数。
        :type passed_count: int
        :param alarm_count: 权限检查的告警条目个数。
        :type alarm_count: int
        :param failed_count: 权限检查的失败条目个数。
        :type failed_count: int
        """
        
        super(ListPermissionCheckResultResponse, self).__init__()

        self._total_count = None
        self._passed_permission_items = None
        self._alarm_permission_items = None
        self._failed_permission_items = None
        self._passed_count = None
        self._alarm_count = None
        self._failed_count = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if passed_permission_items is not None:
            self.passed_permission_items = passed_permission_items
        if alarm_permission_items is not None:
            self.alarm_permission_items = alarm_permission_items
        if failed_permission_items is not None:
            self.failed_permission_items = failed_permission_items
        if passed_count is not None:
            self.passed_count = passed_count
        if alarm_count is not None:
            self.alarm_count = alarm_count
        if failed_count is not None:
            self.failed_count = failed_count

    @property
    def total_count(self):
        """Gets the total_count of this ListPermissionCheckResultResponse.

        权限检查的总条目个数。

        :return: The total_count of this ListPermissionCheckResultResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListPermissionCheckResultResponse.

        权限检查的总条目个数。

        :param total_count: The total_count of this ListPermissionCheckResultResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def passed_permission_items(self):
        """Gets the passed_permission_items of this ListPermissionCheckResultResponse.

        权限检查的通过条目。

        :return: The passed_permission_items of this ListPermissionCheckResultResponse.
        :rtype: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        """
        return self._passed_permission_items

    @passed_permission_items.setter
    def passed_permission_items(self, passed_permission_items):
        """Sets the passed_permission_items of this ListPermissionCheckResultResponse.

        权限检查的通过条目。

        :param passed_permission_items: The passed_permission_items of this ListPermissionCheckResultResponse.
        :type passed_permission_items: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        """
        self._passed_permission_items = passed_permission_items

    @property
    def alarm_permission_items(self):
        """Gets the alarm_permission_items of this ListPermissionCheckResultResponse.

        权限检查的告警条目。

        :return: The alarm_permission_items of this ListPermissionCheckResultResponse.
        :rtype: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        """
        return self._alarm_permission_items

    @alarm_permission_items.setter
    def alarm_permission_items(self, alarm_permission_items):
        """Sets the alarm_permission_items of this ListPermissionCheckResultResponse.

        权限检查的告警条目。

        :param alarm_permission_items: The alarm_permission_items of this ListPermissionCheckResultResponse.
        :type alarm_permission_items: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        """
        self._alarm_permission_items = alarm_permission_items

    @property
    def failed_permission_items(self):
        """Gets the failed_permission_items of this ListPermissionCheckResultResponse.

        权限检查的失败条目。

        :return: The failed_permission_items of this ListPermissionCheckResultResponse.
        :rtype: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        """
        return self._failed_permission_items

    @failed_permission_items.setter
    def failed_permission_items(self, failed_permission_items):
        """Sets the failed_permission_items of this ListPermissionCheckResultResponse.

        权限检查的失败条目。

        :param failed_permission_items: The failed_permission_items of this ListPermissionCheckResultResponse.
        :type failed_permission_items: list[:class:`huaweicloudsdkugo.v1.PermissionItem`]
        """
        self._failed_permission_items = failed_permission_items

    @property
    def passed_count(self):
        """Gets the passed_count of this ListPermissionCheckResultResponse.

        权限检查的通过条目个数。

        :return: The passed_count of this ListPermissionCheckResultResponse.
        :rtype: int
        """
        return self._passed_count

    @passed_count.setter
    def passed_count(self, passed_count):
        """Sets the passed_count of this ListPermissionCheckResultResponse.

        权限检查的通过条目个数。

        :param passed_count: The passed_count of this ListPermissionCheckResultResponse.
        :type passed_count: int
        """
        self._passed_count = passed_count

    @property
    def alarm_count(self):
        """Gets the alarm_count of this ListPermissionCheckResultResponse.

        权限检查的告警条目个数。

        :return: The alarm_count of this ListPermissionCheckResultResponse.
        :rtype: int
        """
        return self._alarm_count

    @alarm_count.setter
    def alarm_count(self, alarm_count):
        """Sets the alarm_count of this ListPermissionCheckResultResponse.

        权限检查的告警条目个数。

        :param alarm_count: The alarm_count of this ListPermissionCheckResultResponse.
        :type alarm_count: int
        """
        self._alarm_count = alarm_count

    @property
    def failed_count(self):
        """Gets the failed_count of this ListPermissionCheckResultResponse.

        权限检查的失败条目个数。

        :return: The failed_count of this ListPermissionCheckResultResponse.
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """Sets the failed_count of this ListPermissionCheckResultResponse.

        权限检查的失败条目个数。

        :param failed_count: The failed_count of this ListPermissionCheckResultResponse.
        :type failed_count: int
        """
        self._failed_count = failed_count

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
        if not isinstance(other, ListPermissionCheckResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
