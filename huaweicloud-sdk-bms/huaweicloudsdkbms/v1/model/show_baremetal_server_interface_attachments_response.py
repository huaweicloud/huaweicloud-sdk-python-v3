# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBaremetalServerInterfaceAttachmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interface_attachments': 'list[InterfaceAttachments]'
    }

    attribute_map = {
        'interface_attachments': 'interfaceAttachments'
    }

    def __init__(self, interface_attachments=None):
        """ShowBaremetalServerInterfaceAttachmentsResponse

        The model defined in huaweicloud sdk

        :param interface_attachments: 裸金属服务器网卡信息列表，详情请参见表2 interfaceAttachments字段数据结构说明。
        :type interface_attachments: list[:class:`huaweicloudsdkbms.v1.InterfaceAttachments`]
        """
        
        super(ShowBaremetalServerInterfaceAttachmentsResponse, self).__init__()

        self._interface_attachments = None
        self.discriminator = None

        if interface_attachments is not None:
            self.interface_attachments = interface_attachments

    @property
    def interface_attachments(self):
        """Gets the interface_attachments of this ShowBaremetalServerInterfaceAttachmentsResponse.

        裸金属服务器网卡信息列表，详情请参见表2 interfaceAttachments字段数据结构说明。

        :return: The interface_attachments of this ShowBaremetalServerInterfaceAttachmentsResponse.
        :rtype: list[:class:`huaweicloudsdkbms.v1.InterfaceAttachments`]
        """
        return self._interface_attachments

    @interface_attachments.setter
    def interface_attachments(self, interface_attachments):
        """Sets the interface_attachments of this ShowBaremetalServerInterfaceAttachmentsResponse.

        裸金属服务器网卡信息列表，详情请参见表2 interfaceAttachments字段数据结构说明。

        :param interface_attachments: The interface_attachments of this ShowBaremetalServerInterfaceAttachmentsResponse.
        :type interface_attachments: list[:class:`huaweicloudsdkbms.v1.InterfaceAttachments`]
        """
        self._interface_attachments = interface_attachments

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
        if not isinstance(other, ShowBaremetalServerInterfaceAttachmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
