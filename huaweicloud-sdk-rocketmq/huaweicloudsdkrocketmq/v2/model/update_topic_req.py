# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTopicReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'read_queue_num': 'float',
        'write_queue_num': 'float',
        'permission': 'str'
    }

    attribute_map = {
        'read_queue_num': 'read_queue_num',
        'write_queue_num': 'write_queue_num',
        'permission': 'permission'
    }

    def __init__(self, read_queue_num=None, write_queue_num=None, permission=None):
        """UpdateTopicReq

        The model defined in huaweicloud sdk

        :param read_queue_num: 总读队列个数。
        :type read_queue_num: float
        :param write_queue_num: 总写队列个数。
        :type write_queue_num: float
        :param permission: 权限。
        :type permission: str
        """
        
        

        self._read_queue_num = None
        self._write_queue_num = None
        self._permission = None
        self.discriminator = None

        if read_queue_num is not None:
            self.read_queue_num = read_queue_num
        if write_queue_num is not None:
            self.write_queue_num = write_queue_num
        if permission is not None:
            self.permission = permission

    @property
    def read_queue_num(self):
        """Gets the read_queue_num of this UpdateTopicReq.

        总读队列个数。

        :return: The read_queue_num of this UpdateTopicReq.
        :rtype: float
        """
        return self._read_queue_num

    @read_queue_num.setter
    def read_queue_num(self, read_queue_num):
        """Sets the read_queue_num of this UpdateTopicReq.

        总读队列个数。

        :param read_queue_num: The read_queue_num of this UpdateTopicReq.
        :type read_queue_num: float
        """
        self._read_queue_num = read_queue_num

    @property
    def write_queue_num(self):
        """Gets the write_queue_num of this UpdateTopicReq.

        总写队列个数。

        :return: The write_queue_num of this UpdateTopicReq.
        :rtype: float
        """
        return self._write_queue_num

    @write_queue_num.setter
    def write_queue_num(self, write_queue_num):
        """Sets the write_queue_num of this UpdateTopicReq.

        总写队列个数。

        :param write_queue_num: The write_queue_num of this UpdateTopicReq.
        :type write_queue_num: float
        """
        self._write_queue_num = write_queue_num

    @property
    def permission(self):
        """Gets the permission of this UpdateTopicReq.

        权限。

        :return: The permission of this UpdateTopicReq.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this UpdateTopicReq.

        权限。

        :param permission: The permission of this UpdateTopicReq.
        :type permission: str
        """
        self._permission = permission

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
        if not isinstance(other, UpdateTopicReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
