# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenericLinkQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_need_total': 'bool',
        'latest_only': 'bool',
        'object_id': 'str',
        'role': 'str'
    }

    attribute_map = {
        'is_need_total': 'isNeedTotal',
        'latest_only': 'latestOnly',
        'object_id': 'objectId',
        'role': 'role'
    }

    def __init__(self, is_need_total=None, latest_only=None, object_id=None, role=None):
        """GenericLinkQueryDTO

        The model defined in huaweicloud sdk

        :param is_need_total: 是否需要查询总记录数。 - true：需要。 - false：不需要。
        :type is_need_total: bool
        :param latest_only: 是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。 - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。默认为false。
        :type latest_only: bool
        :param object_id: 角色对应数据实例ID。
        :type object_id: str
        :param role: 角色。 - TARGET：目标模型。 - SOURCE：源模型。
        :type role: str
        """
        
        

        self._is_need_total = None
        self._latest_only = None
        self._object_id = None
        self._role = None
        self.discriminator = None

        if is_need_total is not None:
            self.is_need_total = is_need_total
        if latest_only is not None:
            self.latest_only = latest_only
        if object_id is not None:
            self.object_id = object_id
        if role is not None:
            self.role = role

    @property
    def is_need_total(self):
        """Gets the is_need_total of this GenericLinkQueryDTO.

        是否需要查询总记录数。 - true：需要。 - false：不需要。

        :return: The is_need_total of this GenericLinkQueryDTO.
        :rtype: bool
        """
        return self._is_need_total

    @is_need_total.setter
    def is_need_total(self, is_need_total):
        """Sets the is_need_total of this GenericLinkQueryDTO.

        是否需要查询总记录数。 - true：需要。 - false：不需要。

        :param is_need_total: The is_need_total of this GenericLinkQueryDTO.
        :type is_need_total: bool
        """
        self._is_need_total = is_need_total

    @property
    def latest_only(self):
        """Gets the latest_only of this GenericLinkQueryDTO.

        是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。 - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。默认为false。

        :return: The latest_only of this GenericLinkQueryDTO.
        :rtype: bool
        """
        return self._latest_only

    @latest_only.setter
    def latest_only(self, latest_only):
        """Sets the latest_only of this GenericLinkQueryDTO.

        是否返回源模型数据实例关联的最新版本目标模型数据实例。此参数仅对源/目标模型为M-V模型实体有效。 - true：返回源模型数据实例关联的最新版本的目标模型数据实例。 - false：返回源模型数据实例关联的所有版本的目标模型数据实例。默认为false。

        :param latest_only: The latest_only of this GenericLinkQueryDTO.
        :type latest_only: bool
        """
        self._latest_only = latest_only

    @property
    def object_id(self):
        """Gets the object_id of this GenericLinkQueryDTO.

        角色对应数据实例ID。

        :return: The object_id of this GenericLinkQueryDTO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this GenericLinkQueryDTO.

        角色对应数据实例ID。

        :param object_id: The object_id of this GenericLinkQueryDTO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def role(self):
        """Gets the role of this GenericLinkQueryDTO.

        角色。 - TARGET：目标模型。 - SOURCE：源模型。

        :return: The role of this GenericLinkQueryDTO.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this GenericLinkQueryDTO.

        角色。 - TARGET：目标模型。 - SOURCE：源模型。

        :param role: The role of this GenericLinkQueryDTO.
        :type role: str
        """
        self._role = role

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
        if not isinstance(other, GenericLinkQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
