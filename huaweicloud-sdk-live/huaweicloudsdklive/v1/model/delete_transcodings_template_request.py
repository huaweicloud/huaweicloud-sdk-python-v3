# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTranscodingsTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'app_name': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'app_name': 'app_name'
    }

    def __init__(self, domain=None, app_name=None):
        r"""DeleteTranscodingsTemplateRequest

        The model defined in huaweicloud sdk

        :param domain: 推流域名
        :type domain: str
        :param app_name: 应用名称
        :type app_name: str
        """
        
        

        self._domain = None
        self._app_name = None
        self.discriminator = None

        self.domain = domain
        self.app_name = app_name

    @property
    def domain(self):
        r"""Gets the domain of this DeleteTranscodingsTemplateRequest.

        推流域名

        :return: The domain of this DeleteTranscodingsTemplateRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this DeleteTranscodingsTemplateRequest.

        推流域名

        :param domain: The domain of this DeleteTranscodingsTemplateRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def app_name(self):
        r"""Gets the app_name of this DeleteTranscodingsTemplateRequest.

        应用名称

        :return: The app_name of this DeleteTranscodingsTemplateRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this DeleteTranscodingsTemplateRequest.

        应用名称

        :param app_name: The app_name of this DeleteTranscodingsTemplateRequest.
        :type app_name: str
        """
        self._app_name = app_name

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
        if not isinstance(other, DeleteTranscodingsTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
