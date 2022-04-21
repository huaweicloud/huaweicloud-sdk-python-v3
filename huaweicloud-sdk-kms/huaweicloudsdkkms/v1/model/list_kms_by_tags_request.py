# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKmsByTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_instances': 'str',
        'version_id': 'str',
        'body': 'ListKmsByTagsRequestBody'
    }

    attribute_map = {
        'resource_instances': 'resource_instances',
        'version_id': 'version_id',
        'body': 'body'
    }

    def __init__(self, resource_instances=None, version_id=None, body=None):
        """ListKmsByTagsRequest

        The model defined in huaweicloud sdk

        :param resource_instances: 资源实例
        :type resource_instances: str
        :param version_id: API版本号
        :type version_id: str
        :param body: Body of the ListKmsByTagsRequest
        :type body: :class:`huaweicloudsdkkms.v1.ListKmsByTagsRequestBody`
        """
        
        

        self._resource_instances = None
        self._version_id = None
        self._body = None
        self.discriminator = None

        self.resource_instances = resource_instances
        self.version_id = version_id
        if body is not None:
            self.body = body

    @property
    def resource_instances(self):
        """Gets the resource_instances of this ListKmsByTagsRequest.

        资源实例

        :return: The resource_instances of this ListKmsByTagsRequest.
        :rtype: str
        """
        return self._resource_instances

    @resource_instances.setter
    def resource_instances(self, resource_instances):
        """Sets the resource_instances of this ListKmsByTagsRequest.

        资源实例

        :param resource_instances: The resource_instances of this ListKmsByTagsRequest.
        :type resource_instances: str
        """
        self._resource_instances = resource_instances

    @property
    def version_id(self):
        """Gets the version_id of this ListKmsByTagsRequest.

        API版本号

        :return: The version_id of this ListKmsByTagsRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this ListKmsByTagsRequest.

        API版本号

        :param version_id: The version_id of this ListKmsByTagsRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def body(self):
        """Gets the body of this ListKmsByTagsRequest.


        :return: The body of this ListKmsByTagsRequest.
        :rtype: :class:`huaweicloudsdkkms.v1.ListKmsByTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListKmsByTagsRequest.


        :param body: The body of this ListKmsByTagsRequest.
        :type body: :class:`huaweicloudsdkkms.v1.ListKmsByTagsRequestBody`
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
        if not isinstance(other, ListKmsByTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
