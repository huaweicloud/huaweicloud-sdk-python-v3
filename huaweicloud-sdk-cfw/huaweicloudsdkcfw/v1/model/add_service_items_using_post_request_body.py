# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddServiceItemsUsingPOSTRequestBody:

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
        'service_items': 'list[AddServiceItemsUsingPOSTRequestBodyServiceItems]'
    }

    attribute_map = {
        'set_id': 'set_id',
        'service_items': 'service_items'
    }

    def __init__(self, set_id=None, service_items=None):
        r"""AddServiceItemsUsingPOSTRequestBody

        The model defined in huaweicloud sdk

        :param set_id: 服务组id，可通过[获取服务组列表接口](ListServiceSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。
        :type set_id: str
        :param service_items: 服务组成员列表
        :type service_items: list[:class:`huaweicloudsdkcfw.v1.AddServiceItemsUsingPOSTRequestBodyServiceItems`]
        """
        
        

        self._set_id = None
        self._service_items = None
        self.discriminator = None

        self.set_id = set_id
        self.service_items = service_items

    @property
    def set_id(self):
        r"""Gets the set_id of this AddServiceItemsUsingPOSTRequestBody.

        服务组id，可通过[获取服务组列表接口](ListServiceSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :return: The set_id of this AddServiceItemsUsingPOSTRequestBody.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        r"""Sets the set_id of this AddServiceItemsUsingPOSTRequestBody.

        服务组id，可通过[获取服务组列表接口](ListServiceSets.xml)查询获得，通过返回值中的data.records.set_id（.表示各对象之间层级的区分）获得。

        :param set_id: The set_id of this AddServiceItemsUsingPOSTRequestBody.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def service_items(self):
        r"""Gets the service_items of this AddServiceItemsUsingPOSTRequestBody.

        服务组成员列表

        :return: The service_items of this AddServiceItemsUsingPOSTRequestBody.
        :rtype: list[:class:`huaweicloudsdkcfw.v1.AddServiceItemsUsingPOSTRequestBodyServiceItems`]
        """
        return self._service_items

    @service_items.setter
    def service_items(self, service_items):
        r"""Sets the service_items of this AddServiceItemsUsingPOSTRequestBody.

        服务组成员列表

        :param service_items: The service_items of this AddServiceItemsUsingPOSTRequestBody.
        :type service_items: list[:class:`huaweicloudsdkcfw.v1.AddServiceItemsUsingPOSTRequestBodyServiceItems`]
        """
        self._service_items = service_items

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
        if not isinstance(other, AddServiceItemsUsingPOSTRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
