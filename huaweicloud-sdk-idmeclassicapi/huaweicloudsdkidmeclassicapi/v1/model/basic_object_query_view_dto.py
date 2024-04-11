# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BasicObjectQueryViewDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'creator': 'str',
        'create_time': 'str',
        'modifier': 'str',
        'last_update_time': 'str',
        'rdm_extension_type': 'str',
        'tenant': 'TenantViewDTO',
        'class_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'creator': 'creator',
        'create_time': 'createTime',
        'modifier': 'modifier',
        'last_update_time': 'lastUpdateTime',
        'rdm_extension_type': 'rdmExtensionType',
        'tenant': 'tenant',
        'class_name': 'className'
    }

    def __init__(self, id=None, creator=None, create_time=None, modifier=None, last_update_time=None, rdm_extension_type=None, tenant=None, class_name=None):
        """BasicObjectQueryViewDTO

        The model defined in huaweicloud sdk

        :param id: 唯一编码。
        :type id: str
        :param creator: 创建者。
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: str
        :param modifier: 修改人。
        :type modifier: str
        :param last_update_time: 最后的修改时间。
        :type last_update_time: str
        :param rdm_extension_type: 扩展类型。
        :type rdm_extension_type: str
        :param tenant: 
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        :param class_name: 类名。
        :type class_name: str
        """
        
        

        self._id = None
        self._creator = None
        self._create_time = None
        self._modifier = None
        self._last_update_time = None
        self._rdm_extension_type = None
        self._tenant = None
        self._class_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if modifier is not None:
            self.modifier = modifier
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if rdm_extension_type is not None:
            self.rdm_extension_type = rdm_extension_type
        if tenant is not None:
            self.tenant = tenant
        if class_name is not None:
            self.class_name = class_name

    @property
    def id(self):
        """Gets the id of this BasicObjectQueryViewDTO.

        唯一编码。

        :return: The id of this BasicObjectQueryViewDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BasicObjectQueryViewDTO.

        唯一编码。

        :param id: The id of this BasicObjectQueryViewDTO.
        :type id: str
        """
        self._id = id

    @property
    def creator(self):
        """Gets the creator of this BasicObjectQueryViewDTO.

        创建者。

        :return: The creator of this BasicObjectQueryViewDTO.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this BasicObjectQueryViewDTO.

        创建者。

        :param creator: The creator of this BasicObjectQueryViewDTO.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this BasicObjectQueryViewDTO.

        创建时间。

        :return: The create_time of this BasicObjectQueryViewDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BasicObjectQueryViewDTO.

        创建时间。

        :param create_time: The create_time of this BasicObjectQueryViewDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def modifier(self):
        """Gets the modifier of this BasicObjectQueryViewDTO.

        修改人。

        :return: The modifier of this BasicObjectQueryViewDTO.
        :rtype: str
        """
        return self._modifier

    @modifier.setter
    def modifier(self, modifier):
        """Sets the modifier of this BasicObjectQueryViewDTO.

        修改人。

        :param modifier: The modifier of this BasicObjectQueryViewDTO.
        :type modifier: str
        """
        self._modifier = modifier

    @property
    def last_update_time(self):
        """Gets the last_update_time of this BasicObjectQueryViewDTO.

        最后的修改时间。

        :return: The last_update_time of this BasicObjectQueryViewDTO.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this BasicObjectQueryViewDTO.

        最后的修改时间。

        :param last_update_time: The last_update_time of this BasicObjectQueryViewDTO.
        :type last_update_time: str
        """
        self._last_update_time = last_update_time

    @property
    def rdm_extension_type(self):
        """Gets the rdm_extension_type of this BasicObjectQueryViewDTO.

        扩展类型。

        :return: The rdm_extension_type of this BasicObjectQueryViewDTO.
        :rtype: str
        """
        return self._rdm_extension_type

    @rdm_extension_type.setter
    def rdm_extension_type(self, rdm_extension_type):
        """Sets the rdm_extension_type of this BasicObjectQueryViewDTO.

        扩展类型。

        :param rdm_extension_type: The rdm_extension_type of this BasicObjectQueryViewDTO.
        :type rdm_extension_type: str
        """
        self._rdm_extension_type = rdm_extension_type

    @property
    def tenant(self):
        """Gets the tenant of this BasicObjectQueryViewDTO.

        :return: The tenant of this BasicObjectQueryViewDTO.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this BasicObjectQueryViewDTO.

        :param tenant: The tenant of this BasicObjectQueryViewDTO.
        :type tenant: :class:`huaweicloudsdkidmeclassicapi.v1.TenantViewDTO`
        """
        self._tenant = tenant

    @property
    def class_name(self):
        """Gets the class_name of this BasicObjectQueryViewDTO.

        类名。

        :return: The class_name of this BasicObjectQueryViewDTO.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this BasicObjectQueryViewDTO.

        类名。

        :param class_name: The class_name of this BasicObjectQueryViewDTO.
        :type class_name: str
        """
        self._class_name = class_name

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
        if not isinstance(other, BasicObjectQueryViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
