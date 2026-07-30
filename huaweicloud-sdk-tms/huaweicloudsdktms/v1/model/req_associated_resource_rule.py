# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqAssociatedResourceRule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setting_name': 'str',
        'tag_keys': 'list[str]',
        'existing_resource_status': 'str',
        'auto_delete_status': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'setting_name': 'setting_name',
        'tag_keys': 'tag_keys',
        'existing_resource_status': 'existing_resource_status',
        'auto_delete_status': 'auto_delete_status',
        'region_id': 'region_id'
    }

    def __init__(self, setting_name=None, tag_keys=None, existing_resource_status=None, auto_delete_status=None, region_id=None):
        r"""ReqAssociatedResourceRule

        The model defined in huaweicloud sdk

        :param setting_name: 规则配置名称
        :type setting_name: str
        :param tag_keys: 标签键列表
        :type tag_keys: list[str]
        :param existing_resource_status: 存量资源生效状态：enable、disable
        :type existing_resource_status: str
        :param auto_delete_status: 关系解除后自动删除能力状态：enable、disable
        :type auto_delete_status: str
        :param region_id: 规则生效的regionId
        :type region_id: str
        """
        
        

        self._setting_name = None
        self._tag_keys = None
        self._existing_resource_status = None
        self._auto_delete_status = None
        self._region_id = None
        self.discriminator = None

        self.setting_name = setting_name
        if tag_keys is not None:
            self.tag_keys = tag_keys
        if existing_resource_status is not None:
            self.existing_resource_status = existing_resource_status
        if auto_delete_status is not None:
            self.auto_delete_status = auto_delete_status
        self.region_id = region_id

    @property
    def setting_name(self):
        r"""Gets the setting_name of this ReqAssociatedResourceRule.

        规则配置名称

        :return: The setting_name of this ReqAssociatedResourceRule.
        :rtype: str
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self, setting_name):
        r"""Sets the setting_name of this ReqAssociatedResourceRule.

        规则配置名称

        :param setting_name: The setting_name of this ReqAssociatedResourceRule.
        :type setting_name: str
        """
        self._setting_name = setting_name

    @property
    def tag_keys(self):
        r"""Gets the tag_keys of this ReqAssociatedResourceRule.

        标签键列表

        :return: The tag_keys of this ReqAssociatedResourceRule.
        :rtype: list[str]
        """
        return self._tag_keys

    @tag_keys.setter
    def tag_keys(self, tag_keys):
        r"""Sets the tag_keys of this ReqAssociatedResourceRule.

        标签键列表

        :param tag_keys: The tag_keys of this ReqAssociatedResourceRule.
        :type tag_keys: list[str]
        """
        self._tag_keys = tag_keys

    @property
    def existing_resource_status(self):
        r"""Gets the existing_resource_status of this ReqAssociatedResourceRule.

        存量资源生效状态：enable、disable

        :return: The existing_resource_status of this ReqAssociatedResourceRule.
        :rtype: str
        """
        return self._existing_resource_status

    @existing_resource_status.setter
    def existing_resource_status(self, existing_resource_status):
        r"""Sets the existing_resource_status of this ReqAssociatedResourceRule.

        存量资源生效状态：enable、disable

        :param existing_resource_status: The existing_resource_status of this ReqAssociatedResourceRule.
        :type existing_resource_status: str
        """
        self._existing_resource_status = existing_resource_status

    @property
    def auto_delete_status(self):
        r"""Gets the auto_delete_status of this ReqAssociatedResourceRule.

        关系解除后自动删除能力状态：enable、disable

        :return: The auto_delete_status of this ReqAssociatedResourceRule.
        :rtype: str
        """
        return self._auto_delete_status

    @auto_delete_status.setter
    def auto_delete_status(self, auto_delete_status):
        r"""Sets the auto_delete_status of this ReqAssociatedResourceRule.

        关系解除后自动删除能力状态：enable、disable

        :param auto_delete_status: The auto_delete_status of this ReqAssociatedResourceRule.
        :type auto_delete_status: str
        """
        self._auto_delete_status = auto_delete_status

    @property
    def region_id(self):
        r"""Gets the region_id of this ReqAssociatedResourceRule.

        规则生效的regionId

        :return: The region_id of this ReqAssociatedResourceRule.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ReqAssociatedResourceRule.

        规则生效的regionId

        :param region_id: The region_id of this ReqAssociatedResourceRule.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, ReqAssociatedResourceRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
