# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProtectedBranchRequest:

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
        'branch_name': 'str',
        'body': 'list[ProtectedBranchProtectedActionBodyDto]'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'branch_name': 'branch_name',
        'body': 'body'
    }

    def __init__(self, repository_id=None, branch_name=None, body=None):
        r"""UpdateProtectedBranchRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param branch_name: **参数解释：** 保护分支名或通配符表达式。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type branch_name: str
        :param body: 保护分支权限列表
        :type body: list[:class:`huaweicloudsdkcodehub.v4.ProtectedBranchProtectedActionBodyDto`]
        """
        
        

        self._repository_id = None
        self._branch_name = None
        self._body = None
        self.discriminator = None

        self.repository_id = repository_id
        self.branch_name = branch_name
        if body is not None:
            self.body = body

    @property
    def repository_id(self):
        r"""Gets the repository_id of this UpdateProtectedBranchRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this UpdateProtectedBranchRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this UpdateProtectedBranchRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this UpdateProtectedBranchRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def branch_name(self):
        r"""Gets the branch_name of this UpdateProtectedBranchRequest.

        **参数解释：** 保护分支名或通配符表达式。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The branch_name of this UpdateProtectedBranchRequest.
        :rtype: str
        """
        return self._branch_name

    @branch_name.setter
    def branch_name(self, branch_name):
        r"""Sets the branch_name of this UpdateProtectedBranchRequest.

        **参数解释：** 保护分支名或通配符表达式。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param branch_name: The branch_name of this UpdateProtectedBranchRequest.
        :type branch_name: str
        """
        self._branch_name = branch_name

    @property
    def body(self):
        r"""Gets the body of this UpdateProtectedBranchRequest.

        保护分支权限列表

        :return: The body of this UpdateProtectedBranchRequest.
        :rtype: list[:class:`huaweicloudsdkcodehub.v4.ProtectedBranchProtectedActionBodyDto`]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateProtectedBranchRequest.

        保护分支权限列表

        :param body: The body of this UpdateProtectedBranchRequest.
        :type body: list[:class:`huaweicloudsdkcodehub.v4.ProtectedBranchProtectedActionBodyDto`]
        """
        self._body = body

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
        if not isinstance(other, UpdateProtectedBranchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
