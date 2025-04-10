# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleIssueVo:

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
        'path': 'str',
        'tracker_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'tracker_name': 'tracker_name'
    }

    def __init__(self, id=None, name=None, path=None, tracker_name=None):
        r"""SimpleIssueVo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param name: 名称
        :type name: str
        :param path: 层级路径
        :type path: str
        :param tracker_name: 类型
        :type tracker_name: str
        """
        
        

        self._id = None
        self._name = None
        self._path = None
        self._tracker_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if tracker_name is not None:
            self.tracker_name = tracker_name

    @property
    def id(self):
        r"""Gets the id of this SimpleIssueVo.

        ID

        :return: The id of this SimpleIssueVo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SimpleIssueVo.

        ID

        :param id: The id of this SimpleIssueVo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SimpleIssueVo.

        名称

        :return: The name of this SimpleIssueVo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SimpleIssueVo.

        名称

        :param name: The name of this SimpleIssueVo.
        :type name: str
        """
        self._name = name

    @property
    def path(self):
        r"""Gets the path of this SimpleIssueVo.

        层级路径

        :return: The path of this SimpleIssueVo.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this SimpleIssueVo.

        层级路径

        :param path: The path of this SimpleIssueVo.
        :type path: str
        """
        self._path = path

    @property
    def tracker_name(self):
        r"""Gets the tracker_name of this SimpleIssueVo.

        类型

        :return: The tracker_name of this SimpleIssueVo.
        :rtype: str
        """
        return self._tracker_name

    @tracker_name.setter
    def tracker_name(self, tracker_name):
        r"""Sets the tracker_name of this SimpleIssueVo.

        类型

        :param tracker_name: The tracker_name of this SimpleIssueVo.
        :type tracker_name: str
        """
        self._tracker_name = tracker_name

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
        if not isinstance(other, SimpleIssueVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
