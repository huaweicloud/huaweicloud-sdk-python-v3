# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'eihealth_project_id': 'str',
        'name': 'str',
        'show_empty': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'eihealth_project_id': 'eihealth_project_id',
        'name': 'name',
        'show_empty': 'show_empty'
    }

    def __init__(self, type=None, eihealth_project_id=None, name=None, show_empty=None):
        """ListImageRequest

        The model defined in huaweicloud sdk

        :param type: 镜像类型
        :type type: str
        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param name: 镜像名称
        :type name: str
        :param show_empty: 是否展示无镜像版本的镜像
        :type show_empty: bool
        """
        
        

        self._type = None
        self._eihealth_project_id = None
        self._name = None
        self._show_empty = None
        self.discriminator = None

        if type is not None:
            self.type = type
        self.eihealth_project_id = eihealth_project_id
        if name is not None:
            self.name = name
        if show_empty is not None:
            self.show_empty = show_empty

    @property
    def type(self):
        """Gets the type of this ListImageRequest.

        镜像类型

        :return: The type of this ListImageRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListImageRequest.

        镜像类型

        :param type: The type of this ListImageRequest.
        :type type: str
        """
        self._type = type

    @property
    def eihealth_project_id(self):
        """Gets the eihealth_project_id of this ListImageRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ListImageRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        """Sets the eihealth_project_id of this ListImageRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ListImageRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def name(self):
        """Gets the name of this ListImageRequest.

        镜像名称

        :return: The name of this ListImageRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListImageRequest.

        镜像名称

        :param name: The name of this ListImageRequest.
        :type name: str
        """
        self._name = name

    @property
    def show_empty(self):
        """Gets the show_empty of this ListImageRequest.

        是否展示无镜像版本的镜像

        :return: The show_empty of this ListImageRequest.
        :rtype: bool
        """
        return self._show_empty

    @show_empty.setter
    def show_empty(self, show_empty):
        """Sets the show_empty of this ListImageRequest.

        是否展示无镜像版本的镜像

        :param show_empty: The show_empty of this ListImageRequest.
        :type show_empty: bool
        """
        self._show_empty = show_empty

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
        if not isinstance(other, ListImageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
