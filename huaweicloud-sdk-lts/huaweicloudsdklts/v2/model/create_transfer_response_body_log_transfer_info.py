# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTransferResponseBodyLogTransferInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_agency_transfer': 'CreateTransferResponseBodyLogTransferInfoLogAgencyTransfer',
        'log_create_time': 'int',
        'log_storage_format': 'str',
        'log_transfer_detail': 'TransferDetail',
        'log_transfer_mode': 'str',
        'log_transfer_status': 'str',
        'log_transfer_type': 'str'
    }

    attribute_map = {
        'log_agency_transfer': 'log_agency_transfer',
        'log_create_time': 'log_create_time',
        'log_storage_format': 'log_storage_format',
        'log_transfer_detail': 'log_transfer_detail',
        'log_transfer_mode': 'log_transfer_mode',
        'log_transfer_status': 'log_transfer_status',
        'log_transfer_type': 'log_transfer_type'
    }

    def __init__(self, log_agency_transfer=None, log_create_time=None, log_storage_format=None, log_transfer_detail=None, log_transfer_mode=None, log_transfer_status=None, log_transfer_type=None):
        """CreateTransferResponseBodyLogTransferInfo

        The model defined in huaweicloud sdk

        :param log_agency_transfer: 
        :type log_agency_transfer: :class:`huaweicloudsdklts.v2.CreateTransferResponseBodyLogTransferInfoLogAgencyTransfer`
        :param log_create_time: 日志转储创建时间
        :type log_create_time: int
        :param log_storage_format: 日志转储格式。只支持\&quot;RAW\&quot;, \&quot;JSON\&quot;。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW
        :type log_storage_format: str
        :param log_transfer_detail: 日志转储详细信息
        :type log_transfer_detail: :class:`huaweicloudsdklts.v2.TransferDetail`
        :param log_transfer_mode: 日志转储方式。cycle是指周期性转储，realTime是指实时转储。OBS转储只支持\&quot;cycle\&quot;，DIS转储和DMS转储只支持\&quot;realTime\&quot;。
        :type log_transfer_mode: str
        :param log_transfer_status: 日志转储状态，ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态
        :type log_transfer_status: str
        :param log_transfer_type: 日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储
        :type log_transfer_type: str
        """
        
        

        self._log_agency_transfer = None
        self._log_create_time = None
        self._log_storage_format = None
        self._log_transfer_detail = None
        self._log_transfer_mode = None
        self._log_transfer_status = None
        self._log_transfer_type = None
        self.discriminator = None

        if log_agency_transfer is not None:
            self.log_agency_transfer = log_agency_transfer
        self.log_create_time = log_create_time
        self.log_storage_format = log_storage_format
        self.log_transfer_detail = log_transfer_detail
        self.log_transfer_mode = log_transfer_mode
        self.log_transfer_status = log_transfer_status
        self.log_transfer_type = log_transfer_type

    @property
    def log_agency_transfer(self):
        """Gets the log_agency_transfer of this CreateTransferResponseBodyLogTransferInfo.

        :return: The log_agency_transfer of this CreateTransferResponseBodyLogTransferInfo.
        :rtype: :class:`huaweicloudsdklts.v2.CreateTransferResponseBodyLogTransferInfoLogAgencyTransfer`
        """
        return self._log_agency_transfer

    @log_agency_transfer.setter
    def log_agency_transfer(self, log_agency_transfer):
        """Sets the log_agency_transfer of this CreateTransferResponseBodyLogTransferInfo.

        :param log_agency_transfer: The log_agency_transfer of this CreateTransferResponseBodyLogTransferInfo.
        :type log_agency_transfer: :class:`huaweicloudsdklts.v2.CreateTransferResponseBodyLogTransferInfoLogAgencyTransfer`
        """
        self._log_agency_transfer = log_agency_transfer

    @property
    def log_create_time(self):
        """Gets the log_create_time of this CreateTransferResponseBodyLogTransferInfo.

        日志转储创建时间

        :return: The log_create_time of this CreateTransferResponseBodyLogTransferInfo.
        :rtype: int
        """
        return self._log_create_time

    @log_create_time.setter
    def log_create_time(self, log_create_time):
        """Sets the log_create_time of this CreateTransferResponseBodyLogTransferInfo.

        日志转储创建时间

        :param log_create_time: The log_create_time of this CreateTransferResponseBodyLogTransferInfo.
        :type log_create_time: int
        """
        self._log_create_time = log_create_time

    @property
    def log_storage_format(self):
        """Gets the log_storage_format of this CreateTransferResponseBodyLogTransferInfo.

        日志转储格式。只支持\"RAW\", \"JSON\"。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW

        :return: The log_storage_format of this CreateTransferResponseBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_storage_format

    @log_storage_format.setter
    def log_storage_format(self, log_storage_format):
        """Sets the log_storage_format of this CreateTransferResponseBodyLogTransferInfo.

        日志转储格式。只支持\"RAW\", \"JSON\"。RAW是指原始日志格式，JSON是指JSON日志格式。OBS转储和DIS转储支持JSON和RAW，DMS转储仅支持RAW

        :param log_storage_format: The log_storage_format of this CreateTransferResponseBodyLogTransferInfo.
        :type log_storage_format: str
        """
        self._log_storage_format = log_storage_format

    @property
    def log_transfer_detail(self):
        """Gets the log_transfer_detail of this CreateTransferResponseBodyLogTransferInfo.

        日志转储详细信息

        :return: The log_transfer_detail of this CreateTransferResponseBodyLogTransferInfo.
        :rtype: :class:`huaweicloudsdklts.v2.TransferDetail`
        """
        return self._log_transfer_detail

    @log_transfer_detail.setter
    def log_transfer_detail(self, log_transfer_detail):
        """Sets the log_transfer_detail of this CreateTransferResponseBodyLogTransferInfo.

        日志转储详细信息

        :param log_transfer_detail: The log_transfer_detail of this CreateTransferResponseBodyLogTransferInfo.
        :type log_transfer_detail: :class:`huaweicloudsdklts.v2.TransferDetail`
        """
        self._log_transfer_detail = log_transfer_detail

    @property
    def log_transfer_mode(self):
        """Gets the log_transfer_mode of this CreateTransferResponseBodyLogTransferInfo.

        日志转储方式。cycle是指周期性转储，realTime是指实时转储。OBS转储只支持\"cycle\"，DIS转储和DMS转储只支持\"realTime\"。

        :return: The log_transfer_mode of this CreateTransferResponseBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_transfer_mode

    @log_transfer_mode.setter
    def log_transfer_mode(self, log_transfer_mode):
        """Sets the log_transfer_mode of this CreateTransferResponseBodyLogTransferInfo.

        日志转储方式。cycle是指周期性转储，realTime是指实时转储。OBS转储只支持\"cycle\"，DIS转储和DMS转储只支持\"realTime\"。

        :param log_transfer_mode: The log_transfer_mode of this CreateTransferResponseBodyLogTransferInfo.
        :type log_transfer_mode: str
        """
        self._log_transfer_mode = log_transfer_mode

    @property
    def log_transfer_status(self):
        """Gets the log_transfer_status of this CreateTransferResponseBodyLogTransferInfo.

        日志转储状态，ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态

        :return: The log_transfer_status of this CreateTransferResponseBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_transfer_status

    @log_transfer_status.setter
    def log_transfer_status(self, log_transfer_status):
        """Sets the log_transfer_status of this CreateTransferResponseBodyLogTransferInfo.

        日志转储状态，ENABLE是指日志转储开启状态，DISABLE是指日志转储关闭状态，EXCEPTION是指日志转储异常状态

        :param log_transfer_status: The log_transfer_status of this CreateTransferResponseBodyLogTransferInfo.
        :type log_transfer_status: str
        """
        self._log_transfer_status = log_transfer_status

    @property
    def log_transfer_type(self):
        """Gets the log_transfer_type of this CreateTransferResponseBodyLogTransferInfo.

        日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储

        :return: The log_transfer_type of this CreateTransferResponseBodyLogTransferInfo.
        :rtype: str
        """
        return self._log_transfer_type

    @log_transfer_type.setter
    def log_transfer_type(self, log_transfer_type):
        """Sets the log_transfer_type of this CreateTransferResponseBodyLogTransferInfo.

        日志转储类型。OBS指OBS日志转储，DIS指DIS日志转储，DMS指DMS日志转储

        :param log_transfer_type: The log_transfer_type of this CreateTransferResponseBodyLogTransferInfo.
        :type log_transfer_type: str
        """
        self._log_transfer_type = log_transfer_type

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
        if not isinstance(other, CreateTransferResponseBodyLogTransferInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
