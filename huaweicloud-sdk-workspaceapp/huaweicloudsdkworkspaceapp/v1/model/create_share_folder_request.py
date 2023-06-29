# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShareFolderRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_id': 'str',
        'body': 'CreateShareFolderReq'
    }

    attribute_map = {
        'storage_id': 'storage_id',
        'body': 'body'
    }

    def __init__(self, storage_id=None, body=None):
        """CreateShareFolderRequest

        The model defined in huaweicloud sdk

        :param storage_id: WKS存储ID
        :type storage_id: str
        :param body: Body of the CreateShareFolderRequest
        :type body: :class:`huaweicloudsdkworkspaceapp.v1.CreateShareFolderReq`
        """
        
        

        self._storage_id = None
        self._body = None
        self.discriminator = None

        self.storage_id = storage_id
        if body is not None:
            self.body = body

    @property
    def storage_id(self):
        """Gets the storage_id of this CreateShareFolderRequest.

        WKS存储ID

        :return: The storage_id of this CreateShareFolderRequest.
        :rtype: str
        """
        return self._storage_id

    @storage_id.setter
    def storage_id(self, storage_id):
        """Sets the storage_id of this CreateShareFolderRequest.

        WKS存储ID

        :param storage_id: The storage_id of this CreateShareFolderRequest.
        :type storage_id: str
        """
        self._storage_id = storage_id

    @property
    def body(self):
        """Gets the body of this CreateShareFolderRequest.

        :return: The body of this CreateShareFolderRequest.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.CreateShareFolderReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateShareFolderRequest.

        :param body: The body of this CreateShareFolderRequest.
        :type body: :class:`huaweicloudsdkworkspaceapp.v1.CreateShareFolderReq`
        """
        self._body = body

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
        if not isinstance(other, CreateShareFolderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
