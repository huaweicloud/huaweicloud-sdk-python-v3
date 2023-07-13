# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GatewayDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'apig_type': 'str',
        'apig_instance_id': 'str',
        'group_id_in_apig': 'str',
        'roma_app_id': 'str'
    }

    attribute_map = {
        'apig_type': 'apig_type',
        'apig_instance_id': 'apig_instance_id',
        'group_id_in_apig': 'group_id_in_apig',
        'roma_app_id': 'roma_app_id'
    }

    def __init__(self, apig_type=None, apig_instance_id=None, group_id_in_apig=None, roma_app_id=None):
        """GatewayDTO

        The model defined in huaweicloud sdk

        :param apig_type: 网关类型
        :type apig_type: str
        :param apig_instance_id: 网关实例id
        :type apig_instance_id: str
        :param group_id_in_apig: 网关分组id
        :type group_id_in_apig: str
        :param roma_app_id: roma网关集成应用id
        :type roma_app_id: str
        """
        
        

        self._apig_type = None
        self._apig_instance_id = None
        self._group_id_in_apig = None
        self._roma_app_id = None
        self.discriminator = None

        if apig_type is not None:
            self.apig_type = apig_type
        if apig_instance_id is not None:
            self.apig_instance_id = apig_instance_id
        if group_id_in_apig is not None:
            self.group_id_in_apig = group_id_in_apig
        if roma_app_id is not None:
            self.roma_app_id = roma_app_id

    @property
    def apig_type(self):
        """Gets the apig_type of this GatewayDTO.

        网关类型

        :return: The apig_type of this GatewayDTO.
        :rtype: str
        """
        return self._apig_type

    @apig_type.setter
    def apig_type(self, apig_type):
        """Sets the apig_type of this GatewayDTO.

        网关类型

        :param apig_type: The apig_type of this GatewayDTO.
        :type apig_type: str
        """
        self._apig_type = apig_type

    @property
    def apig_instance_id(self):
        """Gets the apig_instance_id of this GatewayDTO.

        网关实例id

        :return: The apig_instance_id of this GatewayDTO.
        :rtype: str
        """
        return self._apig_instance_id

    @apig_instance_id.setter
    def apig_instance_id(self, apig_instance_id):
        """Sets the apig_instance_id of this GatewayDTO.

        网关实例id

        :param apig_instance_id: The apig_instance_id of this GatewayDTO.
        :type apig_instance_id: str
        """
        self._apig_instance_id = apig_instance_id

    @property
    def group_id_in_apig(self):
        """Gets the group_id_in_apig of this GatewayDTO.

        网关分组id

        :return: The group_id_in_apig of this GatewayDTO.
        :rtype: str
        """
        return self._group_id_in_apig

    @group_id_in_apig.setter
    def group_id_in_apig(self, group_id_in_apig):
        """Sets the group_id_in_apig of this GatewayDTO.

        网关分组id

        :param group_id_in_apig: The group_id_in_apig of this GatewayDTO.
        :type group_id_in_apig: str
        """
        self._group_id_in_apig = group_id_in_apig

    @property
    def roma_app_id(self):
        """Gets the roma_app_id of this GatewayDTO.

        roma网关集成应用id

        :return: The roma_app_id of this GatewayDTO.
        :rtype: str
        """
        return self._roma_app_id

    @roma_app_id.setter
    def roma_app_id(self, roma_app_id):
        """Sets the roma_app_id of this GatewayDTO.

        roma网关集成应用id

        :param roma_app_id: The roma_app_id of this GatewayDTO.
        :type roma_app_id: str
        """
        self._roma_app_id = roma_app_id

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
        if not isinstance(other, GatewayDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
