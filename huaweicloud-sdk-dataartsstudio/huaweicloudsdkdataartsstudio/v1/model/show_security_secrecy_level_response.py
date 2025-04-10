# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecuritySecrecyLevelResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secrecy_level_id': 'str',
        'secrecy_level_name': 'str',
        'secrecy_level_number': 'int',
        'description': 'str',
        'created_by': 'str',
        'created_at': 'int',
        'updated_by': 'str',
        'updated_at': 'int',
        'instance_id': 'str'
    }

    attribute_map = {
        'secrecy_level_id': 'secrecy_level_id',
        'secrecy_level_name': 'secrecy_level_name',
        'secrecy_level_number': 'secrecy_level_number',
        'description': 'description',
        'created_by': 'created_by',
        'created_at': 'created_at',
        'updated_by': 'updated_by',
        'updated_at': 'updated_at',
        'instance_id': 'instance_id'
    }

    def __init__(self, secrecy_level_id=None, secrecy_level_name=None, secrecy_level_number=None, description=None, created_by=None, created_at=None, updated_by=None, updated_at=None, instance_id=None):
        r"""ShowSecuritySecrecyLevelResponse

        The model defined in huaweicloud sdk

        :param secrecy_level_id: 密级id
        :type secrecy_level_id: str
        :param secrecy_level_name: 密级名称
        :type secrecy_level_name: str
        :param secrecy_level_number: 密级等级
        :type secrecy_level_number: int
        :param description: 密级描述
        :type description: str
        :param created_by: 创建者
        :type created_by: str
        :param created_at: 创建时间
        :type created_at: int
        :param updated_by: 更新者
        :type updated_by: str
        :param updated_at: 更新时间
        :type updated_at: int
        :param instance_id: DataArts实例ID
        :type instance_id: str
        """
        
        super(ShowSecuritySecrecyLevelResponse, self).__init__()

        self._secrecy_level_id = None
        self._secrecy_level_name = None
        self._secrecy_level_number = None
        self._description = None
        self._created_by = None
        self._created_at = None
        self._updated_by = None
        self._updated_at = None
        self._instance_id = None
        self.discriminator = None

        if secrecy_level_id is not None:
            self.secrecy_level_id = secrecy_level_id
        if secrecy_level_name is not None:
            self.secrecy_level_name = secrecy_level_name
        if secrecy_level_number is not None:
            self.secrecy_level_number = secrecy_level_number
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_at is not None:
            self.updated_at = updated_at
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def secrecy_level_id(self):
        r"""Gets the secrecy_level_id of this ShowSecuritySecrecyLevelResponse.

        密级id

        :return: The secrecy_level_id of this ShowSecuritySecrecyLevelResponse.
        :rtype: str
        """
        return self._secrecy_level_id

    @secrecy_level_id.setter
    def secrecy_level_id(self, secrecy_level_id):
        r"""Sets the secrecy_level_id of this ShowSecuritySecrecyLevelResponse.

        密级id

        :param secrecy_level_id: The secrecy_level_id of this ShowSecuritySecrecyLevelResponse.
        :type secrecy_level_id: str
        """
        self._secrecy_level_id = secrecy_level_id

    @property
    def secrecy_level_name(self):
        r"""Gets the secrecy_level_name of this ShowSecuritySecrecyLevelResponse.

        密级名称

        :return: The secrecy_level_name of this ShowSecuritySecrecyLevelResponse.
        :rtype: str
        """
        return self._secrecy_level_name

    @secrecy_level_name.setter
    def secrecy_level_name(self, secrecy_level_name):
        r"""Sets the secrecy_level_name of this ShowSecuritySecrecyLevelResponse.

        密级名称

        :param secrecy_level_name: The secrecy_level_name of this ShowSecuritySecrecyLevelResponse.
        :type secrecy_level_name: str
        """
        self._secrecy_level_name = secrecy_level_name

    @property
    def secrecy_level_number(self):
        r"""Gets the secrecy_level_number of this ShowSecuritySecrecyLevelResponse.

        密级等级

        :return: The secrecy_level_number of this ShowSecuritySecrecyLevelResponse.
        :rtype: int
        """
        return self._secrecy_level_number

    @secrecy_level_number.setter
    def secrecy_level_number(self, secrecy_level_number):
        r"""Sets the secrecy_level_number of this ShowSecuritySecrecyLevelResponse.

        密级等级

        :param secrecy_level_number: The secrecy_level_number of this ShowSecuritySecrecyLevelResponse.
        :type secrecy_level_number: int
        """
        self._secrecy_level_number = secrecy_level_number

    @property
    def description(self):
        r"""Gets the description of this ShowSecuritySecrecyLevelResponse.

        密级描述

        :return: The description of this ShowSecuritySecrecyLevelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowSecuritySecrecyLevelResponse.

        密级描述

        :param description: The description of this ShowSecuritySecrecyLevelResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_by(self):
        r"""Gets the created_by of this ShowSecuritySecrecyLevelResponse.

        创建者

        :return: The created_by of this ShowSecuritySecrecyLevelResponse.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this ShowSecuritySecrecyLevelResponse.

        创建者

        :param created_by: The created_by of this ShowSecuritySecrecyLevelResponse.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowSecuritySecrecyLevelResponse.

        创建时间

        :return: The created_at of this ShowSecuritySecrecyLevelResponse.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowSecuritySecrecyLevelResponse.

        创建时间

        :param created_at: The created_at of this ShowSecuritySecrecyLevelResponse.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_by(self):
        r"""Gets the updated_by of this ShowSecuritySecrecyLevelResponse.

        更新者

        :return: The updated_by of this ShowSecuritySecrecyLevelResponse.
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        r"""Sets the updated_by of this ShowSecuritySecrecyLevelResponse.

        更新者

        :param updated_by: The updated_by of this ShowSecuritySecrecyLevelResponse.
        :type updated_by: str
        """
        self._updated_by = updated_by

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowSecuritySecrecyLevelResponse.

        更新时间

        :return: The updated_at of this ShowSecuritySecrecyLevelResponse.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowSecuritySecrecyLevelResponse.

        更新时间

        :param updated_at: The updated_at of this ShowSecuritySecrecyLevelResponse.
        :type updated_at: int
        """
        self._updated_at = updated_at

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowSecuritySecrecyLevelResponse.

        DataArts实例ID

        :return: The instance_id of this ShowSecuritySecrecyLevelResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowSecuritySecrecyLevelResponse.

        DataArts实例ID

        :param instance_id: The instance_id of this ShowSecuritySecrecyLevelResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, ShowSecuritySecrecyLevelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
