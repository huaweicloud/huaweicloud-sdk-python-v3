# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAttachmentsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'resource_uri': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'resource_uri': 'resource_uri',
        'resource_type': 'resource_type'
    }

    def __init__(self, project_id=None, resource_uri=None, resource_type=None):
        """ListAttachmentsRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目ID，固定长度32位字符（字母和数字）。
        :type project_id: str
        :param resource_uri: 资源Uri
        :type resource_uri: str
        :param resource_type: 资源类型
        :type resource_type: str
        """
        
        

        self._project_id = None
        self._resource_uri = None
        self._resource_type = None
        self.discriminator = None

        self.project_id = project_id
        self.resource_uri = resource_uri
        self.resource_type = resource_type

    @property
    def project_id(self):
        """Gets the project_id of this ListAttachmentsRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :return: The project_id of this ListAttachmentsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListAttachmentsRequest.

        项目ID，固定长度32位字符（字母和数字）。

        :param project_id: The project_id of this ListAttachmentsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_uri(self):
        """Gets the resource_uri of this ListAttachmentsRequest.

        资源Uri

        :return: The resource_uri of this ListAttachmentsRequest.
        :rtype: str
        """
        return self._resource_uri

    @resource_uri.setter
    def resource_uri(self, resource_uri):
        """Sets the resource_uri of this ListAttachmentsRequest.

        资源Uri

        :param resource_uri: The resource_uri of this ListAttachmentsRequest.
        :type resource_uri: str
        """
        self._resource_uri = resource_uri

    @property
    def resource_type(self):
        """Gets the resource_type of this ListAttachmentsRequest.

        资源类型

        :return: The resource_type of this ListAttachmentsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListAttachmentsRequest.

        资源类型

        :param resource_type: The resource_type of this ListAttachmentsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, ListAttachmentsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
