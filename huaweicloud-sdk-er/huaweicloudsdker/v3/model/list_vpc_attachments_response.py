# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcAttachmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_attachments': 'list[VpcAttachmentDetails]',
        'page_info': 'PageInfo',
        'request_id': 'str'
    }

    attribute_map = {
        'vpc_attachments': 'vpc_attachments',
        'page_info': 'page_info',
        'request_id': 'request_id'
    }

    def __init__(self, vpc_attachments=None, page_info=None, request_id=None):
        r"""ListVpcAttachmentsResponse

        The model defined in huaweicloud sdk

        :param vpc_attachments: VPC连接列表
        :type vpc_attachments: list[:class:`huaweicloudsdker.v3.VpcAttachmentDetails`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        :param request_id: 请求ID
        :type request_id: str
        """
        
        super(ListVpcAttachmentsResponse, self).__init__()

        self._vpc_attachments = None
        self._page_info = None
        self._request_id = None
        self.discriminator = None

        if vpc_attachments is not None:
            self.vpc_attachments = vpc_attachments
        if page_info is not None:
            self.page_info = page_info
        if request_id is not None:
            self.request_id = request_id

    @property
    def vpc_attachments(self):
        r"""Gets the vpc_attachments of this ListVpcAttachmentsResponse.

        VPC连接列表

        :return: The vpc_attachments of this ListVpcAttachmentsResponse.
        :rtype: list[:class:`huaweicloudsdker.v3.VpcAttachmentDetails`]
        """
        return self._vpc_attachments

    @vpc_attachments.setter
    def vpc_attachments(self, vpc_attachments):
        r"""Sets the vpc_attachments of this ListVpcAttachmentsResponse.

        VPC连接列表

        :param vpc_attachments: The vpc_attachments of this ListVpcAttachmentsResponse.
        :type vpc_attachments: list[:class:`huaweicloudsdker.v3.VpcAttachmentDetails`]
        """
        self._vpc_attachments = vpc_attachments

    @property
    def page_info(self):
        r"""Gets the page_info of this ListVpcAttachmentsResponse.

        :return: The page_info of this ListVpcAttachmentsResponse.
        :rtype: :class:`huaweicloudsdker.v3.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListVpcAttachmentsResponse.

        :param page_info: The page_info of this ListVpcAttachmentsResponse.
        :type page_info: :class:`huaweicloudsdker.v3.PageInfo`
        """
        self._page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListVpcAttachmentsResponse.

        请求ID

        :return: The request_id of this ListVpcAttachmentsResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListVpcAttachmentsResponse.

        请求ID

        :param request_id: The request_id of this ListVpcAttachmentsResponse.
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
        if not isinstance(other, ListVpcAttachmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
