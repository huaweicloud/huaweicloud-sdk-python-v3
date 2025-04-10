# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddDataMaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'masked_data': 'list[dict(str, object)]'
    }

    attribute_map = {
        'masked_data': 'masked_data'
    }

    def __init__(self, masked_data=None):
        r"""BatchAddDataMaskResponse

        The model defined in huaweicloud sdk

        :param masked_data: 脱敏后的数据的数据列表，结构与请求中结构相同
        :type masked_data: list[dict(str, object)]
        """
        
        super(BatchAddDataMaskResponse, self).__init__()

        self._masked_data = None
        self.discriminator = None

        if masked_data is not None:
            self.masked_data = masked_data

    @property
    def masked_data(self):
        r"""Gets the masked_data of this BatchAddDataMaskResponse.

        脱敏后的数据的数据列表，结构与请求中结构相同

        :return: The masked_data of this BatchAddDataMaskResponse.
        :rtype: list[dict(str, object)]
        """
        return self._masked_data

    @masked_data.setter
    def masked_data(self, masked_data):
        r"""Sets the masked_data of this BatchAddDataMaskResponse.

        脱敏后的数据的数据列表，结构与请求中结构相同

        :param masked_data: The masked_data of this BatchAddDataMaskResponse.
        :type masked_data: list[dict(str, object)]
        """
        self._masked_data = masked_data

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
        if not isinstance(other, BatchAddDataMaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
