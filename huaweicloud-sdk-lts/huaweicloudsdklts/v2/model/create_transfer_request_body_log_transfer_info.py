# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTransferRequestBodyLogTransferInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_transfer_type': 'str',
        'log_transfer_mode': 'str',
        'log_storage_format': 'str',
        'log_transfer_status': 'str',
        'log_agency_transfer': 'CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer',
        'log_transfer_detail': 'TransferDetail'
    }

    attribute_map = {
        'log_transfer_type': 'log_transfer_type',
        'log_transfer_mode': 'log_transfer_mode',
        'log_storage_format': 'log_storage_format',
        'log_transfer_status': 'log_transfer_status',
        'log_agency_transfer': 'log_agency_transfer',
        'log_transfer_detail': 'log_transfer_detail'
    }

    def __init__(self, log_transfer_type=None, log_transfer_mode=None, log_storage_format=None, log_transfer_status=None, log_agency_transfer=None, log_transfer_detail=None):
        """CreateTransferRequestBodyLogTransferInfo

        The model defined in huaweicloud sdk

        :param log_transfer_type: 日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储
        :type log_transfer_type: str
        :param log_transfer_mode: 日志转储方式。cycle是指周期性转储，realTime是指实时转储。OBS转储只支持\&quot;cycle\&quot;，DIS转储和DMS转储只支持\&quot;realTime\&quot;。
        :type log_transfer_mode: str
        :param log_storage_format: 日志转储格式。只支持\&quot;RAW\&quot;, \&quot;JSON\&quot;。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW
        :type log_storage_format: str
        :param log_transfer_status: 日志转储状态，只支持\&quot;ENABLE\&quot;,\&quot;DISABLE\&quot;,\&quot;EXCEPTION\&quot;。ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态
        :type log_transfer_status: str
        :param log_agency_transfer: 
        :type log_agency_transfer: :class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer`
        :param log_transfer_detail: 
        :type log_transfer_detail: :class:`huaweicloudsdklts.v2.TransferDetail`
        """
        
        

        self._log_transfer_type = None
        self._log_transfer_mode = None
        self._log_storage_format = None
        self._log_transfer_status = None
        self._log_agency_transfer = None
        self._log_transfer_detail = None
        self.discriminator = None

        self.log_transfer_type = log_transfer_type
        self.log_transfer_mode = log_transfer_mode
        self.log_storage_format = log_storage_format
        self.log_transfer_status = log_transfer_status
        if log_agency_transfer is not None:
            self.log_agency_transfer = log_agency_transfer
        self.log_transfer_detail = log_transfer_detail

    @property
    def log_transfer_type(self):
        """Gets the log_transfer_type of this CreateTransferRequestBodyLogTransferInfo.

        日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储

        :return: The log_transfer_type of this CreateTransferRequestBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_transfer_type

    @log_transfer_type.setter
    def log_transfer_type(self, log_transfer_type):
        """Sets the log_transfer_type of this CreateTransferRequestBodyLogTransferInfo.

        日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储

        :param log_transfer_type: The log_transfer_type of this CreateTransferRequestBodyLogTransferInfo.
        :type log_transfer_type: str
        """
        self._log_transfer_type = log_transfer_type

    @property
    def log_transfer_mode(self):
        """Gets the log_transfer_mode of this CreateTransferRequestBodyLogTransferInfo.

        日志转储方式。cycle是指周期性转储，realTime是指实时转储。OBS转储只支持\"cycle\"，DIS转储和DMS转储只支持\"realTime\"。

        :return: The log_transfer_mode of this CreateTransferRequestBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_transfer_mode

    @log_transfer_mode.setter
    def log_transfer_mode(self, log_transfer_mode):
        """Sets the log_transfer_mode of this CreateTransferRequestBodyLogTransferInfo.

        日志转储方式。cycle是指周期性转储，realTime是指实时转储。OBS转储只支持\"cycle\"，DIS转储和DMS转储只支持\"realTime\"。

        :param log_transfer_mode: The log_transfer_mode of this CreateTransferRequestBodyLogTransferInfo.
        :type log_transfer_mode: str
        """
        self._log_transfer_mode = log_transfer_mode

    @property
    def log_storage_format(self):
        """Gets the log_storage_format of this CreateTransferRequestBodyLogTransferInfo.

        日志转储格式。只支持\"RAW\", \"JSON\"。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW

        :return: The log_storage_format of this CreateTransferRequestBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_storage_format

    @log_storage_format.setter
    def log_storage_format(self, log_storage_format):
        """Sets the log_storage_format of this CreateTransferRequestBodyLogTransferInfo.

        日志转储格式。只支持\"RAW\", \"JSON\"。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW

        :param log_storage_format: The log_storage_format of this CreateTransferRequestBodyLogTransferInfo.
        :type log_storage_format: str
        """
        self._log_storage_format = log_storage_format

    @property
    def log_transfer_status(self):
        """Gets the log_transfer_status of this CreateTransferRequestBodyLogTransferInfo.

        日志转储状态，只支持\"ENABLE\",\"DISABLE\",\"EXCEPTION\"。ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态

        :return: The log_transfer_status of this CreateTransferRequestBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_transfer_status

    @log_transfer_status.setter
    def log_transfer_status(self, log_transfer_status):
        """Sets the log_transfer_status of this CreateTransferRequestBodyLogTransferInfo.

        日志转储状态，只支持\"ENABLE\",\"DISABLE\",\"EXCEPTION\"。ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态

        :param log_transfer_status: The log_transfer_status of this CreateTransferRequestBodyLogTransferInfo.
        :type log_transfer_status: str
        """
        self._log_transfer_status = log_transfer_status

    @property
    def log_agency_transfer(self):
        """Gets the log_agency_transfer of this CreateTransferRequestBodyLogTransferInfo.

        :return: The log_agency_transfer of this CreateTransferRequestBodyLogTransferInfo.
        :rtype: :class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer`
        """
        return self._log_agency_transfer

    @log_agency_transfer.setter
    def log_agency_transfer(self, log_agency_transfer):
        """Sets the log_agency_transfer of this CreateTransferRequestBodyLogTransferInfo.

        :param log_agency_transfer: The log_agency_transfer of this CreateTransferRequestBodyLogTransferInfo.
        :type log_agency_transfer: :class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogTransferInfoLogAgencyTransfer`
        """
        self._log_agency_transfer = log_agency_transfer

    @property
    def log_transfer_detail(self):
        """Gets the log_transfer_detail of this CreateTransferRequestBodyLogTransferInfo.

        :return: The log_transfer_detail of this CreateTransferRequestBodyLogTransferInfo.
        :rtype: :class:`huaweicloudsdklts.v2.TransferDetail`
        """
        return self._log_transfer_detail

    @log_transfer_detail.setter
    def log_transfer_detail(self, log_transfer_detail):
        """Sets the log_transfer_detail of this CreateTransferRequestBodyLogTransferInfo.

        :param log_transfer_detail: The log_transfer_detail of this CreateTransferRequestBodyLogTransferInfo.
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
        if not isinstance(other, CreateTransferRequestBodyLogTransferInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
