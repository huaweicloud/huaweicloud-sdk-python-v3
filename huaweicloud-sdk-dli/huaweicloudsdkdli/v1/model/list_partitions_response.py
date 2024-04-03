# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPartitionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'partitions': 'PartitionList'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'partitions': 'partitions'
    }

    def __init__(self, is_success=None, message=None, partitions=None):
        """ListPartitionsResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求结果，true为成功，false为失败
        :type is_success: bool
        :param message: 信息
        :type message: str
        :param partitions: 
        :type partitions: :class:`huaweicloudsdkdli.v1.PartitionList`
        """
        
        super(ListPartitionsResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._partitions = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if partitions is not None:
            self.partitions = partitions

    @property
    def is_success(self):
        """Gets the is_success of this ListPartitionsResponse.

        请求结果，true为成功，false为失败

        :return: The is_success of this ListPartitionsResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListPartitionsResponse.

        请求结果，true为成功，false为失败

        :param is_success: The is_success of this ListPartitionsResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListPartitionsResponse.

        信息

        :return: The message of this ListPartitionsResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListPartitionsResponse.

        信息

        :param message: The message of this ListPartitionsResponse.
        :type message: str
        """
        self._message = message

    @property
    def partitions(self):
        """Gets the partitions of this ListPartitionsResponse.

        :return: The partitions of this ListPartitionsResponse.
        :rtype: :class:`huaweicloudsdkdli.v1.PartitionList`
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ListPartitionsResponse.

        :param partitions: The partitions of this ListPartitionsResponse.
        :type partitions: :class:`huaweicloudsdkdli.v1.PartitionList`
        """
        self._partitions = partitions

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
        if not isinstance(other, ListPartitionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
