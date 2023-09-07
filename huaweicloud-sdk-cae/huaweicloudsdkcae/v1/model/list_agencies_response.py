# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgenciesResponse(SdkResponse):

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
        'kind': 'AgencyKindObj',
        'agencies': 'list[AgencyItem]'
    }

    attribute_map = {
        'api_version': 'api_version',
        'kind': 'kind',
        'agencies': 'agencies'
    }

    def __init__(self, api_version=None, kind=None, agencies=None):
        """ListAgenciesResponse

        The model defined in huaweicloud sdk

        :param api_version: 
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        :param kind: 
        :type kind: :class:`huaweicloudsdkcae.v1.AgencyKindObj`
        :param agencies: 委托列表。
        :type agencies: list[:class:`huaweicloudsdkcae.v1.AgencyItem`]
        """
        
        super(ListAgenciesResponse, self).__init__()

        self._api_version = None
        self._kind = None
        self._agencies = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if agencies is not None:
            self.agencies = agencies

    @property
    def api_version(self):
        """Gets the api_version of this ListAgenciesResponse.

        :return: The api_version of this ListAgenciesResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ListAgenciesResponse.

        :param api_version: The api_version of this ListAgenciesResponse.
        :type api_version: :class:`huaweicloudsdkcae.v1.ApiVersionObj`
        """
        self._api_version = api_version

    @property
    def kind(self):
        """Gets the kind of this ListAgenciesResponse.

        :return: The kind of this ListAgenciesResponse.
        :rtype: :class:`huaweicloudsdkcae.v1.AgencyKindObj`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ListAgenciesResponse.

        :param kind: The kind of this ListAgenciesResponse.
        :type kind: :class:`huaweicloudsdkcae.v1.AgencyKindObj`
        """
        self._kind = kind

    @property
    def agencies(self):
        """Gets the agencies of this ListAgenciesResponse.

        委托列表。

        :return: The agencies of this ListAgenciesResponse.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AgencyItem`]
        """
        return self._agencies

    @agencies.setter
    def agencies(self, agencies):
        """Sets the agencies of this ListAgenciesResponse.

        委托列表。

        :param agencies: The agencies of this ListAgenciesResponse.
        :type agencies: list[:class:`huaweicloudsdkcae.v1.AgencyItem`]
        """
        self._agencies = agencies

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
        if not isinstance(other, ListAgenciesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
