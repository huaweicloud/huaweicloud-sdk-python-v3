# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ScalingInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_name': 'str',
        'instance_id': 'str',
        'failed_reason': 'str',
        'failed_details': 'str',
        'instance_config': 'str'
    }

    attribute_map = {
        'instance_name': 'instance_name',
        'instance_id': 'instance_id',
        'failed_reason': 'failed_reason',
        'failed_details': 'failed_details',
        'instance_config': 'instance_config'
    }

    def __init__(self, instance_name=None, instance_id=None, failed_reason=None, failed_details=None, instance_config=None):
        """ScalingInstance

        The model defined in huaweicloud sdk

        :param instance_name: 云服务器名称。
        :type instance_name: str
        :param instance_id: 云服务器id。
        :type instance_id: str
        :param failed_reason: 实例伸缩失败原因。
        :type failed_reason: str
        :param failed_details: 实例伸缩失败详情。
        :type failed_details: str
        :param instance_config: 实例配置信息。
        :type instance_config: str
        """
        
        

        self._instance_name = None
        self._instance_id = None
        self._failed_reason = None
        self._failed_details = None
        self._instance_config = None
        self.discriminator = None

        if instance_name is not None:
            self.instance_name = instance_name
        if instance_id is not None:
            self.instance_id = instance_id
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if failed_details is not None:
            self.failed_details = failed_details
        if instance_config is not None:
            self.instance_config = instance_config

    @property
    def instance_name(self):
        """Gets the instance_name of this ScalingInstance.

        云服务器名称。

        :return: The instance_name of this ScalingInstance.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this ScalingInstance.

        云服务器名称。

        :param instance_name: The instance_name of this ScalingInstance.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ScalingInstance.

        云服务器id。

        :return: The instance_id of this ScalingInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ScalingInstance.

        云服务器id。

        :param instance_id: The instance_id of this ScalingInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def failed_reason(self):
        """Gets the failed_reason of this ScalingInstance.

        实例伸缩失败原因。

        :return: The failed_reason of this ScalingInstance.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this ScalingInstance.

        实例伸缩失败原因。

        :param failed_reason: The failed_reason of this ScalingInstance.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def failed_details(self):
        """Gets the failed_details of this ScalingInstance.

        实例伸缩失败详情。

        :return: The failed_details of this ScalingInstance.
        :rtype: str
        """
        return self._failed_details

    @failed_details.setter
    def failed_details(self, failed_details):
        """Sets the failed_details of this ScalingInstance.

        实例伸缩失败详情。

        :param failed_details: The failed_details of this ScalingInstance.
        :type failed_details: str
        """
        self._failed_details = failed_details

    @property
    def instance_config(self):
        """Gets the instance_config of this ScalingInstance.

        实例配置信息。

        :return: The instance_config of this ScalingInstance.
        :rtype: str
        """
        return self._instance_config

    @instance_config.setter
    def instance_config(self, instance_config):
        """Sets the instance_config of this ScalingInstance.

        实例配置信息。

        :param instance_config: The instance_config of this ScalingInstance.
        :type instance_config: str
        """
        self._instance_config = instance_config

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
        if not isinstance(other, ScalingInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
