# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadBasicPluginRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'plugin_name': 'str',
        'business_type': 'str',
        'body': 'UploadBasicPluginRequestBody'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'plugin_name': 'plugin_name',
        'business_type': 'business_type',
        'body': 'body'
    }

    def __init__(self, domain_id=None, plugin_name=None, business_type=None, body=None):
        """UploadBasicPluginRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param plugin_name: 插件名
        :type plugin_name: str
        :param business_type: 业务类型
        :type business_type: str
        :param body: Body of the UploadBasicPluginRequest
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.UploadBasicPluginRequestBody`
        """
        
        

        self._domain_id = None
        self._plugin_name = None
        self._business_type = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        self.plugin_name = plugin_name
        self.business_type = business_type
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        """Gets the domain_id of this UploadBasicPluginRequest.

        租户ID

        :return: The domain_id of this UploadBasicPluginRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this UploadBasicPluginRequest.

        租户ID

        :param domain_id: The domain_id of this UploadBasicPluginRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def plugin_name(self):
        """Gets the plugin_name of this UploadBasicPluginRequest.

        插件名

        :return: The plugin_name of this UploadBasicPluginRequest.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        """Sets the plugin_name of this UploadBasicPluginRequest.

        插件名

        :param plugin_name: The plugin_name of this UploadBasicPluginRequest.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def business_type(self):
        """Gets the business_type of this UploadBasicPluginRequest.

        业务类型

        :return: The business_type of this UploadBasicPluginRequest.
        :rtype: str
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        """Sets the business_type of this UploadBasicPluginRequest.

        业务类型

        :param business_type: The business_type of this UploadBasicPluginRequest.
        :type business_type: str
        """
        self._business_type = business_type

    @property
    def body(self):
        """Gets the body of this UploadBasicPluginRequest.

        :return: The body of this UploadBasicPluginRequest.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UploadBasicPluginRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UploadBasicPluginRequest.

        :param body: The body of this UploadBasicPluginRequest.
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.UploadBasicPluginRequestBody`
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
        if not isinstance(other, UploadBasicPluginRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
