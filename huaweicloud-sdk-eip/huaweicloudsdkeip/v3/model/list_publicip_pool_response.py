# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicipPoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_pools': 'list[PublicipPoolShowResp]',
        'request_id': 'str',
        'page_info': 'PageInfoOption'
    }

    attribute_map = {
        'publicip_pools': 'publicip_pools',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, publicip_pools=None, request_id=None, page_info=None):
        """ListPublicipPoolResponse

        The model defined in huaweicloud sdk

        :param publicip_pools: 功能说明：公网池对象
        :type publicip_pools: list[:class:`huaweicloudsdkeip.v3.PublicipPoolShowResp`]
        :param request_id: 本次请求的编号
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoOption`
        """
        
        super(ListPublicipPoolResponse, self).__init__()

        self._publicip_pools = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if publicip_pools is not None:
            self.publicip_pools = publicip_pools
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def publicip_pools(self):
        """Gets the publicip_pools of this ListPublicipPoolResponse.

        功能说明：公网池对象

        :return: The publicip_pools of this ListPublicipPoolResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v3.PublicipPoolShowResp`]
        """
        return self._publicip_pools

    @publicip_pools.setter
    def publicip_pools(self, publicip_pools):
        """Sets the publicip_pools of this ListPublicipPoolResponse.

        功能说明：公网池对象

        :param publicip_pools: The publicip_pools of this ListPublicipPoolResponse.
        :type publicip_pools: list[:class:`huaweicloudsdkeip.v3.PublicipPoolShowResp`]
        """
        self._publicip_pools = publicip_pools

    @property
    def request_id(self):
        """Gets the request_id of this ListPublicipPoolResponse.

        本次请求的编号

        :return: The request_id of this ListPublicipPoolResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListPublicipPoolResponse.

        本次请求的编号

        :param request_id: The request_id of this ListPublicipPoolResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListPublicipPoolResponse.

        :return: The page_info of this ListPublicipPoolResponse.
        :rtype: :class:`huaweicloudsdkeip.v3.PageInfoOption`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPublicipPoolResponse.

        :param page_info: The page_info of this ListPublicipPoolResponse.
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoOption`
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
        if not isinstance(other, ListPublicipPoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
