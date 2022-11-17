# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[ShowInstanceResp]',
        'instance_num': 'int'
    }

    attribute_map = {
        'instances': 'instances',
        'instance_num': 'instance_num'
    }

    def __init__(self, instances=None, instance_num=None):
        """ListInstancesResponse

        The model defined in huaweicloud sdk

        :param instances: 实例列表
        :type instances: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceResp`]
        :param instance_num: 实例数量。
        :type instance_num: int
        """
        
        super(ListInstancesResponse, self).__init__()

        self._instances = None
        self._instance_num = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if instance_num is not None:
            self.instance_num = instance_num

    @property
    def instances(self):
        """Gets the instances of this ListInstancesResponse.

        实例列表

        :return: The instances of this ListInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceResp`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ListInstancesResponse.

        实例列表

        :param instances: The instances of this ListInstancesResponse.
        :type instances: list[:class:`huaweicloudsdkkafka.v2.ShowInstanceResp`]
        """
        self._instances = instances

    @property
    def instance_num(self):
        """Gets the instance_num of this ListInstancesResponse.

        实例数量。

        :return: The instance_num of this ListInstancesResponse.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        """Sets the instance_num of this ListInstancesResponse.

        实例数量。

        :param instance_num: The instance_num of this ListInstancesResponse.
        :type instance_num: int
        """
        self._instance_num = instance_num

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
        if not isinstance(other, ListInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
