# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadResourcesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'body': 'UploadPackageGroupReq'
    }

    attribute_map = {
        'user_id': 'USER-ID',
        'body': 'body'
    }

    def __init__(self, user_id=None, body=None):
        """UploadResourcesRequest

        The model defined in huaweicloud sdk

        :param user_id: 
        :type user_id: str
        :param body: Body of the UploadResourcesRequest
        :type body: :class:`huaweicloudsdkdli.v1.UploadPackageGroupReq`
        """
        
        

        self._user_id = None
        self._body = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def user_id(self):
        """Gets the user_id of this UploadResourcesRequest.

        :return: The user_id of this UploadResourcesRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UploadResourcesRequest.

        :param user_id: The user_id of this UploadResourcesRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        """Gets the body of this UploadResourcesRequest.

        :return: The body of this UploadResourcesRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.UploadPackageGroupReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadResourcesRequest.

        :param body: The body of this UploadResourcesRequest.
        :type body: :class:`huaweicloudsdkdli.v1.UploadPackageGroupReq`
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
        if not isinstance(other, UploadResourcesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
