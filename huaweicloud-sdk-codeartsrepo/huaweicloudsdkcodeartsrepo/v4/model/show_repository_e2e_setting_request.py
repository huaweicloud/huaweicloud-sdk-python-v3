# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryE2eSettingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'take_effect': 'bool'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'take_effect': 'take_effect'
    }

    def __init__(self, repository_id=None, take_effect=None):
        r"""ShowRepositoryE2eSettingRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param take_effect: **参数解释：** 是否查询生效的E2E配置。 **取值范围：** true：查询仓库实际生效的E2E配置，比如继承自代码组或者项目的E2E设置，false：查询仓库自身的E2E配置。
        :type take_effect: bool
        """
        
        

        self._repository_id = None
        self._take_effect = None
        self.discriminator = None

        self.repository_id = repository_id
        if take_effect is not None:
            self.take_effect = take_effect

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowRepositoryE2eSettingRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowRepositoryE2eSettingRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowRepositoryE2eSettingRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[[查询用户所有仓库](https://support.huaweicloud.com/eu/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowRepositoryE2eSettingRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def take_effect(self):
        r"""Gets the take_effect of this ShowRepositoryE2eSettingRequest.

        **参数解释：** 是否查询生效的E2E配置。 **取值范围：** true：查询仓库实际生效的E2E配置，比如继承自代码组或者项目的E2E设置，false：查询仓库自身的E2E配置。

        :return: The take_effect of this ShowRepositoryE2eSettingRequest.
        :rtype: bool
        """
        return self._take_effect

    @take_effect.setter
    def take_effect(self, take_effect):
        r"""Sets the take_effect of this ShowRepositoryE2eSettingRequest.

        **参数解释：** 是否查询生效的E2E配置。 **取值范围：** true：查询仓库实际生效的E2E配置，比如继承自代码组或者项目的E2E设置，false：查询仓库自身的E2E配置。

        :param take_effect: The take_effect of this ShowRepositoryE2eSettingRequest.
        :type take_effect: bool
        """
        self._take_effect = take_effect

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
        if not isinstance(other, ShowRepositoryE2eSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
