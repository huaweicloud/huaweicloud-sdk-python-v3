# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type_name': 'str',
        'urn_template': 'str'
    }

    attribute_map = {
        'type_name': 'type_name',
        'urn_template': 'urn_template'
    }

    def __init__(self, type_name=None, urn_template=None):
        r"""Resource

        The model defined in huaweicloud sdk

        :param type_name: 云服务资源类型名称。
        :type type_name: str
        :param urn_template: 统一资源名称模板，表示可以通过这类资源的统一资源名称对该授权项进行资源粒度的授权。
        :type urn_template: str
        """
        
        

        self._type_name = None
        self._urn_template = None
        self.discriminator = None

        self.type_name = type_name
        self.urn_template = urn_template

    @property
    def type_name(self):
        r"""Gets the type_name of this Resource.

        云服务资源类型名称。

        :return: The type_name of this Resource.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        r"""Sets the type_name of this Resource.

        云服务资源类型名称。

        :param type_name: The type_name of this Resource.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def urn_template(self):
        r"""Gets the urn_template of this Resource.

        统一资源名称模板，表示可以通过这类资源的统一资源名称对该授权项进行资源粒度的授权。

        :return: The urn_template of this Resource.
        :rtype: str
        """
        return self._urn_template

    @urn_template.setter
    def urn_template(self, urn_template):
        r"""Sets the urn_template of this Resource.

        统一资源名称模板，表示可以通过这类资源的统一资源名称对该授权项进行资源粒度的授权。

        :param urn_template: The urn_template of this Resource.
        :type urn_template: str
        """
        self._urn_template = urn_template

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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
