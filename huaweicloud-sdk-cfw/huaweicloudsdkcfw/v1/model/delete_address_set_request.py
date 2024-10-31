# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAddressSetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'set_id': 'str',
        'enterprise_project_id': 'str',
        'fw_instance_id': 'str'
    }

    attribute_map = {
        'set_id': 'set_id',
        'enterprise_project_id': 'enterprise_project_id',
        'fw_instance_id': 'fw_instance_id'
    }

    def __init__(self, set_id=None, enterprise_project_id=None, fw_instance_id=None):
        """DeleteAddressSetRequest

        The model defined in huaweicloud sdk

        :param set_id: 地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。
        :type set_id: str
        :param enterprise_project_id: 企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0
        :type enterprise_project_id: str
        :param fw_instance_id: 防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        """
        
        

        self._set_id = None
        self._enterprise_project_id = None
        self._fw_instance_id = None
        self.discriminator = None

        self.set_id = set_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id

    @property
    def set_id(self):
        """Gets the set_id of this DeleteAddressSetRequest.

        地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :return: The set_id of this DeleteAddressSetRequest.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this DeleteAddressSetRequest.

        地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :param set_id: The set_id of this DeleteAddressSetRequest.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this DeleteAddressSetRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :return: The enterprise_project_id of this DeleteAddressSetRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this DeleteAddressSetRequest.

        企业项目ID，用户根据组织规划企业项目，对应的ID为企业项目ID，可通过[如何获取企业项目ID](cfw_02_0027.xml)获取，用户未开启企业项目时为0

        :param enterprise_project_id: The enterprise_project_id of this DeleteAddressSetRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this DeleteAddressSetRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this DeleteAddressSetRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this DeleteAddressSetRequest.

        防火墙id，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this DeleteAddressSetRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

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
        if not isinstance(other, DeleteAddressSetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
