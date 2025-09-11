# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudServiceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'cloud_services': 'list[ListCloudServiceResponseItemInfo]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'cloud_services': 'cloud_services'
    }

    def __init__(self, request_id=None, cloud_services=None):
        r"""ListCloudServiceResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param cloud_services: 云服务信息列表。
        :type cloud_services: list[:class:`huaweicloudsdksmn.v2.ListCloudServiceResponseItemInfo`]
        """
        
        super(ListCloudServiceResponse, self).__init__()

        self._request_id = None
        self._cloud_services = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if cloud_services is not None:
            self.cloud_services = cloud_services

    @property
    def request_id(self):
        r"""Gets the request_id of this ListCloudServiceResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListCloudServiceResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListCloudServiceResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListCloudServiceResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def cloud_services(self):
        r"""Gets the cloud_services of this ListCloudServiceResponse.

        云服务信息列表。

        :return: The cloud_services of this ListCloudServiceResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ListCloudServiceResponseItemInfo`]
        """
        return self._cloud_services

    @cloud_services.setter
    def cloud_services(self, cloud_services):
        r"""Sets the cloud_services of this ListCloudServiceResponse.

        云服务信息列表。

        :param cloud_services: The cloud_services of this ListCloudServiceResponse.
        :type cloud_services: list[:class:`huaweicloudsdksmn.v2.ListCloudServiceResponseItemInfo`]
        """
        self._cloud_services = cloud_services

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
        if not isinstance(other, ListCloudServiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
