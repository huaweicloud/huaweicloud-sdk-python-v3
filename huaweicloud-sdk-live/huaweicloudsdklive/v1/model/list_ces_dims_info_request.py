# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCesDimsInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str'
    }

    attribute_map = {
        'namespace': 'namespace'
    }

    def __init__(self, namespace=None):
        r"""ListCesDimsInfoRequest

        The model defined in huaweicloud sdk

        :param namespace: 命名空间，如 SYS.LIVE，与服务上报指标时使用的namespace一致。
        :type namespace: str
        """
        
        

        self._namespace = None
        self.discriminator = None

        self.namespace = namespace

    @property
    def namespace(self):
        r"""Gets the namespace of this ListCesDimsInfoRequest.

        命名空间，如 SYS.LIVE，与服务上报指标时使用的namespace一致。

        :return: The namespace of this ListCesDimsInfoRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListCesDimsInfoRequest.

        命名空间，如 SYS.LIVE，与服务上报指标时使用的namespace一致。

        :param namespace: The namespace of this ListCesDimsInfoRequest.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, ListCesDimsInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
