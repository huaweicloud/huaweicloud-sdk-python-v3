# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KafkaContentRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connection_type': 'str',
        'instance_id': 'str',
        'vpcep_infos': 'list[VpcepInfoRsp]',
        'broker_infos': 'list[KafkaBrokerInfo]',
        'auth_info': 'KafkaAuthInfo'
    }

    attribute_map = {
        'connection_type': 'connection_type',
        'instance_id': 'instance_id',
        'vpcep_infos': 'vpcep_infos',
        'broker_infos': 'broker_infos',
        'auth_info': 'auth_info'
    }

    def __init__(self, connection_type=None, instance_id=None, vpcep_infos=None, broker_infos=None, auth_info=None):
        r"""KafkaContentRsp

        The model defined in huaweicloud sdk

        :param connection_type: KAFKA连接类型
        :type connection_type: str
        :param instance_id: Kafka实例ID
        :type instance_id: str
        :param vpcep_infos: Kafka的VPCEP信息包括service_id,service_name,client_port
        :type vpcep_infos: list[:class:`huaweicloudsdkiotanalytics.v1.VpcepInfoRsp`]
        :param broker_infos: Kafka的broker信息包括broker_ip, broker_port
        :type broker_infos: list[:class:`huaweicloudsdkiotanalytics.v1.KafkaBrokerInfo`]
        :param auth_info: 
        :type auth_info: :class:`huaweicloudsdkiotanalytics.v1.KafkaAuthInfo`
        """
        
        

        self._connection_type = None
        self._instance_id = None
        self._vpcep_infos = None
        self._broker_infos = None
        self._auth_info = None
        self.discriminator = None

        if connection_type is not None:
            self.connection_type = connection_type
        if instance_id is not None:
            self.instance_id = instance_id
        if vpcep_infos is not None:
            self.vpcep_infos = vpcep_infos
        if broker_infos is not None:
            self.broker_infos = broker_infos
        if auth_info is not None:
            self.auth_info = auth_info

    @property
    def connection_type(self):
        r"""Gets the connection_type of this KafkaContentRsp.

        KAFKA连接类型

        :return: The connection_type of this KafkaContentRsp.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        r"""Sets the connection_type of this KafkaContentRsp.

        KAFKA连接类型

        :param connection_type: The connection_type of this KafkaContentRsp.
        :type connection_type: str
        """
        self._connection_type = connection_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this KafkaContentRsp.

        Kafka实例ID

        :return: The instance_id of this KafkaContentRsp.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this KafkaContentRsp.

        Kafka实例ID

        :param instance_id: The instance_id of this KafkaContentRsp.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def vpcep_infos(self):
        r"""Gets the vpcep_infos of this KafkaContentRsp.

        Kafka的VPCEP信息包括service_id,service_name,client_port

        :return: The vpcep_infos of this KafkaContentRsp.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.VpcepInfoRsp`]
        """
        return self._vpcep_infos

    @vpcep_infos.setter
    def vpcep_infos(self, vpcep_infos):
        r"""Sets the vpcep_infos of this KafkaContentRsp.

        Kafka的VPCEP信息包括service_id,service_name,client_port

        :param vpcep_infos: The vpcep_infos of this KafkaContentRsp.
        :type vpcep_infos: list[:class:`huaweicloudsdkiotanalytics.v1.VpcepInfoRsp`]
        """
        self._vpcep_infos = vpcep_infos

    @property
    def broker_infos(self):
        r"""Gets the broker_infos of this KafkaContentRsp.

        Kafka的broker信息包括broker_ip, broker_port

        :return: The broker_infos of this KafkaContentRsp.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.KafkaBrokerInfo`]
        """
        return self._broker_infos

    @broker_infos.setter
    def broker_infos(self, broker_infos):
        r"""Sets the broker_infos of this KafkaContentRsp.

        Kafka的broker信息包括broker_ip, broker_port

        :param broker_infos: The broker_infos of this KafkaContentRsp.
        :type broker_infos: list[:class:`huaweicloudsdkiotanalytics.v1.KafkaBrokerInfo`]
        """
        self._broker_infos = broker_infos

    @property
    def auth_info(self):
        r"""Gets the auth_info of this KafkaContentRsp.

        :return: The auth_info of this KafkaContentRsp.
        :rtype: :class:`huaweicloudsdkiotanalytics.v1.KafkaAuthInfo`
        """
        return self._auth_info

    @auth_info.setter
    def auth_info(self, auth_info):
        r"""Sets the auth_info of this KafkaContentRsp.

        :param auth_info: The auth_info of this KafkaContentRsp.
        :type auth_info: :class:`huaweicloudsdkiotanalytics.v1.KafkaAuthInfo`
        """
        self._auth_info = auth_info

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
        if not isinstance(other, KafkaContentRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
