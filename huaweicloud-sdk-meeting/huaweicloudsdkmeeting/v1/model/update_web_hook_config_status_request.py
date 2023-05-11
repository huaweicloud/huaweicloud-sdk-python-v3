# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateWebHookConfigStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, id=None, status=None):
        """UpdateWebHookConfigStatusRequest

        The model defined in huaweicloud sdk

        :param id: 订阅配置记录ID。
        :type id: str
        :param status: 事件推送状态。 * 0：启用 * 1：禁用 * 2：锁定 
        :type status: int
        """
        
        

        self._id = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.status = status

    @property
    def id(self):
        """Gets the id of this UpdateWebHookConfigStatusRequest.

        订阅配置记录ID。

        :return: The id of this UpdateWebHookConfigStatusRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateWebHookConfigStatusRequest.

        订阅配置记录ID。

        :param id: The id of this UpdateWebHookConfigStatusRequest.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this UpdateWebHookConfigStatusRequest.

        事件推送状态。 * 0：启用 * 1：禁用 * 2：锁定 

        :return: The status of this UpdateWebHookConfigStatusRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateWebHookConfigStatusRequest.

        事件推送状态。 * 0：启用 * 1：禁用 * 2：锁定 

        :param status: The status of this UpdateWebHookConfigStatusRequest.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, UpdateWebHookConfigStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
