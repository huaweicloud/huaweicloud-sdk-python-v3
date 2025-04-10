# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GcbBindingServiceAll:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'binding_service': 'str'
    }

    attribute_map = {
        'binding_service': 'binding_service'
    }

    def __init__(self, binding_service=None):
        r"""GcbBindingServiceAll

        The model defined in huaweicloud sdk

        :param binding_service: 功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型
        :type binding_service: str
        """
        
        

        self._binding_service = None
        self.discriminator = None

        if binding_service is not None:
            self.binding_service = binding_service

    @property
    def binding_service(self):
        r"""Gets the binding_service of this GcbBindingServiceAll.

        功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型

        :return: The binding_service of this GcbBindingServiceAll.
        :rtype: str
        """
        return self._binding_service

    @binding_service.setter
    def binding_service(self, binding_service):
        r"""Sets the binding_service of this GcbBindingServiceAll.

        功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型

        :param binding_service: The binding_service of this GcbBindingServiceAll.
        :type binding_service: str
        """
        self._binding_service = binding_service

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
        if not isinstance(other, GcbBindingServiceAll):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
