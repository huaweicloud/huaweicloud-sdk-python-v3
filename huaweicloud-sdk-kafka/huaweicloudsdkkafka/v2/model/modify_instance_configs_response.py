# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyInstanceConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'dynamic_config': 'int',
        'static_config': 'int'
    }

    attribute_map = {
        'job_id': 'job_id',
        'dynamic_config': 'dynamic_config',
        'static_config': 'static_config'
    }

    def __init__(self, job_id=None, dynamic_config=None, static_config=None):
        """ModifyInstanceConfigsResponse

        The model defined in huaweicloud sdk

        :param job_id: 配置修改任务ID。
        :type job_id: str
        :param dynamic_config: 本次修改动态配置参数个数。
        :type dynamic_config: int
        :param static_config: 本次修改静态配置参数个数。
        :type static_config: int
        """
        
        super(ModifyInstanceConfigsResponse, self).__init__()

        self._job_id = None
        self._dynamic_config = None
        self._static_config = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if dynamic_config is not None:
            self.dynamic_config = dynamic_config
        if static_config is not None:
            self.static_config = static_config

    @property
    def job_id(self):
        """Gets the job_id of this ModifyInstanceConfigsResponse.

        配置修改任务ID。

        :return: The job_id of this ModifyInstanceConfigsResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ModifyInstanceConfigsResponse.

        配置修改任务ID。

        :param job_id: The job_id of this ModifyInstanceConfigsResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def dynamic_config(self):
        """Gets the dynamic_config of this ModifyInstanceConfigsResponse.

        本次修改动态配置参数个数。

        :return: The dynamic_config of this ModifyInstanceConfigsResponse.
        :rtype: int
        """
        return self._dynamic_config

    @dynamic_config.setter
    def dynamic_config(self, dynamic_config):
        """Sets the dynamic_config of this ModifyInstanceConfigsResponse.

        本次修改动态配置参数个数。

        :param dynamic_config: The dynamic_config of this ModifyInstanceConfigsResponse.
        :type dynamic_config: int
        """
        self._dynamic_config = dynamic_config

    @property
    def static_config(self):
        """Gets the static_config of this ModifyInstanceConfigsResponse.

        本次修改静态配置参数个数。

        :return: The static_config of this ModifyInstanceConfigsResponse.
        :rtype: int
        """
        return self._static_config

    @static_config.setter
    def static_config(self, static_config):
        """Sets the static_config of this ModifyInstanceConfigsResponse.

        本次修改静态配置参数个数。

        :param static_config: The static_config of this ModifyInstanceConfigsResponse.
        :type static_config: int
        """
        self._static_config = static_config

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
        if not isinstance(other, ModifyInstanceConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
