# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSubCustomerResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name'
    }

    def __init__(self, domain_id=None, domain_name=None):
        """CreateSubCustomerResponse

        The model defined in huaweicloud sdk

        :param domain_id: 客户ID。 只有成功或者错误码在CBC.99000050时才会返回。
        :type domain_id: str
        :param domain_name: 客户的华为云账号名。 若请求参数中传递了此参数值，此处返回的响应值与请求参数中取值一致。若请求参数中未传递此参数值，此处返回的响应值为系统随机生成的32位字符串。 只有成功时或者错误码在CBC.99000050时才会返回。
        :type domain_name: str
        """
        
        super(CreateSubCustomerResponse, self).__init__()

        self._domain_id = None
        self._domain_name = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateSubCustomerResponse.

        客户ID。 只有成功或者错误码在CBC.99000050时才会返回。

        :return: The domain_id of this CreateSubCustomerResponse.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateSubCustomerResponse.

        客户ID。 只有成功或者错误码在CBC.99000050时才会返回。

        :param domain_id: The domain_id of this CreateSubCustomerResponse.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this CreateSubCustomerResponse.

        客户的华为云账号名。 若请求参数中传递了此参数值，此处返回的响应值与请求参数中取值一致。若请求参数中未传递此参数值，此处返回的响应值为系统随机生成的32位字符串。 只有成功时或者错误码在CBC.99000050时才会返回。

        :return: The domain_name of this CreateSubCustomerResponse.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this CreateSubCustomerResponse.

        客户的华为云账号名。 若请求参数中传递了此参数值，此处返回的响应值与请求参数中取值一致。若请求参数中未传递此参数值，此处返回的响应值为系统随机生成的32位字符串。 只有成功时或者错误码在CBC.99000050时才会返回。

        :param domain_name: The domain_name of this CreateSubCustomerResponse.
        :type domain_name: str
        """
        self._domain_name = domain_name

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
        if not isinstance(other, CreateSubCustomerResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
