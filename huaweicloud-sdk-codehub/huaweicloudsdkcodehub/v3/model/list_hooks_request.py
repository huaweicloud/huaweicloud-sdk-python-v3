# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHooksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'hook_id': 'str',
        'repository_name': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'hook_id': 'hook_id',
        'repository_name': 'repository_name'
    }

    def __init__(self, group_name=None, hook_id=None, repository_name=None):
        """ListHooksRequest

        The model defined in huaweicloud sdk

        :param group_name: 组名(克隆地址中域名后面仓库名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )
        :type group_name: str
        :param hook_id: hook id
        :type hook_id: str
        :param repository_name: 仓库名
        :type repository_name: str
        """
        
        

        self._group_name = None
        self._hook_id = None
        self._repository_name = None
        self.discriminator = None

        self.group_name = group_name
        if hook_id is not None:
            self.hook_id = hook_id
        self.repository_name = repository_name

    @property
    def group_name(self):
        """Gets the group_name of this ListHooksRequest.

        组名(克隆地址中域名后面仓库名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )

        :return: The group_name of this ListHooksRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListHooksRequest.

        组名(克隆地址中域名后面仓库名前的一段 示例：git@repo.alpha.devcloud.inhuawei.com:Demo00228/testword.git  组名：Demo00228 )

        :param group_name: The group_name of this ListHooksRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def hook_id(self):
        """Gets the hook_id of this ListHooksRequest.

        hook id

        :return: The hook_id of this ListHooksRequest.
        :rtype: str
        """
        return self._hook_id

    @hook_id.setter
    def hook_id(self, hook_id):
        """Sets the hook_id of this ListHooksRequest.

        hook id

        :param hook_id: The hook_id of this ListHooksRequest.
        :type hook_id: str
        """
        self._hook_id = hook_id

    @property
    def repository_name(self):
        """Gets the repository_name of this ListHooksRequest.

        仓库名

        :return: The repository_name of this ListHooksRequest.
        :rtype: str
        """
        return self._repository_name

    @repository_name.setter
    def repository_name(self, repository_name):
        """Sets the repository_name of this ListHooksRequest.

        仓库名

        :param repository_name: The repository_name of this ListHooksRequest.
        :type repository_name: str
        """
        self._repository_name = repository_name

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
        if not isinstance(other, ListHooksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
