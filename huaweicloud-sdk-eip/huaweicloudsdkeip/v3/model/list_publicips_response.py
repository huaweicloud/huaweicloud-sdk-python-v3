# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPublicipsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'publicips': 'list[PublicipSingleShowResp]',
        'page_info': 'PageInfoOption',
        'total_count': 'int'
    }

    attribute_map = {
        'request_id': 'request_id',
        'publicips': 'publicips',
        'page_info': 'page_info',
        'total_count': 'total_count'
    }

    def __init__(self, request_id=None, publicips=None, page_info=None, total_count=None):
        """ListPublicipsResponse

        The model defined in huaweicloud sdk

        :param request_id: 本次请求的编号
        :type request_id: str
        :param publicips: 功能说明：弹性公网IP对象
        :type publicips: list[:class:`huaweicloudsdkeip.v3.PublicipSingleShowResp`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoOption`
        :param total_count: 公网IP总条目数
        :type total_count: int
        """
        
        super(ListPublicipsResponse, self).__init__()

        self._request_id = None
        self._publicips = None
        self._page_info = None
        self._total_count = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if publicips is not None:
            self.publicips = publicips
        if page_info is not None:
            self.page_info = page_info
        if total_count is not None:
            self.total_count = total_count

    @property
    def request_id(self):
        """Gets the request_id of this ListPublicipsResponse.

        本次请求的编号

        :return: The request_id of this ListPublicipsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListPublicipsResponse.

        本次请求的编号

        :param request_id: The request_id of this ListPublicipsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def publicips(self):
        """Gets the publicips of this ListPublicipsResponse.

        功能说明：弹性公网IP对象

        :return: The publicips of this ListPublicipsResponse.
        :rtype: list[:class:`huaweicloudsdkeip.v3.PublicipSingleShowResp`]
        """
        return self._publicips

    @publicips.setter
    def publicips(self, publicips):
        """Sets the publicips of this ListPublicipsResponse.

        功能说明：弹性公网IP对象

        :param publicips: The publicips of this ListPublicipsResponse.
        :type publicips: list[:class:`huaweicloudsdkeip.v3.PublicipSingleShowResp`]
        """
        self._publicips = publicips

    @property
    def page_info(self):
        """Gets the page_info of this ListPublicipsResponse.


        :return: The page_info of this ListPublicipsResponse.
        :rtype: :class:`huaweicloudsdkeip.v3.PageInfoOption`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListPublicipsResponse.


        :param page_info: The page_info of this ListPublicipsResponse.
        :type page_info: :class:`huaweicloudsdkeip.v3.PageInfoOption`
        """
        self._page_info = page_info

    @property
    def total_count(self):
        """Gets the total_count of this ListPublicipsResponse.

        公网IP总条目数

        :return: The total_count of this ListPublicipsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListPublicipsResponse.

        公网IP总条目数

        :param total_count: The total_count of this ListPublicipsResponse.
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
        if not isinstance(other, ListPublicipsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
