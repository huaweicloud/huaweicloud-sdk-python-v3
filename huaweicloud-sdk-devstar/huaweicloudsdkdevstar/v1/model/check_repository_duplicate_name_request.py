# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRepositoryDuplicateNameRequest:

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
        'project_id': 'str',
        'name': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'project_id': 'project_id',
        'name': 'name',
        'region_id': 'region_id'
    }

    def __init__(self, x_language=None, project_id=None, name=None, region_id=None):
        r"""CheckRepositoryDuplicateNameRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言类型 中文:zh-cn 英文:en-us
        :type x_language: str
        :param project_id: 项目id
        :type project_id: str
        :param name: 仓库名称
        :type name: str
        :param region_id: 区域id
        :type region_id: str
        """
        
        

        self._x_language = None
        self._project_id = None
        self._name = None
        self._region_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.project_id = project_id
        self.name = name
        self.region_id = region_id

    @property
    def x_language(self):
        r"""Gets the x_language of this CheckRepositoryDuplicateNameRequest.

        语言类型 中文:zh-cn 英文:en-us

        :return: The x_language of this CheckRepositoryDuplicateNameRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this CheckRepositoryDuplicateNameRequest.

        语言类型 中文:zh-cn 英文:en-us

        :param x_language: The x_language of this CheckRepositoryDuplicateNameRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def project_id(self):
        r"""Gets the project_id of this CheckRepositoryDuplicateNameRequest.

        项目id

        :return: The project_id of this CheckRepositoryDuplicateNameRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CheckRepositoryDuplicateNameRequest.

        项目id

        :param project_id: The project_id of this CheckRepositoryDuplicateNameRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this CheckRepositoryDuplicateNameRequest.

        仓库名称

        :return: The name of this CheckRepositoryDuplicateNameRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CheckRepositoryDuplicateNameRequest.

        仓库名称

        :param name: The name of this CheckRepositoryDuplicateNameRequest.
        :type name: str
        """
        self._name = name

    @property
    def region_id(self):
        r"""Gets the region_id of this CheckRepositoryDuplicateNameRequest.

        区域id

        :return: The region_id of this CheckRepositoryDuplicateNameRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this CheckRepositoryDuplicateNameRequest.

        区域id

        :param region_id: The region_id of this CheckRepositoryDuplicateNameRequest.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, CheckRepositoryDuplicateNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
