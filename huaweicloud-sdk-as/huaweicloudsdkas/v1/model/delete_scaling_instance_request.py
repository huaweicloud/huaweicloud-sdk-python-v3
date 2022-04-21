# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteScalingInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_delete': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_delete': 'instance_delete'
    }

    def __init__(self, instance_id=None, instance_delete=None):
        """DeleteScalingInstanceRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID，可参考[查询弹性伸缩组中的实例列表](https://support.huaweicloud.com/api-as/as_06_0301.html)获取。
        :type instance_id: str
        :param instance_delete: 实例移出伸缩组，是否删除云服务器实例。默认为no；可选值为yes或no。
        :type instance_delete: str
        """
        
        

        self._instance_id = None
        self._instance_delete = None
        self.discriminator = None

        self.instance_id = instance_id
        if instance_delete is not None:
            self.instance_delete = instance_delete

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteScalingInstanceRequest.

        实例ID，可参考[查询弹性伸缩组中的实例列表](https://support.huaweicloud.com/api-as/as_06_0301.html)获取。

        :return: The instance_id of this DeleteScalingInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteScalingInstanceRequest.

        实例ID，可参考[查询弹性伸缩组中的实例列表](https://support.huaweicloud.com/api-as/as_06_0301.html)获取。

        :param instance_id: The instance_id of this DeleteScalingInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_delete(self):
        """Gets the instance_delete of this DeleteScalingInstanceRequest.

        实例移出伸缩组，是否删除云服务器实例。默认为no；可选值为yes或no。

        :return: The instance_delete of this DeleteScalingInstanceRequest.
        :rtype: str
        """
        return self._instance_delete

    @instance_delete.setter
    def instance_delete(self, instance_delete):
        """Sets the instance_delete of this DeleteScalingInstanceRequest.

        实例移出伸缩组，是否删除云服务器实例。默认为no；可选值为yes或no。

        :param instance_delete: The instance_delete of this DeleteScalingInstanceRequest.
        :type instance_delete: str
        """
        self._instance_delete = instance_delete

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
        if not isinstance(other, DeleteScalingInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
