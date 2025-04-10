# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMonitorSystemResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'api_version': 'ApiVersionObj',
        'kind': 'MonitorSystemKindObj',
        'spec': 'ShowMonitorSystemResponseBodySpec'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'spec': 'spec'
    }

    def __init__(self, api_version=None, kind=None, spec=None):
        r"""ShowMonitorSystemResponse

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param kind: 
        :type kind: :class:`huaweicloudsdkcae.v1.MonitorSystemKindObj`
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.ShowMonitorSystemResponseBodySpec`
        """
        
        super(ShowMonitorSystemResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._spec = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if spec is not None:
            self.spec = spec

    @property
    def api_version(self):
        r"""Gets the api_version of this ShowMonitorSystemResponse.

        :return: The api_version of this ShowMonitorSystemResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        r"""Sets the api_version of this ShowMonitorSystemResponse.

        :param api_version: The api_version of this ShowMonitorSystemResponse.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def kind(self):
        r"""Gets the kind of this ShowMonitorSystemResponse.

        :return: The kind of this ShowMonitorSystemResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.MonitorSystemKindObj`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this ShowMonitorSystemResponse.

        :param kind: The kind of this ShowMonitorSystemResponse.
        :type kind: :class:`huaweicloudsdkcae.v1.MonitorSystemKindObj`
        """
        self._kind = kind

    @property
    def spec(self):
        r"""Gets the spec of this ShowMonitorSystemResponse.

        :return: The spec of this ShowMonitorSystemResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ShowMonitorSystemResponseBodySpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ShowMonitorSystemResponse.

        :param spec: The spec of this ShowMonitorSystemResponse.
        :type spec: :class:`huaweicloudsdkcae.v1.ShowMonitorSystemResponseBodySpec`
        """
        self._spec = spec

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
        if not isinstance(other, ShowMonitorSystemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
