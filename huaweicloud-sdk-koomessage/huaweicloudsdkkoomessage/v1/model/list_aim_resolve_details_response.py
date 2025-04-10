# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimResolveDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resolve_details': 'list[AIMResolveDetail]',
        'page_info': 'Page'
    }

    attribute_map = {
        'resolve_details': 'resolve_details',
        'page_info': 'page_info'
    }

    def __init__(self, resolve_details=None, page_info=None):
        r"""ListAimResolveDetailsResponse

        The model defined in huaweicloud sdk

        :param resolve_details: 查询解析结果集。
        :type resolve_details: list[:class:`huaweicloudsdkkoomessage.v1.AIMResolveDetail`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        
        super(ListAimResolveDetailsResponse, self).__init__()

        self._resolve_details = None
        self._page_info = None
        self.discriminator = None

        if resolve_details is not None:
            self.resolve_details = resolve_details
        if page_info is not None:
            self.page_info = page_info

    @property
    def resolve_details(self):
        r"""Gets the resolve_details of this ListAimResolveDetailsResponse.

        查询解析结果集。

        :return: The resolve_details of this ListAimResolveDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkkoomessage.v1.AIMResolveDetail`]
        """
        return self._resolve_details

    @resolve_details.setter
    def resolve_details(self, resolve_details):
        r"""Sets the resolve_details of this ListAimResolveDetailsResponse.

        查询解析结果集。

        :param resolve_details: The resolve_details of this ListAimResolveDetailsResponse.
        :type resolve_details: list[:class:`huaweicloudsdkkoomessage.v1.AIMResolveDetail`]
        """
        self._resolve_details = resolve_details

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAimResolveDetailsResponse.

        :return: The page_info of this ListAimResolveDetailsResponse.
        :rtype: :class:`huaweicloudsdkkoomessage.v1.Page`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAimResolveDetailsResponse.

        :param page_info: The page_info of this ListAimResolveDetailsResponse.
        :type page_info: :class:`huaweicloudsdkkoomessage.v1.Page`
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
        if not isinstance(other, ListAimResolveDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
