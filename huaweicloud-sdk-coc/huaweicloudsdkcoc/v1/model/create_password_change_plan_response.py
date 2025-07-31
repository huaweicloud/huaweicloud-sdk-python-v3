# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePasswordChangePlanResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider_code': 'str',
        'error_code': 'str',
        'error_msg': 'str',
        'data': 'CreatePasswordChangePlanResponseBodyData'
    }

    attribute_map = {
        'provider_code': 'provider_code',
        'error_code': 'error_code',
        'error_msg': 'error_msg',
        'data': 'data'
    }

    def __init__(self, provider_code=None, error_code=None, error_msg=None, data=None):
        r"""CreatePasswordChangePlanResponse

        The model defined in huaweicloud sdk

        :param provider_code: 服务标识
        :type provider_code: str
        :param error_code: 请求响应代码，范围：0000~9999，正常时取值：0
        :type error_code: str
        :param error_msg: 请求响应描述
        :type error_msg: str
        :param data: 
        :type data: :class:`huaweicloudsdkcoc.v1.CreatePasswordChangePlanResponseBodyData`
        """
        
        super(CreatePasswordChangePlanResponse, self).__init__()

        self._provider_code = None
        self._error_code = None
        self._error_msg = None
        self._data = None
        self.discriminator = None

        if provider_code is not None:
            self.provider_code = provider_code
        if error_code is not None:
            self.error_code = error_code
        if error_msg is not None:
            self.error_msg = error_msg
        if data is not None:
            self.data = data

    @property
    def provider_code(self):
        r"""Gets the provider_code of this CreatePasswordChangePlanResponse.

        服务标识

        :return: The provider_code of this CreatePasswordChangePlanResponse.
        :rtype: str
        """
        return self._provider_code

    @provider_code.setter
    def provider_code(self, provider_code):
        r"""Sets the provider_code of this CreatePasswordChangePlanResponse.

        服务标识

        :param provider_code: The provider_code of this CreatePasswordChangePlanResponse.
        :type provider_code: str
        """
        self._provider_code = provider_code

    @property
    def error_code(self):
        r"""Gets the error_code of this CreatePasswordChangePlanResponse.

        请求响应代码，范围：0000~9999，正常时取值：0

        :return: The error_code of this CreatePasswordChangePlanResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this CreatePasswordChangePlanResponse.

        请求响应代码，范围：0000~9999，正常时取值：0

        :param error_code: The error_code of this CreatePasswordChangePlanResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_msg(self):
        r"""Gets the error_msg of this CreatePasswordChangePlanResponse.

        请求响应描述

        :return: The error_msg of this CreatePasswordChangePlanResponse.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this CreatePasswordChangePlanResponse.

        请求响应描述

        :param error_msg: The error_msg of this CreatePasswordChangePlanResponse.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def data(self):
        r"""Gets the data of this CreatePasswordChangePlanResponse.

        :return: The data of this CreatePasswordChangePlanResponse.
        :rtype: :class:`huaweicloudsdkcoc.v1.CreatePasswordChangePlanResponseBodyData`
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this CreatePasswordChangePlanResponse.

        :param data: The data of this CreatePasswordChangePlanResponse.
        :type data: :class:`huaweicloudsdkcoc.v1.CreatePasswordChangePlanResponseBodyData`
        """
        self._data = data

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
        if not isinstance(other, CreatePasswordChangePlanResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
