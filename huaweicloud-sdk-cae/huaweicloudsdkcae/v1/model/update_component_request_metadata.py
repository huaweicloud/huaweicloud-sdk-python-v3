# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateComponentRequestMetadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'annotations': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'annotations': 'annotations'
    }

    def __init__(self, name=None, annotations=None):
        r"""UpdateComponentRequestMetadata

        The model defined in huaweicloud sdk

        :param name: 组件名称。
        :type name: str
        :param annotations: 更新组件请求体附加参数，当前只支持version参数，此参数必填。
        :type annotations: dict(str, str)
        """
        
        

        self._name = None
        self._annotations = None
        self.discriminator = None

        self.name = name
        if annotations is not None:
            self.annotations = annotations

    @property
    def name(self):
        r"""Gets the name of this UpdateComponentRequestMetadata.

        组件名称。

        :return: The name of this UpdateComponentRequestMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateComponentRequestMetadata.

        组件名称。

        :param name: The name of this UpdateComponentRequestMetadata.
        :type name: str
        """
        self._name = name

    @property
    def annotations(self):
        r"""Gets the annotations of this UpdateComponentRequestMetadata.

        更新组件请求体附加参数，当前只支持version参数，此参数必填。

        :return: The annotations of this UpdateComponentRequestMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this UpdateComponentRequestMetadata.

        更新组件请求体附加参数，当前只支持version参数，此参数必填。

        :param annotations: The annotations of this UpdateComponentRequestMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

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
        if not isinstance(other, UpdateComponentRequestMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
