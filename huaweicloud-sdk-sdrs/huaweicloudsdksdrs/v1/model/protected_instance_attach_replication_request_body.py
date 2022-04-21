# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectedInstanceAttachReplicationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'replication_attachment': 'ProtectedInstanceAttachReplicationRequestParams'
    }

    attribute_map = {
        'replication_attachment': 'replicationAttachment'
    }

    def __init__(self, replication_attachment=None):
        """ProtectedInstanceAttachReplicationRequestBody

        The model defined in huaweicloud sdk

        :param replication_attachment: 
        :type replication_attachment: :class:`huaweicloudsdksdrs.v1.ProtectedInstanceAttachReplicationRequestParams`
        """
        
        

        self._replication_attachment = None
        self.discriminator = None

        self.replication_attachment = replication_attachment

    @property
    def replication_attachment(self):
        """Gets the replication_attachment of this ProtectedInstanceAttachReplicationRequestBody.


        :return: The replication_attachment of this ProtectedInstanceAttachReplicationRequestBody.
        :rtype: :class:`huaweicloudsdksdrs.v1.ProtectedInstanceAttachReplicationRequestParams`
        """
        return self._replication_attachment

    @replication_attachment.setter
    def replication_attachment(self, replication_attachment):
        """Sets the replication_attachment of this ProtectedInstanceAttachReplicationRequestBody.


        :param replication_attachment: The replication_attachment of this ProtectedInstanceAttachReplicationRequestBody.
        :type replication_attachment: :class:`huaweicloudsdksdrs.v1.ProtectedInstanceAttachReplicationRequestParams`
        """
        self._replication_attachment = replication_attachment

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
        if not isinstance(other, ProtectedInstanceAttachReplicationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
