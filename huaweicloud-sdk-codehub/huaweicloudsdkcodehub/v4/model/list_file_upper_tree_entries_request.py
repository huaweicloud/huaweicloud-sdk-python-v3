# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFileUpperTreeEntriesRequest:

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
        'file_path': 'str',
        'ref_name': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'file_path': 'file_path',
        'ref_name': 'ref_name'
    }

    def __init__(self, repository_id=None, file_path=None, ref_name=None):
        r"""ListFileUpperTreeEntriesRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param file_path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。
        :type file_path: str
        :param ref_name: **参数解释：** 分支或者tag名称。 **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。 **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 仓库默认分支。
        :type ref_name: str
        """
        
        

        self._repository_id = None
        self._file_path = None
        self._ref_name = None
        self.discriminator = None

        self.repository_id = repository_id
        if file_path is not None:
            self.file_path = file_path
        if ref_name is not None:
            self.ref_name = ref_name

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListFileUpperTreeEntriesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListFileUpperTreeEntriesRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListFileUpperTreeEntriesRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListFileUpperTreeEntriesRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def file_path(self):
        r"""Gets the file_path of this ListFileUpperTreeEntriesRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :return: The file_path of this ListFileUpperTreeEntriesRequest.
        :rtype: str
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        r"""Sets the file_path of this ListFileUpperTreeEntriesRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过10000。

        :param file_path: The file_path of this ListFileUpperTreeEntriesRequest.
        :type file_path: str
        """
        self._file_path = file_path

    @property
    def ref_name(self):
        r"""Gets the ref_name of this ListFileUpperTreeEntriesRequest.

        **参数解释：** 分支或者tag名称。 **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。 **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 仓库默认分支。

        :return: The ref_name of this ListFileUpperTreeEntriesRequest.
        :rtype: str
        """
        return self._ref_name

    @ref_name.setter
    def ref_name(self, ref_name):
        r"""Sets the ref_name of this ListFileUpperTreeEntriesRequest.

        **参数解释：** 分支或者tag名称。 **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。 **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 仓库默认分支。

        :param ref_name: The ref_name of this ListFileUpperTreeEntriesRequest.
        :type ref_name: str
        """
        self._ref_name = ref_name

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
        if not isinstance(other, ListFileUpperTreeEntriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
