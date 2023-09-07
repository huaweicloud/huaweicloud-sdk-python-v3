# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'params': 'UpdateJob'
    }

    attribute_map = {
        'type': 'type',
        'params': 'params'
    }

    def __init__(self, type=None, params=None):
        """UpdateJobReq

        The model defined in huaweicloud sdk

        :param type: 更新指定ID任务详情类型。  场景一：更新单个任务详情，取值： - name：更新该任务名称。 - description：更新该任务描述。 - re_create：配置中任务三天以后虚拟机删除后重建。 - expired_days：更新任务异常自动结束时间，单位为天。  场景二：更新批量异步任务详情，取值： - all：批量异步创建的任务，参数校验不通过，需要指定全部参数进行更新时。 - network：批量异步创建的任务，测试连接不通过，需要更新源库/目标库信息时。 - policy：批量异步创建的任务，需要更新任务配置时。 - db_object：批量异步创建的任务，需要更新对象信息时。 - precheck：批量异步创建的任务，需要重新预检查时。
        :type type: str
        :param params: 
        :type params: :class:`huaweicloudsdkdrs.v5.UpdateJob`
        """
        
        

        self._type = None
        self._params = None
        self.discriminator = None

        self.type = type
        self.params = params

    @property
    def type(self):
        """Gets the type of this UpdateJobReq.

        更新指定ID任务详情类型。  场景一：更新单个任务详情，取值： - name：更新该任务名称。 - description：更新该任务描述。 - re_create：配置中任务三天以后虚拟机删除后重建。 - expired_days：更新任务异常自动结束时间，单位为天。  场景二：更新批量异步任务详情，取值： - all：批量异步创建的任务，参数校验不通过，需要指定全部参数进行更新时。 - network：批量异步创建的任务，测试连接不通过，需要更新源库/目标库信息时。 - policy：批量异步创建的任务，需要更新任务配置时。 - db_object：批量异步创建的任务，需要更新对象信息时。 - precheck：批量异步创建的任务，需要重新预检查时。

        :return: The type of this UpdateJobReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateJobReq.

        更新指定ID任务详情类型。  场景一：更新单个任务详情，取值： - name：更新该任务名称。 - description：更新该任务描述。 - re_create：配置中任务三天以后虚拟机删除后重建。 - expired_days：更新任务异常自动结束时间，单位为天。  场景二：更新批量异步任务详情，取值： - all：批量异步创建的任务，参数校验不通过，需要指定全部参数进行更新时。 - network：批量异步创建的任务，测试连接不通过，需要更新源库/目标库信息时。 - policy：批量异步创建的任务，需要更新任务配置时。 - db_object：批量异步创建的任务，需要更新对象信息时。 - precheck：批量异步创建的任务，需要重新预检查时。

        :param type: The type of this UpdateJobReq.
        :type type: str
        """
        self._type = type

    @property
    def params(self):
        """Gets the params of this UpdateJobReq.

        :return: The params of this UpdateJobReq.
        :rtype: :class:`huaweicloudsdkdrs.v5.UpdateJob`
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this UpdateJobReq.

        :param params: The params of this UpdateJobReq.
        :type params: :class:`huaweicloudsdkdrs.v5.UpdateJob`
        """
        self._params = params

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
        if not isinstance(other, UpdateJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
