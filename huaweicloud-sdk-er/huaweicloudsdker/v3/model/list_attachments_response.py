# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttachmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'attachments': 'list[AttachmentDetails]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'attachments': 'attachments',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, attachments=None, page_info=None, request_id=None):
        """ListAttachmentsResponse

        The model defined in huaweicloud sdk

        :param attachments: 连接列表
        :type attachments: list[:class:`huaweicloudsdker.v3.AttachmentDetails`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ListAttachmentsResponse, self).__init__()

        self._attachments = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if attachments is not None:
            self.attachments = attachments
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def attachments(self):
        """Gets the attachments of this ListAttachmentsResponse.

        连接列表

        :return: The attachments of this ListAttachmentsResponse.
        :rtype: list[:class:`huaweicloudsdker.v3.AttachmentDetails`]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this ListAttachmentsResponse.

        连接列表

        :param attachments: The attachments of this ListAttachmentsResponse.
        :type attachments: list[:class:`huaweicloudsdker.v3.AttachmentDetails`]
        """
        self._attachments = attachments

    @property
    def page_info(self):
        """Gets the page_info of this ListAttachmentsResponse.


        :return: The page_info of this ListAttachmentsResponse.
        :rtype: :class:`huaweicloudsdker.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListAttachmentsResponse.


        :param page_info: The page_info of this ListAttachmentsResponse.
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        """Gets the request_id of this ListAttachmentsResponse.

        请求ID

        :return: The request_id of this ListAttachmentsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListAttachmentsResponse.

        请求ID

        :param request_id: The request_id of this ListAttachmentsResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ListAttachmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
