# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEnvironmentRequestBodyMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'annotations': 'dict(str, str)',
        'name': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'name': 'name'
    }

    def __init__(self, annotations=None, name=None):
        r"""CreateEnvironmentRequestBodyMetadata

        The model defined in huaweicloud sdk

        :param annotations: 创建环境请求体附加参数。 - vpc_id：创建环境绑定的VPC的ID。 - group_name：创建环境绑定的SWR组织的组织名称。 - type：环境类型，当前仅支持exclusive类型。 - subnet_id: 创建环境绑定的VPC子网的ID。 - security_group_id：创建环境绑定的安全组的ID，可不填，不填由CAE后台自动创建。
        :type annotations: dict(str, str)
        :param name: 环境名称。
        :type name: str
        """
        
        

        self._annotations = None
        self._name = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        self.name = name

    @property
    def annotations(self):
        r"""Gets the annotations of this CreateEnvironmentRequestBodyMetadata.

        创建环境请求体附加参数。 - vpc_id：创建环境绑定的VPC的ID。 - group_name：创建环境绑定的SWR组织的组织名称。 - type：环境类型，当前仅支持exclusive类型。 - subnet_id: 创建环境绑定的VPC子网的ID。 - security_group_id：创建环境绑定的安全组的ID，可不填，不填由CAE后台自动创建。

        :return: The annotations of this CreateEnvironmentRequestBodyMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this CreateEnvironmentRequestBodyMetadata.

        创建环境请求体附加参数。 - vpc_id：创建环境绑定的VPC的ID。 - group_name：创建环境绑定的SWR组织的组织名称。 - type：环境类型，当前仅支持exclusive类型。 - subnet_id: 创建环境绑定的VPC子网的ID。 - security_group_id：创建环境绑定的安全组的ID，可不填，不填由CAE后台自动创建。

        :param annotations: The annotations of this CreateEnvironmentRequestBodyMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def name(self):
        r"""Gets the name of this CreateEnvironmentRequestBodyMetadata.

        环境名称。

        :return: The name of this CreateEnvironmentRequestBodyMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateEnvironmentRequestBodyMetadata.

        环境名称。

        :param name: The name of this CreateEnvironmentRequestBodyMetadata.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, CreateEnvironmentRequestBodyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
