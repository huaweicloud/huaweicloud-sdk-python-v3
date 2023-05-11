# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateElasticResourcePoolRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'elastic_resource_pool_name': 'str',
        'body': 'UpdateElasticResourcePoolRequestBody'
    }

    attribute_map = {
        'elastic_resource_pool_name': 'elastic_resource_pool_name',
        'body': 'body'
    }

    def __init__(self, elastic_resource_pool_name=None, body=None):
        """UpdateElasticResourcePoolRequest

        The model defined in huaweicloud sdk

        :param elastic_resource_pool_name: 弹性资源池名称
        :type elastic_resource_pool_name: str
        :param body: Body of the UpdateElasticResourcePoolRequest
        :type body: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolRequestBody`
        """
        
        

        self._elastic_resource_pool_name = None
        self._body = None
        self.discriminator = None

        self.elastic_resource_pool_name = elastic_resource_pool_name
        if body is not None:
            self.body = body

    @property
    def elastic_resource_pool_name(self):
        """Gets the elastic_resource_pool_name of this UpdateElasticResourcePoolRequest.

        弹性资源池名称

        :return: The elastic_resource_pool_name of this UpdateElasticResourcePoolRequest.
        :rtype: str
        """
        return self._elastic_resource_pool_name

    @elastic_resource_pool_name.setter
    def elastic_resource_pool_name(self, elastic_resource_pool_name):
        """Sets the elastic_resource_pool_name of this UpdateElasticResourcePoolRequest.

        弹性资源池名称

        :param elastic_resource_pool_name: The elastic_resource_pool_name of this UpdateElasticResourcePoolRequest.
        :type elastic_resource_pool_name: str
        """
        self._elastic_resource_pool_name = elastic_resource_pool_name

    @property
    def body(self):
        """Gets the body of this UpdateElasticResourcePoolRequest.

        :return: The body of this UpdateElasticResourcePoolRequest.
        :rtype: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateElasticResourcePoolRequest.

        :param body: The body of this UpdateElasticResourcePoolRequest.
        :type body: :class:`huaweicloudsdkdli.v1.UpdateElasticResourcePoolRequestBody`
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
        if not isinstance(other, UpdateElasticResourcePoolRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
