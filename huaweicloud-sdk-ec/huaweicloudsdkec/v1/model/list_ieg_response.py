# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIegResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'intelligent_enterprise_gateways': 'list[IegItem]',
        'page_info': 'PageInfo',
        'total_count': 'int'
    }

    attribute_map = {
        'intelligent_enterprise_gateways': 'intelligent_enterprise_gateways',
        'page_info': 'page_info',
        'total_count': 'total_count'
    }

    def __init__(self, intelligent_enterprise_gateways=None, page_info=None, total_count=None):
        r"""ListIegResponse

        The model defined in huaweicloud sdk

        :param intelligent_enterprise_gateways: 智能企业网关列表
        :type intelligent_enterprise_gateways: list[:class:`huaweicloudsdkec.v1.IegItem`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkec.v1.PageInfo`
        :param total_count: 智能企业网关数量
        :type total_count: int
        """
        
        super(ListIegResponse, self).__init__()

        self._intelligent_enterprise_gateways = None
        self._page_info = None
        self._total_count = None
        self.discriminator = None

        if intelligent_enterprise_gateways is not None:
            self.intelligent_enterprise_gateways = intelligent_enterprise_gateways
        if page_info is not None:
            self.page_info = page_info
        if total_count is not None:
            self.total_count = total_count

    @property
    def intelligent_enterprise_gateways(self):
        r"""Gets the intelligent_enterprise_gateways of this ListIegResponse.

        智能企业网关列表

        :return: The intelligent_enterprise_gateways of this ListIegResponse.
        :rtype: list[:class:`huaweicloudsdkec.v1.IegItem`]
        """
        return self._intelligent_enterprise_gateways

    @intelligent_enterprise_gateways.setter
    def intelligent_enterprise_gateways(self, intelligent_enterprise_gateways):
        r"""Sets the intelligent_enterprise_gateways of this ListIegResponse.

        智能企业网关列表

        :param intelligent_enterprise_gateways: The intelligent_enterprise_gateways of this ListIegResponse.
        :type intelligent_enterprise_gateways: list[:class:`huaweicloudsdkec.v1.IegItem`]
        """
        self._intelligent_enterprise_gateways = intelligent_enterprise_gateways

    @property
    def page_info(self):
        r"""Gets the page_info of this ListIegResponse.

        :return: The page_info of this ListIegResponse.
        :rtype: :class:`huaweicloudsdkec.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListIegResponse.

        :param page_info: The page_info of this ListIegResponse.
        :type page_info: :class:`huaweicloudsdkec.v1.PageInfo`
        """
        self._page_info = page_info

    @property
    def total_count(self):
        r"""Gets the total_count of this ListIegResponse.

        智能企业网关数量

        :return: The total_count of this ListIegResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListIegResponse.

        智能企业网关数量

        :param total_count: The total_count of this ListIegResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListIegResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
