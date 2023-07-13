# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushMenuInfoResponseModelData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_id': 'str',
        'message': 'str'
    }

    attribute_map = {
        'log_id': 'log_id',
        'message': 'message'
    }

    def __init__(self, log_id=None, message=None):
        """PushMenuInfoResponseModelData

        The model defined in huaweicloud sdk

        :param log_id: 菜单申请记录ID。
        :type log_id: str
        :param message: 返回信息。
        :type message: str
        """
        
        

        self._log_id = None
        self._message = None
        self.discriminator = None

        if log_id is not None:
            self.log_id = log_id
        if message is not None:
            self.message = message

    @property
    def log_id(self):
        """Gets the log_id of this PushMenuInfoResponseModelData.

        菜单申请记录ID。

        :return: The log_id of this PushMenuInfoResponseModelData.
        :rtype: str
        """
        return self._log_id

    @log_id.setter
    def log_id(self, log_id):
        """Sets the log_id of this PushMenuInfoResponseModelData.

        菜单申请记录ID。

        :param log_id: The log_id of this PushMenuInfoResponseModelData.
        :type log_id: str
        """
        self._log_id = log_id

    @property
    def message(self):
        """Gets the message of this PushMenuInfoResponseModelData.

        返回信息。

        :return: The message of this PushMenuInfoResponseModelData.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PushMenuInfoResponseModelData.

        返回信息。

        :param message: The message of this PushMenuInfoResponseModelData.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, PushMenuInfoResponseModelData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
