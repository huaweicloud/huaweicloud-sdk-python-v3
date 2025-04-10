# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRegisteredServicesForAuthSchemaV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_codes': 'list[str]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'service_codes': 'service_codes',
        'page_info': 'page_info'
    }

    def __init__(self, service_codes=None, page_info=None):
        r"""ListRegisteredServicesForAuthSchemaV5Response

        The model defined in huaweicloud sdk

        :param service_codes: 服务名称缩写列表。
        :type service_codes: list[str]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        
        super(ListRegisteredServicesForAuthSchemaV5Response, self).__init__()

        self._service_codes = None
        self._page_info = None
        self.discriminator = None

        if service_codes is not None:
            self.service_codes = service_codes
        if page_info is not None:
            self.page_info = page_info

    @property
    def service_codes(self):
        r"""Gets the service_codes of this ListRegisteredServicesForAuthSchemaV5Response.

        服务名称缩写列表。

        :return: The service_codes of this ListRegisteredServicesForAuthSchemaV5Response.
        :rtype: list[str]
        """
        return self._service_codes

    @service_codes.setter
    def service_codes(self, service_codes):
        r"""Sets the service_codes of this ListRegisteredServicesForAuthSchemaV5Response.

        服务名称缩写列表。

        :param service_codes: The service_codes of this ListRegisteredServicesForAuthSchemaV5Response.
        :type service_codes: list[str]
        """
        self._service_codes = service_codes

    @property
    def page_info(self):
        r"""Gets the page_info of this ListRegisteredServicesForAuthSchemaV5Response.

        :return: The page_info of this ListRegisteredServicesForAuthSchemaV5Response.
        :rtype: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListRegisteredServicesForAuthSchemaV5Response.

        :param page_info: The page_info of this ListRegisteredServicesForAuthSchemaV5Response.
        :type page_info: :class:`huaweicloudsdkiam.v5.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListRegisteredServicesForAuthSchemaV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
