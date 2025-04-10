# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceProviderConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schemas': 'list[str]',
        'documentation_uri': 'str',
        'authentication_schemes': 'list[AuthenticationSchemeItemDto]',
        'patch': 'PatchDto',
        'bulk': 'BulkDto',
        'filter': 'FilterDto',
        'change_password': 'ChangePasswordDto',
        'sort': 'SortDto',
        'etag': 'EtagDto'
    }

    attribute_map = {
        'schemas': 'schemas',
        'documentation_uri': 'documentationUri',
        'authentication_schemes': 'authenticationSchemes',
        'patch': 'patch',
        'bulk': 'bulk',
        'filter': 'filter',
        'change_password': 'changePassword',
        'sort': 'sort',
        'etag': 'etag'
    }

    def __init__(self, schemas=None, documentation_uri=None, authentication_schemes=None, patch=None, bulk=None, filter=None, change_password=None, sort=None, etag=None):
        r"""ServiceProviderConfigResponse

        The model defined in huaweicloud sdk

        :param schemas: 概要
        :type schemas: list[str]
        :param documentation_uri: 帮助文档链接
        :type documentation_uri: str
        :param authentication_schemes: 认证概要列表
        :type authentication_schemes: list[:class:`huaweicloudsdkidentitycenterscim.v1.AuthenticationSchemeItemDto`]
        :param patch: 
        :type patch: :class:`huaweicloudsdkidentitycenterscim.v1.PatchDto`
        :param bulk: 
        :type bulk: :class:`huaweicloudsdkidentitycenterscim.v1.BulkDto`
        :param filter: 
        :type filter: :class:`huaweicloudsdkidentitycenterscim.v1.FilterDto`
        :param change_password: 
        :type change_password: :class:`huaweicloudsdkidentitycenterscim.v1.ChangePasswordDto`
        :param sort: 
        :type sort: :class:`huaweicloudsdkidentitycenterscim.v1.SortDto`
        :param etag: 
        :type etag: :class:`huaweicloudsdkidentitycenterscim.v1.EtagDto`
        """
        
        super(ServiceProviderConfigResponse, self).__init__()

        self._schemas = None
        self._documentation_uri = None
        self._authentication_schemes = None
        self._patch = None
        self._bulk = None
        self._filter = None
        self._change_password = None
        self._sort = None
        self._etag = None
        self.discriminator = None

        if schemas is not None:
            self.schemas = schemas
        if documentation_uri is not None:
            self.documentation_uri = documentation_uri
        if authentication_schemes is not None:
            self.authentication_schemes = authentication_schemes
        if patch is not None:
            self.patch = patch
        if bulk is not None:
            self.bulk = bulk
        if filter is not None:
            self.filter = filter
        if change_password is not None:
            self.change_password = change_password
        if sort is not None:
            self.sort = sort
        if etag is not None:
            self.etag = etag

    @property
    def schemas(self):
        r"""Gets the schemas of this ServiceProviderConfigResponse.

        概要

        :return: The schemas of this ServiceProviderConfigResponse.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this ServiceProviderConfigResponse.

        概要

        :param schemas: The schemas of this ServiceProviderConfigResponse.
        :type schemas: list[str]
        """
        self._schemas = schemas

    @property
    def documentation_uri(self):
        r"""Gets the documentation_uri of this ServiceProviderConfigResponse.

        帮助文档链接

        :return: The documentation_uri of this ServiceProviderConfigResponse.
        :rtype: str
        """
        return self._documentation_uri

    @documentation_uri.setter
    def documentation_uri(self, documentation_uri):
        r"""Sets the documentation_uri of this ServiceProviderConfigResponse.

        帮助文档链接

        :param documentation_uri: The documentation_uri of this ServiceProviderConfigResponse.
        :type documentation_uri: str
        """
        self._documentation_uri = documentation_uri

    @property
    def authentication_schemes(self):
        r"""Gets the authentication_schemes of this ServiceProviderConfigResponse.

        认证概要列表

        :return: The authentication_schemes of this ServiceProviderConfigResponse.
        :rtype: list[:class:`huaweicloudsdkidentitycenterscim.v1.AuthenticationSchemeItemDto`]
        """
        return self._authentication_schemes

    @authentication_schemes.setter
    def authentication_schemes(self, authentication_schemes):
        r"""Sets the authentication_schemes of this ServiceProviderConfigResponse.

        认证概要列表

        :param authentication_schemes: The authentication_schemes of this ServiceProviderConfigResponse.
        :type authentication_schemes: list[:class:`huaweicloudsdkidentitycenterscim.v1.AuthenticationSchemeItemDto`]
        """
        self._authentication_schemes = authentication_schemes

    @property
    def patch(self):
        r"""Gets the patch of this ServiceProviderConfigResponse.

        :return: The patch of this ServiceProviderConfigResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.PatchDto`
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        r"""Sets the patch of this ServiceProviderConfigResponse.

        :param patch: The patch of this ServiceProviderConfigResponse.
        :type patch: :class:`huaweicloudsdkidentitycenterscim.v1.PatchDto`
        """
        self._patch = patch

    @property
    def bulk(self):
        r"""Gets the bulk of this ServiceProviderConfigResponse.

        :return: The bulk of this ServiceProviderConfigResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.BulkDto`
        """
        return self._bulk

    @bulk.setter
    def bulk(self, bulk):
        r"""Sets the bulk of this ServiceProviderConfigResponse.

        :param bulk: The bulk of this ServiceProviderConfigResponse.
        :type bulk: :class:`huaweicloudsdkidentitycenterscim.v1.BulkDto`
        """
        self._bulk = bulk

    @property
    def filter(self):
        r"""Gets the filter of this ServiceProviderConfigResponse.

        :return: The filter of this ServiceProviderConfigResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.FilterDto`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ServiceProviderConfigResponse.

        :param filter: The filter of this ServiceProviderConfigResponse.
        :type filter: :class:`huaweicloudsdkidentitycenterscim.v1.FilterDto`
        """
        self._filter = filter

    @property
    def change_password(self):
        r"""Gets the change_password of this ServiceProviderConfigResponse.

        :return: The change_password of this ServiceProviderConfigResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.ChangePasswordDto`
        """
        return self._change_password

    @change_password.setter
    def change_password(self, change_password):
        r"""Sets the change_password of this ServiceProviderConfigResponse.

        :param change_password: The change_password of this ServiceProviderConfigResponse.
        :type change_password: :class:`huaweicloudsdkidentitycenterscim.v1.ChangePasswordDto`
        """
        self._change_password = change_password

    @property
    def sort(self):
        r"""Gets the sort of this ServiceProviderConfigResponse.

        :return: The sort of this ServiceProviderConfigResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.SortDto`
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ServiceProviderConfigResponse.

        :param sort: The sort of this ServiceProviderConfigResponse.
        :type sort: :class:`huaweicloudsdkidentitycenterscim.v1.SortDto`
        """
        self._sort = sort

    @property
    def etag(self):
        r"""Gets the etag of this ServiceProviderConfigResponse.

        :return: The etag of this ServiceProviderConfigResponse.
        :rtype: :class:`huaweicloudsdkidentitycenterscim.v1.EtagDto`
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        r"""Sets the etag of this ServiceProviderConfigResponse.

        :param etag: The etag of this ServiceProviderConfigResponse.
        :type etag: :class:`huaweicloudsdkidentitycenterscim.v1.EtagDto`
        """
        self._etag = etag

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
        if not isinstance(other, ServiceProviderConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
