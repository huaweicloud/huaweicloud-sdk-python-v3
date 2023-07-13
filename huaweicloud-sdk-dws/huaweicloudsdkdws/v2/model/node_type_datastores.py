# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeTypeDatastores:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'attachments': 'NodeTypeDatastoresAttachments'
    }

    attribute_map = {
        'version': 'version',
        'attachments': 'attachments'
    }

    def __init__(self, version=None, attachments=None):
        """NodeTypeDatastores

        The model defined in huaweicloud sdk

        :param version: 内核版本号。
        :type version: str
        :param attachments: 
        :type attachments: :class:`huaweicloudsdkdws.v2.NodeTypeDatastoresAttachments`
        """
        
        

        self._version = None
        self._attachments = None
        self.discriminator = None

        self.version = version
        self.attachments = attachments

    @property
    def version(self):
        """Gets the version of this NodeTypeDatastores.

        内核版本号。

        :return: The version of this NodeTypeDatastores.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NodeTypeDatastores.

        内核版本号。

        :param version: The version of this NodeTypeDatastores.
        :type version: str
        """
        self._version = version

    @property
    def attachments(self):
        """Gets the attachments of this NodeTypeDatastores.

        :return: The attachments of this NodeTypeDatastores.
        :rtype: :class:`huaweicloudsdkdws.v2.NodeTypeDatastoresAttachments`
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this NodeTypeDatastores.

        :param attachments: The attachments of this NodeTypeDatastores.
        :type attachments: :class:`huaweicloudsdkdws.v2.NodeTypeDatastoresAttachments`
        """
        self._attachments = attachments

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
        if not isinstance(other, NodeTypeDatastores):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
