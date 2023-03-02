# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOtaPackageInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'packages': 'list[OtaPackageInfo]',
        'page': 'PageInfo'
    }

    attribute_map = {
        'packages': 'packages',
        'page': 'page'
    }

    def __init__(self, packages=None, page=None):
        """ListOtaPackageInfoResponse

        The model defined in huaweicloud sdk

        :param packages: 升级包列表
        :type packages: list[:class:`huaweicloudsdkiotda.v5.OtaPackageInfo`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.PageInfo`
        """
        
        super(ListOtaPackageInfoResponse, self).__init__()

        self._packages = None
        self._page = None
        self.discriminator = None

        if packages is not None:
            self.packages = packages
        if page is not None:
            self.page = page

    @property
    def packages(self):
        """Gets the packages of this ListOtaPackageInfoResponse.

        升级包列表

        :return: The packages of this ListOtaPackageInfoResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.OtaPackageInfo`]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this ListOtaPackageInfoResponse.

        升级包列表

        :param packages: The packages of this ListOtaPackageInfoResponse.
        :type packages: list[:class:`huaweicloudsdkiotda.v5.OtaPackageInfo`]
        """
        self._packages = packages

    @property
    def page(self):
        """Gets the page of this ListOtaPackageInfoResponse.

        :return: The page of this ListOtaPackageInfoResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.PageInfo`
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this ListOtaPackageInfoResponse.

        :param page: The page of this ListOtaPackageInfoResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.PageInfo`
        """
        self._page = page

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
        if not isinstance(other, ListOtaPackageInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
