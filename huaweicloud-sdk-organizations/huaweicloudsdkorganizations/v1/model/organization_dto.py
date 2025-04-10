# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationDto:

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
        'urn': 'str',
        'management_account_id': 'str',
        'management_account_name': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'management_account_id': 'management_account_id',
        'management_account_name': 'management_account_name',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, urn=None, management_account_id=None, management_account_name=None, created_at=None):
        r"""OrganizationDto

        The model defined in huaweicloud sdk

        :param id: 组织的唯一标识符（ID）。
        :type id: str
        :param urn: 组织的统一资源名称。
        :type urn: str
        :param management_account_id: 组织管理账号的唯一标识符（ID）。
        :type management_account_id: str
        :param management_account_name: 组织的管理账号的名称。
        :type management_account_name: str
        :param created_at: 组织的创建时间。
        :type created_at: datetime
        """
        
        

        self._id = None
        self._urn = None
        self._management_account_id = None
        self._management_account_name = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.urn = urn
        self.management_account_id = management_account_id
        self.management_account_name = management_account_name
        self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this OrganizationDto.

        组织的唯一标识符（ID）。

        :return: The id of this OrganizationDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OrganizationDto.

        组织的唯一标识符（ID）。

        :param id: The id of this OrganizationDto.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this OrganizationDto.

        组织的统一资源名称。

        :return: The urn of this OrganizationDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this OrganizationDto.

        组织的统一资源名称。

        :param urn: The urn of this OrganizationDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def management_account_id(self):
        r"""Gets the management_account_id of this OrganizationDto.

        组织管理账号的唯一标识符（ID）。

        :return: The management_account_id of this OrganizationDto.
        :rtype: str
        """
        return self._management_account_id

    @management_account_id.setter
    def management_account_id(self, management_account_id):
        r"""Sets the management_account_id of this OrganizationDto.

        组织管理账号的唯一标识符（ID）。

        :param management_account_id: The management_account_id of this OrganizationDto.
        :type management_account_id: str
        """
        self._management_account_id = management_account_id

    @property
    def management_account_name(self):
        r"""Gets the management_account_name of this OrganizationDto.

        组织的管理账号的名称。

        :return: The management_account_name of this OrganizationDto.
        :rtype: str
        """
        return self._management_account_name

    @management_account_name.setter
    def management_account_name(self, management_account_name):
        r"""Sets the management_account_name of this OrganizationDto.

        组织的管理账号的名称。

        :param management_account_name: The management_account_name of this OrganizationDto.
        :type management_account_name: str
        """
        self._management_account_name = management_account_name

    @property
    def created_at(self):
        r"""Gets the created_at of this OrganizationDto.

        组织的创建时间。

        :return: The created_at of this OrganizationDto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this OrganizationDto.

        组织的创建时间。

        :param created_at: The created_at of this OrganizationDto.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, OrganizationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
