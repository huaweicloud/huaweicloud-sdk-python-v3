# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page': 'Page',
        'flavors': 'list[InstanceFlavor]'
    }

    attribute_map = {
        'page': 'page',
        'flavors': 'flavors'
    }

    def __init__(self, page=None, flavors=None):
        r"""ListInstanceFlavorsResponse

        The model defined in huaweicloud sdk

        :param page: 
        :type page: :class:`huaweicloudsdkiotdm.v5.Page`
        :param flavors: **参数说明**：设备接入实例规格的详情列表。 
        :type flavors: list[:class:`huaweicloudsdkiotdm.v5.InstanceFlavor`]
        """
        
        super(ListInstanceFlavorsResponse, self).__init__()

        self._page = None
        self._flavors = None
        self.discriminator = None

        if page is not None:
            self.page = page
        if flavors is not None:
            self.flavors = flavors

    @property
    def page(self):
        r"""Gets the page of this ListInstanceFlavorsResponse.

        :return: The page of this ListInstanceFlavorsResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.Page`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListInstanceFlavorsResponse.

        :param page: The page of this ListInstanceFlavorsResponse.
        :type page: :class:`huaweicloudsdkiotdm.v5.Page`
        """
        self._page = page

    @property
    def flavors(self):
        r"""Gets the flavors of this ListInstanceFlavorsResponse.

        **参数说明**：设备接入实例规格的详情列表。 

        :return: The flavors of this ListInstanceFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.InstanceFlavor`]
        """
        return self._flavors

    @flavors.setter
    def flavors(self, flavors):
        r"""Sets the flavors of this ListInstanceFlavorsResponse.

        **参数说明**：设备接入实例规格的详情列表。 

        :param flavors: The flavors of this ListInstanceFlavorsResponse.
        :type flavors: list[:class:`huaweicloudsdkiotdm.v5.InstanceFlavor`]
        """
        self._flavors = flavors

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
        if not isinstance(other, ListInstanceFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
