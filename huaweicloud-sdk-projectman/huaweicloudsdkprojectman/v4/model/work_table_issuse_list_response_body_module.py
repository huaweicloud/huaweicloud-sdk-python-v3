# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkTableIssuseListResponseBodyModule:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'path_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path_name': 'path_name'
    }

    def __init__(self, id=None, name=None, path_name=None):
        r"""WorkTableIssuseListResponseBodyModule

        The model defined in huaweicloud sdk

        :param id: 模块id
        :type id: int
        :param name: 模块名称
        :type name: str
        :param path_name: 模块路径名称
        :type path_name: str
        """
        
        

        self._id = None
        self._name = None
        self._path_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path_name is not None:
            self.path_name = path_name

    @property
    def id(self):
        r"""Gets the id of this WorkTableIssuseListResponseBodyModule.

        模块id

        :return: The id of this WorkTableIssuseListResponseBodyModule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WorkTableIssuseListResponseBodyModule.

        模块id

        :param id: The id of this WorkTableIssuseListResponseBodyModule.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this WorkTableIssuseListResponseBodyModule.

        模块名称

        :return: The name of this WorkTableIssuseListResponseBodyModule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WorkTableIssuseListResponseBodyModule.

        模块名称

        :param name: The name of this WorkTableIssuseListResponseBodyModule.
        :type name: str
        """
        self._name = name

    @property
    def path_name(self):
        r"""Gets the path_name of this WorkTableIssuseListResponseBodyModule.

        模块路径名称

        :return: The path_name of this WorkTableIssuseListResponseBodyModule.
        :rtype: str
        """
        return self._path_name

    @path_name.setter
    def path_name(self, path_name):
        r"""Sets the path_name of this WorkTableIssuseListResponseBodyModule.

        模块路径名称

        :param path_name: The path_name of this WorkTableIssuseListResponseBodyModule.
        :type path_name: str
        """
        self._path_name = path_name

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
        if not isinstance(other, WorkTableIssuseListResponseBodyModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
