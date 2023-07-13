# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectorOrderRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'url': 'url'
    }

    def __init__(self, instance_id=None, url=None):
        """ConnectorOrderRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: 需要关闭connector的实例id，和请求路径上的一致。
        :type instance_id: str
        :param url: 提交关闭connector订单后前端跳转的页面
        :type url: str
        """
        
        

        self._instance_id = None
        self._url = None
        self.discriminator = None

        self.instance_id = instance_id
        if url is not None:
            self.url = url

    @property
    def instance_id(self):
        """Gets the instance_id of this ConnectorOrderRequestBody.

        需要关闭connector的实例id，和请求路径上的一致。

        :return: The instance_id of this ConnectorOrderRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ConnectorOrderRequestBody.

        需要关闭connector的实例id，和请求路径上的一致。

        :param instance_id: The instance_id of this ConnectorOrderRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def url(self):
        """Gets the url of this ConnectorOrderRequestBody.

        提交关闭connector订单后前端跳转的页面

        :return: The url of this ConnectorOrderRequestBody.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConnectorOrderRequestBody.

        提交关闭connector订单后前端跳转的页面

        :param url: The url of this ConnectorOrderRequestBody.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, ConnectorOrderRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
