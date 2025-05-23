# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadPluginIconRequest:

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
        'body': 'UploadPluginIconRequestBody'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'plugin_name': 'plugin_name',
        'body': 'body'
    }

    def __init__(self, domain_id=None, plugin_name=None, body=None):
        r"""UploadPluginIconRequest

        The model defined in huaweicloud sdk

        :param domain_id: 租户ID
        :type domain_id: str
        :param plugin_name: 
        :type plugin_name: str
        :param body: Body of the UploadPluginIconRequest
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPluginIconRequestBody`
        """
        
        

        self._domain_id = None
        self._plugin_name = None
        self._body = None
        self.discriminator = None

        self.domain_id = domain_id
        self.plugin_name = plugin_name
        if body is not None:
            self.body = body

    @property
    def domain_id(self):
        r"""Gets the domain_id of this UploadPluginIconRequest.

        租户ID

        :return: The domain_id of this UploadPluginIconRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this UploadPluginIconRequest.

        租户ID

        :param domain_id: The domain_id of this UploadPluginIconRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this UploadPluginIconRequest.

        :return: The plugin_name of this UploadPluginIconRequest.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this UploadPluginIconRequest.

        :param plugin_name: The plugin_name of this UploadPluginIconRequest.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def body(self):
        r"""Gets the body of this UploadPluginIconRequest.

        :return: The body of this UploadPluginIconRequest.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPluginIconRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UploadPluginIconRequest.

        :param body: The body of this UploadPluginIconRequest.
        :type body: :class:`huaweicloudsdkcodeartspipeline.v2.UploadPluginIconRequestBody`
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
        if not isinstance(other, UploadPluginIconRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
