# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DecryptDatakeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_key': 'str',
        'datakey_length': 'str',
        'datakey_dgst': 'str'
    }

    attribute_map = {
        'data_key': 'data_key',
        'datakey_length': 'datakey_length',
        'datakey_dgst': 'datakey_dgst'
    }

    def __init__(self, data_key=None, datakey_length=None, datakey_dgst=None):
        """DecryptDatakeyResponse

        The model defined in huaweicloud sdk

        :param data_key: DEK明文的16进制字符串。
        :type data_key: str
        :param datakey_length: DEK明文字节长度。
        :type datakey_length: str
        :param datakey_dgst: DEK明文的SHA256值对应的16进制字符串。
        :type datakey_dgst: str
        """
        
        super(DecryptDatakeyResponse, self).__init__()

        self._data_key = None
        self._datakey_length = None
        self._datakey_dgst = None
        self.discriminator = None

        if data_key is not None:
            self.data_key = data_key
        if datakey_length is not None:
            self.datakey_length = datakey_length
        if datakey_dgst is not None:
            self.datakey_dgst = datakey_dgst

    @property
    def data_key(self):
        """Gets the data_key of this DecryptDatakeyResponse.

        DEK明文的16进制字符串。

        :return: The data_key of this DecryptDatakeyResponse.
        :rtype: str
        """
        return self._data_key

    @data_key.setter
    def data_key(self, data_key):
        """Sets the data_key of this DecryptDatakeyResponse.

        DEK明文的16进制字符串。

        :param data_key: The data_key of this DecryptDatakeyResponse.
        :type data_key: str
        """
        self._data_key = data_key

    @property
    def datakey_length(self):
        """Gets the datakey_length of this DecryptDatakeyResponse.

        DEK明文字节长度。

        :return: The datakey_length of this DecryptDatakeyResponse.
        :rtype: str
        """
        return self._datakey_length

    @datakey_length.setter
    def datakey_length(self, datakey_length):
        """Sets the datakey_length of this DecryptDatakeyResponse.

        DEK明文字节长度。

        :param datakey_length: The datakey_length of this DecryptDatakeyResponse.
        :type datakey_length: str
        """
        self._datakey_length = datakey_length

    @property
    def datakey_dgst(self):
        """Gets the datakey_dgst of this DecryptDatakeyResponse.

        DEK明文的SHA256值对应的16进制字符串。

        :return: The datakey_dgst of this DecryptDatakeyResponse.
        :rtype: str
        """
        return self._datakey_dgst

    @datakey_dgst.setter
    def datakey_dgst(self, datakey_dgst):
        """Sets the datakey_dgst of this DecryptDatakeyResponse.

        DEK明文的SHA256值对应的16进制字符串。

        :param datakey_dgst: The datakey_dgst of this DecryptDatakeyResponse.
        :type datakey_dgst: str
        """
        self._datakey_dgst = datakey_dgst

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
        if not isinstance(other, DecryptDatakeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
