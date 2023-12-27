# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IDERepoRevisionModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_ids': 'str',
        'format': 'str'
    }

    attribute_map = {
        'repository_ids': 'repository_ids',
        'format': 'format'
    }

    def __init__(self, repository_ids=None, format=None):
        """IDERepoRevisionModel

        The model defined in huaweicloud sdk

        :param repository_ids: 仓库id集合
        :type repository_ids: str
        :param format: 类型
        :type format: str
        """
        
        

        self._repository_ids = None
        self._format = None
        self.discriminator = None

        if repository_ids is not None:
            self.repository_ids = repository_ids
        if format is not None:
            self.format = format

    @property
    def repository_ids(self):
        """Gets the repository_ids of this IDERepoRevisionModel.

        仓库id集合

        :return: The repository_ids of this IDERepoRevisionModel.
        :rtype: str
        """
        return self._repository_ids

    @repository_ids.setter
    def repository_ids(self, repository_ids):
        """Sets the repository_ids of this IDERepoRevisionModel.

        仓库id集合

        :param repository_ids: The repository_ids of this IDERepoRevisionModel.
        :type repository_ids: str
        """
        self._repository_ids = repository_ids

    @property
    def format(self):
        """Gets the format of this IDERepoRevisionModel.

        类型

        :return: The format of this IDERepoRevisionModel.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this IDERepoRevisionModel.

        类型

        :param format: The format of this IDERepoRevisionModel.
        :type format: str
        """
        self._format = format

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
        if not isinstance(other, IDERepoRevisionModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
