# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusServiceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'metric_name': 'str',
        'server_list': 'list[ShowStatusServiceResponseBodyServerList]'
    }

    attribute_map = {
        'metric_name': 'metric_name',
        'server_list': 'server_list'
    }

    def __init__(self, metric_name=None, server_list=None):
        r"""ShowStatusServiceResponse

        The model defined in huaweicloud sdk

        :param metric_name: 资源名称
        :type metric_name: str
        :param server_list: 服务列表
        :type server_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusServiceResponseBodyServerList`]
        """
        
        super().__init__()

        self._metric_name = None
        self._server_list = None
        self.discriminator = None

        if metric_name is not None:
            self.metric_name = metric_name
        if server_list is not None:
            self.server_list = server_list

    @property
    def metric_name(self):
        r"""Gets the metric_name of this ShowStatusServiceResponse.

        资源名称

        :return: The metric_name of this ShowStatusServiceResponse.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        r"""Sets the metric_name of this ShowStatusServiceResponse.

        资源名称

        :param metric_name: The metric_name of this ShowStatusServiceResponse.
        :type metric_name: str
        """
        self._metric_name = metric_name

    @property
    def server_list(self):
        r"""Gets the server_list of this ShowStatusServiceResponse.

        服务列表

        :return: The server_list of this ShowStatusServiceResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusServiceResponseBodyServerList`]
        """
        return self._server_list

    @server_list.setter
    def server_list(self, server_list):
        r"""Sets the server_list of this ShowStatusServiceResponse.

        服务列表

        :param server_list: The server_list of this ShowStatusServiceResponse.
        :type server_list: list[:class:`huaweicloudsdkcpcs.v1.ShowStatusServiceResponseBodyServerList`]
        """
        self._server_list = server_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatusServiceResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStatusServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
