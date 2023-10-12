# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateNotificationMasksResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relation_ids': 'list[str]',
        'notification_mask_id': 'str'
    }

    attribute_map = {
        'relation_ids': 'relation_ids',
        'notification_mask_id': 'notification_mask_id'
    }

    def __init__(self, relation_ids=None, notification_mask_id=None):
        """BatchUpdateNotificationMasksResponse

        The model defined in huaweicloud sdk

        :param relation_ids: 创建成功的关联ID列表
        :type relation_ids: list[str]
        :param notification_mask_id: 屏蔽规则ID
        :type notification_mask_id: str
        """
        
        super(BatchUpdateNotificationMasksResponse, self).__init__()

        self._relation_ids = None
        self._notification_mask_id = None
        self.discriminator = None

        if relation_ids is not None:
            self.relation_ids = relation_ids
        if notification_mask_id is not None:
            self.notification_mask_id = notification_mask_id

    @property
    def relation_ids(self):
        """Gets the relation_ids of this BatchUpdateNotificationMasksResponse.

        创建成功的关联ID列表

        :return: The relation_ids of this BatchUpdateNotificationMasksResponse.
        :rtype: list[str]
        """
        return self._relation_ids

    @relation_ids.setter
    def relation_ids(self, relation_ids):
        """Sets the relation_ids of this BatchUpdateNotificationMasksResponse.

        创建成功的关联ID列表

        :param relation_ids: The relation_ids of this BatchUpdateNotificationMasksResponse.
        :type relation_ids: list[str]
        """
        self._relation_ids = relation_ids

    @property
    def notification_mask_id(self):
        """Gets the notification_mask_id of this BatchUpdateNotificationMasksResponse.

        屏蔽规则ID

        :return: The notification_mask_id of this BatchUpdateNotificationMasksResponse.
        :rtype: str
        """
        return self._notification_mask_id

    @notification_mask_id.setter
    def notification_mask_id(self, notification_mask_id):
        """Sets the notification_mask_id of this BatchUpdateNotificationMasksResponse.

        屏蔽规则ID

        :param notification_mask_id: The notification_mask_id of this BatchUpdateNotificationMasksResponse.
        :type notification_mask_id: str
        """
        self._notification_mask_id = notification_mask_id

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
        if not isinstance(other, BatchUpdateNotificationMasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
