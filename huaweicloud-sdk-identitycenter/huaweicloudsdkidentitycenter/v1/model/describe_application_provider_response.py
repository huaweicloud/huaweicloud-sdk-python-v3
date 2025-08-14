# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DescribeApplicationProviderResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_provider_urn': 'str',
        'display_data': 'DisplayDataDto',
        'federation_protocol': 'str',
        'application_provider_id': 'str'
    }

    attribute_map = {
        'application_provider_urn': 'application_provider_urn',
        'display_data': 'display_data',
        'federation_protocol': 'federation_protocol',
        'application_provider_id': 'application_provider_id'
    }

    def __init__(self, application_provider_urn=None, display_data=None, federation_protocol=None, application_provider_id=None):
        r"""DescribeApplicationProviderResponse

        The model defined in huaweicloud sdk

        :param application_provider_urn: 应用程序提供者URN
        :type application_provider_urn: str
        :param display_data: 
        :type display_data: :class:`huaweicloudsdkidentitycenter.v1.DisplayDataDto`
        :param federation_protocol: 支持的协议
        :type federation_protocol: str
        :param application_provider_id: 应用程序提供者唯一标识符（ID）
        :type application_provider_id: str
        """
        
        super(DescribeApplicationProviderResponse, self).__init__()

        self._application_provider_urn = None
        self._display_data = None
        self._federation_protocol = None
        self._application_provider_id = None
        self.discriminator = None

        if application_provider_urn is not None:
            self.application_provider_urn = application_provider_urn
        if display_data is not None:
            self.display_data = display_data
        if federation_protocol is not None:
            self.federation_protocol = federation_protocol
        if application_provider_id is not None:
            self.application_provider_id = application_provider_id

    @property
    def application_provider_urn(self):
        r"""Gets the application_provider_urn of this DescribeApplicationProviderResponse.

        应用程序提供者URN

        :return: The application_provider_urn of this DescribeApplicationProviderResponse.
        :rtype: str
        """
        return self._application_provider_urn

    @application_provider_urn.setter
    def application_provider_urn(self, application_provider_urn):
        r"""Sets the application_provider_urn of this DescribeApplicationProviderResponse.

        应用程序提供者URN

        :param application_provider_urn: The application_provider_urn of this DescribeApplicationProviderResponse.
        :type application_provider_urn: str
        """
        self._application_provider_urn = application_provider_urn

    @property
    def display_data(self):
        r"""Gets the display_data of this DescribeApplicationProviderResponse.

        :return: The display_data of this DescribeApplicationProviderResponse.
        :rtype: :class:`huaweicloudsdkidentitycenter.v1.DisplayDataDto`
        """
        return self._display_data

    @display_data.setter
    def display_data(self, display_data):
        r"""Sets the display_data of this DescribeApplicationProviderResponse.

        :param display_data: The display_data of this DescribeApplicationProviderResponse.
        :type display_data: :class:`huaweicloudsdkidentitycenter.v1.DisplayDataDto`
        """
        self._display_data = display_data

    @property
    def federation_protocol(self):
        r"""Gets the federation_protocol of this DescribeApplicationProviderResponse.

        支持的协议

        :return: The federation_protocol of this DescribeApplicationProviderResponse.
        :rtype: str
        """
        return self._federation_protocol

    @federation_protocol.setter
    def federation_protocol(self, federation_protocol):
        r"""Sets the federation_protocol of this DescribeApplicationProviderResponse.

        支持的协议

        :param federation_protocol: The federation_protocol of this DescribeApplicationProviderResponse.
        :type federation_protocol: str
        """
        self._federation_protocol = federation_protocol

    @property
    def application_provider_id(self):
        r"""Gets the application_provider_id of this DescribeApplicationProviderResponse.

        应用程序提供者唯一标识符（ID）

        :return: The application_provider_id of this DescribeApplicationProviderResponse.
        :rtype: str
        """
        return self._application_provider_id

    @application_provider_id.setter
    def application_provider_id(self, application_provider_id):
        r"""Sets the application_provider_id of this DescribeApplicationProviderResponse.

        应用程序提供者唯一标识符（ID）

        :param application_provider_id: The application_provider_id of this DescribeApplicationProviderResponse.
        :type application_provider_id: str
        """
        self._application_provider_id = application_provider_id

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
        if not isinstance(other, DescribeApplicationProviderResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
