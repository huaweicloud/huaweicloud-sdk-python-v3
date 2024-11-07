# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteFunctionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('sp_auth_token')
    sensitive_list.append('stage_auth_token')

    openapi_types = {
        'instance_id': 'str',
        'sp_auth_token': 'str',
        'stage_auth_token': 'str',
        'function_id': 'str'
    }

    attribute_map = {
        'instance_id': 'Instance-Id',
        'sp_auth_token': 'Sp-Auth-Token',
        'stage_auth_token': 'Stage-Auth-Token',
        'function_id': 'function_id'
    }

    def __init__(self, instance_id=None, sp_auth_token=None, stage_auth_token=None, function_id=None):
        """DeleteFunctionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。
        :type instance_id: str
        :param sp_auth_token: **参数说明**：Sp用户Token。通过调用IoBPS服务获取SP用户Token。
        :type sp_auth_token: str
        :param stage_auth_token: **参数说明**：Stage用户的Token, 仅提供给IoStage服务使用。
        :type stage_auth_token: str
        :param function_id: **参数说明**：函数ID。
        :type function_id: str
        """
        
        

        self._instance_id = None
        self._sp_auth_token = None
        self._stage_auth_token = None
        self._function_id = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if sp_auth_token is not None:
            self.sp_auth_token = sp_auth_token
        if stage_auth_token is not None:
            self.stage_auth_token = stage_auth_token
        self.function_id = function_id

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteFunctionsRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :return: The instance_id of this DeleteFunctionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteFunctionsRequest.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，建议携带该参数，在使用专业版时必须携带该参数。您可以在IoTDA管理控制台界面，选择左侧导航栏“总览”页签查看当前实例的ID，具体获取方式请参考[[查看实例详情](https://support.huaweicloud.com/usermanual-iothub/iot_01_0079.html#section1)](tag:hws) [[查看实例详情](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0079.html#section1)](tag:hws_hk)。

        :param instance_id: The instance_id of this DeleteFunctionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def sp_auth_token(self):
        """Gets the sp_auth_token of this DeleteFunctionsRequest.

        **参数说明**：Sp用户Token。通过调用IoBPS服务获取SP用户Token。

        :return: The sp_auth_token of this DeleteFunctionsRequest.
        :rtype: str
        """
        return self._sp_auth_token

    @sp_auth_token.setter
    def sp_auth_token(self, sp_auth_token):
        """Sets the sp_auth_token of this DeleteFunctionsRequest.

        **参数说明**：Sp用户Token。通过调用IoBPS服务获取SP用户Token。

        :param sp_auth_token: The sp_auth_token of this DeleteFunctionsRequest.
        :type sp_auth_token: str
        """
        self._sp_auth_token = sp_auth_token

    @property
    def stage_auth_token(self):
        """Gets the stage_auth_token of this DeleteFunctionsRequest.

        **参数说明**：Stage用户的Token, 仅提供给IoStage服务使用。

        :return: The stage_auth_token of this DeleteFunctionsRequest.
        :rtype: str
        """
        return self._stage_auth_token

    @stage_auth_token.setter
    def stage_auth_token(self, stage_auth_token):
        """Sets the stage_auth_token of this DeleteFunctionsRequest.

        **参数说明**：Stage用户的Token, 仅提供给IoStage服务使用。

        :param stage_auth_token: The stage_auth_token of this DeleteFunctionsRequest.
        :type stage_auth_token: str
        """
        self._stage_auth_token = stage_auth_token

    @property
    def function_id(self):
        """Gets the function_id of this DeleteFunctionsRequest.

        **参数说明**：函数ID。

        :return: The function_id of this DeleteFunctionsRequest.
        :rtype: str
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """Sets the function_id of this DeleteFunctionsRequest.

        **参数说明**：函数ID。

        :param function_id: The function_id of this DeleteFunctionsRequest.
        :type function_id: str
        """
        self._function_id = function_id

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
        if not isinstance(other, DeleteFunctionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
