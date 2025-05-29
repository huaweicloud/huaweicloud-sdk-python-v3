# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObjectInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'fw_instance_id': 'str',
        'item_id': 'str',
        'set_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'fw_instance_id': 'fw_instance_id',
        'item_id': 'item_id',
        'set_id': 'set_id',
        'type': 'type'
    }

    def __init__(self, description=None, fw_instance_id=None, item_id=None, set_id=None, type=None):
        r"""ObjectInfoDto

        The model defined in huaweicloud sdk

        :param description: 成员描述
        :type description: str
        :param fw_instance_id: 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param item_id: 成员id，地址组成员id，可通过[查询地址组成员接口](ListAddressItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。服务组成员id，可通过[查询服务成员列表接口](ListServiceItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。域名id可通过[获取域名组下域名列表接口](ListDomains.xml)查询获得，通过返回值中的data.records.domain_address_id（.表示各对象之间层级的区分）获得。
        :type item_id: str
        :param set_id: 组id，地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。服务组id，可通过[获取服务组列表接口](ListServiceSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。域名组id，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。
        :type set_id: str
        :param type: 组类型，包含：地址组ADDR_SET，服务组SERV_SET，域名组DOMAIN_SET，URL组URL_SET
        :type type: str
        """
        
        

        self._description = None
        self._fw_instance_id = None
        self._item_id = None
        self._set_id = None
        self._type = None
        self.discriminator = None

        self.description = description
        self.fw_instance_id = fw_instance_id
        self.item_id = item_id
        self.set_id = set_id
        self.type = type

    @property
    def description(self):
        r"""Gets the description of this ObjectInfoDto.

        成员描述

        :return: The description of this ObjectInfoDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ObjectInfoDto.

        成员描述

        :param description: The description of this ObjectInfoDto.
        :type description: str
        """
        self._description = description

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ObjectInfoDto.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ObjectInfoDto.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ObjectInfoDto.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ObjectInfoDto.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def item_id(self):
        r"""Gets the item_id of this ObjectInfoDto.

        成员id，地址组成员id，可通过[查询地址组成员接口](ListAddressItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。服务组成员id，可通过[查询服务成员列表接口](ListServiceItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。域名id可通过[获取域名组下域名列表接口](ListDomains.xml)查询获得，通过返回值中的data.records.domain_address_id（.表示各对象之间层级的区分）获得。

        :return: The item_id of this ObjectInfoDto.
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        r"""Sets the item_id of this ObjectInfoDto.

        成员id，地址组成员id，可通过[查询地址组成员接口](ListAddressItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。服务组成员id，可通过[查询服务成员列表接口](ListServiceItems.xml)查询获得，通过返回值中的data.records.item_id（.表示各对象之间层级的区分）获得。域名id可通过[获取域名组下域名列表接口](ListDomains.xml)查询获得，通过返回值中的data.records.domain_address_id（.表示各对象之间层级的区分）获得。

        :param item_id: The item_id of this ObjectInfoDto.
        :type item_id: str
        """
        self._item_id = item_id

    @property
    def set_id(self):
        r"""Gets the set_id of this ObjectInfoDto.

        组id，地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。服务组id，可通过[获取服务组列表接口](ListServiceSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。域名组id，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :return: The set_id of this ObjectInfoDto.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this ObjectInfoDto.

        组id，地址组id，可通过[查询地址组列表接口](ListAddressSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。服务组id，可通过[获取服务组列表接口](ListServiceSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。域名组id，可通过[查询域名组列表接口](ListDomainSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :param set_id: The set_id of this ObjectInfoDto.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def type(self):
        r"""Gets the type of this ObjectInfoDto.

        组类型，包含：地址组ADDR_SET，服务组SERV_SET，域名组DOMAIN_SET，URL组URL_SET

        :return: The type of this ObjectInfoDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ObjectInfoDto.

        组类型，包含：地址组ADDR_SET，服务组SERV_SET，域名组DOMAIN_SET，URL组URL_SET

        :param type: The type of this ObjectInfoDto.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ObjectInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
