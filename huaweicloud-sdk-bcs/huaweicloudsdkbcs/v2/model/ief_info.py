# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IefInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'deploy_mode': 'int'
    }

    attribute_map = {
        'deploy_mode': 'deploy_mode'
    }

    def __init__(self, deploy_mode=None):
        r"""IefInfo

        The model defined in huaweicloud sdk

        :param deploy_mode: BCS服务边缘节点部署模式，分为：随机模式（0），绑定模式（1）
        :type deploy_mode: int
        """
        
        

        self._deploy_mode = None
        self.discriminator = None

        if deploy_mode is not None:
            self.deploy_mode = deploy_mode

    @property
    def deploy_mode(self):
        r"""Gets the deploy_mode of this IefInfo.

        BCS服务边缘节点部署模式，分为：随机模式（0），绑定模式（1）

        :return: The deploy_mode of this IefInfo.
        :rtype: int
        """
        return self._deploy_mode

    @deploy_mode.setter
    def deploy_mode(self, deploy_mode):
        r"""Sets the deploy_mode of this IefInfo.

        BCS服务边缘节点部署模式，分为：随机模式（0），绑定模式（1）

        :param deploy_mode: The deploy_mode of this IefInfo.
        :type deploy_mode: int
        """
        self._deploy_mode = deploy_mode

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
        if not isinstance(other, IefInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
