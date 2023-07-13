# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTransferRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_transfer_id': 'str',
        'log_transfer_info': 'UpdateTransferRequestBodyLogTransferInfo'
    }

    attribute_map = {
        'log_transfer_id': 'log_transfer_id',
        'log_transfer_info': 'log_transfer_info'
    }

    def __init__(self, log_transfer_id=None, log_transfer_info=None):
        """UpdateTransferRequestBody

        The model defined in huaweicloud sdk

        :param log_transfer_id: 日志转储ID
        :type log_transfer_id: str
        :param log_transfer_info: 
        :type log_transfer_info: :class:`huaweicloudsdklts.v2.UpdateTransferRequestBodyLogTransferInfo`
        """
        
        

        self._log_transfer_id = None
        self._log_transfer_info = None
        self.discriminator = None

        self.log_transfer_id = log_transfer_id
        self.log_transfer_info = log_transfer_info

    @property
    def log_transfer_id(self):
        """Gets the log_transfer_id of this UpdateTransferRequestBody.

        日志转储ID

        :return: The log_transfer_id of this UpdateTransferRequestBody.
        :rtype: str
        """
        return self._log_transfer_id

    @log_transfer_id.setter
    def log_transfer_id(self, log_transfer_id):
        """Sets the log_transfer_id of this UpdateTransferRequestBody.

        日志转储ID

        :param log_transfer_id: The log_transfer_id of this UpdateTransferRequestBody.
        :type log_transfer_id: str
        """
        self._log_transfer_id = log_transfer_id

    @property
    def log_transfer_info(self):
        """Gets the log_transfer_info of this UpdateTransferRequestBody.

        :return: The log_transfer_info of this UpdateTransferRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.UpdateTransferRequestBodyLogTransferInfo`
        """
        return self._log_transfer_info

    @log_transfer_info.setter
    def log_transfer_info(self, log_transfer_info):
        """Sets the log_transfer_info of this UpdateTransferRequestBody.

        :param log_transfer_info: The log_transfer_info of this UpdateTransferRequestBody.
        :type log_transfer_info: :class:`huaweicloudsdklts.v2.UpdateTransferRequestBodyLogTransferInfo`
        """
        self._log_transfer_info = log_transfer_info

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
        if not isinstance(other, UpdateTransferRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
