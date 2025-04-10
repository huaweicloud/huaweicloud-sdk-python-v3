# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteserviceDiscoveryRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_code': 'str',
        'error_message': 'str',
        'response_status': 'int',
        'id': 'list[str]'
    }

    attribute_map = {
        'error_code': 'errorCode',
        'error_message': 'errorMessage',
        'response_status': 'responseStatus',
        'id': 'id'
    }

    def __init__(self, error_code=None, error_message=None, response_status=None, id=None):
        r"""DeleteserviceDiscoveryRulesResponse

        The model defined in huaweicloud sdk

        :param error_code: 响应码。
        :type error_code: str
        :param error_message: 响应信息描述。
        :type error_message: str
        :param response_status: 响应状态码（不再使用）。
        :type response_status: int
        :param id: 服务发现规则id列表，多AZ配置同步时使用。
        :type id: list[str]
        """
        
        super(DeleteserviceDiscoveryRulesResponse, self).__init__()

        self._error_code = None
        self._error_message = None
        self._response_status = None
        self._id = None
        self.discriminator = None

        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if response_status is not None:
            self.response_status = response_status
        if id is not None:
            self.id = id

    @property
    def error_code(self):
        r"""Gets the error_code of this DeleteserviceDiscoveryRulesResponse.

        响应码。

        :return: The error_code of this DeleteserviceDiscoveryRulesResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this DeleteserviceDiscoveryRulesResponse.

        响应码。

        :param error_code: The error_code of this DeleteserviceDiscoveryRulesResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this DeleteserviceDiscoveryRulesResponse.

        响应信息描述。

        :return: The error_message of this DeleteserviceDiscoveryRulesResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this DeleteserviceDiscoveryRulesResponse.

        响应信息描述。

        :param error_message: The error_message of this DeleteserviceDiscoveryRulesResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def response_status(self):
        r"""Gets the response_status of this DeleteserviceDiscoveryRulesResponse.

        响应状态码（不再使用）。

        :return: The response_status of this DeleteserviceDiscoveryRulesResponse.
        :rtype: int
        """
        return self._response_status

    @response_status.setter
    def response_status(self, response_status):
        r"""Sets the response_status of this DeleteserviceDiscoveryRulesResponse.

        响应状态码（不再使用）。

        :param response_status: The response_status of this DeleteserviceDiscoveryRulesResponse.
        :type response_status: int
        """
        self._response_status = response_status

    @property
    def id(self):
        r"""Gets the id of this DeleteserviceDiscoveryRulesResponse.

        服务发现规则id列表，多AZ配置同步时使用。

        :return: The id of this DeleteserviceDiscoveryRulesResponse.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DeleteserviceDiscoveryRulesResponse.

        服务发现规则id列表，多AZ配置同步时使用。

        :param id: The id of this DeleteserviceDiscoveryRulesResponse.
        :type id: list[str]
        """
        self._id = id

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
        if not isinstance(other, DeleteserviceDiscoveryRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
