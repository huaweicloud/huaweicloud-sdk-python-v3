# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadAttachmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_type': 'str',
        'doc_id': 'str'
    }

    attribute_map = {
        'ticket_type': 'ticket_type',
        'doc_id': 'doc_id'
    }

    def __init__(self, ticket_type=None, doc_id=None):
        r"""DownloadAttachmentRequest

        The model defined in huaweicloud sdk

        :param ticket_type: **参数解释：** 工单类型，此处传递固定值incident。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type ticket_type: str
        :param doc_id: **参数解释：** 需要下载的文件唯一ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type doc_id: str
        """
        
        

        self._ticket_type = None
        self._doc_id = None
        self.discriminator = None

        self.ticket_type = ticket_type
        self.doc_id = doc_id

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this DownloadAttachmentRequest.

        **参数解释：** 工单类型，此处传递固定值incident。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The ticket_type of this DownloadAttachmentRequest.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this DownloadAttachmentRequest.

        **参数解释：** 工单类型，此处传递固定值incident。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param ticket_type: The ticket_type of this DownloadAttachmentRequest.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def doc_id(self):
        r"""Gets the doc_id of this DownloadAttachmentRequest.

        **参数解释：** 需要下载的文件唯一ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The doc_id of this DownloadAttachmentRequest.
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        r"""Sets the doc_id of this DownloadAttachmentRequest.

        **参数解释：** 需要下载的文件唯一ID。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param doc_id: The doc_id of this DownloadAttachmentRequest.
        :type doc_id: str
        """
        self._doc_id = doc_id

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
        if not isinstance(other, DownloadAttachmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
