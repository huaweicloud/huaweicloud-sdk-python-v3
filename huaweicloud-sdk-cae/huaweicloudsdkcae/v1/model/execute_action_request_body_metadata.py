# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteActionRequestBodyMetadata:

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
        """ExecuteActionRequestBodyMetadata

        The model defined in huaweicloud sdk

        :param annotations: 资源信息。
        :type annotations: dict(str, str)
        :param name: action名称，具体action如下。 - deploy：部署。 - upgrade：升级。 - configure：生效配置。 - scale：伸缩。 - restart：重启。 - start：启动。 - stop：停止。 - rollback：回滚。
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
        """Gets the annotations of this ExecuteActionRequestBodyMetadata.

        资源信息。

        :return: The annotations of this ExecuteActionRequestBodyMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ExecuteActionRequestBodyMetadata.

        资源信息。

        :param annotations: The annotations of this ExecuteActionRequestBodyMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def name(self):
        """Gets the name of this ExecuteActionRequestBodyMetadata.

        action名称，具体action如下。 - deploy：部署。 - upgrade：升级。 - configure：生效配置。 - scale：伸缩。 - restart：重启。 - start：启动。 - stop：停止。 - rollback：回滚。

        :return: The name of this ExecuteActionRequestBodyMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ExecuteActionRequestBodyMetadata.

        action名称，具体action如下。 - deploy：部署。 - upgrade：升级。 - configure：生效配置。 - scale：伸缩。 - restart：重启。 - start：启动。 - stop：停止。 - rollback：回滚。

        :param name: The name of this ExecuteActionRequestBodyMetadata.
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
        if not isinstance(other, ExecuteActionRequestBodyMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
