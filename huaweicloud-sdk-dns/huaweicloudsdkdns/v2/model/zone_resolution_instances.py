# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ZoneResolutionInstances:

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
        'name': 'str',
        'status': 'str',
        'region': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, id=None, name=None, status=None, region=None, enterprise_project_id=None):
        r"""ZoneResolutionInstances

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 域名ID。 **取值范围：** 不涉及。
        :type id: str
        :param name: **参数解释：** 域名。 **取值范围：** 不涉及。
        :type name: str
        :param status: **参数解释：** 域名状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败
        :type status: str
        :param region: **参数解释：** 域名所属的区域。 **取值范围：** 不涉及。
        :type region: str
        :param enterprise_project_id: **参数解释：** 企业项目ID。 **取值范围：** 不涉及。
        :type enterprise_project_id: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._region = None
        self._enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ZoneResolutionInstances.

        **参数解释：** 域名ID。 **取值范围：** 不涉及。

        :return: The id of this ZoneResolutionInstances.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ZoneResolutionInstances.

        **参数解释：** 域名ID。 **取值范围：** 不涉及。

        :param id: The id of this ZoneResolutionInstances.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ZoneResolutionInstances.

        **参数解释：** 域名。 **取值范围：** 不涉及。

        :return: The name of this ZoneResolutionInstances.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ZoneResolutionInstances.

        **参数解释：** 域名。 **取值范围：** 不涉及。

        :param name: The name of this ZoneResolutionInstances.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ZoneResolutionInstances.

        **参数解释：** 域名状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败

        :return: The status of this ZoneResolutionInstances.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ZoneResolutionInstances.

        **参数解释：** 域名状态。 **取值范围：** - ACTIVE：正常 - PENDING_CREATE：创建中 - PENDING_UPDATE：更新中 - PENDING_DELETE：删除中 - PENDING_FREEZE：冻结中 - FREEZE：冻结 - ILLEGAL：违规冻结 - POLICE：公安冻结 - PENDING_DISABLE：暂停中 - DISABLE：暂停 - ERROR：失败

        :param status: The status of this ZoneResolutionInstances.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        r"""Gets the region of this ZoneResolutionInstances.

        **参数解释：** 域名所属的区域。 **取值范围：** 不涉及。

        :return: The region of this ZoneResolutionInstances.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ZoneResolutionInstances.

        **参数解释：** 域名所属的区域。 **取值范围：** 不涉及。

        :param region: The region of this ZoneResolutionInstances.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ZoneResolutionInstances.

        **参数解释：** 企业项目ID。 **取值范围：** 不涉及。

        :return: The enterprise_project_id of this ZoneResolutionInstances.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ZoneResolutionInstances.

        **参数解释：** 企业项目ID。 **取值范围：** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this ZoneResolutionInstances.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ZoneResolutionInstances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
