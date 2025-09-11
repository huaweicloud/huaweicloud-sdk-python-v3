# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllPopsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pops': 'list[PopOuterDetail]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'pops': 'pops',
        'page_info': 'page_info'
    }

    def __init__(self, pops=None, page_info=None):
        r"""ListAllPopsResponse

        The model defined in huaweicloud sdk

        :param pops: 接入点列表。
        :type pops: list[:class:`huaweicloudsdkga.v1.PopOuterDetail`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkga.v1.PageInfo`
        """
        
        super(ListAllPopsResponse, self).__init__()

        self._pops = None
        self._page_info = None
        self.discriminator = None

        if pops is not None:
            self.pops = pops
        if page_info is not None:
            self.page_info = page_info

    @property
    def pops(self):
        r"""Gets the pops of this ListAllPopsResponse.

        接入点列表。

        :return: The pops of this ListAllPopsResponse.
        :rtype: list[:class:`huaweicloudsdkga.v1.PopOuterDetail`]
        """
        return self._pops

    @pops.setter
    def pops(self, pops):
        r"""Sets the pops of this ListAllPopsResponse.

        接入点列表。

        :param pops: The pops of this ListAllPopsResponse.
        :type pops: list[:class:`huaweicloudsdkga.v1.PopOuterDetail`]
        """
        self._pops = pops

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAllPopsResponse.

        :return: The page_info of this ListAllPopsResponse.
        :rtype: :class:`huaweicloudsdkga.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAllPopsResponse.

        :param page_info: The page_info of this ListAllPopsResponse.
        :type page_info: :class:`huaweicloudsdkga.v1.PageInfo`
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
        if not isinstance(other, ListAllPopsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
