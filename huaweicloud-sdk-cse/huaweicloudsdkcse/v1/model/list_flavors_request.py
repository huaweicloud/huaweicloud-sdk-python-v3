# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlavorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_type': 'str'
    }

    attribute_map = {
        'spec_type': 'spec_type'
    }

    def __init__(self, spec_type=None):
        """ListFlavorsRequest

        The model defined in huaweicloud sdk

        :param spec_type: 微服务引擎专享版应用部署类型，查询CSE微服务引擎专享版需要将该值设置为CSE2。
        :type spec_type: str
        """
        
        

        self._spec_type = None
        self.discriminator = None

        if spec_type is not None:
            self.spec_type = spec_type

    @property
    def spec_type(self):
        """Gets the spec_type of this ListFlavorsRequest.

        微服务引擎专享版应用部署类型，查询CSE微服务引擎专享版需要将该值设置为CSE2。

        :return: The spec_type of this ListFlavorsRequest.
        :rtype: str
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        """Sets the spec_type of this ListFlavorsRequest.

        微服务引擎专享版应用部署类型，查询CSE微服务引擎专享版需要将该值设置为CSE2。

        :param spec_type: The spec_type of this ListFlavorsRequest.
        :type spec_type: str
        """
        self._spec_type = spec_type

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
        if not isinstance(other, ListFlavorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
