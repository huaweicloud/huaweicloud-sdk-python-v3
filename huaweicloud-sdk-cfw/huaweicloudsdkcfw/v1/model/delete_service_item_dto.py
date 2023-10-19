# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteServiceItemDto:

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
        'service_item_ids': 'list[str]'
    }

    attribute_map = {
        'set_id': 'set_id',
        'service_item_ids': 'service_item_ids'
    }

    def __init__(self, set_id=None, service_item_ids=None):
        """DeleteServiceItemDto

        The model defined in huaweicloud sdk

        :param set_id: 服务组id
        :type set_id: str
        :param service_item_ids: 服务组成员id列表
        :type service_item_ids: list[str]
        """
        
        

        self._set_id = None
        self._service_item_ids = None
        self.discriminator = None

        self.set_id = set_id
        self.service_item_ids = service_item_ids

    @property
    def set_id(self):
        """Gets the set_id of this DeleteServiceItemDto.

        服务组id

        :return: The set_id of this DeleteServiceItemDto.
        :rtype: str
        """
        return self._set_id

    @set_id.setter
    def set_id(self, set_id):
        """Sets the set_id of this DeleteServiceItemDto.

        服务组id

        :param set_id: The set_id of this DeleteServiceItemDto.
        :type set_id: str
        """
        self._set_id = set_id

    @property
    def service_item_ids(self):
        """Gets the service_item_ids of this DeleteServiceItemDto.

        服务组成员id列表

        :return: The service_item_ids of this DeleteServiceItemDto.
        :rtype: list[str]
        """
        return self._service_item_ids

    @service_item_ids.setter
    def service_item_ids(self, service_item_ids):
        """Sets the service_item_ids of this DeleteServiceItemDto.

        服务组成员id列表

        :param service_item_ids: The service_item_ids of this DeleteServiceItemDto.
        :type service_item_ids: list[str]
        """
        self._service_item_ids = service_item_ids

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
        if not isinstance(other, DeleteServiceItemDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
