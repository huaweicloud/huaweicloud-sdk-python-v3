# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationMaskResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notification_mask_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'notification_mask_id': 'notification_mask_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, notification_mask_id=None, offset=None, limit=None):
        """ListNotificationMaskResourcesRequest

        The model defined in huaweicloud sdk

        :param notification_mask_id: 屏蔽规则ID
        :type notification_mask_id: str
        :param offset: 分页偏移量
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        """
        
        

        self._notification_mask_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.notification_mask_id = notification_mask_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def notification_mask_id(self):
        """Gets the notification_mask_id of this ListNotificationMaskResourcesRequest.

        屏蔽规则ID

        :return: The notification_mask_id of this ListNotificationMaskResourcesRequest.
        :rtype: str
        """
        return self._notification_mask_id

    @notification_mask_id.setter
    def notification_mask_id(self, notification_mask_id):
        """Sets the notification_mask_id of this ListNotificationMaskResourcesRequest.

        屏蔽规则ID

        :param notification_mask_id: The notification_mask_id of this ListNotificationMaskResourcesRequest.
        :type notification_mask_id: str
        """
        self._notification_mask_id = notification_mask_id

    @property
    def offset(self):
        """Gets the offset of this ListNotificationMaskResourcesRequest.

        分页偏移量

        :return: The offset of this ListNotificationMaskResourcesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListNotificationMaskResourcesRequest.

        分页偏移量

        :param offset: The offset of this ListNotificationMaskResourcesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListNotificationMaskResourcesRequest.

        分页大小

        :return: The limit of this ListNotificationMaskResourcesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNotificationMaskResourcesRequest.

        分页大小

        :param limit: The limit of this ListNotificationMaskResourcesRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListNotificationMaskResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
