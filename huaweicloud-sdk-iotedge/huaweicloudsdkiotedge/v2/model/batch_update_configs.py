# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateConfigs:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'product_id': 'str',
        'app_id': 'str',
        'protocol_mapping': 'object',
        'instance_id': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'app_id': 'app_id',
        'protocol_mapping': 'protocol_mapping',
        'instance_id': 'instance_id'
    }

    def __init__(self, product_id=None, app_id=None, protocol_mapping=None, instance_id=None):
        """BatchUpdateConfigs - a model defined in huaweicloud sdk"""
        
        

        self._product_id = None
        self._app_id = None
        self._protocol_mapping = None
        self._instance_id = None
        self.discriminator = None

        self.product_id = product_id
        if app_id is not None:
            self.app_id = app_id
        self.protocol_mapping = protocol_mapping
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def product_id(self):
        """Gets the product_id of this BatchUpdateConfigs.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :return: The product_id of this BatchUpdateConfigs.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this BatchUpdateConfigs.

        设备关联的产品ID，用于唯一标识一个产品模型，在管理门户导入产品模型后由平台分配获得。

        :param product_id: The product_id of this BatchUpdateConfigs.
        :type: str
        """
        self._product_id = product_id

    @property
    def app_id(self):
        """Gets the app_id of this BatchUpdateConfigs.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定归属到哪个资源空间下，否则将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this BatchUpdateConfigs.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this BatchUpdateConfigs.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定归属到哪个资源空间下，否则将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this BatchUpdateConfigs.
        :type: str
        """
        self._app_id = app_id

    @property
    def protocol_mapping(self):
        """Gets the protocol_mapping of this BatchUpdateConfigs.

        设备协议配置数据。

        :return: The protocol_mapping of this BatchUpdateConfigs.
        :rtype: object
        """
        return self._protocol_mapping

    @protocol_mapping.setter
    def protocol_mapping(self, protocol_mapping):
        """Sets the protocol_mapping of this BatchUpdateConfigs.

        设备协议配置数据。

        :param protocol_mapping: The protocol_mapping of this BatchUpdateConfigs.
        :type: object
        """
        self._protocol_mapping = protocol_mapping

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchUpdateConfigs.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :return: The instance_id of this BatchUpdateConfigs.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchUpdateConfigs.

        **参数说明**：实例ID。物理多租下各实例的唯一标识，一般华为云租户无需携带该参数，仅在物理多租场景下从管理面访问API时需要携带该参数。

        :param instance_id: The instance_id of this BatchUpdateConfigs.
        :type: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, BatchUpdateConfigs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
