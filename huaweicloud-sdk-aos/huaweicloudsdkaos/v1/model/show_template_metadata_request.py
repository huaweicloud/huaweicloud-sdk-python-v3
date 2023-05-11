# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateMetadataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_request_id': 'str',
        'template_name': 'str',
        'template_id': 'str'
    }

    attribute_map = {
        'client_request_id': 'Client-Request-Id',
        'template_name': 'template_name',
        'template_id': 'template_id'
    }

    def __init__(self, client_request_id=None, template_name=None, template_id=None):
        """ShowTemplateMetadataRequest

        The model defined in huaweicloud sdk

        :param client_request_id: 用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID
        :type client_request_id: str
        :param template_name: 用户希望创建的模板名称
        :type template_name: str
        :param template_id: 模板的ID。当template_id存在时，模板服务会检查template_id是否和template_name匹配，不匹配会返回400
        :type template_id: str
        """
        
        

        self._client_request_id = None
        self._template_name = None
        self._template_id = None
        self.discriminator = None

        self.client_request_id = client_request_id
        self.template_name = template_name
        if template_id is not None:
            self.template_id = template_id

    @property
    def client_request_id(self):
        """Gets the client_request_id of this ShowTemplateMetadataRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :return: The client_request_id of this ShowTemplateMetadataRequest.
        :rtype: str
        """
        return self._client_request_id

    @client_request_id.setter
    def client_request_id(self, client_request_id):
        """Sets the client_request_id of this ShowTemplateMetadataRequest.

        用户指定的，对于此请求的唯一ID，用于定位某个请求，推荐使用UUID

        :param client_request_id: The client_request_id of this ShowTemplateMetadataRequest.
        :type client_request_id: str
        """
        self._client_request_id = client_request_id

    @property
    def template_name(self):
        """Gets the template_name of this ShowTemplateMetadataRequest.

        用户希望创建的模板名称

        :return: The template_name of this ShowTemplateMetadataRequest.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this ShowTemplateMetadataRequest.

        用户希望创建的模板名称

        :param template_name: The template_name of this ShowTemplateMetadataRequest.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def template_id(self):
        """Gets the template_id of this ShowTemplateMetadataRequest.

        模板的ID。当template_id存在时，模板服务会检查template_id是否和template_name匹配，不匹配会返回400

        :return: The template_id of this ShowTemplateMetadataRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this ShowTemplateMetadataRequest.

        模板的ID。当template_id存在时，模板服务会检查template_id是否和template_name匹配，不匹配会返回400

        :param template_id: The template_id of this ShowTemplateMetadataRequest.
        :type template_id: str
        """
        self._template_id = template_id

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
        if not isinstance(other, ShowTemplateMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
