# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddServiceSetUsingPOSTRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'object_id': 'object_id',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, object_id=None, name=None, description=None):
        """AddServiceSetUsingPOSTRequestBody

        The model defined in huaweicloud sdk

        :param object_id: 互联网边界防护对象id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，type为0的为互联网边界防护对象id。
        :type object_id: str
        :param name: 服务组名称
        :type name: str
        :param description: 服务组描述信息
        :type description: str
        """
        
        

        self._object_id = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.object_id = object_id
        self.name = name
        if description is not None:
            self.description = description

    @property
    def object_id(self):
        """Gets the object_id of this AddServiceSetUsingPOSTRequestBody.

        互联网边界防护对象id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，type为0的为互联网边界防护对象id。

        :return: The object_id of this AddServiceSetUsingPOSTRequestBody.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this AddServiceSetUsingPOSTRequestBody.

        互联网边界防护对象id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，type为0的为互联网边界防护对象id。

        :param object_id: The object_id of this AddServiceSetUsingPOSTRequestBody.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def name(self):
        """Gets the name of this AddServiceSetUsingPOSTRequestBody.

        服务组名称

        :return: The name of this AddServiceSetUsingPOSTRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddServiceSetUsingPOSTRequestBody.

        服务组名称

        :param name: The name of this AddServiceSetUsingPOSTRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this AddServiceSetUsingPOSTRequestBody.

        服务组描述信息

        :return: The description of this AddServiceSetUsingPOSTRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddServiceSetUsingPOSTRequestBody.

        服务组描述信息

        :param description: The description of this AddServiceSetUsingPOSTRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AddServiceSetUsingPOSTRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
