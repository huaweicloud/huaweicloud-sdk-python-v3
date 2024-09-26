# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachmentInstanceSiteCode:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attachment_instance_site_code': 'str'
    }

    attribute_map = {
        'attachment_instance_site_code': 'attachment_instance_site_code'
    }

    def __init__(self, attachment_instance_site_code=None):
        """AttachmentInstanceSiteCode

        The model defined in huaweicloud sdk

        :param attachment_instance_site_code: 中心网络附件对端实例的站点编码。
        :type attachment_instance_site_code: str
        """
        
        

        self._attachment_instance_site_code = None
        self.discriminator = None

        self.attachment_instance_site_code = attachment_instance_site_code

    @property
    def attachment_instance_site_code(self):
        """Gets the attachment_instance_site_code of this AttachmentInstanceSiteCode.

        中心网络附件对端实例的站点编码。

        :return: The attachment_instance_site_code of this AttachmentInstanceSiteCode.
        :rtype: str
        """
        return self._attachment_instance_site_code

    @attachment_instance_site_code.setter
    def attachment_instance_site_code(self, attachment_instance_site_code):
        """Sets the attachment_instance_site_code of this AttachmentInstanceSiteCode.

        中心网络附件对端实例的站点编码。

        :param attachment_instance_site_code: The attachment_instance_site_code of this AttachmentInstanceSiteCode.
        :type attachment_instance_site_code: str
        """
        self._attachment_instance_site_code = attachment_instance_site_code

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
        if not isinstance(other, AttachmentInstanceSiteCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
