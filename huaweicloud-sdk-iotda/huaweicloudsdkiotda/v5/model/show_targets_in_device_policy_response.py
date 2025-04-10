# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTargetsInDevicePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'targets': 'list[PolicyTargetBase]',
        'page': 'Page'
    }

    attribute_map = {
        'targets': 'targets',
        'page': 'page'
    }

    def __init__(self, targets=None, page=None):
        r"""ShowTargetsInDevicePolicyResponse

        The model defined in huaweicloud sdk

        :param targets: 策略绑定信息列表。
        :type targets: list[:class:`huaweicloudsdkiotda.v5.PolicyTargetBase`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
        """
        
        super(ShowTargetsInDevicePolicyResponse, self).__init__()

        self._targets = None
        self._page = None
        self.discriminator = None

        if targets is not None:
            self.targets = targets
        if page is not None:
            self.page = page

    @property
    def targets(self):
        r"""Gets the targets of this ShowTargetsInDevicePolicyResponse.

        策略绑定信息列表。

        :return: The targets of this ShowTargetsInDevicePolicyResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.PolicyTargetBase`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this ShowTargetsInDevicePolicyResponse.

        策略绑定信息列表。

        :param targets: The targets of this ShowTargetsInDevicePolicyResponse.
        :type targets: list[:class:`huaweicloudsdkiotda.v5.PolicyTargetBase`]
        """
        self._targets = targets

    @property
    def page(self):
        r"""Gets the page of this ShowTargetsInDevicePolicyResponse.

        :return: The page of this ShowTargetsInDevicePolicyResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ShowTargetsInDevicePolicyResponse.

        :param page: The page of this ShowTargetsInDevicePolicyResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.Page`
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
        if not isinstance(other, ShowTargetsInDevicePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
