# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLifeCycleHookRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'scaling_group_id': 'str',
        'lifecycle_hook_name': 'str'
    }

    attribute_map = {
        'scaling_group_id': 'scaling_group_id',
        'lifecycle_hook_name': 'lifecycle_hook_name'
    }

    def __init__(self, scaling_group_id=None, lifecycle_hook_name=None):
        """ShowLifeCycleHookRequest

        The model defined in huaweicloud sdk

        :param scaling_group_id: 伸缩组标识。
        :type scaling_group_id: str
        :param lifecycle_hook_name: 生命周期挂钩标识。
        :type lifecycle_hook_name: str
        """
        
        

        self._scaling_group_id = None
        self._lifecycle_hook_name = None
        self.discriminator = None

        self.scaling_group_id = scaling_group_id
        self.lifecycle_hook_name = lifecycle_hook_name

    @property
    def scaling_group_id(self):
        """Gets the scaling_group_id of this ShowLifeCycleHookRequest.

        伸缩组标识。

        :return: The scaling_group_id of this ShowLifeCycleHookRequest.
        :rtype: str
        """
        return self._scaling_group_id

    @scaling_group_id.setter
    def scaling_group_id(self, scaling_group_id):
        """Sets the scaling_group_id of this ShowLifeCycleHookRequest.

        伸缩组标识。

        :param scaling_group_id: The scaling_group_id of this ShowLifeCycleHookRequest.
        :type scaling_group_id: str
        """
        self._scaling_group_id = scaling_group_id

    @property
    def lifecycle_hook_name(self):
        """Gets the lifecycle_hook_name of this ShowLifeCycleHookRequest.

        生命周期挂钩标识。

        :return: The lifecycle_hook_name of this ShowLifeCycleHookRequest.
        :rtype: str
        """
        return self._lifecycle_hook_name

    @lifecycle_hook_name.setter
    def lifecycle_hook_name(self, lifecycle_hook_name):
        """Sets the lifecycle_hook_name of this ShowLifeCycleHookRequest.

        生命周期挂钩标识。

        :param lifecycle_hook_name: The lifecycle_hook_name of this ShowLifeCycleHookRequest.
        :type lifecycle_hook_name: str
        """
        self._lifecycle_hook_name = lifecycle_hook_name

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
        if not isinstance(other, ShowLifeCycleHookRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
