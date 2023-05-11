# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTransferRequestBodyLogTransferInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_storage_format': 'str',
        'log_transfer_status': 'str',
        'log_transfer_detail': 'TransferDetail'
    }

    attribute_map = {
        'log_storage_format': 'log_storage_format',
        'log_transfer_status': 'log_transfer_status',
        'log_transfer_detail': 'log_transfer_detail'
    }

    def __init__(self, log_storage_format=None, log_transfer_status=None, log_transfer_detail=None):
        """UpdateTransferRequestBodyLogTransferInfo

        The model defined in huaweicloud sdk

        :param log_storage_format: 日志转储格式。只支持\&quot;RAW\&quot;, \&quot;JSON\&quot;。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW
        :type log_storage_format: str
        :param log_transfer_status: 日志转储状态，ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态
        :type log_transfer_status: str
        :param log_transfer_detail: 
        :type log_transfer_detail: :class:`huaweicloudsdklts.v2.TransferDetail`
        """
        
        

        self._log_storage_format = None
        self._log_transfer_status = None
        self._log_transfer_detail = None
        self.discriminator = None

        self.log_storage_format = log_storage_format
        self.log_transfer_status = log_transfer_status
        self.log_transfer_detail = log_transfer_detail

    @property
    def log_storage_format(self):
        """Gets the log_storage_format of this UpdateTransferRequestBodyLogTransferInfo.

        日志转储格式。只支持\"RAW\", \"JSON\"。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW

        :return: The log_storage_format of this UpdateTransferRequestBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_storage_format

    @log_storage_format.setter
    def log_storage_format(self, log_storage_format):
        """Sets the log_storage_format of this UpdateTransferRequestBodyLogTransferInfo.

        日志转储格式。只支持\"RAW\", \"JSON\"。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW

        :param log_storage_format: The log_storage_format of this UpdateTransferRequestBodyLogTransferInfo.
        :type log_storage_format: str
        """
        self._log_storage_format = log_storage_format

    @property
    def log_transfer_status(self):
        """Gets the log_transfer_status of this UpdateTransferRequestBodyLogTransferInfo.

        日志转储状态，ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态

        :return: The log_transfer_status of this UpdateTransferRequestBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_transfer_status

    @log_transfer_status.setter
    def log_transfer_status(self, log_transfer_status):
        """Sets the log_transfer_status of this UpdateTransferRequestBodyLogTransferInfo.

        日志转储状态，ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态

        :param log_transfer_status: The log_transfer_status of this UpdateTransferRequestBodyLogTransferInfo.
        :type log_transfer_status: str
        """
        self._log_transfer_status = log_transfer_status

    @property
    def log_transfer_detail(self):
        """Gets the log_transfer_detail of this UpdateTransferRequestBodyLogTransferInfo.

        :return: The log_transfer_detail of this UpdateTransferRequestBodyLogTransferInfo.
        :rtype: :class:`huaweicloudsdklts.v2.TransferDetail`
        """
        return self._log_transfer_detail

    @log_transfer_detail.setter
    def log_transfer_detail(self, log_transfer_detail):
        """Sets the log_transfer_detail of this UpdateTransferRequestBodyLogTransferInfo.

        :param log_transfer_detail: The log_transfer_detail of this UpdateTransferRequestBodyLogTransferInfo.
        :type log_transfer_detail: :class:`huaweicloudsdklts.v2.TransferDetail`
        """
        self._log_transfer_detail = log_transfer_detail

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
        if not isinstance(other, UpdateTransferRequestBodyLogTransferInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
