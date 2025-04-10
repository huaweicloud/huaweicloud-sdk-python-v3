# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryStatisticalDataV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'repository_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'repository_id': 'repository_id'
    }

    def __init__(self, x_language=None, repository_id=None):
        r"""ShowRepositoryStatisticalDataV2Request

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us
        :type x_language: str
        :param repository_id: 代码仓库id
        :type repository_id: str
        """
        
        

        self._x_language = None
        self._repository_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.repository_id = repository_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowRepositoryStatisticalDataV2Request.

        语言类型 中文:zh-cn 英文:en-us

        :return: The x_language of this ShowRepositoryStatisticalDataV2Request.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowRepositoryStatisticalDataV2Request.

        语言类型 中文:zh-cn 英文:en-us

        :param x_language: The x_language of this ShowRepositoryStatisticalDataV2Request.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowRepositoryStatisticalDataV2Request.

        代码仓库id

        :return: The repository_id of this ShowRepositoryStatisticalDataV2Request.
        :rtype: str
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowRepositoryStatisticalDataV2Request.

        代码仓库id

        :param repository_id: The repository_id of this ShowRepositoryStatisticalDataV2Request.
        :type repository_id: str
        """
        self._repository_id = repository_id

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
        if not isinstance(other, ShowRepositoryStatisticalDataV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
