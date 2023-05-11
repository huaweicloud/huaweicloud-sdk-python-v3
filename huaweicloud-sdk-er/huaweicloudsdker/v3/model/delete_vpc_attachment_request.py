# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteVpcAttachmentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'vpc_attachment_id': 'str'
    }

    attribute_map = {
        'er_id': 'er_id',
        'vpc_attachment_id': 'vpc_attachment_id'
    }

    def __init__(self, er_id=None, vpc_attachment_id=None):
        """DeleteVpcAttachmentRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器实例ID
        :type er_id: str
        :param vpc_attachment_id: VPC连接ID
        :type vpc_attachment_id: str
        """
        
        

        self._er_id = None
        self._vpc_attachment_id = None
        self.discriminator = None

        self.er_id = er_id
        self.vpc_attachment_id = vpc_attachment_id

    @property
    def er_id(self):
        """Gets the er_id of this DeleteVpcAttachmentRequest.

        企业路由器实例ID

        :return: The er_id of this DeleteVpcAttachmentRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this DeleteVpcAttachmentRequest.

        企业路由器实例ID

        :param er_id: The er_id of this DeleteVpcAttachmentRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def vpc_attachment_id(self):
        """Gets the vpc_attachment_id of this DeleteVpcAttachmentRequest.

        VPC连接ID

        :return: The vpc_attachment_id of this DeleteVpcAttachmentRequest.
        :rtype: str
        """
        return self._vpc_attachment_id

    @vpc_attachment_id.setter
    def vpc_attachment_id(self, vpc_attachment_id):
        """Sets the vpc_attachment_id of this DeleteVpcAttachmentRequest.

        VPC连接ID

        :param vpc_attachment_id: The vpc_attachment_id of this DeleteVpcAttachmentRequest.
        :type vpc_attachment_id: str
        """
        self._vpc_attachment_id = vpc_attachment_id

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
        if not isinstance(other, DeleteVpcAttachmentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
