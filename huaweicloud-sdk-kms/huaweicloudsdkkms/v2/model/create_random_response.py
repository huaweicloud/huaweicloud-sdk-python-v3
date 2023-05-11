# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRandomResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'random_data': 'str'
    }

    attribute_map = {
        'random_data': 'random_data'
    }

    def __init__(self, random_data=None):
        """CreateRandomResponse

        The model defined in huaweicloud sdk

        :param random_data: 随机数16进制表示，两位表示1byte。随机数的长度与用户传入的参数 “random_data_length”的长度保持一致。
        :type random_data: str
        """
        
        super(CreateRandomResponse, self).__init__()

        self._random_data = None
        self.discriminator = None

        if random_data is not None:
            self.random_data = random_data

    @property
    def random_data(self):
        """Gets the random_data of this CreateRandomResponse.

        随机数16进制表示，两位表示1byte。随机数的长度与用户传入的参数 “random_data_length”的长度保持一致。

        :return: The random_data of this CreateRandomResponse.
        :rtype: str
        """
        return self._random_data

    @random_data.setter
    def random_data(self, random_data):
        """Sets the random_data of this CreateRandomResponse.

        随机数16进制表示，两位表示1byte。随机数的长度与用户传入的参数 “random_data_length”的长度保持一致。

        :param random_data: The random_data of this CreateRandomResponse.
        :type random_data: str
        """
        self._random_data = random_data

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
        if not isinstance(other, CreateRandomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
