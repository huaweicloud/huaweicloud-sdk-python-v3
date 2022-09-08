# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssociationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'associations': 'list[Association]',
        'request_id': 'str',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'associations': 'associations',
        'request_id': 'request_id',
        'page_info': 'page_info'
    }

    def __init__(self, associations=None, request_id=None, page_info=None):
        """ListAssociationsResponse

        The model defined in huaweicloud sdk

        :param associations: 路由表关联列表
        :type associations: list[:class:`huaweicloudsdker.v3.Association`]
        :param request_id: 请求ID
        :type request_id: str
        :param page_info: 
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        """
        
        super(ListAssociationsResponse, self).__init__()

        self._associations = None
        self._request_id = None
        self._page_info = None
        self.discriminator = None

        if associations is not None:
            self.associations = associations
        if request_id is not None:
            self.request_id = request_id
        if page_info is not None:
            self.page_info = page_info

    @property
    def associations(self):
        """Gets the associations of this ListAssociationsResponse.

        路由表关联列表

        :return: The associations of this ListAssociationsResponse.
        :rtype: list[:class:`huaweicloudsdker.v3.Association`]
        """
        return self._associations

    @associations.setter
    def associations(self, associations):
        """Sets the associations of this ListAssociationsResponse.

        路由表关联列表

        :param associations: The associations of this ListAssociationsResponse.
        :type associations: list[:class:`huaweicloudsdker.v3.Association`]
        """
        self._associations = associations

    @property
    def request_id(self):
        """Gets the request_id of this ListAssociationsResponse.

        请求ID

        :return: The request_id of this ListAssociationsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListAssociationsResponse.

        请求ID

        :param request_id: The request_id of this ListAssociationsResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def page_info(self):
        """Gets the page_info of this ListAssociationsResponse.


        :return: The page_info of this ListAssociationsResponse.
        :rtype: :class:`huaweicloudsdker.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAssociationsResponse.


        :param page_info: The page_info of this ListAssociationsResponse.
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
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
        if not isinstance(other, ListAssociationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
