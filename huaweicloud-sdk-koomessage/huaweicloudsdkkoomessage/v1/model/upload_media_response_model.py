# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadMediaResponseModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'int',
        'resource_id': 'str',
        'resource_url': 'str'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'resource_url': 'resource_url'
    }

    def __init__(self, resource_type=None, resource_id=None, resource_url=None):
        """UploadMediaResponseModel

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。 - 1：图片 
        :type resource_type: int
        :param resource_id: 资源ID。
        :type resource_id: str
        :param resource_url: 资源路径。
        :type resource_url: str
        """
        
        

        self._resource_type = None
        self._resource_id = None
        self._resource_url = None
        self.discriminator = None

        if resource_type is not None:
            self.resource_type = resource_type
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_url is not None:
            self.resource_url = resource_url

    @property
    def resource_type(self):
        """Gets the resource_type of this UploadMediaResponseModel.

        资源类型。 - 1：图片 

        :return: The resource_type of this UploadMediaResponseModel.
        :rtype: int
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this UploadMediaResponseModel.

        资源类型。 - 1：图片 

        :param resource_type: The resource_type of this UploadMediaResponseModel.
        :type resource_type: int
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this UploadMediaResponseModel.

        资源ID。

        :return: The resource_id of this UploadMediaResponseModel.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this UploadMediaResponseModel.

        资源ID。

        :param resource_id: The resource_id of this UploadMediaResponseModel.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def resource_url(self):
        """Gets the resource_url of this UploadMediaResponseModel.

        资源路径。

        :return: The resource_url of this UploadMediaResponseModel.
        :rtype: str
        """
        return self._resource_url

    @resource_url.setter
    def resource_url(self, resource_url):
        """Sets the resource_url of this UploadMediaResponseModel.

        资源路径。

        :param resource_url: The resource_url of this UploadMediaResponseModel.
        :type resource_url: str
        """
        self._resource_url = resource_url

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
        if not isinstance(other, UploadMediaResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
