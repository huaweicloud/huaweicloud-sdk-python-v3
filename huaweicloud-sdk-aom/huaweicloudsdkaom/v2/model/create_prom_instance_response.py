# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePromInstanceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prometheus': 'list[PromInstanceEpsCreateModel]'
    }

    attribute_map = {
        'prometheus': 'prometheus'
    }

    def __init__(self, prometheus=None):
        r"""CreatePromInstanceResponse

        The model defined in huaweicloud sdk

        :param prometheus: Prometheus实例名称列表。
        :type prometheus: list[:class:`huaweicloudsdkaom.v2.PromInstanceEpsCreateModel`]
        """
        
        super(CreatePromInstanceResponse, self).__init__()

        self._prometheus = None
        self.discriminator = None

        if prometheus is not None:
            self.prometheus = prometheus

    @property
    def prometheus(self):
        r"""Gets the prometheus of this CreatePromInstanceResponse.

        Prometheus实例名称列表。

        :return: The prometheus of this CreatePromInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkaom.v2.PromInstanceEpsCreateModel`]
        """
        return self._prometheus

    @prometheus.setter
    def prometheus(self, prometheus):
        r"""Sets the prometheus of this CreatePromInstanceResponse.

        Prometheus实例名称列表。

        :param prometheus: The prometheus of this CreatePromInstanceResponse.
        :type prometheus: list[:class:`huaweicloudsdkaom.v2.PromInstanceEpsCreateModel`]
        """
        self._prometheus = prometheus

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
        if not isinstance(other, CreatePromInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
