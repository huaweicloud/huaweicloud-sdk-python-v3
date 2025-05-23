# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_need_content': 'bool',
        'eihealth_project_id': 'str',
        'path': 'str'
    }

    attribute_map = {
        'x_need_content': 'X-Need-Content',
        'eihealth_project_id': 'eihealth_project_id',
        'path': 'path'
    }

    def __init__(self, x_need_content=None, eihealth_project_id=None, path=None):
        r"""ShowDataRequest

        The model defined in huaweicloud sdk

        :param x_need_content: 返回文件内容
        :type x_need_content: bool
        :param eihealth_project_id: 平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。
        :type eihealth_project_id: str
        :param path: 对象全路径（项目名称:|路径）
        :type path: str
        """
        
        

        self._x_need_content = None
        self._eihealth_project_id = None
        self._path = None
        self.discriminator = None

        if x_need_content is not None:
            self.x_need_content = x_need_content
        self.eihealth_project_id = eihealth_project_id
        self.path = path

    @property
    def x_need_content(self):
        r"""Gets the x_need_content of this ShowDataRequest.

        返回文件内容

        :return: The x_need_content of this ShowDataRequest.
        :rtype: bool
        """
        return self._x_need_content

    @x_need_content.setter
    def x_need_content(self, x_need_content):
        r"""Sets the x_need_content of this ShowDataRequest.

        返回文件内容

        :param x_need_content: The x_need_content of this ShowDataRequest.
        :type x_need_content: bool
        """
        self._x_need_content = x_need_content

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this ShowDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :return: The eihealth_project_id of this ShowDataRequest.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this ShowDataRequest.

        平台项目ID，您可以在平台单击所需的项目名称，进入项目设置页面查看。

        :param eihealth_project_id: The eihealth_project_id of this ShowDataRequest.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def path(self):
        r"""Gets the path of this ShowDataRequest.

        对象全路径（项目名称:|路径）

        :return: The path of this ShowDataRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowDataRequest.

        对象全路径（项目名称:|路径）

        :param path: The path of this ShowDataRequest.
        :type path: str
        """
        self._path = path

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
        if not isinstance(other, ShowDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
