# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAuthorizeInterfaceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policies': 'list[LakeFormationPolicy]',
        'page_info': 'PagedInfo'
    }

    attribute_map = {
        'policies': 'policies',
        'page_info': 'page_info'
    }

    def __init__(self, policies=None, page_info=None):
        r"""BatchAuthorizeInterfaceResponse

        The model defined in huaweicloud sdk

        :param policies: lakecat策略信息
        :type policies: list[:class:`huaweicloudsdklakeformation.v1.LakeFormationPolicy`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        
        super(BatchAuthorizeInterfaceResponse, self).__init__()

        self._policies = None
        self._page_info = None
        self.discriminator = None

        if policies is not None:
            self.policies = policies
        if page_info is not None:
            self.page_info = page_info

    @property
    def policies(self):
        r"""Gets the policies of this BatchAuthorizeInterfaceResponse.

        lakecat策略信息

        :return: The policies of this BatchAuthorizeInterfaceResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.LakeFormationPolicy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this BatchAuthorizeInterfaceResponse.

        lakecat策略信息

        :param policies: The policies of this BatchAuthorizeInterfaceResponse.
        :type policies: list[:class:`huaweicloudsdklakeformation.v1.LakeFormationPolicy`]
        """
        self._policies = policies

    @property
    def page_info(self):
        r"""Gets the page_info of this BatchAuthorizeInterfaceResponse.

        :return: The page_info of this BatchAuthorizeInterfaceResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this BatchAuthorizeInterfaceResponse.

        :param page_info: The page_info of this BatchAuthorizeInterfaceResponse.
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
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
        if not isinstance(other, BatchAuthorizeInterfaceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
