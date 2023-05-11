# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DebugApiV2Request:

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
        'api_id': 'str',
        'body': 'ApiDebugInfo'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'api_id': 'api_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, api_id=None, body=None):
        """DebugApiV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，在API网关控制台的“实例信息”中获取。
        :type instance_id: str
        :param api_id: API的编号
        :type api_id: str
        :param body: Body of the DebugApiV2Request
        :type body: :class:`huaweicloudsdkapig.v2.ApiDebugInfo`
        """
        
        

        self._instance_id = None
        self._api_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.api_id = api_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this DebugApiV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :return: The instance_id of this DebugApiV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DebugApiV2Request.

        实例ID，在API网关控制台的“实例信息”中获取。

        :param instance_id: The instance_id of this DebugApiV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def api_id(self):
        """Gets the api_id of this DebugApiV2Request.

        API的编号

        :return: The api_id of this DebugApiV2Request.
        :rtype: str
        """
        return self._api_id

    @api_id.setter
    def api_id(self, api_id):
        """Sets the api_id of this DebugApiV2Request.

        API的编号

        :param api_id: The api_id of this DebugApiV2Request.
        :type api_id: str
        """
        self._api_id = api_id

    @property
    def body(self):
        """Gets the body of this DebugApiV2Request.

        :return: The body of this DebugApiV2Request.
        :rtype: :class:`huaweicloudsdkapig.v2.ApiDebugInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DebugApiV2Request.

        :param body: The body of this DebugApiV2Request.
        :type body: :class:`huaweicloudsdkapig.v2.ApiDebugInfo`
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
        if not isinstance(other, DebugApiV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
