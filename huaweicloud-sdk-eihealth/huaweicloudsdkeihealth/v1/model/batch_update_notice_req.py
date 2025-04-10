# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateNoticeReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notice_ids': 'list[str]',
        'operation': 'NoticeOperation'
    }

    attribute_map = {
        'notice_ids': 'notice_ids',
        'operation': 'operation'
    }

    def __init__(self, notice_ids=None, operation=None):
        r"""BatchUpdateNoticeReq

        The model defined in huaweicloud sdk

        :param notice_ids: 批量更新通知消息id列表
        :type notice_ids: list[str]
        :param operation: 
        :type operation: :class:`huaweicloudsdkeihealth.v1.NoticeOperation`
        """
        
        

        self._notice_ids = None
        self._operation = None
        self.discriminator = None

        self.notice_ids = notice_ids
        self.operation = operation

    @property
    def notice_ids(self):
        r"""Gets the notice_ids of this BatchUpdateNoticeReq.

        批量更新通知消息id列表

        :return: The notice_ids of this BatchUpdateNoticeReq.
        :rtype: list[str]
        """
        return self._notice_ids

    @notice_ids.setter
    def notice_ids(self, notice_ids):
        r"""Sets the notice_ids of this BatchUpdateNoticeReq.

        批量更新通知消息id列表

        :param notice_ids: The notice_ids of this BatchUpdateNoticeReq.
        :type notice_ids: list[str]
        """
        self._notice_ids = notice_ids

    @property
    def operation(self):
        r"""Gets the operation of this BatchUpdateNoticeReq.

        :return: The operation of this BatchUpdateNoticeReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.NoticeOperation`
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this BatchUpdateNoticeReq.

        :param operation: The operation of this BatchUpdateNoticeReq.
        :type operation: :class:`huaweicloudsdkeihealth.v1.NoticeOperation`
        """
        self._operation = operation

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
        if not isinstance(other, BatchUpdateNoticeReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
