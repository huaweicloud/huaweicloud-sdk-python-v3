# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNoticeResponse(SdkResponse):

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
        'unread_count': 'int',
        'notices': 'list[NoticeRsp]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'unread_count': 'unread_count',
        'notices': 'notices'
    }

    def __init__(self, total_count=None, unread_count=None, notices=None):
        r"""ListNoticeResponse

        The model defined in huaweicloud sdk

        :param total_count: 通知消息总数
        :type total_count: int
        :param unread_count: 通知消息未读总数
        :type unread_count: int
        :param notices: 通知消息列表
        :type notices: list[:class:`huaweicloudsdkeihealth.v1.NoticeRsp`]
        """
        
        super(ListNoticeResponse, self).__init__()

        self._total_count = None
        self._unread_count = None
        self._notices = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if unread_count is not None:
            self.unread_count = unread_count
        if notices is not None:
            self.notices = notices

    @property
    def total_count(self):
        r"""Gets the total_count of this ListNoticeResponse.

        通知消息总数

        :return: The total_count of this ListNoticeResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListNoticeResponse.

        通知消息总数

        :param total_count: The total_count of this ListNoticeResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def unread_count(self):
        r"""Gets the unread_count of this ListNoticeResponse.

        通知消息未读总数

        :return: The unread_count of this ListNoticeResponse.
        :rtype: int
        """
        return self._unread_count

    @unread_count.setter
    def unread_count(self, unread_count):
        r"""Sets the unread_count of this ListNoticeResponse.

        通知消息未读总数

        :param unread_count: The unread_count of this ListNoticeResponse.
        :type unread_count: int
        """
        self._unread_count = unread_count

    @property
    def notices(self):
        r"""Gets the notices of this ListNoticeResponse.

        通知消息列表

        :return: The notices of this ListNoticeResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.NoticeRsp`]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        r"""Sets the notices of this ListNoticeResponse.

        通知消息列表

        :param notices: The notices of this ListNoticeResponse.
        :type notices: list[:class:`huaweicloudsdkeihealth.v1.NoticeRsp`]
        """
        self._notices = notices

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
        if not isinstance(other, ListNoticeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
