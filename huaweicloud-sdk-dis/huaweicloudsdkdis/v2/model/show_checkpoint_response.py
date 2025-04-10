# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCheckpointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sequence_number': 'str',
        'metadata': 'str'
    }

    attribute_map = {
        'sequence_number': 'sequence_number',
        'metadata': 'metadata'
    }

    def __init__(self, sequence_number=None, metadata=None):
        r"""ShowCheckpointResponse

        The model defined in huaweicloud sdk

        :param sequence_number: 序列号，用来记录该通道的消费检查点。
        :type sequence_number: str
        :param metadata: 用户消费程序端的元数据信息。
        :type metadata: str
        """
        
        super(ShowCheckpointResponse, self).__init__()

        self._sequence_number = None
        self._metadata = None
        self.discriminator = None

        if sequence_number is not None:
            self.sequence_number = sequence_number
        if metadata is not None:
            self.metadata = metadata

    @property
    def sequence_number(self):
        r"""Gets the sequence_number of this ShowCheckpointResponse.

        序列号，用来记录该通道的消费检查点。

        :return: The sequence_number of this ShowCheckpointResponse.
        :rtype: str
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        r"""Sets the sequence_number of this ShowCheckpointResponse.

        序列号，用来记录该通道的消费检查点。

        :param sequence_number: The sequence_number of this ShowCheckpointResponse.
        :type sequence_number: str
        """
        self._sequence_number = sequence_number

    @property
    def metadata(self):
        r"""Gets the metadata of this ShowCheckpointResponse.

        用户消费程序端的元数据信息。

        :return: The metadata of this ShowCheckpointResponse.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ShowCheckpointResponse.

        用户消费程序端的元数据信息。

        :param metadata: The metadata of this ShowCheckpointResponse.
        :type metadata: str
        """
        self._metadata = metadata

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
        if not isinstance(other, ShowCheckpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
