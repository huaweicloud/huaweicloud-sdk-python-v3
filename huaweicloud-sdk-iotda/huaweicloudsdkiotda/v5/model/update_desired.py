# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDesired:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'service_id': 'str',
        'desired': 'object',
        'version': 'int'
    }

    attribute_map = {
        'service_id': 'service_id',
        'desired': 'desired',
        'version': 'version'
    }

    def __init__(self, service_id=None, desired=None, version=None):
        """UpdateDesired

        The model defined in huaweicloud sdk

        :param service_id: **参数说明**：设备的服务ID，在设备关联的产品模型中定义。
        :type service_id: str
        :param desired: **参数说明**：设备影子期望属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构；如果想要删除整个desired可以填写空Object(例如\&quot;desired\&quot;:{})，如果想要删除某一个属性期望值可以将属性置位null(例如{\&quot;temperature\&quot;:null})
        :type desired: object
        :param version: **参数说明**：设备影子的版本，携带该参数时平台会校验值必须等于当前影子版本，初始从0开始。
        :type version: int
        """
        
        

        self._service_id = None
        self._desired = None
        self._version = None
        self.discriminator = None

        self.service_id = service_id
        self.desired = desired
        if version is not None:
            self.version = version

    @property
    def service_id(self):
        """Gets the service_id of this UpdateDesired.

        **参数说明**：设备的服务ID，在设备关联的产品模型中定义。

        :return: The service_id of this UpdateDesired.
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this UpdateDesired.

        **参数说明**：设备的服务ID，在设备关联的产品模型中定义。

        :param service_id: The service_id of this UpdateDesired.
        :type service_id: str
        """
        self._service_id = service_id

    @property
    def desired(self):
        """Gets the desired of this UpdateDesired.

        **参数说明**：设备影子期望属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构；如果想要删除整个desired可以填写空Object(例如\"desired\":{})，如果想要删除某一个属性期望值可以将属性置位null(例如{\"temperature\":null})

        :return: The desired of this UpdateDesired.
        :rtype: object
        """
        return self._desired

    @desired.setter
    def desired(self, desired):
        """Sets the desired of this UpdateDesired.

        **参数说明**：设备影子期望属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构；如果想要删除整个desired可以填写空Object(例如\"desired\":{})，如果想要删除某一个属性期望值可以将属性置位null(例如{\"temperature\":null})

        :param desired: The desired of this UpdateDesired.
        :type desired: object
        """
        self._desired = desired

    @property
    def version(self):
        """Gets the version of this UpdateDesired.

        **参数说明**：设备影子的版本，携带该参数时平台会校验值必须等于当前影子版本，初始从0开始。

        :return: The version of this UpdateDesired.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UpdateDesired.

        **参数说明**：设备影子的版本，携带该参数时平台会校验值必须等于当前影子版本，初始从0开始。

        :param version: The version of this UpdateDesired.
        :type version: int
        """
        self._version = version

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
        if not isinstance(other, UpdateDesired):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
