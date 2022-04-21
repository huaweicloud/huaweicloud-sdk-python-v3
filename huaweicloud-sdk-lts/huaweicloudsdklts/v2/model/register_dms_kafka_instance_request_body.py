# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RegisterDmsKafkaInstanceRequestBody:

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
        'kafka_name': 'str',
        'connect_info': 'RegisterDmsKafkaInstanceRequestBodyConnectInfo'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'kafka_name': 'kafka_name',
        'connect_info': 'connect_info'
    }

    def __init__(self, instance_id=None, kafka_name=None, connect_info=None):
        """RegisterDmsKafkaInstanceRequestBody

        The model defined in huaweicloud sdk

        :param instance_id: kafka ID
        :type instance_id: str
        :param kafka_name: kafka 名称
        :type kafka_name: str
        :param connect_info: 
        :type connect_info: :class:`huaweicloudsdklts.v2.RegisterDmsKafkaInstanceRequestBodyConnectInfo`
        """
        
        

        self._instance_id = None
        self._kafka_name = None
        self._connect_info = None
        self.discriminator = None

        self.instance_id = instance_id
        self.kafka_name = kafka_name
        self.connect_info = connect_info

    @property
    def instance_id(self):
        """Gets the instance_id of this RegisterDmsKafkaInstanceRequestBody.

        kafka ID

        :return: The instance_id of this RegisterDmsKafkaInstanceRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this RegisterDmsKafkaInstanceRequestBody.

        kafka ID

        :param instance_id: The instance_id of this RegisterDmsKafkaInstanceRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def kafka_name(self):
        """Gets the kafka_name of this RegisterDmsKafkaInstanceRequestBody.

        kafka 名称

        :return: The kafka_name of this RegisterDmsKafkaInstanceRequestBody.
        :rtype: str
        """
        return self._kafka_name

    @kafka_name.setter
    def kafka_name(self, kafka_name):
        """Sets the kafka_name of this RegisterDmsKafkaInstanceRequestBody.

        kafka 名称

        :param kafka_name: The kafka_name of this RegisterDmsKafkaInstanceRequestBody.
        :type kafka_name: str
        """
        self._kafka_name = kafka_name

    @property
    def connect_info(self):
        """Gets the connect_info of this RegisterDmsKafkaInstanceRequestBody.


        :return: The connect_info of this RegisterDmsKafkaInstanceRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.RegisterDmsKafkaInstanceRequestBodyConnectInfo`
        """
        return self._connect_info

    @connect_info.setter
    def connect_info(self, connect_info):
        """Sets the connect_info of this RegisterDmsKafkaInstanceRequestBody.


        :param connect_info: The connect_info of this RegisterDmsKafkaInstanceRequestBody.
        :type connect_info: :class:`huaweicloudsdklts.v2.RegisterDmsKafkaInstanceRequestBodyConnectInfo`
        """
        self._connect_info = connect_info

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
        if not isinstance(other, RegisterDmsKafkaInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
