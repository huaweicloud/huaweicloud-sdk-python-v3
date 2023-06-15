# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncIamUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sync_user': 'list[str]'
    }

    attribute_map = {
        'sync_user': 'sync_user'
    }

    def __init__(self, sync_user=None):
        """SyncIamUsersResponse

        The model defined in huaweicloud sdk

        :param sync_user: 创建成功用户列表
        :type sync_user: list[str]
        """
        
        super(SyncIamUsersResponse, self).__init__()

        self._sync_user = None
        self.discriminator = None

        if sync_user is not None:
            self.sync_user = sync_user

    @property
    def sync_user(self):
        """Gets the sync_user of this SyncIamUsersResponse.

        创建成功用户列表

        :return: The sync_user of this SyncIamUsersResponse.
        :rtype: list[str]
        """
        return self._sync_user

    @sync_user.setter
    def sync_user(self, sync_user):
        """Sets the sync_user of this SyncIamUsersResponse.

        创建成功用户列表

        :param sync_user: The sync_user of this SyncIamUsersResponse.
        :type sync_user: list[str]
        """
        self._sync_user = sync_user

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
        if not isinstance(other, SyncIamUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
