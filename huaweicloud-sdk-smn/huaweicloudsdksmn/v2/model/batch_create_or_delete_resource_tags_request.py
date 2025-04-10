# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateOrDeleteResourceTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'resource_id': 'str',
        'body': 'BatchCreateOrDeleteResourceTagsRequestBody'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'body': 'body'
    }

    def __init__(self, resource_type=None, resource_id=None, body=None):
        r"""BatchCreateOrDeleteResourceTagsRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型，目前有:  smn_topic，主题  smn_sms，短信  smn_application，移动推送
        :type resource_type: str
        :param resource_id: 资源ID。  获取resource_id的方法：  当resource_type为“smn_topic”时， 手动添加请求消息头“X-SMN-RESOURCEID-TYPE&#x3D;name”，资源ID即为topic名称。 不添加请求消息头，通过“查询资源实例”，获取资源ID。 当resource_type为“smn_sms”时，resource_id为签名ID。您可在控制台获取。
        :type resource_id: str
        :param body: Body of the BatchCreateOrDeleteResourceTagsRequest
        :type body: :class:`huaweicloudsdksmn.v2.BatchCreateOrDeleteResourceTagsRequestBody`
        """
        
        

        self._resource_type = None
        self._resource_id = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        self.resource_id = resource_id
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        r"""Gets the resource_type of this BatchCreateOrDeleteResourceTagsRequest.

        资源类型，目前有:  smn_topic，主题  smn_sms，短信  smn_application，移动推送

        :return: The resource_type of this BatchCreateOrDeleteResourceTagsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this BatchCreateOrDeleteResourceTagsRequest.

        资源类型，目前有:  smn_topic，主题  smn_sms，短信  smn_application，移动推送

        :param resource_type: The resource_type of this BatchCreateOrDeleteResourceTagsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        r"""Gets the resource_id of this BatchCreateOrDeleteResourceTagsRequest.

        资源ID。  获取resource_id的方法：  当resource_type为“smn_topic”时， 手动添加请求消息头“X-SMN-RESOURCEID-TYPE=name”，资源ID即为topic名称。 不添加请求消息头，通过“查询资源实例”，获取资源ID。 当resource_type为“smn_sms”时，resource_id为签名ID。您可在控制台获取。

        :return: The resource_id of this BatchCreateOrDeleteResourceTagsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this BatchCreateOrDeleteResourceTagsRequest.

        资源ID。  获取resource_id的方法：  当resource_type为“smn_topic”时， 手动添加请求消息头“X-SMN-RESOURCEID-TYPE=name”，资源ID即为topic名称。 不添加请求消息头，通过“查询资源实例”，获取资源ID。 当resource_type为“smn_sms”时，resource_id为签名ID。您可在控制台获取。

        :param resource_id: The resource_id of this BatchCreateOrDeleteResourceTagsRequest.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateOrDeleteResourceTagsRequest.

        :return: The body of this BatchCreateOrDeleteResourceTagsRequest.
        :rtype: :class:`huaweicloudsdksmn.v2.BatchCreateOrDeleteResourceTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateOrDeleteResourceTagsRequest.

        :param body: The body of this BatchCreateOrDeleteResourceTagsRequest.
        :type body: :class:`huaweicloudsdksmn.v2.BatchCreateOrDeleteResourceTagsRequestBody`
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
        if not isinstance(other, BatchCreateOrDeleteResourceTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
