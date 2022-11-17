# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoListInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repositorys': 'list[RepoInfo]',
        'total': 'int'
    }

    attribute_map = {
        'repositorys': 'repositorys',
        'total': 'total'
    }

    def __init__(self, repositorys=None, total=None):
        """RepoListInfo

        The model defined in huaweicloud sdk

        :param repositorys: 仓库列表
        :type repositorys: list[:class:`huaweicloudsdkcodehub.v3.RepoInfo`]
        :param total: 仓库总数
        :type total: int
        """
        
        

        self._repositorys = None
        self._total = None
        self.discriminator = None

        if repositorys is not None:
            self.repositorys = repositorys
        if total is not None:
            self.total = total

    @property
    def repositorys(self):
        """Gets the repositorys of this RepoListInfo.

        仓库列表

        :return: The repositorys of this RepoListInfo.
        :rtype: list[:class:`huaweicloudsdkcodehub.v3.RepoInfo`]
        """
        return self._repositorys

    @repositorys.setter
    def repositorys(self, repositorys):
        """Sets the repositorys of this RepoListInfo.

        仓库列表

        :param repositorys: The repositorys of this RepoListInfo.
        :type repositorys: list[:class:`huaweicloudsdkcodehub.v3.RepoInfo`]
        """
        self._repositorys = repositorys

    @property
    def total(self):
        """Gets the total of this RepoListInfo.

        仓库总数

        :return: The total of this RepoListInfo.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RepoListInfo.

        仓库总数

        :param total: The total of this RepoListInfo.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, RepoListInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
