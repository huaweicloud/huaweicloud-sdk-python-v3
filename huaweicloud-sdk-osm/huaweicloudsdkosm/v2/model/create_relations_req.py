# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRelationsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'related_id_list': 'list[str]',
        'group_id': 'str'
    }

    attribute_map = {
        'related_id_list': 'related_id_list',
        'group_id': 'group_id'
    }

    def __init__(self, related_id_list=None, group_id=None):
        """CreateRelationsReq

        The model defined in huaweicloud sdk

        :param related_id_list: 要关联的工单id列表，最多3个
        :type related_id_list: list[str]
        :param group_id: 组id
        :type group_id: str
        """
        
        

        self._related_id_list = None
        self._group_id = None
        self.discriminator = None

        self.related_id_list = related_id_list
        self.group_id = group_id

    @property
    def related_id_list(self):
        """Gets the related_id_list of this CreateRelationsReq.

        要关联的工单id列表，最多3个

        :return: The related_id_list of this CreateRelationsReq.
        :rtype: list[str]
        """
        return self._related_id_list

    @related_id_list.setter
    def related_id_list(self, related_id_list):
        """Sets the related_id_list of this CreateRelationsReq.

        要关联的工单id列表，最多3个

        :param related_id_list: The related_id_list of this CreateRelationsReq.
        :type related_id_list: list[str]
        """
        self._related_id_list = related_id_list

    @property
    def group_id(self):
        """Gets the group_id of this CreateRelationsReq.

        组id

        :return: The group_id of this CreateRelationsReq.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this CreateRelationsReq.

        组id

        :param group_id: The group_id of this CreateRelationsReq.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, CreateRelationsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
