# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTransferRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_group_id': 'str',
        'log_streams': 'list[CreateTransferRequestBodyLogStreams]',
        'log_transfer_info': 'CreateTransferRequestBodyLogTransferInfo'
    }

    attribute_map = {
        'log_group_id': 'log_group_id',
        'log_streams': 'log_streams',
        'log_transfer_info': 'log_transfer_info'
    }

    def __init__(self, log_group_id=None, log_streams=None, log_transfer_info=None):
        """CreateTransferRequestBody

        The model defined in huaweicloud sdk

        :param log_group_id: 日志组ID
        :type log_group_id: str
        :param log_streams: 日志流ID集合
        :type log_streams: list[:class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogStreams`]
        :param log_transfer_info: 
        :type log_transfer_info: :class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogTransferInfo`
        """
        
        

        self._log_group_id = None
        self._log_streams = None
        self._log_transfer_info = None
        self.discriminator = None

        self.log_group_id = log_group_id
        self.log_streams = log_streams
        self.log_transfer_info = log_transfer_info

    @property
    def log_group_id(self):
        """Gets the log_group_id of this CreateTransferRequestBody.

        日志组ID

        :return: The log_group_id of this CreateTransferRequestBody.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this CreateTransferRequestBody.

        日志组ID

        :param log_group_id: The log_group_id of this CreateTransferRequestBody.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_streams(self):
        """Gets the log_streams of this CreateTransferRequestBody.

        日志流ID集合

        :return: The log_streams of this CreateTransferRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogStreams`]
        """
        return self._log_streams

    @log_streams.setter
    def log_streams(self, log_streams):
        """Sets the log_streams of this CreateTransferRequestBody.

        日志流ID集合

        :param log_streams: The log_streams of this CreateTransferRequestBody.
        :type log_streams: list[:class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogStreams`]
        """
        self._log_streams = log_streams

    @property
    def log_transfer_info(self):
        """Gets the log_transfer_info of this CreateTransferRequestBody.

        :return: The log_transfer_info of this CreateTransferRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogTransferInfo`
        """
        return self._log_transfer_info

    @log_transfer_info.setter
    def log_transfer_info(self, log_transfer_info):
        """Sets the log_transfer_info of this CreateTransferRequestBody.

        :param log_transfer_info: The log_transfer_info of this CreateTransferRequestBody.
        :type log_transfer_info: :class:`huaweicloudsdklts.v2.CreateTransferRequestBodyLogTransferInfo`
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
        if not isinstance(other, CreateTransferRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
